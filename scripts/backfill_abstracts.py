#!/usr/bin/env python3
"""Scan published posts for missing abstracts and backfill from S2/OpenAlex.

Papers whose abstracts are successfully filled (or confirmed permanently
unavailable) are recorded in data/abstract_backfill.json so they won't be
re-queried on subsequent runs.

Usage:
    python scripts/backfill_abstracts.py              # dry-run (show what would change)
    python scripts/backfill_abstracts.py --apply       # actually write changes to files
"""

import argparse
import json
import os
import re
import sys
import time
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

# ── Paths ──────────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent.parent
PAGES_DIR = REPO_ROOT / "_pages"
TRACKING_FILE = REPO_ROOT / "data" / "abstract_backfill.json"

# ── API clients (minimal, reusing the same logic as harvest.py) ───────────

S2_BASE = "https://api.semanticscholar.org/graph/v1/paper"
OA_BASE = "https://api.openalex.org"
S2_API_KEY = os.getenv("SEMANTIC_SCHOLAR_API_KEY", "")
S2_DELAY = 1.5   # seconds between S2 requests
OA_DELAY = 0.1

session = requests.Session()
session.headers.update({"User-Agent": "HydroSense/2.0 (abstract-backfill)"})
if S2_API_KEY:
    session.headers.update({"x-api-key": S2_API_KEY})


def clean_abstract(text: str) -> str:
    """Strip JATS XML tags and stray markup."""
    text = re.sub(r"</?jats:[^>]+>", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    return text.strip()


def fetch_abstract_s2(doi: str) -> str:
    """Try Semantic Scholar graph API."""
    try:
        r = session.get(
            f"{S2_BASE}/DOI:{doi}",
            params={"fields": "abstract"},
            timeout=15,
        )
        time.sleep(S2_DELAY)
        if r.status_code == 200:
            abstract = r.json().get("abstract", "")
            return clean_abstract(abstract) if abstract else ""
        if r.status_code == 429:
            print("  ⚠ S2 rate-limited, waiting 5 s …", file=sys.stderr)
            time.sleep(5)
    except Exception as e:
        print(f"  ⚠ S2 error: {e}", file=sys.stderr)
    return ""


def fetch_abstract_openalex(doi: str) -> str:
    """Try OpenAlex inverted-index abstract."""
    try:
        r = session.get(f"{OA_BASE}/works/doi:{doi}", timeout=15)
        time.sleep(OA_DELAY)
        if r.status_code == 200:
            inv = r.json().get("abstract_inverted_index")
            if inv:
                words = [""] * 1000
                for word, positions in inv.items():
                    for pos in positions:
                        if pos < len(words):
                            words[pos] = word
                return " ".join(w for w in words if w)
    except Exception as e:
        print(f"  ⚠ OpenAlex error: {e}", file=sys.stderr)
    return ""


# Meta-tag patterns for publisher landing pages.
# Publishers embed the abstract in standardized <meta> tags — Nature uses
# dc.description, many others use og:description or citation_abstract.
# Both attribute orders (name/content vs content/name) must be matched.
_META_PATTERNS = [
    # <meta name="dc.description" content="...">
    (r'<meta[^>]+name=["\']dc\.description["\'][^>]+content=["\']([^"\']{50,})["\']', re.IGNORECASE),
    (r'<meta[^>]+content=["\']([^"\']{50,})["\'][^>]+name=["\']dc\.description["\']', re.IGNORECASE),
    # <meta name="citation_abstract" content="...">
    (r'<meta[^>]+name=["\']citation_abstract["\'][^>]+content=["\']([^"\']{50,})["\']', re.IGNORECASE),
    (r'<meta[^>]+content=["\']([^"\']{50,})["\'][^>]+name=["\']citation_abstract["\']', re.IGNORECASE),
    # <meta property="og:description" content="...">  (often truncated, so last resort)
    (r'<meta[^>]+property=["\']og:description["\'][^>]+content=["\']([^"\']{80,})["\']', re.IGNORECASE),
    (r'<meta[^>]+content=["\']([^"\']{80,})["\'][^>]+property=["\']og:description["\']', re.IGNORECASE),
]

PUBLISHER_DELAY = 0.5  # be polite to publisher sites


def fetch_abstract_publisher(doi: str) -> str:
    """Fetch abstract from the DOI landing page via <meta> tags.

    This is the most reliable source for very recent papers that haven't
    been indexed by S2 or OpenAlex yet — the publisher page has the
    abstract from day one.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; HydroSense/2.0; +https://hydrosense.simhydro.com)",
            "Accept": "text/html,application/xhtml+xml",
        }
        r = requests.get(
            f"https://doi.org/{doi}",
            headers=headers,
            timeout=15,
            allow_redirects=True,
        )
        time.sleep(PUBLISHER_DELAY)
        if r.status_code != 200:
            return ""
        # Scan a generous chunk — some publishers place meta tags deep in the HTML.
        html = r.text[:250_000]
        for pattern, flags in _META_PATTERNS:
            m = re.search(pattern, html, flags)
            if m:
                abstract = m.group(1).strip()
                # Decode common HTML entities
                abstract = (
                    abstract
                    .replace("&amp;", "&")
                    .replace("&lt;", "<")
                    .replace("&gt;", ">")
                    .replace("&#x27;", "'")
                    .replace("&quot;", '"')
                    .replace("&#39;", "'")
                )
                abstract = clean_abstract(abstract)
                if len(abstract) > 50:  # reject tiny marketing blurbs
                    return abstract
    except Exception as e:
        print(f"  ⚠ Publisher page error: {e}", file=sys.stderr)
    return ""


# ── Tracking file ─────────────────────────────────────────────────────────

def load_tracking() -> dict:
    if TRACKING_FILE.exists():
        return json.loads(TRACKING_FILE.read_text())
    return {}


def save_tracking(data: dict):
    TRACKING_FILE.parent.mkdir(parents=True, exist_ok=True)
    TRACKING_FILE.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n")


# ── Scanning and patching ─────────────────────────────────────────────────

# Matches "> Abstract not available." (English) and common Chinese variants.
MISSING_RE = re.compile(
    r"^> (?:Abstract not available\.?|摘要暂缺。?|摘要未提供。?|摘要暂无。?)$",
    re.MULTILINE,
)

# Extracts DOI from a line like:
#   **DOI**: [10.xxxx/...](https://doi.org/10.xxxx/...)
DOI_RE = re.compile(r"\*\*DOI\*\*:\s*\[([^\]]+)\]\(https://doi\.org/[^)]+\)")


def find_missing_abstracts(root: Path) -> list[dict]:
    """Return a list of {file, doi, line} for every missing abstract."""
    results = []
    for md in sorted(root.rglob("*.md")):
        text = md.read_text()
        for m in MISSING_RE.finditer(text):
            # Walk backwards from the match to find the DOI line.
            before = text[: m.start()]
            doi_match = None
            for dm in DOI_RE.finditer(before):
                doi_match = dm  # keep the last (nearest) one
            if doi_match:
                results.append({
                    "file": md,
                    "doi": doi_match.group(1),
                    "placeholder": m.group(0),
                })
    return results


def patch_file(filepath: Path, doi: str, abstract: str) -> bool:
    """Replace the missing-abstract placeholder for this DOI in the file.

    Returns True if a replacement was made.
    """
    text = filepath.read_text()

    # Find the specific placeholder that belongs to this DOI
    # by locating the DOI line first, then the next placeholder after it.
    doi_positions = [m.start() for m in DOI_RE.finditer(text) if m.group(1) == doi]
    if not doi_positions:
        return False

    for doi_pos in doi_positions:
        after_doi = text[doi_pos:]
        placeholder_match = MISSING_RE.search(after_doi)
        if placeholder_match:
            abs_start = doi_pos + placeholder_match.start()
            abs_end = doi_pos + placeholder_match.end()
            new = f"> {abstract}"
            text = text[:abs_start] + new + text[abs_end:]
            filepath.write_text(text)
            return True
    return False


# ── Main ──────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Backfill missing abstracts in posts")
    parser.add_argument("--apply", action="store_true", help="Write changes to disk (default is dry-run)")
    args = parser.parse_args()

    tracking = load_tracking()
    missing = find_missing_abstracts(PAGES_DIR)

    # Deduplicate by DOI (same DOI can appear in en + zh, but we fetch once).
    # Also filter out zh files — we patch them from the en pass.
    en_missing = []
    seen_dois = set()
    for entry in missing:
        rel = entry["file"].relative_to(PAGES_DIR)
        if rel.parts[0] == "zh":
            continue  # handled when we patch the en file
        if entry["doi"] in seen_dois:
            continue
        seen_dois.add(entry["doi"])
        en_missing.append(entry)

    # Filter out DOIs already marked "completed" (abstract was filled).
    # Always retry "unavailable" ones — the abstract may have been indexed since.
    to_fetch = [e for e in en_missing if tracking.get(e["doi"], {}).get("status") != "completed"]

    print(f"Found {len(en_missing)} English papers with missing abstracts")
    print(f"  Already tracked (completed/unavailable): {len(en_missing) - len(to_fetch)}")
    print(f"  To fetch: {len(to_fetch)}")
    print()

    filled = 0
    unavailable = 0

    for entry in to_fetch:
        doi = entry["doi"]
        print(f"  [{doi}]")

        # Try S2 first, then OpenAlex, then the publisher landing page.
        abstract = fetch_abstract_s2(doi)
        source = "S2"
        if not abstract:
            abstract = fetch_abstract_openalex(doi)
            source = "OpenAlex"
        if not abstract:
            abstract = fetch_abstract_publisher(doi)
            source = "Publisher"

        if abstract:
            print(f"    ✓ Found via {source} ({len(abstract)} chars)")
            if args.apply:
                patched = patch_file(entry["file"], doi, abstract)
                if patched:
                    print(f"    ✓ Patched {entry['file'].relative_to(REPO_ROOT)}")
                tracking[doi] = {"status": "completed", "source": source, "length": len(abstract)}
            else:
                print(f"    (dry-run, use --apply to write)")
            filled += 1
        else:
            print(f"    ✗ Not available in S2, OpenAlex, or publisher page")
            if args.apply:
                tracking[doi] = {"status": "unavailable"}
            unavailable += 1

    print()
    print(f"Results: {filled} filled, {unavailable} still unavailable")

    if args.apply:
        save_tracking(tracking)
        print(f"Tracking saved to {TRACKING_FILE.relative_to(REPO_ROOT)}")
    elif filled > 0:
        print()
        print("Run with --apply to write changes to files.")


if __name__ == "__main__":
    main()

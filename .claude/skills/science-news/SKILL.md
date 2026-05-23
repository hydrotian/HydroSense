---
name: science-news
description: Curate AI-for-science news from RSS feeds (Nature, Science, Ars Technica, MIT Tech Review, Quanta, DeepMind, OpenAI). Filter for relevance to earth-science research, dedup across sources, and produce a short markdown fragment that the daily-harvest skill injects into the daily post. Use when running the daily science-news curation, or standalone for testing.
allowed-tools: [Bash, Read, Write, Edit]
---

# AI-for-Science News Curation

Produce a short "AI for Science" markdown fragment for the daily-harvest post by filtering RSS items from curated science-news sources. Output is two-bucket, strictly curated, and may be empty (in which case daily-harvest omits the section entirely).

## Goals

Capture two distinct signals:

1. **How AI is changing research** — methods, tools, workflows, agentic systems, hypothesis generation, software co-development, "AI scientist" style work. Stay current on the *practice* of AI-assisted science.
2. **Cross-discipline sparks** — items (often *not* AI-themed themselves) that hint at earth-science project ideas now newly tractable because AI dissolves prior barriers: missing domain expertise, missing engineering capacity, missing team scale. The LLM's job here is to surface the connection: "what about this could a small earth-science team plausibly do now that they couldn't pre-AI?"

The bar is high. Most days will yield 0-3 items total. Some days yield nothing. Skipping is the correct default.

## Workflow

### Step 1: Fetch raw candidates

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python scripts/fetch_science_news.py --days-back 2 > /tmp/science_news_raw.json 2>/tmp/science_news_log.txt
```

A 2-day window covers the gap if the daily run was skipped a day. The state file (Step 2) prevents re-considering yesterday's items.

If you're testing a longer window or specific sources:

```bash
python scripts/fetch_science_news.py --days-back 7 --sources nature,nature-ml,science-news > /tmp/science_news_raw.json
```

### Step 2: Filter against state file

Read `data/science_news_seen.json` (create with `{"seen": {}}` if missing). For each raw item, drop it if its `id` is already in `seen`. The state file holds both `kept` and `rejected` decisions — both count as "already considered, skip."

```python
# Conceptual logic; do this inline in the skill, no separate script needed.
import json
from pathlib import Path

state_path = Path("data/science_news_seen.json")
state = json.loads(state_path.read_text()) if state_path.exists() else {"seen": {}}
raw = json.loads(Path("/tmp/science_news_raw.json").read_text())
candidates = [i for i in raw["items"] if i["id"] not in state["seen"]]
```

### Step 3: LLM filter, dedup, bucket

Apply judgment in one pass. For each candidate item, decide:

**(a) Relevance** — does it belong in either bucket? Drop if not.

- **Bucket "ai-method"**: the item is about AI changing how research is done. Includes: foundation models for science, agentic research workflows, automated hypothesis generation, AI lab automation, AI-driven software development for science. Excludes: pure product announcements ("X Inc launches new chatbot"), industry partnerships without research substance, leadership/funding/Gartner-quadrant news.
- **Bucket "cross-discipline"**: the item describes a result, technique, or capability in *another* field (biology, chemistry, materials, physics, math) where the LLM can articulate a concrete earth-science angle — what could be tried now in hydrology / land-surface / climate / remote sensing that wouldn't have been feasible pre-AI. The connection must be specific, not "AI is general so this could be useful." If you can't write a concrete sentence about the earth-science application, drop it.
- **Drop**: anything that doesn't fit either bucket. Drop generously. When in doubt, drop.

**(b) Dedup** — across the surviving items, group ones covering the same underlying story (e.g., Quanta and Ars Technica both write up the same Nature paper). Pick the canonical source per group: prefer original (Nature/Science) > Quanta/MIT TR (deeper takes) > Ars/lab blogs (coverage). Drop the duplicates.

**(c) Edit** — for the cross-discipline bucket especially, write a real sentence (or short paragraph) that does the cross-domain translation. This is where the value is. Don't just summarize the source — connect it to earth science.

Expected output: 0-3 items per bucket, ~0-5 items total per day. If both buckets are empty, write an empty fragment file (Step 4) and stop.

### Step 4: Write the markdown fragment

Write to `/tmp/science_news_fragment.md`. The daily-harvest skill reads this and injects it into the daily post if non-empty.

Format:

```markdown
## AI for Science

### How AI is changing research

- **[Title](url)** (Source, YYYY-MM-DD) — One-sentence why-this-matters. Optionally a follow-up paragraph if there's genuine commentary worth adding.

### Cross-discipline sparks

- **[Title](url)** (Source, YYYY-MM-DD) — Cross-domain translation: what about this becomes tractable for an earth-science researcher / small team now? Be specific about the connection.
```

Omit a `###` subsection entirely if its bucket is empty. If both buckets are empty, write the file but make it empty (zero bytes) so daily-harvest knows there's nothing to inject.

### Step 5: Update state file

For *every* candidate considered in Step 3 (both kept and dropped), append to `data/science_news_seen.json`. Use this exact snippet — the only thing you fill in is `KEPT`, a dict mapping **item `id` (not url)** to bucket name. Everything else gets `decision="rejected"`, `bucket=None`.

**Why `id` not `url`:** some RSS feeds (MIT Tech Review, Quanta, sometimes OpenAI) use opaque IDs like `https://www.technologyreview.com/?p=1137813` as the canonical `id` while exposing a different friendly URL. The state file is keyed by `id` so we must match on `id`. Lookups by URL silently miss these items and mis-record them as rejected.

```python
import json
from datetime import date
from pathlib import Path

# Fill in: LLM-kept items as { item_id: bucket_name }
# Read item_id from the "id" field of each candidate (NOT the "url" field).
KEPT = {
    "https://www.nature.com/articles/d41586-026-01651-0": "ai-method",
    "https://www.technologyreview.com/?p=1137813":         "ai-method",
    # ...
}

raw = json.loads(Path("/tmp/science_news_raw.json").read_text())
state_path = Path("data/science_news_seen.json")
state = json.loads(state_path.read_text()) if state_path.exists() else {"seen": {}}
today = date.today().isoformat()

# Sanity check: every KEPT id must exist in the raw items.
raw_ids = {i["id"] for i in raw["items"]}
unknown = set(KEPT) - raw_ids
if unknown:
    raise SystemExit(f"KEPT contains ids not in raw items (probably you used url, not id): {unknown}")

for item in raw["items"]:
    if item["id"] in state["seen"]:
        continue  # already considered on a previous run
    bucket = KEPT.get(item["id"])
    state["seen"][item["id"]] = {
        "first_seen": today,
        "url": item["url"],
        "decision": "kept" if bucket else "rejected",
        "bucket": bucket,
    }

state_path.write_text(json.dumps(state, indent=2, ensure_ascii=False) + "\n")
kept_n = sum(1 for v in state["seen"].values() if v["decision"] == "kept")
print(f"State updated: {len(state['seen'])} total, {kept_n} kept, {len(state['seen'])-kept_n} rejected")
```

Keep entries forever — the file stays small (a few KB per year). Don't prune.

### Step 6: Flag editorial items for DOI extraction

For items in the kept set whose `source_type` is `editorial` (Nature, Science Magazine), write their URLs to `/tmp/science_news_doi_candidates.json`:

```json
{"urls": ["https://www.nature.com/articles/d41586-...", ...]}
```

This is consumed by the DOI-extraction step (added in a follow-up chunk). For now, just write the file; downstream consumers can ignore it if empty.

## Standalone Testing

```bash
/science-news
```

Runs the full workflow with `--days-back 2`. Check:
- `/tmp/science_news_raw.json` — what was fetched
- `/tmp/science_news_fragment.md` — final output (may be empty)
- `/tmp/science_news_doi_candidates.json` — editorial DOIs to extract later
- `data/science_news_seen.json` — state has been updated

To re-run on the same items (e.g., to test prompt changes), delete the relevant entries from `data/science_news_seen.json` first.

## Selection Examples

**Keep (ai-method):** "Anthropic's Claude Opus shipped a new agentic research workflow." Why: methodology shift directly relevant to AI-assisted research.

**Keep (cross-discipline):** A Nature paper on AlphaFold-style structure prediction for materials science. Cross-domain note: "The same masked-pretraining recipe could plausibly be applied to remote-sensing time series — pretrain on raw MODIS/Sentinel reflectance, fine-tune for hydrologic state estimation. The barrier was always architecture + compute; with off-the-shelf foundation-model recipes, a 1-2 person team could attempt it."

**Drop:** "OpenAI named leader in Gartner Magic Quadrant." Why: industry PR, no research substance.

**Drop:** "AI helps doctors triage patients faster." Why: cross-discipline (medical), but the LLM can't articulate a specific earth-science adaptation beyond "AI is helpful" — fails the specificity test.

**Drop (dedup):** Ars Technica covers a Nature paper that Nature itself also published a news-feature about. Keep the Nature one (canonical), drop Ars.

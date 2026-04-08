#!/usr/bin/env python3
"""
Paper Harvester for HydroSense

Fetches papers from tracked journals and classifies them using deterministic filters:
  - Keyword matching against TOPICS in title/abstract
  - Semantic Scholar field classification against RELEVANT_FIELDS
  - Peer-review status verification (journal-article type)

Supports two output formats:
  - json: Structured JSON to stdout (for Claude scheduled triggers)
  - markdown: Jekyll post saved to _pages/YYYY/monthname/YYYY-MM-DD-daily-harvest.md

Usage:
    python harvest.py                                    # Default: last 30 days, top-tier only
    python harvest.py --date 2026-01-13                  # Specific date
    python harvest.py --journals all                     # All journals
    python harvest.py --output-format json               # JSON output for Claude
    python harvest.py --backfill                         # Next backfill month
    python harvest.py --backfill --backfill-start 2015-01-01  # Backfill from 2015
"""

import argparse
import json
import logging
import os
import re
import requests
import time
from calendar import monthrange
from datetime import datetime, timedelta
from typing import List, Dict, Optional

from dotenv import load_dotenv
load_dotenv()

# API Keys (from environment variables)
SEMANTIC_SCHOLAR_API_KEY = os.getenv('SEMANTIC_SCHOLAR_API_KEY')
CROSSREF_EMAIL = os.getenv('CROSSREF_EMAIL')

# Setup logging (stderr so it doesn't pollute JSON stdout)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Backfill counter file
BACKFILL_COUNTER_FILE = os.path.join(os.path.dirname(__file__), '.backfill_counter')
BACKFILL_START_DATE = datetime(2020, 1, 1)


def _read_backfill_months_offset() -> int:
    """Read the backfill counter (months offset) from file.

    Returns 0 if the file does not exist, is empty, or contains invalid data.
    """
    if not os.path.exists(BACKFILL_COUNTER_FILE):
        return 0

    with open(BACKFILL_COUNTER_FILE, 'r') as f:
        raw_value = f.read().strip()

    if not raw_value:
        return 0

    try:
        return int(raw_value)
    except ValueError:
        logger.warning(
            "Backfill counter file '%s' contains invalid data '%s'; resetting to 0",
            BACKFILL_COUNTER_FILE,
            raw_value,
        )
        return 0


def get_next_backfill_month(start_date: datetime = None):
    """Get the next backfill month range from counter file.

    Returns (from_str, until_str, months_offset) where the date range covers one full month.
    """
    start = start_date or BACKFILL_START_DATE
    months_offset = _read_backfill_months_offset()

    # Calculate target month
    year = start.year + (start.month - 1 + months_offset) // 12
    month = (start.month - 1 + months_offset) % 12 + 1

    from_str = f"{year:04d}-{month:02d}-01"
    last_day = monthrange(year, month)[1]
    until_str = f"{year:04d}-{month:02d}-{last_day:02d}"

    return from_str, until_str, months_offset


def increment_backfill_counter():
    """Increment the backfill counter after successful harvest."""
    months_offset = _read_backfill_months_offset()

    with open(BACKFILL_COUNTER_FILE, 'w') as f:
        f.write(str(months_offset + 1))

    logger.info(f"Backfill counter incremented to {months_offset + 1}")


# Tracked journals
JOURNALS = [
    {"name": "Nature", "issn": "1476-4687", "category": "top-tier"},
    {"name": "Science", "issn": "1095-9203", "category": "top-tier"},
    {"name": "Proceedings of the National Academy of Sciences", "issn": "1091-6490", "category": "top-tier"},
    {"name": "Geophysical Research Letters", "issn": "1944-8007", "category": "top-tier"},
    {"name": "Bulletin of the American Meteorological Society", "issn": "1520-0477", "category": "top-tier"},
    {"name": "Nature Climate Change", "issn": "1758-6798", "category": "top-tier"},
    {"name": "Nature Geoscience", "issn": "1752-0908", "category": "top-tier"},
    {"name": "Nature Water", "issn": "2731-6084", "category": "top-tier"},
    {"name": "Reviews of Geophysics", "issn": "1944-9208", "category": "top-tier"},
    {"name": "Nature Communications", "issn": "2041-1723", "category": "top-tier"},
    {"name": "Nature Reviews Earth & Environment", "issn": "2662-138X", "category": "top-tier"},
    {"name": "Water Resources Research", "issn": "1944-7973", "category": "High-impact"},
    {"name": "Journal of Hydrology", "issn": "1879-2707", "category": "High-impact"},
    {"name": "Hydrology and Earth System Sciences", "issn": "1607-7938", "category": "High-impact"},
    {"name": "Advances in Water Resources", "issn": "1872-9657", "category": "High-impact"},
    {"name": "Journal of Climate", "issn": "1520-0442", "category": "High-impact"},
    {"name": "Earth System Dynamics", "issn": "2190-4987", "category": "High-impact"},
    {"name": "Global Change Biology", "issn": "1365-2486", "category": "High-impact"},
    {"name": "Environmental Research Letters", "issn": "1748-9326", "category": "High-impact"},
    {"name": "Journal of Geophysical Research: Atmospheres", "issn": "2169-8996", "category": "High-impact"},
    {"name": "Journal of Hydrometeorology", "issn": "1525-7541", "category": "High-impact"},
    {"name": "Journal of Advances in Modeling Earth Systems", "issn": "1942-2466", "category": "High-impact"},
    {"name": "Earth-Science Reviews", "issn": "1872-6828", "category": "High-impact"},
    {"name": "Journal of Geophysical Research: Machine Learning and Computation", "issn": "2993-5210", "category": "High-impact"},
    {"name": "Geoscientific Model Development", "issn": "1991-9603", "category": "High-impact"},
    {"name": "Earth's Future", "issn": "2328-4277", "category": "High-impact"},
    {"name": "Scientific Data", "issn": "2052-4463", "category": "High-impact"},
    {"name": "Scientific Reports", "issn": "2045-2322", "category": "High-impact"},
    {"name": "Hydrological Processes", "issn": "1099-1085", "category": "High-impact"},
    {"name": "Journal of the American Water Resources Association", "issn": "1752-1688", "category": "High-impact"}
]

# Keywords for relevance filtering
TOPICS = ["hydrology", "hydrologic model", "river", "runoff", "streamflow", "reservoir", "water management", "flood", "drought",
          "seasonal", "land surface model", "climate change", "hydropower", "surface water", "irrigation", "earth system model",
          "estuary", "coastal", "freshwater discharge", "river plume", "ocean biogeochemistry", "marine heatwave",
          "paleohydrology", "paleoclimate", "Quaternary", "Holocene", "Pleistocene", "fluvial geomorphology",
          "river terrace", "loess", "drainage network", "river capture", "landscape evolution", "luminescence dating"]

# Relevant Semantic Scholar fields for filtering
RELEVANT_FIELDS = [
    'engineering',
    'environmental science',
    'computer science',
    'geology',
    'geography'
]


class CrossRefClient:
    """CrossRef API client for journal paper metadata."""

    def __init__(self, email: str = None):
        self.base_url = "https://api.crossref.org"
        self.session = requests.Session()
        if email:
            self.session.headers.update({'User-Agent': f'HydroSense/2.0 (mailto:{email})'})
        else:
            self.session.headers.update({'User-Agent': 'HydroSense/2.0'})
        self.rate_limit_delay = 0.1

    def get_papers(self, issn: str, from_date: str, until_date: str) -> List[Dict]:
        """Fetch papers from a journal within date range."""
        papers = []
        offset = 0
        rows = 100

        logger.info(f"  Fetching from {issn} ({from_date} to {until_date})")

        while True:
            try:
                params = {
                    'filter': f'issn:{issn},from-pub-date:{from_date},until-pub-date:{until_date}',
                    'rows': rows,
                    'offset': offset,
                    'select': 'DOI,title,author,published,container-title,abstract,type,subject'
                }

                response = self.session.get(f"{self.base_url}/works", params=params, timeout=30)
                response.raise_for_status()

                data = response.json()
                items = data.get('message', {}).get('items', [])

                if not items:
                    break

                for item in items:
                    parsed = self._parse_item(item)
                    if parsed:
                        papers.append(parsed)

                total = data.get('message', {}).get('total-results', 0)
                if offset + rows >= total:
                    break

                offset += rows
                time.sleep(self.rate_limit_delay)

            except Exception as e:
                logger.error(f"  Error fetching {issn}: {e}")
                break

        logger.info(f"    Found {len(papers)} papers")
        return papers

    def _parse_item(self, item: Dict) -> Optional[Dict]:
        """Parse CrossRef item."""
        try:
            doi = item.get('DOI')
            if not doi:
                return None

            pub_date = None
            if 'published' in item:
                parts = item['published'].get('date-parts', [[]])[0]
                if len(parts) >= 3:
                    pub_date = f"{parts[0]:04d}-{parts[1]:02d}-{parts[2]:02d}"

            title = item.get('title', [None])[0]

            authors = []
            for a in item.get('author', []):
                name = f"{a.get('given', '')} {a.get('family', '')}".strip()
                if name:
                    authors.append(name)

            journal = item.get('container-title', [None])[0]
            abstract = item.get('abstract', '')
            item_type = item.get('type', 'unknown')

            return {
                'doi': doi,
                'title': title,
                'authors': authors,
                'publication_date': pub_date,
                'journal': journal,
                'abstract': abstract,
                'type': item_type,
                'source': 'CrossRef'
            }
        except Exception:
            return None


class OpenAlexClient:
    """OpenAlex API client for abstract retrieval."""

    def __init__(self):
        self.base_url = "https://api.openalex.org"
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'HydroSense/2.0 (mailto:hydro.luna.bot@gmail.com)'})
        self.rate_limit_delay = 0.1

    def get_abstract(self, doi: str) -> str:
        """Get abstract for a paper by DOI."""
        try:
            url = f"{self.base_url}/works/doi:{doi}"
            response = self.session.get(url, timeout=15)

            if response.status_code == 200:
                data = response.json()
                abstract_inverted = data.get('abstract_inverted_index')
                if abstract_inverted:
                    words = [''] * 1000
                    for word, positions in abstract_inverted.items():
                        for pos in positions:
                            if pos < len(words):
                                words[pos] = word
                    abstract = ' '.join(w for w in words if w)
                    time.sleep(self.rate_limit_delay)
                    return abstract
            return ''
        except Exception as e:
            logger.debug(f"OpenAlex error for {doi}: {e}")
            return ''


def fetch_hero_image(doi: str, timeout: int = 10) -> str:
    """Fetch the og:image URL from a paper's DOI landing page.

    Most publishers set <meta property="og:image"> to their graphical abstract
    or hero figure (the image that shows up when a link is shared on social
    media). We hotlink to this URL rather than downloading the image to avoid
    copyright and bandwidth concerns — the publisher is already serving it
    for public sharing.

    Returns the image URL string, or an empty string on any failure.
    """
    if not doi:
        return ''
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (compatible; HydroSense/2.0; +https://hydrosense.simhydro.com)',
            'Accept': 'text/html,application/xhtml+xml',
        }
        r = requests.get(
            f"https://doi.org/{doi}",
            headers=headers,
            timeout=timeout,
            allow_redirects=True,
        )
        if r.status_code != 200:
            return ''
        # Scan a generous chunk — Nature.com places og:image ~85k into the HTML
        html = r.text[:250000]
        # Match <meta property="og:image" ... content="...">
        # or the reverse order, with either single or double quotes.
        patterns = [
            r'<meta[^>]+property=["\']og:image["\'][^>]+content=["\']([^"\']+)["\']',
            r'<meta[^>]+content=["\']([^"\']+)["\'][^>]+property=["\']og:image["\']',
            r'<meta[^>]+name=["\']twitter:image["\'][^>]+content=["\']([^"\']+)["\']',
        ]
        for pat in patterns:
            m = re.search(pat, html, re.IGNORECASE)
            if m:
                url = m.group(1).strip()
                # Decode basic HTML entities
                url = url.replace('&amp;', '&').replace('&#x2F;', '/').replace('&#47;', '/')
                # Reject tiny 1x1 trackers or obvious logos
                if url and not url.endswith('.svg') and 'logo' not in url.lower():
                    return url
        return ''
    except Exception as e:
        logger.debug(f"hero image fetch failed for {doi}: {e}")
        return ''


class SemanticScholarClient:
    """Semantic Scholar client for paper metadata and field classification."""

    def __init__(self, api_key: str = None):
        self.base_url = "https://api.semanticscholar.org/graph/v1/paper"
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'HydroSense/2.0'})
        self.api_key = api_key
        if api_key:
            self.session.headers.update({'x-api-key': api_key})
        self.rate_limit_delay = 1.5


def clean_abstract(abstract: str) -> str:
    """Clean JATS XML tags and other markup from abstract text."""
    if not abstract:
        return ''
    abstract = str(abstract)
    abstract = re.sub(r'<jats:[^>]+>', '', abstract)
    abstract = re.sub(r'</jats:[^>]+>', '', abstract)
    abstract = re.sub(r'<[^>]+>', '', abstract)
    return abstract.strip()


def format_journal_list(all_papers: List[Dict], selected_papers: List[Dict]) -> str:
    """Create a text-based journal list with paper counts."""
    journal_total = {}
    journal_selected = {}

    for paper in all_papers:
        journal = paper.get('journal_name', 'Unknown')
        journal_total[journal] = journal_total.get(journal, 0) + 1

    for paper in selected_papers:
        journal = paper.get('journal_name', 'Unknown')
        journal_selected[journal] = journal_selected.get(journal, 0) + 1

    journals = [j for j in journal_total.keys() if journal_total[j] > 0]
    journals.sort(key=lambda x: journal_total[x], reverse=True)

    max_name_length = 50
    lines = []
    for journal in journals:
        total = journal_total[journal]
        selected = journal_selected.get(journal, 0)
        if len(journal) > max_name_length:
            journal_display = journal[:max_name_length-3] + "..."
        else:
            journal_display = journal.ljust(max_name_length)
        lines.append(f"{journal_display} ({selected}/{total})")

    return "\n".join(lines)


def format_paper(paper: Dict) -> str:
    """Format a single paper for markdown output."""
    lines = []

    title = paper.get('title') or 'No title'
    lines.append(f"### {title}")
    lines.append("")

    authors = paper.get('authors', [])
    if authors:
        author_str = ", ".join(authors[:5])
        if len(authors) > 5:
            author_str += f" et al. ({len(authors)} authors)"
        lines.append(f"**Authors:** {author_str}")

    journal = paper.get('journal', 'Unknown journal')
    category = paper.get('category', '')
    tier_marker = " ⭐" if category == 'top-tier' else ""
    date = paper.get('publication_date', 'No date')
    lines.append(f"**Journal:** {journal}{tier_marker} ({date})")

    content_type = paper.get('type', 'unknown')
    if content_type != 'journal-article':
        type_display = content_type.replace('-', ' ').title()
        lines.append(f"**Content Type:** {type_display}")

    doi = paper.get('doi', '')
    lines.append(f"**DOI:** [{doi}](https://doi.org/{doi})")

    matched_fields = paper.get('matched_fields', [])
    matched_topics = paper.get('matched_topics', [])
    if matched_topics or matched_fields:
        lines.append("")
        if matched_topics:
            lines.append(f"**Matched Topics:** {', '.join(matched_topics)}")
        if matched_fields:
            lines.append(f"**Matched Fields:** {', '.join(matched_fields)}")

    abstract = paper.get('abstract')
    if abstract:
        abstract = clean_abstract(abstract)
        if len(abstract) > 800:
            abstract = abstract[:800] + "..."
        lines.append(f"\n**Abstract:**\n\n{abstract}")
    else:
        lines.append(f"\n*Abstract not available*")

    return "\n".join(lines)


def enrich_papers(all_papers: List[Dict], s2: SemanticScholarClient, openalex: OpenAlexClient) -> tuple:
    """Enrich papers with S2 metadata and classify into part1/part2.

    Returns (part1_papers, part2_papers, s2_stats).
    """
    part1_papers = []
    part2_papers = []
    s2_found = 0
    s2_not_found = 0
    s2_errors = 0

    for i, paper in enumerate(all_papers, 1):
        title = paper.get('title') or 'Untitled'
        is_top_tier = paper.get('category') == 'top-tier'

        logger.info(f"[{i}/{len(all_papers)}] {title[:70]}...")

        # Get S2 metadata
        doi = paper['doi']
        try:
            url = f"https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}"
            params = {'fields': 'paperId,fieldsOfStudy,title,abstract'}
            response = s2.session.get(url, params=params, timeout=15)
            time.sleep(s2.rate_limit_delay)

            if response.status_code == 200:
                s2_found += 1
                data = response.json()
            elif response.status_code == 429:
                s2_errors += 1
                logger.warning(f"  ⚠ Rate limited by S2 - waiting 5 seconds...")
                time.sleep(5)
                continue
            elif response.status_code == 404:
                s2_not_found += 1
                logger.info(f"  ✗ Not in S2 (404)")
                continue
            else:
                s2_errors += 1
                logger.info(f"  ✗ Not in S2 (status {response.status_code})")
                continue
        except Exception as e:
            s2_errors += 1
            logger.warning(f"  ✗ Error checking S2: {e}")
            continue

        # Process S2 data
        fields_raw = data.get('fieldsOfStudy') or []
        fields = [f.lower() for f in fields_raw]
        matched_fields = [f for f in fields if f in RELEVANT_FIELDS]

        s2_title = data.get('title') or title
        s2_abstract = data.get('abstract') or paper.get('abstract', '')
        content = (s2_title + " " + s2_abstract).lower()
        matched_topics = [t for t in TOPICS if t.lower() in content]

        paper['s2_paper_id'] = data.get('paperId')
        paper['matched_fields'] = matched_fields
        paper['matched_topics'] = matched_topics

        # Abstract priority: S2 > OpenAlex > CrossRef
        if s2_abstract:
            paper['abstract'] = s2_abstract
            paper['abstract_source'] = 'S2'
        else:
            openalex_abstract = openalex.get_abstract(doi)
            if openalex_abstract:
                paper['abstract'] = openalex_abstract
                paper['abstract_source'] = 'OpenAlex'
            elif paper.get('abstract'):
                paper['abstract_source'] = 'CrossRef'
            else:
                paper['abstract_source'] = 'None'

        # Deterministic classification (no LLM)
        paper_type = paper.get('type', 'unknown')
        is_peer_reviewed = paper_type == 'journal-article'

        if matched_topics and is_peer_reviewed:
            # Only fetch hero image for papers that made the cut — saves HTTP
            # requests on rejected ones. Politeness: 0.3s between fetches.
            hero_url = fetch_hero_image(doi)
            paper['hero_image_url'] = hero_url
            if hero_url:
                logger.info(f"  🖼  Hero image: {hero_url[:80]}")
            time.sleep(0.3)

            if is_top_tier:
                part1_papers.append(paper)
                logger.info(f"  ⭐ PART 1: Top-tier + topics: {', '.join(matched_topics[:2])}")
            else:
                part2_papers.append(paper)
                logger.info(f"  ✓ PART 2: High-impact + topics: {', '.join(matched_topics[:2])}")
        elif matched_topics and not is_peer_reviewed:
            logger.info(f"  ✗ Rejected: {paper_type} (not peer-reviewed)")
        else:
            logger.info(f"  ✗ Rejected: No topic match")

    s2_stats = {
        's2_found': s2_found,
        's2_not_found': s2_not_found,
        's2_errors': s2_errors,
    }

    return part1_papers, part2_papers, s2_stats


def output_json(all_papers, part1, part2, s2_stats, from_str, until_str, journals_searched):
    """Output results as JSON to stdout."""
    all_selected = part1 + part2
    papers_with_abstract = sum(1 for p in all_selected if p.get('abstract'))

    def paper_to_json(p):
        return {
            'doi': p.get('doi', ''),
            'title': p.get('title', ''),
            'authors': p.get('authors', []),
            'journal': p.get('journal_name', p.get('journal', '')),
            'category': p.get('category', ''),
            'publication_date': p.get('publication_date', ''),
            'abstract': clean_abstract(p.get('abstract', '')),
            'abstract_source': p.get('abstract_source', ''),
            'type': p.get('type', ''),
            'matched_topics': p.get('matched_topics', []),
            'matched_fields': p.get('matched_fields', []),
            's2_paper_id': p.get('s2_paper_id', ''),
            'hero_image_url': p.get('hero_image_url', ''),
        }

    result = {
        'harvest_date': datetime.now().strftime('%Y-%m-%d'),
        'date_range': {'from': from_str, 'to': until_str},
        'journals_searched': journals_searched,
        'total_fetched': len(all_papers),
        'papers': {
            'part1': [paper_to_json(p) for p in part1],
            'part2': [paper_to_json(p) for p in part2],
        },
        'statistics': {
            's2_found': s2_stats['s2_found'],
            's2_not_found': s2_stats['s2_not_found'],
            's2_errors': s2_stats['s2_errors'],
            'papers_with_abstracts': papers_with_abstract,
            'total_selected': len(all_selected),
        }
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))


def output_markdown(all_papers, part1, part2, s2_stats, from_str, until_str):
    """Output results as a Jekyll markdown post."""
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    total = len(part1) + len(part2)
    all_selected = part1 + part2
    papers_with_abstract = sum(1 for p in all_selected if p.get('abstract'))

    # Console output
    print(f"\n{'='*70}")
    print(f"📋 Papers Selected: {total}")
    print(f"   Part 1 (Top-tier + topics): {len(part1)}")
    print(f"   Part 2 (High-impact + topics): {len(part2)}")
    print(f"   Papers with abstracts: {papers_with_abstract}/{total}")
    print(f"{'='*70}\n")

    # Determine post path
    month_name = datetime.strptime(until_str, '%Y-%m-%d').strftime('%B')
    year = until_str[:4]
    month_folder = month_name.lower()
    posts_dir = f"{project_dir}/_pages/{year}/{month_folder}"
    os.makedirs(posts_dir, exist_ok=True)

    # Create year index if needed
    year_index = f"{project_dir}/_pages/{year}/index.md"
    if not os.path.exists(year_index):
        year_order = int(year) - 2023
        with open(year_index, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write("layout: default\n")
            f.write(f"title: {year}\n")
            f.write(f"nav_order: {year_order}\n")
            f.write("has_children: true\n")
            f.write("---\n\n")
            f.write(f"# {year} Harvest Reports\n\n")
            f.write(f"All paper harvest reports from {year}, organized by month.\n")

    # Create month index if needed
    month_index = f"{posts_dir}/index.md"
    if not os.path.exists(month_index):
        month_order = datetime.strptime(until_str, '%Y-%m-%d').month
        with open(month_index, 'w', encoding='utf-8') as f:
            f.write("---\n")
            f.write("layout: default\n")
            f.write(f"title: {month_name}\n")
            f.write(f"parent: {year}\n")
            f.write(f"nav_order: {month_order}\n")
            f.write("has_children: true\n")
            f.write("---\n\n")
            f.write(f"# {month_name} {year}\n\n")
            f.write(f"Daily harvest reports for {month_name} {year}.\n")

    # Write Jekyll post
    post_file = f"{posts_dir}/{until_str}-daily-harvest.md"
    day = datetime.strptime(until_str, '%Y-%m-%d').day

    selection_pct = (total/len(all_papers)*100) if len(all_papers) > 0 else 0
    abstract_pct = (papers_with_abstract/total*100) if total > 0 else 0
    s2_coverage = (s2_stats['s2_found']/len(all_papers)*100) if len(all_papers) > 0 else 0

    with open(post_file, 'w', encoding='utf-8') as f:
        # Front matter
        f.write("---\n")
        f.write("layout: default\n")
        f.write(f'title: "{month_name} {day:02d} - Daily Harvest"\n')
        f.write(f"parent: {month_name}\n")
        f.write(f"grand_parent: {year}\n")
        f.write(f"nav_order: {day}\n")
        f.write(f"date: {until_str}\n")
        f.write(f'categories: [daily, {year}, {month_name.lower()}]\n')
        f.write(f'tags: [hydrology, paper-harvest, research]\n')
        f.write("---\n\n")

        f.write(f"# Paper Harvest Report\n\n")
        f.write(f"**Date Range:** {from_str} to {until_str}\n\n")
        f.write(f"**{len(part1)}** top-tier and **{len(part2)}** high-impact papers were selected out of **{len(all_papers)}** total publications ({selection_pct:.1f}%).\n\n")
        f.write("---\n\n")

        if part1:
            f.write(f"# Part 1: Top-Tier Journals + Topic Match ({len(part1)} papers)\n\n")
            f.write("*Peer-reviewed research articles from top-tier journals that match your research topics.*\n\n")
            for paper in part1:
                f.write(format_paper(paper))
                f.write("\n\n---\n\n")

        if part2:
            f.write(f"# Part 2: High-Impact Journals + Topic Match ({len(part2)} papers)\n\n")
            f.write("*Peer-reviewed research articles from high-impact journals that match your topics.*\n\n")
            for paper in part2:
                f.write(format_paper(paper))
                f.write("\n\n---\n\n")

        # Statistics
        f.write("---\n\n")
        f.write(f"## Statistics\n\n")
        f.write(f"- **Papers Published:** {len(all_papers)} (research articles from tracked journals)\n")
        f.write(f"- **Papers Selected:** {total} ({selection_pct:.1f}%)\n")
        f.write(f"- **Papers with Abstracts:** {papers_with_abstract}/{total} ({abstract_pct:.1f}%)\n")
        f.write(f"- **Semantic Scholar Coverage:** {s2_stats['s2_found']}/{len(all_papers)} ({s2_coverage:.1f}%)\n")
        f.write(f"  - Not in S2: {s2_stats['s2_not_found']} papers (404 errors are normal for non-indexed content)\n\n")

        f.write(f"### Papers by Journal\n\n")
        f.write(f"```\n")
        f.write(format_journal_list(all_papers, all_selected))
        f.write(f"\n```\n\n")
        f.write(f"*Format: Journal Name (selected/published)*\n\n")

        f.write(f"### Selection Breakdown\n\n")
        f.write(f"- Part 1 (Top-tier + topics): {len(part1)}\n")
        f.write(f"- Part 2 (High-impact + topics): {len(part2)}\n\n")

        f.write(f"### Filtering Criteria\n\n")
        f.write(f"**Relevant Fields:** {', '.join(RELEVANT_FIELDS)}\n\n")
        f.write(f"**Topics:** {', '.join(TOPICS)}\n\n")

    print(f"\n📁 Jekyll post saved to: {post_file}")
    print(f"🌐 Blog URL: https://hydrosense.simhydro.com/{year}/{month_name.lower()}/{until_str}-daily-harvest.html")


def main():
    """Main harvester logic."""

    def valid_date(s):
        try:
            datetime.strptime(s, '%Y-%m-%d')
            return s
        except ValueError:
            raise argparse.ArgumentTypeError(f"Invalid date '{s}'. Use YYYY-MM-DD format.")

    parser = argparse.ArgumentParser(description='HydroSense Paper Harvester')
    parser.add_argument('--date', type=valid_date, help='Specific date to harvest (YYYY-MM-DD)')
    parser.add_argument('--journals', choices=['top-tier', 'high-impact', 'all'], default='top-tier',
                        help='Which journal set to scan (default: top-tier)')
    parser.add_argument('--output-format', choices=['markdown', 'json'], default='markdown',
                        help='Output format (default: markdown)')
    parser.add_argument('--backfill', action='store_true', help='Run backfill for next month')
    parser.add_argument('--backfill-start', type=valid_date,
                        help='Override backfill start date (default: 2020-01-01)')
    parser.add_argument('--no-increment', action='store_true', help='Do not increment backfill counter')
    args = parser.parse_args()

    # Date range
    if args.date:
        from_str = args.date
        until_str = args.date
    elif args.backfill:
        start_date = datetime.strptime(args.backfill_start, '%Y-%m-%d') if args.backfill_start else None
        from_str, until_str, _ = get_next_backfill_month(start_date)
        # Backfill always uses top-tier
        args.journals = 'top-tier'
    else:
        from_str = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        until_str = (datetime.now() - timedelta(days=1)).strftime('%Y-%m-%d')

    # Filter journals
    if args.journals == 'top-tier':
        active_journals = [j for j in JOURNALS if j['category'] == 'top-tier']
    elif args.journals == 'high-impact':
        active_journals = [j for j in JOURNALS if j['category'] == 'High-impact']
    else:
        active_journals = JOURNALS

    logger.info(f"Paper Harvest: {from_str} to {until_str}")
    logger.info(f"Journals: {args.journals} ({len(active_journals)} journals)")
    logger.info(f"Output: {args.output_format}")

    # Initialize clients
    crossref = CrossRefClient(email=CROSSREF_EMAIL or "hydro.luna.bot@gmail.com")
    openalex = OpenAlexClient()

    s2 = None
    s2_available = False
    if SEMANTIC_SCHOLAR_API_KEY:
        s2 = SemanticScholarClient(api_key=SEMANTIC_SCHOLAR_API_KEY)
        s2_available = True
        logger.info(f"Semantic Scholar API: configured (rate limit: {s2.rate_limit_delay}s)")
    else:
        logger.warning("Semantic Scholar API not configured - set SEMANTIC_SCHOLAR_API_KEY in .env")

    # Fetch papers
    all_papers = []
    for journal in active_journals:
        papers = crossref.get_papers(journal['issn'], from_str, until_str)
        for paper in papers:
            paper['journal_name'] = journal['name']
            paper['category'] = journal['category']
            all_papers.append(paper)

    logger.info(f"Total papers fetched: {len(all_papers)}")

    # Enrich and classify
    if s2_available:
        part1, part2, s2_stats = enrich_papers(all_papers, s2, openalex)
    else:
        logger.warning("S2 not available - all papers go to part2 unfiltered")
        part1, part2 = [], all_papers
        s2_stats = {'s2_found': 0, 's2_not_found': 0, 's2_errors': 0}

    logger.info(f"Results: Part 1={len(part1)}, Part 2={len(part2)}")

    # Output
    if args.output_format == 'json':
        output_json(all_papers, part1, part2, s2_stats, from_str, until_str, len(active_journals))
    else:
        output_markdown(all_papers, part1, part2, s2_stats, from_str, until_str)

    # Increment backfill counter
    if args.backfill and not args.no_increment:
        increment_backfill_counter()


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
DOI Citation Extractor for HydroSense Science-News

Given URLs of editorial articles (Nature News, Science Magazine), fetches each
page, regex-extracts cited DOIs, looks them up via CrossRef + Semantic Scholar
+ OpenAlex, and outputs enriched paper records in the shape the daily-harvest
post expects.

Used by the science-news skill to surface peer-reviewed papers cited in news
pieces so they join the daily post's Top-Tier Journal Papers section.

Usage:
    python extract_doi_citations.py /tmp/science_news_doi_candidates.json
    python extract_doi_citations.py --url https://www.nature.com/articles/d41586-...
    python extract_doi_citations.py /tmp/in.json --output /tmp/out.json
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from datetime import datetime, timezone
from typing import Dict, List, Optional, Set

import requests
from dotenv import load_dotenv

load_dotenv()
SEMANTIC_SCHOLAR_API_KEY = os.getenv('SEMANTIC_SCHOLAR_API_KEY')
CROSSREF_EMAIL = os.getenv('CROSSREF_EMAIL')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)


# DOI pattern. Standard DOI is 10.NNNN/<suffix> where the suffix allows a
# generous character set. We anchor on the prefix and consume until whitespace,
# quote, angle bracket, or HTML entity boundary.
DOI_REGEX = re.compile(r'10\.\d{4,9}/[-._;()/:A-Za-z0-9]+')

# DOI candidates often carry trailing junk: prose punctuation (`.`, `,`),
# URL/metadata attributes that leak in from Nature's HTML (`;subjmeta=...`,
# `?foo=bar`, `#fragment`), or HTML-attribute terminators. Strip everything
# from the first such boundary onward. This loses the rare DOI that
# legitimately contains `;`, but for the publishers we extract from
# (Springer/Nature, AAAS) those are non-existent in practice.
TRAILING_JUNK = re.compile(r'[;?#].*$|[.,)\]\}>]+$')


def fetch_html(url: str, timeout: int = 30) -> Optional[str]:
    try:
        resp = requests.get(
            url,
            timeout=timeout,
            headers={'User-Agent': 'HydroSense/2.0 (citation extractor)'},
        )
        resp.raise_for_status()
        return resp.text
    except Exception as e:
        logger.warning(f"  Failed to fetch {url}: {e}")
        return None


def extract_dois(html: str, exclude: Set[str] = None) -> List[str]:
    """Pull unique DOIs out of article HTML, in first-seen order."""
    exclude = exclude or set()
    seen = set(exclude)
    out = []
    for match in DOI_REGEX.findall(html):
        doi = TRAILING_JUNK.sub('', match)
        # Strip trailing chars that DOI suffixes commonly catch but rarely
        # contain. Repeat until stable (handles "10.x/y).." → "10.x/y").
        while True:
            stripped = TRAILING_JUNK.sub('', doi)
            if stripped == doi:
                break
            doi = stripped
        doi_lower = doi.lower()
        if doi_lower in seen:
            continue
        seen.add(doi_lower)
        out.append(doi)
    return out


def article_own_doi(url: str) -> Optional[str]:
    """Best-effort: derive the article's own DOI from its URL so we can exclude
    it from the extracted-citations list."""
    # Nature: /articles/d41586-026-01651-0 → 10.1038/d41586-026-01651-0
    m = re.search(r'nature\.com/articles/([a-z0-9]+-\d+-\d+(?:-[a-z0-9]+)?)', url, re.I)
    if m:
        return f"10.1038/{m.group(1)}"
    # Science: /doi/10.1126/science.<id>
    m = re.search(r'science\.org/doi/(10\.\d{4,9}/[^/?#]+)', url, re.I)
    if m:
        return m.group(1)
    return None


def crossref_lookup(doi: str, timeout: int = 15) -> Optional[Dict]:
    """Look up paper metadata via CrossRef. Returns paper dict in harvest.py
    shape, or None on failure."""
    headers = {'User-Agent': f'HydroSense/2.0 (mailto:{CROSSREF_EMAIL})' if CROSSREF_EMAIL else 'HydroSense/2.0'}
    try:
        resp = requests.get(f'https://api.crossref.org/works/{doi}', timeout=timeout, headers=headers)
        if resp.status_code != 200:
            logger.info(f"  CrossRef {resp.status_code} for {doi}")
            return None
        msg = resp.json().get('message', {})
    except Exception as e:
        logger.warning(f"  CrossRef error for {doi}: {e}")
        return None

    title_list = msg.get('title') or []
    title = title_list[0] if title_list else ''
    journal_list = msg.get('container-title') or []
    journal = journal_list[0] if journal_list else ''

    authors = []
    for a in msg.get('author', []):
        name = ' '.join(x for x in [a.get('given'), a.get('family')] if x).strip()
        if name:
            authors.append(name)

    # Published date: prefer published-online > published-print > created.
    date_parts = None
    for field in ('published-online', 'published-print', 'published', 'created'):
        v = msg.get(field, {})
        if isinstance(v, dict) and v.get('date-parts'):
            date_parts = v['date-parts'][0]
            break
    published = '-'.join(f"{p:02d}" if i > 0 else str(p) for i, p in enumerate(date_parts)) if date_parts else ''

    return {
        'doi': doi,
        'title': title.strip(),
        'authors': authors,
        'journal_name': journal,
        'published': published,
        'abstract': msg.get('abstract', ''),
        'abstract_source': 'CrossRef' if msg.get('abstract') else 'None',
        'type': msg.get('type', 'unknown'),
        'category': 'top-tier',  # cited-from-editorial → treat as top-tier
    }


def clean_abstract(abstract: str) -> str:
    if not abstract:
        return ''
    abstract = re.sub(r'<jats:[^>]+>', '', str(abstract))
    abstract = re.sub(r'</jats:[^>]+>', '', abstract)
    abstract = re.sub(r'<[^>]+>', '', abstract)
    return abstract.strip()


def s2_enrich(doi: str, session: requests.Session, delay: float = 1.5) -> Dict:
    """Pull abstract + paperId from Semantic Scholar."""
    try:
        url = f'https://api.semanticscholar.org/graph/v1/paper/DOI:{doi}'
        resp = session.get(url, params={'fields': 'paperId,abstract,title'}, timeout=15)
        time.sleep(delay)
        if resp.status_code == 200:
            d = resp.json()
            return {'s2_paper_id': d.get('paperId'), 'abstract': d.get('abstract') or '', 'title': d.get('title') or ''}
        if resp.status_code == 429:
            logger.warning("  S2 rate-limited, sleeping 5s")
            time.sleep(5)
    except Exception as e:
        logger.debug(f"  S2 error for {doi}: {e}")
    return {}


def openalex_abstract(doi: str, session: requests.Session, delay: float = 0.1) -> str:
    try:
        resp = session.get(f'https://api.openalex.org/works/doi:{doi}', timeout=15)
        time.sleep(delay)
        if resp.status_code != 200:
            return ''
        inverted = resp.json().get('abstract_inverted_index')
        if not inverted:
            return ''
        # Reconstruct from positional index
        max_pos = max((p for positions in inverted.values() for p in positions), default=-1)
        words = [''] * (max_pos + 1)
        for word, positions in inverted.items():
            for p in positions:
                words[p] = word
        return ' '.join(w for w in words if w)
    except Exception as e:
        logger.debug(f"  OpenAlex error for {doi}: {e}")
        return ''


def enrich_paper(paper: Dict, s2_session: requests.Session, oa_session: requests.Session) -> Dict:
    """Add S2 paperId + best-available abstract (S2 > OpenAlex > CrossRef)."""
    doi = paper['doi']
    s2 = s2_enrich(doi, s2_session)
    if s2.get('s2_paper_id'):
        paper['s2_paper_id'] = s2['s2_paper_id']
    if s2.get('abstract'):
        paper['abstract'] = s2['abstract']
        paper['abstract_source'] = 'S2'
    else:
        oa_abs = openalex_abstract(doi, oa_session)
        if oa_abs:
            paper['abstract'] = oa_abs
            paper['abstract_source'] = 'OpenAlex'
    paper['abstract'] = clean_abstract(paper.get('abstract', ''))
    return paper


def process_url(url: str, s2_session: requests.Session, oa_session: requests.Session) -> Dict:
    logger.info(f"Processing {url}")
    html = fetch_html(url)
    if not html:
        return {'url': url, 'extracted_dois': [], 'papers': [], 'error': 'fetch failed'}

    own = article_own_doi(url)
    exclude = {own.lower()} if own else set()
    dois = extract_dois(html, exclude=exclude)
    logger.info(f"  Found {len(dois)} DOIs (excluding own={own})")

    papers = []
    for doi in dois:
        meta = crossref_lookup(doi)
        if not meta:
            continue
        meta['via_source'] = url
        meta = enrich_paper(meta, s2_session, oa_session)
        papers.append(meta)
        logger.info(f"  ✓ {doi}: {meta.get('title','')[:60]}")

    return {'url': url, 'extracted_dois': dois, 'papers': papers}


def main():
    parser = argparse.ArgumentParser(description='Extract & enrich DOIs cited in science-news articles')
    parser.add_argument('input', nargs='?', help='JSON file with {"urls": [...]} (default: /tmp/science_news_doi_candidates.json)')
    parser.add_argument('--url', action='append', help='Add a single URL (repeatable). Overrides input file.')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')
    args = parser.parse_args()

    if args.url:
        urls = args.url
    else:
        path = args.input or '/tmp/science_news_doi_candidates.json'
        try:
            data = json.loads(open(path).read())
            urls = data.get('urls', [])
        except FileNotFoundError:
            logger.error(f"Input file not found: {path}")
            sys.exit(1)

    if not urls:
        logger.info("No URLs to process — exiting with empty output")
        result = {'generated_at': datetime.now(timezone.utc).isoformat(), 'source_articles': [], 'papers': []}
    else:
        logger.info(f"Processing {len(urls)} URL(s)")
        s2_session = requests.Session()
        s2_session.headers.update({'User-Agent': 'HydroSense/2.0'})
        if SEMANTIC_SCHOLAR_API_KEY:
            s2_session.headers.update({'x-api-key': SEMANTIC_SCHOLAR_API_KEY})
        oa_session = requests.Session()
        oa_session.headers.update({'User-Agent': 'HydroSense/2.0 (mailto:hydro.luna.bot@gmail.com)'})

        source_articles = [process_url(u, s2_session, oa_session) for u in urls]
        all_papers = [p for sa in source_articles for p in sa['papers']]

        # Dedup across source articles (a paper cited by two editorials only
        # appears once). Keep first occurrence; track via_source list.
        by_doi = {}
        for p in all_papers:
            key = p['doi'].lower()
            if key in by_doi:
                existing = by_doi[key]
                via = existing.get('via_source')
                vias = via if isinstance(via, list) else [via]
                if p['via_source'] not in vias:
                    vias.append(p['via_source'])
                existing['via_source'] = vias
            else:
                by_doi[key] = p
        papers = list(by_doi.values())

        result = {
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'source_articles': [{'url': sa['url'], 'extracted_dois': sa['extracted_dois']} for sa in source_articles],
            'papers': papers,
        }
        logger.info(f"Total: {len(all_papers)} papers extracted, {len(papers)} after dedup")

    output_str = json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        open(args.output, 'w').write(output_str)
        logger.info(f"Wrote {args.output}")
    else:
        print(output_str)


if __name__ == '__main__':
    main()

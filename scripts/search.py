#!/usr/bin/env python3
"""
Keyword-Based Literature Search for HydroSense

Searches academic databases by keywords (not journal-specific) to find
relevant papers across all venues. Outputs structured JSON for Claude
to synthesize into reviews at any frequency (weekly, monthly, yearly).

Databases searched:
  - Semantic Scholar (Academic Graph API)
  - OpenAlex

Usage:
    python search.py                                          # Last 7 days, default topics
    python search.py --weeks-back 2                           # Last 2 weeks
    python search.py --from-date 2025-01-01 --to-date 2025-12-31  # Specific date range
    python search.py --topics "flood,reservoir,runoff"        # Custom topics
    python search.py --output-format markdown                 # Simple markdown list
"""

import argparse
import json
import logging
import os
import re
import requests
import time
from datetime import datetime, timedelta
from typing import List, Dict, Optional

from dotenv import load_dotenv
load_dotenv()

SEMANTIC_SCHOLAR_API_KEY = os.getenv('SEMANTIC_SCHOLAR_API_KEY')

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Default topics (same as harvest.py)
DEFAULT_TOPICS = [
    "hydrology", "hydrologic model", "river", "runoff", "streamflow",
    "reservoir", "water management", "flood", "drought", "seasonal",
    "land surface model", "climate change", "hydropower", "surface water",
    "irrigation", "earth system model"
]

# Relevant fields for filtering S2 results
RELEVANT_FIELDS = [
    'Environmental Science',
    'Engineering',
    'Computer Science',
    'Geology',
    'Geography',
]


class SemanticScholarSearch:
    """Semantic Scholar Academic Graph API for keyword-based paper search."""

    def __init__(self, api_key: str = None):
        self.base_url = "https://api.semanticscholar.org/graph/v1"
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'HydroSense/2.0'})
        if api_key:
            self.session.headers.update({'x-api-key': api_key})
        self.rate_limit_delay = 3.0  # Search API is more aggressively rate-limited than graph API

    def search_papers(self, query: str, year_from: int, year_to: int, limit: int = 100) -> List[Dict]:
        """Search for papers by keyword query."""
        papers = []
        offset = 0
        batch_size = min(limit, 100)
        rate_limit_retries = 0
        max_rate_limit_retries = 3

        while offset < limit:
            try:
                params = {
                    'query': query,
                    'year': f"{year_from}-{year_to}",
                    'fields': 'paperId,title,authors,year,venue,externalIds,abstract,fieldsOfStudy,publicationDate,citationCount',
                    'offset': offset,
                    'limit': batch_size,
                }

                response = self.session.get(f"{self.base_url}/paper/search", params=params, timeout=30)
                time.sleep(self.rate_limit_delay)

                if response.status_code == 429:
                    rate_limit_retries += 1
                    if rate_limit_retries > max_rate_limit_retries:
                        logger.warning(f"S2 rate limited {max_rate_limit_retries} times for '{query}', moving on")
                        break
                    wait_time = 10 * rate_limit_retries
                    logger.warning(f"S2 rate limited, waiting {wait_time} seconds (retry {rate_limit_retries}/{max_rate_limit_retries})...")
                    time.sleep(wait_time)
                    continue

                if response.status_code != 200:
                    logger.error(f"S2 search error {response.status_code}: {response.text[:200]}")
                    break

                data = response.json()
                batch = data.get('data', [])

                if not batch:
                    break

                for item in batch:
                    paper = self._parse_result(item, query)
                    if paper:
                        papers.append(paper)

                total = data.get('total', 0)
                offset += batch_size
                if offset >= total:
                    break

            except Exception as e:
                logger.error(f"S2 search error for '{query}': {e}")
                break

        logger.info(f"  S2: '{query}' -> {len(papers)} papers")
        return papers

    def _parse_result(self, item: Dict, query: str) -> Optional[Dict]:
        """Parse a Semantic Scholar search result."""
        doi = None
        ext_ids = item.get('externalIds') or {}
        doi = ext_ids.get('DOI')
        if not doi:
            return None

        authors = []
        for a in (item.get('authors') or []):
            name = a.get('name', '')
            if name:
                authors.append(name)

        fields = [f for f in (item.get('fieldsOfStudy') or [])]

        return {
            'doi': doi,
            'title': item.get('title', ''),
            'authors': authors,
            'journal': item.get('venue', ''),
            'publication_date': item.get('publicationDate', ''),
            'abstract': item.get('abstract', ''),
            'type': 'journal-article',
            'fields_of_study': fields,
            'citation_count': item.get('citationCount', 0),
            's2_paper_id': item.get('paperId', ''),
            'search_query': query,
            'source_db': 'S2',
        }


class OpenAlexSearch:
    """OpenAlex API for keyword-based paper search."""

    def __init__(self):
        self.base_url = "https://api.openalex.org"
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'HydroSense/2.0 (mailto:hydro.luna.bot@gmail.com)'})
        self.rate_limit_delay = 0.1

    def search_papers(self, query: str, from_date: str, to_date: str, limit: int = 100) -> List[Dict]:
        """Search for papers by keyword query."""
        papers = []
        page = 1
        per_page = min(limit, 50)

        while len(papers) < limit:
            try:
                params = {
                    'search': query,
                    'filter': f'from_publication_date:{from_date},to_publication_date:{to_date},type:article',
                    'per_page': per_page,
                    'page': page,
                    'select': 'doi,title,authorships,publication_date,primary_location,abstract_inverted_index,type,cited_by_count,concepts',
                }

                response = self.session.get(f"{self.base_url}/works", params=params, timeout=30)
                time.sleep(self.rate_limit_delay)

                if response.status_code != 200:
                    logger.error(f"OpenAlex search error {response.status_code}")
                    break

                data = response.json()
                results = data.get('results', [])

                if not results:
                    break

                for item in results:
                    paper = self._parse_result(item, query)
                    if paper:
                        papers.append(paper)

                total = data.get('meta', {}).get('count', 0)
                if page * per_page >= total:
                    break

                page += 1

            except Exception as e:
                logger.error(f"OpenAlex search error for '{query}': {e}")
                break

        logger.info(f"  OpenAlex: '{query}' -> {len(papers)} papers")
        return papers

    def _parse_result(self, item: Dict, query: str) -> Optional[Dict]:
        """Parse an OpenAlex search result."""
        doi_url = item.get('doi', '')
        if not doi_url:
            return None
        doi = doi_url.replace('https://doi.org/', '')

        authors = []
        for a in (item.get('authorships') or []):
            author_data = a.get('author', {})
            name = author_data.get('display_name', '')
            if name:
                authors.append(name)

        journal = ''
        primary_loc = item.get('primary_location') or {}
        source = primary_loc.get('source') or {}
        journal = source.get('display_name', '')

        abstract = ''
        abstract_inv = item.get('abstract_inverted_index')
        if abstract_inv:
            words = [''] * 1000
            for word, positions in abstract_inv.items():
                for pos in positions:
                    if pos < len(words):
                        words[pos] = word
            abstract = ' '.join(w for w in words if w)

        return {
            'doi': doi,
            'title': item.get('title', ''),
            'authors': authors,
            'journal': journal,
            'publication_date': item.get('publication_date', ''),
            'abstract': abstract,
            'type': 'journal-article',
            'fields_of_study': [],
            'citation_count': item.get('cited_by_count', 0),
            's2_paper_id': '',
            'search_query': query,
            'source_db': 'OpenAlex',
        }


def deduplicate_papers(papers: List[Dict]) -> List[Dict]:
    """Deduplicate papers by DOI, merging metadata from multiple sources."""
    seen = {}
    for paper in papers:
        doi = paper.get('doi', '').strip().lower()
        if not doi:
            continue

        if doi in seen:
            existing = seen[doi]
            # Merge: keep the richer record
            if not existing.get('abstract') and paper.get('abstract'):
                existing['abstract'] = paper['abstract']
            if paper.get('citation_count', 0) > existing.get('citation_count', 0):
                existing['citation_count'] = paper['citation_count']
            if paper.get('s2_paper_id') and not existing.get('s2_paper_id'):
                existing['s2_paper_id'] = paper['s2_paper_id']
            if paper.get('fields_of_study') and not existing.get('fields_of_study'):
                existing['fields_of_study'] = paper['fields_of_study']
            # Track all queries that found this paper
            existing_queries = existing.get('matched_queries', [])
            new_query = paper.get('search_query', '')
            if new_query and new_query not in existing_queries:
                existing_queries.append(new_query)
            existing['matched_queries'] = existing_queries
            # Track source databases
            existing_sources = existing.get('source_databases', [])
            new_source = paper.get('source_db', '')
            if new_source and new_source not in existing_sources:
                existing_sources.append(new_source)
            existing['source_databases'] = existing_sources
        else:
            paper['matched_queries'] = [paper.get('search_query', '')]
            paper['source_databases'] = [paper.get('source_db', '')]
            seen[doi] = paper

    return list(seen.values())


def clean_abstract(abstract: str) -> str:
    """Clean markup from abstract text."""
    if not abstract:
        return ''
    abstract = re.sub(r'<[^>]+>', '', str(abstract))
    return abstract.strip()


def main():
    parser = argparse.ArgumentParser(description='HydroSense Keyword-Based Literature Search')
    parser.add_argument('--weeks-back', type=int, default=None,
                        help='How many weeks back to search (default: 1 if no --from-date)')
    parser.add_argument('--from-date', type=str, default=None,
                        help='Start date for search (YYYY-MM-DD). Overrides --weeks-back')
    parser.add_argument('--to-date', type=str, default=None,
                        help='End date for search (YYYY-MM-DD). Defaults to today')
    parser.add_argument('--topics', type=str, default=None,
                        help='Comma-separated topic keywords (default: built-in TOPICS list)')
    parser.add_argument('--output-format', choices=['json', 'markdown'], default='json',
                        help='Output format (default: json)')
    parser.add_argument('--max-per-topic', type=int, default=50,
                        help='Max papers to fetch per topic per database (default: 50)')
    args = parser.parse_args()

    # Parse topics
    if args.topics:
        topics = [t.strip() for t in args.topics.split(',') if t.strip()]
    else:
        topics = DEFAULT_TOPICS

    # Date range
    to_date = datetime.now()
    if args.to_date:
        to_date = datetime.strptime(args.to_date, '%Y-%m-%d')

    if args.from_date:
        from_date = datetime.strptime(args.from_date, '%Y-%m-%d')
    else:
        weeks_back = args.weeks_back if args.weeks_back is not None else 1
        from_date = to_date - timedelta(weeks=weeks_back)

    from_str = from_date.strftime('%Y-%m-%d')
    to_str = to_date.strftime('%Y-%m-%d')
    year_from = from_date.year
    year_to = to_date.year

    logger.info(f"Literature Search: {from_str} to {to_str}")
    logger.info(f"Topics: {', '.join(topics)}")
    logger.info(f"Max per topic per DB: {args.max_per_topic}")

    # Initialize search clients
    s2 = SemanticScholarSearch(api_key=SEMANTIC_SCHOLAR_API_KEY)
    openalex = OpenAlexSearch()

    # Search across all topics
    all_papers = []
    for topic in topics:
        logger.info(f"Searching topic: '{topic}'")
        s2_papers = s2.search_papers(topic, year_from, year_to, limit=args.max_per_topic)
        oa_papers = openalex.search_papers(topic, from_str, to_str, limit=args.max_per_topic)
        all_papers.extend(s2_papers)
        all_papers.extend(oa_papers)

    logger.info(f"Total papers before dedup: {len(all_papers)}")

    # Deduplicate
    unique_papers = deduplicate_papers(all_papers)
    logger.info(f"Unique papers after dedup: {len(unique_papers)}")

    # Sort by citation count (most cited first)
    unique_papers.sort(key=lambda p: p.get('citation_count', 0), reverse=True)

    # Clean abstracts
    for paper in unique_papers:
        paper['abstract'] = clean_abstract(paper.get('abstract', ''))

    # Output
    if args.output_format == 'json':
        result = {
            'search_date': datetime.now().strftime('%Y-%m-%d'),
            'date_range': {'from': from_str, 'to': to_str},
            'topics_searched': topics,
            'total_before_dedup': len(all_papers),
            'total_unique': len(unique_papers),
            'papers': [
                {
                    'doi': p.get('doi', ''),
                    'title': p.get('title', ''),
                    'authors': p.get('authors', []),
                    'journal': p.get('journal', ''),
                    'publication_date': p.get('publication_date', ''),
                    'abstract': p.get('abstract', ''),
                    'citation_count': p.get('citation_count', 0),
                    'fields_of_study': p.get('fields_of_study', []),
                    'matched_queries': p.get('matched_queries', []),
                    'source_databases': p.get('source_databases', []),
                    's2_paper_id': p.get('s2_paper_id', ''),
                }
                for p in unique_papers
            ],
        }
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        # Simple markdown list
        print(f"# Literature Search Results\n")
        print(f"**Date Range:** {from_str} to {to_str}")
        print(f"**Topics:** {', '.join(topics)}")
        print(f"**Papers Found:** {len(unique_papers)} (from {len(all_papers)} total)\n")
        print("---\n")

        for i, paper in enumerate(unique_papers, 1):
            title = paper.get('title', 'No title')
            doi = paper.get('doi', '')
            journal = paper.get('journal', 'Unknown')
            citations = paper.get('citation_count', 0)
            queries = ', '.join(paper.get('matched_queries', []))

            print(f"### {i}. {title}\n")
            print(f"**Journal:** {journal} | **Citations:** {citations}")
            print(f"**DOI:** [{doi}](https://doi.org/{doi})")
            print(f"**Matched Topics:** {queries}")

            abstract = paper.get('abstract', '')
            if abstract:
                if len(abstract) > 500:
                    abstract = abstract[:500] + "..."
                print(f"\n{abstract}")
            print("\n---\n")


if __name__ == "__main__":
    main()

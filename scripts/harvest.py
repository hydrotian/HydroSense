#!/usr/bin/env python3
"""
Standalone Paper Harvester

Fetches papers from tracked journals and classifies them using a three-tier priority system:

Part 1 (Highest Priority): Top-tier journals + Topic keywords + Peer-reviewed
  • Must be peer-reviewed research articles (journal-article type)
  • Must match TOPICS in title/abstract
  • Gets abstracts from S2/OpenAlex

Part 2: High-impact journals + Topic keywords + Peer-reviewed
  • Must be peer-reviewed research articles
  • Must match TOPICS in title/abstract

Part 3 (Field Awareness): Top-tier journals + Field match only
  • Must match RELEVANT_FIELDS (S2 classification)
  • Allows all content types (news, editorials, research)

Output: Markdown report saved to <project_directory>/harvest_<date>.md

Usage:
    python harvest.py                      # Default: 30 days ago
    python harvest.py --date 2026-01-13  # Specific date
    python harvest.py --backfill          # Next backfill date (from counter file)
"""

import argparse
import logging
import os
from datetime import datetime, timedelta
import sys
from typing import List, Dict, Optional
import requests
import time

# Load API keys from .env file (not committed to git)
from dotenv import load_dotenv
load_dotenv()

# API Keys (from environment variables)
SEMANTIC_SCHOLAR_API_KEY = os.getenv('SEMANTIC_SCHOLAR_API_KEY')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
CROSSREF_EMAIL = os.getenv('CROSSREF_EMAIL')

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


# Backfill counter file
BACKFILL_COUNTER_FILE = os.path.join(os.path.dirname(__file__), '.backfill_counter')
BACKFILL_START_DATE = datetime(2020, 1, 1)


def get_next_backfill_date():
    """Get the next backfill date from counter file."""
    if os.path.exists(BACKFILL_COUNTER_FILE):
        with open(BACKFILL_COUNTER_FILE, 'r') as f:
            days_offset = int(f.read().strip())
    else:
        days_offset = 0
    
    next_date = BACKFILL_START_DATE + timedelta(days=days_offset)
    return next_date.strftime('%Y-%m-%d'), days_offset


def increment_backfill_counter():
    """Increment the backfill counter after successful harvest."""
    if os.path.exists(BACKFILL_COUNTER_FILE):
        with open(BACKFILL_COUNTER_FILE, 'r') as f:
            days_offset = int(f.read().strip())
    else:
        days_offset = 0
    
    with open(BACKFILL_COUNTER_FILE, 'w') as f:
        f.write(str(days_offset + 1))
    
    logger.info(f"Backfill counter incremented to {days_offset + 1}")


# Tracked journals (from FieldSense config)
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
          "seasonal", "land surface model", "climate change", "hydropower", "surface water", "irrigation", "earth system model"]

# Relevant Semantic Scholar fields for filtering
# Based on official S2 taxonomy: https://api.semanticscholar.org/api-docs/
RELEVANT_FIELDS = [
    'engineering',
    'environmental science',
    'computer science',
    'geology',
    'geography'
]

class CrossRefClient:
    """Simplified CrossRef API client."""

    def __init__(self, email: str = None):
        self.base_url = "https://api.crossref.org"
        self.session = requests.Session()
        if email:
            self.session.headers.update({'User-Agent': f'LunaPaperHarvester/1.0 (mailto:{email})'})
        else:
            self.session.headers.update({'User-Agent': 'LunaPaperHarvester/1.0'})
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

            # Date
            pub_date = None
            if 'published' in item:
                parts = item['published'].get('date-parts', [[]])[0]
                if len(parts) >= 3:
                    pub_date = f"{parts[0]:04d}-{parts[1]:02d}-{parts[2]:02d}"

            # Title
            title = item.get('title', [None])[0]

            # Authors
            authors = []
            for a in item.get('author', []):
                name = f"{a.get('given', '')} {a.get('family', '')}".strip()
                if name:
                    authors.append(name)

            # Journal
            journal = item.get('container-title', [None])[0]

            # Abstract (often not available)
            abstract = item.get('abstract', '')

            # Type (journal-article, news, editorial, etc.)
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
        except Exception as e:
            return None


class OpenAlexClient:
    """OpenAlex API client for abstract retrieval."""

    def __init__(self):
        self.base_url = "https://api.openalex.org"
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'LunaPaperHarvester/1.0 (mailto:hydro.luna.bot@gmail.com)'})
        self.rate_limit_delay = 0.1

    def get_abstract(self, doi: str) -> str:
        """Get abstract for a paper by DOI."""
        try:
            url = f"{self.base_url}/works/doi:{doi}"
            response = self.session.get(url, timeout=15)

            if response.status_code == 200:
                data = response.json()
                # OpenAlex stores abstract in inverted index format, need to reconstruct
                abstract_inverted = data.get('abstract_inverted_index')
                if abstract_inverted:
                    # Reconstruct abstract from inverted index
                    words = [''] * 1000  # Allocate space
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


class SemanticScholarClient:
    """Simplified Semantic Scholar client for paper metadata."""

    def __init__(self, api_key: str = None):
        self.base_url = "https://api.semanticscholar.org/graph/v1/paper"
        self.session = requests.Session()
        self.session.headers.update({'User-Agent': 'LunaPaperHarvester/1.0'})
        self.api_key = api_key
        if api_key:
            self.session.headers.update({'x-api-key': api_key})
        # Rate limit: 1 req/sec - use 1.5 sec to be safe with network latency and timing variations
        self.rate_limit_delay = 1.5


class GeminiClient:
    """Gemini API client for binary relevance classification (Stage 1 LLM filtering)."""

    def __init__(self, api_key: str = None):
        self.api_key = api_key or GEMINI_API_KEY
        self.base_url = "https://generativelanguage.googleapis.com/v1beta"
        self.model = "gemini-2.0-flash-lite"
        self.rate_limit_delay = 4.0  # 15 requests/minute = 4s between requests

    def generate_daily_summary(self, papers: List[Dict]) -> str:
        """
        Generate a brief AI summary of the day's harvested papers.

        Uses Gemini 2.5 Flash Lite for fast, cost-effective summarization.

        Args:
            papers: List of Part 1 + Part 2 paper dicts with 'title' and 'abstract' keys

        Returns:
            A summary paragraph string, or empty string on failure.
        """
        if not self.api_key or not papers:
            return ''

        # Build paper descriptions for the prompt
        paper_descriptions = []
        for p in papers[:30]:  # Cap at 30 papers to stay within token limits
            title = p.get('title', 'Untitled')
            abstract = p.get('abstract', '')
            if abstract:
                abstract = abstract[:300]
            paper_descriptions.append(f"- {title}: {abstract}")

        papers_text = "\n".join(paper_descriptions)

        prompt = f"""You are a hydrology research assistant. Summarize the key themes and highlights from today's harvested papers in 1 short paragraph (3-5 sentences). Focus on the major research themes, notable findings, and any emerging trends. Write in a concise, informative style suitable for a daily research briefing.

Today's papers:
{papers_text}

Write only the summary paragraph, no headers or bullet points."""

        try:
            summary_model = "gemini-2.5-flash-lite"
            url = f"{self.base_url}/models/{summary_model}:generateContent"
            params = {'key': self.api_key}

            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }],
                "generationConfig": {
                    "temperature": 0.3,
                    "maxOutputTokens": 300
                }
            }

            response = requests.post(url, params=params, json=payload, timeout=30)
            response.raise_for_status()

            data = response.json()
            text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')

            time.sleep(self.rate_limit_delay)
            return text.strip()

        except Exception as e:
            logger.warning(f"Gemini summary generation failed: {e}")
            return ''

    def is_relevant(self, title: str, abstract: str, journal: str) -> Dict:
        """
        Determine if a paper is relevant to hydrology research using LLM classification.

        Returns:
            Dict with 'relevant' (bool), 'confidence' (float), 'reason' (str)
        """
        if not self.api_key:
            logger.warning("No Gemini API key configured, skipping LLM check")
            return {'relevant': True, 'confidence': 0.5, 'reason': 'No API key'}

        prompt = f"""You are a hydrology research assistant. Determine if this paper is relevant.

RESEARCHER'S DOMAIN:
- E3SM Earth system modeling
- MOSART river routing
- Reservoirs and dams
- Water management
- Hydrologic connectivity
- Land-river coupling
- Surface hydrology
- Streamflow and runoff modeling

RELEVANT TOPICS:
- Hydrology and water resources
- River/reservoir operations
- Flood and drought modeling
- Land surface hydrology
- Water management infrastructure
- Climate impacts on water
- Earth system models

IRRELEVANT (unless hydrology-focused):
- Pure atmospheric science (no water focus)
- Marine/ocean-only studies
- Medical/biochemistry
- Pure ecology without water connection
- Agriculture without water resources focus

PAPER TO EVALUATE:
Title: {title}
Abstract: {abstract[:1500]}
Journal: {journal}

OUTPUT (JSON only, no markdown):
{{"relevant": true/false, "confidence": 0.0-1.0, "reason": "brief explanation"}}"""

        try:
            url = f"{self.base_url}/models/{self.model}:generateContent"
            params = {'key': self.api_key}

            payload = {
                "contents": [{
                    "parts": [{"text": prompt}]
                }],
                "generationConfig": {
                    "temperature": 0.1,
                    "maxOutputTokens": 100
                }
            }

            response = requests.post(url, params=params, json=payload, timeout=30)
            response.raise_for_status()

            data = response.json()
            text = data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')

            # Parse JSON from response
            import json
            text = text.strip().replace('```json', '').replace('```', '')
            result = json.loads(text)

            # Clean up reason
            result['reason'] = result.get('reason', '').strip()

            time.sleep(self.rate_limit_delay)
            return result

        except Exception as e:
            logger.warning(f"Gemini API error: {e}")
            return {'relevant': True, 'confidence': 0.5, 'reason': f'API error: {str(e)[:50]}'}


def format_journal_list(all_papers: List[Dict], selected_papers: List[Dict]) -> str:
    """Create a text-based journal list with paper counts."""
    # Count papers by journal
    journal_total = {}
    journal_selected = {}

    # Count all papers
    for paper in all_papers:
        journal = paper.get('journal_name', 'Unknown')
        journal_total[journal] = journal_total.get(journal, 0) + 1

    # Count selected papers
    for paper in selected_papers:
        journal = paper.get('journal_name', 'Unknown')
        journal_selected[journal] = journal_selected.get(journal, 0) + 1

    # Filter journals that have at least one paper
    journals = [j for j in journal_total.keys() if journal_total[j] > 0]

    # Sort by total papers (descending)
    journals.sort(key=lambda x: journal_total[x], reverse=True)

    # Find maximum journal name length for alignment
    max_name_length = 50  # Fixed width for journal names

    # Build the list
    lines = []
    for journal in journals:
        total = journal_total[journal]
        selected = journal_selected.get(journal, 0)

        # Trim journal name to fixed length
        if len(journal) > max_name_length:
            journal_display = journal[:max_name_length-3] + "..."
        else:
            journal_display = journal.ljust(max_name_length)

        # Format the count
        count_display = f"({selected}/{total})"

        lines.append(f"{journal_display} {count_display}")

    return "\n".join(lines)


def format_paper(paper: Dict) -> str:
    """Format a single paper for markdown output."""
    lines = []

    # Title
    title = paper.get('title') or 'No title'
    lines.append(f"### {title}")
    lines.append("")

    # Authors
    authors = paper.get('authors', [])
    if authors:
        author_str = ", ".join(authors[:5])
        if len(authors) > 5:
            author_str += f" et al. ({len(authors)} authors)"
        lines.append(f"**Authors:** {author_str}")

    # Journal and date
    journal = paper.get('journal', 'Unknown journal')
    category = paper.get('category', '')
    tier_marker = " ⭐" if category == 'top-tier' else ""
    date = paper.get('publication_date', 'No date')
    lines.append(f"**Journal:** {journal}{tier_marker} ({date})")

    # Content type (show if not a regular journal article)
    content_type = paper.get('type', 'unknown')
    if content_type != 'journal-article':
        type_display = content_type.replace('-', ' ').title()
        lines.append(f"**Content Type:** {type_display}")

    # DOI
    doi = paper.get('doi', '')
    lines.append(f"**DOI:** [{doi}](https://doi.org/{doi})")

    # Show why this paper was selected
    matched_fields = paper.get('matched_fields', [])
    matched_topics = paper.get('matched_topics', [])
    if matched_topics or matched_fields:
        lines.append("")
        if matched_topics:
            lines.append(f"**Matched Topics:** {', '.join(matched_topics)}")
        if matched_fields:
            lines.append(f"**Matched Fields:** {', '.join(matched_fields)}")

    # Abstract - always show if available (provides context when no recommendations)
    abstract = paper.get('abstract')
    if abstract:
        # Clean XML tags
        abstract = str(abstract).replace('<jats:p>', '').replace('</jats:p>', '')
        abstract = abstract.replace('<jats:title>', '').replace('</jacs:title>', '')
        abstract = abstract.replace('<jats:italic>', '*').replace('</jats:italic>', '*')
        # Truncate if too long
        if len(abstract) > 800:
            abstract = abstract[:800] + "..."
        lines.append(f"\n**Abstract:**\n\n{abstract}")
    else:
        # If no abstract available, note it
        lines.append(f"\n*Abstract not available*")

    return "\n".join(lines)


def main():
    """Main harvester logic."""
    
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Paper Harvester')
    parser.add_argument('--date', type=str, help='Specific date to harvest (YYYY-MM-DD)')
    parser.add_argument('--backfill', action='store_true', help='Run backfill for next date')
    parser.add_argument('--no-increment', action='store_true', help='Do not increment backfill counter')
    args = parser.parse_args()

    # ============================================================
    # DATE RANGE CONFIGURATION
    # ============================================================
    if args.date:
        # Specific date provided
        from_str = args.date
        until_str = args.date
    elif args.backfill:
        # Backfill mode - get next date from counter
        from_str, _ = get_next_backfill_date()
        until_str = from_str
    else:
        # Default: 30 days ago
        from_str = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')
        until_str = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

    # ============================================================

    print(f"\n{'='*70}")
    print(f"📚 Paper Harvest: {from_str} to {until_str}")
    print(f"{'='*70}\n")

    # Initialize clients
    crossref = CrossRefClient(email="hydro.luna.bot@gmail.com")
    openalex = OpenAlexClient()

    # S2 enrichment with API key
    try:
        if SEMANTIC_SCHOLAR_API_KEY:
            s2 = SemanticScholarClient(api_key=SEMANTIC_SCHOLAR_API_KEY)
            s2_available = True
            masked_key = f"...{SEMANTIC_SCHOLAR_API_KEY[-8:]}" if len(SEMANTIC_SCHOLAR_API_KEY) > 8 else "***"
            print(f"\n🔑 Semantic Scholar API Configuration:")
            print(f"   Key: {masked_key}")
        print(f"   Rate limit: {s2.rate_limit_delay}s delay between requests (conservative)")
        print(f"   x-api-key header: {'x-api-key' in s2.session.headers}\n")
    except Exception as e:
        s2_available = False
        print(f"\n⚠️  Semantic Scholar not available: {e}\n")

    # Gemini LLM configuration
    if GEMINI_API_KEY:
        print(f"🔑 Gemini API Configuration:")
        print(f"   Model: gemini-2.5-flash-lite")
        print(f"   Rate limit: 4s delay between requests")
        gemini_available = True
    else:
        print(f"⚠️  Gemini API not configured (set GEMINI_API_KEY in .env)")
        gemini_available = False
    print()

    all_papers = []

    # Fetch from each journal
    for journal in JOURNALS:
        issn = journal['issn']
        name = journal['name']
        category = journal['category']

        papers = crossref.get_papers(issn, from_str, until_str)

        for paper in papers:
            paper['journal_name'] = name
            paper['category'] = category
            all_papers.append(paper)

    logger.info(f"\nTotal papers fetched from CrossRef: {len(all_papers)}")

    # Three-tier classification with S2
    if s2_available:
        logger.info("\nApplying three-tier classification:")
        logger.info("  Part 1: Top-tier + topics (with recommendations)")
        logger.info("  Part 2: High-impact + topics (no recommendations)")
        logger.info("  Part 3: Top-tier + fields only (no recommendations)\n")

        part1_papers = []  # Top-tier + topics
        part2_papers = []  # High-impact + topics
        part3_papers = []  # Top-tier + fields only

        # Track S2 status
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

                # Always sleep after S2 request to respect rate limit
                time.sleep(s2.rate_limit_delay)

                if response.status_code == 200:
                    s2_found += 1
                    data = response.json()
                elif response.status_code == 429:
                    # Rate limited - wait and skip
                    s2_errors += 1
                    logger.warning(f"  ⚠ Rate limited by S2 - waiting 5 seconds then continuing...")
                    time.sleep(5)
                    logger.info(f"  ✗ Skipping this paper due to rate limit")
                    continue
                elif response.status_code == 404:
                    s2_not_found += 1
                    logger.info(f"  ✗ Not in S2 (404 - paper not indexed)")
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

            # Get title and abstract from S2 (more complete than CrossRef)
            s2_title = data.get('title') or title
            s2_abstract = data.get('abstract') or paper.get('abstract', '')
            content = (s2_title + " " + s2_abstract).lower()
            matched_topics = [t for t in TOPICS if t.lower() in content]

            # Store S2 data back to paper
            paper['s2_paper_id'] = data.get('paperId')
            paper['matched_fields'] = matched_fields
            paper['matched_topics'] = matched_topics
            # Update abstract - try S2 first, then OpenAlex fallback
            if s2_abstract:
                paper['abstract'] = s2_abstract
                paper['abstract_source'] = 'S2'
                logger.debug(f"  Abstract from S2 ({len(s2_abstract)} chars)")
            else:
                # Try OpenAlex as fallback
                logger.debug(f"  No S2 abstract, trying OpenAlex...")
                openalex_abstract = openalex.get_abstract(doi)
                if openalex_abstract:
                    paper['abstract'] = openalex_abstract
                    paper['abstract_source'] = 'OpenAlex'
                    logger.debug(f"  Abstract from OpenAlex ({len(openalex_abstract)} chars)")
                elif paper.get('abstract'):
                    # Keep CrossRef abstract if we have it
                    paper['abstract_source'] = 'CrossRef'
                    logger.debug(f"  Using CrossRef abstract")
                else:
                    paper['abstract_source'] = 'None'
                    logger.debug(f"  No abstract available")

            # Three-tier classification
            paper_type = paper.get('type', 'unknown')
            is_peer_reviewed = paper_type == 'journal-article'

            if is_top_tier and matched_topics and is_peer_reviewed:
                # Stage 1: Gemini LLM binary relevance check
                gemini = GeminiClient()
                llm_result = gemini.is_relevant(
                    s2_title,
                    s2_abstract,
                    paper.get('journal', journal)
                )

                # Log LLM decision
                llm_status = "✅ RELEVANT" if llm_result.get('relevant') else "❌ NOT RELEVANT"
                logger.info(f"  🤖 Gemini: {llm_status} ({llm_result.get('confidence', 0):.2f}) - {llm_result.get('reason', '')[:50]}")

                # Only include if LLM says relevant
                if not llm_result.get('relevant', True):
                    logger.info(f"  ✗ Rejected by Gemini LLM")
                    continue

                # Part 1: Top-tier + topics + peer-reviewed ONLY
                paper['llm_result'] = llm_result
                part1_papers.append(paper)
                logger.info(f"  ⭐ PART 1: Top-tier + topics: {', '.join(matched_topics[:2])}")
            elif not is_top_tier and matched_topics and is_peer_reviewed:
                # Stage 1: Gemini LLM binary relevance check (Part 2)
                gemini = GeminiClient()
                llm_result = gemini.is_relevant(
                    s2_title,
                    s2_abstract,
                    paper.get('journal', journal)
                )

                # Log LLM decision
                llm_status = "✅ RELEVANT" if llm_result.get('relevant') else "❌ NOT RELEVANT"
                logger.info(f"  🤖 Gemini: {llm_status} ({llm_result.get('confidence', 0):.2f}) - {llm_result.get('reason', '')[:50]}")

                # Only include if LLM says relevant
                if not llm_result.get('relevant', True):
                    logger.info(f"  ✗ Rejected by Gemini LLM")
                    continue

                # Part 2: High-impact + topics + peer-reviewed ONLY
                paper['llm_result'] = llm_result
                part2_papers.append(paper)
                logger.info(f"  ✓ PART 2: High-impact + topics: {', '.join(matched_topics[:2])}")
            elif is_top_tier and matched_fields:
                # Part 3: Top-tier + fields (allows news/editorials for awareness)
                part3_papers.append(paper)
                type_label = f" [{paper_type}]" if paper_type != 'journal-article' else ""
                logger.info(f"  ○ PART 3: Top-tier + fields: {', '.join(matched_fields[:2])}{type_label}")
            elif is_top_tier and matched_topics and not is_peer_reviewed:
                # Rejected: Top-tier + topics but not peer-reviewed
                logger.info(f"  ✗ Rejected: {paper_type} (not peer-reviewed)")
            elif not is_top_tier and matched_topics and not is_peer_reviewed:
                # Rejected: High-impact + topics but not peer-reviewed
                logger.info(f"  ✗ Rejected: {paper_type} (not peer-reviewed)")
            else:
                logger.info(f"  ✗ Rejected: No match")

        logger.info(f"\n📊 Classification Results:")
        logger.info(f"   Part 1 (Top-tier + topics): {len(part1_papers)}")
        logger.info(f"   Part 2 (High-impact + topics): {len(part2_papers)}")
        logger.info(f"   Part 3 (Top-tier + fields only): {len(part3_papers)}")
        logger.info(f"   Total selected: {len(part1_papers) + len(part2_papers) + len(part3_papers)}/{len(all_papers)}")

        logger.info(f"\n📈 Semantic Scholar Coverage:")
        s2_coverage = (s2_found/len(all_papers)*100) if len(all_papers) > 0 else 0
        logger.info(f"   Found in S2: {s2_found} ({s2_coverage:.1f}%)")
        logger.info(f"   Not in S2 (404): {s2_not_found}")
        logger.info(f"   Errors/Rate limits: {s2_errors}\n")

        relevant_papers = {'part1': part1_papers, 'part2': part2_papers, 'part3': part3_papers}
    else:
        logger.warning("Semantic Scholar not available - skipping filtering")
        relevant_papers = {'part1': [], 'part2': all_papers, 'part3': []}
        # Set default S2 stats
        s2_found = 0
        s2_not_found = 0
        s2_errors = 0

    # Output
    part1 = relevant_papers.get('part1', [])
    part2 = relevant_papers.get('part2', [])
    part3 = relevant_papers.get('part3', [])
    total = len(part1) + len(part2) + len(part3)

    # Generate AI summary from Part 1 + Part 2 papers
    daily_summary = ''
    if gemini_available and (part1 or part2):
        logger.info("Generating AI daily summary with Gemini 2.5 Flash Lite...")
        gemini = GeminiClient()
        daily_summary = gemini.generate_daily_summary(part1 + part2)
        if daily_summary:
            logger.info(f"  Summary generated ({len(daily_summary)} chars)")
        else:
            logger.warning("  Summary generation failed or returned empty")

    # Count papers with abstracts
    all_selected = part1 + part2 + part3
    papers_with_abstract = sum(1 for p in all_selected if p.get('abstract'))

    print(f"\n{'='*70}")
    print(f"📋 Papers Selected: {total}")
    print(f"   Part 1 (Top-tier + topics): {len(part1)}")
    print(f"   Part 2 (High-impact + topics): {len(part2)}")
    print(f"   Part 3 (Top-tier + fields): {len(part3)}")
    print(f"   Papers with abstracts: {papers_with_abstract}/{total}")
    print(f"{'='*70}\n")

    if total == 0:
        print("No papers passed the three-tier filter.")
        print(f"\nTotal fetched: {len(all_papers)}")
        print(f"Journals searched: {len(JOURNALS)}")
        print(f"Relevant fields: {', '.join(RELEVANT_FIELDS)}")
        print(f"Topics: {', '.join(TOPICS)}")
    else:
        print("\n=== PART 1: TOP-TIER + TOPICS (with recommendations) ===\n")
        for i, paper in enumerate(part1, 1):
            print(f"\n--- Paper {i}/{len(part1)} ---")
            print(format_paper(paper))

        if part2:
            print("\n\n=== PART 2: HIGH-IMPACT + TOPICS ===\n")
            for i, paper in enumerate(part2, 1):
                print(f"\n--- Paper {i}/{len(part2)} ---")
                print(format_paper(paper))

        if part3:
            print("\n\n=== PART 3: TOP-TIER + FIELDS ONLY ===\n")
            for i, paper in enumerate(part3, 1):
                print(f"\n--- Paper {i}/{len(part3)} ---")
                print(format_paper(paper))

    # Save to file (Jekyll format)
    # Get project directory (where harvest.py is located)
    project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Determine post category
    month_name = datetime.strptime(until_str, '%Y-%m-%d').strftime('%B')
    month_num = datetime.strptime(until_str, '%Y-%m-%d').strftime('%m')
    year = until_str[:4]

    # Create Jekyll post path (nested folder structure: _pages/2025/january/)
    month_folder = month_name.lower()
    posts_dir = f"{project_dir}/_pages/{year}/{month_folder}"
    os.makedirs(posts_dir, exist_ok=True)

    # Create year index page if it doesn't exist
    year_index = f"{project_dir}/_pages/{year}/index.md"
    if not os.path.exists(year_index):
        # nav_order: use last 2 digits so 2025->25, 2026->26, etc.
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

    # Create month index page if it doesn't exist
    month_index = f"{posts_dir}/index.md"
    if not os.path.exists(month_index):
        # Determine month order (1-12)
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
            f.write(f"Daily harvest reports and monthly summary for {month_name} {year}.\n")

    # Jekyll post filename
    post_file = f"{posts_dir}/{until_str}-daily-harvest.md"

    # Get day for title
    day = datetime.strptime(until_str, '%Y-%m-%d').day

    # Write Jekyll post with front matter
    with open(post_file, 'w', encoding='utf-8') as f:
        # Front matter for just-the-docs theme
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

        # Summary statistics (computed here, used below)
        selection_pct = (total/len(all_papers)*100) if len(all_papers) > 0 else 0
        abstract_pct = (papers_with_abstract/total*100) if total > 0 else 0
        s2_coverage = (s2_found/len(all_papers)*100) if len(all_papers) > 0 else 0

        # One-line selection count
        f.write(f"**{len(part1)}** top-tier and **{len(part2)}** high-impact papers were selected out of **{len(all_papers)}** total publications ({selection_pct:.1f}%).\n\n")

        # AI-generated summary
        if daily_summary:
            f.write(f"## Today's Highlights\n\n")
            f.write(f"{daily_summary}\n\n")

        f.write("---\n\n")

        # Part 1
        if part1:
            f.write(f"# Part 1: Top-Tier Journals + Topic Match ({len(part1)} papers)\n\n")
            f.write("*Peer-reviewed research articles from top-tier journals that match your research topics.*\n\n")
            for i, paper in enumerate(part1, 1):
                f.write(format_paper(paper))
                f.write("\n\n---\n\n")

        # Part 2
        if part2:
            f.write(f"# Part 2: High-Impact Journals + Topic Match ({len(part2)} papers)\n\n")
            f.write("*Peer-reviewed research articles from high-impact journals that match your topics.*\n\n")
            for i, paper in enumerate(part2, 1):
                f.write(format_paper(paper))
                f.write("\n\n---\n\n")

        # Statistics at the bottom
        f.write("---\n\n")
        f.write(f"## Statistics\n\n")
        f.write(f"- **Papers Published:** {len(all_papers)} (research articles from tracked journals)\n")
        f.write(f"- **Papers Selected:** {total} ({selection_pct:.1f}%)\n")
        f.write(f"- **Papers with Abstracts:** {papers_with_abstract}/{total} ({abstract_pct:.1f}%)\n")
        f.write(f"- **Semantic Scholar Coverage:** {s2_found}/{len(all_papers)} ({s2_coverage:.1f}%)\n")
        f.write(f"  - Not in S2: {s2_not_found} papers (404 errors are normal for non-indexed content)\n\n")

        # Journal list with counts
        f.write(f"### Papers by Journal\n\n")
        f.write(f"```\n")
        f.write(format_journal_list(all_papers, all_selected))
        f.write(f"\n```\n\n")
        f.write(f"*Format: Journal Name (selected/published)*\n\n")

        # Breakdown
        f.write(f"### Selection Breakdown\n\n")
        f.write(f"- Part 1 (Top-tier + topics): {len(part1)}\n")
        f.write(f"- Part 2 (High-impact + topics): {len(part2)}\n\n")

        # Filtering criteria
        f.write(f"### Filtering Criteria\n\n")
        f.write(f"**Relevant Fields:** {', '.join(RELEVANT_FIELDS)}\n\n")
        f.write(f"**Topics:** {', '.join(TOPICS)}\n\n")

    print(f"\n\n📁 Jekyll post saved to: {post_file}")
    print(f"🌐 Blog URL: https://hydrotian.github.io/hydrosense/{year}/{month_name.lower()}/{until_str}-daily-harvest.html")

    # Increment backfill counter if in backfill mode
    if args.backfill and not args.no_increment:
        increment_backfill_counter()


if __name__ == "__main__":
    main()

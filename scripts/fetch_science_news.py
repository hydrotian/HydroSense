#!/usr/bin/env python3
"""
Science News RSS Aggregator for HydroSense

Fetches recent items from curated science-news and AI-lab RSS feeds.
Outputs normalized JSON for LLM filtering / dedup / bucketing in the
science-news skill.

Source types:
  - editorial: Nature News, Science Magazine — written about peer-reviewed
    work, so they may cite DOIs that the downstream skill can extract and
    feed into the existing CrossRef + S2 enrichment.
  - tech-news: Ars Technica, MIT Tech Review, Quanta — surfaced by URL only.
  - ai-lab-blog: DeepMind, Anthropic, OpenAI — surfaced by URL only.

Usage:
    python fetch_science_news.py                       # Last 1 day
    python fetch_science_news.py --days-back 7         # Last week
    python fetch_science_news.py --sources nature-news,science-news
    python fetch_science_news.py --list-sources
"""

import argparse
import json
import logging
import sys
import time
from datetime import datetime, timedelta, timezone
from typing import Dict, List, Optional

import feedparser
import requests

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    stream=sys.stderr,
)
logger = logging.getLogger(__name__)


# Curated RSS sources.
#
# AI-lab blog URLs change occasionally as companies rebuild their sites; the
# script logs and skips broken feeds rather than failing the whole run, so
# stale entries here are recoverable.
SOURCES = [
    # Nature: journal-wide feed mixes news (d41586-*) and research (s41586-*).
    # The downstream skill keeps news for narrative + cites and lets research
    # items flow into the existing harvest pipeline.
    {"id": "nature",         "name": "Nature",               "type": "editorial",  "url": "https://www.nature.com/nature.rss"},
    # Cross-journal subject feed for ML; catches AI work in NMI, Nat Comms, etc.
    {"id": "nature-ml",      "name": "Nature: Machine Learning", "type": "editorial", "url": "https://www.nature.com/subjects/machine-learning.rss"},
    # Science Magazine news
    {"id": "science-news",   "name": "Science News",         "type": "editorial",  "url": "https://www.science.org/rss/news_current.xml"},
    # Industry tech press
    {"id": "ars-science",    "name": "Ars Technica Science", "type": "tech-news",  "url": "https://feeds.arstechnica.com/arstechnica/science"},
    {"id": "mit-tr",         "name": "MIT Tech Review",      "type": "tech-news",  "url": "https://www.technologyreview.com/feed/"},
    {"id": "quanta",         "name": "Quanta Magazine",      "type": "tech-news",  "url": "https://api.quantamagazine.org/feed/"},
    # AI lab blogs. Anthropic has no public RSS (checked 2026-05) — add if/when
    # they ship one. DeepMind and OpenAI URLs occasionally rotate; bad feeds
    # log a warning and don't fail the run.
    {"id": "deepmind",       "name": "Google DeepMind",      "type": "ai-lab-blog","url": "https://deepmind.google/blog/rss.xml"},
    {"id": "openai",         "name": "OpenAI Blog",          "type": "ai-lab-blog","url": "https://openai.com/news/rss.xml"},
]


def parse_published_date(entry) -> Optional[datetime]:
    """Pull a UTC datetime from whichever date field the feed provides."""
    for attr in ('published_parsed', 'updated_parsed', 'created_parsed'):
        t = getattr(entry, attr, None)
        if t:
            return datetime(*t[:6], tzinfo=timezone.utc)
    return None


def normalize_entry(entry, source: Dict) -> Optional[Dict]:
    title = (entry.get('title') or '').strip()
    url = entry.get('link') or ''
    if not title or not url:
        return None

    summary = (entry.get('summary') or entry.get('description') or '').strip()
    published = parse_published_date(entry)

    return {
        'id': entry.get('id') or url,
        'source_id': source['id'],
        'source_name': source['name'],
        'source_type': source['type'],
        'title': title,
        'url': url,
        'summary': summary,
        'published': published.isoformat() if published else None,
    }


def fetch_source(source: Dict, timeout: int = 30) -> List[Dict]:
    logger.info(f"Fetching {source['name']}")
    try:
        resp = requests.get(
            source['url'],
            timeout=timeout,
            headers={'User-Agent': 'HydroSense/2.0 (science-news aggregator)'},
        )
        resp.raise_for_status()
        feed = feedparser.parse(resp.content)
    except Exception as e:
        logger.warning(f"  Failed: {e}")
        return []

    if feed.bozo and not feed.entries:
        logger.warning(f"  Feed parse error: {feed.bozo_exception}")
        return []

    entries = [n for e in feed.entries if (n := normalize_entry(e, source))]
    logger.info(f"  {len(entries)} entries")
    return entries


def filter_by_date(items: List[Dict], cutoff: datetime) -> List[Dict]:
    """Keep items at or after cutoff. Undated items are kept (some feeds
    legitimately omit pub dates; downstream dedup handles stragglers)."""
    kept = []
    for item in items:
        published = item.get('published')
        if not published or datetime.fromisoformat(published) >= cutoff:
            kept.append(item)
    return kept


def main():
    parser = argparse.ArgumentParser(description='Fetch science-news RSS feeds')
    parser.add_argument('--days-back', type=int, default=1,
                        help='Look back N days from now (default: 1)')
    parser.add_argument('--sources', type=str, default=None,
                        help='Comma-separated source ids to include (default: all)')
    parser.add_argument('--list-sources', action='store_true',
                        help='List configured sources and exit')
    args = parser.parse_args()

    if args.list_sources:
        for s in SOURCES:
            print(f"  {s['id']:18s} {s['type']:14s} {s['name']}")
        return

    sources = SOURCES
    if args.sources:
        wanted = {s.strip() for s in args.sources.split(',')}
        sources = [s for s in SOURCES if s['id'] in wanted]
        if not sources:
            logger.error(f"No sources matched: {wanted}")
            sys.exit(1)

    cutoff = datetime.now(timezone.utc) - timedelta(days=args.days_back)
    logger.info(f"Cutoff: {cutoff.isoformat()} ({args.days_back} day(s) back)")

    all_items = []
    for source in sources:
        all_items.extend(fetch_source(source))
        time.sleep(0.3)  # politeness between feeds

    kept = filter_by_date(all_items, cutoff)
    logger.info(f"Total: {len(all_items)} fetched, {len(kept)} within range")

    output = {
        'generated_at': datetime.now(timezone.utc).isoformat(),
        'cutoff': cutoff.isoformat(),
        'sources_polled': [s['id'] for s in sources],
        'item_count': len(kept),
        'items': kept,
    }
    print(json.dumps(output, indent=2, ensure_ascii=False))


if __name__ == '__main__':
    main()

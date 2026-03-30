#!/usr/bin/env python3
"""
Paper Registry for HydroSense

Tracks all papers seen across daily harvests, weekly reviews, and backfill runs.
Provides deduplication, importance scoring, and coverage tracking.

Registry file: data/paper_registry.json (committed to repo for persistence across Claude trigger runs)
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional

REGISTRY_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'paper_registry.json')


def _empty_registry() -> dict:
    return {"papers": {}, "runs": {}}


def load_registry() -> dict:
    """Load the paper registry from disk. Returns empty registry if file doesn't exist."""
    if not os.path.exists(REGISTRY_FILE):
        return _empty_registry()
    try:
        with open(REGISTRY_FILE, 'r', encoding='utf-8') as f:
            data = json.load(f)
        # Ensure required keys exist
        if 'papers' not in data:
            data['papers'] = {}
        if 'runs' not in data:
            data['runs'] = {}
        return data
    except (json.JSONDecodeError, IOError):
        return _empty_registry()


def save_registry(data: dict):
    """Save the paper registry to disk."""
    os.makedirs(os.path.dirname(REGISTRY_FILE), exist_ok=True)
    with open(REGISTRY_FILE, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def register_run(registry: dict, run_id: str, run_type: str, **metadata) -> dict:
    """Record a harvest/review run in the registry.

    Args:
        registry: The registry dict
        run_id: Unique run identifier (e.g., "daily-2026-03-29", "weekly-2026-W13")
        run_type: One of "daily", "weekly", "backfill"
        **metadata: Additional metadata (date, topics, month, etc.)
    """
    registry['runs'][run_id] = {
        'type': run_type,
        'timestamp': datetime.now().isoformat(),
        **metadata,
    }
    return registry


def register_papers(registry: dict, run_id: str, papers: List[Dict]) -> dict:
    """Register papers from a run in the registry.

    Args:
        registry: The registry dict
        run_id: The run identifier this batch came from
        papers: List of paper dicts (must have 'doi' key)

    Returns:
        Updated registry dict
    """
    today = datetime.now().strftime('%Y-%m-%d')

    for paper in papers:
        doi = paper.get('doi', '').strip()
        if not doi:
            continue

        if doi in registry['papers']:
            entry = registry['papers'][doi]
            entry['appearance_count'] += 1
            if run_id not in entry['sources']:
                entry['sources'].append(run_id)
            if entry['appearance_count'] >= 2:
                entry['important'] = True
        else:
            registry['papers'][doi] = {
                'title': paper.get('title', ''),
                'journal': paper.get('journal', paper.get('journal_name', '')),
                'first_seen': today,
                'sources': [run_id],
                'appearance_count': 1,
                'important': False,
            }

    return registry


def is_duplicate(registry: dict, doi: str, run_type: str) -> bool:
    """Check if a paper was already included in a post of the same run type.

    A paper in a daily harvest is not considered a duplicate if it also appeared
    in a weekly review (different run type). Only same-type duplicates are flagged.
    """
    if doi not in registry['papers']:
        return False

    entry = registry['papers'][doi]
    for source in entry['sources']:
        # Source IDs are formatted as "daily-YYYY-MM-DD", "weekly-YYYY-WNN", etc.
        source_type = source.split('-')[0]
        if source_type == run_type:
            return True

    return False


def get_cross_references(registry: dict, doi: str, current_run_type: str) -> List[str]:
    """Get cross-references for a paper from other run types.

    Returns list of run IDs where this paper appeared in a different run type.
    """
    if doi not in registry['papers']:
        return []

    entry = registry['papers'][doi]
    refs = []
    for source in entry['sources']:
        source_type = source.split('-')[0]
        if source_type != current_run_type:
            refs.append(source)
    return refs


def get_important_papers(registry: dict) -> List[Dict]:
    """Get all papers flagged as important (appeared in multiple sources)."""
    result = []
    for doi, entry in registry['papers'].items():
        if entry.get('important'):
            result.append({'doi': doi, **entry})
    return result


def get_run_history(registry: dict, run_type: Optional[str] = None) -> List[Dict]:
    """Get history of runs, optionally filtered by type."""
    runs = []
    for run_id, run_data in registry['runs'].items():
        if run_type is None or run_data.get('type') == run_type:
            runs.append({'run_id': run_id, **run_data})
    return sorted(runs, key=lambda r: r.get('timestamp', ''), reverse=True)


def get_stats(registry: dict) -> dict:
    """Get summary statistics from the registry."""
    total = len(registry['papers'])
    important = sum(1 for p in registry['papers'].values() if p.get('important'))
    runs = len(registry['runs'])
    run_types = {}
    for r in registry['runs'].values():
        t = r.get('type', 'unknown')
        run_types[t] = run_types.get(t, 0) + 1

    return {
        'total_papers': total,
        'important_papers': important,
        'total_runs': runs,
        'runs_by_type': run_types,
    }

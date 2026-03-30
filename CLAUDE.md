# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HydroSense is an intelligent paper harvesting tool for hydrology and water resources research. It operates in two modes:

- **Daily harvest**: Fetches papers from 11 top-tier journals via CrossRef, enriches with Semantic Scholar + OpenAlex, and applies deterministic filters (keywords, fields, peer-review). Claude provides LLM relevance filtering and summary generation via scheduled triggers.
- **Weekly literature review**: Keyword-based search across Semantic Scholar and OpenAlex (no journal limits), deduplicated and synthesized by Claude into thematic reviews.

Output is published as a Jekyll blog at [hydrosense.simhydro.com](https://hydrosense.simhydro.com).

## Development Commands

### Setup

```bash
pip install -r requirements.txt
cp .env.example .env   # then edit .env with API keys
```

### Running the Harvester

```bash
python scripts/harvest.py                                    # Default: last 30 days, top-tier only
python scripts/harvest.py --date 2026-01-15                  # Specific date
python scripts/harvest.py --journals all                     # All 29 journals
python scripts/harvest.py --output-format json               # JSON output for Claude triggers
python scripts/harvest.py --backfill                         # Next backfill month (from counter)
python scripts/harvest.py --backfill --backfill-start 2015-01-01  # Backfill from 2015
```

### Running the Weekly Review

```bash
python scripts/weekly_review.py                              # Last 7 days, default topics
python scripts/weekly_review.py --weeks-back 2               # Last 2 weeks
python scripts/weekly_review.py --topics "flood,reservoir"    # Custom topics
python scripts/weekly_review.py --output-format markdown     # Simple markdown list
```

### Local Blog Development

```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000/
```

### Testing

There is no automated test suite. Validate changes by running scripts with `--date` on a known date and inspecting the output.

## Architecture

### Scripts

**`scripts/harvest.py`** — Journal-based paper harvester.

- `CrossRefClient`: Fetches paper metadata by journal ISSN + date range
- `SemanticScholarClient`: Enriches with field classification and abstracts
- `OpenAlexClient`: Fallback abstract source
- `enrich_papers()`: Core enrichment + deterministic classification loop
- `output_json()` / `output_markdown()`: Two output paths
- Flags: `--journals {top-tier,high-impact,all}`, `--output-format {markdown,json}`, `--backfill`

**`scripts/weekly_review.py`** — Keyword-based literature search.

- `SemanticScholarSearch`: Keyword search via S2 Academic Graph API
- `OpenAlexSearch`: Keyword search via OpenAlex API
- `deduplicate_papers()`: Merges results by DOI across databases
- Outputs JSON sorted by citation count

**`scripts/registry.py`** — Paper registry for dedup and importance tracking.

- `load_registry()` / `save_registry()`: Read/write `data/paper_registry.json`
- `register_papers()`: Add DOIs, increment appearance counts
- `is_duplicate()`: Check if DOI already in a post of the same run type
- `get_cross_references()`: Find cross-references across run types
- `get_important_papers()`: Papers with `appearance_count >= 2`

### Paper Registry (`data/paper_registry.json`)

Tracks all DOIs across all runs (daily, weekly, backfill). Papers appearing in multiple sources are flagged as "important". The registry also records run history for coverage tracking.

### Claude Skills

- **`.claude/skills/daily-harvest/`**: Instructions for Claude to run harvest, evaluate relevance, generate Jekyll post, register papers, and create PR
- **`.claude/skills/weekly-review/`**: Instructions for Claude to run weekly search, synthesize thematically, generate post, register papers, and create PR

### Two-Tier Classification (harvest.py)

- **Part 1**: Top-tier journals + topic keywords + peer-reviewed (`journal-article` type)
- **Part 2**: High-impact journals + topic keywords + peer-reviewed

When run via Claude triggers, Claude adds LLM relevance filtering on top of the deterministic filters.

### Backfill System

- Counter file at `scripts/.backfill_counter` (gitignored) tracks months offset from `BACKFILL_START_DATE` (2020-01-01)
- Each `--backfill` run processes one full month
- `--backfill-start` overrides the start date for pre-2020 coverage
- Backfill always uses top-tier journals only

### Configuration

**API Keys** (via python-dotenv from `.env`):

- `SEMANTIC_SCHOLAR_API_KEY`: Required for field classification and weekly search (free at semanticscholar.org)
- `CROSSREF_EMAIL`: Optional, for faster CrossRef polite pool

**Key constants in `harvest.py`:**

- `JOURNALS`: 11 top-tier + 18 high-impact journals (ISSN, name, category)
- `TOPICS`: Keywords for topic-based filtering
- `RELEVANT_FIELDS`: Semantic Scholar field classifications

### Rate Limiting

Critical for API compliance — violating these causes 429 errors:

- CrossRef: 0.1s delay
- Semantic Scholar: 1.5s delay (most sensitive — 1 req/sec limit)
- OpenAlex: 0.1s delay

### Output

- **Daily posts**: `_pages/YYYY/monthname/YYYY-MM-DD-daily-harvest.md`
- **Weekly reviews**: `_pages/YYYY/monthname/YYYY-MM-DD-weekly-review.md`

Scripts auto-create year index (`_pages/YYYY/index.md`) and month index pages as needed, with correct Just the Docs front matter.

## Common Development Tasks

### Adding a New Journal

Add to `JOURNALS` list in `scripts/harvest.py`:

```python
{"name": "Journal Name", "issn": "1234-5678", "category": "top-tier"}
```

Test with `--date` on a recent date to verify papers are retrieved.

### Handling 429 Rate Limit Errors

Increase `rate_limit_delay` in the affected client class. Semantic Scholar is most sensitive.

## Technical Notes

- **Abstract priority**: S2 > OpenAlex > CrossRef. S2 typically covers ~75-85%.
- **S2 404s are normal**: Recent papers may not be indexed yet.
- **Backfill counter**: Stored in `scripts/.backfill_counter` (gitignored). Delete to reset.
- **JATS XML cleanup**: Abstracts are cleaned of JATS XML tags via regex in both scripts.
- **Branch protection**: `main` requires PRs. Automated runs create feature branches and PRs via `gh`.

## Blog Site (GitHub Pages)

Jekyll site using the [Just the Docs](https://just-the-docs.com/) remote theme.

- **Custom color scheme**: `_sass/color_schemes/hydrosense.scss` (light blue `#5b9bd5`)
- **Dark mode**: Auto via `@media (prefers-color-scheme: dark)` in `_sass/custom/custom.scss`
- **Full-text search**: Enabled with `index_full_content: true` in `_config.yml`
- **Deployment**: GitHub Actions (`.github/workflows/jekyll.yml`) on push to `main`; also supports manual `workflow_dispatch`
- **Custom domain**: `hydrosense.simhydro.com` (CNAME DNS record)

### Navigation Hierarchy

Uses Just the Docs `parent`/`grand_parent`/`has_children` front matter:

- **Level 1**: `_pages/YYYY/index.md` — year page (`has_children: true`, `nav_order: year-2023`)
- **Level 2**: `_pages/YYYY/monthname/index.md` — month page (`parent: YYYY`, `has_children: true`, `nav_order: month_num`)
- **Level 3**: `_pages/YYYY/monthname/*.md` — daily/weekly posts (`parent: Monthname`, `grand_parent: YYYY`, `nav_order: day`)

The scripts auto-generate posts with correct front matter including `layout: default`, `parent`, `grand_parent`, and `nav_order`.

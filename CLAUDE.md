# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HydroSense is an intelligent paper harvesting tool for hydrology and water resources research. It has two complementary search modes at multiple frequencies:

- **Daily harvest** (`harvest.py`): Fetches papers from 11 top-tier journals via CrossRef, enriches with Semantic Scholar + OpenAlex, and applies deterministic filters. Claude provides LLM relevance filtering and summary generation via scheduled triggers.
- **Keyword search** (`search.py`): Searches across Semantic Scholar and OpenAlex by topic keywords (no journal limits). Used for weekly, monthly, and yearly reviews. Claude synthesizes results thematically.

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

### Running the Keyword Search

```bash
python scripts/search.py                                     # Last 7 days, default topics
python scripts/search.py --weeks-back 2                      # Last 2 weeks
python scripts/search.py --from-date 2025-01-01 --to-date 2025-12-31  # Specific year
python scripts/search.py --from-date 2025-06-01 --to-date 2025-06-30  # Specific month
python scripts/search.py --topics "flood,reservoir"           # Custom topics
python scripts/search.py --max-per-topic 100                  # More results (for yearly)
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

**`scripts/search.py`** — Keyword-based literature search (used by weekly, monthly, and yearly reviews).

- `SemanticScholarSearch`: Keyword search via S2 Academic Graph API
- `OpenAlexSearch`: Keyword search via OpenAlex API
- `deduplicate_papers()`: Merges results by DOI across databases
- Supports `--from-date`/`--to-date` for arbitrary date ranges, or `--weeks-back` for relative
- Outputs JSON sorted by citation count

**`scripts/registry.py`** — Paper registry for dedup and importance tracking.

- `load_registry()` / `save_registry()`: Read/write `data/paper_registry.json`
- `register_papers()`: Add DOIs, increment appearance counts
- `is_duplicate()`: Check if DOI already in a post of the same run type
- `get_cross_references()`: Find cross-references across run types
- `get_important_papers()`: Papers with `appearance_count >= 2`

### Paper Registry (`data/paper_registry.json`)

Tracks all DOIs across all runs (daily, weekly, monthly, yearly). Papers appearing in multiple sources are flagged as "important". The registry also records run history for coverage tracking.

### Claude Skills

- **`.claude/skills/daily-harvest/`**: Daily journal-based harvest, LLM filtering, Jekyll post, PR
- **`.claude/skills/weekly-review/`**: Weekly keyword search, thematic synthesis, Jekyll post, PR
- **`.claude/skills/monthly-review/`**: Monthly keyword search for a specific month, deeper synthesis, Jekyll post, PR
- **`.claude/skills/yearly-review/`**: Yearly keyword search for a specific year, comprehensive survey, Jekyll post, PR

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
- **Monthly reviews**: `_pages/YYYY/monthname/YYYY-MM-monthly-review.md`
- **Yearly reviews**: `_pages/YYYY/YYYY-yearly-review.md`

Scripts auto-create year index (`_pages/YYYY/index.md`) and month index pages as needed, with correct Just the Docs front matter.

## Running Reviews Manually

To run any review manually, use the corresponding skill command. Claude will execute the full workflow: run the search script, filter for relevance, check the registry, synthesize findings, generate the Jekyll post, register papers, and create a PR.

### Daily Harvest
```
/daily-harvest
```
Harvests today's papers from the 11 top-tier journals. To harvest a specific date, tell Claude: "Run daily harvest for 2026-03-15".

### Weekly Review
```
/weekly-review
```
Searches the past 7 days by keyword across all databases.

### Monthly Review
```
/monthly-review
```
Claude will ask which month. Specify like: "Run monthly review for January 2025" or "Run monthly review for 2024-06".

### Yearly Review
```
/yearly-review
```
Claude will ask which year. Specify like: "Run yearly review for 2001". Good for backfilling historical coverage. Run in reverse chronological order (2025, 2024, ... 2001) to build up the registry progressively.

### Manual Script Execution (without skills)

If you want to run the search script directly and handle the post yourself:
```bash
# Weekly (last 7 days)
python scripts/search.py --weeks-back 1 --output-format json > /tmp/search_output.json

# Specific month
python scripts/search.py --from-date 2025-06-01 --to-date 2025-06-30 --output-format json > /tmp/search_output.json

# Specific year (use higher max-per-topic for broader coverage)
python scripts/search.py --from-date 2001-01-01 --to-date 2001-12-31 --max-per-topic 100 --output-format json > /tmp/search_output.json

# Daily harvest
python scripts/harvest.py --date 2026-03-15 --journals top-tier --output-format json > /tmp/harvest_output.json
```

Then ask Claude to read the JSON output, filter, synthesize, and generate the post.

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

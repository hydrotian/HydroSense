# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HydroSense is an intelligent paper harvesting tool for hydrology and water resources research. It has two complementary search modes at multiple frequencies:

- **Daily harvest** (`harvest.py`): Fetches papers from 11 top-tier journals via CrossRef, enriches with Semantic Scholar + OpenAlex, and applies deterministic filters. Claude provides LLM relevance filtering and summary generation via scheduled triggers.
- **Keyword search** (`search.py`): Searches across Semantic Scholar and OpenAlex by topic keywords (no journal limits). Used for weekly reviews. Claude synthesizes results thematically.

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

**`scripts/search.py`** — Keyword-based literature search (used by weekly reviews).

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

**`scripts/post_tweet.py`** — Posts a tweet to X via API v2 (OAuth1). Handles t.co URL-length accounting and truncation. Invoked by the daily-harvest skill after a post is published. Requires `X_API_KEY`, `X_API_SECRET`, `X_ACCESS_TOKEN`, `X_ACCESS_TOKEN_SECRET` in `.env`.

### Paper Registry (`data/paper_registry.json`)

Tracks all DOIs across all runs (daily, weekly). Papers appearing in multiple sources are flagged as "important". The registry also records run history for coverage tracking.

### Claude Skills

- **`.claude/skills/daily-harvest/`**: Daily journal-based harvest, LLM filtering, Jekyll post, push to main, tweet
- **`.claude/skills/weekly-review/`**: Weekly keyword search, thematic synthesis, Jekyll post, push to main

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

### Multilingual Content (`_pages/zh/`)

The site has a complete Chinese mirror under `_pages/zh/` with the same `YYYY/monthname/` hierarchy plus its own year/month index pages, homepage (`_pages/zh/index.md` at `/zh/`), and About page (`_pages/zh/about.md` at `/zh/about/`). The Python scripts only emit English content under `_pages/`; the Chinese translations are generated by the daily-harvest and weekly-review **skills** (not by `harvest.py`/`search.py`). When editing post generation logic in scripts, do not assume zh posts will also be updated — that is the skill's responsibility.

**Front matter convention.** Every English page that has a Chinese counterpart should declare:

```yaml
lang: en
lang_link: /zh/path/to/counterpart   # without .md, no trailing slash for posts
```

And every Chinese page declares:

```yaml
lang: zh
lang_link: /path/to/english/counterpart
nav_exclude: true   # zh pages are not part of the Just-the-Docs sidebar
permalink: /zh/...  # zh index pages need an explicit permalink
```

These two fields are how the language toggle finds the counterpart. The skill workflows include a verification step that fails if `lang_link` is missing on the English file before commit.

**Differences between the two trees:**

- English uses `categories: [daily, ...]` / `[weekly, ...]`; Chinese uses `[daily-zh, ...]` / `[weekly-zh, ...]` so Liquid filters don't accidentally mix the two languages.
- English index pages use `parent`/`grand_parent`/`has_children` for sidebar nav; Chinese index pages use `permalink` + `nav_exclude: true` (zh pages are excluded from the sidebar entirely; the on-page JS rewrites the English sidebar to point at zh counterparts when on a zh page).

**Language toggle (`_includes/head_custom.html`).** A single self-contained file handles both languages:

- Renders a floating fixed-position pill button (bottom-right corner) on every page. The pill is `position: fixed` so it works identically on desktop, tablet, and mobile and can't be hidden by a collapsed header.
- To pick the toggle's target URL, the script prefers `page.lang_link` from front matter. If that's empty (legacy pages), it falls back to URL rewriting (`/path` → `/zh/path` or vice versa).
- For English → Chinese, the script checks a build-time **manifest** of all zh URLs (`{% for p in site.pages | where: "lang", "zh" %}`) and **hides the toggle entirely** if no counterpart exists. This prevents broken 404 links when a translation hasn't been written yet.
- When on any `/zh/` page, the same script also translates the **site chrome** client-side: sidebar nav links and labels, search box placeholder, back-to-top text, footer, aux-nav links, and the `<html lang>` attribute. The sidebar selector must be permissive (`.site-nav .nav-list a, .side-bar a`, etc.) — Just-the-Docs uses `.nav-list-link`, NOT `.navigation-list-link` (an earlier typo silently broke sidebar rewriting for months).

**When touching this file**, test on both an English and a Chinese page, and re-test after any Just-the-Docs theme upgrade — class names in the rendered HTML can change. Bugs here are silent (the JS just selects nothing).

## Running Reviews Manually

Use the corresponding skill command. Claude runs the full workflow: search, filter, synthesize, generate Jekyll post, register papers, push to main (and tweet for daily).

### Daily Harvest

```text
/daily-harvest
```

Harvests papers from 11 top-tier journals (default: 8 days ago). To harvest a specific date: "Run daily harvest for 2026-03-15".

### Weekly Review

```text
/weekly-review
```

Searches the past 7 days by keyword across all databases.

### Manual Script Execution (without skills)

To drive the workflow by hand, run either script with `--output-format json` redirected to a temp file, then ask Claude to read the JSON, filter, synthesize, and generate the post. See the command sections above for flag details.

## Common Development Tasks

### Adding a New Journal

Add to `JOURNALS` list in `scripts/harvest.py`:

```python
{"name": "Journal Name", "issn": "1234-5678", "category": "top-tier"}
```

Test with `--date` on a recent date to verify papers are retrieved.

## Technical Notes

- **Abstract priority**: S2 > OpenAlex > CrossRef. S2 typically covers ~75-85%.
- **S2 404s are normal**: Recent papers may not be indexed yet.
- **Backfill counter**: Stored in `scripts/.backfill_counter` (gitignored). Delete to reset.
- **JATS XML cleanup**: Abstracts are cleaned of JATS XML tags via regex in both scripts.
- **Direct push**: Automated runs push directly to `main` (branch protection bypassed for the bot user).

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

# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HydroSense is an intelligent paper harvesting tool for hydrology and water resources research. It automatically fetches, filters, and organizes publications from top-tier and high-impact journals using a two-tier priority system with LLM-enhanced filtering. Output is published as a Jekyll blog at [hydrosense.simhydro.com](https://hydrosense.simhydro.com).

## Development Commands

### Setup
```bash
pip install -r requirements.txt
cp .env.example .env   # then edit .env with API keys
```

### Running the Harvester
```bash
python scripts/harvest.py                        # Default: last 30 days
python scripts/harvest.py --date 2026-01-15      # Specific date
python scripts/harvest.py --backfill             # Next date from counter (starts 2020-01-01)
python scripts/harvest.py --backfill --no-increment  # Backfill without advancing counter
```

### Local Blog Development
```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000/
```

### Testing

There is no automated test suite. Validate changes by running `harvest.py` with `--date` on a known date and inspecting the generated Markdown output.

## Architecture

### Core Script

**scripts/harvest.py** — Single monolithic script. All harvesting logic lives here.

**API Clients:**
- `CrossRefClient`: Primary paper metadata source (by journal ISSN + date range)
- `SemanticScholarClient`: Field classification and abstracts
- `OpenAlexClient`: Fallback abstract source
- `GeminiClient`: LLM binary relevance filtering + daily summary generation (Gemini 2.5 Flash Lite)

**Two-Tier Classification:**
- **Part 1**: Top-tier journals + topic keywords + peer-reviewed (`journal-article` type) + LLM-approved
- **Part 2**: High-impact journals + topic keywords + peer-reviewed + LLM-approved

**Backfill System:**
- Counter file at `scripts/.backfill_counter` (gitignored) tracks days offset from `BACKFILL_START_DATE` (2020-01-01)
- `get_next_backfill_date()` / `increment_backfill_counter()` manage the counter

**Data Flow:** Parse Args → Fetch (CrossRef) → Enrich (S2 + OpenAlex fallback) → Classify (keywords + field match + LLM) → Summarize (Gemini) → Output (Jekyll post to `_pages/YYYY/monthname/`)

### Configuration

**API Keys** (via python-dotenv from `.env`):
- `SEMANTIC_SCHOLAR_API_KEY`: Required (free at semanticscholar.org)
- `GEMINI_API_KEY`: Required (free at aistudio.google.com)
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
- Gemini: 4.0s delay (15 req/min limit)

**Runtime**: ~15-20 minutes for 600-700 papers.

### Output

Reports saved as Jekyll posts: `_pages/YYYY/monthname/YYYY-MM-DD-daily-harvest.md`

The script auto-creates year index (`_pages/YYYY/index.md`) and month index pages as needed, with correct Just the Docs front matter (`parent`/`grand_parent`/`has_children`/`nav_order`).

## Common Development Tasks

### Adding a New Journal
Add to `JOURNALS` list in `scripts/harvest.py`:
```python
{"name": "Journal Name", "issn": "1234-5678", "category": "top-tier"}
```
Test with `--date` on a recent date to verify papers are retrieved.

### Customizing LLM Filtering
The Gemini prompt is in `GeminiClient.is_relevant()`. Modify the researcher's domain/topics sections and `generationConfig` as needed.

### Handling 429 Rate Limit Errors
Increase `rate_limit_delay` in the affected client class. Semantic Scholar is most sensitive.

## Technical Notes

- **Abstract priority**: S2 > OpenAlex > CrossRef. S2 typically covers ~75-85%.
- **S2 404s are normal**: Recent papers may not be indexed yet.
- **Backfill counter**: Stored in `scripts/.backfill_counter` (gitignored). Delete to reset to 2020-01-01.
- **JATS XML cleanup**: The output generator strips JATS XML tags from abstracts via regex.

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
- **Level 3**: `_pages/YYYY/monthname/*.md` — daily posts (`parent: Monthname`, `grand_parent: YYYY`, `nav_order: day`)

The harvest script auto-generates posts with correct front matter including `layout: default`, `parent`, `grand_parent`, and `nav_order`.

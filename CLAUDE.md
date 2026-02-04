# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

HydroSense is an intelligent paper harvesting tool for hydrology and water resources research. It automatically fetches, filters, and organizes publications from top-tier and high-impact journals using a three-tier priority system.

## Development Commands

### Setup
```bash
# Install dependencies
pip install -r requirements.txt

# Configure API keys
cp .env.example .env
# Edit .env with your actual API keys
```

### Running the Harvester
```bash
# Run from scripts directory
python scripts/harvest.py

# Or from project root
python scripts/harvest.py
```

### Date Range Configuration
Edit the date range in `scripts/harvest.py` in the `main()` function:
- For recent papers: Use `datetime.now() - timedelta(days=N)`
- For specific dates: Set `from_str` and `until_str` directly (format: "YYYY-MM-DD")

## Architecture

### Core Components

**scripts/harvest.py** - Single monolithic script containing all harvesting logic:

1. **API Clients** (lines ~100-343):
   - `CrossRefClient`: Primary source for paper metadata from journals via CrossRef API
   - `SemanticScholarClient`: Enrichment for field classification and abstracts
   - `OpenAlexClient`: Fallback abstract source when Semantic Scholar lacks coverage
   - `GeminiClient`: LLM-based binary relevance filtering (Stage 1 filtering)

2. **Three-Tier Classification System** (lines ~518-669):
   - **Part 1**: Top-tier journals + topic keywords + peer-reviewed + LLM-approved
     - Most important papers, highest priority for reading
     - Gets S2 recommendations if available
   - **Part 2**: High-impact journals + topic keywords + peer-reviewed + LLM-approved
     - Important specialized papers
     - No S2 recommendations
   - **Part 3**: Top-tier journals + relevant fields only
     - Field awareness, includes news/editorials
     - No topic matching required

3. **Filtering Logic**:
   - Semantic Scholar field classification against `RELEVANT_FIELDS` list
   - Keyword matching against `TOPICS` list in title/abstract
   - Peer-review status verification (must be 'journal-article' type for Parts 1 & 2)
   - Gemini LLM binary relevance check (Parts 1 & 2 only)

4. **Output Generation** (lines ~390-449, ~733-794):
   - Markdown report with paper details, abstracts, author info
   - Summary statistics (S2 coverage, journal distribution)
   - Three-part structure matching classification tiers

### Configuration

**API Keys** (loaded via python-dotenv from .env file):
- `SEMANTIC_SCHOLAR_API_KEY`: Required for field classification (free at semanticscholar.org)
- `GEMINI_API_KEY`: Required for LLM relevance filtering (free at aistudio.google.com)
- `CROSSREF_EMAIL`: Optional, for faster CrossRef polite pool access

**Journal Lists** (lines ~53-84):
- `JOURNALS`: List of tracked journals with ISSN, name, and category (top-tier/High-impact)
- Update this to add new journals to monitor

**Filtering Parameters**:
- `TOPICS` (lines ~87-88): Keywords for topic-based filtering
- `RELEVANT_FIELDS` (lines ~92-98): Semantic Scholar field classifications to match

### Rate Limiting

Critical for API compliance:
- CrossRef: 0.1s delay between requests (line ~110)
- Semantic Scholar: 1.5s delay (line ~250) - conservative for 1 req/sec limit
- OpenAlex: 0.1s delay (line ~211)
- Gemini: 4.0s delay (line ~260) - 15 requests/minute limit

**Runtime**: Expect ~15-20 minutes for 600-700 papers due to rate limits.

### Data Flow

1. **Fetch** (lines ~503-514): CrossRef API retrieves papers by journal ISSN and date range
2. **Enrich** (lines ~533-607): For each paper:
   - Query Semantic Scholar for field classification and abstract
   - Fallback to OpenAlex for abstract if S2 lacks it
   - Extract matched fields and topics
3. **Classify** (lines ~608-669): Apply three-tier logic with peer-review filtering and LLM checks
4. **Format** (lines ~733-794): Generate markdown report with summary statistics

### Output Location

Default: `/Users/zhou014/Local_Drive/Temp/harvest_<date>.md`

Modify `output_file` variable in `main()` function (line ~734) to change location.

## Common Development Tasks

### Adding a New Journal

1. Find the journal's ISSN (usually on the journal website or from CrossRef)
2. Add to `JOURNALS` list in harvest.py:
```python
{"name": "Journal Name", "issn": "1234-5678", "category": "top-tier"}
```
3. Test with a small date range to verify papers are retrieved

### Modifying Topic Keywords

Edit the `TOPICS` list (line ~87-88) to change what keywords trigger Part 1/2 classification.

### Adjusting Field Classifications

Edit `RELEVANT_FIELDS` (lines ~92-98) to change which Semantic Scholar fields are considered relevant for Part 3.

### Changing Rate Limits

If experiencing 429 errors:
- Increase `rate_limit_delay` in respective client classes
- Semantic Scholar is most sensitive (line ~250)

### Customizing LLM Filtering

The Gemini prompt for relevance checking is in `GeminiClient.is_relevant()` (lines ~273-307):
- Modify the researcher's domain and relevant topics sections
- Adjust temperature and maxOutputTokens in generationConfig (lines ~317-319)

## Technical Notes

- **Paper Type Filtering**: Only 'journal-article' type passes peer-review check for Parts 1 & 2. Part 3 allows all types (news, editorial, etc.) for field awareness.
- **Abstract Sources**: Prioritized as S2 > OpenAlex > CrossRef. S2 typically has best coverage (~75-85%).
- **S2 404s are Normal**: Not all papers are immediately indexed in Semantic Scholar, especially recent publications.
- **LLM Filtering**: Gemini 2.0 Flash Lite provides binary relevance classification to reduce false positives from keyword matching.

## Blog Site (GitHub Pages)

The repository includes a Jekyll-based blog site that hosts daily and monthly harvest reports.

### Structure

```
HydroSense/
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── index.md                 # Homepage
├── _pages/                  # Static pages (about, etc.)
├── _pages/2025.md          # Year navigation page
├── _pages/2025/            # 2025 posts
│   ├── january.md          # Month navigation page
│   ├── february.md         # Month navigation page
│   ├── 2025-01-03-daily-harvest.md
│   ├── 2025-01-31-monthly-summary.md
│   └── ...
└── _pages/2026/            # 2026 posts
```

### Local Development

```bash
# Install Jekyll dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Site will be available at http://localhost:4000/
```

### Theme: Jekyll-GitBook

Uses the `jekyll-gitbook` theme (https://github.com/sighingnow/jekyll-gitbook) which provides:
- Sidebar navigation with hierarchical structure
- Built-in full-text search (including abstracts)
- Clean, book-like layout
- Table of contents for long posts

### Adding New Posts

**Daily Reports:**
1. Generate report using `scripts/harvest.py`
2. Script automatically saves to `_pages/YYYY/YYYY-MM-DD-daily-harvest.md`
3. Front matter template:
```yaml
---
layout: page
title: "January 03 - Daily Harvest"
parent: January
grand_parent: 2025
nav_order: 3
date: 2025-01-03
categories: [daily, 2025, january]
tags: [hydrology, paper-harvest, research]
---
```

**Monthly Summaries:**
1. Create manually or with a script
2. Save to `_pages/YYYY/YYYY-MM-31-monthly-summary.md`
3. Set `nav_order: 31` to appear after daily reports

**Important:** Before adding daily reports for a new month:
1. Create month navigation page: `_pages/YYYY/monthname.md`
2. Set proper `parent: YYYY` and `nav_order`

### Search Configuration

Full-text search is enabled in `_config.yml`:
```yaml
search:
  enabled: true
  index_full_content: true
```

This indexes:
- Paper titles
- Author names
- Journal names
- Abstracts
- Keywords and topics
- All markdown content

### GitHub Pages Deployment

The site is deployed via GitHub Actions (`.github/workflows/jekyll.yml`):
- Automatically builds on push to main branch
- Deploys to `https://hydrosense.simhydro.com`
- No pre-building required

To manually trigger deployment:
1. Go to Actions tab in GitHub
2. Select "Deploy Jekyll site to Pages"
3. Click "Run workflow"

### File Naming Conventions

- Daily reports: `YYYY-MM-DD-daily-harvest.md`
- Monthly summaries: `YYYY-MM-31-monthly-summary.md`
- Organize all posts in `_pages/YYYY/` for automatic navigation

### Navigation Hierarchy

The site uses a three-level hierarchy:
- **Level 1:** Year pages (e.g., `2025.md`)
- **Level 2:** Month pages (e.g., `january.md` with `parent: 2025`)
- **Level 3:** Daily/monthly posts (with `parent: January` and `grand_parent: 2025`)

Jekyll-GitBook automatically generates the sidebar navigation tree from these relationships.

## Blog Site (GitHub Pages)

The repository includes a Jekyll-based blog site that hosts daily and monthly harvest reports.

### Structure

```
HydroSense/
├── _config.yml              # Jekyll configuration
├── Gemfile                  # Ruby dependencies
├── index.md                 # Homepage
├── _pages/                  # Static pages (about, etc.)
├── _posts_2025/            # 2025 posts collection
│   ├── 01-January/         # January daily reports
│   │   ├── 2025-01-03-daily-harvest.md
│   │   ├── 2025-01-04-daily-harvest.md
│   │   └── 2025-01-31-monthly-summary.md
│   └── 02-February/        # February reports
└── _posts_2026/            # 2026 posts collection
```

### Local Development

```bash
# Install Jekyll dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Site will be available at http://localhost:4000/hydrosense/
```

### Theme: Jekyll-GitBook

Uses the `jekyll-gitbook` theme (https://github.com/sighingnow/jekyll-gitbook) which provides:
- Sidebar navigation with hierarchical structure
- Built-in full-text search (including abstracts)
- Clean, book-like layout
- Table of contents for long posts

### Adding New Posts

**Daily Reports:**
1. Generate report using `scripts/harvest.py`
2. Save to `_posts_YYYY/MM-MonthName/YYYY-MM-DD-daily-harvest.md`
3. Add front matter:
```yaml
---
layout: post
title: "Daily Harvest - January 3, 2025"
date: 2025-01-03
categories: [daily, 2025, january]
tags: [hydrology, climate, water-resources]
toc: true
---
```

**Monthly Summaries:**
1. Save to `_posts_YYYY/MM-MonthName/YYYY-MM-31-monthly-summary.md`
2. Add front matter:
```yaml
---
layout: post
title: "Monthly Summary - January 2025"
date: 2025-01-31
categories: [monthly, 2025, january]
tags: [summary, trends, hydrology]
toc: true
---
```

### Search Configuration

Full-text search is enabled in `_config.yml`:
```yaml
search:
  enabled: true
  index_full_content: true
```

This indexes:
- Paper titles
- Author names
- Journal names
- Abstracts
- Keywords and topics
- All markdown content

### GitHub Pages Deployment

The site is deployed via GitHub Actions (`.github/workflows/jekyll.yml`):
- Automatically builds on push to main branch
- Deploys to `https://hydrotian.github.io/hydrosense/`
- No pre-building required

To manually trigger deployment:
1. Go to Actions tab in GitHub
2. Select "Deploy Jekyll site to Pages"
3. Click "Run workflow"

### File Naming Conventions

- Daily reports: `YYYY-MM-DD-daily-harvest.md`
- Monthly summaries: `YYYY-MM-31-monthly-summary.md`
- Organize by year/month folders for better navigation

### Theme Customization

The jekyll-gitbook theme can be customized via `_config.yml`:
- `toc.h_min` / `toc.h_max`: Control table of contents depth
- `syntax_highlighter_style`: Code highlighting theme
- `collections`: Define post organization structure

# HydroSense

An intelligent paper harvesting tool for hydrology and water resources research. HydroSense automatically fetches, filters, and organizes recent publications, helping researchers stay current with the latest developments in their field.

## Features

- **Two-Mode Operation**:
  - **Daily Harvest**: Papers from 11 top-tier journals, filtered by topic keywords and field classification
  - **Keyword Search**: Search across all academic databases by topic, used for weekly, monthly, and yearly reviews

- **Claude-Enhanced Filtering**:
  - LLM relevance evaluation via Claude scheduled triggers
  - AI-generated daily summaries and weekly thematic synthesis
  - Reduces false positives from keyword-only matching

- **Multi-Source Data Integration**:
  - CrossRef API for journal-based paper metadata
  - Semantic Scholar for field classification, abstracts, and keyword search
  - OpenAlex for keyword search and fallback abstracts

- **Paper Registry**: Central DOI tracking across all runs for deduplication, importance scoring (papers found by multiple sources), and cross-referencing between daily and weekly outputs

- **Rich Output**: Jekyll-compatible Markdown reports with paper abstracts, DOI links, classification metadata, and journal statistics

## Installation

### Prerequisites

- Python 3.7+
- API keys (see Setup below)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/hydrotian/HydroSense.git
cd HydroSense
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure API keys:
```bash
cp .env.example .env
# Edit .env with your actual API keys
```

Required keys in `.env`:
- `SEMANTIC_SCHOLAR_API_KEY`: Free at https://www.semanticscholar.org/product/api
- `CROSSREF_EMAIL`: Optional, for faster CrossRef polite pool access

## Usage

### Daily Harvest

```bash
python scripts/harvest.py                              # Default: last 30 days, top-tier only
python scripts/harvest.py --date 2026-01-15            # Specific date
python scripts/harvest.py --journals all               # All 29 journals
python scripts/harvest.py --output-format json         # JSON output for Claude triggers
python scripts/harvest.py --backfill                   # Next backfill month
```

### Keyword Search (Weekly / Monthly / Yearly)

```bash
python scripts/search.py                                    # Last 7 days, default topics
python scripts/search.py --weeks-back 2                     # Last 2 weeks
python scripts/search.py --from-date 2025-06-01 --to-date 2025-06-30  # Specific month
python scripts/search.py --from-date 2001-01-01 --to-date 2001-12-31  # Specific year
python scripts/search.py --topics "flood,reservoir"          # Custom topics
```

### Output

- **Daily posts**: `_pages/YYYY/monthname/YYYY-MM-DD-daily-harvest.md`
- **Weekly reviews**: `_pages/YYYY/monthname/YYYY-MM-DD-weekly-review.md`
- **Monthly reviews**: `_pages/YYYY/monthname/YYYY-MM-monthly-review.md`
- **Yearly reviews**: `_pages/YYYY/YYYY-yearly-review.md`

Reports automatically appear on the blog site when pushed.

## Rate Limits

- **Semantic Scholar**: 1.5s delay (graph API), 3.0s delay (search API)
- **CrossRef**: 0.1s delay
- **OpenAlex**: 0.1s delay

## Tracked Journals

### Top-Tier (11 journals)
- Nature, Science, PNAS
- Geophysical Research Letters, BAMS
- Nature Climate Change, Nature Geoscience, Nature Water
- Nature Communications, Nature Reviews Earth & Environment
- Reviews of Geophysics

### High-Impact (18 journals)
Water Resources Research, Journal of Hydrology, Hydrology and Earth System Sciences, and more. See full list in `scripts/harvest.py`.

## Blog Site

Jekyll-based blog at [hydrosense.simhydro.com](https://hydrosense.simhydro.com) with full-text search, hierarchical navigation, and automatic dark mode.

### Local Development
```bash
bundle install
bundle exec jekyll serve   # http://localhost:4000/
```

## Technical Details

- **Language**: Python 3.7+
- **External APIs**: CrossRef, Semantic Scholar, OpenAlex
- **LLM**: Claude (via scheduled triggers)
- **Output Format**: Jekyll-compatible Markdown
- **Theme**: [Just the Docs](https://just-the-docs.com/) with custom color scheme

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see LICENSE file for details

## Acknowledgments

- CrossRef API for comprehensive metadata
- Semantic Scholar for field classification and keyword search
- OpenAlex for abstract coverage and keyword search
- Claude for LLM relevance filtering and synthesis

---

**Note**: This tool is for research purposes. Please respect API rate limits and terms of service.

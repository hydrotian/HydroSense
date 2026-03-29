# HydroSense

An intelligent paper harvesting tool for hydrology and water resources research. HydroSense automatically fetches, filters, and organizes recent publications from top-tier and high-impact journals, helping researchers stay current with the latest developments in their field.

## Features

- **Two-Tier Priority System**: Automatically classifies papers by relevance and importance
  - **Part 1**: Peer-reviewed articles from top-tier journals matching your research topics
  - **Part 2**: Peer-reviewed articles from high-impact journals matching your topics

- **LLM-Enhanced Filtering**:
  - Gemini 2.5 Flash Lite for binary relevance classification
  - AI-generated daily summaries highlighting key themes
  - Reduces false positives from keyword-only matching

- **Multi-Source Data Integration**:
  - CrossRef API for comprehensive paper metadata
  - Semantic Scholar for field classification and enhanced metadata
  - OpenAlex as fallback for abstracts

- **Smart Filtering**:
  - Topic-based keyword matching
  - Academic field classification
  - Peer-review status verification
  - Customizable journal lists

- **Rich Output**: Jekyll-compatible Markdown reports with:
  - AI-generated daily highlights
  - Paper abstracts
  - Author information
  - DOI links
  - Classification metadata
  - Journal distribution statistics

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
- `GEMINI_API_KEY`: Free at https://aistudio.google.com
- `CROSSREF_EMAIL`: Optional, for faster CrossRef polite pool access

## Usage

### Quick Start

```bash
# Default: harvest papers from the last 30 days
python scripts/harvest.py

# Harvest a specific date
python scripts/harvest.py --date 2026-01-15

# Backfill mode: harvest next date in sequence (starting from 2020-01-01)
python scripts/harvest.py --backfill

# Backfill without incrementing the counter (for testing)
python scripts/harvest.py --backfill --no-increment
```

### Output

Reports are saved as Jekyll posts to `_pages/YYYY/monthname/YYYY-MM-DD-daily-harvest.md` and automatically appear on the blog site when pushed.

### Customization

#### Modify Journal List

Edit the `JOURNALS` list in `scripts/harvest.py`:
```python
JOURNALS = [
    {"name": "Nature", "issn": "1476-4687", "category": "top-tier"},
    {"name": "Water Resources Research", "issn": "1944-7973", "category": "High-impact"},
    # Add your journals here
]
```

#### Adjust Topic Keywords

Modify the `TOPICS` list:
```python
TOPICS = ["hydrology", "flood", "drought", "climate", ...]
```

#### Change Relevant Fields

Update `RELEVANT_FIELDS` for different research areas:
```python
RELEVANT_FIELDS = [
    'engineering',
    'environmental science',
    'computer science',
    'geology',
    'geography'
]
```

## Rate Limits

- **Semantic Scholar**: 1.5s delay (conservative for 1 req/sec limit)
- **CrossRef**: 0.1s delay
- **OpenAlex**: 0.1s delay
- **Gemini**: 4.0s delay (15 requests/minute limit)

**Estimated runtime**: ~15-20 minutes for 600-700 papers

## Tracked Journals

### Top-Tier (11 journals)
- Nature, Science, PNAS
- Geophysical Research Letters, BAMS
- Nature Climate Change, Nature Geoscience, Nature Water
- Nature Communications, Nature Reviews Earth & Environment
- Reviews of Geophysics

### High-Impact (18 journals)
Water Resources Research, Journal of Hydrology, Hydrology and Earth System Sciences, and more.

See full list in `scripts/harvest.py`.

## Technical Details

- **Language**: Python 3.7+
- **External APIs**: CrossRef, Semantic Scholar, OpenAlex, Gemini
- **Output Format**: Jekyll-compatible Markdown
- **Classification**: Two-tier priority system with peer-review filtering and LLM verification

## Blog Site

HydroSense includes a Jekyll-based blog site that hosts daily harvest reports with full-text search.

**Live Site:** [https://hydrosense.simhydro.com](https://hydrosense.simhydro.com)

### Features
- Daily harvest reports organized by year and month
- AI-generated daily highlights
- Full-text search (authors, journals, titles, abstracts)
- Hierarchical sidebar navigation (Year > Month > Daily reports)
- Automatic dark mode support
- Mobile responsive

### Local Development
```bash
# Install Jekyll dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Visit: http://localhost:4000/
```

### Theme

Uses the [Just the Docs](https://just-the-docs.com/) theme with custom light blue color scheme and automatic dark mode via CSS `prefers-color-scheme` media query.

## Troubleshooting

**429 Rate Limit Errors**
- Increase `rate_limit_delay` in respective client classes
- Semantic Scholar is most sensitive

**No Papers Found**
- Check date range (papers may not be indexed yet)
- Verify journal ISSNs are correct
- Ensure TOPICS match paper content

**Missing Abstracts**
- Normal for recent papers (can take weeks to index)
- S2 coverage: ~75-85% typical
- OpenAlex provides fallback coverage

## Contributing

Contributions welcome! Please feel free to:
- Add new journal sources
- Improve filtering algorithms
- Enhance output formats
- Fix bugs

## License

MIT License - see LICENSE file for details

## Acknowledgments

- CrossRef API for comprehensive metadata
- Semantic Scholar for field classification and recommendations
- OpenAlex for abstract coverage
- Google Gemini for LLM relevance filtering

## Contact

For questions or issues, please open an issue on GitHub.

---

**Note**: This tool is for research purposes. Please respect API rate limits and terms of service.

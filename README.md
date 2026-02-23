# HydroSense

An intelligent paper harvesting tool for hydrology and water resources research. HydroSense automatically fetches, filters, and organizes recent publications from top-tier and high-impact journals, helping researchers stay current with the latest developments in their field.

## Features

- **Three-Tier Priority System**: Automatically classifies papers by relevance and importance
  - **Part 1**: Peer-reviewed articles from top-tier journals matching your research topics
  - **Part 2**: Peer-reviewed articles from high-impact journals matching your topics
  - **Part 3**: All content from top-tier journals in relevant fields (includes news and editorials)

- **Multi-Source Data Integration**:
  - CrossRef API for comprehensive paper metadata
  - Semantic Scholar for field classification and enhanced metadata
  - OpenAlex as fallback for abstracts

- **Smart Filtering**:
  - Topic-based keyword matching
  - Academic field classification
  - Peer-review status verification
  - Customizable journal lists

- **Rich Output**: Markdown reports with:
  - Paper abstracts
  - Author information
  - DOI links
  - Classification metadata
  - Journal distribution statistics

## Installation

### Prerequisites

- Python 3.7+
- Semantic Scholar API key (free, get yours at https://www.semanticscholar.org/product/api)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/HydroSense.git
cd HydroSense
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure your API key:
   - Open `harvest.py`
   - Replace `api_key` value on line ~375 with your Semantic Scholar API key

## Usage

### Quick Start

1. Set your date range in `harvest.py`:
```python
# For recent papers (last 3 days)
from_str = (datetime.now() - timedelta(days=3)).strftime('%Y-%m-%d')
until_str = datetime.now().strftime('%Y-%m-%d')

# Or for specific dates
from_str = "2025-01-01"
until_str = "2025-01-07"
```

2. Run the harvester:
```bash
python harvest.py
```

3. Check the output:
   - Report saved to: `/Users/zhou014/Local_Drive/Temp/harvest_<date>.md`
   - Console shows progress and statistics

### Customization

#### Modify Journal List

Edit the `JOURNALS` list in `harvest.py`:
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

## Output Format

The tool generates a structured Markdown report with:

### Summary Section
- Total papers published
- Papers selected by tier
- Semantic Scholar coverage statistics
- Papers by journal distribution

### Part 1: Top-Tier + Topics (Peer-reviewed)
Highest priority papers for detailed reading.

### Part 2: High-Impact + Topics (Peer-reviewed)
Important papers from specialized journals.

### Part 3: Field Awareness
News, editorials, and research for staying aware of field developments.

## Rate Limits

- **Semantic Scholar**: 1 request/second (with API key)
- **CrossRef**: Polite rate (0.1s delay)
- **OpenAlex**: 0.1s delay

**Estimated runtime**: ~15-20 minutes for 600-700 papers

## Configuration

### API Keys
- **Semantic Scholar**: Required (set in `harvest.py`)
- **CrossRef**: Optional email for polite pool access
- **OpenAlex**: No key required

### Output Directory
Default: `/Users/zhou014/Local_Drive/Temp/`

Modify in `harvest.py`:
```python
output_file = f"/your/custom/path/harvest_{until_str}.md"
```

## Tracked Journals

### Top-Tier (11 journals)
- Nature, Science, PNAS
- Geophysical Research Letters
- Nature Climate Change, Nature Geoscience, Nature Water
- Nature Communications, Nature Reviews Earth & Environment
- Reviews of Geophysics

### High-Impact (18 journals)
Water Resources Research, Journal of Hydrology, Hydrology and Earth System Sciences, and more.

See full list in `harvest.py`.

## Technical Details

- **Language**: Python 3.7+
- **External APIs**: CrossRef, Semantic Scholar, OpenAlex
- **Output Format**: Markdown
- **Classification**: Three-tier priority system with peer-review filtering

## Troubleshooting

**429 Rate Limit Errors**
- Increase `rate_limit_delay` in SemanticScholarClient (line ~237)
- Ensure API key is correctly configured

**No Papers Found**
- Check date range (papers may not be indexed yet)
- Verify journal ISSNs are correct
- Ensure TOPICS match paper content

**Missing Abstracts**
- Normal for recent papers (can take weeks to index)
- S2 coverage: ~75-85% typical
- OpenAlex provides fallback coverage

## Blog Site

HydroSense includes a Jekyll-based blog site that hosts daily and monthly harvest reports with full-text search.

**Live Site:** [https://hydrotian.github.io/hydrosense/](https://hydrotian.github.io/hydrosense/)

### Features
- Daily harvest reports organized by year and month
- Monthly summaries with trends and highlights
- Full-text search (authors, journals, titles, abstracts)
- Clean, book-like interface with sidebar navigation
- Mobile responsive

### Local Development
```bash
# Install Jekyll dependencies
bundle install

# Serve locally
bundle exec jekyll serve

# Visit: http://localhost:4000/hydrosense/
```

See `BLOG_README.md` for detailed documentation on the blog site.

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

## Contact

For questions or issues, please open an issue on GitHub.

---

**Note**: This tool is for research purposes. Please respect API rate limits and terms of service.


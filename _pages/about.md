---
layout: default
title: About
nav_order: 10
permalink: /about/
---

# About HydroSense

HydroSense is an automated literature monitoring system designed specifically for researchers in hydrology, water resources, and Earth system science.

## How It Works

### Data Sources

HydroSense integrates multiple APIs to provide comprehensive paper coverage:

1. **CrossRef API** - Primary source for publication metadata
2. **Semantic Scholar** - Field classification and enhanced abstracts
3. **OpenAlex** - Fallback source for abstract content
4. **Gemini LLM** - Intelligent relevance filtering

### Three-Tier Classification

Papers are automatically classified into three tiers based on journal prestige and topic relevance:

**Part 1: Highest Priority**
- Top-tier journals (Nature, Science, GRL, Nature Water, etc.)
- Matches specific research topics
- Peer-reviewed research articles only
- Passes LLM relevance check

**Part 2: Important Papers**
- High-impact specialized journals (WRR, JoH, HESS, etc.)
- Matches research topics
- Peer-reviewed research articles only
- Passes LLM relevance check

**Part 3: Field Awareness**
- Top-tier journals in relevant fields
- Includes all content types (news, editorials, research)
- Helps stay aware of broader developments

### Tracked Topics

- Hydrology and hydrologic modeling
- River systems and streamflow
- Reservoirs and water management
- Floods and droughts
- Climate change impacts on water
- Land surface modeling
- Seasonal forecasting
- Hydropower and irrigation
- Earth system models

### Research Focus

This system is optimized for researchers working on:
- E3SM (Energy Exascale Earth System Model)
- MOSART river routing model
- Land-river coupling and connectivity
- Reservoir operations and management
- Large-scale hydrologic modeling

## Tracked Journals

### Top-Tier (11 journals)

- Nature
- Science
- Proceedings of the National Academy of Sciences (PNAS)
- Geophysical Research Letters (GRL)
- Bulletin of the American Meteorological Society (BAMS)
- Nature Climate Change
- Nature Geoscience
- Nature Water
- Reviews of Geophysics
- Nature Communications
- Nature Reviews Earth & Environment

### High-Impact Specialized (18 journals)

- Water Resources Research (WRR)
- Journal of Hydrology (JoH)
- Hydrology and Earth System Sciences (HESS)
- Advances in Water Resources (AWR)
- Journal of Climate
- Earth System Dynamics
- Global Change Biology
- Environmental Research Letters
- Journal of Geophysical Research: Atmospheres
- Journal of Hydrometeorology
- Journal of Advances in Modeling Earth Systems (JAMES)
- Earth-Science Reviews
- Journal of Geophysical Research: Machine Learning and Computation
- Geoscientific Model Development (GMD)
- Earth's Future
- Scientific Data
- Scientific Reports
- Hydrological Processes
- Journal of the American Water Resources Association (JAWRA)

## Coverage Statistics

- **Daily Harvest:** ~600-700 papers scanned per day
- **Selection Rate:** Typically 15-20% pass filters
- **Abstract Coverage:** 75-85% (via Semantic Scholar + OpenAlex)
- **Processing Time:** ~15-20 minutes per harvest (due to API rate limits)

## Technology Stack

- **Harvesting:** Python 3.7+ with requests library
- **APIs:** CrossRef, Semantic Scholar, OpenAlex, Gemini
- **Website:** Jekyll with GitBook theme
- **Search:** Full-text search including abstracts
- **Hosting:** GitHub Pages

## Contributing

This is an open-source project. The harvest script and website code are available in the [HydroSense GitHub repository](https://github.com/hydrotian/HydroSense).

## Contact

For questions or suggestions:
- Email: hydro.luna.bot@gmail.com
- GitHub Issues: [HydroSense Issues](https://github.com/hydrotian/HydroSense/issues)

---

*Last updated: February 2025*

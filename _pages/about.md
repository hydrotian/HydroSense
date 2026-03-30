---
layout: default
title: About
nav_order: 10
permalink: /about/
---

# About HydroSense

HydroSense is an automated literature monitoring system designed specifically for researchers in hydrology, water resources, and Earth system science.

## How It Works

### Two-Mode Operation

**Daily Harvest** scans 11 top-tier journals via CrossRef, enriches papers with Semantic Scholar and OpenAlex, and applies deterministic filters (keywords, field classification, peer-review status). Claude provides LLM relevance filtering and summary generation.

**Weekly Literature Review** searches by keyword across Semantic Scholar and OpenAlex (no journal limits), deduplicates results, and Claude synthesizes findings into thematic reviews.

### Data Sources

1. **CrossRef API** - Journal-based paper metadata (daily harvest)
2. **Semantic Scholar** - Field classification, abstracts, and keyword search
3. **OpenAlex** - Keyword search and fallback abstracts
4. **Claude** - LLM relevance filtering and thematic synthesis

### Paper Registry

A central registry tracks all DOIs across runs. Papers discovered by multiple pathways (daily + weekly, or multiple search topics) are flagged as "important" — a strong relevance signal.

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

## Technology Stack

- **Harvesting:** Python 3.7+ with requests library
- **APIs:** CrossRef, Semantic Scholar, OpenAlex
- **LLM:** Claude (via scheduled triggers)
- **Website:** Jekyll with Just the Docs theme
- **Search:** Full-text search including abstracts
- **Hosting:** GitHub Pages

## Contributing

This is an open-source project. The harvest script and website code are available in the [HydroSense GitHub repository](https://github.com/hydrotian/HydroSense).

## Contact

For questions or suggestions:
- Email: hydro.luna.bot@gmail.com
- GitHub Issues: [HydroSense Issues](https://github.com/hydrotian/HydroSense/issues)

---

*Last updated: March 2026*

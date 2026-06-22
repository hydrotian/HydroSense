---
layout: default
title: "Week 24 (Jun 8 - Jun 15), 6 papers"
parent: June
grand_parent: "2026"
nav_order: 36
date: 2026-06-22
categories: [weekly, 2026, june]
tags: [hydrology, literature-review, research]
paper_count: 6
highlight: "Adding overland-flow physics to the Noah-MP land surface model lets WRF reproduce a record Pearl River Basin flood that the original scheme could not simulate at all."
lang: en
lang_link: /zh/2026/june/2026-06-22-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 24** · Jun 8–Jun 15, 2026
{: .text-grey-dk-000 }

**6** relevant papers found across **3** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's review is unusually compact: OpenAlex's search API returned HTTP 429 for every query during this run, so all results come from Semantic Scholar alone — treat the 6-paper count as a lower bound on what was actually published, not a verdict on a slow week. Within what was retrieved, two land-surface modeling papers push flood-relevant process realism forward (overland flow in Noah-MP/WRF reproducing a record Pearl River Basin flood; an LSM-based riverflow simulation for the Limpopo Basin), alongside a new generic coupling library for hydrology-Earth System Model integration. On the management side, irrigation remote-sensing and socio-hydrologic multiagent modeling point toward better integration of human decisions and Earth observation into water-resource planning.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Land Surface & Hydrologic Model Coupling

Three papers this week advance the technical machinery of coupled hydrologic and land-surface simulation. Qiu et al. integrate an explicit overland-flow scheme into the community Noah-MP land surface model and couple it with WRF, applying the system to a record April 2024 precipitation event in South China's Pearl River Basin — the modified scheme reproduces the satellite-observed inundation extent, while the original WRF configuration could not simulate the flood at all, and the added hydrological realism even feeds back to improve simulated precipitation through land-atmosphere interactions. Mohomi et al. take a parallel approach for South Africa's Limpopo River Basin, applying a terrestrial land surface model to simulate riverflow in this transboundary, semi-arid, and data-sparse catchment. At the infrastructure level, Abele et al. address the plumbing behind these kinds of coupled simulations: their new preCICE-based adapters connect the Ice-sheet and Sea-level System Model (ISSM) with the subglacial hydrology model CUAS-MPI, providing a generic, reusable bidirectional coupling layer that extends beyond the ice-sheet use case to any multi-physics Earth System Model coupling involving a hydrology submodel.

### Incorporating Overland Flow into the WRF Noah-MP Land Surface Scheme and Applying to a Record Flood Simulation in the Pearl River Basin

**Authors**: Shengyuan Qiu, H. Ren, Ping Zhao, Yuhao Wang, Weiteng Qiu, Yinghan Sang

**Journal**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0081.1](https://doi.org/10.1175/jhm-d-25-0081.1) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> With global warming increasing flood intensity and frequency, the authors integrate an overland-flow scheme into the Noah-MP land surface model and couple it with WRF, applying the system to a record precipitation event over the Pearl River Basin in April 2024. The modified scheme's simulated inundation aligns with satellite observations and reduces soil-moisture error, whereas the original WRF configuration fails to reproduce the flooding — and the improved hydrological process representation also enhances simulated precipitation via land-atmosphere coupling.

---

### Simulating riverflow in South Africa's Limpopo River Basin using term land surface model

**Authors**: Tumelo Mohomi, V. Stepanenko, A. Medvedev, I. Dhau, Hector Chikoore, M. Bopape

**Journal**: *Theoretical and Applied Climatology* · **DOI**: [10.1007/s00704-026-06337-1](https://doi.org/10.1007/s00704-026-06337-1) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Abstract not available. Based on the title, the study applies a land surface model to simulate riverflow in the Limpopo River Basin, a transboundary, semi-arid catchment spanning South Africa, Botswana, Zimbabwe, and Mozambique.

---

### New generic coupling adapters for ice sheet and subglacial hydrology models (ISSM-preCICE Adapter 0.4, CUAS-MPI 0.1)

**Authors**: Daniel Abele, T. Kleiner, Yannic Fischler, B. Uekermann, G. Chourdakis, M. Morlighem et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-5019-2026](https://doi.org/10.5194/gmd-19-5019-2026) · **Citations**: 0

**Matched topics**: hydrology
{: .label .label-green }

> The authors use the preCICE coupling library to connect the Ice-sheet and Sea-level System Model (ISSM) with the subglacial hydrology model CUAS-MPI, building generic adapters that pass meshes and coupled variables between the models without requiring monolithic, ad-hoc coupling code. Performance tests on an HPC cluster show low computational overhead and stable scaling for both unidirectional and bidirectional coupling, with the adapters designed to be reusable for coupling tasks beyond ice-hydrology interaction, including global Earth System Models or other process models.

---

## Water Resources Management & Irrigation

Two papers approach water management from the angle of human decisions and Earth observation. Zhang and Chui propose a bi-level multiagent framework for socio-hydrologic dynamics, explicitly modeling how strategy-driven actor behavior interacts with uncertainty in watershed water-resource systems — a step toward representing human decision-making as a dynamic, strategic process rather than a static boundary condition in hydrologic models. Rossi et al. survey 83 peer-reviewed studies (2002–2025) on remote sensing for irrigation water management, synthesizing progress in multi-sensor integration, UAV-based monitoring, and machine-learning-enhanced irrigation scheduling and soil-moisture estimation, while flagging persistent gaps in model transferability, ground validation, and the translation of remote-sensing outputs into operational decision support — a useful state-of-the-field reference for irrigation and agro-hydrological modeling work.

### Modeling Strategy-Driven Socio-Hydrologic Dynamics in Uncertain Watershed Water Resource Systems Using a Bi-level Multiagent Framework

**Authors**: Mengxiang Zhang, T. M. Chui

**Journal**: *Water Resources Management* · **DOI**: [10.1007/s11269-026-04770-5](https://doi.org/10.1007/s11269-026-04770-5) · **Citations**: 0

**Matched topics**: hydrologic model
{: .label .label-green }

> Abstract not available. Based on the title, the paper proposes a bi-level multiagent modeling framework to capture how strategy-driven actor behavior shapes socio-hydrologic dynamics in watershed water resource systems under uncertainty.

---

### Remote Sensing for Irrigation Water Management Under Climate Change: Advances, Challenges, and Future Directions

**Authors**: Hala Rossi, E. Cherif, El Mustapha Azzirgue, Hamza El Azhari, Hakim Boulaassal, O. E. Kharki

**Journal**: *Climate* · **DOI**: [10.3390/cli14060124](https://doi.org/10.3390/cli14060124) · **Citations**: 0

**Matched topics**: climate change
{: .label .label-green }

> With irrigated agriculture accounting for 70% of global freshwater withdrawals, this review synthesizes 83 peer-reviewed studies (2002–2025) on optical, thermal, and microwave remote sensing for monitoring soil moisture, evapotranspiration, crop growth, and irrigation performance. It highlights progress in multi-sensor integration, UAV-based monitoring, and machine-learning approaches for irrigation scheduling and crop water-stress detection, while noting persistent challenges in data integration, model transferability, ground validation, and policy-level gaps that limit operational use.

---

## Climate Change Impacts on Water & Compound Hazards

Mohammadi and Mostafazadeh's scoping review of 92 studies (1999–2025) maps extreme and compound climate hazards across Iranian urban areas, finding that the country is experiencing "hydroclimate whiplash" — abrupt transitions between drought and flood — compounded by urbanization-driven increases in impervious surfaces and surface runoff, plus coastal exposure to sea-level rise and storm-driven compound flooding. It's a useful regional case study reinforcing the broader literature on non-stationary hydroclimate extremes under warming.

### Intensification of Extreme and Compound Hazards in Urban Areas Under Climate Change in Iran: A Scoping Review

**Authors**: Niloofar Mohammadi, R. Mostafazadeh

**Journal**: *Climate* · **DOI**: [10.3390/cli14060126](https://doi.org/10.3390/cli14060126) · **Citations**: 0

**Matched topics**: climate change
{: .label .label-green }

> This scoping review synthesizes 92 studies (1999–2025) on extreme and compound climate hazards in Iranian urban areas, covering heatwaves, drought, torrential rainfall, sea-level rise, and compound events. Western Iran faces high torrential-rainfall risk amplified by urbanization-driven runoff, coastal areas show high vulnerability to compound flooding from sea-level rise and storms, and the country overall is experiencing "hydroclimate whiplash" — abrupt drought-to-flood transitions driven by global warming.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 14 |
| After deduplication | 10 |
| After LLM relevance filtering | 6 |
| Rejected (not relevant) | 4 |

**Note**: OpenAlex's search API returned HTTP 429 (rate limited) for every query during this run; all 14 fetched papers came from Semantic Scholar only. Coverage for this week should be treated as a lower bound, not a complete picture of the literature published Jun 8–15.

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Climate | 2 |
| Geoscientific Model Development | 1 |
| Journal of Hydrometeorology | 1 |
| Theoretical and Applied Climatology | 1 |
| Water Resources Management | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

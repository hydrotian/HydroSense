---
layout: default
title: "Week 01 (December 29 - January 4), 12 papers"
parent: January
grand_parent: "2026"
nav_order: 33
date: 2026-01-04
categories: [weekly, 2026, january]
tags: [hydrology, literature-review, research]
paper_count: 12
highlight: "A bibliometric synthesis of 152,000+ papers charts a century of drought research as deep learning becomes a first-class tool for streamflow and reservoir modeling."
lang: en
lang_link: /zh/2026/january/2026-01-04-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 01** · December 29, 2025 – January 4, 2026
{: .text-grey-dk-000 }

**12** relevant papers found across **4** themes
{: .fs-5 .fw-300 }

## Executive Summary

The first ISO week of 2026 — spanning the new-year rollover — delivered an unusually cohesive set of papers on drought science, deep learning for streamflow, and cold-region and water-tower hydrology. A century-scale bibliometric review in Water Resources Research synthesizes 152,000+ drought papers, while two Earth's Future studies expose the climatic and subsurface drivers of baseflow drought and record-shattering compound drought–heatwave events. Methodologically, the standout contribution is a WRR paper that opens the LSTM black box using hydrology-specific explainable-AI, probing whether deep rainfall–runoff models' internal reasoning is physically defensible — a question that defines the next phase of ML–hydrology integration.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Drought Science: Centuries, Compounds, and Baseflows

Three complementary papers reshape how we think about drought. Sabut and Mishra mine a century of drought research (1900–2023) using bibliometric analysis of over 152,000 publications, mapping the methodological evolution from statistical modeling through satellite remote sensing to machine learning, and charting the emerging frontier of attribution to human influence. Ghaneei et al. turn to a less studied but decisive component — baseflow — and use the DeepBase dataset and explainable machine learning to show that baseflow drought in the western U.S. has intensified over four decades, driven mainly by atmospheric water-balance anomalies and soil properties, while eastern trends are declining. Li et al. zoom in on the most dangerous tail of drought: record-shattering compound drought–heatwave events, which their nine-member ensemble projects to double in annual probability between 2015 and 2040 under SSP5-8.5, with disproportionate impacts on southern North America, northern South America, and southern Europe.

### A Century of Drought Research (1900–2023): Scientific Developments, Methodological Innovations, and Emerging Frontiers

**Authors**: A. Sabut, A. Mishra

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025WR041987](https://doi.org/10.1029/2025WR041987) · **Citations**: 4

**Matched topics**: hydrologic model, drought, land surface model
{: .label .label-green }

> Synthesizes 1900–2023 drought research through bibliometric analysis of over 152,000 peer-reviewed publications. Traces the evolution from ancient climatic reconstructions through statistical and probabilistic modeling, to machine learning, deep learning, and satellite-based hydrological and land-surface modeling. Highlights emerging frontiers including human-influence attribution and the integration of climate-variability understanding into drought process representation.

---

### Four Decades of Baseflow Drought Analysis Reveals Varying Contributions of Climatic Drivers and Physical Controls

**Authors**: P. Ghaneei, E. Foroumandi, K. Stahl, H. Ajami, N. Wanders, H. Moradkhani

**Journal**: *Earth's Future* · **DOI**: [10.1029/2025EF006934](https://doi.org/10.1029/2025EF006934) · **Citations**: 2

**Matched topics**: hydrology, hydrologic model, streamflow, drought, earth system model
{: .label .label-green }

> Uses the long-term DeepBase baseflow dataset and explainable machine learning to quantify the evolution of baseflow drought (BFD) across the contiguous US over four decades. The western US — especially the Southwest — shows increased BFD frequency and duration, while much of the east trends downward. BFD frequency is governed mainly by atmospheric water-balance anomalies and soil properties, while duration is controlled by hydrogeological characteristics — evidence that subsurface controls cannot be ignored in drought attribution.

---

### Understanding the Dynamics of Record-Shattering Compound Drought-Heatwave Events and Their Impacts on Ecosystems

**Authors**: B. Li, K. Y. Liu, M. Wang, Y. Yang, M. He, Y. Wang et al.

**Journal**: *Earth's Future* · **DOI**: [10.1029/2024EF005714](https://doi.org/10.1029/2024EF005714) · **Citations**: 2

**Matched topics**: drought, land surface model, earth system model
{: .label .label-green }

> Uses a nine-member ensemble under three future scenarios to project that record-shattering compound drought–heatwave (CDHW) events — exceeding historical severity by more than two standard deviations — will double in annual probability between 2015 and 2040 under SSP5-8.5. Identifies southern North America, northern South America, and southern Europe as most vulnerable, with record-shattering CDHW events distinguished from ordinary ones by weaker water-vapor transport, reduced convection, and larger ecosystem impacts.

---

## Explainable Deep Learning for Rainfall–Runoff and Reservoir Operations

A triplet of deep-learning papers moves the conversation past predictive accuracy toward interpretability and operational integration. Bayati et al. develop a hydrology-specific explainable-AI framework that extracts nonlinear, lag-dependent, time-varying impulse response functions from trained LSTMs — revealing how these models internalize streamflow generation from precipitation, temperature, and PET, and providing the first structured way to ask whether their reasoning is physically defensible. Yang et al. pair an LSTM with the Xin'anjiang (XAJ) conceptual model and EEMD signal decomposition for multi-step runoff forecasting, combining physical priors with data-driven flexibility. Zhu et al. integrate deep learning with an improved multi-objective optimization algorithm to schedule cascade reservoir operations while satisfying ecological dissolved-oxygen constraints — an operationally oriented use of ML that broadens beyond prediction to decision support.

### Evaluating the Functional Realism of Deep Learning Rainfall-Runoff Models Using Catchment Hydrology Principles

**Authors**: A. Bayati, A. Ameli, S. Razavi

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025WR040076](https://doi.org/10.1029/2025WR040076) · **Citations**: 5

**Matched topics**: hydrology, hydrologic model, runoff, streamflow, land surface model
{: .label .label-green }

> Introduces a hydrology-specific explainable-AI framework that extracts nonlinear, lag-dependent, time-varying Impulse Response Functions from trained LSTMs, quantifying the isolated influence of precipitation, temperature, and potential evapotranspiration on simulated streamflow. The framework offers the first structured way to test whether the internal reasoning of deep rainfall-runoff models aligns with defensible catchment-hydrology mechanisms — a cornerstone for responsible integration of ML into operational hydrology.

---

### Development of a Two-Stage LSTM for Multi-Step Runoff Forecasting Using a XAJ Model and EEMD

**Authors**: Z. Yang, Q. Dong, X. Zhang, H. Zhu, Z. Cheng

**Journal**: *Water Resources Management* · **DOI**: [10.1007/s11269-025-04420-2](https://doi.org/10.1007/s11269-025-04420-2) · **Citations**: 4

**Matched topics**: hydrologic model, runoff, water management
{: .label .label-green }

> Combines the Xin'anjiang (XAJ) conceptual hydrologic model with a two-stage LSTM architecture and Ensemble Empirical Mode Decomposition (EEMD) signal processing for multi-step runoff forecasting. The hybrid approach blends physical priors from XAJ with data-driven flexibility from LSTM to improve multi-horizon runoff prediction.

---

### Integration of deep learning and improved multi-objective algorithm to optimize cascade reservoirs operation with consideration of ecological dissolved oxygen needs

**Authors**: Z. Zhu, H. Li, Z. Wang, X. Zhang, Z. Tan

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134899](https://doi.org/10.1016/j.jhydrol.2025.134899) · **Citations**: 2

**Matched topics**: hydrology, reservoir, hydropower
{: .label .label-green }

> Integrates deep learning with an improved multi-objective optimization algorithm to schedule cascade reservoir operations, explicitly accounting for ecological dissolved-oxygen requirements alongside hydropower and flood-control objectives. Extends ML applications in hydrology from prediction into decision support for multi-objective water-resource operations.

---

## Water Towers, Runoff Drivers, and Soil-Moisture Coupling

Three papers sharpen how we quantify runoff generation and its drivers. Yue et al. reconstruct Central China Water Tower (CCWT) runoff back to 1595 CE using a dendrochronological network of 100 tree-ring sites, then compare with similar records from six Pacific Rim water towers to show that the CCWT provides the most stable water supply while the Tibetan Plateau is most prone to extreme runoff; 21st-century projections indicate rising runoff for most Pacific Rim water towers, with the Northern Rockies as a substantial exception. Palumbo et al. apply causal inference to historical Upper Colorado River Basin data and find that runoff efficiency is boosted by higher precipitation, larger snowpack, cooler springs, and delayed vegetation phenology — while summer temperature, often invoked as a driver, is not statistically significant. Feng et al. take the calibration route, extending a rank-correlation-based soil-moisture calibration approach from basin to grid-by-grid scale within VIC, enabling streamflow simulation in data-sparse regions where ground observations are unavailable.

### Runoff Reconstructions and Future Projections Indicate Highly Variable Water Supply From Pacific Rim Water Towers

**Authors**: W. Yue, M. C. A. Torbenson, F. Chen, F. Reinig, J. Esper, E. Martínez del Castillo et al.

**Journal**: *AGU Advances* · **DOI**: [10.1029/2025AV002053](https://doi.org/10.1029/2025AV002053) · **Citations**: 2

**Matched topics**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> Uses a 100-site tree-ring network to reconstruct Central China Water Tower runoff back to 1595 CE, then compares with records from six Pacific Rim water towers (Mongolian Plateau, Tibetan Plateau, Great Dividing Range, Northern and Southern Rockies, Andes). The CCWT provides the most stable water supply; the Tibetan Plateau is most susceptible to extreme runoff. 21st-century projections show generally rising runoff across the Pacific Rim, with the Northern Rockies projected to decline substantially.

---

### Precipitation, moderated by spring temperature and vegetation, drives runoff efficiency in the Upper Colorado River Basin

**Authors**: D. Palumbo, S. Gangopadhyay, U. Lall

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-025-03136-w](https://doi.org/10.1038/s43247-025-03136-w) · **Citations**: 1

**Matched topics**: river, runoff, streamflow
{: .label .label-green }

> Uses causal inference on historical Upper Colorado River Basin data to identify drivers of surface runoff efficiency. Runoff efficiency rises with higher precipitation, larger snowpack, cooler spring temperatures, and delayed vegetation phenology; it falls in drier, warmer springs when vegetation activity accelerates. Notably, summer temperature — often invoked as a drying driver — does not emerge as statistically significant. Extreme precipitation phases are linked to distinct atmospheric circulation patterns and sea-surface temperature anomalies.

---

### Optimizing Soil Moisture-Runoff Coupling Strength With Remotely Sensed Soil Moisture for Improved Hydrological Modeling

**Authors**: H. Feng, J. Zhou, Z. Wu, J. Dong, L. Brocca, L. Zhao

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2024WR039571](https://doi.org/10.1029/2024WR039571) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow
{: .label .label-green }

> Extends a rank-correlation calibration approach that exploits remotely sensed soil moisture from basin-level to grid-by-grid parameter calibration within the Variable Infiltration Capacity (VIC) model, coupled with routing for streamflow simulation. Enables hydrological model calibration in data-sparse regions where ground streamflow observations are unavailable.

---

## Process Foundations: Cold Regions, Model Parameters, and Catchment Nutrients

Three papers anchor hydrological modeling in its process foundations. Zhao et al. publish a Reviews of Geophysics synthesis on frozen-soil hydrology, cataloging recent advances in freeze–thaw dynamics, preferential flow, groundwater–permafrost interactions, and resulting shifts in streamflow seasonality — while laying out a tiered modeling roadmap for the scaling and parameterization gaps that remain. Clerc-Schwarzenbach et al. take on an uncomfortable modeling habit: "sweep parameters" that let water enter or leave bucket-type catchment models through paths beyond precipitation, evaporation, and streamflow. Rather than condemning the practice, they argue these parameters can legitimately represent real processes and often improve both robustness and performance, as long as they are transparently documented. Jiang et al. apply a process-based catchment model (HYPE) to a subtropical Chinese catchment and find that climate change plays a larger role than land-use change in driving hydrology, but climate change amplifies land-use effects on dissolved inorganic nitrogen export — underlining why water-quality projections must be run under coupled climate–LULC scenarios.

### Frozen Soil Hydrological Processes and Their Effects: A Review and Synthesis

**Authors**: Y. Zhao, C. Zheng, A. Gelfan, K. Watanabe, H. Liu, S. Wright et al.

**Journal**: *Reviews of Geophysics* · **DOI**: [10.1029/2024RG000839](https://doi.org/10.1029/2024RG000839) · **Citations**: 1

**Matched topics**: hydrology, hydrologic model, streamflow, land surface model
{: .label .label-green }

> Synthesizes recent advances in the physics, observation, and modeling of frozen-soil hydrology, covering freeze-thaw dynamics, preferential flow, groundwater-permafrost interactions (including talik development), and resulting shifts in streamflow seasonality. Reviews progress in in situ sensing, geophysics, and remote sensing, and in land-surface and tracer-aided model representation of phase change, macropore bypass, and vapor transport. Outlines persistent challenges in scaling, ice-impeded hydraulics, and abrupt thaw, and proposes a tiered modeling path forward.

---

### Cheeky Cheating or a Sensible Strategy? 'Sweep Parameters' in Bucket-Type Hydrological Models

**Authors**: F. Clerc-Schwarzenbach, P. C. Astagneau, E. Muñoz Castro, I. van Meerveld, J. Seibert, V. Andréassian

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70375](https://doi.org/10.1002/hyp.70375) · **Citations**: 1

**Matched topics**: hydrology, hydrologic model, streamflow, land surface model
{: .label .label-green }

> Examines "sweep parameters" — parameters in bucket-type hydrological models that allow water to enter or leave the catchment through paths other than precipitation, evaporation, and streamflow. Argues that while such parameters can be seen as fixing the water balance "by the back door", they are in fact ubiquitous, transparent when acknowledged, and sometimes represent real physical processes. Empirical results show they do not reduce robustness under meteorological perturbations and often improve streamflow simulation.

---

### Climate change expected to amplify land-use change impacts on nitrogen export from a subtropical catchment in China

**Authors**: S. Jiang, A. D. Werner, L. Gao, M. Rode

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134888](https://doi.org/10.1016/j.jhydrol.2025.134888) · **Citations**: 2

**Matched topics**: hydrology, hydrologic model, runoff, streamflow, climate change
{: .label .label-green }

> Applies the HYPE hydrological model, calibrated with PEST and Differential Evolution Markov Chain algorithms, to the Yifeng River catchment in subtropical China to study dissolved inorganic nitrogen (DIN) export. Finds that climate change plays a larger role than land-use change in driving hydrology, but climate change amplifies land-use impacts on DIN export — reinforcing the need for coupled climate–LULC scenarios in water-quality projections.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers before dedup | 2,238 |
| Unique papers after dedup | 2,040 |
| After relevance filtering | 12 |
| Rejected (not relevant) | 2,028 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

**Sort mode**: established (citation-count-first for retrofit searches)

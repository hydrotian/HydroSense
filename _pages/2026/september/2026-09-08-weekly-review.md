---
layout: default
title: "Week 36 (Sep 01 - Sep 08), 5 papers"
parent: September
grand_parent: "2026"
nav_order: 33
date: 2026-09-08
categories: [weekly, 2026, september]
tags: [hydrology, literature-review, research]
paper_count: 5
lang: en
lang_link: /zh/2026/september/2026-09-08-weekly-review
highlight: "ORCHIDEE gains improved soil macroporosity and snow densification physics this week, alongside new LSM parameterizations for leaf turnover and rootzone soil moisture bias in hyper-resolution simulations."
---

# Weekly Literature Review
{: .no_toc }

**Week 36** · September 01–September 08, 2026
{: .text-grey-dk-000 }

**5** relevant papers found across **3** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's literature centers on land surface model process improvement and hydrologic modeling under precipitation uncertainty. Three studies advance the physical realism of water-cycle representation in land surface models — addressing soil vertical heterogeneity, soil macroporosity subgrid effects, and snowpack densification over ice sheets — while a fourth improves vegetation phenology in a grassland land surface model. A fifth study interrogates whether gridded precipitation products actually improve SWAT+ streamflow simulation in data-scarce monsoonal mountain catchments, finding no consistent performance advantage over gauge-based inputs.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Soil Physics and Water Partitioning in Land Surface Models

Accurate representation of soil hydraulic processes remains a persistent challenge in land surface models. Krishnan et al. demonstrate that accounting for soil vertical heterogeneity substantially reduces rootzone soil moisture bias in a hyper-resolution (30 m) configuration of a land surface model applied to smallholder agricultural systems — a finding with implications for global LSM calibration where the default assumption of vertically uniform soil properties introduces systematic errors. At the 100-km scales typical of coupled ESMs, Kiałka et al. show that soil macroporosity — long neglected in large-scale models — significantly alters drainage and the runoff–infiltration partition in ORCHIDEE, and that subgrid parametrization choices mediate how strongly this effect projects onto large-scale water cycle fluxes. Together, these studies highlight a vertical dimension (within-profile heterogeneity) and a horizontal dimension (subgrid structure) that are both consequential for LSM water cycle fidelity and have historically been underparameterized.

### Soil vertical heterogeneity reduces rootzone soil moisture bias in hyper-resolution land surface model over smallholder agricultural systems

**Authors**: Vishnu U. Krishnan, N. Vergopolan, B. B. Singh, J. Indu, L. Karthikeyan

**Journal**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2026.110673](https://doi.org/10.1016/j.agwat.2026.110673) · **Citations**: 2

**Matched topics**: land surface model
{: .label .label-green }

> Abstract not available.

---

### Subgrid parametrizations mediate the large‐scale effects of soil macroporosity on the water cycle in the ORCHIDEE land surface model

**Authors**: Filip Kiałka, V. Bastrikov, Omar Flores, K. Naudts, S. Luyssaert, Bertrand Guenet

**Journal**: *Vadose Zone Journal* · **DOI**: [10.1002/vzj2.70136](https://doi.org/10.1002/vzj2.70136) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Soil structure is nearly as important as soil texture in determining the soil hydraulic properties at the core scale. At plot scale, soil structure—and particularly soil macroporosity—strongly affects drainage and the runoff–infiltration partition. At the 100‐km scale typical for land surface models, the effect of macroporosity on the water cycle is modulated by the choice of subgrid parametrization scheme.

---

## Cryosphere and Vegetation Processes in Earth System Models

Two studies this week extend the process envelope of land surface models into domains where phenological and cryospheric dynamics interact with the broader water and carbon cycles. Conesa et al. implement dry snow initialization and densification physics for ice sheet applications in ORCHIDEE, enabling more accurate snowpack evolution over Greenland and Antarctica — a component with direct consequences for surface mass balance closure and sea-level projections. Working in a contrasting biome, Seitz et al. introduce a physiologically driven leaf turnover scheme for grasslands in the QUINCY land surface model, grounding a previously empirical process in mechanistic principles that better couple vegetation turnover rates to climate forcing. Both developments reflect a broader trend in the LSM community: moving from empirically tuned relationships toward process-based representations that are more transferable across climate regimes.

### Dry snow initialization and densification over the Greenland and Antarctic ice sheets in the ORCHIDEE land surface model

**Authors**: Philippe Conesa, C. Agosta, S. Charbit, C. Dumas, Simon Beylat, N. Raoult

**Journal**: *The Cryosphere* · **DOI**: [10.5194/tc-20-4973-2026](https://doi.org/10.5194/tc-20-4973-2026) · **Citations**: 1

**Matched topics**: land surface model
{: .label .label-green }

> Accurate modeling of the snowpack over ice sheets is essential for quantifying their surface mass balance contribution and their resulting impact on sea level rise. The snowpack evolution is largely governed by surface climate but also by internal processes such as densification. In land surface models, these processes must be accurately initialized and dynamically represented to reproduce observed snow density profiles and surface mass balance.

---

### A general physiologically driven representation of leaf turnover in grasslands in the QUINCY land surface model

**Authors**: Josua Seitz, Midori Yajima, Yu Zhu, L. S. K. Joseph, Jin-Yan Yang, F. Lacroix et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-8289-2026](https://doi.org/10.5194/gmd-19-8289-2026) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Terrestrial vegetation plays an important role in shaping the Earth's climate due to its control on the global carbon cycle. Understanding and predicting vegetation phenology and biomass turnover into soil organic matter is therefore of great importance for our understanding and quantification of land–climate feedbacks in Earth system models.

---

## Precipitation Uncertainty in Streamflow Simulation

De la Fraga et al. evaluate four precipitation input datasets — combinations of gauge observations and gridded products — on SWAT+ model performance in a mountainous Mexican catchment with a monsoonal climate. The study contributes to an ongoing debate about whether the spatial density of gridded precipitation offsets its well-documented biases in orographic settings. The finding that no single product consistently improves upon gauge-only inputs underscores the site-specific nature of precipitation input sensitivity and the difficulty of generalizing across topographic and climatic contexts — a relevant challenge for large-scale river routing models that must specify precipitation fields globally.

### Hydrologic modeling in mountainous terrains with monsoonal climate: Do gridded precipitation data improve streamflow simulations?

**Authors**: Pasquinel de la Fraga, E. Vivoni, Yalina Montecelos-Zamora, Francisco José Del-Toro-Guerrero, Tereza Cavazos, T. Kretzschmar

**Journal**: *Frontiers in Water* · **DOI**: [10.3389/frwa.2026.1788195](https://doi.org/10.3389/frwa.2026.1788195) · **Citations**: 0

**Matched topics**: hydrologic model
{: .label .label-green }

> Accurate hydrologic modeling in data-scarce mountainous regions remains challenging due to strong climatic variability, complex topography, and limited ground data. This study evaluates the influence of four precipitation inputs on the performance of the Soil and Water Assessment Tool Plus (SWAT+) model in a monsoonal mountain catchment, comparing gridded products against gauge-based inputs to determine whether improved spatial coverage translates to better streamflow simulation.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 9 |
| After deduplication | 8 |
| After LLM relevance filtering | 5 |
| Rejected (not relevant) | 3 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Vadose Zone Journal | 1 |
| Agricultural Water Management | 1 |
| The Cryosphere | 1 |
| Geoscientific Model Development | 1 |
| Frontiers in Water | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

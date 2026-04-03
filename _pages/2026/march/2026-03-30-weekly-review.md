---
layout: default
title: "Week 14 - Literature Review"
parent: March
grand_parent: "2026"
nav_order: 34
date: 2026-03-30
categories: [weekly, 2026, march]
tags: [hydrology, literature-review, research]
---

# Weekly Literature Review
{: .no_toc }

**Week 14** · March 23–30, 2026
{: .text-grey-dk-000 }

**20** relevant papers found across **5** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's literature features significant advances in drought projection methodology and land surface modeling. A notable finding from Environmental Research Climate challenges the accuracy of standard drought projections by demonstrating that neglecting plant physiological responses to elevated CO₂ leads to systematic overestimation of future drought severity. In parallel, two new land surface models — NoahPy (a differentiable Noah LSM for permafrost) and ClimaLand (designed for data-driven parameterizations) — represent the growing convergence of physics-based modeling and machine learning. A study in JAMES on machine learning calibration of groundwater table depth in ELM is particularly relevant to the E3SM community, demonstrating substantial improvements in hydrological cycling when GWTD representations are corrected.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Drought Projections and Climate Change Impacts

Drought under climate change received strong attention this week, with studies spanning continental to basin scales. Stagl et al. project hydrological drought trajectories across Europe using multi-model ensembles, finding intensifying drought conditions under both moderate and high-emission scenarios. Fowler et al. tackle the persistent uncertainty in Australian drought projections by analyzing seasonal drought changes, finding that despite disagreement in precipitation projections, streamflow drought intensification is robust across models. Tian et al. investigate the critical but often overlooked role of reservoirs in modifying drought-to-flood propagation in the Lancang-Mekong River Basin. Importantly, Slater et al. argue that most drought projections systematically overestimate drought severity by neglecting plant physiological responses to elevated CO₂, which reduces stomatal conductance and thus actual evapotranspiration — with major implications for water resource planning.

### Hydrological drought projections across Europe under climate change

**Authors**: J. Stagl et al.

**Journal**: *npj Natural Hazards* · **DOI**: [10.1038/s44304-025-00152-w](https://doi.org/10.1038/s44304-025-00152-w) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow, drought, climate change
{: .label .label-green }

> Projects hydrological drought trajectories across Europe using multi-model ensembles under moderate and high-emission scenarios, finding intensifying drought conditions across the continent.

---

### Future changes in seasonal drought in Australia

**Authors**: A. Ukkola, S. Thomas, E. Vogel, U. Bende-Michl, S. T. Siems, V. Matic et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-1463-2026](https://doi.org/10.5194/hess-30-1463-2026) · **Citations**: 4

**Matched topics**: hydrologic model, streamflow, drought, seasonal
{: .label .label-green }

> Uses the National Hydrological Projections ensemble to assess future drought changes in Australia, finding that despite disagreement in precipitation projections, streamflow drought intensification is robust across models.

---

### Mitigating drought-flood abrupt alternation: role of reservoirs in the Lancang-Mekong Basin

**Authors**: Z. Tian et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-671-2026](https://doi.org/10.5194/hess-30-671-2026) · **Citations**: 0

**Matched topics**: flood, drought
{: .label .label-green }

> Investigates the role of reservoirs in modifying drought-to-flood propagation in the Lancang-Mekong River Basin, showing that reservoir operations can substantially mitigate drought-flood abrupt alternation events under climate change.

---

### Neglecting plant physiology leads to systematic overestimation of drought projections

**Authors**: L. Slater et al.

**Journal**: *Environmental Research Climate* · **DOI**: [10.1088/2752-5295/ae583c](https://doi.org/10.1088/2752-5295/ae583c) · **Citations**: 0

**Matched topics**: hydrology, streamflow, drought
{: .label .label-green }

> Demonstrates that neglecting plant physiological responses to elevated CO₂ leads to systematic overestimation of future drought severity, as reduced stomatal conductance lowers actual evapotranspiration. Has major implications for water resource planning under climate change.

---

### The Future of Snowpack Drought in the Upper Colorado River Basin (USA)

**Authors**: Authors not listed

**Journal**: *Hydrology* · **DOI**: [10.3390/hydrology13040100](https://doi.org/10.3390/hydrology13040100) · **Citations**: 0

**Matched topics**: river, runoff, streamflow, drought
{: .label .label-green }

> Examines future snowpack drought projections in the Upper Colorado River Basin, a critical water supply region for the western United States.

---

## Land Surface Models and Earth System Modeling

A cluster of papers advances land surface modeling through machine learning integration. Li et al. present NoahPy, a differentiable version of the Noah land surface model targeting permafrost thermo-hydrology. Wang et al. introduce ClimaLand, a new LSM designed specifically to accommodate data-driven parameterizations. Of particular note for the E3SM community, a study on ML calibration of groundwater table depth in ELM demonstrates that correcting GWTD biases significantly improves land surface hydrology and land-atmosphere fluxes. Additionally, Salimi et al. enhance glacier and ice sheet representation in the ECMWF ecLand model.

### NoahPy: a differentiable Noah LSM for permafrost thermo-hydrology

**Authors**: W. Tian, H. Yu, S. Zhao, Y. Cao, W. Yi, J. Xu et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-57-2026](https://doi.org/10.5194/gmd-19-57-2026) · **Citations**: 1

**Matched topics**: hydrology, land surface model, earth system model
{: .label .label-green }

> Creates a differentiable version of the Noah LSM to enable hybrid models that synergize process-based physics with deep learning for permafrost simulation, opening the door to automatic parameter calibration and hybrid physics-ML approaches for cold-region hydrology.

---

### ClimaLand: A Land Surface Model for Data-Driven Parameterizations

**Authors**: K. Deck, R. K. Braghiere, A. A. Renchon, J. Sloan, G. Bozzola, E. Speer et al.

**Journal**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025ms005118](https://doi.org/10.1029/2025ms005118) · **Citations**: 3

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> A new land surface model specifically designed to enable data-driven parameterizations of sub-grid processes, offering a framework where traditional parameterizations can be replaced or augmented with machine learning components.

---

### ML Calibration of Groundwater Table Depth in ELM

**Authors**: Authors not listed

**Journal**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025MS005184](https://doi.org/10.1029/2025MS005184) · **Citations**: 0

**Matched topics**: hydrology, land surface model
{: .label .label-green }

> Demonstrates that correcting groundwater table depth biases using machine learning significantly improves land surface hydrology and land-atmosphere fluxes in the E3SM Land Model (ELM).

---

### Enhancing Glaciers and Ice Sheets in ecLand

**Authors**: S. Salimi et al.

**Journal**: *The Cryosphere* · **DOI**: [10.5194/tc-20-1119-2026](https://doi.org/10.5194/tc-20-1119-2026) · **Citations**: 0

**Matched topics**: hydrology, land surface model
{: .label .label-green }

> Enhances glacier and ice sheet representation in the ECMWF ecLand model, improving surface energy balance and meltwater hydrology across scales.

---

### Advancing ecohydrological modelling: LPJ-GUESS with ParFlow

**Authors**: Z. Jia, S. Chen, Y. H. Fu, D. Martín Belda, D. Wårlind, S. Olin et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-1727-2026](https://doi.org/10.5194/gmd-19-1727-2026) · **Citations**: 2

**Matched topics**: hydrology, hydrologic model
{: .label .label-green }

> Integrates the LPJ-GUESS dynamic vegetation model with ParFlow to capture topography-driven vegetation–surface–groundwater interactions that many Earth system models currently neglect.

---

## Reservoir Operations and Water Management

Reservoir impacts on hydrology received attention from multiple angles. Vicente-Serrano et al. analyze a century of discharge trends in the Mediterranean Basin (1914–2022), finding that vegetation greening and reservoir construction — not just climate change — are major drivers of declining streamflow. Li et al. demonstrate the use of SWOT satellite data integrated with multi-source observations for near-daily reservoir water level monitoring. Wu et al. quantify previously underestimated evaporation losses from reservoir development on the Loess Plateau.

### Vegetation greening and reservoir construction as drivers of discharge trends in the Mediterranean

**Authors**: S. M. Vicente-Serrano et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135387](https://doi.org/10.1016/j.jhydrol.2026.135387) · **Citations**: 0

**Matched topics**: runoff, streamflow, reservoir
{: .label .label-green }

> Analyzes a century of discharge trends in the Mediterranean Basin (1914–2022), finding that vegetation greening and reservoir construction are major drivers of declining streamflow alongside climate change.

---

### Rolling predictive optimal scheduling of reservoirs for flood control and power generation

**Authors**: Authors not listed

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-43532-6](https://doi.org/10.1038/s41598-026-43532-6) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, reservoir
{: .label .label-green }

> Develops rolling predictive optimal scheduling under prediction uncertainty to balance flood control and hydropower generation objectives for reservoir operations.

---

### Integrating SWOT for Near-Daily Reservoir Water Level Monitoring

**Authors**: P. Zhan, J. Wang, T. Chen, S. Luo, K. Liu, L. Ke et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2024WR039711](https://doi.org/10.1029/2024WR039711) · **Citations**: 1

**Matched topics**: hydrologic model, reservoir
{: .label .label-green }

> Develops a framework integrating SWOT with multi-source satellite observations to achieve near-daily reservoir water level monitoring, advancing remote sensing capabilities for reservoir management.

---

### Increased surface water evaporation loss from reservoir development on the Loess Plateau

**Authors**: Z. Wu et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-67-2026](https://doi.org/10.5194/hess-30-67-2026) · **Citations**: 1

**Matched topics**: reservoir, surface water
{: .label .label-green }

> Quantifies previously underestimated evaporation losses from reservoir development on the Loess Plateau, revealing significant impacts on regional water budgets.

---

### Drought propagation under reservoir regulation in the Hanjiang River Basin

**Authors**: Authors not listed

**Journal**: *River* · **DOI**: [10.1002/rvr2.70045](https://doi.org/10.1002/rvr2.70045) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, reservoir, drought
{: .label .label-green }

> Examines how reservoir regulation modifies drought propagation characteristics in the Hanjiang River Basin, with implications for water management under changing climate conditions.

---

## Hydrologic Modeling Advances

Several papers advance hydrologic modeling methodology. Knoben et al. evaluate how well hydrological models simulate streamflow extremes and drought-to-flood transitions, revealing important model limitations for compound events. Poncelet et al. develop a method for tracking rainfall contributions through a conceptual runoff model, showing that wetter catchments respond more to short-term rainfall while drier catchments increasingly depend on multi-annual rainfall. Munkhjargal et al. reveal the individual contributions of topography and vegetation to catchment hydrology in cold alpine basins.

### How well do hydrological models simulate streamflow extremes and drought-to-flood transitions?

**Authors**: E. Muñoz-Castro, B. Anderson, P. C. Astagneau, D. L. Swain, P. A. Mendoza, M. I. Brunner

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-825-2026](https://doi.org/10.5194/hess-30-825-2026) · **Citations**: 4

**Matched topics**: streamflow, flood, drought
{: .label .label-green }

> Evaluates how well hydrological models capture compound extreme events — specifically floods occurring shortly after droughts — identifying which modeling decisions most influence the simulation of these increasingly important transitions.

---

### Tracking rainfall contribution in a conceptual runoff model

**Authors**: C. Poncelet et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135366](https://doi.org/10.1016/j.jhydrol.2026.135366) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow, surface water
{: .label .label-green }

> Develops a method for tracking rainfall contributions through a conceptual runoff model, showing that wetter catchments respond more to short-term rainfall while drier catchments increasingly depend on multi-annual rainfall.

---

### Revealing the influence of topography and vegetation on hydrological processes in cold alpine basins

**Authors**: M. Munkhjargal et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-1585-2026](https://doi.org/10.5194/hess-30-1585-2026) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> Reveals the individual contributions of topography and vegetation to catchment hydrology in cold alpine basins using a stepwise modeling approach.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers before dedup | 2,156 |
| Unique papers after dedup | 1,863 |
| After LLM relevance filtering | 20 |
| Rejected (not relevant) | 1,843 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

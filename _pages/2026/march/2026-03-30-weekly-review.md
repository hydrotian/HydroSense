---
layout: default
title: "Week 14 - Literature Review"
parent: March
grand_parent: "2026"
nav_order: 30
date: 2026-03-30
categories: [weekly, 2026, march]
tags: [hydrology, literature-review, research]
---

# Weekly Literature Review

**Week 14 (March 23 – March 30, 2026)**

**20** relevant papers selected out of **1,863** unique publications across **16** search topics.

## Executive Summary

This week's literature features significant advances in drought projection methodology and land surface modeling. A notable finding from Environmental Research Climate challenges the accuracy of standard drought projections by demonstrating that neglecting plant physiological responses to elevated CO₂ leads to systematic overestimation of future drought severity. In parallel, two new land surface models—NoahPy (a differentiable Noah LSM for permafrost) and ClimaLand (designed for data-driven parameterizations)—represent the growing convergence of physics-based modeling and machine learning. A study in JAMES on machine learning calibration of groundwater table depth in ELM is particularly relevant to the E3SM community, demonstrating substantial improvements in hydrological cycling when GWTD representations are corrected.

## Drought Projections and Climate Change Impacts

Drought under climate change received strong attention this week, with studies spanning continental to basin scales. **Stagl et al.** project hydrological drought trajectories across Europe using multi-model ensembles, finding intensifying drought conditions under both moderate and high-emission scenarios (*npj Natural Hazards*). **Fowler et al.** tackle the persistent uncertainty in Australian drought projections by analyzing seasonal drought changes, finding that despite disagreement in precipitation projections, streamflow drought intensification is robust across models (*HESS*, 4 citations). **Tian et al.** investigate the critical but often overlooked role of reservoirs in modifying drought-to-flood propagation in the Lancang-Mekong River Basin, showing that reservoir operations can substantially mitigate drought-flood abrupt alternation events under climate change (*HESS*).

Importantly, **Slater et al.** argue that most drought projections systematically overestimate drought severity by neglecting plant physiological responses to elevated CO₂, which reduces stomatal conductance and thus actual evapotranspiration (*Environmental Research Climate*). This has major implications for water resource planning under climate change.

| Paper | Journal | DOI | Queries | Cites |
|-------|---------|-----|---------|-------|
| Hydrological drought projections across Europe under climate change | npj Natural Hazards | [10.1038/s44304-025-00152-w](https://doi.org/10.1038/s44304-025-00152-w) | hydrologic model, runoff, streamflow, drought, climate change | 0 |
| Future changes in seasonal drought in Australia | HESS | [10.5194/hess-30-1463-2026](https://doi.org/10.5194/hess-30-1463-2026) | hydrologic model, streamflow, drought, seasonal | 4 |
| Mitigating drought-flood abrupt alternation: role of reservoirs in the Lancang-Mekong Basin | HESS | [10.5194/hess-30-671-2026](https://doi.org/10.5194/hess-30-671-2026) | flood, drought | 0 |
| Neglecting plant physiology: systematic overestimation of drought projections | Env. Res. Climate | [10.1088/2752-5295/ae583c](https://doi.org/10.1088/2752-5295/ae583c) | hydrology, streamflow, drought | 0 |
| The Future of Snowpack Drought in the Upper Colorado River Basin (USA) | Hydrology | [10.3390/hydrology13040100](https://doi.org/10.3390/hydrology13040100) | river, runoff, streamflow, drought | 0 |

## Land Surface Models and Earth System Modeling

A cluster of papers advances the state of land surface modeling through machine learning integration. **Li et al.** present **NoahPy**, a differentiable version of the Noah land surface model targeting permafrost thermo-hydrology, enabling hybrid physics-ML approaches for an area of major Earth system uncertainty (*GMD*, 1 citation). **Wang et al.** introduce **ClimaLand**, a new LSM in JAMES designed specifically to accommodate data-driven parameterizations, representing a shift toward ML-ready model architectures (*JAMES*, 3 citations).

Of particular note for the E3SM community, **a study on ML calibration of groundwater table depth in ELM** demonstrates that correcting GWTD biases significantly improves land surface hydrology and land-atmosphere fluxes in Earth system models (*JAMES*). Additionally, **Salimi et al.** enhance glacier and ice sheet representation in the ECMWF ecLand model, improving surface energy balance and meltwater hydrology across scales (*The Cryosphere*).

| Paper | Journal | DOI | Queries | Cites |
|-------|---------|-----|---------|-------|
| NoahPy: a differentiable Noah LSM for permafrost thermo-hydrology | GMD | [10.5194/gmd-19-57-2026](https://doi.org/10.5194/gmd-19-57-2026) | hydrology, land surface model, earth system model | 1 |
| ClimaLand: A Land Surface Model for Data-Driven Parameterizations | JAMES | [10.1029/2025ms005118](https://doi.org/10.1029/2025ms005118) | land surface model, earth system model | 3 |
| ML Calibration of Groundwater Table Depth in ELM | JAMES | [10.1029/2025MS005184](https://doi.org/10.1029/2025MS005184) | hydrology, land surface model | 0 |
| Enhancing Glaciers and Ice Sheets in ecLand | The Cryosphere | [10.5194/tc-20-1119-2026](https://doi.org/10.5194/tc-20-1119-2026) | hydrology, land surface model | 0 |
| Advancing ecohydrological modelling: LPJ-GUESS with ParFlow | GMD | [10.5194/gmd-19-1727-2026](https://doi.org/10.5194/gmd-19-1727-2026) | hydrology, hydrologic model | 2 |

## Reservoir Operations and Water Management

Reservoir impacts on hydrology received attention from multiple angles. **Vicente-Serrano et al.** analyze a century of discharge trends in the Mediterranean Basin (1914–2022), finding that vegetation greening and reservoir construction—not just climate change—are major drivers of declining streamflow (*Journal of Hydrology*). **A study on the Xiajiang Reservoir** develops rolling predictive optimal scheduling under prediction uncertainty to balance flood control and hydropower generation (*Scientific Reports*). **Li et al.** demonstrate the use of SWOT satellite data integrated with multi-source observations for near-daily reservoir water level monitoring, advancing remote sensing capabilities for reservoir management (*WRR*, 1 citation). **Wu et al.** quantify previously underestimated evaporation losses from reservoir development on the Loess Plateau (*HESS*, 1 citation).

| Paper | Journal | DOI | Queries | Cites |
|-------|---------|-----|---------|-------|
| Vegetation greening and reservoir construction as drivers of discharge trends in the Mediterranean | J. Hydrology | [10.1016/j.jhydrol.2026.135387](https://doi.org/10.1016/j.jhydrol.2026.135387) | runoff, streamflow, reservoir | 0 |
| Rolling predictive optimal scheduling of reservoirs for flood control and power generation | Scientific Reports | [10.1038/s41598-026-43532-6](https://doi.org/10.1038/s41598-026-43532-6) | hydrology, hydrologic model, reservoir | 0 |
| Integrating SWOT for Near-Daily Reservoir Water Level Monitoring | WRR | [10.1029/2024WR039711](https://doi.org/10.1029/2024WR039711) | hydrologic model, reservoir | 1 |
| Increased surface water evaporation loss from reservoir development on the Loess Plateau | HESS | [10.5194/hess-30-67-2026](https://doi.org/10.5194/hess-30-67-2026) | reservoir, surface water | 1 |
| Drought propagation under reservoir regulation in the Hanjiang River Basin | River | [10.1002/rvr2.70045](https://doi.org/10.1002/rvr2.70045) | hydrologic model, streamflow, reservoir, drought | 0 |

## Hydrologic Modeling Advances

Several papers advance hydrologic modeling methodology. **Knoben et al.** evaluate how well hydrological models simulate streamflow extremes and drought-to-flood transitions, revealing important model limitations for compound events (*HESS*, 4 citations). **Poncelet et al.** develop a method for tracking rainfall contributions through a conceptual runoff model, showing that wetter catchments respond more to short-term rainfall while drier catchments increasingly depend on multi-annual rainfall (*Journal of Hydrology*). **Munkhjargal et al.** reveal the individual contributions of topography and vegetation to catchment hydrology in cold alpine basins using a stepwise modeling approach (*HESS*).

| Paper | Journal | DOI | Queries | Cites |
|-------|---------|-----|---------|-------|
| How well do hydrological models simulate streamflow extremes and drought-to-flood transitions? | HESS | [10.5194/hess-30-825-2026](https://doi.org/10.5194/hess-30-825-2026) | streamflow, flood, drought | 4 |
| Tracking rainfall contribution in a conceptual runoff model | J. Hydrology | [10.1016/j.jhydrol.2026.135366](https://doi.org/10.1016/j.jhydrol.2026.135366) | hydrologic model, runoff, streamflow, surface water | 0 |
| Revealing the influence of topography and vegetation on hydrological processes in cold alpine basins | HESS | [10.5194/hess-30-1585-2026](https://doi.org/10.5194/hess-30-1585-2026) | hydrology, hydrologic model, runoff, streamflow | 0 |

## Climate Change and River Basin Studies

**Investigations of climate-driven changes in major river basins** round out this week's literature. The Yellow River Basin's dry-wet differentiation is examined using terrestrial water storage anomalies from remote sensing (*Remote Sensing*). **Hydrological response to compounding climate change and forest management** in the Upper Kings River Basin (Sierra Nevada) highlights the interaction between fire suppression legacy and warming on watershed hydrology (*Ecohydrology*, 1 citation). A review paper traces the evolution from GIS-based hydrology to AI-native spatial water intelligence (*Water*).

| Paper | Journal | DOI | Queries | Cites |
|-------|---------|-----|---------|-------|
| Dry-Wet Differentiation of the Yellow River Basin | Remote Sensing | [10.3390/rs18070974](https://doi.org/10.3390/rs18070974) | river, streamflow, climate change | 0 |
| Hydrological Response to Climate Change and Forest Management in Upper Kings River Basin | Ecohydrology | [10.1002/eco.70157](https://doi.org/10.1002/eco.70157) | river, climate change | 1 |

## Search Statistics

| Metric | Value |
|--------|-------|
| Date range | March 23 – March 30, 2026 |
| Topics searched | 16 |
| Databases | Semantic Scholar, OpenAlex |
| Total papers before dedup | 2,156 |
| Unique papers after dedup | 1,863 |
| Papers selected (relevant) | 20 |
| Selection rate | 1.1% |

**Topics searched:** hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

---

*Generated by [HydroSense](https://github.com/hydrotian/HydroSense)*

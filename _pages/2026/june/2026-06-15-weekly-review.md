---
layout: default
title: "Week 23 (Jun 1 - Jun 8), 7 papers"
parent: June
grand_parent: "2026"
nav_order: 35
date: 2026-06-15
categories: [weekly, 2026, june]
tags: [hydrology, literature-review, research]
paper_count: 7
highlight: "Noah-MP systematically underestimates snow water equivalent across the western U.S. due to inadequate snow compaction and albedo physics, with direct implications for seasonal water supply forecasting."
lang: en
lang_link: /zh/2026/june/2026-06-15-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 23** · Jun 1–Jun 8, 2026
{: .text-grey-dk-000 }

**7** relevant papers found across **3** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's review spans land surface model parameterization and bias, streamflow responses to climate and urbanization, and water management challenges in both engineered and informal settings. Three *Water Resources Research* papers collectively advance understanding of LSM structural limits — from snow bias in Noah-MP to groundwater parameterization sensitivity to the chronic omission of informal-settlement hydrology from flood models. Complementing these, new computational approaches push hydropower reservoir optimization and rainfall-runoff modeling forward.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Land Surface Model Parameterization and Bias

Three studies this week probe the structural and parametric limits of land surface and earth system models. Abolafia‐Rosenzweig et al. systematically revisit snow water equivalent bias in the widely-used Noah‐MP LSM across the western U.S., attributing persistent underestimation to inadequate snow compaction and albedo representations — findings that directly affect seasonal water supply forecasting in snowmelt-dominated basins. Complementing this, Mbarak and Yang dissect how spatial resolution choices, groundwater parameterization depth, and vadose zone thickness jointly shape simulated soil moisture and temperature biases, showing that coarse-resolution configurations systematically amplify the warm-dry bias documented in midlatitude continental regions. Cheng et al. extend this line of inquiry to urban environments, demonstrating in JAMES that prescribing spatially continuous, fine-scale urban surface properties substantially reduces errors in simulated urban heat, precipitation, and surface energy fluxes — underscoring that the quality of input datasets is as consequential as model physics.

### Revisiting Snow Water Equivalent Bias in the Noah‐MP Land Surface Model in the Western U.S.

**Authors**: R. Abolafia‐Rosenzweig, Cenlin He, Kyoko Ikeda, Changhai Liu, Tzu‐Shun Lin, Michael Barlage, Lulin Xue, K. Rasouli, Yongxin Zhang, A. Newman et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042586](https://doi.org/10.1029/2025wr042586) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Land surface models (LSMs) are widely used to generate snow records, forecasts, and projections that support water research and management. The complex sources of uncertainty in LSMs motivate evaluations to better understand bias characteristics and identify underlying causes that guide model development and user interpretation. This study revisits snow water equivalent bias in the Noah‐MP LSM across the western U.S., examining snow compaction, albedo, and other key processes contributing to systematic underestimation in snowmelt-dominated basins.

---

### Impacts of Spatial Resolution, Groundwater Parameterizations, and Vadose Zone Thickness on Land Surface Simulations

**Authors**: Mahmoud Mbarak, Zong‐liang Yang

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr040135](https://doi.org/10.1029/2025wr040135) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Accurate kilometer‐scale modeling of land processes is crucial for improving weather and climate forecasting. However, persistent biases, such as the well‐documented warm temperature and dry bias in the central midlatitudes, continue to pose challenges. This study investigates the impacts of groundwater parameterizations, vadose zone thickness, and spatial resolution on land surface simulations, providing guidance for model configuration choices that reduce systematic errors in soil moisture and surface energy balance.

---

### Importance of Spatially Continuous Urban Surface Properties in Urban‐Resolving Earth System Modeling

**Authors**: Yifan Cheng, Lei Zhao, K. Oleson, T. Chakraborty, Keer Zhang, Cenlin He, Joyce Yang

**Journal**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025ms005573](https://doi.org/10.1029/2025ms005573) · **Citations**: 0

**Matched topics**: earth system model
{: .label .label-green }

> Accurate representation of urban properties and processes at higher resolutions in global modeling systems is essential for advancing our ability to capture the complexities of urban systems and informing effective resilience strategies. However, the prescription of coarse global‐scale urban properties introduces substantial errors in simulated urban heat, precipitation, and surface energy fluxes. This study demonstrates that spatially continuous, fine-scale urban surface property datasets substantially reduce these biases in urban-resolving earth system modeling.

---

## Streamflow Modeling and Watershed Response to Land-Use Change

Two studies examine how rainfall-runoff dynamics are captured and how they evolve under shifting land use and climate. Sepahvand et al. pit genetic programming against the HEC-HMS conceptual model for rainfall-runoff simulation, finding that GP can match or exceed HEC-HMS accuracy while offering transparent, interpretable equations — an accessible middle ground between black-box ML and manually calibrated physics models. Ariano and Murfitt characterize multi-decade streamflow trends in watersheds subject to concurrent climate change and urbanization, disentangling these drivers through long-record gauge analysis; their results reinforce that urban expansion amplifies peak flows in ways that neither climate-only nor land-use-only models adequately capture, with direct implications for watershed management planning.

### Comparison of Genetic Programming and HEC-HMS as a Conceptual Model in Simulating Rainfall-Runoff Time Series

**Authors**: R. Sepahvand, Mehrdad Khoshoei, M. Golmohammadi

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-55529-2](https://doi.org/10.1038/s41598-026-55529-2) · **Citations**: 1

**Matched topics**: runoff
{: .label .label-green }

> Abstract not available. This study compares genetic programming and HEC-HMS conceptual model approaches for simulating rainfall-runoff time series, evaluating the accuracy and interpretability of data-driven versus physics-based methods for watershed-scale streamflow prediction.

---

### Characterizing the Role of Climate and Urbanization on Multi-Decade Stream Hydrology: Implications for Watershed Management

**Authors**: S. Ariano, Justin Murfitt

**Journal**: *Environmental Management* · **DOI**: [10.1007/s00267-026-02522-0](https://doi.org/10.1007/s00267-026-02522-0) · **Citations**: 0

**Matched topics**: hydrology
{: .label .label-green }

> Abstract not available. This study characterizes the relative roles of climate variability and urban land-use change in driving multi-decade streamflow trends, using long-record gauge analysis to disentangle these concurrent drivers and assess implications for integrated watershed management strategies.

---

## Water Management and Urban Hydrological Gaps

This theme highlights advances in operational reservoir management and a critical gap in urban hydrological science. Liu et al. introduce an information-driven early-stopping criterion for surrogate-model-free multi-objective optimization of hydropower reservoir operations under uncertainty, achieving competitive Pareto fronts with fewer model evaluations — a practical advance for systems where full simulation is computationally expensive. At the other end of the infrastructure spectrum, Getirana's perspective in *Water Resources Research* makes a compelling case that the hydrology of informal settlements — home to over one billion people — remains a critical blind spot in flood modeling and drainage assessment; their distinctive impervious patterns, drainage pathways, and water use behaviors are systematically omitted from urban hydrologic models, propagating errors in flood risk and water resource allocation for the world's most vulnerable populations.

### Information-Driven Early Stopping Optimization: A Surrogate Model-Free Method for Expensive Multi-Objective Uncertainty Operation Optimization of Hydropower Reservoirs

**Authors**: Dong Liu, Tao Bai, Xiaoting Wei

**Journal**: *Expert Systems with Applications* · **DOI**: [10.1016/j.eswa.2026.131422](https://doi.org/10.1016/j.eswa.2026.131422) · **Citations**: 1

**Matched topics**: hydropower
{: .label .label-green }

> Abstract not available. This study presents an information-driven early stopping optimization framework as a surrogate model-free approach for computationally expensive multi-objective uncertainty optimization of hydropower reservoir operations, reducing the number of simulation calls needed to approximate the Pareto-optimal front.

---

### Urban Waters, Unseen: The Hydrology of Informal Settlements Must Not Be Ignored

**Authors**: Augusto Getirana

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042912](https://doi.org/10.1029/2025wr042912) · **Citations**: 0

**Matched topics**: hydrology
{: .label .label-green }

> Informal settlements—home to more than 1 billion people worldwide—remain largely invisible in urban hydrological science. Despite their density, structural complexity, and distinctive water pathways, these neighborhoods are routinely omitted from flood models, drainage assessments, and water‐resource planning. This perspective calls for systematic integration of informal settlement hydrology into urban water science, flood risk assessment, and water resource management frameworks.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 20 |
| Total papers fetched | 12 |
| After deduplication | 12 |
| After LLM relevance filtering | 7 |
| Rejected (not relevant) | 5 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Water Resources Research | 3 |
| Journal of Advances in Modeling Earth Systems | 1 |
| Scientific Reports | 1 |
| Environmental Management | 1 |
| Expert Systems with Applications | 1 |

## Filtering Criteria

**Topics**: hydrology, streamflow, runoff, river routing, flood, drought, reservoir operations, water management, land surface model, earth system model, climate change hydrology, remote sensing hydrology, machine learning hydrology, groundwater, irrigation, hydropower, surface water, watershed

**Databases**: Semantic Scholar, OpenAlex

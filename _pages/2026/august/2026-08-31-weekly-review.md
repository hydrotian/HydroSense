---
layout: default
title: "Week 34 (Aug 17 - Aug 24), 6 papers"
parent: August
grand_parent: "2026"
nav_order: 36
date: 2026-08-31
categories: [weekly, 2026, august]
tags: [hydrology, literature-review, research]
paper_count: 6
lang: en
lang_link: /zh/2026/august/2026-08-31-weekly-review
highlight: "New tropical peatland scheme in JULES (Congo Basin) and N-C coupling in ISBA advance land surface model biogeochemical realism for climate-water projections."
---

# Weekly Literature Review
{: .no_toc }

**Week 34** · Aug 17–Aug 24, 2026
{: .text-grey-dk-000 }

**6** relevant papers found across **3** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's literature spans two connected scales of Earth-system modeling: at the process level, new land surface model developments bring tropical peatland hydrology (JULES/Congo Basin) and nitrogen-carbon coupling (ISBA) into large-scale frameworks that influence hydrologic projections. At the model-analysis level, methodological advances in Gaussian process emulation and a validation of overshoot emulation errors both improve the efficiency and reliability of uncertainty quantification in climate projections used for water resource assessment. Snow catchment calibration work and hydropeaking habitat metrics round out a week focused on model improvement across scales.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Land Surface Model Development

Two papers this week push the boundaries of land surface model (LSM) physics in complementary directions. A study embedded a detailed tropical peatland scheme in JULES, calibrated against Congo Basin process measurements — filling a long-standing gap in large-scale terrestrial models where peat hydrology and carbon stocks are poorly represented, with direct implications for African hydroclimate projections. Separately, another team coupled the nitrogen cycle to the carbon cycle in ISBA (SURFEX v9), evaluated against two Free-Air CO₂ Enrichment experiment sites; improved nutrient controls on photosynthesis and decomposition feed back on evapotranspiration and soil water dynamics. Together, these papers signal a maturing effort to bring biogeochemical realism into the LSMs that underpin both operational weather forecasting and long-range Earth system projections.

### Improving the representation of tropical peatland processes in the JULES land surface model using data from the central Congo Basin

**Authors**: Nair et al.

**Journal**: *Philosophical Transactions of the Royal Society B* · **DOI**: [10.1098/rstb.2024.0487](https://doi.org/10.1098/rstb.2024.0487) · **Citations**: 1

**Matched topics**: land surface model
{: .label .label-green }

> Tropical peatlands are not currently represented in large-scale terrestrial ecosystem models. Recent work in the central Congo Basin (CCB) measuring peatland processes and reconstructing peatland evolution provides new insights into the controls on peatland formation, carbon accumulation and hydrological functioning. Here, we present a new peatland scheme for the JULES land surface model, which has been developed using CCB data, and evaluate the scheme's performance against observations. The new scheme improves the representation of peat hydrology and carbon dynamics, with implications for simulating the response of tropical peatlands to climate change.

---

### Representation of the nitrogen cycle and its coupling with the carbon cycle in ISBA (SURFEX v9) the land surface model: evaluation using two Free-Air CO₂ Enrichment experiment sites

**Authors**: Zheng et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-7787-2026](https://doi.org/10.5194/gmd-19-7787-2026) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Nitrogen (N) is a critical nutrient, that controls photosynthesis and decomposition processes. It is important to include the N cycle in the land component of climate models to improve the estimation of carbon fluxes, and their response to elevated CO₂. Here, we present the nitrogen cycle in the land surface model ISBA (SURFEX v9) and its coupling with the carbon cycle. We evaluate the model against observations at two FACE experiment sites to assess model performance regarding carbon, nitrogen and water fluxes. Results show that including N cycling significantly improves the simulated ecosystem response to elevated CO₂, with downstream implications for simulated evapotranspiration and soil moisture.

---

## Hydrologic Model Calibration and Hydropower Operations

Snow-dominated headwater catchments remain among the most challenging environments for hydrologic model calibration, and this week's HESS contribution shows that multi-dataset calibration — combining streamflow with satellite snow cover and other observational products — substantially reduces parameter equifinality and improves snow water equivalent estimates relative to streamflow-only approaches. On the operational side, a study in *Environmental Management* quantifies the sub-daily hydrological signature of hydropeaking on benthic habitat availability, deriving patch-scale metrics for habitat suitability that have direct application to minimum-flow regulations and hydropower scheduling; the results underscore how discharge management decisions propagate down to habitat structure at fine spatial and temporal scales.

### Hydrologic model parameter estimation in snow-dominated headwater catchments using multiple observation datasets

**Authors**: Griessinger et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-5195-2026](https://doi.org/10.5194/hess-30-5195-2026) · **Citations**: 0

**Matched topics**: hydrologic model
{: .label .label-green }

> Hydrologic models are often calibrated using streamflow alone, but increasing availability of in situ and satellite-based observations provide numerous opportunities to constrain model output with additional variables. Here, we evaluate different multi-variable calibration strategies for snow-dominated headwater catchments, examining the use of snow cover extent, snow water equivalent, soil moisture, and evapotranspiration as additional calibration targets alongside streamflow. Multi-variable calibration systematically reduces parameter uncertainty, improves snow state estimates, and yields more physically consistent parameter sets, while slightly degrading streamflow performance — a tradeoff that depends on the intended application.

---

### Macroinvertebrate Habitat Dynamics under Frequent Hydropower-Induced Discharge Fluctuations: Patch-Scale Metrics to Quantify Effects of Hydropeaking and Morphological Complexity

**Authors**: Fröhlich et al.

**Journal**: *Environmental Management* · **DOI**: [10.1007/s00267-026-02574-2](https://doi.org/10.1007/s00267-026-02574-2) · **Citations**: 1

**Matched topics**: hydropower
{: .label .label-green }

> Hydropeaking, driven by intermittent hydropower production, induces frequent and rapid sub-daily discharge fluctuations that alter riverine habitats and cause biodiversity loss worldwide. Benthic macroinvertebrate communities are particularly vulnerable as suitable habitat patches shift dynamically with changing discharge. Using high-resolution discharge data from a regulated Alpine river, we develop patch-scale habitat suitability metrics that capture the timing and magnitude of hydropeaking-driven habitat loss. Results show that morphological complexity buffers habitat availability and that targeted channel modifications can substantially reduce hydropeaking impacts, with implications for minimum-flow policy and hydropower scheduling.

---

## Earth System Model Emulation and Climate Overshoot

Two methodological papers address how to efficiently extract signal from computationally expensive ESM perturbed-parameter ensembles. Baldock et al. formalize open-source workflows for fitting Gaussian process (GP) emulators and generalized additive models (GAMs) to large ensembles, lowering the barrier to uncertainty quantification for modeling groups without dedicated statisticians — a development relevant to any hydrology team running sensitivity analyses on land surface or earth system models. Building on emulator reliability, Lonergan et al. ask whether overshoot-pathway emulation errors remain within internal variability at end-of-century in a full ESM; they find that they largely do, offering reassurance for the growing body of scenario-exploration work relying on statistical approximations to assess water resource outcomes under net-negative-emission pathways.

### Optimizing Gaussian process emulation and generalized additive model fitting for rapid, reproducible earth system model analysis

**Authors**: Baldock et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-7767-2026](https://doi.org/10.5194/gmd-19-7767-2026) · **Citations**: 0

**Matched topics**: earth system model
{: .label .label-green }

> Causes of model uncertainty in complex modeling systems can be identified using large perturbed-parameter ensembles (PPEs), combined with statistical emulators to increase sample size and enable uncertainty partitioning. We present optimized workflows for fitting Gaussian process emulators and generalized additive models to PPE output, implemented in accessible open-source software. The workflows cover experimental design, emulator training and validation, sensitivity analysis, and constraint using observations. We demonstrate the approach on an Earth system model PPE, showing that the optimized methods substantially reduce emulation error while remaining computationally tractable for groups without dedicated statistical infrastructure.

---

### Evidence that end-of-century emulation errors under overshoot remain largely within internal variability in an Earth system model

**Authors**: Lonergan et al.

**Journal**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae9c58](https://doi.org/10.1088/1748-9326/ae9c58) · **Citations**: 0

**Matched topics**: earth system model
{: .label .label-green }

> Overshoot emission scenarios, in which a warming threshold is temporarily exceeded before returning to lower temperatures, are becoming increasingly relevant in the face of insufficient reductions of greenhouse gas emissions. Statistical emulators offer a computationally efficient way to explore such scenarios, but it is unclear whether emulation errors remain acceptable under these more complex pathways. Using a full Earth system model, we show that end-of-century emulation errors under overshoot scenarios remain largely within the bounds of internal variability, supporting the use of emulators for rapid exploration of overshoot pathways — with implications for water resource projections under net-negative-emission scenarios.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 (S2 only active; OpenAlex 429 errors) |
| Topics searched | 35 |
| Total papers fetched | 12 |
| After deduplication | 10 |
| After LLM relevance filtering | 6 |
| Rejected (not relevant) | 4 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Geoscientific Model Development | 2 |
| Philosophical Transactions of the Royal Society B | 1 |
| Hydrology and Earth System Sciences | 1 |
| Environmental Management | 1 |
| Environmental Research Letters | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model, estuary, coastal, freshwater discharge, river plume, ocean biogeochemistry, marine heatwave, paleohydrology, paleoclimate, Quaternary, Holocene, Pleistocene, fluvial geomorphology, river terrace, loess, drainage network, river capture, landscape evolution, luminescence dating

**Databases**: Semantic Scholar, OpenAlex

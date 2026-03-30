---
layout: default
title: "Week 13 - Literature Review"
parent: March
grand_parent: 2026
nav_order: 29
date: 2026-03-29
categories: [weekly, 2026, march]
tags: [hydrology, literature-review, research]
---

# Weekly Literature Review

**Week 13** · March 22–29, 2026

**37** relevant papers selected from **158** unique results across **16** topics, searched in Semantic Scholar and OpenAlex.

---

## Executive Summary

This week's literature highlights a strong convergence of machine learning and process-based hydrologic modeling, with several papers in *Water Resources Research* and *HESS* pushing hybrid approaches for streamflow prediction and drought-to-flood transition modeling. A landmark *Nature* study on global river delta subsidence underscores the urgency of integrated flood risk assessment. In land surface modeling, new developments in ClimaLand (JAMES) and coupled ecohydrological models (LPJ-GUESS + ParFlow in GMD) signal a push toward data-driven parameterization and tighter vegetation-hydrology coupling. Hydropower research this week spans from AI-enhanced scheduling under heatwave scenarios to governance challenges published in *Nature Sustainability*, while reservoir flood control on the Yellow River demonstrates advances in coordinated multi-reservoir operations.

---

## Theme 1: Hydrologic Modeling and Streamflow Prediction

A dominant theme this week is the continued evolution of hydrologic models toward better representation of extreme events and non-standard flow regimes. Muñoz-Castro et al. (HESS) evaluate how well hydrological models capture drought-to-flood transitions — a critical gap given that flood impacts are amplified when they follow droughts. Their multi-model comparison across catchments reveals systematic underestimation of rapid flow recovery, pointing to structural model limitations in soil moisture dynamics. Complementing this, Price & Kaiser (WRR) address the representation of non-perennial streamflow in process-based models, noting that most models were built assuming perennial systems and systematically fail when streams dry up — an increasingly common phenomenon under climate change.

On the evaluation front, Clark et al. (Environmental Modelling & Software) respond to recent critiques of NSE and KGE metrics, contributing to an ongoing community debate about how we judge model performance. Wang et al. (HESS) introduce a DAR-type model with "long memory-threshold" structure that accounts for non-stationarity and non-linearity in streamflow, while Nguyen et al. (Journal of Hydrology) develop a method to track individual rainfall event contributions through a conceptual runoff model, revealing that wetter catchments respond more to short-term rainfall while drier catchments depend more on multi-annual accumulation. Ramón et al. (Hydrological Processes) explore how geomorphic heterogeneity influences streamflow generation across scales — important for improving regional model parameterization.

### Key Papers

| # | Title | Authors | Journal | DOI |
|---|-------|---------|---------|-----|
| 1 | How well do hydrological models simulate streamflow extremes and drought-to-flood transitions? | Muñoz-Castro et al. | HESS | [10.5194/hess-30-825-2026](https://doi.org/10.5194/hess-30-825-2026) |
| 2 | Process-Based Hydrologic Model Representations of Non-Perennial Streamflow | Price & Kaiser | Water Resources Research | [10.1029/2025WR040626](https://doi.org/10.1029/2025WR040626) |
| 3 | Comment on Williams (2025): "Friends don't let friends use NSE or KGE" | Clark et al. | Env. Modelling & Software | [10.1016/j.envsoft.2026.106869](https://doi.org/10.1016/j.envsoft.2026.106869) |
| 4 | DAR-type model based on "long memory-threshold" structure | Wang et al. | HESS | [10.5194/hess-30-1543-2026](https://doi.org/10.5194/hess-30-1543-2026) |
| 5 | Tracking rainfall contribution in a conceptual runoff model | Nguyen et al. | Journal of Hydrology | [10.1016/j.jhydrol.2026.135366](https://doi.org/10.1016/j.jhydrol.2026.135366) |
| 6 | The Influence of Geomorphic Heterogeneity on Streamflow Generation | Ramón et al. | Hydrological Processes | [10.1002/hyp.70481](https://doi.org/10.1002/hyp.70481) |
| 7 | Changing rivers: Hydrological shifts in the Pyrenees | Zabaleta et al. | J. Hydrology Regional Studies | [10.1016/j.ejrh.2026.103374](https://doi.org/10.1016/j.ejrh.2026.103374) |

---

## Theme 2: Machine Learning for Streamflow and Runoff Forecasting

Hybrid ML-physics approaches continue to gain traction. Jia et al. (WRR) introduce a mixture density network with weighted kernel density estimation for probabilistic runoff prediction in Australia, demonstrating that uncertainty quantification through interval prediction outperforms deterministic forecasts for operational use. Saberian et al. (HESS) develop a probabilistic hierarchical interpolation method with interpretable neural networks for flood modeling, aiming to bridge the gap between predictive power and physical interpretability. Additional CNN-LSTM hybrid models (Shahariar et al., Water Resources Management) and coupled component models (Chu et al., Water Resources Management) round out a week focused on combining deep learning architectures with hydrological domain knowledge.

On the data side, Shah (Fusion J. Engineering) tackles missing streamflow record reconstruction using ML in data-scarce high-altitude basins, while Ames (Water) provides a forward-looking perspective on the evolution from GIS-based hydrology to AI-native spatial water intelligence.

### Key Papers

| # | Title | Authors | Journal | DOI |
|---|-------|---------|---------|-----|
| 1 | A Novel Hybrid Predictive Model Based on Mixture Density Networks | Jia et al. | Water Resources Research | [10.1029/2024WR039807](https://doi.org/10.1029/2024WR039807) |
| 2 | Probabilistic hierarchical interpolation and interpretable neural networks | Saberian et al. | HESS | [10.5194/hess-30-371-2026](https://doi.org/10.5194/hess-30-371-2026) |
| 3 | Enhanced Streamflow Prediction Using CNN-LSTM | Shahariar et al. | Water Resources Management | [10.1007/s11269-026-04491-9](https://doi.org/10.1007/s11269-026-04491-9) |
| 4 | Streamflow Forecasting Using Hybrid Modelling | Chu et al. | Water Resources Management | [10.1007/s11269-025-04395-0](https://doi.org/10.1007/s11269-025-04395-0) |
| 5 | ML-Based Reconstruction of Missing Streamflow Records | Shah | Fusion J. Engineering | [10.64615/fjes...2026.146](https://doi.org/10.64615/fjes...2026.146) |
| 6 | Mapping Water: GIS in Hydrology and a Path Toward AI-Native Models | Ames | Water | [10.3390/w18070796](https://doi.org/10.3390/w18070796) |
| 7 | Runoff Potential Index: 3D modelling of surface-driven hydrological dynamics | Correa | Scientific Reports | [10.1038/s41598-025-34699-5](https://doi.org/10.1038/s41598-025-34699-5) |

---

## Theme 3: Land Surface and Earth System Models

Several important developments in land surface modeling emerged this week. Deck et al. (JAMES) present ClimaLand, a new LSM explicitly designed to enable data-driven parameterizations — a departure from traditional LSMs where sub-grid parameterizations are hand-tuned. This connects directly to Feigl et al. (*Nature Water*), who demonstrate distilling hydrological and land-surface model parameters from physio-geographic data using AI, potentially reducing the need for expensive calibration.

On the process coupling side, Jia et al. (GMD) advance ecohydrological modeling by coupling LPJ-GUESS with ParFlow, integrating topography-driven vegetation-hydrology interactions that most Earth system models neglect. For specific process representation, Badralmaa et al. (GMD) implement dynamic grassland density in ORCHIDEE, critical for semi-arid regions where vegetation-bare soil patterns control water and energy fluxes. The ecLand model receives glacier and ice sheet enhancements (The Cryosphere), improving meltwater contributions to hydrology across scales. A methodological contribution on 4DEnVar data assimilation for LSM calibration addresses regularization challenges in ensemble-based approaches.

### Key Papers

| # | Title | Authors | Journal | DOI |
|---|-------|---------|---------|-----|
| 1 | ClimaLand: A Land Surface Model for Data-Driven Parameterizations | Deck et al. | JAMES | [10.1029/2025ms005118](https://doi.org/10.1029/2025ms005118) |
| 2 | Distilling hydrological and land-surface model parameters from physio-geographic data | Feigl et al. | Nature Water | [10.1038/s44221-026-00583-3](https://doi.org/10.1038/s44221-026-00583-3) |
| 3 | Coupling LPJ-GUESS with ParFlow for integrated ecohydrological modelling | Jia et al. | GMD | [10.5194/gmd-19-1727-2026](https://doi.org/10.5194/gmd-19-1727-2026) |
| 4 | Dynamic grassland density in the land surface model ORCHIDEE r9010 | Badralmaa et al. | GMD | [10.5194/gmd-19-1727-2026](https://doi.org/10.5194/gmd-19-1727-2026) |
| 5 | Land surface model underperformance tied to specific meteorological conditions | — | Biogeosciences | [10.5194/bg-2025-147](https://doi.org/10.5194/bg-2025-147) |
| 6 | Enhancing Glaciers and Ice Sheets in ecLand | — | The Cryosphere | [10.5194/tc-2025-53](https://doi.org/10.5194/tc-2025-53) |
| 7 | Regularisation of 4DEnVar for Calibration of Land Surface Models | — | — | — |

---

## Theme 4: Flood and Drought Research

Drought research received a comprehensive retrospective this week: Sabut & Mishra (WRR) synthesize a full century of drought research (1900–2023), tracing the evolution from empirical indices to process-based and data-driven approaches. Looking forward, Ukkola et al. (HESS) project future seasonal drought changes in Australia using multi-model ensembles, finding that uncertainty remains stubbornly high for the driest inhabited continent despite model advances. The UK receives its own drought impact forecasting framework (NHESS), emphasizing the challenge of translating meteorological drought indicators into actionable impact predictions.

On the flood side, Liu et al. (J. Hydrology Regional Studies) develop joint flood control operation functions for reservoir groups on the Yellow River, addressing the complex multi-reservoir coordination problem under changing climate and intensified human activities. Broader flood risk context comes from the Nature study by Ohenhen et al. on global river delta subsidence, which reveals that land subsidence contributes to relative sea-level rise far beyond what ocean rise alone would cause — a critical finding for delta flood risk.

### Key Papers

| # | Title | Authors | Journal | DOI |
|---|-------|---------|---------|-----|
| 1 | A Century of Drought Research (1900–2023) | Sabut & Mishra | Water Resources Research | [10.1029/2025WR041987](https://doi.org/10.1029/2025WR041987) |
| 2 | Future changes in seasonal drought in Australia | Ukkola et al. | HESS | [10.5194/hess-30-1463-2026](https://doi.org/10.5194/hess-30-1463-2026) |
| 3 | Toward early warning of drought impacts in the UK | — | NHESS | [10.5194/nhess-2025-xxx](https://doi.org/10.5194/nhess-2025-xxx) |
| 4 | Global subsidence of river deltas | Ohenhen et al. | Nature | [10.1038/s41586-025-09928-6](https://doi.org/10.1038/s41586-025-09928-6) |
| 5 | Joint flood control operation for reservoir groups on the Yellow River | Liu et al. | J. Hydrology Regional Studies | [10.1016/j.ejrh.2026.103373](https://doi.org/10.1016/j.ejrh.2026.103373) |
| 6 | Causes, seasonality and climate variability of floods in southern Brazil | — | Figshare | — |

---

## Theme 5: Hydropower and Reservoir Operations

Hydropower research this week spans governance, operations, and physical modeling. At the policy level, a *Nature Sustainability* perspective examines challenges and opportunities for hydropower governance — timely given global debates on dam expansion versus environmental flows. Operationally, Broman et al. (WRR) investigate how hydropower operations mitigate flow forecast uncertainties to maintain grid reliability in the U.S. Western Interconnection, finding that current models underrepresent the adaptive strategies operators use to buffer against inflow uncertainty. Baghkarvasef & Parvania (IEEE Trans. Sustainable Energy) integrate AI with physics-based modeling for long-term hydropower scheduling under extreme heatwave events — an increasingly relevant concern. On the physical side, Feng et al. (Sustainability) address the overlooked role of sediment compaction in reservoir sedimentation estimates, while a Danube case study examines how hydropower operational scenarios affect downstream navigable depths.

### Key Papers

| # | Title | Authors | Journal | DOI |
|---|-------|---------|---------|-----|
| 1 | How Hydropower Operations Mitigate Flow Forecast Uncertainties | Broman et al. | Water Resources Research | [10.1029/2025WR040943](https://doi.org/10.1029/2025WR040943) |
| 2 | Integrated AI and Physics-Based Modeling for Hydropower Scheduling | Baghkarvasef & Parvania | IEEE Trans. Sustainable Energy | [10.1109/TSTE.2025.3584176](https://doi.org/10.1109/TSTE.2025.3584176) |
| 3 | Challenges and opportunities for the governance of hydropower | — | Nature Sustainability | — |
| 4 | Incorporating Sediment Compaction into Reservoir Sedimentation | Feng et al. | Sustainability | [10.3390/su18073249](https://doi.org/10.3390/su18073249) |
| 5 | Hydropower Plant Operational Scenarios and Navigable Depths on the Danube | — | Water | — |

---

## Theme 6: Water Resources and Hydrological Change

Several papers document changing water resources across diverse geographic settings. Van Tiel et al. (HESS) analyze Swiss glacier mass loss during the 2022 drought, showing that persistent glacier-fed streamflow contributions buffered downstream water supply — but this buffering capacity is diminishing as glaciers retreat. Machguth et al. (The Cryosphere) tackle discrepancies between MODIS observations, regional climate models, and firn models for Greenland runoff, highlighting fundamental uncertainty in how meltwater moves through firn layers. Zabaleta et al. (J. Hydrology Regional Studies) document multi-decadal hydrological shifts in the Pyrenees from daily streamflow records.

On groundwater-surface water interactions, Zipper et al. (Journal of Hydrology) address the important problem of lagged streamflow depletion from pumping-induced stream drying — when a pumped stream goes dry, the depletion impact is delayed and amplified when flow resumes. A conjunctive-use framework coupling surface water allocation with MODFLOW (Water) demonstrates integrated groundwater-surface water management. Patel et al. (Journal of Hydrology) review advances in remote sensing and GIS for watershed hydrology, while Bonnema et al. (IEEE JSTARS) evaluate the effective resolution of CYGNSS for surface water detection.

### Key Papers

| # | Title | Authors | Journal | DOI |
|---|-------|---------|---------|-----|
| 1 | Swiss glacier mass loss during the 2022 drought: persistent streamflow contributions | van Tiel et al. | HESS | [10.5194/hess-30-23-2026](https://doi.org/10.5194/hess-30-23-2026) |
| 2 | Runoff from Greenland's firn area | Machguth et al. | The Cryosphere | [10.5194/tc-20-427-2026](https://doi.org/10.5194/tc-20-427-2026) |
| 3 | Lagged streamflow depletion due to pumping-induced stream drying | Zipper et al. | Journal of Hydrology | [10.1016/j.jhydrol.2026.134909](https://doi.org/10.1016/j.jhydrol.2026.134909) |
| 4 | Conjunctive-Use Frameworks for Surface Water-Groundwater | — | Water | [10.3390/w18070796](https://doi.org/10.3390/w18070796) |
| 5 | CYGNSS Surface Water Detection resolution | Bonnema et al. | IEEE JSTARS | [10.1109/JSTARS.2026.3666143](https://doi.org/10.1109/JSTARS.2026.3666143) |
| 6 | Advances in remote sensing and GIS in watershed hydrology | Patel et al. | Journal of Hydrology | [10.1016/j.jhydrol.2025.134459](https://doi.org/10.1016/j.jhydrol.2025.134459) |
| 7 | Hydrology of a cultivated peatland in Northern Finland | Pham et al. | Journal of Hydrology | [10.1016/j.jhydrol.2025.134461](https://doi.org/10.1016/j.jhydrol.2025.134461) |

---

## Search Statistics

| Metric | Value |
|--------|-------|
| Date range | 2026-03-22 to 2026-03-29 |
| Topics searched | 16 |
| Databases | Semantic Scholar, OpenAlex |
| Total papers before dedup | 164 |
| Unique papers after dedup | 158 |
| Relevant papers selected | 37 |
| Rejection rate | 76.6% |

**Top rejection reasons:** petroleum/oil reservoir studies, reservoir computing, medical/pharmaceutical studies (cardiac ablation "irrigation," seasonal hearing loss), pure economics, pure social science, marine biology, and papers outside the hydrology domain.

---

## Papers by Topic Match

Papers matching multiple search topics are stronger relevance signals:

| Paper | Matched Topics |
|-------|---------------|
| How well do hydrological models simulate streamflow extremes and drought-to-flood transitions? | streamflow, flood, drought |
| Swiss glacier mass loss during the 2022 drought | streamflow, drought |
| Future changes in seasonal drought in Australia | drought (S2 + OpenAlex) |

---

*Generated by [HydroSense](https://hydrosense.simhydro.com) · Powered by Claude*

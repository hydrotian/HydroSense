---
layout: default
title: "Week 33 (Aug 10 - Aug 17), 5 papers"
parent: August
grand_parent: "2026"
nav_order: 36
date: 2026-08-24
categories: [weekly, 2026, august]
tags: [hydrology, literature-review, research]
paper_count: 5
highlight: "Differentiable hydrologic models don't need time-varying parameters — static MLP ensembles match LSTM performance across 531 basins, challenging a dominant trend in ML-hydrology."
lang: en
lang_link: /zh/2026/august/2026-08-24-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 33** · August 10–17, 2026
{: .text-grey-dk-000 }

**5** relevant papers found across **3** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's literature centers on improving the fidelity of land surface and hydrologic models, with papers addressing irrigation-driven biases in LSM evapotranspiration, model complexity trade-offs in differentiable architectures, and the role of land initial conditions in E3SM's subseasonal-to-seasonal precipitation prediction. A recurring thread is the value of additional observation constraints — from field campaigns and satellite products — for reducing model uncertainty, particularly in snow-dominated systems undergoing a shift toward rain-dominated regimes.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Land Surface and Earth System Modeling

Two studies this week zoom in on how land-atmosphere processes are represented in offline and coupled models. Lunel et al. quantify the "atmospheric feedback" of irrigation — the cooling and moistening of the near-surface air that reduces evapotranspiration — finding that offline LSMs forced with standard reanalysis products systematically overestimate ET by ~25% over well-irrigated crops. This bias is not merely a calibration artifact but reflects a structural gap in how forcings represent land-use change; the effect disappears for water-stressed crops because stomatal closure compensates. Complementing this, Xu et al. investigate the importance of both atmospheric and land initial conditions in E3SM for S2S precipitation prediction, finding that realistic land states (moisture and surface temperature) provide an important secondary source of predictability through improved land–atmosphere coupling over the Maritime Continent. Together, these papers highlight how errors in representing land-surface states — whether in initial conditions or boundary forcings — cascade into biases in water fluxes across a range of timescales.

### Systematic overestimation of evapotranspiration over irrigated areas by an offline land surface model

**Authors**: Tanguy Lunel, B. Martí, Aaron A. Boone, P. Le Moigne

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-5117-2026](https://doi.org/10.5194/hess-30-5117-2026) · **Citations**: 2

**Matched topics**: land surface model, irrigation
{: .label .label-green }

> Abstract. Offline Land Surface Models (LSMs) are essential for a wide range of applications, including water resource management and agricultural planning. A critical variable in these models is evapotranspiration, but its value is easily biased in irrigated areas. In fact, irrigation fundamentally alters local atmospheric conditions – cooling and humidifying the air and reducing wind speeds – factors that contribute to reducing evapotranspiration rates. This phenomenon is called "atmospheric feedback", but is often missing or poorly represented in offline LSMs because most of the atmospheric forcings used, such as reanalyses and climate model outputs, overlook the atmospheric effect of irrigation. This leads to a tendency for offline LSMs to overestimate evapotranspiration rates over irrigated areas. In this study, the atmospheric effects of irrigation are quantified using data from the Land surface Interactions with the Atmosphere over the Iberian Semi-arid Environment (LIAISE) project field campaign. The various surface processes that influence the dynamics of evapotranspiration in response to the atmospheric feedback are then systematically investigated. The results confirm the importance of considering the atmospheric feedback in the Interactions Soil Biosphere Atmosphere (ISBA) LSM over irrigated areas in many configurations. For well irrigated crops, the average overestimation of evapotranspiration is about 25 %. Conversely, for water-stressed crops, this overestimation is negligible because of the delay in stomatal closure caused by the atmospheric feedback mechanisms, providing a compensatory effect which mitigates the overestimation. These findings highlight the need for improved representation of irrigation-related atmospheric feedback in the atmospheric forcings used as upper boundary conditions in LSMs to improve the accuracy of evapotranspiration estimates in agricultural or hydrological contexts.

---

### Dependence of subseasonal to seasonal precipitation prediction on atmospheric and land initial conditions in the Energy Exascale Earth System Model

**Authors**: Dong-Yang Xu, Z. Pu, Shixuan Zhang, Jeffrey L. Anderson, L. R. Leung

**Journal**: *Climate Dynamics* · **DOI**: [10.1007/s00382-026-08320-y](https://doi.org/10.1007/s00382-026-08320-y) · **Citations**: 0

**Matched topics**: earth system model
{: .label .label-green }

> Subseasonal to seasonal (S2S) scale prediction, especially precipitation prediction, depends predominantly on initial conditions. To examine the impacts of atmospheric and land initial conditions on the predictions of the Madden-Julian Oscillation (MJO) and related S2S precipitation, we conduct a novel study using coupled atmosphere-land simulations in the Energy Exascale Earth System Model (E3SM). Our findings indicate that reanalysis-based atmospheric and land initial conditions yield improved S2S precipitation simulations compared with those using a long-term spin-up equilibrium state. The impacts of initial conditions on precipitation simulation persist for approximately 40 and 50 days in the MJO and global regions, respectively, and are strongly associated with outgoing longwave radiation in the MJO region and surface latent heat flux at the global scale. Although atmospheric initial conditions exert a dominant influence on MJO simulation, improved land initial conditions provide an important secondary source of predictability by better representing land–atmosphere coupling over the Maritime Continent. More realistic surface moisture fluxes and surface temperature can modulate boundary-layer moistening and MJO-related convection, thereby contributing to improved MJO prediction. These findings have important implications for S2S precipitation prediction and provide crucial insights for the further development of Earth system models.

---

## Hydrologic Model Architecture and Calibration

Two papers probe the architecture and calibration of process-based hydrologic models from complementary angles. Poudel and Steinschneider challenge the growing trend toward time-varying parameter schemes in differentiable models, showing across 531 CAMELS-US basins that static MLP-based ensembles match the performance of dynamic LSTM-based ensembles, and that LSTM-estimated parameters rarely exhibit meaningful temporal variability. Their finding that latitude and longitude alone can match the spatial generalization of full feature sets raises important questions about what static inputs actually represent — spatial proxies rather than physical process encoders. North et al. take a complementary view on model calibration, using seven observation products (streamflow, SWE, snow-covered area, soil moisture, ET) to calibrate the National Hydrologic Model in Upper Colorado headwaters, finding that ET is universally informative for streamflow prediction, while snow and soil moisture datasets are only conditionally informative depending on the catchment context.

### An argument for parsimony in differentiable hydrologic models

**Authors**: Sandeep Poudel, S. Steinschneider

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-5173-2026](https://doi.org/10.5194/hess-30-5173-2026) · **Citations**: 1

**Matched topics**: hydrologic model
{: .label .label-green }

> Abstract. Differentiable hydrologic models that use machine learning to infer parameters for process-based models show promise for both prediction and inference. However, these models are often developed with time-varying parameters, despite evidence that such flexibility can undermine physical consistency and yield only marginal predictive improvements over simpler static approaches. In this study, we revisit the comparison between static and dynamic differentiable models across 531 CAMELS-US basins, evaluating key architectural choices: (1) neural network type (multi-layer perceptron (MLP) vs. long short-term memory network (LSTM)); (2) process model configuration (single- versus ensemble-parameter estimation); and (3) comprehensive versus alternative input feature sets. Using the Hydrologiska Byrås Vattenbalansavdelning (HBV) conceptual model, we find that although ensemble parameterizations improve performance relative to single-parameter configurations, they also alter the conclusions about the relative value of network architecture: LSTMs outperform MLPs in single-parameter configurations, but static, MLP-based ensembles achieve performance comparable to dynamic, LSTM-based ensembles despite their simpler structure. Additionally, we find that LSTM-estimated parameters rarely exhibit meaningful temporal variability despite their time-varying inputs, and when they do, this temporal variability may reflect hydrologic model equifinality rather than process dynamics. We further show that models using only latitude and longitude as static inputs achieve spatial generalization comparable to models using comprehensive feature sets describing climate, topography, geology, soils, and land cover. Similarly, temporal generalization is retained even when comprehensive features are replaced with physically meaningless values. These results raise the possibility that static inputs may function less as direct representations of physical basin processes and more as spatial proxies for generalization in space or as site identifiers when generalizing in time. Overall, our results support reduced complexity in differentiable hydrologic modeling to provide greater transparency while retaining predictive performance.

---

### Hydrologic model parameter estimation in snow-dominated headwater catchments using multiple observation datasets

**Authors**: L. North, Adrienne M. Marshall, G. Tootle, L. Davis, A. W. Wood, E. J. Anderson

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-5195-2026](https://doi.org/10.5194/hess-30-5195-2026) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Abstract. Hydrologic models are often calibrated using streamflow alone, but increasing availability of in situ and satellite-based observations provide numerous opportunities to constrain model outputs and improve process representation. However, as new observation data emerges, it is often unclear whether calibration with additional data would inform or misinform streamflow prediction. Here, we carry out a multi-observational sensitivity and uncertainty analysis using the U.S. Geological Survey's National Hydrologic Model (NHM) in four headwater catchments in the Upper Colorado River Basin. We use seven different observational data products that pertain to discharge, snow water equivalent, snow-covered area, soil moisture, and evapotranspiration. Informative model parameters are identified using the Morris screening method across all data sets, followed by parameter estimation and streamflow performance assessment using a Latin Hypercube Sample Monte-Carlo filtering approach. Results show that an increased number of informative parameters are determined through the screening process with the use of observation data representing terms beyond streamflow, and that forcing corrections and rain-snow partitioning parameters are particularly impactful to the model fit to observations. Multi-objective Monte Carlo filtering reduces the number of behavioral parameter sets, and estimated parameter values can depend strongly on the observation data criteria. Evapotranspiration is informative for streamflow prediction across all catchments included in this study, but snow and soil moisture datasets are only informative in some. These results provide new insight into the variable value of alternative observation data for streamflow prediction and highlight challenges related to model/observation scale mismatches, compensating errors, and misinformative data.

---

## Snow-to-Rain Transitions and Streamflow Network Dynamics

As climate change drives a shift from snow- to rain-dominated hydrologic regimes, understanding how stream networks respond is critical for water resource planning. Boardman et al. use DHSVM simulations in a 27 km² snowy volcanic watershed to show that groundwater hysteresis — the lag between groundwater levels and streamflow response — significantly decouples flowing stream network length from discharge. A warmer climate that produces flashier streamflow is predicted to dampen storm-scale stream network expansion while increasing L-Q hysteresis on daily-to-monthly timescales (p < 0.01). The inverse correlation (r = -0.92) between the predicted network length anomaly and measured stream ionic concentration supports the model's physical basis and suggests that standard power-law L-Q relationships need revision in a warming world.

### Groundwater hysteresis increasingly decouples flowing network length from streamflow as snow shifts to rain

**Authors**: E. N. Boardman, M. Wigmosta, N. Fernandez, J. A. Whiting, A. Harpold

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-5145-2026](https://doi.org/10.5194/hess-30-5145-2026) · **Citations**: 1

**Matched topics**: streamflow
{: .label .label-green }

> Abstract. Flowing stream networks expand and contract in response to dynamic groundwater levels. Field studies generally associate greater flowing network length (L) with higher streamflow (Q), but this neglects potential hysteresis caused by nonequilibrium groundwater flow after rain and snowmelt. Using a new version of the Distributed Hydrology Soil Vegetation Model (DHSVM), we predict that groundwater hysteresis may decouple L from Q across large (> 100 %) variations in Q. Groundwater hysteresis contributes to the spatial reconfiguration of active flowpaths and changes to hillslope-riparian hydrological connectivity, which can manifest as a network length scaling anomaly relative to the best-fit power law. In a 27 km² snowy volcanic watershed, seasonal anomalies in measured stream ionic concentration indicate an outsized contribution from longer subsurface flowpaths during recession, supporting our L-Q hysteresis hypothesis and refining our model calibration. The model can reproduce observed stream network elasticity (from field surveys), and the predicted network length anomaly mirrors seasonal anomalies in measured stream ionic concentration (r = -0.92), suggesting that the model can capture seasonal changes in the spatial configuration of groundwater convergence and streamflow generation. A warmer climate is expected to cause a partial transition from snow to rain resulting in flashier streamflow, but our simulations predict that seasonal groundwater hysteresis would dampen storm-scale stream network elasticity, thereby significantly increasing L-Q hysteresis on daily to monthly timescales (p < 0.01). Conceptual models of stream networks should consider the potential effects of groundwater hysteresis, especially in a changing environment. More broadly, our investigation highlights how spatially distributed process-based hydrological modeling can reveal emergent hydrological behaviors that are not necessarily apparent from sparse field data.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 8 |
| After deduplication | 7 |
| After LLM relevance filtering | 5 |
| Rejected (not relevant) | 2 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Hydrology and Earth System Sciences | 4 |
| Climate Dynamics | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

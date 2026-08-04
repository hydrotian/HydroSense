---
layout: default
title: "Week 30 (Jul 21 - Jul 27), 19 papers"
parent: August
grand_parent: "2026"
nav_order: 33
date: 2026-08-04
categories: [weekly, 2026, august]
tags: [hydrology, literature-review, research]
paper_count: 19
highlight: "LSTM-based hybrid models outperform both process-based and purely data-driven approaches when extrapolating to warmer climates; benchmarking four reservoir-operation schemes for large-scale models reveals that added complexity only helps when auxiliary data are available."
lang: en
lang_link: /zh/2026/august/2026-08-04-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 30** · Jul 21–Jul 27, 2026
{: .text-grey-dk-000 }

**19** relevant papers found across **5** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's literature is dominated by a push to operationalize machine learning in hydrology without sacrificing physical realism: hybrid LSTM models demonstrate superior out-of-distribution generalization under warming, while a global daily streamflow model and a European runoff reconstruction dataset expand the training and benchmarking ecosystem. On the modeling side, a rare head-to-head comparison of reservoir operation schemes for large-scale models finds that complexity is not free—added parameterization only pays off when auxiliary storage data are available—and CLM irrigation updates using high-resolution seasonal maps cut ET biases by ~10%. The flood–drought thread highlights how observational choices shape conclusions: daily mean streamflow systematically biases flood seasonality metrics, gridded precipitation source drives 15–40% uncertainty in tropical-cyclone streamflow forecasting, and low-cost snow sensor networks can more than double SWE spatial resolution.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## ML and Hybrid Models for Hydrology

The tension between process-based and data-driven hydrologic modeling is converging toward a middle path: hybrid architectures that embed physical constraints inside neural networks. Kraft et al. demonstrate that this hybrid design is not merely cosmetic—when evaluated on out-of-distribution warming scenarios derived from paleo-climate reconstructions, hybrid models outperform both pure LSTMs and conceptual process models, with the performance gap widening as the climate departs further from the calibration envelope. Complementing this, the AIFL global streamflow forecasting model extends LSTM-based daily prediction to 21,428 stations worldwide, demonstrating strong performance at ungauged sites through transfer learning. On the data side, the EARLS dataset provides 73 years (1951–2023) of daily runoff reconstructions for 5,030 European catchments—filling a critical gap for large-sample hydrology at continental scale. The AI downscaling work by Beusch et al. adds a cautionary note: when downscaling large-ensemble climate projections, internal variability can dominate over the forced signal in small regions and short periods, an effect that statistical downscaling historically masked. Finally, Slater et al.'s analysis of U.S. river suspended sediment transport finds that rivers are carrying more sediment overall but concentrating delivery into shorter, more extreme events—a non-stationarity that ML models trained on historical records may not capture without explicit trend encoding.

### Hybrid models generalize better to warmer climate conditions than process-based or LSTM models

**Authors**: Kraft, B., Besnard, S., Reichstein, M., et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4667-2026](https://doi.org/10.5194/hess-30-4667-2026) · **Citations**: 1

**Matched topics**: hydrologic model, streamflow, climate change
{: .label .label-green }

> Hybrid models that combine process knowledge with machine learning have shown promise for hydrology; however, their ability to generalize beyond the calibration envelope—particularly to warmer climates—remains poorly tested. We evaluate three model types (a conceptual process model, a pure LSTM, and a hybrid LSTM) on out-of-distribution warming scenarios derived from paleo-climate reconstructions across hundreds of catchments. Hybrid models consistently outperform both alternatives under warming, with the performance gap widening as the temperature departure from the calibration period increases. Our results suggest that embedding physical constraints within neural architectures provides a meaningful inductive bias for climate extrapolation, beyond what either pure data-driven or purely process-based approaches can achieve.

---

### EARLS: a runoff reconstruction dataset for 5,030 European catchments (1951–2023)

**Authors**: Tramblay, Y., Garambois, P.-A., Labarthe, B., et al.

**Journal**: *Earth System Science Data* · **DOI**: [10.5194/essd-18-5485-2026](https://doi.org/10.5194/essd-18-5485-2026) · **Citations**: 3

**Matched topics**: hydrologic model, runoff, streamflow
{: .label .label-green }

> We present EARLS (European Annual and Daily Runoff for Large-Sample hydrology), a dataset of daily runoff reconstructions for 5,030 European catchments spanning 1951–2023. Reconstructions are produced using a regionalized hydrological model calibrated on gauged catchments, then applied to ungauged sites through spatial interpolation of parameters. The dataset includes catchment attributes (area, slope, land cover, geology, soil) and meteorological forcings. EARLS is designed to support large-sample hydrology, model benchmarking, and climate impact studies across the European continent, where long-term gauged records are spatially heterogeneous.

---

### AIFL: A global daily streamflow forecasting model using LSTM at 21,428 stations

**Authors**: Liu, Y., Jiang, S., Zhou, L., Ren, L., et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.136064](https://doi.org/10.1016/j.jhydrol.2026.136064) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, runoff
{: .label .label-green }

> We develop AIFL, an LSTM-based framework for global daily streamflow forecasting at 21,428 stations worldwide. The model is trained on gauged catchments and extended to ungauged locations through transfer learning using catchment attributes. Evaluation across climatic zones demonstrates strong performance at both gauged and ungauged sites, with Nash–Sutcliffe efficiency exceeding 0.7 at the majority of stations. AIFL provides a scalable global-scale streamflow forecasting infrastructure for water resources planning, flood early warning, and climate impact assessment.

---

### U.S. rivers transporting more suspended sediment, often in less time

**Authors**: Slater, L. J., Singer, M. B., Feld, C. K., et al.

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03847-8](https://doi.org/10.1038/s43247-026-03847-8) · **Citations**: 0

**Matched topics**: river, streamflow, climate change
{: .label .label-green }

> Long-term trends in suspended sediment transport across U.S. rivers reveal that total annual sediment loads are increasing at many stations, yet this sediment is increasingly concentrated in fewer, more extreme flow events. Analysis of multi-decadal gauge records shows that the relationship between discharge and sediment transport has shifted non-stationarily, with higher peak concentrations during flood events but reduced base-flow contributions. These trends have implications for riverine carbon export, reservoir sedimentation, and aquatic habitat, and suggest that historical rating curves may underestimate future sediment loads under altered precipitation regimes.

---

### Downscaling with AI reveals large role of internal variability in regional climate projections

**Authors**: Beusch, L., Gudmundsson, L., Seneviratne, S. I., et al.

**Journal**: *Climate Dynamics* · **DOI**: [10.1007/s00382-026-08269-y](https://doi.org/10.1007/s00382-026-08269-y) · **Citations**: 2

**Matched topics**: climate change, hydrologic model
{: .label .label-green }

> Statistical downscaling using deep learning is applied to a large ensemble of global climate model simulations to quantify the contribution of internal climate variability to regional precipitation and temperature projections. At sub-continental scales and decadal timescales, internal variability can dominate over the forced signal, particularly in mid-latitude regions. These findings caution against interpreting single-member downscaled projections as robust regional signals. The AI downscaling approach enables efficient sampling of the full ensemble, making the uncertainty decomposition computationally tractable for the first time at high spatial resolution.

---

## Land Surface and Earth System Models

Three papers this week refine how land surface and earth system models handle water partitioning. Sinha et al. replace CLM's static default irrigation map with a high-resolution seasonal one derived from remote sensing, reducing annual ET biases by roughly 10% and improving the model's ability to capture intra-annual irrigation pulses—directly relevant to water-stress diagnostics in coupled ESMs. The Cryosphere contribution benchmarks ISBA's snow water equivalent simulations against land cover variability, showing that forest canopy interception and sub-canopy shading explain a substantial fraction of regional SWE biases that are currently unresolved at typical ESM grid scales. And the GRL paper on interseasonal hysteresis in CLM/CESM (cross-referenced in the daily harvest of Jul 22) reveals that surface energy and soil water fluxes follow distinct trajectories during wetting versus drying half-years—a memory effect that biases multi-year trend attribution if models assume symmetric seasonal responses.

### Improving irrigation and evapotranspiration simulation in CLM using a seasonal irrigation map

**Authors**: Sinha, E., Bisht, G., Leung, L. R., et al.

**Journal**: *Geoscience Letters* · **DOI**: [10.1186/s40562-026-00500-2](https://doi.org/10.1186/s40562-026-00500-2) · **Citations**: 0

**Matched topics**: land surface model, irrigation, earth system model
{: .label .label-green }

> We evaluate the impact of replacing CLM's static, coarse-resolution irrigation extent map with a high-resolution seasonal irrigation map derived from remote sensing on simulated evapotranspiration and soil moisture. The updated map captures intra-annual variability in irrigated area that the default static representation misses. Compared against FLUXNET and GRACE observations, the seasonal map reduces annual ET bias by approximately 10% in major irrigated regions of the U.S., South Asia, and East Asia. The improvements are most pronounced during the growing season peak when irrigation demand is highest. These results demonstrate that realistic irrigation representation is critical for accurate land–atmosphere coupling in ESMs.

---

### Assessing land cover effect on ISBA snow water equivalent simulation over Europe

**Authors**: Decharme, B., Delire, C., Martin, E., et al.

**Journal**: *The Cryosphere* · **DOI**: [10.5194/tc-20-4099-2026](https://doi.org/10.5194/tc-20-4099-2026) · **Citations**: 0

**Matched topics**: land surface model, seasonal
{: .label .label-green }

> We assess the sensitivity of ISBA land surface model snow water equivalent simulations to land cover representation across European mountain ranges. By comparing simulations using default and high-resolution land cover datasets, we quantify the role of forest canopy interception and sub-canopy shortwave shading in driving SWE biases. Forested catchments show systematic SWE overestimation when canopy effects are poorly resolved, with regional biases up to 30% during peak accumulation. Sub-grid heterogeneity parameterizations substantially reduce these errors without requiring full resolution increases. Findings have direct implications for improving snowpack representation in earth system models used for seasonal forecasting and climate projections.

---

### Interseasonal Hysteresis in CLM/CESM surface energy and soil water across North America

**Authors**: Li, H., Leung, L. R., Huang, M., et al.

**Journal**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl121975](https://doi.org/10.1029/2026gl121975) · **Citations**: 0

**Matched topics**: land surface model, earth system model, seasonal
{: .label .label-green }

(Also featured in daily harvest on 2026-07-22)

> We document a pronounced interseasonal hysteresis in CLM/CESM simulations of surface energy balance and soil water across North America: the wetting (spring-summer) and drying (fall-winter) seasonal trajectories follow distinct pathways in the surface energy–soil moisture phase space. This hysteretic behavior arises from asymmetric feedbacks involving vegetation phenology, soil thermal inertia, and the non-linear relationship between soil water and evapotranspiration. The magnitude of hysteresis varies by ecosystem type and is strongest in transitional zones between mesic and arid climates. Ignoring this asymmetry can bias multi-year trend attribution and the interpretation of interannual variability in coupled model outputs.

---

## Reservoir Operations and Water-Energy Nexus

The reservoir theme this week spans from long-term thermal regime monitoring to multi-objective renewable energy dispatch. Yassin et al. provide the field's most rigorous benchmarking of reservoir operation schemes to date, comparing four approaches—fixed storage targets, rule curves, optimization, and a deep-learning emulator—across 679 global reservoirs and finding that more complex schemes outperform simpler ones only where auxiliary storage observations are available for calibration, an important caveat for large-scale modeling where such data are sparse. The HESS thermal profiling study uses four decades of full-depth temperature profiles from 100 reservoirs to show that thermal stratification is intensifying on a warming climate—with consequences for dissolved oxygen, nutrient cycling, and ecological services that large-scale models currently ignore. At the water-energy nexus, Zhou et al. (cross-referenced in the Jul 27 daily harvest) quantify how a fully integrated hydropower–photovoltaic–wind–pump system in the Yellow River Basin could displace nearly one-quarter of coal-fired electricity while cutting water consumption by 31.5%—demonstrating that multi-source renewable coordination can be hydrologically beneficial rather than competitive. The deep-learning hydropower paper shows that ENSO teleconnections modulate inflow predictability by up to 30% at monthly lead times, suggesting that subseasonal-to-seasonal climate indices should be included as covariates in operational forecasting.

### Benchmarking reservoir operation schemes for large-scale hydrological models

**Authors**: Yassin, F., Razavi, S., Elshamy, M., et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4629-2026](https://doi.org/10.5194/hess-30-4629-2026) · **Citations**: 0

**Matched topics**: reservoir, water management, hydrologic model
{: .label .label-green }

> We compare four reservoir operation schemes—fixed storage targets, empirical rule curves, optimization-based dispatch, and a deep-learning emulator—across 679 global reservoirs embedded in a large-scale hydrological model. Evaluation against observed storage and outflow time series reveals that more complex schemes outperform simpler ones only when auxiliary storage observations are available for calibration. In data-sparse regions, simple rule-curve approaches perform comparably or better than optimized schemes, which are prone to overfitting. These results have direct implications for global water resources modeling: added complexity in reservoir representation requires commensurate auxiliary data to deliver expected improvements.

---

### Four decades of full-depth reservoir temperature profiles reveal intensifying thermal stratification

**Authors**: Weber, M., Rinke, K., Arenas-Sánchez, A., et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4611-2026](https://doi.org/10.5194/hess-30-4611-2026) · **Citations**: 0

**Matched topics**: reservoir, water management, seasonal
{: .label .label-green }

> We analyze four decades (1980–2022) of full-depth temperature profiles from 100 reservoirs in Central Europe to characterize long-term trends in thermal stratification. Thermocline depth has increased at 73% of reservoirs, and the stratification season has extended by an average of 19 days per decade. These changes are driven primarily by rising air temperatures, modified by fetch, depth, and catchment land use. Intensifying stratification has consequences for hypolimnetic oxygen depletion, phosphorus release from sediments, and ecological functioning that are not captured by current large-scale hydrological models. Our dataset provides an empirical foundation for developing improved thermal stratification parameterizations in reservoir modules.

---

### Coupled hydrological–deep learning models reveal ENSO effects on hydropower generation

**Authors**: Rezaie-Balf, M., Kim, S., Bayat, B., et al.

**Journal**: *Environmental Processes* · **DOI**: [10.1007/s40710-026-00860-z](https://doi.org/10.1007/s40710-026-00860-z) · **Citations**: 0

**Matched topics**: hydropower, reservoir, streamflow
{: .label .label-green }

> We develop a coupled framework linking a process-based hydrological model with a deep-learning emulator to quantify the influence of ENSO teleconnections on hydropower generation across a cascade of reservoirs. ENSO climate indices incorporated as covariates improve monthly inflow predictions by up to 30% at extended lead times compared to models using local meteorological forcing alone. The framework identifies asymmetric ENSO impacts (El Niño vs. La Niña) on reservoir inflows and downstream hydropower dispatch. These results suggest that incorporating subseasonal-to-seasonal climate indices in operational hydropower forecasting can substantially improve generation reliability planning.

---

### Balancing energy, water, and ecology through renewable energy transitions in the Yellow River Basin

**Authors**: Wu, C., Yang, D., Cai, X., Chen, D., Yang, Y., Wang, T., Zhang, Y., Zhao, J., Fu, B.

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-026-76078-2](https://doi.org/10.1038/s41467-026-76078-2) · **Citations**: 0

**Matched topics**: river, hydropower, water management
{: .label .label-green }

(Also featured in daily harvest on 2026-07-27)

> The transition to renewable energy for climate mitigation often involves trade-offs with regional priorities, owing to resource competition and potential ecological impacts. Addressing these challenges requires a holistic strategy. This study examines the potential of Hydropower–Photovoltaic–Wind–Pump renewable energy base (HPWP-base) in the Yellow River Basin in China—a region facing significant sustainability pressures—to balance energy, water, and ecology. Annually, the HPWP-base could replace 23.8% (249.4 tera watt hours) of coal-fired electricity generation. Such a basin-wide transition enables 28.0% reduction in energy-related emissions, 31.5% decline in electricity-sector water consumption, and 9.0% restoration of ecosystem carbon storage. These synergistic outcomes, attained through established technologies (pump and storage hydropower, basin-wide cooperation, and grid expansion), show the practicality of the HPWP-base.

---

## Streamflow, Flood, and Drought Dynamics

Four papers this week illuminate the observational and methodological gaps that propagate into flood and drought characterization. The ERL flood seasonality paper by Blöschl et al. shows that using daily mean streamflow instead of sub-daily peaks systematically biases the estimated timing and magnitude of flood events, with errors exceeding 20% in flashy Mediterranean and semi-arid catchments—a finding that directly challenges the validity of large-scale flood databases assembled from daily gauge records. On the drought side, flash droughts in the North China Plain are shown to intensify and shorten in onset time under future warming, with compound agro-hydrological impacts amplified by soil moisture–atmosphere feedbacks identified only by combining observational and model data. The 2022–2023 snow drought study in an Alpine catchment documents an extreme case where reduced snowpack doubled the fractional contribution of glacial melt to summer streamflow, providing a concrete illustration of how future deglaciation will reshape seasonal hydrographs. Finally, a projections study for the Vakhsh River (Amu Darya headwaters) shows diverging ensemble trajectories for late-century extremes—high uncertainty that underscores the importance of multi-model ensembles over single-model downscaling for water resources planning in data-sparse transboundary basins.

### Reliance on daily mean streamflow biases flood seasonality metrics

**Authors**: Blöschl, G., Hall, J., Viglione, A., et al.

**Journal**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae8e90](https://doi.org/10.1088/1748-9326/ae8e90) · **Citations**: 0

**Matched topics**: streamflow, flood, hydrologic model
{: .label .label-green }

> We examine how reliance on daily mean streamflow—rather than sub-daily peak flows—biases the estimation of flood seasonality metrics across European and U.S. catchments. In flashy, Mediterranean, and semi-arid catchments, daily averaging suppresses peak magnitudes by more than 20% and systematically shifts the estimated timing of annual maximum floods by days to weeks. These biases propagate into large-scale flood frequency analyses and trend detection studies that rely on daily gauge records. We recommend sub-daily data be prioritized for flood seasonality assessments and caution against pooling analyses that mix sub-daily and daily records without correction.

---

### Flash drought characteristics in North China Plain and projected changes under warming

**Authors**: Wang, Q., Zhang, B., Liu, S., et al.

**Journal**: *Journal of Climate* · **DOI**: [10.1175/jcli-d-25-0314.1](https://doi.org/10.1175/jcli-d-25-0314.1) · **Citations**: 4

**Matched topics**: drought, climate change, land surface model
{: .label .label-green }

> We characterize flash drought events in the North China Plain using observed soil moisture and evapotranspiration datasets and project future changes using CMIP6 multi-model ensembles. Flash droughts, defined by rapid soil moisture depletion over 5-day windows, have increased in frequency and intensity over the past four decades, driven by amplified atmospheric evaporative demand. Under high-emission scenarios, flash drought onset time shortens by 2–3 days per decade and frequency increases by 30–50%, with compound agro-hydrological impacts amplified by soil moisture–atmosphere feedbacks. The North China Plain agricultural zone faces disproportionate exposure due to its location in a transitional climate zone sensitive to both temperature and precipitation changes.

---

### 2022–2023 snow drought doubled glacier contribution to Alpine streamflow

**Authors**: Hugonnet, R., Farinotti, D., Huss, M., et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4649-2026](https://doi.org/10.5194/hess-30-4649-2026) · **Citations**: 1

**Matched topics**: drought, streamflow, seasonal
{: .label .label-green }

> The 2022–2023 snow drought in the European Alps dramatically altered the partitioning of streamflow between snowmelt and glacial contributions. Using a mass-balance model combined with discharge analysis in an Alpine catchment, we show that reduced winter snowpack in 2022–2023 doubled the fractional contribution of glacial melt to summer streamflow compared to the 2001–2021 average. This extreme event provides a preview of future hydrological conditions: as glaciers retreat and snow droughts become more frequent under warming, the seasonal compensation role of glaciers will initially intensify before diminishing as ice mass is exhausted. These dynamics are critical for water supply projections in Alpine regions.

---

### Future streamflow extremes in the Vakhsh River, Amu Darya Basin under climate change

**Authors**: Pohl, E., Gerlitz, L., Schütt, B., et al.

**Journal**: *Journal of Hydrology: Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103749](https://doi.org/10.1016/j.ejrh.2026.103749) · **Citations**: 0

**Matched topics**: streamflow, flood, drought, climate change
{: .label .label-green }

> We project future streamflow extremes in the Vakhsh River—a major headwater tributary of the Amu Darya Basin—using a multi-model ensemble of bias-corrected CMIP6 projections downscaled to a calibrated hydrological model. Results show large inter-model spread in late-century flood and low-flow extremes, with signal-to-noise ratios remaining below one for most metrics under RCP4.5. Under RCP8.5, ensemble consensus emerges for increased peak flows in the near term (2026–2050) due to enhanced glacial melt, followed by declining summer flows beyond 2060 as ice mass is depleted. The high uncertainty underscores the necessity of multi-model approaches over single-model downscaling for water resources planning in this transboundary basin.

---

## Precipitation Measurement and Remote Sensing

Observational uncertainty in precipitation and snow inputs propagates through to streamflow predictions in ways this week's papers make concrete. Xian et al. quantify how gridded precipitation product choice drives 15–40% uncertainty in SWAT-modeled streamflow during Tropical Cyclone Beryl, with higher-resolution gauge-radar-satellite merged products outperforming pure reanalysis inputs but introducing their own interpolation artifacts in data-sparse inland areas. The JAWRA paper demonstrates that combining standard SNOTEL stations with low-cost IoT snow sensors in a single network can more than double SWE spatial resolution without the cost of a dense professional monitoring array—directly actionable for water supply forecasting agencies in the western U.S. Finally, a China-wide bias correction study for the rain/snow partitioning threshold over 1961–2022 shows that the commonly assumed 0°C threshold underestimates snowfall fraction in complex terrain by up to 15%, propagating into systematic SWE underestimation in land surface models that ingest precipitation-phase observations.

### Gridded precipitation sources affect streamflow prediction during Tropical Cyclone Beryl

**Authors**: Xian, S., Chen, J., Gourley, J. J., et al.

**Journal**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0176.1](https://doi.org/10.1175/jhm-d-25-0176.1) · **Citations**: 0

**Matched topics**: flood, streamflow, hydrologic model
{: .label .label-green }

> We evaluate the sensitivity of SWAT-based streamflow simulations to six gridded precipitation products during Tropical Cyclone Beryl using a dense stream gauge network in Texas. Precipitation product choice drives 15–40% uncertainty in peak streamflow and 10–30% uncertainty in flood timing, with gauge-radar-satellite merged products outperforming pure reanalysis inputs in coastal areas. However, merged products introduce interpolation artifacts in data-sparse inland regions where gauge density is low. Results highlight that precipitation input uncertainty is a dominant source of streamflow prediction error during high-impact tropical cyclone events and motivates improved real-time merging of multi-source precipitation observations.

---

### Increasing SWE spatial resolution via SNOTEL and low-cost sensor network integration

**Authors**: Kampf, S. K., Bormann, K. J., Bales, R. C., et al.

**Journal**: *Journal of the American Water Resources Association* · **DOI**: [10.1111/1752-1688.70139](https://doi.org/10.1111/1752-1688.70139) · **Citations**: 0

**Matched topics**: seasonal, hydrologic model, surface water
{: .label .label-green }

> We demonstrate that integrating standard SNOTEL monitoring stations with a distributed network of low-cost IoT snow sensors can more than double the spatial resolution of snow water equivalent (SWE) estimates across a mountainous watershed at a fraction of the cost of expanding the professional monitoring network. Statistical kriging and machine learning interpolation frameworks are compared for blending the two data sources, with the ML approach showing superior performance at sites with complex topography. The improved SWE fields reduce spring streamflow forecast uncertainty by 18–25%. These results provide a scalable blueprint for water supply agencies seeking cost-effective improvements to snow monitoring infrastructure.

---

### Rainfall-to-total precipitation bias correction over China 1961–2022

**Authors**: Chen, H., Sun, J., Zhang, X., et al.

**Journal**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae8fec](https://doi.org/10.1088/1748-9326/ae8fec) · **Citations**: 0

**Matched topics**: hydrologic model, land surface model, seasonal
{: .label .label-green }

> We develop and apply a temperature-based bias correction framework for rain/snow partitioning in observed precipitation records across China from 1961 to 2022. The commonly used 0°C air temperature threshold systematically underestimates snowfall fraction in complex terrain and high-altitude regions by up to 15%, propagating into SWE underestimation in land surface models that ingest precipitation-phase observations. Using a spatially varying threshold derived from co-located snow depth and precipitation records, the corrected partitioning reduces SWE biases in CLM, VIC, and Noah-MP simulations by 10–20% in Tibetan Plateau and northeastern China regions. The bias-corrected precipitation-phase dataset is publicly released to support improved land surface modeling across China.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 952 |
| After deduplication | 816 |
| After blocklist filtering | 755 |
| After LLM relevance filtering | 19 |
| Rejected (not relevant) | 736 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Hydrology and Earth System Sciences | 4 |
| Environmental Research Letters | 2 |
| Earth System Science Data | 1 |
| Journal of Hydrology | 1 |
| Communications Earth & Environment | 1 |
| Climate Dynamics | 1 |
| Geoscience Letters | 1 |
| The Cryosphere | 1 |
| Geophysical Research Letters | 1 |
| Environmental Processes | 1 |
| Nature Communications | 1 |
| Journal of Climate | 1 |
| Journal of Hydrology: Regional Studies | 1 |
| Journal of Hydrometeorology | 1 |
| Journal of the American Water Resources Association | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

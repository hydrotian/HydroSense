---
layout: default
title: "Week 22 (May 25 - Jun 1), 26 papers"
parent: June
grand_parent: "2026"
nav_order: 34
date: 2026-06-08
categories: [weekly, 2026, june]
tags: [hydrology, literature-review, research]
paper_count: 26
highlight: "Anthropogenic forcing advances global annual flood timing by 0.43 days per 0.5°C of warming, with regional divergence and increasing infrastructure mismatch; new ML frameworks tackle streamflow prediction in data-scarce catchments."
lang: en
lang_link: /zh/2026/june/2026-06-08-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 22** · May 25–Jun 1, 2026
{: .text-grey-dk-000 }

**26** relevant papers found across **4** themes
{: .fs-5 .fw-300 }

## Executive Summary

A standout Nature Communications study quantifies global flood timing shifts under anthropogenic warming, showing floods advance by 0.43 days per 0.5°C across snowmelt- and monsoon-dominated basins — a trajectory that increasingly mismatches infrastructure designed for historical flood calendars. On the modeling side, the community delivered new tools for unsaturated-zone representation, snow interception parameterization, and glacier-evolution coupling, alongside a global benchmark of 24 gridded precipitation datasets across 18,000+ catchments. Machine learning continues its rapid advance into operational hydrology, with novel transfer-learning, knowledge-distillation, and model-interoperability frameworks targeting the persistent challenge of data-scarce prediction.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Climate Change and Flood Dynamics

This week's climate-hydrology literature converges on a central message: flood timing, magnitude, and drivers are shifting faster than existing infrastructure and forecasting systems can accommodate. Qi et al. provide the first global-scale quantification of anthropogenic flood timing shifts, while Makhmudova et al. dissect the compound snowmelt-rainfall drivers behind Kazakhstan's extreme spring floods. Dykman et al. tackle the inverse problem — how to calibrate models for flood extremes that fall outside historical experience — and Meng et al. show that ENSO teleconnections to regional flood risk can be parameterized within SWAT. Two additional studies close the loop: one examining how drought-fire interactions reshape the rainfall-runoff relationship, another assessing how glacier-fed basins will respond under CMIP6 warming scenarios.

### Anthropogenic climate change accelerates the onset of global flood timing

**Authors**: Wei Qi, Ying Liu, Xin Jiang, Junguo Liu

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-026-73839-x](https://doi.org/10.1038/s41467-026-73839-x) · **Citations**: 0

**Matched topics**: hydrology, streamflow, flood
{: .label .label-green }

(Also featured in daily harvest on 2026-05-29)

> Floods are among Earth's most devastating natural disasters, with cascading societal and ecological impacts. Flood timing shifts amplify risks by disrupting preparedness, yet their global patterns remain largely unquantified. Using multi-model ensembles, we provide a global-scale assessment of flood timing changes under incremental warming (1.5 °C–4.0 °C). Here we show that anthropogenic forcing advances global flood timing by 0.43 ± 0.25 days per 0.5 °C of warming, with regional divergence: early-flood regions shift even earlier, while late-flood regions experience further delay. At 1.5 °C, approximately 52% of global river basins experience a statistically significant timing advance, rising to 74% at 4.0 °C. These shifts outpace the adaptation capacity of flood-management infrastructure designed for historical flood calendars.

---

### Compound Drivers of Extreme Spring Floods in a Changing Climate: The Esil River Case, Kazakhstan

**Authors**: Lyazzat Makhmudova, Sayat Alimkulov, Ainur Mussina, Harris Vangelis, Elmira Talipova, Oirat Alzhanov et al.

**Journal**: *Earth Systems and Environment* · **DOI**: [10.1007/s41748-026-01219-y](https://doi.org/10.1007/s41748-026-01219-y) · **Citations**: 1

**Matched topics**: hydrology, hydrologic model, river, runoff, water management, flood, climate change
{: .label .label-green }

> There is a global increase in the frequency and intensity of extreme floods driven by climate change, enhanced hydrological variability, and transformations in seasonal moisture accumulation and runoff formation processes. In recent decades, shifts in the temporal and spatial characteristics of spring floods have led to more frequent exceedances of design water levels and increased damage to water management systems, infrastructure, and agriculture. Regions dominated by snow-fed rivers are particularly vulnerable, as imbalances between winter moisture accumulation and spring snowmelt intensification create compound flood risks. This study examines the Esil River in Kazakhstan, analyzing meteorological and hydrological records to characterize how simultaneous increases in winter precipitation and temperature-driven snowmelt acceleration combine with soil moisture antecedent conditions to produce extreme spring flood peaks.

---

### Robust Calibration of Hydrological Models for Simulating Unseen Flood Extremes

**Authors**: Caleb Dykman, Conrad Wasko, Rory Nathan, Ashish Sharma

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr040134](https://doi.org/10.1029/2025wr040134) · **Citations**: 0

**Matched topics**: hydrologic model, flood
{: .label .label-green }

> Calibrating conceptual rainfall–runoff models to predict a catchment's response to extreme rainfall events is a significant challenge, especially when historical data is limited and the events of interest exceed the calibration record. Standard performance metrics such as Nash–Sutcliffe efficiency weight average conditions over extreme events, producing models that systematically underestimate tail behavior. This study introduces a calibration framework that explicitly targets the representation of unseen flood extremes by conditioning on quantile-based loss functions and incorporating storm-scaling constraints from regional frequency analysis. Applied across a large ensemble of Australian catchments, the approach significantly reduces the systematic underestimation of extreme flows while maintaining acceptable performance for median conditions.

---

### Fire can explain rainfall-runoff shifts during and after drought

**Authors**: Sreelakshmi Cherampatta Mana, Tim Peterson, Barry Croke, Takuya Iwanaga, Steven J. Lade

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135776](https://doi.org/10.1016/j.jhydrol.2026.135776) · **Citations**: 0

**Matched topics**: runoff, drought
{: .label .label-green }

> Abstract not available.

---

### A three-layer parameterization framework for ENSO-runoff coupling: Enhanced flood risk in the Huaihe River Basin under climate change

**Authors**: Xianyong Meng, Zhenfei Ge, Jianli Ding, Guoqing Wang, Yiping Wu, Chengbin Chu et al.

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103562](https://doi.org/10.1016/j.ejrh.2026.103562) · **Citations**: 0

**Matched topics**: runoff, streamflow
{: .label .label-green }

> Study region Huaihe River Basin, China, a region significantly affected by ENSO events. Study focus This research develops a three-layer parameterization framework within the SWAT model to quantify ENSO's influence on runoff processes at basin scale. The framework decomposes ENSO's hydrological impact into three mechanistic pathways: precipitation variability, temperature-driven evapotranspiration shifts, and snowmelt timing modifications. Under projected ENSO intensification and warming scenarios, the Huaihe Basin faces substantially elevated flood risk during El Niño years, with peak flows potentially increasing by 15–30% relative to historical baselines.

---

### CMIP6 multi-model projections and glacier-explicit hydrological modelling for seasonal runoff shifts in the Hunza River Basin

**Authors**: Hafsah Batool, Jamal Hassan Ougahi, Amir Ali, Ameer Faisal, Maira Malik, Syed Mahmood et al.

**Journal**: *Meteorology and Atmospheric Physics* · **DOI**: [10.1007/s00703-026-01149-4](https://doi.org/10.1007/s00703-026-01149-4) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow, seasonal, hydropower
{: .label .label-green }

> Abstract not available.

---

## Hydrological Model Development and Calibration

Model development this week spans the full spectrum from subsurface physics to canopy processes and global-scale forcing evaluation. Kootanoor Sheshadrivasan & Langhammer introduce GWSWEX v1.0, a dual-solver approach that bridges physically-based groundwater representation and computationally tractable distributed modeling. Cebulski et al. benchmark new snow interception parameterizations across forest types, addressing a gap in land-surface energy budgets covering 23% of the global land surface. Ruelland et al. present an integrated glacier evolution module for snow-ice-runoff models with multi-criteria calibration. A landmark HESS study (Abbas et al.) benchmarks 24 precipitation datasets across 18,428 catchments, providing an authoritative guide for dataset selection in hydrological modeling. Complementing these physical advances, two Journal of Hydrology Regional Studies papers demonstrate targeted ML calibration techniques for karst basins and gradient-boosting-based runoff calibration.

### GWSWEX v1.0: a dual-solver 1D unsaturated zone model for mass-conservative groundwater recharge and runoff computation in distributed hydrological modelling

**Authors**: Veethahavya Kootanoor Sheshadrivasan, Jakub Langhammer

**Journal**: *Geoscientific Model Development (preprint)* · **DOI**: [10.5194/egusphere-2026-2941](https://doi.org/10.5194/egusphere-2026-2941) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, runoff
{: .label .label-green }

> The faithful numerical representation of the coupled dynamics between groundwater (GW), the unsaturated zone (UZ) and surface water (SW) remains one of the more persistent challenges of regional-scale integrated hydrological modelling. Physically-based models that solve the Richards equation in three dimensions provide a rigorous description of vertical fluxes, but their computational cost, sensitivity to parameter uncertainty, and tendency to over-emphasise capillary forces at the expense of preferential and non-equilibrium flow regimes limit their suitability as self-contained UZ modules in distributed models. GWSWEX v1.0 addresses this by implementing a dual-solver approach: a fast kinematic-wave solver for typical conditions and a Richards-equation solver for near-saturation states. The model is mass-conservative by design and benchmarked against analytical solutions and lysimeter experiments.

---

### An Evaluation of New Snow Interception and Ablation Parameterisations in Continental, Subarctic and Maritime Needleleaf Forests

**Authors**: Alex C. Cebulski, John W. Pomeroy, William C. Floyd

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70573](https://doi.org/10.1002/hyp.70573) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, land surface model
{: .label .label-green }

> Snow interception by forest canopies occurs over 23% of the global land surface, influencing both subcanopy snow accumulation and land-surface energy exchanges. The processes governing snow interception are strongly influenced by both meteorological conditions and canopy density, resulting in differing process emergence in distinctive climates, seasons and forest types. Recent studies have revealed new relationships to represent snow interception and canopy snow ablation processes with potential applicability across a broader range of canopy structures and climatic conditions. This study evaluates three new snow interception and ablation parameterisations against existing approaches in three contrasting forest environments: continental needleleaf forest in Saskatchewan (Canada), subarctic needleleaf forest in northern Finland, and maritime needleleaf forest in British Columbia (Canada). The new parameterisations show improved representation across all three environments.

---

### Representing glacier evolution for modelling hydrological responses to climate change in mountainous catchments

**Authors**: Denis Ruelland, Florian Antoine, Antoine Rabatel

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135769](https://doi.org/10.1016/j.jhydrol.2026.135769) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow
{: .label .label-green }

> Parsimonious snow–ice–runoff model with integrated glacier evolution module. Multi-criteria calibration constrained by streamflow, snow and glacier data. Glacier retreat induces contrasting runoff trajectories across Alpine catchments. Future projections show peak water timing within 2026–2055 for most studied basins.

---

### Comprehensive Global Assessment of 24 Gridded Precipitation Datasets Across 18,428 Catchments Using Hydrological Modeling

**Authors**: A. Abbas, Y. Yang, M. Pan, Y. Tramblay, C. Shen, H. Ji et al.

**Journal**: *Hydrology and Earth System Sciences (HESS)* · **DOI**: [10.5194/hess-30-3399-2026](https://doi.org/10.5194/hess-30-3399-2026) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Numerous gridded precipitation (P) datasets have been developed to address a variety of needs and challenges. However, selecting the most suitable and reliable dataset remains difficult for users. We assessed 24 gridded P datasets across 18,428 catchments using hydrological modeling, providing a global benchmark for precipitation product performance. Results reveal strong regional and climatic dependencies in dataset skill, with no single product outperforming all others globally. Ensemble-based approaches combining top-performing products consistently outperform any individual dataset, particularly in regions with sparse rain-gauge networks.

---

### Modelling multi-component lagged hydrological responses in karst basins using a Bayesian-optimized dual-branch LSTM

**Authors**: Hang Chen, Yu Bao Li, Lihua Chen

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103594](https://doi.org/10.1016/j.ejrh.2026.103594) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow
{: .label .label-green }

> Study region The Qingjiang River Basin (QJB), southwestern China. Study focus Accurate daily runoff prediction in karst basins remains challenging due to the distinctive dual-flow structure. To address this, a Bayesian-optimized dual-branch LSTM is proposed to represent conduit-dominated fast flow and diffuse matrix-dominated slow flow simultaneously. The dual-branch structure explicitly models the contrasting lag responses of these two pathways, and Bayesian optimization efficiently searches the hyperparameter space without manual tuning. Applied to the Qingjiang karst system, the model outperforms standard LSTM and process-based karst models across low-flow, average-flow, and high-flow conditions.

---

### Basin runoff calibration using gradient boosting decision trees: Impact of dual gridded potential evapotranspiration sources on model performance

**Authors**: Ali Amiri, Feza Örüç

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103574](https://doi.org/10.1016/j.ejrh.2026.103574) · **Citations**: 0

**Matched topics**: runoff, streamflow
{: .label .label-green }

> Study region This study focuses on the Iznik Basin, an endorheic catchment in a semi-humid region of Bursa, Türkiye, characterized by significant anthropogenic influence and hydrological sensitivity. Study focus The study implements gradient boosting decision trees (GBDT) for basin runoff calibration and systematically evaluates the sensitivity of calibration performance to two gridded potential evapotranspiration (PET) sources — ERA5-based and GLEAM-based estimates. Differences in PET formulation propagate into significant performance differences, highlighting the importance of PET dataset selection in data-driven hydrological calibration.

---

### Assessing Hydrological Responses to Land Use Type Transition in Watershed with Reservoir Operation Using SWAT Model

**Authors**: Hiyaw Hatiya Ware, Il-Moon Chung, Ju-Young Shin, Myoung-Jin Um

**Journal**: *Water Resources Management* · **DOI**: [10.1007/s11269-026-04766-1](https://doi.org/10.1007/s11269-026-04766-1) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow, reservoir
{: .label .label-green }

> Abstract not available.

---

## Machine Learning and Deep Learning for Streamflow

The ML-for-hydrology field this week presents both state-of-the-art architectures and foundational infrastructure work. FlowGATFormer (Liu et al.) combines graph attention with temporal attention for spatial-temporal streamflow prediction, while Hagen et al. demonstrate that LSTMs can translate GCM signals into daily streamflow for flood projection in Norwegian catchments. Jahangir et al. introduce knowledge distillation as a framework to compress large hydrological DL models while preserving their predictive skill. On the infrastructure side, Singh et al. propose HydroModelSpec — a standardized exchange format that could do for ML hydrological models what NetCDF did for gridded data — and Gao et al. present a multi-source adaptive-fusion transfer learning approach for prediction in data-scarce basins. Liu et al. round out this theme with a 60-day forecasting framework that integrates deep learning with process-based modeling.

### FlowGATFormer: A streamflow prediction model based on spatiotemporal dual attention

**Authors**: Feng Liu, Zhigang Han, J H, Peiqing Xiao, Pan Zhang, Fengrui Chen et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135771](https://doi.org/10.1016/j.jhydrol.2026.135771) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Achieving high accuracy in long-term river streamflow prediction is essential for simulating the terrestrial hydrological cycle and managing water resources. However, traditional hydrological models are limited in capturing complex nonlinear relationships, and existing deep learning models fail to effectively integrate spatial dependencies among hydrological stations with temporal dynamics. This paper proposes FlowGATFormer, a streamflow prediction model combining graph attention networks (GAT) and a Transformer encoder with dual attention mechanisms. The spatial attention module captures inter-station hydrological relationships via a learned adjacency graph, while the temporal attention module weights historical time steps according to their relevance for the prediction horizon. Benchmarked against LSTM, GRU, and Transformer baselines across multiple Chinese river basins, FlowGATFormer achieves state-of-the-art performance at 1–30 day lead times.

---

### Using sequential and non-sequential LSTM neural networks with global climate model forcing for daily streamflow reconstruction and flood projection: Applications to two contrasting flood regimes in Norway

**Authors**: J. S. Hagen, D. Lawrence, A. Sorteberg

**Journal**: *Hydrology research* · **DOI**: [10.1016/j.hydrch.2026.100017](https://doi.org/10.1016/j.hydrch.2026.100017) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, flood
{: .label .label-green }

> Climate change is altering floods in northern, high latitude catchments. This study assesses the ability of Long Short-Term Memory (LSTM) neural networks to translate changes in large-scale atmospheric patterns into daily streamflow for two Norwegian catchments with contrasting flood regimes: a rain-dominated coastal catchment and a snowmelt-dominated inland catchment. Both sequential (standard LSTM) and non-sequential (parallel) architectures are tested with forcing from ERA5-corrected GCM outputs. The non-sequential approach performs better for rain-dominated catchments but shows limited added value for snowmelt-dominated ones. Under RCP8.5, both catchments project increases in autumn flood peaks, with the coastal catchment showing the larger relative change.

---

### Knowledge Distillation for Improving Deep Learning-Based Hydrological Prediction and Fine-Tuning

**Authors**: M. S. Jahangir, J. Quilty, S. Steinschneider, J. Adamowski

**Journal**: *Journal of Geophysical Research Machine Learning and Computation* · **DOI**: [10.1029/2025jh001081](https://doi.org/10.1029/2025jh001081) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> This paper introduces knowledge distillation (KD) as a method for improving deep learning (DL)-based hydrological prediction. The performance of DL models, including long short-term memory networks (LSTMs) and related architectures, is often limited by insufficient training data, high-dimensional parameter spaces, and overfitting risks. KD transfers knowledge from a large, well-trained teacher model to a smaller student model, yielding a compact model that retains the accuracy of its teacher while being faster and more amenable to fine-tuning on new catchments. Applied to streamflow prediction across a diverse set of CAMELS catchments, KD-trained students match or exceed the baseline LSTM while requiring 40–60% fewer parameters, with particularly strong gains in data-scarce and hydrologically complex basins.

---

### AI-driven seasonal streamflow prediction in Victoria: a focus on ENSO climate predictor

**Authors**: Sabrina Bani, I. Hossain, M. Imteaz, Patrick Ryan Morrison

**Journal**: *Stochastic Environmental Research and Risk Assessment* · **DOI**: [10.1007/s00477-026-03256-5](https://doi.org/10.1007/s00477-026-03256-5) · **Citations**: 0

**Matched topics**: streamflow, seasonal
{: .label .label-green }

> Seasonal prediction of streamflow plays a crucial role in water allocation in southeastern Australia, where hydroclimatic variability is modulated by large-scale ocean-atmosphere interactions. This study evaluates multiple AI-based seasonal streamflow prediction models — including LSTM, random forest, and XGBoost — with and without ENSO indices as predictors across Victorian catchments. ENSO-informed models significantly outperform ENSO-agnostic models in autumn and winter predictions, reflecting the dominant teleconnection patterns of El Niño-Southern Oscillation on Victorian rainfall. The best-performing configurations achieve Nash-Sutcliffe efficiencies above 0.75 for seasonal prediction horizons of up to four months.

---

### Multi-Source Adaptive-Fusion Transfer Learning for Streamflow Forecasting in Data-Scarce Catchments

**Authors**: Yuxuan Gao, Dongfang Liang, Edoardo Borgomeo, Hiroshi Cho

**Journal**: *ESSOAr (preprint)* · **DOI**: [10.22541/essoar.15004149/v1](https://doi.org/10.22541/essoar.15004149/v1) · **Citations**: 0

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> Streamflow gauging records remain sparse in many regions, limiting hydrological predictions. Transfer Learning (TL), which uses knowledge from data-rich sources to improve predictions in data-scarce target catchments, has emerged as a promising approach. However, existing TL methods typically rely on a single source domain and ignore the heterogeneity of knowledge across multiple potential source catchments. This paper proposes a Multi-Source Adaptive-Fusion Transfer Learning (MSAFTL) framework that adaptively weights contributions from multiple source catchments based on their hydrological similarity and knowledge transferability. Applied across a diverse set of data-scarce catchments in Asia and Africa, MSAFTL substantially outperforms single-source TL and scratch-trained LSTMs, with the largest gains in the most data-limited settings.

---

### HydroModelSpec: Toward Standardized Machine Learning Model Exchange in Hydrology

**Authors**: Nikhil Singh, Ramteja Sajja, Yusuf Sermet, Ibrahim Demir

**Journal**: *EarthArXiv (preprint)* · **DOI**: [10.31223/x53v1b](https://doi.org/10.31223/x53v1b) · **Citations**: 0

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> The rapid growth of deep learning models for hydrological forecasting (e.g., CNNs, LSTMs, Transformers) has created a fragmented ecosystem where trained models remain tied to their original frameworks, training datasets, and preprocessing pipelines. This prevents reproducibility, benchmarking, and operational deployment. HydroModelSpec proposes a standardized exchange format — analogous to ONNX for general ML models — specifically tailored to hydrological models: encoding not only the model weights and architecture but also the forcing variable definitions, catchment metadata, normalization schemes, and calibration history. A reference implementation is provided for PyTorch-based models, with conversion utilities for common hydrological DL frameworks.

---

### Enhancing hydrological hazard early warning: a 60 d streamflow forecasting framework integrating deep learning and process-based modeling

**Authors**: Zhijie Liu, Hanbo Yang, Dawen Yang

**Journal**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-26-2353-2026](https://doi.org/10.5194/nhess-26-2353-2026) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, hydropower
{: .label .label-green }

> Reliable medium- and long-term streamflow forecasting is a cornerstone of hydrological hazard early warning and water resources management, yet achieving accurate predictions with sufficient lead times remains elusive. This paper presents a hybrid framework that combines a process-based hydrological model (providing physical constraints and state variables) with a deep learning post-processor (correcting systematic biases and capturing nonlinear dynamics) to achieve 60-day streamflow forecasts. The framework is evaluated across multiple Chinese river basins spanning diverse hydroclimatic regimes. The hybrid approach consistently outperforms both purely process-based and purely data-driven baselines at lead times beyond 30 days, with the largest relative gains in basins with strong seasonal dynamics and interannual variability.

---

## Water Resources and Hydroclimatic Dynamics

The final theme spans applied and observational hydrology across diverse spatial scales and settings. Wang et al. show that declining snowfall fraction in the Upper Indus Basin is already altering streamflow seasonality — a canary-in-the-coal-mine result for glaciated basins globally. Luan et al. deliver a high-resolution surface water–groundwater interaction model under anthropogenic pressures in riparian zones. Zou et al. document 38 years of reservoir surface water dynamics in the Yellow River Basin using remote sensing, while Huang et al. reveal a tipping-point-like transition from endorheic to exorheic drainage in Tibetan lakes. Two additional papers examine wetland watershed hydrology under climate wetting and streamflow response to climate change in the Bago River Basin.

### Streamflow seasonality responds to changes in snowfall fraction in the Upper Indus Basin

**Authors**: Yixuan Wang, Yan-Jun Shen, Xiaolong Zhang, Muhammad H. Zaman, Muhammad Attique Khan

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135773](https://doi.org/10.1016/j.jhydrol.2026.135773) · **Citations**: 0

**Matched topics**: streamflow, seasonal
{: .label .label-green }

> Abstract not available.

---

### Daily-Resolution Modelling of Surface Water–Groundwater Interaction Under Multiple Human Activities in a Riparian Zone

**Authors**: Qinghua Luan, Yuhara Yamamoto, Qingyan Sun, Chuiyu Lu, Weichen Wu, Chu Wu et al.

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70578](https://doi.org/10.1002/hyp.70578) · **Citations**: 0

**Matched topics**: streamflow, surface water
{: .label .label-green }

> Surface water–groundwater interaction (SGI) is a crucial process for the water cycle, and its remarkable heterogeneity is increasingly shaped by intensifying anthropogenic influences. Understanding SGI under multiple human activities at daily resolution remains an important modeling challenge. This study develops a coupled surface water–groundwater model for a riparian zone subject to irrigation extraction, river regulation, and land-use change. The model resolves daily exchange fluxes across the river-aquifer interface and is validated against piezometric records and streamflow observations. Results reveal that irrigation extraction and river-regulation operations together account for more than 60% of the total temporal variability in daily SGI fluxes, highlighting the dominant role of human management over climate variability in riparian zones.

---

### Long-term reservoir surface water dynamics in the Yellow River Basin (1986–2024)

**Authors**: Yebin Zou, Peiyu Cong, Shuaijuan Zhang, Xiying Wang, Pan Pan, Guoce Gao et al.

**Journal**: *Journal of Arid Environments* · **DOI**: [10.1016/j.jaridenv.2026.105656](https://doi.org/10.1016/j.jaridenv.2026.105656) · **Citations**: 0

**Matched topics**: reservoir, surface water
{: .label .label-green }

> Abstract not available.

---

### From endorheic to exorheic: Tibetan lake hydrodynamics driven by global change and hydrological reorganization and implications to Mars

**Authors**: Chang Huang, Zikang Li, Gaia Stucky de Quay, Zhongping Lai

**Journal**: *Global and Planetary Change* · **DOI**: [10.1016/j.gloplacha.2026.105546](https://doi.org/10.1016/j.gloplacha.2026.105546) · **Citations**: 0

**Matched topics**: hydrology, earth system model
{: .label .label-green }

> Abstract not available.

---

### Hydrological Changes to Climate Wetting in a Wetland-Dominated Agricultural Watershed

**Authors**: Sharhad Wainty, Taufique H. Mahmood

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70589](https://doi.org/10.1002/hyp.70589) · **Citations**: 0

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> Understanding the partition of input flux like precipitation into output fluxes (evapotranspiration (ET) and streamflow (Q)) is important to understand the hydrological responses under a changing climate. A wetland-dominated agricultural watershed in the Red River Basin (USA/Canada) is used as the study region. The study quantifies hydrological responses to observed climate wetting trends and evaluates whether the Budyko framework can capture the documented shifts. Results show that under climate wetting, runoff ratios have increased non-linearly due to wetland storage filling and saturation-excess runoff mechanisms, requiring extensions to the standard Budyko parameterization.

---

### Streamflow response to climate change in the Bago River Basin using SWAT+ hydrological model

**Authors**: Cho Cho Tun, Zin Mar Lar Tin San, Win Win Zin

**Journal**: *Journal of Water and Climate Change* · **DOI**: [10.2166/wcc.2026.092](https://doi.org/10.2166/wcc.2026.092) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> DEM, soil and land cover processed in QGIS to derive streamflow; SWAT+ model calibrated with observed data, bias-corrected GCM inputs used for future climate and impact assessment. Climate change projections from multiple CMIP6 models are applied to assess future changes in annual and seasonal streamflow in the Bago River Basin, Myanmar. Results show a general increase in wet-season peak flows and reduced dry-season baseflows under all warming scenarios, with hydropower and irrigation implications for the basin's water management infrastructure.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 1,232 |
| After deduplication | 1,045 |
| After LLM relevance filtering | 26 |
| Rejected (not relevant) | 1,019 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Journal of Hydrology | 4 |
| Hydrological Processes | 4 |
| Journal of Hydrology Regional Studies | 4 |
| Nature Communications | 1 |
| Water Resources Research | 1 |
| Natural Hazards and Earth System Sciences | 1 |
| Hydrology and Earth System Sciences | 1 |
| Earth Systems and Environment | 1 |
| Hydrology research | 1 |
| Journal of Geophysical Research Machine Learning | 1 |
| Stochastic Environmental Research and Risk Assessment | 1 |
| Water Resources Management | 1 |
| Global and Planetary Change | 1 |
| Journal of Arid Environments | 1 |
| Journal of Water and Climate Change | 1 |
| Meteorology and Atmospheric Physics | 1 |
| Preprints (ESSOAr/EarthArXiv/GMD) | 3 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

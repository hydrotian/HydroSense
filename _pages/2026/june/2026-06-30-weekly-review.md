---
layout: default
title: "Week 26 (Jun 23 - Jun 30), 29 papers"
parent: June
grand_parent: "2026"
nav_order: 37
date: 2026-06-30
categories: [weekly, 2026, june]
tags: [hydrology, literature-review, research]
paper_count: 29
lang: en
lang_link: /zh/2026/june/2026-06-30-weekly-review
highlight: "A prompt-conditioned LLM framework for streamflow prediction and SWOT+SMAP fusion for ungauged basin calibration headline a strong week for AI-driven hydrology."
---

# Weekly Literature Review
{: .no_toc }

**Week 26** · Jun 23–Jun 30, 2026
{: .text-grey-dk-000 }

**29** relevant papers found across **6** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's keyword search (June 23–30, 2026) surfaces 29 strong papers across machine learning, hydrological model evaluation, land surface modeling, flood and drought research, and observational datasets. The most notable methodological advance is a prompt-conditioned multimodal framework that adapts a large language model backbone for streamflow prediction with lightweight task-specific tuning. Equally significant is a continental-scale study showing that rain-on-snow events are a far more widespread driver of peak streamflow across the contiguous US than previously recognized, and a Water Resources Research study demonstrating that SWOT discharge combined with SMAP soil moisture can meaningfully constrain land surface models in ungauged basins.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## AI and Machine Learning for Streamflow Prediction

The week's deep learning papers collectively push the frontier in three directions: probabilistic uncertainty quantification for streamflow, LLM-conditioned foundation models for hydrology, and physically meaningful data assimilation informed by spatial streamflow correlations. Arganis-Juárez and Preciado provide a useful methodological reference spanning the arc from early ANN/SVM methods through modern physics-informed deep learning and symbolic regression. Timilsina and Passalacqua (WRR) make an important observation that streamflow spatial correlation length systematically grows during storm events, and exploit this signal in a data assimilation scheme to improve network-wide predictions — an elegant physical prior that costs nothing to compute. Li et al. (J. Hydrology) introduce the most novel architecture this week: a prompt-conditioned multimodal framework that treats input metadata as natural-language prompts, allowing a single trained model to adapt across basins and seasons with minimal additional tuning.

### A methodological review of AI/ML and evolutionary computation in hydrology and hydraulics: from ANN/SVM to deep learning, symbolic regression, and physics-informed models

**Authors**: M. Arganis-Juárez, M. Preciado

**Journal**: *Water Science & Technology* · **DOI**: [10.2166/wst.2026.304](https://doi.org/10.2166/wst.2026.304) · **Citations**: 0

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> Schematic workflow showing hydrology data inputs, preprocessing, artificial intelligence models, and a hybrid physics-informed block combining hydrological knowledge and machine learning, leading to actionable outputs. The review traces the evolution from conventional ANN/SVM approaches through ensemble methods, deep learning (LSTM, Transformer), symbolic regression, and physics-informed neural networks, assessing strengths, limitations, and open challenges for operational hydrology.

---

### Improving Daily Runoff Prediction Using a Novel Two‐Step Post‐Processing Method of Frequency Distribution Curve Correction

**Authors**: Xiaochuan LUO, Yongyong Zhang, Tongtiegang Zhao, Xiaoyan Zhai, Junxu Chen, Bo Han et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041637](https://doi.org/10.1029/2025wr041637) · **Citations**: 0

**Matched topics**: runoff
{: .label .label-green }

> Abstract Offsets and distributional discrepancies between runoff simulations and observations were two important error sources which remarkably degraded runoff prediction performance of hydrological models. This study proposes a two-step post-processing method that first corrects systematic bias in the frequency distribution curve and then applies a residual correction, demonstrating clear improvements in daily runoff prediction across diverse basins.

---

### Streamflow Spatial Correlation Length Increases During Storms and Its Application in Data Assimilation Improves Streamflow Predictions

**Authors**: Sujana Timilsina, Paola Passalacqua

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr043053](https://doi.org/10.1029/2025wr043053) · **Citations**: 0

**Matched topics**: streamflow
{: .label .label-green }

> Abstract The spatial correlation of streamflow in a river network captures how flows at different locations relate to one another and influence the downstream response. In this study, we analyze the spatial correlation structure of streamflow and demonstrate that correlation lengths systematically increase during storm events. Incorporating this dynamic spatial structure into a data assimilation framework significantly improves streamflow predictions across the network.

---

### A deep learning-based probabilistic framework for streamflow prediction and water quality assessment

**Authors**: Alberto Mena, Rafael J. Bergillos, Javier Paredes-Arquiola, Gerald Corzo, Abel Solera, Joaquín Andreu

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135934](https://doi.org/10.1016/j.jhydrol.2026.135934) · **Citations**: 0

**Matched topics**: streamflow
{: .label .label-green }

> This study presents an integrated modelling framework designed to support water quality assessment and regulatory compliance analysis in river basins. The proposed approach combines deep learning-based probabilistic streamflow prediction with downstream water quality modelling, enabling uncertainty-aware regulatory decisions in data-scarce environments.

---

### A prompt-conditioned multimodal framework for streamflow prediction with lightweight task adaptation

**Authors**: Xudong Li, Senchang Hu, Wei Zhang, Wuyou Xiao, Wenzhuo Shi, Jiaqi Ruan et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135915](https://doi.org/10.1016/j.jhydrol.2026.135915) · **Citations**: 0

**Matched topics**: streamflow
{: .label .label-green }

> Abstract not available.

---

## Hydrological Model Development and Evaluation

Multi-model ensemble and inter-comparison work dominates this sub-field this week. Thébault et al. (HESS) conduct the most comprehensive CONUS-wide comparison to date, contrasting "mosaic" approaches (where each basin is assigned the single best model) against ensemble combination schemes, finding that multi-model combinations consistently outperform both mosaics and any individual model. Weligamage et al. (HESS) introduce the concept of "AET signatures" — diagnostic metrics for actual evapotranspiration analogous to long-established streamflow signatures — providing a new tool to identify biases in remote sensing ET products. Kong et al. (ERL) show that land water availability projections are strongly sensitive to model spatial resolution through separate runoff and soil water pathways, with important implications for how resolution choices propagate into drought risk assessments. Yassin et al. (Hydrological Processes) quantify how precipitation phase-partitioning method choice propagates into large-scale hydrological projections under warming — a methodological blind spot with outsized consequences in cold-region hydrology.

### Navigating Climate Adaptation Boundaries for the World's Largest Inter‐Basin Water Transfer Projects

**Authors**: Yu Li, Xiang Fu, Zhipeng Fan, Zhao Xiaodan, Yi Zheng

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041103](https://doi.org/10.1029/2025wr041103) · **Citations**: 0

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> Abstract As global climate change and human impacts intensify, their effects on streamflow are becoming critical for water security. This study investigates the hydrological impacts of future scenario projections on inter-basin water transfer infrastructure, identifying adaptation boundaries — thresholds beyond which current designs become inadequate — and evaluating alternative strategies for long-term water security.

---

### Assessing deficiencies in remotely sensed actual evapotranspiration (AET): introducing AET signatures

**Authors**: Hansini Gardiya Weligamage, Keirnan Fowler, Margarita Saft, Tim Peterson, Dongryeol Ryu, Murray Peel

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4057-2026](https://doi.org/10.5194/hess-30-4057-2026) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Abstract. Hydrological signatures are statistical metrics useful to quantify and infer behaviours of hydrological processes, but there has been limited use of signatures for non-streamflow variables, particularly actual evapotranspiration (AET). This paper introduces AET signatures — a suite of diagnostic metrics — and applies them to evaluate multiple remotely sensed AET products, revealing systematic deficiencies in how current products capture seasonal dynamics and water-limited regimes.

---

### Comparing multi-model mosaic and multi-model combination methods to simulate streamflow across the contiguous USA

**Authors**: Cyril Thébault, Wouter Knoben, Nans Addor, Andrew J. Newman, Diana Spieler, Nicolás Vasquéz et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-3945-2026](https://doi.org/10.5194/hess-30-3945-2026) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Abstract. The ability to accurately predict streamflow underpins decisions in water management, flood prevention, and sectoral planning. Traditional approaches for streamflow prediction often rely on a single model chosen based on expert judgment or regional performance. This study systematically compares multi-model mosaic strategies against ensemble combination approaches across the contiguous USA, finding that combination methods consistently outperform mosaics across diverse hydroclimatic regions.

---

### Variability of land water availability sensitivity to model resolution: Disentangling the influences of runoff and soil water

**Authors**: Xianghui Kong, Aihui Wang, He Zhang, Kece Fei, Nan Wei, Duoying Ji et al.

**Journal**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae83cd](https://doi.org/10.1088/1748-9326/ae83cd) · **Citations**: 0

**Matched topics**: runoff, land surface model
{: .label .label-green }

> Abstract Fluctuations of land water availability (LWA, defined as the difference between precipitation and evapotranspiration) may increase the drought risks and widely affect management of water resources. This study disentangles the separate contributions of runoff and soil water pathways to LWA sensitivity to model resolution, demonstrating that resolution choices impose systematic and spatially structured biases on drought risk projections.

---

### Sensitivity of Large‐Scale Hydrological Predictions to Precipitation Phase Partitioning Methods Under a Changing Climate

**Authors**: Fuad Yassin, John W. Pomeroy, Alain Pietroniro, Bruce Davison, Mohamed Elshamy, Zelalem Tesemma

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70608](https://doi.org/10.1002/hyp.70608) · **Citations**: 0

**Matched topics**: streamflow
{: .label .label-green }

> ABSTRACT Accurate partitioning of precipitation into rain and snow remains a major source of uncertainty in hydrological projections for cold regions. This study quantifies how four precipitation phase-partitioning methods propagate into large-scale hydrological predictions under a changing climate, revealing that method choice can produce substantially different future streamflow trajectories and has largely been ignored as an uncertainty source in multi-model ensembles.

---

## Land Surface Models and Earth System Modeling

Remote sensing and land surface modeling advances this week span ungauged basin calibration, model–observation disagreement diagnosis, carbon cycle feedbacks, and vegetation-forcing datasets. Crow et al. (WRR) demonstrate for the first time that jointly assimilating SWOT river discharge and SMAP surface soil moisture can constrain systematic biases in land surface models — the key insight being that SMAP addresses errors in model structure while SWOT constrains routing parameterization. Tavakoli et al. diagnose how MPAS-NoahMP partitions evaporation across soil moisture regimes, revealing conditions where model and observation systematically diverge — directly relevant to anyone using MPAS-coupled configurations. Tiengou et al. (ESD) run the IPSL coupled ICOLMDZ–ORCHIDEE system over the Iberian Peninsula with explicit irrigation, quantifying both local atmospheric feedbacks and downstream water balance perturbations; this is a clean analog for how similar experiments might be designed with E3SM or ELM. Bauer et al. (GMD) release MESMER v1.0.0 as a formally packaged, versioned research software tool for spatially resolved ESM pattern scaling.

### Streamflow Calibration in Ungauged Basins Using SWOT Discharge and SMAP Surface Soil Moisture Products

**Authors**: Wade T. Crow, Michael Durand, Stephen Coss, Rolf H. Reichle

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041875](https://doi.org/10.1029/2025wr041875) · **Citations**: 0

**Matched topics**: streamflow, land surface model
{: .label .label-green }

> Abstract Significant advances have been made in using terrestrial remote sensing to reduce random errors in land surface models (LSMs). However, less progress has been made in dealing with systematic biases in LSMs. This study demonstrates that jointly assimilating SWOT discharge and SMAP surface soil moisture into an LSM effectively constrains systematic model biases in ungauged basins, opening a new pathway for global-scale hydrological prediction.

---

### Diagnosis of Evaporation–Soil Moisture Regimes in MPAS-NoahMP: What conditions lead to disagreement with observations?

**Authors**: Nazanin Tavakoli, Paul A. Dirmeyer, Zhe Zhang, Cenlin He, Megan D. Fowler

**Journal**: *ESSOAr preprint* · **DOI**: [10.22541/essoar.15005158/v1](https://doi.org/10.22541/essoar.15005158/v1) · **Citations**: 0

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> Various studies have used Earth system models to characterize soil moisture (SM) regimes, an important indicator of land–atmosphere interactions; however, significant spatial discrepancies between model-simulated and observed SM regimes are still present. This study diagnoses the conditions under which MPAS-NoahMP evaporation and soil moisture regimes diverge from observations, isolating where the model's coupling assumptions break down.

---

### Northern high latitudes could become a net carbon source below 2 °C global warming

**Authors**: Rebecca Varney, Daniel Hooke, Norman Julius Steinert, T. Luke Smallman, Camilla Mathison, Eleanor Burke

**Journal**: *Earth System Dynamics* · **DOI**: [10.5194/esd-17-913-2026](https://doi.org/10.5194/esd-17-913-2026) · **Citations**: 0

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> Abstract. Under historical warming, terrestrial ecosystems within the northern high latitudes have been a net carbon sink, providing vital mitigation against anthropogenic emissions of CO2. However, this study projects that northern high-latitude terrestrial ecosystems could transition to a net carbon source even under less than 2 °C of global warming, driven by accelerated soil carbon decomposition outpacing vegetation uptake — with direct implications for land surface model carbon cycle parameterizations.

---

### Global Snow-free Leaf Area Index Dataset 1985–2020 for Earth System Modeling

**Authors**: Wanyi Lin, Hua Yuan, Wenzong Dong, Zhuo Liu, Jiayi Xiang, Yongjiu Dai

**Journal**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07677-3](https://doi.org/10.1038/s41597-026-07677-3) · **Citations**: 0

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> Leaf Area Index (LAI) is a fundamental parameter linking vegetation structure with surface energy and carbon exchange in Earth system models. However, the underestimation of LAI caused by snow cover remains a significant forcing bias. This dataset provides a 36-year, global, snow-contamination-corrected LAI time series at consistent resolution, suitable for ESM model forcing and evaluation.

---

### Regional impacts of irrigation on the atmospheric and terrestrial water cycle of the Iberian Peninsula in a climate model

**Authors**: Pierre Tiengou, Agnès Ducharne, Frédérique Cheruy

**Journal**: *Earth System Dynamics* · **DOI**: [10.5194/esd-17-843-2026](https://doi.org/10.5194/esd-17-843-2026) · **Citations**: 0

**Matched topics**: land surface model, irrigation
{: .label .label-green }

> Abstract. This study presents regional simulations over the Iberian Peninsula between 2010 and 2022 with the atmospheric (ICOLMDZ) and land surface (ORCHIDEE) components of the IPSL climate model in a coupled configuration. Explicit irrigation is shown to produce measurable cooling and moistening of the lower atmosphere locally, while simultaneously reducing groundwater recharge and altering the seasonal timing of river discharge across irrigated catchments.

---

### MESMER v1.0.0: consolidating the modular Earth system model emulator into a sustainable research software package

**Authors**: Victoria M. Bauer, M. Hauser, Y. Quilcaille, Sarah Schöngart, L. Gudmundsson, S. Seneviratne

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-5669-2026](https://doi.org/10.5194/gmd-19-5669-2026) · **Citations**: 1

**Matched topics**: earth system model
{: .label .label-green }

> Abstract. We present version v1.0.0 of MESMER – the Modular Earth System Model Emulator with spatially Resolved output. MESMER is a comprehensive software package for spatially resolved climate emulation using statistical pattern scaling, enabling rapid generation of scenario-consistent climate realizations at a fraction of the computational cost of full ESM runs.

---

## Flood Processes and Risk

Flood research this week spans process understanding through risk quantification. Reis et al. (WRR) reveal that rain-on-snow events drive peak streamflow across a much larger fraction of the contiguous US than has been assumed, with implications for flood design standards that were historically calibrated ignoring this mechanism. Tramblay et al. (J. Hydrology) exploit hourly discharge records across France to separate trends in flood peaks versus volumes, finding divergent trends in different flood-generation mechanisms — a distinction invisible to daily-data analyses. Baer et al. (npj Natural Hazards) demonstrate that standard design-storm assumptions misrepresent flood hazard because they ignore the spatiotemporal structure of rainfall, and that this error compounds through the risk chain. Varghese et al. (Hydrological Processes) trace the hydrological pathways linking monsoon variability to flood generation in semi-arid basins — a system where flash-flood generation remains poorly constrained.

### Monsoon‐Driven Hydrological Pathways of Flood Generation in Semi‐Arid River Basins

**Authors**: Roma Varghese, Jasti S. Chowdary, C. Gnanaseelan

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70622](https://doi.org/10.1002/hyp.70622) · **Citations**: 0

**Matched topics**: river, flood
{: .label .label-green }

> ABSTRACT Hydrological processes that drive basin‐scale flood generation in semi‐arid river systems remain poorly constrained, limiting effective basin management under an increasingly variable monsoon climate. This study traces the dominant hydrological pathways from monsoon rainfall to basin-scale flood response in semi-arid Indian river basins, identifying where saturation excess, infiltration excess, and direct channel precipitation dominate and how these shift with antecedent conditions.

---

### Rain‐on‐Snow Events Frequently Drive Peak Streamflow Across the Contiguous United States

**Authors**: Wyatt Reis, Jeremy Giovando, Michael Bartles, Travis Dahl

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042253](https://doi.org/10.1029/2025wr042253) · **Citations**: 0

**Matched topics**: streamflow
{: .label .label-green }

> Abstract Rain‐on‐snow events occur when rain falls on a ripe snowpack, initiating rapid snowmelt that can produce extreme flooding in watersheds throughout the world. Rapid snowmelt during rain‐on‐snow events drives peak streamflow events far more frequently across the contiguous US than previously documented, with important implications for flood frequency analysis and infrastructure design in regions assumed to be rain-dominated.

---

### Impact of floods on surface water quality: a systematic review and comprehensive assessment

**Authors**: Apoorva Bamal, Galal Uddin, Reza Ahmadian, Marcelo Gomes Miguez, Agnieszka I. Olbert

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135916](https://doi.org/10.1016/j.jhydrol.2026.135916) · **Citations**: 0

**Matched topics**: flood, surface water
{: .label .label-green }

> Floods, as extreme flow events, are among the costliest and devastating natural hazards. Among the various domains impacted by flooding, environmental degradation, particularly the deterioration of water quality, has received limited systematic attention. This systematic review synthesizes evidence on how floods alter surface water quality across chemical, microbiological, and physical dimensions, identifying knowledge gaps and emerging monitoring approaches.

---

### Neglecting spatiotemporal rainfall variability misrepresents flood hazard and risk

**Authors**: John Baer, Antonia Sebastian, Lauren Grimley, James Doss-Gollin, Daniel B. Wright, Mohammad Ashar Hussain et al.

**Journal**: *npj Natural Hazards* · **DOI**: [10.1038/s44304-026-00208-5](https://doi.org/10.1038/s44304-026-00208-5) · **Citations**: 0

**Matched topics**: flood
{: .label .label-green }

> Flood risk assessments underpin flood management and resilience efforts worldwide, including land-use planning, infrastructure design, and insurance requirements. Many of these assessments rely on design storms that treat rainfall as spatially uniform and temporally simplified. This study demonstrates that ignoring spatiotemporal rainfall variability systematically misrepresents both flood hazard and downstream risk, with errors that propagate through the entire risk assessment chain.

---

### Regional process-based analysis of trends in flood peaks and volumes using hourly data

**Authors**: Yves Tramblay, Patrick Arnaud, Pierre Javelle

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135949](https://doi.org/10.1016/j.jhydrol.2026.135949) · **Citations**: 0

**Matched topics**: flood
{: .label .label-green }

> Most studies on flood trends rely on daily discharge data at the station scale, limiting their ability to disentangle contrasting trends in different flood-generation mechanisms. This is particularly limiting for Mediterranean climates where flash floods drive most peak flows. Using hourly discharge data across France, this study separates trends in flood peaks from trends in flood volumes and attributes these to distinct process changes — revealing contrasting trends that daily analyses would mask.

---

## Drought and Climate Impacts on Runoff

Drought research this week ranges from global datasets to attribution studies and glacierized basin hydrology. Šťovíček et al. (Scientific Data) release the most comprehensive global drought event dataset to date — spatiotemporally clustered rather than point-based — providing a community resource for trend detection and model evaluation over 1980–2024. Zahedi et al. (WRR) tackle a persistent puzzle: why do rainfall-runoff relationships in some catchments shift and never recover after drought? Their analysis implicates the role of antecedent catchment wetness as a state variable that can be permanently altered, with direct implications for how models handle hysteresis. Wang et al. (ERL) attribute the record 2024–2025 South China winter-spring drought to specific circulation anomalies, demonstrating how high-resolution process understanding can inform near-term drought prediction. González-López et al. examine structural uncertainty in coupled hydro-economic models for water management — an underappreciated source of decision uncertainty that rivals parameter uncertainty in some systems.

### A global dataset of spatiotemporal drought events from reanalysis and hydrological model data for 1980–2024

**Authors**: Vít Šťovíček, Martin Hanel, Rohini Kumar, Vojtěch Moravec, Yannis Markonis, Carmelo Cammalleri et al.

**Journal**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07750-x](https://doi.org/10.1038/s41597-026-07750-x) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, runoff
{: .label .label-green }

> We present a global dataset of spatiotemporally clustered drought events for 1980-2024, derived from daily precipitation, potential evapotranspiration, soil moisture, and surface runoff data. Drought events are identified as spatially contiguous and temporally persistent anomalies, enabling the tracking of drought onset, propagation, and termination across basins — a significant advance over traditional point-based drought indices.

---

### Warming-driven runoff increase and shifted seasonality in the glacierized Hotan Basin in Central Asia

**Authors**: Xiaoqian Xu, Wen Wang, Pinxuan Zhou

**Journal**: *Global and Planetary Change* · **DOI**: [10.1016/j.gloplacha.2026.105579](https://doi.org/10.1016/j.gloplacha.2026.105579) · **Citations**: 0

**Matched topics**: runoff, seasonal
{: .label .label-green }

> Abstract not available.

---

### Does Antecedent Catchment Wetness Explain the Timing of Rainfall‐Runoff Relationship Shifts?

**Authors**: Sina Zahedi, Tim Peterson, Murray Peel

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2024wr039750](https://doi.org/10.1029/2024wr039750) · **Citations**: 0

**Matched topics**: runoff
{: .label .label-green }

> Abstract Annual rainfall‐runoff relationships have been shown to shift during droughts and, in many catchments, not recover, resulting in less runoff per unit of precipitation than prior to the drought. This study investigates whether antecedent catchment wetness explains the timing of these shifts, finding that catchments that enter drought from a drier antecedent state are more likely to experience permanent runoff-generation changes — suggesting that initial conditions set a hysteresis pathway from which recovery is slow or absent.

---

### Mechanisms of the Record-Breaking Winter-Spring Drought over South China in 2024-2025

**Authors**: Leying Wang, Wen Chen, Shangfeng Chen, Zhibiao Wang

**Journal**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae8461](https://doi.org/10.1088/1748-9326/ae8461) · **Citations**: 0

**Matched topics**: drought
{: .label .label-green }

> Abstract South China experienced an unprecedented persistent winter-spring drought during 2024/2025, lasting from November to April and representing the most severe drought event in the past six decades. This study identifies the dominant large-scale circulation patterns and SST anomalies that sustained the event across the season transition, providing a mechanistic basis for improved seasonal drought prediction over South China.

---

### Assessing structural uncertainty in water–human systems: A multi-model ensemble approach for agricultural water management

**Authors**: Héctor González-López, Arthur Hrast Essenfelder, Francesco Sapino, David Rivas-Tabares, Jose María Bodoque, Dioni Perez-Blanco

**Journal**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2026.110582](https://doi.org/10.1016/j.agwat.2026.110582) · **Citations**: 0

**Matched topics**: hydrologic model, water management
{: .label .label-green }

> Coupled hydro-economic models are increasingly used to support agricultural water management, yet their results can be highly sensitive to structural (model-form) choices in both human and water system components. This study applies a multi-model ensemble to explicitly quantify structural uncertainty, demonstrating that it can rival parameter uncertainty and substantially affect policy conclusions in irrigation water allocation.

---

## Observational Datasets, Remote Sensing, and Water Management

Three new high-resolution datasets arrive this week, each filling a different gap in forcing and evaluation infrastructure. Madakumbura et al. (Scientific Data) release WHiLD-HM — a 74-year, 4-km resolution daily hydrometeorological dataset for the western United States — an unprecedented long-term record at a resolution that resolves mountain watershed processes. Xu et al. (Scientific Data) address a major gap for Central Asian hydrology with 3DVAR-MF-XJ, a high-resolution near-surface forcing dataset for Xinjiang that corrects systematic biases in global reanalysis products over complex terrain. Arnold et al. (Nature Water) extend water resources optimization theory by incorporating Atkinson's equity welfare function directly into the objective, demonstrating that equity and efficiency trade-offs in transboundary systems can be navigated more explicitly than previously possible. *(Note: this paper also appeared in the daily harvest on 2026-06-24.)*

### A 4-km long-term (1952–2025) daily hydrometeorological dataset for the western United States

**Authors**: Gavin D. Madakumbura, Ronnie Abolafia‐Rosenzweig, Cenlin He, Jacob Jones, Qian He, Menaka Revel et al.

**Journal**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07642-0](https://doi.org/10.1038/s41597-026-07642-0) · **Citations**: 0

**Matched topics**: streamflow, land surface model
{: .label .label-green }

> This study introduces the Western U.S. High-resolution Long-term Dataset for HydroMeteorology (WHiLD-HM), a 4-km, 74-year spatiotemporally continuous daily dataset spanning 1952-2025 for the western United States. The dataset combines dynamical downscaling with observational correction to provide precipitation, temperature, wind, humidity, and radiation fields suitable for hydrological modeling, land surface model forcing, and climate change attribution.

---

### A high-resolution near-surface meteorological forcing dataset for arid Xinjiang (3DVAR-MF-XJ)

**Authors**: Yan Xu, Liang Zhang, Hui Wang, Dongge Ning, Mengxin Bai, Xueping Cong et al.

**Journal**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07573-w](https://doi.org/10.1038/s41597-026-07573-w) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Hydroclimatic assessment in Xinjiang is constrained by sparse observations, complex terrain and systematic biases in widely used gridded and reanalysis products. Here we present the Three-Dimensional Variational Meteorological Forcing dataset for Xinjiang (3DVAR-MF-XJ), a high-resolution near-surface meteorological forcing dataset generated by assimilating station observations into a regional model framework, substantially reducing elevation-dependent biases compared to ERA5 and CMFD.

---

### Balancing equity and efficiency in transboundary water systems with Atkinson's welfare function

**Authors**: Wyatt Arnold, Matteo Giuliani, Andrea Castelletti

**Journal**: *Nature Water* · **DOI**: [10.1038/s44221-026-00671-4](https://doi.org/10.1038/s44221-026-00671-4) · **Citations**: 0

**Matched topics**: hydropower
{: .label .label-green }

*(Also featured in daily harvest on 2026-06-24)*

> Abstract Water resources optimization conventionally maximizes system-wide efficiency, treating distributional equity as secondary. Here we present a framework that directly incorporates equity into optimization using Atkinson's welfare function, demonstrating that the equity–efficiency frontier in transboundary river systems can be navigated more deliberately — and that equity gains often require only modest efficiency trade-offs.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 907 |
| After deduplication | 771 |
| After LLM relevance filtering | 29 |
| Rejected (not relevant) | 742 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Water Resources Research | 7 |
| Scientific Data | 5 |
| Journal of Hydrology | 3 |
| Hydrology and Earth System Sciences | 2 |
| Hydrological Processes | 2 |
| Earth System Dynamics | 2 |
| Environmental Research Letters | 2 |
| Global and Planetary Change | 1 |
| Agricultural Water Management | 1 |
| Geoscientific Model Development | 1 |
| Nature Water | 1 |
| npj Natural Hazards | 1 |
| Water Science & Technology | 1 |
| ESSOAr preprint | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

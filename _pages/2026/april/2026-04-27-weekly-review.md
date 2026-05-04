---
layout: default
title: "Week 17 (Apr 20 - Apr 27), 33 papers"
parent: April
grand_parent: "2026"
nav_order: 33
date: 2026-04-27
categories: [weekly, 2026, april]
tags: [hydrology, literature-review, research]
paper_count: 33
highlight: "E3SM Version 3 spin-up documented; spectral analysis reveals hidden complexity in how reservoirs regulate flow variability."
lang: en
lang_link: /zh/2026/april/2026-04-27-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 17** · April 20–April 27, 2026
{: .text-grey-dk-000 }

**33** relevant papers found across **6** themes
{: .fs-5 .fw-300 }

## Executive Summary

A standout week for Earth system modeling, with the E3SM Version 3 coupled spin-up now documented and a new benchmark revealing systematic soil moisture biases across 16 CMIP6 models. Reservoir research surged with a GRL study using spectral analysis to uncover hidden complexity in flow regulation and several new optimization frameworks for multipurpose operations and hydropower flexibility under extremes.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Earth System Modeling and Land Surface Processes

This week saw significant contributions to Earth system and land surface modeling. Zhang et al. documented the full coupled spin-up procedure for E3SM Version 3 at standard resolution, providing the community with characteristic equilibration timescales across ocean, sea-ice, land, and atmosphere components. Massoud et al. benchmarked soil moisture across 16 CMIP6 ESMs and found substantial inter-model spread in surface and rootzone moisture representation, with implications for ecohydrologic coupling. Zhou et al. raised an important alarm about silent failures when using LLMs for ESM analysis, demonstrating through module-grounded benchmarking that plausible-looking outputs can mask scientifically incorrect results. On the land surface side, Wu et al. advanced parameter sensitivity analysis for groundwater dynamics in the Common Land Model, while Bechtold et al. released a global hourly climate forcing dataset critical for sub-daily impact assessments.

### Overview of Coupled Earth System Model spin-up for E3SM Version 3 at Standard Resolution

**Authors**: Shixuan Zhang, Luke Van Roekel, Carolyn Begeman, Wuyin Lin, Xue Zheng, Mathew Maltrud et al.

**Journal**: *ESSOAr* · **DOI**: [10.22541/essoar.15002235/v1](https://doi.org/10.22541/essoar.15002235/v1) · **Citations**: 0

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> Spinning up fully coupled Earth system models is essential for establishing stable and physically consistent initial conditions, yet it remains one of the most computationally demanding steps in the modeling workflow. Here we assess and document coupled spinup behavior and characteristic equilibration timescales in version 3 of the Energy Exascale Earth System Model (E3SMv3) at standard resolution, providing a reference for the broader modeling community.

---

### Can We Trust LLMs for Complex Earth System Model Analysis? Silent Failure and Evidence from Module-Grounded Benchmarking

**Authors**: Tian Zhou, Yun Qian, L. Ruby Leung

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2237](https://doi.org/10.5194/egusphere-2026-2237) · **Citations**: 0

**Matched topics**: hydrology, streamflow, land surface model, earth system model
{: .label .label-green }

> Large language models (LLMs) are becoming increasingly capable of complex scientific scripting, but this growing robustness creates a paradox: the more trustworthy their outputs appear, the more easily scientifically incorrect results can pass unnoticed. In Earth system model (ESM) analysis, such silent failures are more dangerous than visible crashes because they produce plausible figures and statistics that researchers may accept without verification.

---

### Benchmarking soil moisture and its relationship to ecohydrologic variables in Earth System Models

**Authors**: Elias Massoud, Nathan Collier, Yaoping Wang, Jiafu Mao, Adrian Harpold, Steven A Kannenberg et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-3427-2026](https://doi.org/10.5194/gmd-19-3427-2026) · **Citations**: 1

**Matched topics**: earth system model
{: .label .label-green }

> Soil moisture (SM) is a key regulator of ecosystem biogeophysics, influencing plant water relations and land-atmosphere energy exchanges. We evaluate the representation of SM in 16 Earth System Models from the Coupled Model Intercomparison Project Phase 6 (CMIP6) using the International Land Model Benchmarking (ILAMB) framework, focusing on surface (0–5, 0–10 cm) and rootzone (0–100 cm) depths across global biomes.

---

### Quantifying key parameter sensitivities for water table depth in hydrological schemes of CoLM-PSUADE

**Authors**: Tingting Wu, Shupeng Zhang, Xiaofan Yang, Yongjiu Dai

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2275](https://doi.org/10.5194/egusphere-2026-2275) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, land surface model, surface water
{: .label .label-green }

> Accurately representing groundwater dynamics in land surface models (LSMs) is crucial for understanding water-energy cycles and assessing water resources. However, most LSMs lack systematic sensitivity analyses of parameters regulating water table depth (WTD). This study couples the Common Land Model (CoLM) with Problem Solving environment for Uncertainty Analysis and Design Exploration (PSUADE) to identify and quantify the sensitivity of key parameters controlling WTD simulation.

---

### A global hourly ISIMIP3 climate forcing dataset for impact modeling

**Authors**: Michel Bechtold, Benjamin Poschlod, Christian Otto, Jan Volkholz, Matthias Büchner, Florian Zabel

**Journal**: *ESSD* · **DOI**: [10.5194/essd-2026-227](https://doi.org/10.5194/essd-2026-227) · **Citations**: 0

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> Sub-daily climate data are increasingly important for climate-impact assessments because many processes, such as heat stress, hydrological extremes, land–surface energy balance, and renewable-energy production, respond non-linearly to intra-day variability. Daily data miss short-duration events and obscure sub-daily inter-variable interactions, creating biases in impact estimates. To address this gap, a global hourly ISIMIP3 climate forcing dataset is presented.

---

### High-resolution land surface modeling of climate and CO2 effects on ecosystem carbon-water coupling across the Qinghai-Tibet Plateau

**Authors**: Xiazhen Xi, Xing Yuan, Yi Hao

**Journal**: *Agricultural and Forest Meteorology* · **DOI**: [10.1016/j.agrformet.2026.111195](https://doi.org/10.1016/j.agrformet.2026.111195) · **Citations**: 0

**Matched topics**: hydrologic model, land surface model, surface water
{: .label .label-green }

> Abstract not available.

---

### Dynamic Parameterization of Priestley-Taylor Coefficient for a More Accurate Potential Evapotranspiration Estimation in Ungauged Regions

**Authors**: Pushpendra Raghav, Mukesh Kumar

**Journal**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae6464](https://doi.org/10.1088/1748-9326/ae6464) · **Citations**: 0

**Matched topics**: hydrologic model, land surface model
{: .label .label-green }

> Potential evapotranspiration (PET), defined as the evapotranspirative flux from a region under fully saturated conditions, is a critical variable in hydrologic modeling, water stress assessment, and understanding ecosystem responses to climate. The widely used Priestley–Taylor method provides a simple, low-data requirement approach for estimating PET. However, it uses a fixed coefficient (α = 1.26), which may not capture regional or seasonal variability. This study proposes a dynamic parameterization framework for the Priestley-Taylor coefficient.

---

## Hydrologic Modeling Advances and Machine Learning

A methodologically rich week for hydrologic modeling. Ruzzante et al. in HESS demonstrated that high NSE scores can mask poor simulation of interannual variance in seasonal regimes — a cautionary finding for model evaluation practice. Deep learning continues to push boundaries: Heudorfer et al. tested whether better training data or improved architectures matter more for ungauged basin prediction, while Rosati and Lim revealed how LSTM memory states encode baseflow and snowmelt signatures in the Rio Hondo basin. Physics-informed approaches also advanced, with Mo et al. developing an interpretable hybrid ML framework for karst basin runoff, and Tashie et al. proposing a basin-aware global framework for computationally efficient surface water inundation prediction.

### Technical note: High Nash–Sutcliffe Efficiencies conceal poor simulations of interannual variance in seasonal regimes

**Authors**: Sacha Ruzzante, Wouter Knoben, Thorsten Wagener, Tom Gleeson, Markus Schnorbus

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2337-2026](https://doi.org/10.5194/hess-30-2337-2026) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow, seasonal
{: .label .label-green }

> In highly seasonal regimes hydrologic models generally achieve high scores on common performance metrics such as the Nash–Sutcliffe Efficiency (NSE) and the Kling–Gupta Efficiency (KGE). However, variance in streamflow time series is composed of seasonal, interannual, and irregular variance, and the NSE and KGE do not differentiate between these components. Differences in performance on these variance components are investigated across multiple model structures and catchments.

---

### Better data or better architecture? Improving deep-learning-based prediction in ungauged basins

**Authors**: Benedikt Heudorfer, Hoshin Gupta, Alexander Dölich, Ralf Loritz

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1965](https://doi.org/10.5194/egusphere-2026-1965) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> Large-sample hydrology has recently been driven by two key developments. First, the introduction of hydrological benchmark datasets such as CAMELS-US and CARAVAN, and second, the emergence of deep-learning modelling frameworks, particularly LSTM-based regional models. This study investigates whether better training data or improved model architectures contribute more to prediction skill in ungauged basins.

---

### Climate change-driven runoff variations in alpine catchments: Quantitative attribution using three innovative methods coupled with cryospheric processes

**Authors**: Zhenliang Yin, Chunshuang Fang, Jianan Shan, Zexia Chen, Rui Zhu, Qi Feng

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135566](https://doi.org/10.1016/j.jhydrol.2026.135566) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow, land surface model
{: .label .label-green }

> Abstract not available.

---

### Interpretable residual-informed hybrid physics-informed machine learning framework for runoff prediction in a typical karst basin in southwest China

**Authors**: Chongxun Mo, Changhao Jiang, Jiameng Xu, Yi Huang, Gang Tang, Lingling Tang et al.

**Journal**: *Environmental Modelling & Software* · **DOI**: [10.1016/j.envsoft.2026.106986](https://doi.org/10.1016/j.envsoft.2026.106986) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, hydropower
{: .label .label-green }

> Abstract not available.

---

### Revealing Baseflow and Hydrologic Process Signatures in LSTM Memory: Insights from the Rio Hondo, New Mexico

**Authors**: Michael A. Rosati, Yeo H. Lim

**Journal**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.019](https://doi.org/10.1061/9780784486931.019) · **Citations**: 0

**Matched topics**: hydrologic model, surface water
{: .label .label-green }

> This study investigates how a Long Short-Term Memory (LSTM) model internally encodes hydrologic behavior relevant to baseflow dynamics in a snowmelt-driven, semi-arid mountain basin. Focusing on the Rio Hondo in the Sangre de Cristo Mountains of northern New Mexico, daily flow performance was evaluated, and LSTM memory-state activations were compared with hydrologic variables generated by a two-reservoir conceptual model.

---

### A Basin-Aware Global Framework for Computationally Efficient Surface Water Inundation Prediction

**Authors**: Arik M. Tashie, Isaac D. Gerg, Evan Koester, Carlos D. Hoyos, Eduardo Galindo, David Farnham

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1527](https://doi.org/10.5194/egusphere-2026-1527) · **Citations**: 0

**Matched topics**: streamflow, surface water
{: .label .label-green }

> Predicting surface water inundation at regional to global scales presents a fundamental tension: bespoke local models achieve high accuracy but require proprietary data and are difficult to scale, while globally trained systems offer broad coverage but demand substantial computational infrastructure. This study presents a Basin-Aware Global Inundation framework that balances coverage and computational efficiency.

---

## Streamflow Forecasting and Analysis

Streamflow projection and forecasting were active themes. Sauquet et al. published the most-cited paper of the week (10 citations) describing a large transient multi-scenario ensemble of future streamflow and groundwater projections for France, providing rich spatially consistent information for water resource planning. In the western US, Özcan and Kavvas compared physically based and data-driven approaches for seasonal forecasting in California's Upper Feather River Basin, while Cabezas-Nivin et al. addressed non-stationarity challenges in the Upper Rio Grande. Foley et al. reconstructed over 400 years of streamflow in Alabama's Black Warrior River, revealing dual atmospheric controls on flow extremes.

### A large transient multi-scenario multi-model ensemble of future streamflow and groundwater projections in France

**Authors**: E. Sauquet, G. Évin, Sonia Siauve, Rym Aissat, Patrick Arnaud, Maud Bérel et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2277-2026](https://doi.org/10.5194/hess-30-2277-2026) · **Citations**: 10

**Matched topics**: streamflow
{: .label .label-green }

> A large transient multi-scenario and multi-model ensemble of future streamflow and groundwater projections in France developed in a national project named Explore2 was recently made available. The main objective of Explore2 is to provide rich and spatially-consistent information for the future evolution of hydrological (surface and groundwater) resources and extremes in France to support adaptation policies.

---

### Comparing Physically Based and Data-Driven Approaches for Seasonal Streamflow Forecasting in California's Upper Feather River Basin

**Authors**: Z. Özcan, M. L. Kavvas

**Journal**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.002](https://doi.org/10.1061/9780784486931.002) · **Citations**: 0

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> Seasonal streamflow forecasts are essential for reservoir operations, flood management, and irrigation planning, particularly in snow-dominated basins where climate-driven extremes challenge stationarity-based methods. This study evaluates two complementary forecasting paradigms in the Upper Feather River Basin (UFRB), a critical source for California's State Water Project upstream of Oroville Dam.

---

### Ensemble streamflow forecasting with diverse loss functions

**Authors**: Kshitij Dahal, Atharva Gupta, Laxman Bokati, Saurav Kumar

**Journal**: *Applied Soft Computing* · **DOI**: [10.1016/j.asoc.2026.115276](https://doi.org/10.1016/j.asoc.2026.115276) · **Citations**: 0

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> Abstract not available.

---

### Non-Stationary Streamflow Analysis under Climate Change in the Upper Rio Grande Basin

**Authors**: Oscar M Cabezas-Nivin, Eusebio Ingol-Blanco, Alessandro Apolinario

**Journal**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.080](https://doi.org/10.1061/9780784486931.080) · **Citations**: 0

**Matched topics**: streamflow, climate change
{: .label .label-green }

> Climate change is fundamentally eroding the principles of water resource planning in the American Southwest, particularly within the snow-driven Upper Rio Grande Basin. Conventional infrastructure design depends on stationarity, assuming past hydrological patterns will persist, a premise that is increasingly untenable. A comprehensive non-stationary framework is developed to address this challenge.

---

### Dual Atmospheric Controls Amplify Streamflow Extremes in Alabama

**Authors**: Zachary W. Foley, G. Harley, R. Thaxton, M. Therrell, Charles Jones, Meng Zhao et al.

**Journal**: *Environmental Research Communications* · **DOI**: [10.1088/2515-7620/ae6399](https://doi.org/10.1088/2515-7620/ae6399) · **Citations**: 0

**Matched topics**: streamflow
{: .label .label-green }

> The Southeastern United States (US) has experienced increased population growth and urbanization in recent decades, highlighting the importance of water management and availability. The Black Warrior River basin is in an area with an increasing precipitation trend and no previous streamflow reconstruction. Over 400 years (1550-2023 CE) of May-July streamflow were reconstructed, revealing dual atmospheric controls on flow extremes.

---

## Reservoir Operations and Hydropower

Reservoir research saw a surge of activity. Zhang et al. in GRL applied spectral analysis to 205 US reservoirs, decomposing regulation effects into operational modes and revealing that reservoirs selectively modify flow variability at different timescales — complexity previously hidden by time-domain methods alone. On the optimization front, Chen et al. developed a multi-objective reservoir refill model balancing flood risk, storage, and hydropower at Longtan Reservoir, while Khandaker et al. used dynamic programming for multipurpose operations at Lewisville Lake. Son et al. provided the first systematic quantification of hydropower flexibility during extreme temperature events across 25 years of data. Dell'Aira and Cancelliere explored SEAS5 seasonal forecasts for adaptive operations, and Huang et al. addressed the emerging challenge of drought-flood abrupt alternation for reservoir management.

### Hidden Complexity in Reservoir Flow Regulation Revealed by Spectral Analysis

**Authors**: Fenghe Zhang, Peirong Lin, Tongbi Tu

**Journal**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl121654](https://doi.org/10.1029/2026gl121654) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, reservoir
{: .label .label-green }

> Understanding reservoir regulation of streamflow is critical for hydrological modeling and ecohydrological assessments, yet our knowledge of how reservoirs preferentially modify flow variability remains limited. Here we apply spectral analysis to daily inflow-outflow data from 205 US reservoirs, decomposing regulation effects into operational mode (how reservoirs modify flow variability) and operational intensity (how strongly they do so) across timescales.

---

### Quantifying hydropower flexibility during extreme temperature events

**Authors**: Kyongho Son, Cameron Bracken, Erfaneh Sharifi, Sohom Datta, Abhishek Somani

**Journal**: *ESSOAr* · **DOI**: [10.31223/x5bf4h](https://doi.org/10.31223/x5bf4h) · **Citations**: 0

**Matched topics**: streamflow, hydropower
{: .label .label-green }

> Extreme weather events can impose substantial stress on the electrical grid. Hydropower offers unique operational flexibility, enhancing grid resilience and reliability. Despite this value of flexibility, systematic assessments of hydropower flexibility — particularly during extreme events — remain limited. This study is the first to quantify hydropower operational flexibility using 25 years' observational data.

---

### Developing an Optimization Model for Multipurpose Reservoir Operations at Lewisville Lake

**Authors**: Nabila Khandaker, Mohammad Moradi, Afiya Narzis, Qazi Ashique Mowla

**Journal**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.023](https://doi.org/10.1061/9780784486931.023) · **Citations**: 0

**Matched topics**: hydrologic model, reservoir, hydropower
{: .label .label-green }

> This study develops an optimization model to evaluate improved operating strategies for Lewisville Lake (Garza–Little Elm Reservoir) in Denton County, Texas. The reservoir, completed in 1954, serves multiple purposes, including flood control, municipal and industrial water supply, recreation, and small-scale hydropower generation. A discrete dynamic programming approach is implemented to balance competing objectives.

---

### Multi-objective optimization of reservoir refill operate considering energy storage and hydrological conditions

**Authors**: Lihua Chen, Kaipeng Yang, Yunyao Chen, Xi Zhang, Xuefang Li

**Journal**: *River* · **DOI**: [10.1002/rvr2.70050](https://doi.org/10.1002/rvr2.70050) · **Citations**: 0

**Matched topics**: hydrologic model, reservoir, hydropower
{: .label .label-green }

> Optimizing reservoir refill operation rules is crucial for enhancing reservoir sustainability and resilience. This study proposes a refill operation model designed to derive optimal refill guide curves by considering flood risk prevention, maximum storage levels, and the combined benefits of hydropower generation and energy storage. The proposed model was applied to the Longtan Reservoir.

---

### Assessing water resources service value through simulation of a water supply–hydropower generation–ecosystem photosynthesis nexus system

**Authors**: Yue Feng, Dedi Liu, Hanxu Liang, 张嘉裕 Zhang Jiayu

**Journal**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2026.110365](https://doi.org/10.1016/j.agwat.2026.110365) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, hydropower
{: .label .label-green }

> Water resources generate service values through water supply (S), hydropower generation (H), and ecosystem photosynthesis (E), forming a SHE nexus system that supports sustainable water resource management under the impacts of both climate change and human activities. However, these service values are often assessed in isolation, overlooking the complex interactions within the SHE nexus system.

---

### How Increasingly Frequent Drought-Flood Abrupt Alternation Events Affect Reservoir Operation?

**Authors**: Y Huang, Jianyu Fu, Xuejin Tan, Zhihong Deng, Haibo Peng, Wenzhi Zhang et al.

**Journal**: *Water Resources Management* · **DOI**: [10.1007/s11269-026-04634-y](https://doi.org/10.1007/s11269-026-04634-y) · **Citations**: 0

**Matched topics**: reservoir, flood, drought
{: .label .label-green }

> Abstract not available.

---

### Use of SEAS5 Seasonal Forecast Products for Adaptive Reservoir Operations

**Authors**: Francesco Dell'Aira, Antonino Cancelliere

**Journal**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.038](https://doi.org/10.1061/9780784486931.038) · **Citations**: 0

**Matched topics**: reservoir, seasonal
{: .label .label-green }

> Reservoir operations play a critical role in securing water availability and reliability, particularly in drought-prone regions. Traditionally, water supply reservoirs have been managed using historical climate data and short-term weather forecasts. However, these conventional approaches often lack the predictive power required to implement proactive measures — such as hedging release strategies — to mitigate water shortage risks. This study explores the use of SEAS5 seasonal forecast products for adaptive reservoir management.

---

## Flood and Drought Research

Flood and drought studies spanned diverse geographies and methods. Emamjomehzadeh and Wani in Communications Earth & Environment developed a scalable flood-risk framework evaluating 2300 culvert-served catchments across New York State, revealing patterns of dependence in infrastructure vulnerability. Kuntla and Saharia provided the first comprehensive spatiotemporal assessment of observed riverine flood severity across India. On the drought side, Ogunrinde et al. found emergent reorganization and increased persistence of meteorological drought across Africa using both observations and CMIP6 ensembles. Gupta and Arrighi proposed a novel conceptual framework linking flood drivers to damage for inland hydrological assets, while Jamal et al. advanced dynamic flood routing methods for dendritic channel networks.

### Scalable flood-risk analysis for New York State culvert infrastructure reveals patterns of dependence

**Authors**: Omid Emamjomehzadeh, Omar Wani

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03550-8](https://doi.org/10.1038/s43247-026-03550-8) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> Floodwater flowing over roads can disrupt traffic, threaten public safety, and compromise structural stability. Culverts — structures that convey water beneath roads — are critical for flood mitigation, yet statewide rehabilitation would cost billions of dollars. We evaluated reliability by quantifying the probability of hydraulic capacity exceedance of large culverts serving 2300 catchments across New York State, revealing patterns of dependence in flood risk.

---

### Observed Riverine Flood Severity in India

**Authors**: Sai Kiran Kuntla, Manabendra Saharia

**Journal**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0213.1](https://doi.org/10.1175/jhm-d-25-0213.1) · **Citations**: 0

**Matched topics**: streamflow, flood
{: .label .label-green }

> Floods in India are frequent and destructive, causing significant economic damage and loss of human lives every year. The severity and impact of these floods vary based on catchment geomorphology, climatology, local exposure, vulnerability, and existing flood management practices. Yet, a comprehensive spatiotemporal assessment of observed flood severity across India has been lacking. A holistic analysis is presented to fill this gap.

---

### Emergent reorganization and increased persistence of meteorological drought across Africa

**Authors**: Akinwale T. Ogunrinde, Paul Adigun, Koji Diaraku, Xian Xue, Ebiendele Precious, Ermias Sisay Brhane

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03528-6](https://doi.org/10.1038/s43247-026-03528-6) · **Citations**: 0

**Matched topics**: streamflow, drought
{: .label .label-green }

> African droughts are becoming more frequent and severe, but whether their underlying behavior is also changing remains unclear. Here, we combine observational climate data from the Climatic Research Unit with a 16-member climate model ensemble from the Coupled Model Intercomparison Project Phase 6 to examine drought dynamics across four African regions. Using drought-event characteristics, persistence metrics, and transition probabilities, an emergent reorganization is found.

---

### From drivers to damage: A conceptual framework for integrated flood risk assessment of inland hydrological assets

**Authors**: Kunal Gupta, Chiara Arrighi

**Journal**: *The Science of The Total Environment* · **DOI**: [10.1016/j.scitotenv.2026.181813](https://doi.org/10.1016/j.scitotenv.2026.181813) · **Citations**: 0

**Matched topics**: streamflow, flood
{: .label .label-green }

> Flood risk in inland hydrological systems stems from dynamic interactions among drivers, exposure pathways, and vulnerabilities. Yet, prevailing assessment methods treat these dimensions in isolation, failing to capture cascading and compound effects. This study develops a novel conceptual framework for integrated flood risk assessment that establishes systematic linkages from drivers to damage across inland hydrological assets.

---

### Performance Analysis of Iteration-Based Dynamic Flood Routing Model for Dendritic Channel Networks

**Authors**: Jani Fathima Jamal, Erfan Goharian, Jasim Imran, M. Hanif Chaudhry

**Journal**: *Journal of Hydraulic Engineering* · **DOI**: [10.1061/jhend8.hyeng-14381](https://doi.org/10.1061/jhend8.hyeng-14381) · **Citations**: 0

**Matched topics**: hydrologic model, flood
{: .label .label-green }

> An effective flood forecasting system requires dynamic routing to accurately predict floods under diverse conditions, from slow- to fast-rising events. However, for operational forecasting, dynamic routing is computationally demanding, especially for large channel networks, necessitating efficient solution methods. This study analyzes the performance of an iteration-based dynamic flood routing model for dendritic channel networks.

---

## Climate Change Impacts on Water Resources

Climate change impacts on water resources were explored across contrasting environments. Shafeeque et al. investigated the interplay between dynamic debris cover variations and glacier melt in the Karakoram region of High Mountain Asia, quantifying implications for downstream freshwater availability under projected climate scenarios. Hermosillo et al. examined how warming alters freeze-thaw dynamics and subsurface water-heat fluxes in cold regions, with implications for infiltration and aquifer recharge. Huang et al. assessed enhanced representation of hydrological processes in urban climate models across multiple cities globally, highlighting the importance of coupling urban hydrology with climate projections.

### Investigating Effects of Dynamic Debris Cover Variations on Glacio-Hydrology under Projected Climate Change in High Mountain Asia

**Authors**: Muhammad Shafeeque, Arfan Arshad, Amna Bibi, Tahira Khurshid, Abid Sarwar, T. Tran et al.

**Journal**: *Earth Systems and Environment* · **DOI**: [10.1007/s41748-026-01125-3](https://doi.org/10.1007/s41748-026-01125-3) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model
{: .label .label-green }

> Debris cover on glaciers in High Mountain Asia (HMA) plays a critical role in shaping glacier evolution and downstream freshwater availability. In Karakoram, glacier melt significantly influences river discharge, yet the interplay of climate change and supraglacial debris cover remains insufficiently quantified. A dynamic debris cover framework was developed using the Spatial Processes in Hydrology model to assess these interactions.

---

### Effects of Climate Change on Water and Heat Fluxes in the Shallow Subsurface in Cold Regions

**Authors**: Joaquin Sainz Hermosillo, R. M. Neupauer, Jarkko Okkonen

**Journal**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.017](https://doi.org/10.1061/9780784486931.017) · **Citations**: 0

**Matched topics**: land surface model, surface water
{: .label .label-green }

> Freezing and thawing of water in the shallow subsurface in cold regions plays a significant role in the exchange of water between the land surface (e.g., precipitation, infiltration) and the subsurface (e.g., aquifer recharge). A warming climate will lead to changes in the timing and duration of freezing events, which will impact near-surface water and heat fluxes.

---

### Enhanced representation of hydrological processes in urban climate modeling: A multi-city global assessment

**Authors**: Yuqi Huang, Chenghao Wang, Zhi-Hua Wang

**Journal**: *Urban Climate* · **DOI**: [10.1016/j.uclim.2026.102908](https://doi.org/10.1016/j.uclim.2026.102908) · **Citations**: 0

**Matched topics**: hydrologic model, runoff
{: .label .label-green }

> Abstract not available.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 1350 |
| After deduplication | 1106 |
| After blocklist filtering | 1040 |
| After LLM relevance filtering | 33 |
| Rejected (not relevant) | 1007 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| EGUsphere / ESSOAr | 5 |
| ASCE Proceedings | 5 |
| Geophysical Research Letters | 1 |
| Hydrology and Earth System Sciences | 2 |
| Communications Earth & Environment | 2 |
| Geoscientific Model Development | 1 |
| Journal of Hydrology | 1 |
| Environmental Research Letters | 1 |
| Environmental Modelling & Software | 1 |
| Agricultural and Forest Meteorology | 1 |
| Applied Soft Computing | 1 |
| Environmental Research Communications | 1 |
| Journal of Hydrometeorology | 1 |
| The Science of The Total Environment | 1 |
| Journal of Hydraulic Engineering | 1 |
| Water Resources Management | 2 |
| Agricultural Water Management | 1 |
| River | 1 |
| Earth Systems and Environment | 1 |
| Urban Climate | 1 |
| Nature Communications (not selected — atmospheric rivers) | 0 |
| ESSD | 1 |
| ACS ES&T Water (not selected) | 0 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

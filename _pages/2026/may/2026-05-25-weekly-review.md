---
layout: default
title: "Week 20 (May 11 - May 18), 27 papers"
parent: May
grand_parent: "2026"
nav_order: 35
date: 2026-05-25
categories: [weekly, 2026, may]
tags: [hydrology, literature-review, research]
paper_count: 27
highlight: "New river routing model C-CWatM enables direct ESM/LSM coupling for consistent human-water-climate assessments; Science documents accelerated Himalayan river dynamics under warming."
lang: en
lang_link: /zh/2026/may/2026-05-25-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 20** · May 11–May 18, 2026
{: .text-grey-dk-000 }

**27** relevant papers found across **5** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week saw major advances in coupling water resources modeling with Earth system models, highlighted by C-CWatM v1.0 which enables high-resolution river routing and human water management within ESMs. Climate change impacts on rivers dominated the literature, with a landmark Science paper documenting accelerated Himalayan river meandering and Nature Communications revealing limited meltwater capacity to offset downstream urban water scarcity. Machine learning for hydrology continued its surge, with physics-informed neural operators and semi-supervised approaches addressing the persistent challenge of prediction in data-scarce basins.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Large-Scale Hydrologic and Earth System Modeling

A major development this week is C-CWatM v1.0, a new river routing and water resources model designed for direct coupling with Earth system and land surface models, addressing the longstanding disconnect between climate modeling and human water management. Complementing this, research on hydrologic whiplash in the Mississippi basin (O'Donnell et al.) leveraged ESM projections to reveal mechanisms behind rapid wet-dry transitions, while Green et al. demonstrated in Nature Communications that vegetation responses to atmospheric dryness create a positive feedback loop amplifying land surface warming — a critical finding for land surface model development. At finer scales, new work on soil crack dynamics (Sun et al. in GRL) provides mechanistic understanding of preferential flow that can improve infiltration parameterizations, and causal analyses by Indrawati et al. reveal shifting soil moisture controls under warming that challenge current land-atmosphere coupling assumptions.

### C-CWatM v1.0: A high-resolution water resources and river routing model enabling direct linkage to state-of-the-art Earth-system and land‑surface models

**Authors**: Peter Greve, Amelie U. Schmitt, Sina Jasmin Schreiber, Augustin Clédat, Peter Burek

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2366](https://doi.org/10.5194/egusphere-2026-2366) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow, water management, land surface model, earth system model
{: .label .label-green }

> Abstract. River routing and human water management are often poorly represented in many Earth-system and land-surface models, not permitting consistent assessments of human-water-climate interactions. In this work, we introduce C-CWatM v1.0 (Climate-CWatM v1.0), a land-surface-driven version of the Community Water Model (CWatM) that enables a direct linkage to state-of-the-art Earth-system and land-surface models. C-CWatM v1.0 provides high-resolution river routing and human water management capabilities, including reservoir operations, irrigation, and water demand allocation. We present the model architecture, coupling interface, and demonstrate its performance in reproducing observed streamflow and reservoir storage across global basins.

---

### Hydrologic Whiplash in the Mississippi River Basin: Mechanisms and Projections

**Authors**: Michelle O'Donnell, S. G. Dee, J. Doss-Gollin, Samuel E. Munoz

**Journal**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl122807](https://doi.org/10.1029/2026gl122807) · **Citations**: 0

**Matched topics**: hydrologic model, river, streamflow, earth system model
{: .label .label-green }

(Also featured in daily harvest on 2026-05-12)

> Volatility and unpredictability of hydroclimate systems stresses planning and risk management. Notably, the rapid transition between periods of high and low streamflow, known as hydrologic whiplash, is gaining attention worldwide. Yet the specific mechanisms driving hydrologic whiplash events, and how they may change in the future, remain poorly understood. Here we analyze observed and projected streamflow across the Mississippi River Basin to characterize the drivers and future trajectory of hydrologic whiplash.

---

### Vegetation responses to air dryness amplify future land surface warming

**Authors**: Julia K. Green, Trevor F. Keenan, Xu Lian, David J. P. Moore, Philippe Ciais

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-026-73063-7](https://doi.org/10.1038/s41467-026-73063-7) · **Citations**: 0

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> Temperature exerts a first-order control on vegetation photosynthesis and transpiration. Yet most studies investigating temperature impacts on plants rely on near-surface air temperature, rather than canopy temperature-the temperature plants actually experience. Because canopy temperature directly influences stomatal conductance and transpiration, changes in vegetation function feed back to the land surface energy balance. Here we show that vegetation responses to increasing atmospheric dryness reduce transpiration and amplify land surface warming, creating a positive feedback loop that is underrepresented in current Earth system models.

---

### Causal analyses reveal changing land-atmosphere patterns and soil moisture control under warming

**Authors**: Dian Indrawati, Somnath Mondal, Poulomi Ganguli, Auroop Ganguly

**Journal**: *ESSOAr* · **DOI**: [10.31223/x53b62](https://doi.org/10.31223/x53b62) · **Citations**: 0

**Matched topics**: runoff, earth system model
{: .label .label-green }

> Climate change is projected to modify the global water cycle and land-atmosphere interactions. However, warming-induced changes in multivariate dependence remain insufficiently explored. Here we examine the interdependence among temperature, precipitable water, precipitation, evaporation, soil moisture, and runoff using causal discovery methods applied to reanalysis data and CMIP6 projections. Results reveal that soil moisture exerts an increasingly dominant control on land-atmosphere coupling under warming scenarios.

---

### Soil Crack Width Controls Preferential Flow Velocity Through Drag Partitioning

**Authors**: Chang Sun, Chao‐Sheng Tang, Farshid Vahedifard, Ao Dong, Zhan‐Ming Yang, Bin Shi

**Journal**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl122866](https://doi.org/10.1029/2026gl122866) · **Citations**: 0

**Matched topics**: hydrologic model, land surface model
{: .label .label-green }

> Abstract Preferential flow within soil cracks influences land surface hydrological processes, yet directly quantifying preferential flow velocity (PFV) remains challenging. Here, we develop a method for high‐resolution monitoring and quantifying PFV in soil cracks using optical frequency domain reflectometry. Results demonstrate that crack width exerts primary control on PFV through a drag partitioning mechanism, providing a physically based parameterization for preferential flow in land surface models.

---

## Climate Change Impacts on Rivers and Water Resources

Climate-driven changes to river systems were a dominant theme this week. A landmark Science paper by Lin et al. documented accelerated Himalayan river meandering rates tied to climate warming, while Li et al. in Nature Communications showed that meltwater from the Asian Water Tower has limited potential to offset downstream urban water scarcity — a sobering finding for adaptation planning. Glacier-fed basins are becoming increasingly flood-prone, as Liu et al. demonstrated with projections of more unpredictable flooding in the Third Pole's most glacierized basin. At high latitudes, deep learning projections for Arctic rivers suggest 6–15% streamflow increases by end-of-century, with permafrost degradation shifting the dominant climatic drivers. In western North America, drying summers are threatening river ecosystems and keystone salmon populations, and global analyses reveal systematic shifts in flood seasonality driven by changing precipitation and snowmelt timing.

### Accelerated Himalayan river meandering and dynamics due to climate change

**Authors**: Zhipeng Lin, Zhongpeng Han, David R. Montgomery, Waqas Ul Hussan, Lars Lønsmann Iversen, Mette Bendixen et al.

**Journal**: *Science* · **DOI**: [10.1126/science.adg8401](https://doi.org/10.1126/science.adg8401) · **Citations**: 1

**Matched topics**: river, climate change
{: .label .label-green }

(Also featured in daily harvest on 2026-05-14)

> River meandering and migration are fundamental processes worldwide, and the high Himalayas offer an opportunity to test whether river morphodynamics are shifting in response to a rapidly changing climate. We used remote-sensing imagery and field observations to quantify river meandering and associated dynamics across major Himalayan rivers over multiple decades. Results reveal statistically significant acceleration in river meandering rates linked to increased glacial melt and intensified monsoon precipitation under warming.

---

### Limited meltwater potential in the Asian Water Tower to mitigate downstream urban scarcity

**Authors**: Lei Li, Chunyang He, Tao Qi, Kaiyu Zhao, Arthur Lutz, Bruno Merz

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-026-73245-3](https://doi.org/10.1038/s41467-026-73245-3) · **Citations**: 0

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> The Asian Water Tower, a vital freshwater source for billions downstream, is rapidly transforming under climate change. Accelerated glacier and snowmelt are reshaping meltwater patterns, threatening urban water security amid rapid population growth. Using a high-resolution cryosphere–hydrology model coupled with urban water demand projections, we show that even under optimistic melt scenarios, meltwater contributions are insufficient to offset growing urban water scarcity in downstream cities. The mismatch between meltwater timing and urban demand peaks further limits adaptation options.

---

### More unpredictable river floods at the most glacierized Third Pole basin

**Authors**: Hu Liu, Lei Wang, Deliang Chen, Tandong Yao, Ahmad Bashir

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03623-8](https://doi.org/10.1038/s43247-026-03623-8) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, river, flood
{: .label .label-green }

> Extreme flooding poses threats to earth-and-rock dams and downstream communities, especially in glacierized basins with unclear flood predictability. Here, combining a high-resolution cryosphere-hydrological model with observations, we project a significant increase in flood frequency and intensity in the Hunza basin — the most glacierized basin of the Third Pole. Flood events become more unpredictable as glacier melt contributions shift seasonal runoff patterns, challenging existing dam safety and early warning systems.

---

### Projected hydrological responses to climate change in a high-mountain river basin based on RCM simulations

**Authors**: Adnan Khan, Fiza Gul, Muhammad Fahad Ullah, Hassan Ayaz, Mahmood Ahmad, Feezan Ahmad et al.

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-52852-6](https://doi.org/10.1038/s41598-026-52852-6) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, river, runoff, streamflow, climate change
{: .label .label-green }

> This study assesses future hydrological responses of the Chitral River Basin (CRB), a high-mountain, glacier-fed catchment in northern Pakistan, under climate change. The Soil and Water Assessment Tool (SWAT) was forced with bias-corrected outputs from three CORDEX regional climate models under Representative Concentration Pathways. Results show substantial shifts in seasonal runoff patterns, with earlier spring peaks and reduced summer flows projected under high-emission scenarios, with significant implications for downstream water availability and flood risk management.

---

### Projected changes in Arctic river streamflow and shifting climatic drivers: A linear ensemble deep learning approach

**Authors**: Shiqi Liu, Renjie Zhou, Ping Wang, Jingjie Yu, Vahid Nourani

**Journal**: *Geoscience Frontiers* · **DOI**: [10.1016/j.gsf.2026.102350](https://doi.org/10.1016/j.gsf.2026.102350) · **Citations**: 0

**Matched topics**: hydrology, river, streamflow, earth system model
{: .label .label-green }

> A linear ensemble deep learning approach was proposed for Arctic river streamflow prediction. Streamflow in six Arctic basins is projected to increase by 6.1%–15.3% by 2080–2100. Arctic river streamflow is more sensitive to warming during the early stage of permafrost degradation. Winter streamflow increases are driven by enhanced subsurface flow as permafrost thaws, while summer peaks shift earlier. The approach combines multiple CMIP6 ESM outputs with observed discharge to produce robust ensemble projections.

---

### Drying summers threaten western North American river ecosystems and a keystone migratory fish

**Authors**: Sacha W. Ruzzante, Tom Gleeson, Jonathan W. Moore, Marta Ulaski, Todd Hatfield, Markus Schnorbus et al.

**Journal**: *ESSOAr* · **DOI**: [10.31223/x5sv1j](https://doi.org/10.31223/x5sv1j) · **Citations**: 0

**Matched topics**: river, streamflow
{: .label .label-green }

> Climate change threatens river ecosystems by altering the seasonal streamflow patterns to which aquatic species have adapted, including keystone species like Chinook salmon in western North America. Chinook salmon display diverse life-history adaptations to local hydrologic regimes, contributing to the resilience of the species as a whole. We project future summer streamflow declines across western North American rivers and show that drying summers pose a systematic threat to salmon-bearing rivers.

---

### Shifts in global flood seasonality and their drivers

**Authors**: Sixiang Wang, Yansong Guan, Xihui Gu, Shuangyu Wang

**Journal**: *Hydrological Sciences Journal* · **DOI**: [10.1080/02626667.2026.2661882](https://doi.org/10.1080/02626667.2026.2661882) · **Citations**: 0

**Matched topics**: flood, seasonal
{: .label .label-green }

> Abstract not available.

---

## Reservoir Operations and Water Management

Global-scale reservoir analysis revealed that irrigation reservoirs face disproportionately high risk of water shortages, with Shah et al. in Communications Earth & Environment identifying climate variability and growing demand as dual drivers of reservoir-based drought. Okiria et al. presented a systematic satellite-based validation of reservoir storage simulations in global hydrological models — a critical step given how poorly current GHMs represent managed water systems. In China, a policy evaluation of groundwater-to-surface-water substitution for irrigation in Hebei highlights both the effectiveness and limitations of supply-side adaptation to aquifer depletion.

### Global irrigation reservoirs are at a higher risk of water shortages

**Authors**: Deep Shah, Vimal Mishra, Huilin Gao

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03571-3](https://doi.org/10.1038/s43247-026-03571-3) · **Citations**: 0

**Matched topics**: streamflow, reservoir, irrigation
{: .label .label-green }

> Water shortages induced by Reservoir-Based Droughts (RBD) pose a significant threat to global food, water, and energy security. However, a global-scale assessment of RBD, identification of reservoirs at higher risk of water shortages, and the dominant drivers (climate vs. human) remain underexplored. We analyze over 7,000 reservoirs globally and find that irrigation reservoirs face systematically higher drought risk than hydropower or flood-control reservoirs, with climate variability and demand growth acting as compounding drivers.

---

### Using satellite observations to validate and improve reservoir storage simulations in global hydrological models

**Authors**: Emmanuel Okiria, Naota Hanasaki, Simon N. Gosling, Emmanuel Nyenah, Peter Burek, Yusuke Satoh et al.

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2043](https://doi.org/10.5194/egusphere-2026-2043) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, reservoir
{: .label .label-green }

> Abstract. Global hydrological models (GHMs) increasingly incorporate generic reservoir operation schemes (GROS) to simulate the regulation of rivers by dams. However, the reliability of GROS remains largely unvalidated on a global scale due to the historical scarcity of open in situ data. Here, we leverage satellite-derived reservoir storage estimates to systematically evaluate and improve reservoir simulations across multiple GHMs. Results reveal substantial biases in current GROS implementations, particularly for irrigation-dominated reservoirs, and demonstrate how satellite observations can constrain model parameters.

---

### Substituting Groundwater With Surface Water for Irrigation in Northern China: Current Status, Effectiveness and Challenges

**Authors**: Tianhe Sun, Baozhu Guan, Baozhu Guan, Huang Chen, Yì Wáng, Wei Chao et al.

**Journal**: *Australian Journal of Agricultural and Resource Economics* · **DOI**: [10.1111/1467-8489.70108](https://doi.org/10.1111/1467-8489.70108) · **Citations**: 0

**Matched topics**: surface water, irrigation
{: .label .label-green }

> ABSTRACT China's irrigated heartlands face concurrent pressures of aquifer depletion and grain security. We evaluate Hebei's Substituting Groundwater with Surface Water for Irrigation (SGSWI) project — a medium‐scale, short‐haul program — using county‐level panel data and a staggered difference‐in‐differences framework. Results show that the program has been effective in reducing groundwater extraction but faces sustainability challenges related to surface water availability during drought years and infrastructure maintenance costs.

---

## Machine Learning for Hydrologic Prediction

The application of machine learning to hydrologic prediction continued to accelerate, with a notable shift toward physics-informed and uncertainty-aware approaches. Behroozi et al. (from the Shen group) introduced a physically anchored multi-resolution neural operator for flood inundation that maintains physical consistency while achieving computational speedups over hydrodynamic models. Several papers addressed the critical challenge of data scarcity: Jia et al. proposed semi-supervised deep learning that leverages unlabeled meteorological data, while Zhang et al. developed a prompt-guided differentiable physics model. Peng et al. tackled the underexplored problem of jointly quantifying data and model uncertainty in deep learning streamflow predictions. At the watershed scale, Manoli et al. showed that deep learning error post-processing can substantially improve stochastic watershed model outputs, and data-driven SWE estimation studies demonstrated competitive performance against operational SNOW-17 in the Sierra Nevada.

### Physically Anchored Multi-Resolution Neural Operator Framework for Flood Inundation Prediction

**Authors**: Abdolmehdi Behroozi, Kathryn Lawson, Chaopeng Shen

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1982](https://doi.org/10.5194/egusphere-2026-1982) · **Citations**: 0

**Matched topics**: hydrology, streamflow, flood
{: .label .label-green }

> Abstract. Accurate flood inundation modeling using high-resolution hydrodynamic simulations is computationally demanding, limiting their use for large-scale analysis and rapid scenario evaluation. Although machine learning surrogates have been developed, many struggle to reproduce the full spatiotemporal evolution of flood inundation with physical consistency. We present a physically anchored multi-resolution neural operator framework that preserves mass conservation and topographic constraints while achieving orders-of-magnitude computational speedup over traditional hydrodynamic models.

---

### Streamflow prediction in data-scarce regions with semi-supervised deep learning

**Authors**: Tianlong Jia, Guoding Chen, Yao Li, Xinyu Chang, Uwe Ehret

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1637](https://doi.org/10.5194/egusphere-2026-1637) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Abstract. Deep learning methods have demonstrated great performance in streamflow prediction. However, they typically require large amounts of "labeled" data for supervised learning (SL), including meteorological forcing data paired with corresponding streamflow observations. The data scarcity of streamflow observations in many locations leaves relatively low-accuracy satellite-based estimates as the only option. We propose a semi-supervised deep learning framework that leverages abundant unlabeled meteorological data alongside sparse streamflow observations, significantly improving prediction in data-scarce basins compared to purely supervised approaches.

---

### A prompt-guided differentiable physics model for flood forecasting in data-scarce basins

**Authors**: Jiru Zhang, Jun Feng, Runliang Xia, Pingping Shao, Xin Chi

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135671](https://doi.org/10.1016/j.jhydrol.2026.135671) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model
{: .label .label-green }

> Abstract not available.

---

### Quantification of Data and Model Uncertainty for Deep Learning-based Streamflow Prediction

**Authors**: Kaidi Peng, Daniel Benjamin Wright, Lei Yan, G. Aaron Alexander, Yagmur Derin

**Journal**: *ESSOAr* · **DOI**: [10.22541/essoar.176677052.23567555/v2](https://doi.org/10.22541/essoar.176677052.23567555/v2) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Accurate and timely flood warnings are essential for reducing flooding risks. Achieving this objective requires both accurate data and careful model parameterization. The absence of high-resolution ground-based precipitation observations in many locations leaves relatively low-accuracy satellite-based precipitation estimates as the primary input. We present a framework for jointly quantifying data uncertainty (from satellite precipitation errors) and model uncertainty in deep learning-based streamflow prediction, demonstrating that accounting for both sources substantially improves probabilistic forecast reliability.

---

### Deep learning error post-processing improves stochastic watershed modeling

**Authors**: Benjamin Manoli, Sandeep Poudel, David K. Koval, S. Y. Murphy, Scott Steinschneider, Jonathan Lamontagne

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135663](https://doi.org/10.1016/j.jhydrol.2026.135663) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Abstract not available.

---

### Evaluating data-driven models to estimate snow water equivalent in the Sierra Nevada

**Authors**: Engela Sthapit, Mimi Rose Abel, William Ryan Currier, Rob Cifelli, Peter Fickenscher

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103481](https://doi.org/10.1016/j.ejrh.2026.103481) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Study region: Tuolumne, Merced, American and Feather basins, Sierra Nevada. Study focus: This study explores the ability of data-driven models and an operational, process-based SNOW-17 snow model to estimate historical snow water equivalent (SWE). Current operational streamflow forecasts issued by the California-Nevada River Forecast Center use SWE simulated from SNOW-17. Three machine learning methods of varying complexity — Multiple-Linear Regression, Random Forest Regression, and Long Short-Term Memory networks — are evaluated against SNOW-17 across multiple basins and elevation bands. Results show that ML models achieve competitive or superior SWE estimation accuracy.

---

### Integrating lumped hydrological modelling with GIS-based flow accumulation for spatiotemporal streamflow estimation

**Authors**: Sri Priyanka Kommula, Dongryeol Ryu, Bharat Lohani, Stephan Winter

**Journal**: *Environmental Modelling & Software* · **DOI**: [10.1016/j.envsoft.2026.107026](https://doi.org/10.1016/j.envsoft.2026.107026) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Abstract not available.

---

## Hydrological Data, Monitoring, and Process Studies

New data products and process-level studies rounded out the week. Sun et al. released a comprehensive 63-year daily hydrometeorological dataset for the Yarlung Zangbo basin on the Tibetan Plateau, addressing a critical data gap for this sensitive high-altitude system. Uthayakumar et al. published a novel network connectivity-based stream classification for the entire CONUS, incorporating river network topology — a dimension largely absent from existing classification frameworks. Data assimilation for groundwater estimation advanced with the Aqui-FR platform, while field studies on alpine freeze-thaw runoff processes and dryland river dynamics provided valuable mechanistic insights for model development.

### A 1961–2024 daily hydrometeorological dataset for the Yarlung Zangbo basin of the southern Tibetan Plateau from high-resolution observation and model integration

**Authors**: He Sun, Tandong Yao, Fengge Su, Bowen Zheng, Yi Zhang

**Journal**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07442-6](https://doi.org/10.1038/s41597-026-07442-6) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> Understanding runoff changes in the Yarlung Zangbo (YZ) basin is crucial for water resource management on the Tibetan Plateau (TP), but has been hindered by sparse data. This study provides a comprehensive hydrometeorological dataset for the YZ basin spanning 1961–2024, including both daily meteorological forcing (precipitation, temperature, radiation) and simulated hydrological variables (runoff, evapotranspiration, snow water equivalent). The dataset integrates high-resolution observations with process-based model outputs and is validated against available gauge records.

---

### Network Connectivity-based stream classification for the Conterminous United States

**Authors**: Haripriyan Uthayakumar, Brandon K. Peoples, Julian D. Olden, Stephen Midway, Shweta Singh

**Journal**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07199-y](https://doi.org/10.1038/s41597-026-07199-y) · **Citations**: 0

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> Stream classification plays an important role in the study and management of freshwater ecosystems. Many classification schemes exist that focus predominantly on physical habitat, hydrology, and thermal regimes, but few frameworks explicitly include river network connectivity. Because river network structure fundamentally shapes ecological and hydrological processes, we develop and present a network connectivity-based stream classification for all NHDPlus stream segments across the conterminous United States.

---

### A data assimilation scheme to improve groundwater state estimation in the Aqui-FR modelling platform

**Authors**: Adrien Manlay, Jean‐Pierre Vergnes, Simon Munier, Florence Habets

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1504](https://doi.org/10.5194/egusphere-2026-1504) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> Abstract. Groundwater is a key resource for human activities, and anticipating its evolution months in advance is a major challenge for stakeholders. Hydrological models for subsurface flows can be used for groundwater level forecasts. However, due to uncertainties in the model's forcings and parameters, forecast quality degrades over time. We develop and evaluate a data assimilation scheme within the Aqui-FR modelling platform that ingests observed piezometric levels to improve groundwater state estimation and seasonal forecasting skill.

---

### Integrated analysis of climate and human drivers of streamflow and sediment load in a dryland river

**Authors**: Shihua Yin, Yatong Wu, Enhang Liang, Anqi Huang, Lishan Ran, Guangyao Gao

**Journal**: *CATENA* · **DOI**: [10.1016/j.catena.2026.110210](https://doi.org/10.1016/j.catena.2026.110210) · **Citations**: 0

**Matched topics**: river, streamflow
{: .label .label-green }

> Abstract not available.

---

### Mechanisms driving hydrologic regime shifts in small catchments underlain by continuous permafrost during prolonged warming

**Authors**: Ruixin Wang, Liudmila S. Lebedeva, Ping Wang, Qiwei Huang, Vladimir V. Shamov, Shiqi Liu et al.

**Journal**: *CATENA* · **DOI**: [10.1016/j.catena.2026.110197](https://doi.org/10.1016/j.catena.2026.110197) · **Citations**: 0

**Matched topics**: runoff, streamflow
{: .label .label-green }

> Abstract not available.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 1271 |
| After deduplication | 1001 |
| After LLM relevance filtering | 27 |
| Rejected (not relevant) | 974 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| EGUsphere | 5 |
| Journal of Hydrology | 3 |
| Nature Communications | 2 |
| Communications Earth & Environment | 2 |
| Scientific Data | 2 |
| CATENA | 2 |
| Geophysical Research Letters | 2 |
| ESSOAr | 2 |
| Scientific Reports | 1 |
| Science | 1 |
| Geoscience Frontiers | 1 |
| Hydrological Sciences Journal | 1 |
| Journal of Hydrology Regional Studies | 1 |
| Environmental Modelling & Software | 1 |
| Australian Journal of Agricultural and Resource Economics | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

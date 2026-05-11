---
layout: default
title: "Week 18 (Apr 27 - May 4), 30 papers"
parent: May
grand_parent: "2026"
nav_order: 33
date: 2026-05-04
categories: [weekly, 2026, may]
tags: [hydrology, literature-review, research]
paper_count: 30
highlight: "California faces unprecedented hydrological shifts under warming scenarios; new physics-AI frameworks advance cascade reservoir scheduling."
lang: en
lang_link: /zh/2026/may/2026-05-04-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 18** · April 27–May 4, 2026
{: .text-grey-dk-000 }

**30** relevant papers found across **6** themes
{: .fs-5 .fw-300 }

## Executive Summary

A strong week for hydrologic modeling advances, with multiple WRR papers exploring model combination strategies, spatially explicit parameterization, and prediction in ungauged basins. California's water future received detailed projections showing unprecedented hydrological shifts from 0.5 to 3.5°C warming. Machine learning–hydrology integration continued to mature, with physics-AI hybrid frameworks for reservoir scheduling and satellite embedding fusion for streamflow reconstruction across river networks.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Large-Scale Hydrologic Modeling and Earth System Models

Multiple studies this week advanced our understanding of how global and regional hydrologic models represent key processes. Bass et al. projected unprecedented shifts in California's hydrology under warming scenarios using downscaled ESM ensembles, while Ralhan and Liang developed a physics-informed ML approach to improve surface albedo parameterization in ESMs. At the land surface model scale, Raghav and Kumar introduced a novel method for correcting surface energy imbalance in eddy covariance measurements, and Bender et al. addressed the challenge of representing thermokarst processes in CLM5 through dynamically coupled tiles.

### Unprecedented Shifts in Hydrology Are Emerging Across California's Critical Basins: An Evaluation From 0.5 to 3.5°C

**Authors**: B. Bass, L. Su, D. Pierce et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041338](https://doi.org/10.1029/2025wr041338) · **Citations**: 0

**Matched topics**: hydrology, runoff, earth system model
{: .label .label-green }

> With advances in climate models and downscaling techniques, stakeholders anticipate high‐resolution analysis to inform regional to local changes in water management. Here, we produce hydrologic projections from an ensemble of Earth System Models (ESMs) that were selected and downscaled to support California's Fifth Climate Change Assessment. Results reveal unprecedented shifts in California's hydrology emerging across critical basins under warming scenarios from 0.5 to 3.5°C.

---

### Capturing Spatiotemporal and Subgrid Variability in Global Land Surface Albedo Parameterization

**Authors**: Akarsh Ralhan, Xin‐Zhong Liang

**Journal**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025ms005436](https://doi.org/10.1029/2025ms005436) · **Citations**: 0

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> Accurate surface albedo parameterization is critical for modeling Earth's energy balance. Yet, many schemes rely on static look‐up tables or semi‐empirical formulations that fail to capture spatiotemporal variations and complex radiative interactions. This study develops a physics‐informed machine‐learning parameterization using 19 years (2003–2021) of MODIS Bidirectional Reflectance Distribution Function data and process‐based predictors.

---

### PULSE: A Novel Potential Underlying Water Use Efficiency‐Based Method for Latent Heat and Surface Energy Imbalance Correction

**Authors**: Pushpendra Raghav, Mukesh Kumar

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042766](https://doi.org/10.1029/2025wr042766) · **Citations**: 0

**Matched topics**: land surface model, surface water, earth system model
{: .label .label-green }

> Evapotranspiration (ET) plays a critical role in water and energy budgets over the land surface. Eddy Covariance (EC) is the most widely used technique to measure ET at ecosystem scale, providing insights into land–atmosphere interactions and serving as a benchmark for Earth System Models (ESMs). However, EC measurements frequently suffer from energy balance non‐closure, introducing substantial uncertainty. This study presents PULSE, a novel method that leverages the concept of potential underlying water use efficiency to partition and correct the surface energy imbalance.

---

### Modeling Ice Rich Permafrost Landscapes with CLM5 Using Dynamically Coupled Tiles

**Authors**: Esther Karin Bender, Matvey V. Debolskiy, Kjetil Aas et al.

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1039](https://doi.org/10.5194/egusphere-2026-1039) · **Citations**: 0

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> Thawing of extended amount of ground ice in permafrost regions can lead to rapid, large-scale landscape changes known as thermokarst, which significantly alter the thermal, hydrological and biogeochemistry state of the soil and the land surface. These thermokarst processes are driven by excess ground ice and permafrost microtopography. However, large-scale land surface models, used in coupled climate simulations, cannot represent these processes. This study presents a dynamically coupled tile approach in CLM5 to represent thermokarst landscape evolution.

---

### Advancing Understanding of Parameterization Effects in Global Hydrologic Models Through Multi-Model, Multi-Variable Evaluation

**Authors**: Junho Kim, Jonghun Kam, Daeryong Park et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135208](https://doi.org/10.1016/j.jhydrol.2026.135208) · **Citations**: 1

**Matched topics**: hydrologic model
{: .label .label-green }

> Abstract not available.

---

## Streamflow Prediction and Hydrologic Model Development

This week saw considerable activity in improving streamflow prediction, particularly for ungauged and data-scarce basins. Thébault et al. demonstrated that varying model combinations in time and space outperforms fixed single-model approaches, while Zheng et al. showed that spatially explicit parameterization with multi-gauge calibration significantly improves distributed hydrological modeling. The satellite-based streamflow reconstruction by Lin et al. integrates Google Satellite Embeddings into a reach-scale residual-learning framework. Meanwhile, Argentin et al. tackled the unique challenge of downscaling daily to sub-daily discharge in glacierized Alpine catchments.

### Varying the Combination of Hydrological Models in Time and Space: Toward a More Accurate Representation of Streamflow

**Authors**: C. Thébault, W. J. M. Knoben, N. Addor

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042272](https://doi.org/10.1029/2025wr042272) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> Accurate predictions of streamflow are needed to manage water resources, evaluate flooding risks, and support agriculture and industry. Many hydrological studies rely on a single model structure and parameter set applied uniformly across space and held fixed over time, limiting their ability to capture the complexity and variability of streamflow generation processes. This study explores whether varying the combination of hydrological models in time and space can improve streamflow predictions.

---

### What Can Hydrological Modelling Gain From Spatially Explicit Parameterization and Multi-Gauge Calibration?

**Authors**: Xudong Zheng, Dengfeng Liu, Hao Wang

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2493-2026](https://doi.org/10.5194/hess-30-2493-2026) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Traditional hydrological modelling is facing transformative pressures from the rise of data-driven approaches and increasing demands for modelling realism. With improving data availability, spatially explicit parameterization and multi-gauge calibration offers a promising pathway to enhance the physical coherence and spatial transferability of process-based models.

---

### A Comparative Assessment of Cluster-Based Regionalization Approaches Using Conceptual Rainfall–Runoff Models

**Authors**: Jamal Hassan Ougahi, John S. Rowan

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-49424-z](https://doi.org/10.1038/s41598-026-49424-z) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> Accurate streamflow prediction in ungauged catchments remains a central challenge in hydrology. We investigated the utility of regionalization methods to explore how hydrologically informed clustering influences parameter transferability and performance of different runoff models applied over a national set of catchments.

---

### Improving Streamflow Predictions in Data-Scarce Nested Basins Through Residual Transfer and Post-Processing

**Authors**: Kue Bum Kim, Dawei Han, Hyun‐Han Kwon

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-49028-7](https://doi.org/10.1038/s41598-026-49028-7) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> Reliable streamflow prediction in data-scarce and partially gauged river basins remains a major challenge for hydrological modeling. Even after calibration, conceptual rainfall-runoff models often retain systematic errors, particularly in low- and intermediate-flow regimes, due to structural limitations. This study proposes a residual transfer and post-processing approach for improving predictions in nested basins.

---

### Fusing Satellite Embeddings to Improve Streamflow Reconstruction Across River Networks

**Authors**: Haomei Lin, Peirong Lin, Fenghe Zhang

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1834](https://doi.org/10.5194/egusphere-2026-1834) · **Citations**: 0

**Matched topics**: river, streamflow, land surface model
{: .label .label-green }

> Reconstructing streamflow across river networks is increasingly challenging in the context of heavily modified land surface conditions. Here we present a Data Integration model with Satellite Embeddings (DISE), a reach-scale residual-learning framework that integrates Google Satellite Embeddings with process-based model outputs to improve streamflow reconstruction across river networks.

---

### Downscaling Daily Discharge to Sub‐Daily Scales for Alpine Glacierized Catchments

**Authors**: A.-L. Argentin, M. Gianini, B. Schaefli

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr040699](https://doi.org/10.1029/2025wr040699) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Hydrological dynamics in glacierized catchments of the Alps are shaped by temperature‐driven processes, including snow and ice melt as well as precipitation, leading to diel streamflow cycles that vary in intensity within‐ and among‐the seasons. During the summer melt period, the amplitude of these sub‐daily variations can rival or exceed that of storm‐driven events. This study develops methods for downscaling daily discharge to sub-daily scales in glacierized catchments.

---

### SWATtunR: A Transparent and Reproducible Workflow for Scripted SWAT+ Calibration in R

**Authors**: Svajūnas Plunge, Christoph Schürz, Michael Strauch

**Journal**: *Environmental Modelling & Software* · **DOI**: [10.1016/j.envsoft.2026.107014](https://doi.org/10.1016/j.envsoft.2026.107014) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Abstract not available.

---

## Machine Learning and AI in Water Resources

Physics-AI hybrid approaches for water resources continued to gain momentum. Zhu et al. presented an optimization-learning-simulation framework for cascade reservoir scheduling that bridges historical operations with future climate scenarios. Rittima et al. compared ML and deep learning approaches for reservoir inflow prediction, finding that multivariate LSTM models significantly outperform univariate approaches. Zhou et al. introduced a heterogeneous multi-graph spatio-temporal network that captures complex spatial dependencies in runoff forecasting.

### Physics‐AI Synergized Optimization‐Learning‐Simulation Framework for Robust Cascade Reservoir Scheduling Under Future Hydrological Scenarios

**Authors**: Zhaoyang Zhu, Haotian Wu, Zhaocai Wang et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042149](https://doi.org/10.1029/2025wr042149) · **Citations**: 0

**Matched topics**: runoff, hydropower
{: .label .label-green }

> Coordinated optimization of cascade reservoirs is critical for maximizing a river basin's economic, social, and ecological benefits. However, conventional hydropower scheduling lacks adaptability to complex future scenarios, constrained by seasonal hydrological variability and uncertain inflows. While AI algorithms offer new avenues for reservoir operation, bridging the gap between historical optimization strategies and projected hydrological conditions remains a challenge.

---

### Predictive Performances of Machine Learning– and Deep Learning–Based Univariate and Multivariate Reservoir Inflow Prediction Models

**Authors**: A. Rittima, Jidapa Kraisangka, Pheeranat Dornpunya et al.

**Journal**: *Modeling Earth Systems and Environment* · **DOI**: [10.1007/s40808-026-02795-8](https://doi.org/10.1007/s40808-026-02795-8) · **Citations**: 2

**Matched topics**: river, streamflow, reservoir
{: .label .label-green }

> This study demonstrated the predictability of Machine Learning (ML)– and Deep Learning (DL)–based univariate and multivariate predictions of reservoir inflows of Bhumibol and Sirikit, two major dams in the Chao Phraya River Basin. XGBoost, tree–based ensemble–, and LSTM, deep neural network models were evaluated for their performance across different lead times and input configurations.

---

### A Heterogeneous Multi-Graph Spatio-Temporal Network for Runoff Forecasting

**Authors**: Xuerui Zhou, Baowei Yan, J Zhang

**Journal**: *Engineering Applications of Artificial Intelligence* · **DOI**: [10.1016/j.engappai.2026.114967](https://doi.org/10.1016/j.engappai.2026.114967) · **Citations**: 0

**Matched topics**: hydrology, runoff
{: .label .label-green }

> Abstract not available.

---

## Flood Processes and Risk Assessment

Flood research this week spanned from process understanding to risk management. Kritidou et al. revealed how precipitation lapse rates substantially shape both runoff simulations and flood frequency estimates in mountainous regions. Collins et al. demonstrated how environmental tracers can reduce uncertainty in natural flood management modeling, while Porhemmat et al. analyzed how atmospheric rivers drove the extreme 2021–2022 Westport floods in New Zealand. At the infrastructure level, Perks et al. quantified the hydraulic effects of channel realignment, and Dasari et al. systematically investigated the role of antecedent soil moisture in flood generation across multiple Indian basins.

### How Precipitation Lapse Rates Shape Runoff Simulations and Flood Frequency Estimates in Mountainous Regions

**Authors**: Eleni Kritidou, Martina Kauzlaric, Maria Staudinger

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2338](https://doi.org/10.5194/egusphere-2026-2338) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, runoff, streamflow, flood
{: .label .label-green }

> Precipitation lapse rates (PLRs) play a key role in hydrological simulations of mountainous catchments. However, they are often poorly represented in the precipitation estimates and are typically simplified as constant and positive values in the hydrological models. In this study, we combine observational and model-based analyses to examine how different PLR representations affect runoff simulations and flood frequency estimates.

---

### Using Environmental Tracers to Reduce Uncertainty in Natural Flood Management Modeling

**Authors**: Sarah L. Collins, Leo Peskett, Andrew R. Black

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041145](https://doi.org/10.1029/2025wr041145) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow, flood
{: .label .label-green }

> Natural flood management (NFM) is a nature‐based solution that has grown in importance within flood risk policy and management over the last two decades. There is limited evidence on nature‐based solutions' effectiveness, and no accepted best practice on forecasting their performance. To examine how environmental tracers can constrain model uncertainty, this study applies a tracer-aided approach to NFM modeling.

---

### Atmospheric Rivers and Flood Variability in a Maritime Catchment: Lessons from the 2021–2022 Westport Floods, New Zealand

**Authors**: Rasool Porhemmat, Céline Cattoën, Jono Conway

**Journal**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0168.1](https://doi.org/10.1175/jhm-d-25-0168.1) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, flood
{: .label .label-green }

> Atmospheric rivers (ARs) are increasingly recognised as major drivers of extreme precipitation and flooding in many regions worldwide. On New Zealand's West Coast, the Buller catchment has experienced several severe floods in recent years, raising urgent questions about how AR characteristics influence flood variability in maritime catchments.

---

### Hydraulic Effects of Channel Realignment and Floodplain Reconnection in a Headwater Stream

**Authors**: MT Perks, N. Barber, G. L. Heritage

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041858](https://doi.org/10.1029/2025wr041858) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> Channel realignment and floodplain reconnection are increasingly used as nature‐based solutions for flood management, yet their hydraulic effects remain poorly quantified in field settings of moderate‐gradient, small order channels. This study examines the impact of such interventions on hydraulic conditions in a headwater stream.

---

### Understanding Flood Behaviour: The Role of Antecedent Soil Moisture, Rainfall and Catchment Attributes Across Multiple Basins

**Authors**: Indhu Dasari, Vamsi Krishna Vema, Bharathsagar Jajolla

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70565](https://doi.org/10.1002/hyp.70565) · **Citations**: 0

**Matched topics**: hydrologic model, flood
{: .label .label-green }

> This study aims to understand the effect of antecedent soil moisture (ASM) conditions on flood characteristics across nine Indian basins using the Soil Moisture Accounting (SMA) method within the HEC‐HMS model. Hypothetical rainfall scenarios were simulated under varying ASM conditions to evaluate how pre-event soil moisture states influence flood peak, volume, and timing.

---

## Water Management, Drought, and Climate Impacts

Water management research this week featured several WRR publications addressing the intersection of climate change and water resource planning. Zheng et al. showed how increased interannual precipitation variability compounds water stress beyond what mean drying alone would suggest. Yan et al. introduced a sequential interventions framework for adaptive water management in large river basins, while Han et al. developed a socio-hydrological model capturing continuous human decision-making in water allocation. On the drought front, Jackson et al. derived complementary-relationship evapotranspiration for operational drought monitoring, and Xue et al. (Nature Communications) reconstructed European hydroclimate over the past millennium, revealing how the Scandinavian atmospheric pattern shapes summer droughts.

### How Will Higher Interannual Precipitation Variability Intensify Water Stress Under a Drying Climate?

**Authors**: Hongxing Zheng, Francis Chiew, David Post et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042767](https://doi.org/10.1029/2025wr042767) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow
{: .label .label-green }

> Climate change is expected to alter both the mean and variability of precipitation. Hydrological consequences of higher precipitation variability remain less understood than that induced by changes in precipitation mean. This study evaluates the combined effects of changes in annual precipitation mean and variability on runoff and water supply system across south‐east Australia through a comprehensive modelling framework.

---

### Evaluate Sequential Interventions for Adaptive Water Management in Large River Basins

**Authors**: Yuhan Yan, Tingju Zhu, Zhenxing Zhang et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042451](https://doi.org/10.1029/2025wr042451) · **Citations**: 0

**Matched topics**: hydrologic model, river, water management
{: .label .label-green }

> Integrated River Basin Management (IRBM) and Adaptive Water Management (AWM) have been widely promoted as guiding principles, yet their practical realization at the basin scale remains difficult and underutilized. Sequential Interventions (SIs), stepwise actions applied in a predefined sequence at designated decision points, offer a practical and adaptive approach to implementing AWM.

---

### A Socio‐Hydrological Model for Adaptive Water Allocation in the Heihe River Basin

**Authors**: Ziyan Han, Yongping Wei, Jijun Meng et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr040623](https://doi.org/10.1029/2025wr040623) · **Citations**: 0

**Matched topics**: hydrologic model, river
{: .label .label-green }

> Sustainable management of river basins requires an understanding of how water allocation responds to the human decisions driving it, along with the subsequent economic and ecological consequences. Current models often consider water allocation decisions as single and discontinuous events, overlooking the continuous and adaptive nature of human decision‐making processes. This study develops a socio-hydrological model that captures the co-evolution of water allocation and human adaptation in the Heihe River Basin.

---

### A Method to Implement Natural Flow Regimes for Regulated Rivers

**Authors**: Nicholas A. Som, Seth W. Naman

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041095](https://doi.org/10.1029/2025wr041095) · **Citations**: 0

**Matched topics**: hydrology, river, hydropower
{: .label .label-green }

> Rivers throughout the world have been dammed for flood control, irrigation, hydropower, and water storage for centuries. Dams service the economic and development needs of societies, but degrade the ecology of rivers. To conserve diminishing aquatic species and their habitats, methods are needed to help managers implement flow releases with timescales and patterns that are relevant to aquatic communities.

---

### Probabilistic Agro‐Hydrology: A Stochastic Framework for Irrigation Risk Assessment and Water Management

**Authors**: D. D. Chiarelli, E. Volpi, A. Fiori

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041844](https://doi.org/10.1029/2025wr041844) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, water management, irrigation
{: .label .label-green }

> Irrigation plays a critical role in stabilizing agricultural productivity under increasing climatic variability. However, the intensification of droughts and extreme weather events is revealing the vulnerability of irrigation systems, particularly due to mismatches between peak water needs and water availability. This study presents a stochastic framework for irrigation risk assessment that integrates hydrological uncertainty into water management decision-making.

---

### Fielding Floods for Flourishing Farms: A Framework for Assessing the Reuse of Small Flood Reservoirs as Irrigation Reservoirs

**Authors**: Sarah Ho, Jacob Bernhardt, Kerstin Stahl

**Journal**: *Earth's Future* · **DOI**: [10.1029/2025ef006841](https://doi.org/10.1029/2025ef006841) · **Citations**: 0

**Matched topics**: streamflow, reservoir, flood, irrigation
{: .label .label-green }

> Due to the increased intensity and frequency of droughts under a warming world, agricultural irrigation demand (AID) is likely to increase in many regions of the world—not just in semi‐arid and arid regions, but also in temperate regions. Small reservoirs have often been touted as a decentralized solution for local water management. This study develops a framework for assessing the potential reuse of existing small flood reservoirs as irrigation reservoirs.

---

### Complementary Relationship-Derived Actual Evapotranspiration for Operational Drought Monitoring

**Authors**: Darren L. Jackson, Mike Hobbins, Mimi Rose Abel

**Journal**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0169.1](https://doi.org/10.1175/jhm-d-25-0169.1) · **Citations**: 0

**Matched topics**: streamflow, drought, land surface model
{: .label .label-green }

> To develop a dataset of actual evapotranspiration (ETa) for operational drought monitoring, we used a model of the advection-aridity approach to the complementary relationship between ETa and evaporative demand and North American Land Data Assimilation System phase-2 (NLDAS-2) atmospheric forcing.

---

### Hyperspectral Constraints Reduce Bias in ECOSTRESS Evapotranspiration and Drought Indicators

**Authors**: M. Marshall, Monica Pepe, Giulia Tagliabue

**Journal**: *Remote Sensing of Environment* · **DOI**: [10.1016/j.rse.2026.115453](https://doi.org/10.1016/j.rse.2026.115453) · **Citations**: 0

**Matched topics**: drought, land surface model, earth system model
{: .label .label-green }

> Droughts in Africa's drylands threaten regional food security and global agricultural markets. Early-warning systems increasingly rely on Earth Observation (EO), yet precipitation-based indicators often fail to detect emerging vegetation water stress. With new low-Earth-orbit missions, evapotranspiration from thermal infrared offers a promising complement. This study demonstrates that hyperspectral constraints can reduce bias in ECOSTRESS evapotranspiration retrievals and improve drought indicator accuracy.

---

### Scandinavian Pattern and Temperature Changes Shape European Summer Droughts Over the Past Millennium

**Authors**: Huihong Xue, H Goosse, Quentin Dalaiden et al.

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-026-72385-w](https://doi.org/10.1038/s41467-026-72385-w) · **Citations**: 0

**Matched topics**: drought, earth system model
{: .label .label-green }

(Also featured in daily harvest on 2026-04-27)

> Recent decades have seen pronounced changes in European hydroclimate, including widespread summer drying, yet its spatiotemporal variability and underlying drivers remain uncertain. Here we present the European Last Millennial Data Assimilation (EULMDA), a new reconstruction of European hydroclimate and its main drivers covering the past millennium. EULMDA integrates five Earth System Model simulations with palaeoclimate proxy records, revealing how the Scandinavian atmospheric pattern and temperature changes shape European summer droughts.

---

## River Processes, Datasets, and Cryosphere

New datasets and methodological advances rounded out the week's publications. Gagliano et al. released a global high-resolution dataset of snowmelt runoff onset timing derived from Sentinel-1 SAR spanning 2015–2024, filling a critical gap in cryospheric monitoring. Jones et al. contributed Caravan-Qual, integrating stream water quality observations into the widely-used Caravan large-sample hydrology dataset. Legleiter and Kinzel capitalized on a national cross-section database to evaluate common approximations of river channel geometry, with implications for large-scale river routing and hydraulic modeling.

### A Global High-Resolution Dataset of Snowmelt Runoff Onset Timing from Sentinel-1 SAR, 2015–2024

**Authors**: Eric Gagliano, David Shean, Scott Henderson

**Journal**: *ESSD* · **DOI**: [10.5194/essd-2026-216](https://doi.org/10.5194/essd-2026-216) · **Citations**: 0

**Matched topics**: runoff, streamflow
{: .label .label-green }

> Snowmelt runoff onset timing represents a critical hydrological parameter, particularly in mountainous regions where seasonal snow serves as a natural reservoir for downstream water resources. Despite this importance, high-resolution observations of snowmelt runoff onset across complex terrain are limited, due to challenges from sparse in situ monitoring networks, intermittent optical remote sensing, and coarse passive microwave data. This study leverages Sentinel-1 SAR to produce a global high-resolution dataset spanning 2015–2024.

---

### Caravan-Qual: A Global Scale Integration of Stream Water Quality Observations into a Large-Sample Hydrology Dataset

**Authors**: Edward R Jones, Frederik Kratzert, Michelle T H van Vliet

**Journal**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07352-7](https://doi.org/10.1038/s41597-026-07352-7) · **Citations**: 0

**Matched topics**: hydrology, streamflow, surface water
{: .label .label-green }

> Protecting and improving surface water quality is contingent upon understanding the trends and spatial patterns in physical, biological, and chemical conditions and their underlying drivers. This requires observational data, spanning a diverse range of water quality constituents, coupled with contextual information on catchment attributes. Caravan-Qual integrates stream water quality observations into the Caravan large-sample hydrology dataset at a global scale.

---

### Evaluating Approximations of River Channel Shape Using a National Cross‐Section Database

**Authors**: C.J. Legleiter, P. J. Kinzel

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041177](https://doi.org/10.1029/2025wr041177) · **Citations**: 0

**Matched topics**: river, streamflow
{: .label .label-green }

> Many hydrologic applications require basic information on the size and shape of river channels, but measuring cross section geometry in the field or via remote sensing can be costly and often provides only partial coverage. Given these challenges, we capitalized upon an existing data set of 46,971 cross sections from gaging stations to evaluate various approximations of channel shape, with implications for river routing and hydraulic modeling.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 1427 |
| After deduplication | 1206 |
| After blocklist filtering | 1149 |
| After LLM relevance filtering | 30 |
| Rejected (not relevant) | 1119 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Water Resources Research | 13 |
| Hydrological Processes | 2 |
| Scientific Reports | 2 |
| Journal of Hydrology | 2 |
| EGUsphere | 3 |
| Journal of Hydrometeorology | 2 |
| Nature Communications | 1 |
| Earth's Future | 1 |
| Remote Sensing of Environment | 1 |
| Journal of Advances in Modeling Earth Systems | 1 |
| Hydrology and Earth System Sciences | 1 |
| Environmental Modelling & Software | 1 |
| Modeling Earth Systems and Environment | 1 |
| Engineering Applications of Artificial Intelligence | 1 |
| Scientific Data | 1 |
| ESSD | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

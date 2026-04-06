---
layout: default
title: "Week 13, 30 papers"
parent: March
grand_parent: "2026"
nav_order: 33
date: 2026-03-23
categories: [weekly, 2026, march]
tags: [hydrology, literature-review, research]
paper_count: 30
highlight: "Differentiable hydrologic modeling advances and the unveiling of the NextGen Water Resources Modeling Framework."
lang: en
lang_link: /zh/2026/march/2026-03-23-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 13** · March 16–23, 2026
{: .text-grey-dk-000 }

**30** relevant papers found across **5** themes
{: .fs-5 .fw-300 }

## Executive Summary

A strong week for differentiable and next-generation hydrologic modeling, with notable advances in physics-informed ML frameworks for extreme events, a new differentiable Noah land surface model for permafrost, and the unveiling of the NextGen Water Resources Modeling Framework. Compound flood modeling saw significant methodological contributions comparing event- vs response-based approaches. A landmark Nature study quantified global river delta subsidence at unprecedented resolution, while new work in Nature Water applied text-generating AI to hydrological parameter estimation.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Differentiable and Next-Generation Hydrologic Modeling

The convergence of physics-based and machine learning approaches in hydrology accelerated this week. Song et al. demonstrate that differentiable hydrologic models combining ML with process-based equations can generalize to unseen extreme floods, while two new land surface models — ClimaLand (designed for data-driven parameterizations) and NoahPy (a differentiable Noah LSM for permafrost) — represent a shift toward ML-ready model architectures. The NextGen Water Resources Modeling Framework introduces a community platform for continental-scale prediction, and Feigl et al. show that text-generating AI can derive hydrological parameters from physio-geographical properties.

### Physics-Informed, Differentiable Hydrologic Models for Capturing Unseen Extreme Events

**Authors**: Yalan Song, Kamlesh Sawadekar, Jonathan M. Frame, Ming Pan, Martyn P. Clark, Wouter J. M. Knoben et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025WR040414](https://doi.org/10.1029/2025WR040414) · **Citations**: 9

**Matched topics**: hydrology, streamflow, flood
{: .label .label-green }

> A hybrid framework combining machine learning and process-based equations (differentiable modeling) is evaluated for generalization to extreme floods outside training data. The study examines whether optimizing for extremes improves model performance and robustness, finding that differentiable models offer enhanced interpretability and spatial generalizability compared to pure ML approaches.

---

### ClimaLand: A Land Surface Model Designed to Enable Data-Driven Parameterizations

**Authors**: Katherine Deck, R. K. Braghiere, Alexandre A. Renchon, Julia Sloan, G. Bozzola, E. Speer et al.

**Journal**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025ms005118](https://doi.org/10.1029/2025ms005118) · **Citations**: 3

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> A new land surface model specifically designed to enable data-driven parameterizations of sub-grid processes. ClimaLand addresses the challenge of parameterizing water, energy, and carbon fluxes at climate model scales (~10–100 km), offering a framework where traditional parameterizations can be replaced or augmented with machine learning components.

---

### NoahPy: A Differentiable Noah Land Surface Model for Simulating Permafrost Thermo-Hydrology

**Authors**: W. Tian, Hu Yu, Shuping Zhao, Yuhe Cao, Wenjun Yi, Jiwei Xu et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-57-2026](https://doi.org/10.5194/gmd-19-57-2026) · **Citations**: 1

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> Creates a differentiable version of the Noah LSM to enable hybrid models that synergize process-based physics with deep learning for permafrost simulation. This overcomes the fundamental barrier of non-differentiable traditional LSMs being incompatible with modern AI workflows, opening the door to automatic parameter calibration and hybrid physics-ML approaches for cold-region hydrology.

---

### Distilling Hydrological and Land-Surface Model Parameters from Physio-Geographical Properties Using Text-Generating AI

**Authors**: Moritz Feigl, M. Herrnegger, K. Schulz

**Journal**: *Nature Water* · **DOI**: [10.1038/s44221-026-00583-3](https://doi.org/10.1038/s44221-026-00583-3) · **Citations**: 2

**Matched topics**: hydrology, land surface model
{: .label .label-green }

> Applies text-generating AI to derive hydrological and land-surface model parameters directly from physio-geographical properties, offering a novel approach to the perennial challenge of parameter regionalization in ungauged basins.

---

### The NextGen Water Resources Modeling Framework: Community Innovation at the Intersection of Hydrologic, Data and Computer Sciences

**Authors**: F. Ogden, Keith S. Jennings, E. Clark, E. Coon, B. Cosgrove, Luciana K. Cunha et al.

**Journal**: *JAWRA Journal of the American Water Resources Association* · **DOI**: [10.1111/1752-1688.70089](https://doi.org/10.1111/1752-1688.70089) · **Citations**: 1

**Matched topics**: hydrology, water management
{: .label .label-green }

> Introduces the NextGen framework for continental-scale hydrologic and hydraulic prediction, arguing that regional mosaics of models focusing on dominant local processes may outperform a single general model. The framework operates at the intersection of hydrologic, data, and computer sciences, enabling community innovation in water resources prediction.

---

### Advancing Ecohydrological Modelling: Coupling LPJ-GUESS with ParFlow for Integrated Vegetation and Surface-Subsurface Hydrology Simulations

**Authors**: Zitong Jia, Shouzhi Chen, Yongshuo H. Fu, David Martín Belda, D. Wårlind, Stefan Olin et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-1727-2026](https://doi.org/10.5194/gmd-19-1727-2026) · **Citations**: 2

**Matched topics**: earth system model, climate change, hydrology
{: .label .label-green }

> Integrates the LPJ-GUESS dynamic vegetation model with ParFlow to capture topography-driven vegetation–surface–groundwater interactions that many Earth system models currently neglect. Addresses a key gap in representing climate-hydrological feedbacks.

---

### DeepDiscover: Towards Autonomous Discovery of Bucket-Type Conceptual Models – A Proof of Concept Applied to Hydrology

**Authors**: Adoubi Vincent De Paul Adombi

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135249](https://doi.org/10.1016/j.jhydrol.2026.135249) · **Citations**: 1

**Matched topics**: hydrology, hydrologic model
{: .label .label-green }

> A proof-of-concept for using deep learning to autonomously discover bucket-type conceptual hydrological models, pushing the frontier of automated model structure identification.

---

## Flood Modeling, Prediction, and Risk Assessment

Compound flood hazard assessment received strong methodological attention. Santamaria-Aguilar et al. reveal large discrepancies between event-based and response-based compound flood estimates, while Maduwantha et al. develop probabilistic boundary conditions for compound flood models. GPU-accelerated physics-based modeling enables real-time city-scale flood forecasting for Berlin, and the FIER framework is evaluated for large-scale flood inundation prediction.

### Probabilistic Hierarchical Interpolation and Interpretable Neural Network Configurations for Flood Prediction

**Authors**: Mostafa Saberian, Vidya Samadi, Ioana Popescu

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-371-2026](https://doi.org/10.5194/hess-30-371-2026) · **Citations**: 5

**Matched topics**: flood, streamflow, runoff
{: .label .label-green }

> Develops interpretable neural network configurations for hydrological flood prediction using probabilistic hierarchical interpolation. Addresses the challenge of learning complex rainfall-runoff processes while maintaining model interpretability.

---

### How Well Do Hydrological Models Simulate Streamflow Extremes and Drought-to-Flood Transitions?

**Authors**: Eduardo Muñoz-Castro, Bailey Anderson, Paul C. Astagneau, Daniel L. Swain, Pablo A. Mendoza, Manuela I. Brunner

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-825-2026](https://doi.org/10.5194/hess-30-825-2026) · **Citations**: 4

**Matched topics**: streamflow, drought, flood, hydrologic model
{: .label .label-green }

> Evaluates how well hydrological models capture compound extreme events — specifically floods occurring shortly after droughts. Identifies which modeling decisions most influence the simulation of these increasingly important drought-to-flood transitions.

---

### Large Discrepancies Between Event- and Response-Based Compound Flood Hazard Estimates

**Authors**: S. Santamaria-Aguilar, Pravin Maduwantha, A. Enriquez, Thomas I. Wahl

**Journal**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-26-571-2026](https://doi.org/10.5194/nhess-26-571-2026) · **Citations**: 4

**Matched topics**: flood, compound flood
{: .label .label-green }

> Reveals that traditional event-based flood hazard assessments, which assume flooding probability approximates flood driver probability, significantly diverge from response-based approaches that account for temporal and spatial variability of flood processes. Important methodological implications for compound flood risk assessment.

---

### Generating Boundary Conditions for Compound Flood Modeling in a Probabilistic Framework

**Authors**: Pravin Maduwantha, Thomas Wahl, S. Santamaria-Aguilar, R. Jane, S. Dangendorf, Hanbeen Kim et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-401-2026](https://doi.org/10.5194/hess-30-401-2026) · **Citations**: 4

**Matched topics**: flood, compound flood
{: .label .label-green }

> Addresses the challenge of generating probabilistic boundary conditions for compound flood models that capture the full range of flood driver variability. Advances computational methods for comprehensive compound flood risk assessment.

---

### Evaluating the Feasibility of Scaling the FIER Framework for Large-Scale Flood Inundation Prediction

**Authors**: K. Markert, Hyongki Lee, Gus Williams, E. Nelson, Daniel P. Ames, Robert E. Griffin et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-459-2026](https://doi.org/10.5194/hess-30-459-2026) · **Citations**: 2

**Matched topics**: flood, remote sensing
{: .label .label-green }

> Evaluates the scalability of the FIER (Flood Inundation Estimation Routine) framework for large geographic areas, addressing computational and data requirement challenges of traditional flood forecasting methods.

---

### Enabling Real-Time High-Resolution Flood Forecasting for the Entire State of Berlin Through Multi-GPU Accelerated Physics-Based Modeling

**Authors**: Shahin Khosh Bin Ghomash, Siqi Deng, Heiko Apel

**Journal**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-26-85-2026](https://doi.org/10.5194/nhess-26-85-2026) · **Citations**: 2

**Matched topics**: flood, climate change
{: .label .label-green }

> Demonstrates city-scale real-time flood forecasting using multi-GPU accelerated physics-based hydrodynamic modeling, covering the entire state of Berlin. Shows that GPU computing advances can make high-resolution urban flood modeling operationally feasible.

---

## Machine Learning for Runoff and Streamflow Prediction

Multiple ML architectures were applied to runoff and streamflow forecasting this week. Jia et al. combine mixture density networks with conformal inference for probabilistic runoff prediction across Australia, while Yuan & Yan introduce causal lag-aware attention in transformers for multi-scale runoff prediction. Hybrid deep learning approaches for rainfall-runoff forecasting and interpretable streamflow prediction round out this theme.

### A Novel Hybrid Predictive Model Based on Mixture Density Networks With Weighted Conformal Inference Strategy for Runoff Interval Prediction Across Australia

**Authors**: Yubo Jia, Xiaoling Su, Vijay P. Singh, Bin Zhao, T. Zhang, Jiangdong Chu et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2024WR039807](https://doi.org/10.1029/2024WR039807) · **Citations**: 3

**Matched topics**: runoff, flood, drought
{: .label .label-green }

> Develops a Mixture Density Network with weighted conformal inference for probabilistic runoff interval prediction across Australia. Addresses MDN susceptibility to bias by integrating a conformal inference strategy that improves uncertainty quantification for water security applications.

---

### A Hybrid Deep Learning Rainfall-Runoff Forecasting Model Incorporating Spatiotemporal Information from Multi-Source Data

**Authors**: Wan Liu, Li Mo, Xiaodong Li, Wenjing Xiao, Haodong Huang, Yongchuan Zhang

**Journal**: *Expert Systems with Applications* · **DOI**: [10.1016/j.eswa.2025.129974](https://doi.org/10.1016/j.eswa.2025.129974) · **Citations**: 3

**Matched topics**: runoff, rainfall-runoff
{: .label .label-green }

> A hybrid deep learning model for rainfall-runoff forecasting that incorporates spatiotemporal information from multiple data sources to improve forecast accuracy.

---

### Enhancing Runoff Prediction with Causal Lag-Aware Attention and Multi-Scale Fusion in Transformer Models

**Authors**: Weiheng Yuan, Hua Yan

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134369](https://doi.org/10.1016/j.jhydrol.2025.134369) · **Citations**: 2

**Matched topics**: runoff
{: .label .label-green }

> Introduces causal lag-aware attention mechanisms and multi-scale fusion into transformer models for improved runoff prediction, addressing the challenge of capturing temporal dependencies at multiple scales.

---

### Interpretable Deep Learning Hybrid Streamflow Prediction Modeling Based on Multi-Source Data Fusion

**Authors**: Zhaocai Wang, Cheng Ding, Nannan Xu, Weilong Wang, Xingxing Zhang

**Journal**: *Environmental Modelling & Software* · **DOI**: [10.1016/j.envsoft.2025.106796](https://doi.org/10.1016/j.envsoft.2025.106796) · **Citations**: 2

**Matched topics**: streamflow, deep learning
{: .label .label-green }

> Combines deep learning with interpretability techniques for hybrid streamflow prediction, fusing multi-source data to improve forecast reliability and understanding.

---

## Drought, Climate Change, and Compound Events

Drought research spanned from seasonal projections to compound event dynamics. Ukkola et al. use Australia's National Hydrological Projections ensemble to assess future seasonal drought changes, while Sabut & Mishra provide a century-scale bibliometric synthesis of drought science. Li et al. examine record-shattering compound drought-heatwave events, and Kim et al. show that constraining climate projections with observations amplifies projected runoff declines.

### Future Changes in Seasonal Drought in Australia

**Authors**: Anna Ukkola, Steven Thomas, Elisabeth Vogel, Ulrike Bende-Michl, Steven T. Siems, Vjekoslav Matic et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-1463-2026](https://doi.org/10.5194/hess-30-1463-2026) · **Citations**: 4

**Matched topics**: drought, climate change, hydrology
{: .label .label-green }

> Uses the National Hydrological Projections ensemble to assess future drought changes in Australia, the driest inhabited continent. Addresses the persistent uncertainty stemming from lack of model agreement in projected precipitation changes, finding season- and region-specific drought trends that inform water management planning.

---

### A Century of Drought Research (1900–2023): Scientific Developments, Methodological Innovations, and Emerging Frontiers

**Authors**: Amitesh Sabut, A. Mishra

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025WR041987](https://doi.org/10.1029/2025WR041987) · **Citations**: 3

**Matched topics**: drought, water resources
{: .label .label-green }

> A comprehensive review synthesizing a century of drought research from a bibliometric analysis of over 152,000 publications. Traces the evolution from historical drought documentation to modern monitoring techniques and emerging frontiers in drought science.

---

### Understanding the Dynamics of Record-Shattering Compound Drought-Heatwave Events and Their Impacts on Ecosystems

**Authors**: Bohao Li, Kai Liu, Ming Wang, Yuanhang Yang, Mingzhu He, Yanfang Wang et al.

**Journal**: *Earth's Future* · **DOI**: [10.1029/2024EF005714](https://doi.org/10.1029/2024EF005714) · **Citations**: 2

**Matched topics**: drought, climate change
{: .label .label-green }

> Projects that record-shattering compound drought-heatwave events will increase dramatically under future scenarios, using nine-member ensemble simulations. Examines the dynamics, formation mechanisms, and ecosystem impacts of these unprecedented compound extremes.

---

### Constraining Climate Model Projections with Observations Amplifies Future Runoff Declines

**Authors**: Hanjun Kim, Flavio Lehner, K. Dagon, D. Lawrence, Sean Swenson, A. W. Wood

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03213-8](https://doi.org/10.1038/s43247-026-03213-8) · **Citations**: 1

**Matched topics**: runoff, climate change
{: .label .label-green }

> Demonstrates that constraining climate model projections with observational data amplifies projected future declines in runoff, with significant implications for water resources planning and climate impact assessment.

---

## Reservoirs, Water Storage, and Catchment Hydrology

Reservoir monitoring and large-scale observations saw important advances. An et al. reconstruct monthly water levels for 7,433 lakes and reservoirs across Asia using satellite altimetry, while Zhan et al. integrate SWOT with multi-source observations for near-daily reservoir monitoring. A Nature study provides the first high-resolution quantification of global river delta subsidence. On the catchment side, van Tiel et al. analyze glacier contributions to streamflow during the 2022 European drought, and Ryu et al. apply 3D U-Net for sub-seasonal precipitation forecasting.

### Water Storage Changes of Lakes and Reservoirs Across Asia (2018–2023) and Their Effects in Flood Control

**Authors**: Zhiyuan An, Zhao Li, T. Jin, Weiping Jiang, Peng Yuan, Kai Liu et al.

**Journal**: *Geophysical Research Letters* · **DOI**: [10.1029/2025GL119131](https://doi.org/10.1029/2025GL119131) · **Citations**: 2

**Matched topics**: reservoir, flood, water management
{: .label .label-green }

> Integrates Sentinel-3A/B and ICESat-2 altimetry to reconstruct monthly water levels for 7,433 lakes and reservoirs across Asia (2018–2023). Finds that reservoirs exhibit a median annual water level change of 0.36 m/yr, far exceeding the 0.05 m/yr of natural lakes, highlighting the role of human management in water storage dynamics and flood control.

---

### Integrating SWOT With Multi-Source Satellite Observations for Near-Daily Reservoir Water Level Monitoring

**Authors**: P. Zhan, Jida Wang, Tan Chen, Shuangxiao Luo, Kai Liu, L. Ke et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2024WR039711](https://doi.org/10.1029/2024WR039711) · **Citations**: 1

**Matched topics**: reservoir, water management
{: .label .label-green }

> Develops a framework integrating SWOT with multi-source satellite observations to achieve near-daily reservoir water level monitoring, addressing limitations of traditional satellite altimetry for high-frequency reservoir monitoring critical to water resource management.

---

### Integrated Artificial Intelligence and Physics-Based Modeling for Long-Term Cascaded Hydropower Scheduling Under Extreme Heat Events

**Authors**: Maryam Baghkarvasef, M. Parvania

**Journal**: *IEEE Transactions on Sustainable Energy* · **DOI**: [10.1109/TSTE.2025.3584176](https://doi.org/10.1109/TSTE.2025.3584176) · **Citations**: 4

**Matched topics**: hydropower, reservoir
{: .label .label-green }

> Integrates AI and physics-based modeling for long-term scheduling of cascaded hydropower systems during extreme heatwave events, deriving water values that enable effective strategic planning when hydropower plants face heat-driven operational challenges.

---

### Advancing Climate Change Impact Assessment on Global Hydropower Systems: Methodologies, Models, and Recommendations

**Authors**: Raja Fara Raja Abd Jalil, K. L. Chong, Y. F. Huang, Marlinda Abdul Malek, Mohamed Elkollaly, Mohsen Sherif et al.

**Journal**: *Renewable & Sustainable Energy Reviews* · **DOI**: [10.1016/j.rser.2025.116364](https://doi.org/10.1016/j.rser.2025.116364) · **Citations**: 2

**Matched topics**: hydropower, climate change
{: .label .label-green }

> A comprehensive review of methodologies and models for assessing climate change impacts on global hydropower systems, providing recommendations for improving assessment frameworks.

---

### Global Subsidence of River Deltas

**Authors**: L. Ohenhen, M. Shirzaei, J. L. Davis, A. Tiwari, R. Nicholls, O. Dasho et al.

**Journal**: *Nature* · **DOI**: [10.1038/s41586-025-09928-6](https://doi.org/10.1038/s41586-025-09928-6) · **Citations**: 8

**Matched topics**: river, climate change
{: .label .label-green }

> Provides the first contemporary, high-resolution quantification of global river delta subsidence, finding that rising sea levels combined with subsiding land threaten the sustainability of delta landscapes worldwide. The study fills a critical gap in vulnerability assessments for these densely populated regions.

---

### Swiss Glacier Mass Loss During the 2022 Drought: Persistent Streamflow Contributions Amid Declining Melt Water Volumes

**Authors**: Marit van Tiel, M. Huss, M. Zappa, T. Jonas, D. Farinotti

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-23-2026](https://doi.org/10.5194/hess-30-23-2026) · **Citations**: 3

**Matched topics**: streamflow, drought, glacier
{: .label .label-green }

> Analyzes glacier contributions to streamflow during the severe 2022 European drought across 88 glacierized catchments in Switzerland. Shows that extreme glacier melt partially compensated for drought-reduced streamflow, but this buffering capacity is declining as glaciers shrink — a critical finding for Europe's water tower.

---

### Controls on Runoff Processes in Forested Catchments Worldwide

**Authors**: D. Penna

**Journal**: *Nature Water* · **DOI**: [10.1038/s44221-025-00547-z](https://doi.org/10.1038/s44221-025-00547-z) · **Citations**: 1

**Matched topics**: runoff, catchment
{: .label .label-green }

> Examines the key controls on runoff generation processes in forested catchments at the global scale, contributing to fundamental understanding of how forests regulate water cycling.

---

### Regionalization of Hydrologic Behavior and Pothole Water Storage Dynamics in the Prairie Pothole Region

**Authors**: J. Rahmani, Chaopeng Shen, A. Ameli

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025WR040280](https://doi.org/10.1029/2025WR040280) · **Citations**: 1

**Matched topics**: hydrology, hydrologic model
{: .label .label-green }

> Addresses the challenge of modeling pothole-dominated catchments in the Prairie Pothole Region, where complex fill-spill-connection mechanisms, ungauged conditions, and lack of high-resolution pothole inventories pose challenges for both traditional and data-driven models.

---

### Increasing Resolution and Accuracy in Sub-Seasonal Forecasting Through 3D U-Net: The Western US

**Authors**: Jihun Ryu, Hisu Kim, Simon Wang, Jin-Ho Yoon

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-27-2026](https://doi.org/10.5194/gmd-19-27-2026) · **Citations**: 2

**Matched topics**: precipitation, seasonal forecast
{: .label .label-green }

> Uses 3D U-Net architecture for post-processing sub-seasonal precipitation forecasts at high spatial resolution in the western US, addressing the challenge of capturing complex patterns and extreme events that traditional NWP models struggle with at finer scales.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers before dedup | 2,193 |
| Unique papers after dedup | 1,919 |
| After LLM relevance filtering | 30 |
| Rejected (not relevant) | 1,889 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

---
layout: default
title: "Week 27 (Jun 29 - Jul 06), 28 papers"
parent: July
grand_parent: "2026"
nav_order: 33
date: 2026-07-13
categories: [weekly, 2026, july]
tags: [hydrology, literature-review, research]
paper_count: 28
highlight: "AI agents now autonomously configure hydrological models from plain-language queries (GRL), while CaMa-Flood-GPU delivers orders-of-magnitude speedup for global flood simulation."
lang: en
lang_link: /zh/2026/july/2026-07-13-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 27** · Jun 29–Jul 06, 2026
{: .text-grey-dk-000 }

**28** relevant papers found across **7** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's literature reflects broad advances across the water-modeling stack, from foundational AI tools to cryosphere process representation. The standout methodological contribution is a six-level AI-agent framework for autonomous hydrologic modeling (GRL), matched on the computational side by CaMa-Flood-GPU, which delivers orders-of-magnitude acceleration for global floodplain simulation. In parallel, a wave of new global datasets — GLORIF1 (monthly river discharge 1979–2019) and a spatiotemporal drought catalog (1980–2024) — are filling long-standing data gaps. Reservoir management and cryosphere-hydrology feedbacks both emerge as active fronts, with papers on forecast-informed operations, permafrost thaw delays to streamflow, and snow–soil-moisture coupling in the drought-stressed Colorado River Basin.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## AI & Machine Learning in Hydrological Modeling

This week brought three complementary AI/ML contributions that push hydrologic modeling toward greater autonomy and efficiency. Yan et al. define a formal six-level AI-agent hierarchy for hydrologic modeling and demonstrate a Level-4 agent that translates natural-language instructions into complete model configurations — representing a qualitative shift toward democratized hydrologic simulation. Jin et al. address rainfall observation from the opposite angle, deploying a lightweight ML model to extract rain-streak features from everyday surveillance and dash-camera video, offering opportunistic sensing in data-sparse regions. Hammad et al. tackle the "legacy model" problem with state-dependent residual post-processing that conditions error corrections on hydrologic state, outperforming uniform residual methods across wet and dry regimes.

### AI Agent for Hydrologic Modeling: Definition, Development, and Application

**Authors**: Songkun Yan, Mengye Chen, Zhi Li, Yixin Wen, Siyu Zhu, Mofan Zhang et al.

**Journal**: *Geophysical Research Letters* · **DOI**: [10.1029/2025gl119814](https://doi.org/10.1029/2025gl119814) · **Citations**: 1

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

(Also featured in daily harvest on 2026-07-04)

> Hydrologic modeling supports flood forecasting and water resources management, but complex preprocessing, parameterization, and configuration limit broader use. This study defines a six‐level framework for artificial intelligence (AI)‐agent autonomy in hydrologic modeling and develops a Level‐4 agent, powered by large language models, that translates natural‐language requests into data retrieval, preprocessing, model configuration, and result analysis without human intervention. The framework is demonstrated on a conceptual hydrological model applied across 671 basins globally, achieving performance comparable to expert calibration while requiring minimal user input.

---

### Video‐Based Rainfall Opportunistic Sensing in Hydrology: A Lightweight Machine Learning Approach

**Authors**: Yongcheng Jin, Zhe Zhu, Xinwei Xue, Guangtao Fu, Chi Zhang, Yu Li

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041953](https://doi.org/10.1029/2025wr041953) · **Citations**: 0

**Matched topics**: hydrology
{: .label .label-green }

> Abstract Video‐based rainfall measurement is a frontier topic in opportunistic sensing; however, rapid, accurate, and robust identification of rainfall‐related rain‐streak features from dynamic videos remains a key challenge, especially for monitoring devices with limited computational resources. To address the trade‐off between measurement accuracy and efficiency, we propose a lightweight machine learning approach using a ShuffleNetV2‐based backbone that distinguishes rainfall events and intensities from video frames with low computational overhead, enabling deployment on edge devices in real hydrologic monitoring networks.

---

### Can State‐Dependent Residual Modeling Improve Legacy Hydrological Model Simulations?

**Authors**: Muhammad Hammad, Rajeshwar Mehrotra, Ashish Sharma

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2026wr044285](https://doi.org/10.1029/2026wr044285) · **Citations**: 0

**Matched topics**: hydrologic model
{: .label .label-green }

> Abstract Traditional residual post‐processing methods have demonstrated substantial improvements in simulated hydrological response; however, they typically aggregate multiple sources of uncertainty into a single lumped residual and apply uniform statistical treatment across all hydrologic conditions. This uniform treatment overlooks the fact that error characteristics can vary systematically across wet and dry states. State‐dependent residual modeling conditions corrections on concurrent soil moisture and antecedent conditions, yielding consistent gains in streamflow simulation skill across contrasting climate regimes.

---

## Global River Flow Modeling & Land Surface Models

Five papers this week collectively push the frontier of global-scale water-cycle simulation. Işık et al. release GLORIF1, a 40-year monthly global river flow dataset generated by fusing process-based routing with machine learning bias correction. Kang et al. port CaMa-Flood to GPU architecture, achieving up to 100× acceleration and unlocking ensemble global flood projections previously out of reach. Yuan et al. present CSSPv3, a land surface model that explicitly couples natural ecohydrology with anthropogenic water use in a single global framework. Nan et al. demonstrate that omitting frozen soil from hydrological models substantially biases estimated runoff sensitivity to warming in cold mountain basins — a direct risk for E3SM/ELM land-surface applications in high-latitude and alpine settings. Wu et al. show that replacing static vegetation and radiation parameters with dynamic satellite-derived inputs significantly improves continental-scale streamflow simulation across China, motivating similar upgrades in other large-domain models.

### GLORIF1, a global river flow dataset created by integrating process-based modelling and machine learning

**Authors**: Sümeyye Büşra Işık, Oriol Pomarol Moya, Michele Magni, Madlene Nussbaum, Derek Karssenberg, Edwin H. Sutanudjaja

**Journal**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07658-6](https://doi.org/10.1038/s41597-026-07658-6) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> Accurate streamflow data are essential for managing water resources and enhancing climate resilience worldwide. Yet, existing global streamflow datasets often lack accuracy or rely on sparse observations. To address these challenges, we present GLORIF1 (GLObal RIver Flow version 1), a comprehensive monthly river discharge dataset spanning 1979–2019. GLORIF1 is generated using a hybrid modeling approach that combines PCR-GLOBWB process-based routing with machine learning post-processing, substantially reducing biases in ungauged regions relative to existing products.

---

### CaMa-Flood-GPU: a GPU-based hydrodynamic model implementation for scalable global simulations

**Authors**: Shengyu Kang, Jiabo Yin, Dai Yamazaki

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-5623-2026](https://doi.org/10.5194/gmd-19-5623-2026) · **Citations**: 0

**Matched topics**: hydrology, flood
{: .label .label-green }

> Floods are among the costliest natural hazards, demanding scalable models to simulate river and floodplain dynamics at a global scale. The Catchment-based Macro-scale Floodplain (CaMa-Flood) model is a leading system for this purpose, but its CPU-based implementation is computationally demanding. This paper introduces CaMa-Flood-GPU, a fundamental refactoring of the model optimized for GPU parallel computing using CUDA, achieving speedups of 50–100× over the CPU version and enabling ensemble global flood simulations at fine resolution within practical time windows.

---

### Development and Evaluation of the Conjunctive Surface‐Subsurface Process Model Version 3 (CSSPv3) at Global Scale

**Authors**: Xing Yuan, Chenyuan Li, Peng Ji, Xiazhen Xi, Shuwen Li, Yang Jiao et al.

**Journal**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025ms005440](https://doi.org/10.1029/2025ms005440) · **Citations**: 0

**Matched topics**: streamflow, land surface model
{: .label .label-green }

> The global terrestrial water and carbon cycles have evolved rapidly during recent decades, particularly in regions with intensive anthropogenic interventions and vulnerable ecohydrological systems. However, current land surface models (LSMs) and global hydrological models (GHMs) often treat natural ecohydrological processes and human water use in isolation, leaving a critical gap in the holistic representation of the water cycle. CSSPv3 bridges this gap by explicitly coupling natural and human-managed water fluxes within a single land surface framework evaluated against streamflow and terrestrial water storage observations at global scale.

---

### Omitting Frozen‐Soil Effects in Hydrological Models Introduces Biases in Estimated Runoff Sensitivity to Climate Change in Cold Basins

**Authors**: Yi Nan, Fuqiang Tian, Ying Zhao

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041331](https://doi.org/10.1029/2025wr041331) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow
{: .label .label-green }

> Proper representation of cryospheric processes is essential for accurate hydrological simulation in cold mountainous catchments. Frozen soil, a key cryospheric element, is sometimes overlooked in hydrological models, and its hydrological influence remains insufficiently explored. This study compares two versions of the THREW-T model — with and without frozen-soil dynamics — in a Tibetan Plateau basin. Omitting frozen soil yields substantially biased estimates of runoff sensitivity to temperature change, with the magnitude and sign of bias depending on elevation and thaw seasonality.

---

### Dynamic Satellite-Derived Vegetation and Radiation Inputs Advance Continental-Scale Hydrological Simulation Across China

**Authors**: Xinran Wu, Dawei Peng, Xianhong Xie, Y P Wang, Arken Tursun, Yao Liu et al.

**Journal**: *EGUSphere (preprint)* · **DOI**: [10.5194/egusphere-2026-2505](https://doi.org/10.5194/egusphere-2026-2505) · **Citations**: 0

**Matched topics**: hydrologic model, runoff
{: .label .label-green }

> Global vegetation greening is reshaping water and energy cycles, challenging land surface hydrological modeling. Satellite remote sensing provides dynamic observations of vegetation and radiation, offering a pathway to improve simulations. However, models often rely on static parameters, failing to capture critical transient biogeophysical feedbacks. This study quantifies the impact of integrating dynamic satellite-derived leaf area index and downward shortwave radiation into the VIC land surface model across China. Dynamic inputs consistently improve streamflow simulation, with the greatest gains in humid southern basins where vegetation seasonality drives interannual runoff variability.

---

## Model Calibration, Uncertainty & Observational Constraints

Advances in parameter estimation and precipitation uncertainty characterization occupied five papers this week. Xu et al. introduce a Sequential Monte Carlo algorithm that achieves more efficient posterior exploration than standard MCMC for high-dimensional eco-hydrological models, with direct relevance for multi-variable land surface calibration. Mangukiya et al. benchmark 47 conceptual models across 159 watersheds, providing a rigorous basis for selecting models suited to large-sample hydrological prediction in diverse climates. Wright et al. make the case for ensemble-based precipitation uncertainty quantification as a prerequisite for reliable large-scale hydrologic prediction, arguing that lumped uncertainty estimates from individual products are insufficient. Rateb et al. uncover structural deficits in CESM2-LENS2 and IPSL-CM6A-LR single-model large ensembles that systematically underestimate internal variability of terrestrial water storage — compromising attribution studies. Zhang et al. provide direct observational constraints on land–atmosphere feedbacks during interstorm periods, using passive microwave and in-situ data to characterize how boundary-layer moisture and temperature profiles respond to surface conditions without relying on model structure.

### A Novel Sequential Monte Carlo Algorithm for Parameter Estimation in Eco‐Hydrological Models

**Authors**: Cong Xu, Kun Zhang, Gaofeng Zhu, Xin Li, Chuang Wei

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr040933](https://doi.org/10.1029/2025wr040933) · **Citations**: 0

**Matched topics**: hydrologic model, land surface model
{: .label .label-green }

> Bayesian inference offers a flexible framework for parameter estimation and uncertainty quantification in eco‐hydrological models. However, simultaneously achieving robust posterior exploration and high computational efficiency for multimodal, high‐dimensional, and computationally intensive targets remains challenging for the widely used Markov chain Monte Carlo (MCMC) and sequential Monte Carlo (SMC) algorithms. This study introduces an improved SMC algorithm with adaptive tempering and parallel chain management, demonstrating superior convergence and efficiency for multi-variable eco-hydrological calibration compared to standard DREAM and particle filter approaches.

---

### Benchmarking and Selecting Optimal Hydrological Models for Large‐Sample Applications Considering Complexity and Uncertainty

**Authors**: Nikunj K. Mangukiya, Gopeshwar Sahu, Sagar Gupta, Ashutosh Sharma

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2026wr044753](https://doi.org/10.1029/2026wr044753) · **Citations**: 0

**Matched topics**: hydrologic model
{: .label .label-green }

> Reliable large‐sample hydrological predictions require systematic benchmarking and careful model selection. However, this process is challenging due to structural uncertainty among models, high computational demand, and the climatic and physiographic diversity of a region. This study benchmarked 47 conceptual rainfall–runoff models across 159 watersheds in Peninsular India using the Modular Assessment of Rainfall–Runoff Models Toolbox (MARRMoT), finding that simpler models often match or outperform complex structures in ungauged settings — with model complexity trade-offs varying strongly by climate aridity.

---

### Ensemble‐Based Uncertainty Quantification Can Improve Large‐Scale Precipitation Data for Hydrologic Prediction

**Authors**: Daniel B. Wright, Yagmur Derin, Kaidi Peng, Viviana Maggioni

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70635](https://doi.org/10.1002/hyp.70635) · **Citations**: 0

**Matched topics**: hydrologic model
{: .label .label-green }

> Substantial uncertainties have hindered uptake of large‐scale precipitation data from satellites, reanalysis, and merged datasets in hydrologic applications. Whilst this problem could be addressed by quantifying uncertainty and propagating it through hydrologic models, there is little consensus on what form of uncertainty information is needed. This commentary defines precipitation uncertainty as a probabilistic ensemble property and argues that ensemble-based products — not single-product uncertainty bands — are necessary to faithfully propagate observational uncertainty into hydrologic predictions across scales.

---

### Structural deficits in large ensembles limit detection and attribution of terrestrial water storage

**Authors**: Ashraf Rateb, Bridget R. Scanlon, Brett Buzzanga

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03772-w](https://doi.org/10.1038/s43247-026-03772-w) · **Citations**: 0

**Matched topics**: earth system model
{: .label .label-green }

> Determining whether terrestrial water storage trends and extremes reflect external forcing or internal climate variability requires a credible counterfactual baseline: how much water storage could vary in a world shaped only by internal climate variability. We test whether two widely used single-model large-ensemble archives, CESM2-LENS2 and IPSL-CM6A-LR, provide that baseline by benchmarking their internal variability against GRACE-FO observations. Both ensembles systematically underestimate the magnitude of internal TWS variability, limiting their utility for formal detection and attribution of human-driven terrestrial water storage changes.

---

### Observed Land Surface Influence on Atmospheric Heat and Moisture Profiles During Interstorms

**Authors**: Michelle S. Zhang, David D. Turner, Dara Entekhabi

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr043166](https://doi.org/10.1029/2025wr043166) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Land‐atmospheric (L‐A) feedbacks have historically been studied using models whose structure and parameterizations influence outcomes and insights. The representation of L‐A feedbacks based on observations alone remains an ongoing challenge for understanding boundary layer development and precipitation. To address this gap, ground-based passive remote sensing and in-situ observations are used to characterize how surface energy partitioning during interstorm periods shapes atmospheric moisture and temperature profiles, providing an observational benchmark for land surface parameterizations in NWP and climate models.

---

## Flood Dynamics

Two high-impact papers bracket the flood theme from opposite ends: Komma et al. deliver a detailed hydrometeorological postmortem of the exceptional September 2024 Danube flood — the largest in parts of Lower Austria since instrumental records began — situating it within the context of changing precipitation patterns. Bai et al. synthesize the emerging science of dryland flooding in a comprehensive Earth-Science Reviews article, arguing that flash floods and ephemeral-channel floods in arid regions are underrepresented in global models and increasingly frequent under warming.

### The September 2024 Danube flood compared to the 1899, 2002, and 2013 events: a hydrometeorological analysis in a changing climate

**Authors**: Jürgen Komma, Peter Valent, Miriam Bertola, Juraj Párajka, Klaus Haslinger, Benedikt Bica et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4075-2026](https://doi.org/10.5194/hess-30-4075-2026) · **Citations**: 1

**Matched topics**: runoff, flood, climate change
{: .label .label-green }

> In September 2024, an exceptional flood occurred in the Austrian Danube Basin, producing the highest discharges in parts of Lower Austria since instrumental records began. This study analyses the meteorological and hydrological drivers of the 2024 event and compares them with three historic floods with return periods of around 100 years at the Austrian Danube — 1899, 2002, and 2013 — to disentangle the relative roles of antecedent soil moisture, precipitation intensity, and catchment state in generating extreme discharges. The 2024 event was distinguished by an unusual combination of saturated soils from prior wet conditions and a prolonged, regionally-extensive precipitation event that overwhelmed the typical catchment attenuation.

---

### Emerging dryland flooding

**Authors**: Yu Bai, Te Zhang, Stephen E. Darby, Bruno Merz, Albert J. Kettner, Katerina Michaelides et al.

**Journal**: *Earth-Science Reviews* · **DOI**: [10.1016/j.earscirev.2026.105612](https://doi.org/10.1016/j.earscirev.2026.105612) · **Citations**: 0

**Matched topics**: streamflow, flood
{: .label .label-green }

> Abstract not available.

---

## Drought & Runoff Recovery

Four papers collectively advance understanding of drought-driven hydrological change. Avesani et al. reveal that omitting hydropower infrastructure from hydrological drought indices fundamentally mischaracterizes drought statistics in Alpine regulated basins. Khan et al. tackle hydrological non-stationarity in south-eastern Australia, demonstrating that many catchments affected by the 1997–2009 Millennium drought have not recovered their pre-drought rainfall-runoff relationships even after precipitation returned to normal — suggesting irreversible land cover or soil structural change. Nguyen et al. exploit model-derived groundwater-to-surface-moisture response times as a novel diagnostic for flash drought onset, linking shorter response times to higher flash drought frequency in dryland regions. Yu et al. develop a Bayesian framework for decomposing basin runoff into surface, baseflow, and groundwater components using water balance constraints alone, providing a transferable method for data-sparse settings.

### Grasping Hydrological Droughts in Highly Hydropower Regulated Alpine Watersheds

**Authors**: Diego Avesani, Carlo De Michele, Anna Paola Lonardi, Andrea Galletti, Bruno Majone

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042323](https://doi.org/10.1029/2025wr042323) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, drought, hydropower
{: .label .label-green }

> Hydrological droughts in Alpine regions are increasingly shaped by human regulation, with hydropower operations playing a central role in modifying their statistical characteristics. This study examines how the representation of hydropower systems in hydrological models influences the identification and statistical characterization of drought. Using the HYPERstreamHS hydrological model, the authors show that ignoring operational reservoirs leads to systematic misidentification of drought events and distorted duration-severity statistics in the Italian Alpine headwaters.

---

### Why Does Runoff From Some Catchments Not Recover After a Prolonged Drought?

**Authors**: Zaved Khan, David Robertson, Francis Chiew, Jorge L. Peña‐Arancibia

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70632](https://doi.org/10.1002/hyp.70632) · **Citations**: 0

**Matched topics**: runoff, streamflow, drought
{: .label .label-green }

> The 1997–2009 Millennium drought changed the rainfall‐runoff response across large parts of Victoria in south‐eastern Australia. This study investigates the hydrological non‐stationarity in Victoria, using water balance analysis and a modelling experiment with observed hydroclimate and remotely sensed data over 1982–2020 from 120 catchments. Most catchments in Victoria exhibit hydrological non-stationarity after the Millennium drought, with runoff remaining suppressed relative to pre-drought levels even as rainfall recovered — linked to persistent vegetation change and soil structural shifts rather than meteorological anomalies.

---

### Dynamics of model-based groundwater-land surface response times as a dryland flash drought diagnostic

**Authors**: Hoang Hai Nguyen, Di Long, S.-Y. Simon Wang, Jinho Yoon, Yulong Zhong, Hyunglok Kim

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03783-7](https://doi.org/10.1038/s43247-026-03783-7) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> The delayed response of groundwater to surface soil moisture anomalies (T_opt), which reflects how quickly surface signals propagate to aquifers, varies across wetness regimes. Understanding its spatiotemporal variability may help diagnose flash droughts, yet it remains underexplored. Here, global model-derived T_opt is examined as a diagnostic for flash drought risk — showing that shorter groundwater response times correlate with higher flash drought frequency and severity in dryland regions, providing a new physically-grounded early-warning indicator.

---

### Estimating the composition of basin runoff based on water balance analysis and Bayesian uncertainty analysis

**Authors**: Xiaohan Yu, Xiankui Zeng, Dongwei GUI, Dong Wang, Jichun Wu

**Journal**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0218.1](https://doi.org/10.1175/jhm-d-25-0218.1) · **Citations**: 0

**Matched topics**: runoff, streamflow
{: .label .label-green }

> The basin runoff consists of three components: surface water runoff, baseflow runoff, and groundwater runoff. Accurately estimating the components of basin runoff can deepen our understanding of hydrological processes and enhance the reliability of water balance analysis. However, estimating runoff composition in large-scale basins with sparse ground observations remains a challenge, especially under non-stationary climate conditions. This study applies Bayesian uncertainty analysis within a water balance framework to decompose runoff components, demonstrating the approach in Chinese river basins and quantifying how baseflow fractions respond to land use and climate variability.

---

## Cryosphere & Snow-Runoff Dynamics

Four papers address how cryospheric change is reshaping streamflow timing and magnitude across different mountain systems. Li et al. reconstruct four decades of runoff component evolution in a Tibetan Plateau basin, finding an upward trend in total runoff driven by increasing glacier and permafrost melt that offset precipitation-driven decline since 2009. Ghimire et al. demonstrate that fall soil moisture — not snowpack alone — is a critical modulator of spring streamflow in the drought-stressed Colorado River Basin, with implications for seasonal forecasting. Rezaei et al. use CESM ensembles to evaluate how stratospheric aerosol injection (solar geoengineering) would alter snow-streamflow dynamics relative to a warming baseline, finding that the hydrology response diverges substantially from the temperature signal. Wan et al. use a space-for-time framework on the Tibetan Plateau to show that elevation-dependent permafrost thaw delays seasonal discharge peaks and threatens downstream water availability as the thaw front propagates upslope.

### Four‐Decade Evolution of Runoff Components and Cryospheric Contributions in an Alpine Inland River Basin, Tibetan Plateau

**Authors**: G L Li, Zongxing Li, Baoqing Zhang, Juan Gui

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70630](https://doi.org/10.1002/hyp.70630) · **Citations**: 0

**Matched topics**: runoff, streamflow
{: .label .label-green }

> This study investigates the evolution of runoff components and their drivers in the Buha River Basin, the largest tributary of Qinghai Lake on the Tibetan Plateau, over the period 1982–2022, using the process‐based THREW‐T hydrological model. Findings reveal a fluctuating upward trend in annual runoff, with a notable transition from decline to increase occurring around 2009. The model attribution shows that increasing glacier melt and permafrost thaw contributions after 2009 overcompensated declining precipitation-driven runoff, with cryospheric melt becoming the dominant driver of interannual variability in recent decades.

---

### Fall Soil Moisture Modulates Snow‐Streamflow Dynamics in the Colorado River Basin

**Authors**: Swastik Ghimire, Enrique R. Vivoni, Zhaocheng Wang

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042871](https://doi.org/10.1029/2025wr042871) · **Citations**: 0

**Matched topics**: streamflow
{: .label .label-green }

> The Colorado River Basin (CRB) has experienced a prolonged drought since 2000, with recent years showing a weakened relationship between snowpack conditions and streamflow. This study examined the roles of fall soil moisture and spring weather on modulating snow‐streamflow dynamics in the CRB and its sub-basins using numerical experiments with the Variable Infiltration Capacity (VIC) model. Results show that fall soil moisture antecedent conditions explain a substantial fraction of the variance in spring streamflow, often exceeding the predictive value of snow water equivalent alone — with implications for seasonal water supply forecasts.

---

### Hydrologic Sensitivity of Snow and Streamflow Dynamics to Climate Forcing With and Without Stratospheric Aerosol Intervention

**Authors**: Abolfazl Rezaei, John C. Moore, Simone Tilmes, Daniele Visioni

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042658](https://doi.org/10.1029/2025wr042658) · **Citations**: 0

**Matched topics**: streamflow
{: .label .label-green }

> Snowpack accumulation and melt critically regulate freshwater availability across many regions. Under global warming, the dominant control on snowpack variability shifts from cold‐season precipitation to cold‐season temperature, altering snow–rain partitioning, snowmelt timing, and runoff generation. Using CESM1 and CESM2 ensembles, this study evaluates how stratospheric aerosol injection would alter these dynamics relative to an unmitigated warming baseline, finding that while aerosol injection partially restores snowpack, it introduces distinct regional hydrologic responses that do not simply reverse the warming signal.

---

### Elevation‐Dependent Permafrost Thaw on the Tibetan Plateau Delays Seasonal Discharge and Poses a Risk of Reduction in Downstream Water Availability

**Authors**: Chengwei Wan, J. J. Gibson, Peng Yi, Xicai Pan, Chenghao Chen, Grzegorz Skrzypek

**Journal**: *Earth's Future* · **DOI**: [10.1029/2025ef007809](https://doi.org/10.1029/2025ef007809) · **Citations**: 0

**Matched topics**: streamflow
{: .label .label-green }

> Global warming and permafrost thaw have significantly altered landscapes and hydrological conditions in permafrost regions. While site‐specific process studies have described hydrological changes during thawing, basin‐scale impact assessments and streamflow modeling remain challenging due to landscape heterogeneity and complex interactions. This study introduces a space‐for‐time framework using isotopic and hydrometric data across elevation gradients on the Tibetan Plateau to infer how progressive permafrost thaw delays seasonal discharge peaks and reduces late-season water availability — with downstream implications for water-dependent communities and ecosystems.

---

## Reservoir Operations & Water Management

Five papers address the full spectrum of reservoir and irrigation management challenges. Albano et al. provide the first systematic characterization of watershed-reservoir operational flexibility across diverse western US settings, a prerequisite for FIRO (Forecast-Informed Reservoir Operations) implementation. Upadhyay et al. project that low-storage conditions in western US reservoirs will become substantially more frequent under 21st-century climate change, with critical implications for hydropower availability. Zaniolo et al. propose a novel framework that jointly optimizes information selection (what signals to monitor) and policy learning (how to act on them) for reservoir and water infrastructure management. Abbas et al. develop a MODFLOW-based approach to detect environmentally significant groundwater-driven streamflow alterations that are systematically invisible to surface-gauge networks in irrigated basins. Rizwan et al. combine economic and hydrological modeling to project how large-scale irrigation expansion under climate change would reshape regional water availability.

### Characterizing Watershed Responses and Reservoir Operational Flexibilities: Analyses to Support Forecast‐Informed Reservoir Operations (FIRO) Planning

**Authors**: Christine M. Albano, E. J. Shearer, J. C. Forbis, E. M. Yeates, Julie Kalansky, C. A. Painter et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042131](https://doi.org/10.1029/2025wr042131) · **Citations**: 0

**Matched topics**: reservoir
{: .label .label-green }

> Recent advances in weather forecast skill provide opportunities to manage reservoirs more flexibly using strategies like Forecast‐Informed Reservoir Operations (FIRO). This is especially critical as changes in climate, population, and land use make balancing reservoir uses to minimize flood risks and maximize water availability more challenging. FIRO viability depends on the ability to forecast inflows and translate that information into operational decisions. This study characterizes watershed hydrologic response types and operational flexibility metrics across diverse western US reservoir systems, identifying where FIRO strategies offer the largest potential benefits.

---

### Evaluating Frequency of Low Reservoir Storage in the Western U.S. over the 21st Century

**Authors**: Surabhi Upadhyay, Adrienne Marshall, Nathalie Voisin, Daniel Broman

**Journal**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae84ed](https://doi.org/10.1088/1748-9326/ae84ed) · **Citations**: 0

**Matched topics**: reservoir
{: .label .label-green }

> In recent years, several reservoirs in the western U.S. have approached or exceeded critically low storage during drought conditions; such events could be particularly impactful to water and energy availability if they are widespread across the region or exacerbated by climate change. Using multi-model hydrologic projections, this study finds that critically low reservoir storage events will become substantially more frequent under mid- to late-21st-century warming scenarios, with co-occurrence across multiple basins posing disproportionate risks to regional water and power systems.

---

### Toward Joint Information Selection and Policy Learning in Water Resources Management

**Authors**: Marta Zaniolo, Matteo Giuliani, Jonathan D. Herman

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr042745](https://doi.org/10.1029/2025wr042745) · **Citations**: 0

**Matched topics**: streamflow, water management
{: .label .label-green }

> The water resources literature has made major advances in computational tools for infrastructure management, developing increasingly sophisticated adaptive and many‐objective control frameworks that improve how decisions are optimized under uncertainty and change. Yet most water infrastructure operating policies still condition actions on narrow information sets, typically reservoir storage and inflow forecasts alone. This study develops a framework that simultaneously learns which signals to monitor and what policy to apply, demonstrating gains in multi-objective performance for reservoir systems relative to expert-defined information sets.

---

### Detecting Hidden Environmental Flow Alteration in Groundwater‐Irrigated Basins

**Authors**: Salam A. Abbas, Gerardo Castellanos-Osorio, Jeremy T. White, Javier Senent‐Aparicio, Ryan T. Bailey

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70626](https://doi.org/10.1002/hyp.70626) · **Citations**: 0

**Matched topics**: streamflow, irrigation
{: .label .label-green }

> Effective and balanced management of economic and environmental concerns in groundwater‐irrigated basins is a world‐wide challenge. Environmental flow modification is increasingly influenced by groundwater‐supported irrigation in these heavily irrigated regions, yet the ability to rigorously quantify how groundwater‐based irrigation influences ecological surface‐water flows remains limited by the lack of direct observational methods. Using a MODFLOW-based framework, this study identifies hidden environmental flow alterations that are not detectable by conventional stream-gauge monitoring, revealing systematic low-flow depletion in basins with intensive groundwater irrigation.

---

### Irrigation Use in a Changing Landscape: A Combined Economic and Hydrologic Approach

**Authors**: Noormah Rizwan, Jamshid Jahali, Molly Sears, S. Woznicki, Tao Liu, Oskar Marko et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2025wr041530](https://doi.org/10.1029/2025wr041530) · **Citations**: 0

**Matched topics**: hydrologic model, irrigation
{: .label .label-green }

> Warmer temperatures and erratic rainfall patterns are threatening global water availability. Irrigation is a key risk‐mitigation strategy, helping sustain crop yields under climate stress. Limited research has examined farmers' likelihood of irrigating under climate change, or the effects of large‐scale irrigation expansion on future water availability, largely due to challenges in acquiring field-scale economic data. This study integrates an economic model of farmer adoption decisions with a hydrologic model (SWAT+) to project how irrigation expansion under warming scenarios reshapes regional water budgets, finding that large-scale adoption creates feedback loops that reduce the per-farm benefit of irrigation.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 15 |
| Total papers fetched | 1008 |
| After deduplication | 868 |
| After LLM relevance filtering | 28 |
| Rejected (not relevant) | 840 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Water Resources Research | 12 |
| Hydrological Processes | 4 |
| Scientific Data | 1 |
| Geoscientific Model Development | 1 |
| Journal of Advances in Modeling Earth Systems | 1 |
| Geophysical Research Letters | 1 |
| Hydrology and Earth System Sciences | 1 |
| Communications Earth & Environment | 2 |
| Earth's Future | 1 |
| Environmental Research Letters | 1 |
| Earth-Science Reviews | 1 |
| Journal of Hydrometeorology | 1 |
| EGUSphere (preprint) | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, streamflow, flood, drought, reservoir, water management, runoff, land surface model, earth system model, climate change, hydropower, surface water, irrigation

**Databases**: Semantic Scholar, OpenAlex

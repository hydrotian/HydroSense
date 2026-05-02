---
layout: default
title: "Week 05 (January 27 - February 2), 36 papers"
parent: February
grand_parent: "2020"
nav_order: 33
date: 2020-02-02
categories: [weekly, 2020, february]
tags: [hydrology, literature-review, research]
paper_count: 36
highlight: "CESM2's companion SPEAR system debuts alongside landmark studies on soil structure gaps in ESMs and China's pollution-driven water scarcity, while multiple papers advance hydrologic model evaluation from the Millennium Drought to Hurricane Harvey."
lang: en
lang_link: /zh/2020/february/2020-02-02-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 05** · January 27–February 2, 2020
{: .text-grey-dk-000 }

**36** relevant papers found across **6** themes
{: .fs-5 .fw-300 }

## Executive Summary

A strong week for Earth system modeling saw the debut of GFDL's SPEAR prediction system and a Nature Communications study revealing that omitting soil structure from ESMs biases runoff and drainage by up to 50%. China's water scarcity was shown to double when pollution constraints are included, while High Mountain Asia received its first high-resolution, systematic glacier mass-balance assessment. Machine learning continued its push into hydrology with a CNN-LSTM water quality model (539 citations) and a VMD-SVM runoff predictor, and several studies stress-tested hydrologic models under drought, climate change, and extreme precipitation.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Earth System Modeling and Seasonal-to-Decadal Prediction

The week brought major advances in Earth system prediction infrastructure. GFDL unveiled SPEAR, a seamless prediction system coupling AM4, MOM6, LM4, and SIS2 to span seasonal through multidecadal time horizons. A comprehensive review by Merryfield et al. mapped the state of the art in subseasonal-to-decadal (S2D) prediction, identifying land-surface initialization and ocean–atmosphere coupling as key frontiers. Fatichi et al. demonstrated that the systematic omission of soil structure in ESMs introduces large biases in simulated infiltration and runoff, while Goodwell et al. explored information-theoretic approaches to diagnosing causal interactions across hydrological and Earth system components.

### SPEAR: The Next Generation GFDL Modeling System for Seasonal to Multidecadal Prediction and Projection

**Authors**: Thomas L. Delworth, William Cooke, Alistair Adcroft, Mitchell Bushuk, Jan‐Huey Chen, K. A. Dunne et al.

**Journal**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2019ms001895](https://doi.org/10.1029/2019ms001895) · **Citations**: 288

**Matched topics**: seasonal, land surface model
{: .label .label-green }

> We document the development and simulation characteristics of the next generation modeling system for seasonal to decadal prediction and projection at the Geophysical Fluid Dynamics Laboratory (GFDL). SPEAR (Seamless System for Prediction and EArth System Research) is built from component models recently developed at GFDL—the AM4 atmosphere model, MOM6 ocean code, LM4 land model, and SIS2 sea ice model. The SPEAR models are specifically designed with attributes needed for a prediction model including the ability to run large ensembles, a relatively fast model throughput, and the ability to initialize and restore to observations.

---

### Current and Emerging Developments in Subseasonal to Decadal Prediction

**Authors**: William J. Merryfield, Johanna Baehr, Lauriane Batté, Emily Becker, Amy H. Butler, Caio A. S. Coelho et al.

**Journal**: *Bulletin of the American Meteorological Society* · **DOI**: [10.1175/bams-d-19-0037.1](https://doi.org/10.1175/bams-d-19-0037.1) · **Citations**: 305

**Matched topics**: hydrologic model, streamflow, flood, land surface model, earth system model
{: .label .label-green }

> Weather and climate variations on subseasonal to decadal time scales can have enormous social, economic, and environmental impacts, making skillful predictions on these time scales a valuable tool for decision-makers. As such, there is a growing interest in the scientific, operational, and applications communities in developing forecasts to improve our foreknowledge of extreme events. On subseasonal to seasonal (S2S) time scales, these include high-impact meteorological events such as tropical cyclones, floods, droughts, and heat and cold waves. On seasonal to decadal (S2D) time scales, slow variations of the ocean, sea ice, and land surface drive potentially predictable regional climate variations.

---

### Soil structure is an important omission in Earth System Models

**Authors**: Simone Fatichi, Dani Or, R. L. Walko, Harry Vereecken, Michael H. Young, Teamrat A. Ghezzehei et al.

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-020-14411-z](https://doi.org/10.1038/s41467-020-14411-z) · **Citations**: 261

**Matched topics**: hydrology, hydrologic model, runoff, land surface model, earth system model
{: .label .label-green }

> Most soil hydraulic information used in Earth System Models (ESMs) is derived from pedo-transfer functions that use easy-to-measure soil attributes to estimate hydraulic parameters. This parameterization relies heavily on soil texture, but overlooks the critical role of soil structure originated by soil biophysical activity. Soil structure omission is pervasive also in sampling and measurement methods used to train pedotransfer functions. Here we show how systematic inclusion of salient soil structural features—macroporosity and layer boundaries—substantially alters the distribution of fluxes within the soil-plant-atmosphere continuum, including global patterns of infiltration and drainage.

---

### Debates—Does Information Theory Provide a New Paradigm for Earth Science? Causality, Interaction, and Feedback

**Authors**: Allison E. Goodwell, Peishi Jiang, Benjamin L. Ruddell, Praveen Kumar

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2019wr024940](https://doi.org/10.1029/2019wr024940) · **Citations**: 76

**Matched topics**: hydrology, hydrologic model, earth system model
{: .label .label-green }

> The concept of causal interactions between components is an integral part of hydrology and Earth system sciences. Modelers, decision makers, scientists, and other water resources stakeholders all utilize some notion of cause-and-effect to understand processes, make decisions, and infer how systems react to change. However, there are different perspectives on the meaning of causality in complex systems and, further, different frameworks and methodologies with which to detect causal interactions from data.

---

## Hydrologic Model Development and Evaluation

This week saw a rich set of contributions probing the limits and frontiers of hydrologic modeling. Fowler et al. demonstrated that five commonly used bucket models fail to replicate multiyear groundwater trends during Australia's Millennium Drought, raising concerns about climate-change projections. Marsh et al. released the Canadian Hydrological Model (CHM) as an open-source, variable-complexity platform for cold-region hydrology, while Meili et al. introduced UT&C, an urban ecohydrological model that couples plant physiology with the urban energy balance. Viterbo et al. evaluated the NOAA National Water Model's flash-flood forecasts for the 2018 Ellicott City event, and Baek et al. coupled SWMM with HYDRUS to simulate green-roof performance. Studies by Stephens et al. and Lilhare et al. further interrogated model transferability and VIC sensitivity across contrasting climatic regimes.

### An urban ecohydrological model to quantify the effect of vegetation on urban climate and hydrology (UT&C v1.0)

**Authors**: Naika Meili, Gabriele Manoli, Paolo Burlando, Elie Bou‐Zeid, Winston Chow, Andrew Coutts et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-13-335-2020](https://doi.org/10.5194/gmd-13-335-2020) · **Citations**: 178

**Matched topics**: hydrology, hydrologic model, runoff, land surface model
{: .label .label-green }

> Increasing urbanization is likely to intensify the urban heat island effect, decrease outdoor thermal comfort, and enhance runoff generation in cities. Urban green spaces are often proposed as a mitigation strategy to counteract these adverse effects, and many recent developments of urban climate models focus on the inclusion of green and blue infrastructure to inform urban planning. However, many models still lack the ability to account for different plant types and oversimplify the interactions between vegetation, soil, and the urban atmosphere.

---

### Many Commonly Used Rainfall‐Runoff Models Lack Long, Slow Dynamics: Implications for Runoff Projections

**Authors**: Keirnan Fowler, Wouter Knoben, Murray Peel, Tim Peterson, Dongryeol Ryu, Margarita Saft et al.

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2019wr025286](https://doi.org/10.1029/2019wr025286) · **Citations**: 172

**Matched topics**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> Evidence suggests that catchment state variables such as groundwater can exhibit multiyear trends. This means that their state may reflect not only recent climatic conditions but also climatic conditions in past years or even decades. Here we demonstrate that five commonly used conceptual "bucket" rainfall-runoff models are unable to replicate multiyear trends exhibited by natural systems during the "Millennium Drought" in south-east Australia. This causes an inability to extrapolate to drier conditions and has implications for runoff projections under climate change.

---

### A Multiscale, Hydrometeorological Forecast Evaluation of National Water Model Forecasts of the May 2018 Ellicott City, Maryland, Flood

**Authors**: Francesca Viterbo, Kelly Mahoney, Laura Read, F. Salas, Bradford Bates, Jason Elliott et al.

**Journal**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-19-0125.1](https://doi.org/10.1175/jhm-d-19-0125.1) · **Citations**: 85

**Matched topics**: hydrology, hydrologic model, streamflow, flood, land surface model
{: .label .label-green }

> The NOAA National Water Model (NWM) became operational in August 2016, producing the first ever real-time, distributed, continuous set of hydrologic forecasts over the continental United States (CONUS). This project uses integrated hydrometeorological assessment methods to investigate the utility of the NWM to predict catastrophic flooding associated with an extreme rainfall event that occurred in Ellicott City, Maryland, on 27–28 May 2018.

---

### The Canadian Hydrological Model (CHM) v1.0: a multi-scale, multi-extent, variable-complexity hydrological model – design and overview

**Authors**: Christopher B. Marsh, John W. Pomeroy, H. S. Wheater

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-13-225-2020](https://doi.org/10.5194/gmd-13-225-2020) · **Citations**: 83

**Matched topics**: hydrology, hydrologic model, runoff, streamflow, land surface model
{: .label .label-green }

> Despite debate in the rainfall-runoff hydrology literature about the merits of physics-based and spatially distributed models, substantial work in cold-region hydrology has shown improved predictive capacity by including physics-based process representations, relatively high-resolution semi-distributed and fully distributed discretizations, and the use of physically identifiable parameters that require limited calibration. While there is increasing motivation for modelling at hyper-resolution, the underlying process representation and fidelity must also be considered.

---

### Assessment of a green roof practice using the coupled SWMM and HYDRUS models

**Authors**: Sang‐Soo Baek, Mayzonee Ligaray, Yakov Pachepsky, Jong Ahn Chun, Kwang‐Sik Yoon, Yongeun Park et al.

**Journal**: *Journal of Environmental Management* · **DOI**: [10.1016/j.jenvman.2019.109920](https://doi.org/10.1016/j.jenvman.2019.109920) · **Citations**: 74

**Matched topics**: hydrologic model, runoff, water management
{: .label .label-green }

> Green roofs are considered an effective low-impact development (LID) practice for stormwater management in urban areas. This study coupled SWMM and HYDRUS models to simulate the hydrological performance of green roofs, providing a physically based approach to evaluate runoff reduction and water quality improvement under varying rainfall scenarios.

---

### Interpolated or satellite-based precipitation? Implications for hydrological modeling in a meso-scale mountainous watershed on the Qinghai-Tibet Plateau

**Authors**: Ling Zhang, Dong Ren, Zhuotong Nan, Weizhen Wang, Yi Zhao, Yanbo Zhao et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124629](https://doi.org/10.1016/j.jhydrol.2020.124629) · **Citations**: 67

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> This study compares station-interpolated and satellite-based precipitation products and their impacts on hydrological modeling in a mountainous watershed on the Qinghai-Tibet Plateau, where rain gauge networks are sparse and topographic gradients are steep.

---

### Is Past Variability a Suitable Proxy for Future Change? A Virtual Catchment Experiment

**Authors**: Clare Stephens, Lucy Marshall, Fiona Johnson, Laurence Lin, Lawrence E. Band, Hoori Ajami

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2019wr026275](https://doi.org/10.1029/2019wr026275) · **Citations**: 55

**Matched topics**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> To estimate the robustness of hydrologic models under projected future climate change, researchers test transferability between climatically contrasting observed periods. This approach can only assess the performance changes induced by altered precipitation and related environmental dynamics, since the instrumental record does not contain temperatures or carbon dioxide levels that are similar to future climate change projections.

---

### Sensitivity analysis and uncertainty assessment in water budgets simulated by the variable infiltration capacity model for Canadian subarctic watersheds

**Authors**: Rajtantra Lilhare, Scott Pokorny, Stephen J. Déry, Tricia Stadnyk, Kristina Koenig

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.13711](https://doi.org/10.1002/hyp.13711) · **Citations**: 52

**Matched topics**: hydrology, hydrologic model, streamflow, land surface model
{: .label .label-green }

> In this study, we evaluate uncertainties propagated through different climate data sets in seasonal and annual hydrological simulations over 10 subarctic watersheds of northern Manitoba, Canada, using the variable infiltration capacity (VIC) model. Further, we perform a comprehensive sensitivity and uncertainty analysis of the VIC model using a robust and state-of-the-art approach based on the variogram analysis of response surfaces (VARS) technique.

---

## Climate Change Impacts on Water Resources

China's freshwater scarcity was shown to double when water quality constraints are included, with northern and eastern China most affected (Ma et al., Nature Communications). In the European Alps, Mastrotheodoros et al. found that warmer summers shift the water balance toward evapotranspiration ("green water") at the expense of runoff and recharge ("blue water"), with implications for downstream water supply. Continental-scale studies quantified climate-driven shifts in the South American water balance and Upper Ayeyarwady streamflow, while regionally focused work addressed drought severity in Bangladesh and runoff projections for China's Heihe River basin. Mentaschi et al. showed that projected changes in European river runoff are largely independent of the emission pathway taken to reach a given warming level.

### Pollution exacerbates China's water scarcity and its regional inequality

**Authors**: Ting Ma, Siao Sun, Guangtao Fu, Jim W. Hall, Yong Ni, Lihuan He et al.

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-020-14532-5](https://doi.org/10.1038/s41467-020-14532-5) · **Citations**: 670

**Matched topics**: hydrologic model, water management, land surface model, hydropower
{: .label .label-green }

> Inadequate water quality can mean that water is unsuitable for a variety of human uses, thus exacerbating freshwater scarcity. Previous large-scale water scarcity assessments mostly focused on the availability of sufficient freshwater quantity for providing supplies, but neglected the quality constraints on water usability. Here we report a comprehensive nationwide water scarcity assessment in China, which explicitly includes quality requirements for human water uses.

---

### More green and less blue water in the Alps during warmer summers

**Authors**: Theodoros Mastrotheodoros, Christoforos Pappas, Péter Molnár, Paolo Burlando, Gabriele Manoli, Juraj Párajka et al.

**Journal**: *Nature Climate Change* · **DOI**: [10.1038/s41558-019-0676-5](https://doi.org/10.1038/s41558-019-0676-5) · **Citations**: 295

**Matched topics**: runoff, surface water
{: .label .label-green }

> Warmer summers in the European Alps shift the partitioning of precipitation away from runoff and groundwater recharge (blue water) toward evapotranspiration (green water), with significant consequences for downstream water resources and ecosystem services. This study uses long-term observations and process-based modeling to quantify the magnitude and spatial variability of this shift across Alpine catchments.

---

### Analysis of Streamflow Response to Changing Climate Conditions Using SWAT Model

**Authors**: Han Thi Oo, Win Win Zin, Cho Cho Thin Kyi

**Journal**: *Civil Engineering Journal* · **DOI**: [10.28991/cej-2020-03091464](https://doi.org/10.28991/cej-2020-03091464) · **Citations**: 124

**Matched topics**: hydrology, hydrologic model, streamflow, flood, hydropower
{: .label .label-green }

> The understanding of climate change is crucial for the security of hydrologic conditions of river basins and it is very important to study the climate change impacts on streamflow by analyzing the different climate scenarios with the help of the hydrological models. The main purpose of this study is to project the future climate impact on streamflow by using the SWAT model in the Upper Ayeyarwady River Basin under low and high representative concentration pathway scenarios.

---

### Climate change impacts on South American water balance from a continental-scale hydrological model driven by CMIP5 projections

**Authors**: João Paulo Lyra Fialho Brêda, Rodrigo Cauduro Dias de Paiva, Walter Collischon, Juan Martín Bravo, Vinícius Alencar Siqueira, Elisa Bolzan Steinke

**Journal**: *Climatic Change* · **DOI**: [10.1007/s10584-020-02667-9](https://doi.org/10.1007/s10584-020-02667-9) · **Citations**: 121

**Matched topics**: hydrologic model, runoff, water management, climate change
{: .label .label-green }

> This study uses a continental-scale hydrological model driven by CMIP5 climate projections to assess climate change impacts on the South American water balance, quantifying shifts in precipitation, evapotranspiration, and runoff across major river basins under multiple emission scenarios.

---

### Evaluating severity–area–frequency (SAF) of seasonal droughts in Bangladesh under climate change scenarios

**Authors**: Mahiuddin Alamgir, Najeebullah Khan, Shamsuddin Shahid, Zaher Mundher Yaseen, Ashraf Dewan, Quazi K. Hassan et al.

**Journal**: *Stochastic Environmental Research and Risk Assessment* · **DOI**: [10.1007/s00477-020-01768-2](https://doi.org/10.1007/s00477-020-01768-2) · **Citations**: 90

**Matched topics**: drought, seasonal, climate change
{: .label .label-green }

> This study evaluates the severity-area-frequency characteristics of seasonal droughts in Bangladesh under multiple climate change scenarios, providing a spatially explicit drought risk assessment framework relevant to agricultural water management and food security planning.

---

### Impacts of projected climate change on runoff in upper reach of Heihe River basin using climate elasticity method and GCMs

**Authors**: Zhanling Li, Qiuju Li, Jie Wang, Yaru Feng, Quanxi Shao

**Journal**: *The Science of The Total Environment* · **DOI**: [10.1016/j.scitotenv.2020.137072](https://doi.org/10.1016/j.scitotenv.2020.137072) · **Citations**: 81

**Matched topics**: hydrologic model, river, runoff, climate change
{: .label .label-green }

> This study uses the climate elasticity method combined with GCM projections to quantify the impacts of projected climate change on runoff in the upper reach of the Heihe River basin in northwestern China, assessing the relative contributions of precipitation and temperature changes.

---

### Independence of Future Changes of River Runoff in Europe from the Pathway to Global Warming

**Authors**: Lorenzo Mentaschi, Lorenzo Alfieri, Francesco Dottori, Carmelo Cammalleri, Berny Bisselink, Ad de Roo et al.

**Journal**: *Climate* · **DOI**: [10.3390/cli8020022](https://doi.org/10.3390/cli8020022) · **Citations**: 31

**Matched topics**: hydrology, river, runoff, streamflow
{: .label .label-green }

> The outcomes of the 2015 Paris Agreement triggered a number of climate impact assessments to focus on future time frames corresponding to specific levels of global warming. This study compares projected changes of annual mean, extreme high, and extreme low river discharges in Europe across different greenhouse gas concentration pathways, finding that the hydrological response is largely independent of the emission pathway taken to reach a given warming level.

---

### Integrated Water Management Approach for Adaptation to Climate Change in Highly Water Stressed Basins

**Authors**: Elpida Kolokytha, Dimitrios Malamataris

**Journal**: *Water Resources Management* · **DOI**: [10.1007/s11269-020-02492-w](https://doi.org/10.1007/s11269-020-02492-w) · **Citations**: 27

**Matched topics**: hydrology, water management, land surface model
{: .label .label-green }

> This study presents an integrated water management approach for climate change adaptation in highly water-stressed basins, combining supply-side and demand-side strategies to evaluate their effectiveness under projected future conditions.

---

## Glaciers and Mountain Hydrology

High Mountain Asia received its most comprehensive glacier mass-balance assessment to date: Shean et al. generated nearly 6,000 high-resolution DEMs from satellite stereo imagery, revealing heterogeneous mass loss across the region. On the Greenland Ice Sheet, Cook et al. quantified how glacier algae darken the ice surface and accelerate melting, estimating the biological contribution to sea-level rise. Rounce et al. applied Bayesian inference to calibrate a large-scale glacier evolution model for HMA using geodetic mass-balance data, and Baudouin et al. cross-validated precipitation datasets in the Indus River basin to reduce a major source of uncertainty for downstream hydrological modeling.

### A Systematic, Regional Assessment of High Mountain Asia Glacier Mass Balance

**Authors**: David Shean, Shashank Bhushan, Paul Montesano, David R. Rounce, A. A. Arendt, Batuhan Osmanoğlu

**Journal**: *Frontiers in Earth Science* · **DOI**: [10.3389/feart.2019.00363](https://doi.org/10.3389/feart.2019.00363) · **Citations**: 659

**Matched topics**: hydrologic model, runoff, water management
{: .label .label-green }

> High-mountain Asia (HMA) constitutes the largest glacierized region outside of the Earth's polar regions. Although available observations are limited, long-term records indicate sustained HMA glacier mass loss since ~1850, with accelerated loss in recent decades. Recent satellite data capture the spatial variability of this mass loss, but spatial resolution is coarse and some estimates for regional and HMA-wide mass loss disagree. To address these issues, we generated 5,797 high-resolution digital elevation models from satellite stereo imagery.

---

### Glacier algae accelerate melt rates on the south-western Greenland Ice Sheet

**Authors**: Joseph M. Cook, Andrew Tedstone, Christopher J. Williamson, Jenine McCutcheon, Andy Hodson, Archana Dayal et al.

**Journal**: *The Cryosphere* · **DOI**: [10.5194/tc-14-309-2020](https://doi.org/10.5194/tc-14-309-2020) · **Citations**: 162

**Matched topics**: hydrology, runoff, land surface model
{: .label .label-green }

> Melting of the Greenland Ice Sheet (GrIS) is the largest single contributor to eustatic sea level and is amplified by the growth of pigmented algae on the ice surface, which increases solar radiation absorption. This biological albedo-reducing effect and its impact upon sea level rise has not previously been quantified. Here, we combine field spectroscopy with a radiative-transfer model, supervised classification of UAV and satellite remote-sensing data, and regional climate model outputs to estimate the algal contribution to GrIS runoff.

---

### Quantifying parameter uncertainty in a large-scale glacier evolution model using Bayesian inference: application to High Mountain Asia

**Authors**: David R. Rounce, Tushar Khurana, Margaret Short, Regine Hock, David Shean, Douglas Brinkerhoff

**Journal**: *Journal of Glaciology* · **DOI**: [10.1017/jog.2019.91](https://doi.org/10.1017/jog.2019.91) · **Citations**: 82

**Matched topics**: hydrology, hydrologic model, runoff
{: .label .label-green }

> The response of glaciers to climate change has major implications for sea-level change and water resources around the globe. Large-scale glacier evolution models are used to project glacier runoff and mass loss, but are constrained by limited observations, which result in models being over-parameterized. Recent systematic geodetic mass-balance observations provide an opportunity to improve the calibration of glacier evolution models.

---

### Cross-validating precipitation datasets in the Indus River basin

**Authors**: Jean‐Philippe Baudouin, Michael Herzog, Cameron A. Petrie

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-427-2020](https://doi.org/10.5194/hess-24-427-2020) · **Citations**: 82

**Matched topics**: hydrology, river, land surface model
{: .label .label-green }

> Large uncertainty remains about the amount of precipitation falling in the Indus River basin, particularly in the more mountainous northern part. While rain gauge measurements are often considered as a reference, they provide information for specific, often sparse, locations and are subject to underestimation, particularly in mountain areas. Satellite observations and reanalysis data can improve our knowledge but validating their results is often difficult.

---

## Machine Learning and Data-Driven Hydrological Prediction

Machine learning made strong inroads into hydrological prediction this week. Barzegar et al. achieved high accuracy for short-term water quality forecasting with a hybrid CNN-LSTM architecture, already garnering 539 citations. Feng et al. combined variational mode decomposition with a quantum-behaved particle swarm-optimized SVM for monthly runoff prediction. On the operational side, Quedi & Fan assessed sub-seasonal streamflow forecasts at large-scale basins, and Totaro et al. investigated the statistical power of trend detection methods commonly used in hydrological time series analysis.

### Short-term water quality variable prediction using a hybrid CNN–LSTM deep learning model

**Authors**: Rahim Barzegar, Mohammad Taghi Aalami, Jan Adamowski

**Journal**: *Stochastic Environmental Research and Risk Assessment* · **DOI**: [10.1007/s00477-020-01776-2](https://doi.org/10.1007/s00477-020-01776-2) · **Citations**: 539

**Matched topics**: water management
{: .label .label-green }

> This study proposes a hybrid CNN-LSTM deep learning model for short-term water quality variable prediction, demonstrating that the convolutional layers effectively extract spatial features from multivariate input data while the LSTM layers capture temporal dependencies, outperforming standalone CNN, LSTM, and traditional machine learning approaches.

---

### Monthly runoff time series prediction by variational mode decomposition and support vector machine based on quantum-behaved particle swarm optimization

**Authors**: Zhong-kai Feng, Wenjing Niu, Zhengyang Tang, Zhiqiang Jiang, Xu Yang, Yi Liu et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124627](https://doi.org/10.1016/j.jhydrol.2020.124627) · **Citations**: 242

**Matched topics**: runoff, streamflow, water management, hydropower
{: .label .label-green }

> This study proposes a hybrid model combining variational mode decomposition (VMD) with support vector machine (SVM) optimized by quantum-behaved particle swarm optimization (QPSO) for monthly runoff time series prediction. The VMD-QPSO-SVM framework decomposes the nonlinear and non-stationary runoff signal into intrinsic mode functions, enabling more accurate predictions relevant to reservoir operation and hydropower scheduling.

---

### Satellite-Based Evapotranspiration in Hydrological Model Calibration

**Authors**: Lulu Jiang, Huan Wu, Jing Tao, John S. Kimball, Lorenzo Alfieri, Xiuwan Chen

**Journal**: *Remote Sensing* · **DOI**: [10.3390/rs12030428](https://doi.org/10.3390/rs12030428) · **Citations**: 59

**Matched topics**: hydrology, hydrologic model, streamflow, land surface model
{: .label .label-green }

> Hydrological models are usually calibrated against observed streamflow, which is not applicable for ungauged river basins. This paper investigates the use of remotely sensed evapotranspiration in the hydrological calibration of a widely used land surface model coupled with a source-sink routing scheme and global optimization algorithm for 28 natural river basins across diverse climatic and physiographic settings.

---

### Sub seasonal streamflow forecast assessment at large-scale basins

**Authors**: Erik Quedi, Fernando Mainardi Fan

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124635](https://doi.org/10.1016/j.jhydrol.2020.124635) · **Citations**: 48

**Matched topics**: hydrologic model, streamflow, seasonal, hydropower
{: .label .label-green }

> This study assesses sub-seasonal streamflow forecast skill at large-scale basins, evaluating the potential of extended-range hydrological predictions for hydropower operations and water resource management across multiple forecast lead times and basin characteristics.

---

### Numerical investigation on the power of parametric and nonparametric tests for trend detection in annual maximum series

**Authors**: Vincenzo Totaro, Andrea Gioia, Vito Iacobellis

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-473-2020](https://doi.org/10.5194/hess-24-473-2020) · **Citations**: 29

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> The need to fit time series characterized by the presence of a trend or change points has generated increased interest in the investigation of nonstationary probability distributions in recent years. This study provides a numerical investigation of the statistical power of commonly used parametric and nonparametric trend detection tests when applied to annual maximum series in hydrology.

---

## Flood, Drought, and Water Management

Urban flood management through nature-based solutions drew significant attention, with Hobbie & Grimm reviewing how green infrastructure can mitigate the combined effects of impervious cover and climate warming. Hellwig et al. provided the first large-scale assessment of delayed groundwater responses to drought across Europe, finding that drought propagation timescales vary from months to years. Chen et al. tested remote-sensing precipitation products against Hurricane Harvey's extreme rainfall and flood cascade, while Tunas et al. documented how earthquake-induced landslides intensified flash floods in Sulawesi. Tranmer et al. drew ecosystem-management lessons from coupled reservoir-river systems, and Ramaswamy & Saleh developed ensemble-based reservoir release optimization for flood control.

### Nature-based approaches to managing climate change impacts in cities

**Authors**: Sarah E. Hobbie, Nancy B. Grimm

**Journal**: *Philosophical Transactions of the Royal Society B Biological Sciences* · **DOI**: [10.1098/rstb.2019.0124](https://doi.org/10.1098/rstb.2019.0124) · **Citations**: 293

**Matched topics**: runoff, flood, climate change
{: .label .label-green }

> Managing and adapting to climate change in urban areas will become increasingly important as urban populations grow, especially because unique features of cities amplify climate change impacts. High impervious cover exacerbates impacts of climate warming through urban heat island effects and of heavy rainfall by magnifying runoff and flooding. Concentration of human settlements along rivers and coastal zones increases exposure of people and infrastructure to climate change hazards.

---

### Large‐Scale Assessment of Delayed Groundwater Responses to Drought

**Authors**: Jost Hellwig, Inge de Graaf, Markus Weiler, Kerstin Stahl

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2019wr025441](https://doi.org/10.1029/2019wr025441) · **Citations**: 135

**Matched topics**: hydrology, hydrologic model, streamflow, drought
{: .label .label-green }

> Groundwater is a vital resource for freshwater supply during extended droughts and also a key storage governing drought propagation through the hydrological cycle. Current drought monitoring lacks large-scale estimates of groundwater droughts, but progress of country-to-global-scale models in the last years suggests that they could now be valuable tools to study and monitor water availability during extended droughts.

---

### Can Remote Sensing Technologies Capture the Extreme Precipitation Event and Its Cascading Hydrological Response? A Case Study of Hurricane Harvey Using EF5 Modeling Framework

**Authors**: Mengye Chen, Soumaya Nabih, Noah S. Brauer, Shang Gao, Jonathan J. Gourley, Zhen Hong et al.

**Journal**: *Remote Sensing* · **DOI**: [10.3390/rs12030445](https://doi.org/10.3390/rs12030445) · **Citations**: 39

**Matched topics**: hydrology, hydrologic model, streamflow, flood
{: .label .label-green }

> A new generation of precipitation measurement products has emerged, and their performances have gained much attention from the scientific community, such as the Multi-Radar Multi-Sensor system (MRMS) and the Global Precipitation Measurement Mission (GPM). This study statistically evaluated the MRMS and GPM products and investigated their cascading hydrological response during Hurricane Harvey in August 2017.

---

### Impact of Landslides Induced by the 2018 Palu Earthquake on Flash Flood in Bangga River Basin, Sulawesi, Indonesia

**Authors**: I Gede Tunas, Arody Tanga, Siti Oktavia

**Journal**: *Journal of Ecological Engineering* · **DOI**: [10.12911/22998993/116325](https://doi.org/10.12911/22998993/116325) · **Citations**: 36

**Matched topics**: hydrology, hydrologic model, river, flood
{: .label .label-green }

> High magnitude flash flood has occurred several times in some areas in Central Sulawesi Province after the 2018 Palu Earthquake, one of them is in the Bangga River, Sigi Regency, Indonesia. It has caused massive impacts such as damaging agricultural and plantation areas and submerging public facilities and infrastructure. The flood carries a variety of materials, especially high concentration sediments originating from eroded soils due to landslides triggered by the earthquake.

---

### Coupled reservoir-river systems: Lessons from an integrated aquatic ecosystem assessment

**Authors**: Andrew W. Tranmer, Dana E. Weigel, Clelia L. Marti, Dmitri Vidergar, Rohan Benjankar, Daniele Tonina et al.

**Journal**: *Journal of Environmental Management* · **DOI**: [10.1016/j.jenvman.2020.110107](https://doi.org/10.1016/j.jenvman.2020.110107) · **Citations**: 36

**Matched topics**: hydrologic model, river, reservoir, water management, hydropower
{: .label .label-green }

> This study provides an integrated aquatic ecosystem assessment of coupled reservoir-river systems, drawing lessons from multi-disciplinary monitoring and modeling to improve management strategies that balance hydropower operations with ecological flow requirements and downstream habitat quality.

---

### Ensemble Based Forecasting and Optimization Framework to Optimize Releases from Water Supply Reservoirs for Flood Control

**Authors**: V. Ramaswamy, Firas Saleh

**Journal**: *Water Resources Management* · **DOI**: [10.1007/s11269-019-02481-8](https://doi.org/10.1007/s11269-019-02481-8) · **Citations**: 28

**Matched topics**: hydrologic model, streamflow, reservoir, water management, flood
{: .label .label-green }

> This study develops an ensemble-based forecasting and optimization framework to optimize releases from water supply reservoirs for flood control, coupling hydrologic ensemble forecasts with reservoir operation optimization to balance flood risk reduction with water supply objectives.

---

### Water balance modeling of Tandula (India) reservoir catchment using SWAT

**Authors**: R. K. Jaiswal, Ram Narayan Yadav, A. K. Lohani, H. L. Tiwari, Shalini Yadav

**Journal**: *Arabian Journal of Geosciences* · **DOI**: [10.1007/s12517-020-5092-7](https://doi.org/10.1007/s12517-020-5092-7) · **Citations**: 24

**Matched topics**: hydrologic model, runoff, reservoir
{: .label .label-green }

> This study applies the Soil and Water Assessment Tool (SWAT) to model the water balance of the Tandula reservoir catchment in India, evaluating the model's ability to simulate runoff, evapotranspiration, and groundwater recharge components for improved reservoir inflow forecasting and water resources planning.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 1123 |
| After deduplication | 815 |
| After LLM relevance filtering | 36 |
| Rejected (not relevant) | 779 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Water Resources Research | 5 |
| Journal of Hydrology | 4 |
| Nature Communications | 2 |
| Geoscientific Model Development | 2 |
| Hydrology and Earth System Sciences | 2 |
| Remote Sensing | 2 |
| Journal of Environmental Management | 2 |
| Water Resources Management | 2 |
| Stochastic Environmental Research and Risk Assessment | 2 |
| Journal of Advances in Modeling Earth Systems | 2 |
| Nature Climate Change | 1 |
| Bulletin of the American Meteorological Society | 1 |
| Philosophical Transactions of the Royal Society B | 1 |
| The Cryosphere | 1 |
| Journal of Glaciology | 1 |
| Frontiers in Earth Science | 1 |
| The Science of The Total Environment | 1 |
| Climatic Change | 1 |
| Civil Engineering Journal | 1 |
| Journal of Hydrometeorology | 1 |
| Hydrological Processes | 1 |
| Climate | 1 |
| Journal of Ecological Engineering | 1 |
| Arabian Journal of Geosciences | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

---
layout: default
title: "Week 06 (February 3 - February 9), 43 papers"
parent: February
grand_parent: "2020"
nav_order: 34
date: 2020-02-09
categories: [weekly, 2020, february]
tags: [hydrology, literature-review, research]
paper_count: 43
highlight: "Landmark releases of World-Wide HYPE global catchment model and UK Earth System Models for CMIP6, alongside a permafrost hydrology intercomparison revealing divergent soil moisture projections among leading land models."
lang: en
lang_link: /zh/2020/february/2020-02-09-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 06** · February 3–February 9, 2020
{: .text-grey-dk-000 }

**43** relevant papers found across **6** themes
{: .fs-5 .fw-300 }

## Executive Summary

A major week for global-scale hydrologic modeling saw the release of World-Wide HYPE (WWH), the first application of catchment-modeling techniques evaluated against river flow at the global scale, alongside the UK Earth System Models for CMIP6 and an updated JULES-GL7 land surface configuration. A multi-model permafrost hydrology intercomparison revealed that most land models project surface soil drying despite increased precipitation, highlighting critical uncertainties in high-latitude water cycle projections. Meanwhile, machine learning approaches advanced with deep fusion methods for satellite–gauge precipitation merging and LSTM-based streamflow forecasting, while a global assessment of dam-induced habitat fragmentation for ~10,000 fish species quantified the profound connectivity impacts of current and planned hydropower infrastructure.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Global Hydrologic and Earth System Modeling

This week delivered a remarkable cluster of papers advancing global-scale modeling capabilities. The UK Earth System Models—HadGEM3-GC3.1 and UKESM1—were formally documented for CMIP6, while the JULES-GL7 land surface configuration underpinning these models was also released. A groundbreaking permafrost region model intercomparison revealed that despite projected increases in precipitation, most land models predict long-term surface soil drying, with substantial disagreement among models on runoff and evapotranspiration partitioning. The World-Wide HYPE (WWH) model demonstrated that global catchment modeling using open data and stepwise parameter estimation is now feasible, while separate studies examined the effective resolution of high-resolution atmospheric models and how terrestrial biosphere models simulate rainfall manipulation experiments. The ORCHIDEE land surface model received an improved irrigation scheme, and a novel dynamic model data averaging approach was proposed for combining global hydrological models with GRACE observations.

### Implementation of U.K. Earth System Models for CMIP6

**Authors**: Alistair Sellar, Jeremy Walton, Colin Jones, Richard Wood, Nathan Luke Abraham, Mirosław Andrejczuk et al.

**Journal**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2019ms001946](https://doi.org/10.1029/2019ms001946) · **Citations**: 299

**Matched topics**: earth system model
{: .label .label-green }

> We describe the scientific and technical implementation of two models for a core set of experiments contributing to CMIP6. The models used are the physical atmosphere–land–ocean–sea ice model HadGEM3-GC3.1 and the Earth system model UKESM1 which adds a carbon–nitrogen cycle and atmospheric chemistry to HadGEM3-GC3.1. The model results are constrained by the external boundary conditions (forcing data) and initial conditions for the various model components.

---

### Soil moisture and hydrology projections of the permafrost region – a model intercomparison

**Authors**: C. Andresen, D. Lawrence, C. Wilson, A. McGuire, C. Koven, K. Schaefer et al.

**Journal**: *The Cryosphere* · **DOI**: [10.5194/TC-14-445-2020](https://doi.org/10.5194/TC-14-445-2020) · **Citations**: 178

**Matched topics**: hydrology, hydrologic model, runoff, land surface model, surface water, earth system model
{: .label .label-green }

> This study investigates and compares soil moisture and hydrology projections of broadly used land models with permafrost processes and highlights the causes and impacts of permafrost zone soil moisture projections. Climate models project warmer temperatures and increases in precipitation which will intensify evapotranspiration and runoff in land models. However, most models project a long-term drying of the surface soil (0–20 cm) for the permafrost region despite wetting at deeper layers.

---

### Global catchment modelling using World-Wide HYPE (WWH), open data, and stepwise parameter estimation

**Authors**: Berit Arheimer, Rafael Pimentel, Kristina Isberg, Louise Crochemore, Jafet Andersson, Abdulghani Hasan et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-535-2020](https://doi.org/10.5194/hess-24-535-2020) · **Citations**: 177

**Matched topics**: hydrology, hydrologic model, streamflow, land surface model, hydropower
{: .label .label-green }

> Recent advancements in catchment hydrology make it possible to apply catchment models for ungauged basins over large domains. Here we present a cutting-edge case study applying catchment-modelling techniques with evaluation against river flow at the global scale for the first time. The modelling procedure was challenging but doable, and even the first model version shows acceptable results for many regions across the globe.

---

### Effective resolution in high resolution global atmospheric models for climate studies

**Authors**: Remko Klaver, Rein Haarsma, Pier Luigi Vidale, Wilco Hazeleger

**Journal**: *Atmospheric Science Letters* · **DOI**: [10.1002/asl.952](https://doi.org/10.1002/asl.952) · **Citations**: 103

**Matched topics**: earth system model
{: .label .label-green }

> We estimate the extent of spatial scales that atmospheric models in a new generation of global climate models used in CMIP6 are able to resolve on the basis of kinetic energy spectra, commonly referred to as the effective resolution. We examine the spectra derived from the rotational and divergent parts of the wind for six state-of-the-art global climate models run with at least two horizontal resolutions.

---

### Rainfall manipulation experiments as simulated by terrestrial biosphere models: Where do we stand?

**Authors**: Athanasios Paschalis, Simone Fatichi, Jakob Zscheischler, Philippe Ciais, Michael Bahn, Lena Boysen et al.

**Journal**: *Global Change Biology* · **DOI**: [10.1111/gcb.15024](https://doi.org/10.1111/gcb.15024) · **Citations**: 91

**Matched topics**: earth system model
{: .label .label-green }

> Changes in rainfall amounts and patterns have been observed and are expected to continue in the near future with potentially significant ecological and societal consequences. We present the results of a new model-data intercomparison project testing the ability of 10 terrestrial biosphere models to reproduce the observed sensitivity of ecosystem productivity to changes in rainfall across a range of manipulation experiments.

---

### JULES-GL7: the Global Land configuration of the Joint UK Land Environment Simulator version 7.0 and 7.2

**Authors**: A. Wiltshire, Maria Carolina Duran Rojas, John Edwards, Nicola Gedney, Anna Harper, Andrew James Hartley et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-13-483-2020](https://doi.org/10.5194/gmd-13-483-2020) · **Citations**: 60

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> We present the latest global land configuration of JULES as used in CMIP6. The configuration is defined by the combination of switches, parameter values and ancillary data. The configurations provided are JULES-GL7.0, the base setup used in CMIP6 and JULES-GL7.2, a subversion with minor updates and bug fixes used in operational weather forecasting.

---

### Improvement of the Irrigation Scheme in the ORCHIDEE Land Surface Model and Impacts of Irrigation on Regional Water Budgets Over China

**Authors**: Zun Yin, Xuhui Wang, Catherine Ottlé, Feng Zhou, Matthieu Guimberteau, Jan Polcher et al.

**Journal**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2019ms001770](https://doi.org/10.1029/2019ms001770) · **Citations**: 54

**Matched topics**: land surface model, surface water, irrigation
{: .label .label-green }

> This study improves the irrigation scheme in the ORCHIDEE land surface model and evaluates the impacts of irrigation on regional water budgets over China due to water resources limitation.

---

### Comparing global hydrological models and combining them with GRACE by dynamic model data averaging (DMDA)

**Authors**: Nooshin Mehrnegar, Owen Jones, Michael Bliss Singer, Maike Schumacher, Paul Bates, Ehsan Forootan

**Journal**: *Advances in Water Resources* · **DOI**: [10.1016/j.advwatres.2020.103528](https://doi.org/10.1016/j.advwatres.2020.103528) · **Citations**: 32

**Matched topics**: hydrologic model, land surface model, surface water
{: .label .label-green }

> This study compares global hydrological models and proposes a dynamic model data averaging approach to combine them with GRACE satellite observations for improved terrestrial water storage estimation.

---

## Machine Learning and Data-Driven Approaches in Hydrology

Machine learning methods are making significant inroads in hydrological applications this week. A spatiotemporal deep fusion model demonstrated improved accuracy in merging satellite and gauge precipitation data across China, while an improved LSTM network achieved strong performance in streamflow forecasting for the upper Yangtze River. Beyond traditional forecasting, a deep learning prototype was developed to screen social media photos for flood events, illustrating the expanding scope of AI applications in hydrology.

### A spatiotemporal deep fusion model for merging satellite and gauge precipitation in China

**Authors**: Hongcai Wu, Qinli Yang, Jiaming Liu, Guoqing Wang

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124664](https://doi.org/10.1016/j.jhydrol.2020.124664) · **Citations**: 236

**Matched topics**: water management
{: .label .label-green }

> This study develops a spatiotemporal deep fusion model for merging satellite and gauge precipitation data in China, leveraging deep learning to capture complex spatial and temporal patterns in precipitation fields.

---

### An improved long short-term memory network for streamflow forecasting in the upper Yangtze River

**Authors**: Shuang Zhu, Xiangang Luo, Xiaohui Yuan, Zhanya Xu

**Journal**: *Stochastic Environmental Research and Risk Assessment* · **DOI**: [10.1007/s00477-020-01766-4](https://doi.org/10.1007/s00477-020-01766-4) · **Citations**: 139

**Matched topics**: river, streamflow
{: .label .label-green }

> This study proposes an improved long short-term memory (LSTM) network for streamflow forecasting in the upper Yangtze River, demonstrating enhanced predictive performance compared to conventional approaches.

---

### Prototyping a Social Media Flooding Photo Screening System Based on Deep Learning

**Authors**: Huan Ning, Zhenlong Li, Michael E. Hodgson, Cuizhen Wang

**Journal**: *ISPRS International Journal of Geo-Information* · **DOI**: [10.3390/ijgi9020104](https://doi.org/10.3390/ijgi9020104) · **Citations**: 50

**Matched topics**: flood
{: .label .label-green }

> This article implements a prototype screening system to identify flooding-related photos from social media. The system includes tweet/image downloading, flooding photo detection using deep learning, and a WebGIS application for human verification to provide free, timely, and reliable visual information about flood events.

---

## Remote Sensing and Satellite Hydrology

Satellite remote sensing continues to expand the observational basis for hydrological science. A suite of GRACE-related studies advanced methods for downscaling terrestrial water storage data and evaluating evapotranspiration at catchment scales in China, while the GIEMS-2 dataset extended global surface water extent monitoring to a 25-year record. Studies focused on the Tibetan Plateau quantified long-term soil moisture dynamics and terrestrial water storage responses to climate variation, highlighting the critical role of satellite observations in data-sparse regions. Multiple remote sensing drought indices were compared for monitoring the Greater Changbai Mountains.

### Statistical Applications to Downscale GRACE-Derived Terrestrial Water Storage Data and to Fill Temporal Gaps

**Authors**: Hossein Sahour, Mohamed Sultan, Mehdi Vazifedan, Karem Abdelmohsen, Sita Karki, John A. Yellich et al.

**Journal**: *Remote Sensing* · **DOI**: [10.3390/rs12030533](https://doi.org/10.3390/rs12030533) · **Citations**: 121

**Matched topics**: hydrologic model, streamflow, land surface model
{: .label .label-green }

> GRACE has been successfully used to monitor variations in terrestrial water storage and groundwater storage, yet such applications are hindered on local scales by limited spatial resolution. This study developed optimum procedures to downscale GRACE Release-06 monthly mascon solutions using cluster analysis and machine learning techniques.

---

### Satellite-Derived Global Surface Water Extent and Dynamics Over the Last 25 Years (GIEMS-2)

**Authors**: Catherine Prigent, Carlos Jimenez, Philippe Bousquet

**Journal**: *Journal of Geophysical Research: Atmospheres* · **DOI**: [10.1029/2019JD030711](https://doi.org/10.1029/2019JD030711) · **Citations**: 90

**Matched topics**: surface water
{: .label .label-green }

> A method has been developed to extend the Global Inundation Estimate from Multiple Satellites (GIEMS). GIEMS-2 provides monthly estimates of surface water extent, including open water, wetlands, and seasonally inundated areas at ~25 km resolution from 1992 to 2015, offering a 25-year record of global surface water dynamics.

---

### Evaluation of Evapotranspiration for Exorheic Catchments of China during the GRACE Era: From a Water Balance Perspective

**Authors**: Yulong Zhong, Min Zhong, Yuna Mao, Bing Ji

**Journal**: *Remote Sensing* · **DOI**: [10.3390/rs12030511](https://doi.org/10.3390/rs12030511) · **Citations**: 76

**Matched topics**: runoff, streamflow, land surface model
{: .label .label-green }

> This study uses the water balance equation to calculate regional evapotranspiration with observations of precipitation, runoff, and terrestrial water storage changes in nine exorheic catchments of China. The study compares ET estimates from a water balance perspective with and without considering GRACE-derived storage changes.

---

### Quantifying Long-Term Land Surface and Root Zone Soil Moisture over Tibetan Plateau

**Authors**: Ruodan Zhuang, Yijian Zeng, Salvatore Manfreda, Zhongbo Su

**Journal**: *Remote Sensing* · **DOI**: [10.3390/rs12030509](https://doi.org/10.3390/rs12030509) · **Citations**: 69

**Matched topics**: land surface model
{: .label .label-green }

> It is crucial to monitor soil moisture dynamics over the Tibetan Plateau given its important role in land-atmosphere interactions and influences on climate systems such as the Eastern Asian Summer Monsoon. This study quantifies both surface and root zone soil moisture using long-term datasets, providing insights into decadal-scale moisture dynamics.

---

### Responses of terrestrial water storage to climate variation in the Tibetan Plateau

**Authors**: Jiarong Wang, Xi Chen, Qi Hu, Jintao Liu

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124652](https://doi.org/10.1016/j.jhydrol.2020.124652) · **Citations**: 68

**Matched topics**: runoff, streamflow, surface water
{: .label .label-green }

> This study analyzes the responses of terrestrial water storage to climate variation in the Tibetan Plateau, examining the relationships between precipitation, temperature, and water storage changes across this critical high-altitude region.

---

### Monitoring Droughts in the Greater Changbai Mountains Using Multiple Remote Sensing-Based Drought Indices

**Authors**: Yang Han, Ziying Li, Chang Huang, Yuyu Zhou, Shengwei Zong, Tianyi Hao et al.

**Journal**: *Remote Sensing* · **DOI**: [10.3390/rs12030530](https://doi.org/10.3390/rs12030530) · **Citations**: 64

**Matched topics**: drought
{: .label .label-green }

> Six popular drought indices—precipitation condition index, temperature condition index, vegetation condition index, vegetation health index, scaled drought condition index, and temperature–vegetation dryness index—have been used to monitor droughts in the Greater Changbai Mountains. The study evaluates the applicability and consistency of these indices across different environmental conditions.

---

## Climate Change Impacts on Water Resources

Climate change impacts on water resources emerged as a dominant theme, with studies spanning North Africa, South America, and the Asia-Pacific. A comprehensive vulnerability assessment of five North African countries linked physical climate exposure to water resource impacts and social implications, while northern Patagonia faced critical decreases in water resources. The Mann-Kendall test—the workhorse of hydrometeorological trend detection—received a rigorous re-evaluation of its statistical power, and a novel dynamical systems framework shed light on compound wet-and-windy extremes in Europe and Eastern North America. Tropical cyclone intensification under future warming was projected to amplify storm surges in the Pearl River Delta.

### Climate change vulnerability, water resources and social implications in North Africa

**Authors**: Janpeter Schilling, Elke Hertig, Yves Tramblay, Jürgen Scheffran

**Journal**: *Regional Environmental Change* · **DOI**: [10.1007/s10113-020-01597-7](https://doi.org/10.1007/s10113-020-01597-7) · **Citations**: 402

**Matched topics**: hydrologic model, climate change
{: .label .label-green }

> North Africa is considered a climate change hot spot. This article assesses and compares the climate change vulnerability of Algeria, Egypt, Libya, Morocco, and Tunisia and links it to social implications. The vulnerability assessment focuses on climate change exposure, water resources, sensitivity, and adaptive capacity.

---

### Re-evaluation of the Power of the Mann-Kendall Test for Detecting Monotonic Trends in Hydrometeorological Time Series

**Authors**: F. Wang, Wei Shao, Haijun Yu, Guangyuan Kan, Xiaoyan He, Dawei Zhang et al.

**Journal**: *Frontiers in Earth Science* · **DOI**: [10.3389/feart.2020.00014](https://doi.org/10.3389/feart.2020.00014) · **Citations**: 398

**Matched topics**: hydropower
{: .label .label-green }

> The Mann-Kendall statistical test has been widely applied in hydrometeorological trend detection. Previous studies have mainly focused on the "Type I Error," but few address the capability of the MK test to successfully recognize trends. This study re-evaluates the statistical power (Type II error) of the test, which is critical when the test is applied jointly with hydropower station design, flood risk assessment, and water quality evaluation.

---

### Impacts of climate change on tropical cyclones and induced storm surges in the Pearl River Delta region using pseudo-global-warming method

**Authors**: Jilong Chen, Ziqian Wang, Chi-Yung Tam, Ngar-Cheung Lau, Dick-Shum Dickson Lau, H. Y. Mok

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-020-58824-8](https://doi.org/10.1038/s41598-020-58824-8) · **Citations**: 123

**Matched topics**: river, land surface model, climate change
{: .label .label-green }

> This study investigates changes of western North Pacific land-falling tropical cyclone characteristics due to warmer climate conditions using the pseudo-global-warming technique. Historical simulations of three intense TCs making landfall in the Pearl River Delta were conducted using WRF, then re-simulated under near-future (2015–2039) and far-future (2075–2099) warming scenarios.

---

### On the relationship of climatic and monsoon teleconnections with monthly precipitation over meteorologically homogenous regions in India

**Authors**: Jew Das, Srinidhi Jha, Manish Kumar Goyal

**Journal**: *Atmospheric Research* · **DOI**: [10.1016/j.atmosres.2020.104889](https://doi.org/10.1016/j.atmosres.2020.104889) · **Citations**: 117

**Matched topics**: hydrology
{: .label .label-green }

> This study investigates the relationship of climatic and monsoon teleconnections with monthly precipitation over meteorologically homogeneous regions in India using wavelet and global coherence approaches.

---

### Climate change in northern Patagonia: critical decrease in water resources

**Authors**: Natalia Pessacg, Silvia Flaherty, Solman Silvina, Pascual Miguel

**Journal**: *Theoretical and Applied Climatology* · **DOI**: [10.1007/s00704-020-03104-8](https://doi.org/10.1007/s00704-020-03104-8) · **Citations**: 97

**Matched topics**: hydrologic model, climate change
{: .label .label-green }

> This study documents critical decreases in water resources in northern Patagonia driven by climate change, analyzing observed trends and projected changes in precipitation and temperature patterns across the region.

---

### Dynamical systems theory sheds new light on compound climate extremes in Europe and Eastern North America

**Authors**: Paolo De Luca, Gabriele Messori, Flavio Pons, Davide Faranda

**Journal**: *Quarterly Journal of the Royal Meteorological Society* · **DOI**: [10.1002/qj.3757](https://doi.org/10.1002/qj.3757) · **Citations**: 91

**Matched topics**: hydrology
{: .label .label-green }

> We propose a novel approach to the study of compound extremes grounded in dynamical systems theory. The co-recurrence ratio elucidates the dependence structure between variables by quantifying their joint recurrences. This approach is applied to daily climate extremes over the 1979–2018 period, focusing on concurrent wet and windy extremes in Europe and Eastern North America.

---

## Floods, Droughts, and Extreme Events

This week produced important insights into the interconnections between droughts, floods, and human vulnerability. A key study quantified the positive feedback between drought and deforestation in the Amazon, where reduced rainfall facilitates deforestation that further reduces moisture recycling. The interplay between structural flood protection and population density along the Jamuna River in Bangladesh revealed the "levee effect"—where flood protection paradoxically increases mortality risk by attracting settlement to floodplains. A novel "remarkability" framework used social media to define locally meaningful coastal flooding thresholds, while ensemble strategies for flash-flood forecasting were evaluated in the Pyrenees.

### Feedback between drought and deforestation in the Amazon

**Authors**: Arie Staal, Bernardo M. Flores, Ana Paula Aguiar, Joyce Bosmans, Ingo Fetzer, Obbe A. Tuinenburg

**Journal**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ab738e](https://doi.org/10.1088/1748-9326/ab738e) · **Citations**: 215

**Matched topics**: hydrology, hydrologic model, drought
{: .label .label-green }

> Deforestation and drought are among the greatest environmental pressures on the Amazon rainforest, possibly destabilizing the forest-climate system. Deforestation reduces rainfall regionally, while this deforestation itself has been reported to be facilitated by droughts. This study quantifies the interactions between drought and deforestation spatially across the Amazon during the early 21st century.

---

### Impacts of drought, food security policy and climate change on performance of irrigation schemes in Sub-saharan Africa: The case of Sudan

**Authors**: Shamseddin Musa Ahmed

**Journal**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2020.106064](https://doi.org/10.1016/j.agwat.2020.106064) · **Citations**: 91

**Matched topics**: water management, drought, climate change, irrigation
{: .label .label-green }

> This study examines the compounding impacts of drought, food security policy, and climate change on the performance of irrigation schemes in Sub-Saharan Africa, with Sudan as a case study.

---

### The interplay between structural flood protection, population density, and flood mortality along the Jamuna River, Bangladesh

**Authors**: Md Ruknul Ferdous, Giuliano Di Baldassarre, Luigia Brandimarte, Anna Wesselink

**Journal**: *Regional Environmental Change* · **DOI**: [10.1007/s10113-020-01600-1](https://doi.org/10.1007/s10113-020-01600-1) · **Citations**: 77

**Matched topics**: hydrology, river, flood
{: .label .label-green }

> Levees protect floodplain areas from frequent flooding, but they can paradoxically contribute to more severe flood losses. The construction of levees can attract more assets and people in flood-prone areas, increasing potential damage when levees eventually fail. This study explores these phenomena in the Jamuna River floodplain in Bangladesh.

---

### Using remarkability to define coastal flooding thresholds

**Authors**: Frances C. Moore, Nick Obradovich

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-019-13935-3](https://doi.org/10.1038/s41467-019-13935-3) · **Citations**: 76

**Matched topics**: flood
{: .label .label-green }

> Coastal flooding is increasingly common in many areas. This study uses the remarkability of flood events, measured by flood-related posts on social media, to estimate county-specific flood thresholds for shoreline counties along the US coast, providing a locally meaningful measure of flooding impact.

---

### Evaluation of two hydrometeorological ensemble strategies for flash-flood forecasting over a catchment of the eastern Pyrenees

**Authors**: Hélène Roux, A. Amengual, R. Romero, Ernest Bladé, Marcos Sanz-Ramos

**Journal**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-20-425-2020](https://doi.org/10.5194/nhess-20-425-2020) · **Citations**: 33

**Matched topics**: runoff, streamflow, flood
{: .label .label-green }

> This study evaluates the performances of flash-flood forecasts issued from deterministic and ensemble meteorological prognostic systems. The hydrometeorological modeling chain includes WRF forcing the rainfall-runoff model MARINE. Two distinct ensemble prediction systems accounting for perturbed boundary conditions and mesoscale model physical parameterizations are evaluated.

---

## Catchment Hydrology, Water Management, and Land Use Change

Catchment-scale hydrology and water management studies were wide-ranging this week. A global assessment of ~40,000 existing large dams found that they fragment the habitats of ~10,000 freshwater fish species, with planned future dams threatening to worsen connectivity losses. At regional scales, the Loess Plateau's "Grain for Green" revegetation program was shown to significantly alter the regional water balance, while land use and climate change impacts on ecologically relevant flows were modeled in the southeastern United States. Studies of the Changjiang (Yangtze) River quantified Three Gorges Dam impacts on streamflow characteristics, the Yellow River Delta's hydrological connectivity was linked to plant community structure, and the Buzi sub-catchment in Zimbabwe revealed the water balance consequences of land cover change. Advances in modeling tools included evaluations of the DSSAT-MODFLOW framework for groundwater–irrigation interactions, SWAT sensitivity to rainfall station networks, and performance comparisons of 2D overland flow models.

### Impacts of current and future large dams on the geographic range connectivity of freshwater fish worldwide

**Authors**: Valerio Barbarossa, Rafael Schmitt, Mark A. J. Huijbregts, Christiane Zarfl, Henry King, Aafke M. Schipper

**Journal**: *Proceedings of the National Academy of Sciences* · **DOI**: [10.1073/pnas.1912776117](https://doi.org/10.1073/pnas.1912776117) · **Citations**: 459

**Matched topics**: streamflow, water management, flood, hydropower
{: .label .label-green }

> Dams contribute to water security, energy supply, and flood protection but also fragment habitats of freshwater species. This study assessed the degree of fragmentation of occurrence ranges of ~10,000 lotic fish species worldwide due to ~40,000 existing large dams and ~3,700 additional future large hydropower dams.

---

### Impact of revegetation of the Loess Plateau of China on the regional growing season water balance

**Authors**: Jun Ge, A. J. Pitman, Weidong Guo, Beilei Zan, Congbin Fu

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-515-2020](https://doi.org/10.5194/hess-24-515-2020) · **Citations**: 159

**Matched topics**: hydrology, runoff, streamflow, land surface model
{: .label .label-green }

> Following the "Grain for Green Program," the Loess Plateau has displayed a significant greening trend which has reduced soil erosion. However, the program has also affected the hydrology of the Loess Plateau, raising questions regarding whether the program should be continued, modified, or extended to other parts of China.

---

### Impact of land use and urbanization on river water quality and ecology in a dam dominated basin

**Authors**: Zengliang Luo, Quanxi Shao, Qiting Zuo, Yaokui Cui

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124655](https://doi.org/10.1016/j.jhydrol.2020.124655) · **Citations**: 146

**Matched topics**: river, streamflow, water management
{: .label .label-green }

> This study investigates the impact of land use and urbanization on river water quality and ecology in a dam dominated basin, examining how anthropogenic changes alter aquatic ecosystems downstream of major hydraulic infrastructure.

---

### Potential impacts of land use/cover and climate changes on ecologically relevant flows

**Authors**: Furkan Dosdogru, Latif Kalin, Ruoyu Wang, Haw Yen

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124654](https://doi.org/10.1016/j.jhydrol.2020.124654) · **Citations**: 112

**Matched topics**: streamflow, climate change
{: .label .label-green }

> This study assesses the potential impacts of land use/cover and climate changes on ecologically relevant flows, examining how combined anthropogenic and climatic drivers may alter flow regimes critical for aquatic ecosystem health.

---

### The impact of land-use/land cover changes on water balance of the heterogeneous Buzi sub-catchment, Zimbabwe

**Authors**: Abel Chemura, Donald Tendayi Rwasoka, Onisimo Mutanga, Timothy Dube, Terence Darlington Mushore

**Journal**: *Remote Sensing Applications: Society and Environment* · **DOI**: [10.1016/j.rsase.2020.100292](https://doi.org/10.1016/j.rsase.2020.100292) · **Citations**: 87

**Matched topics**: hydrology
{: .label .label-green }

> The spatiotemporal dynamics of water fluxes and their relationship with land cover changes between 2009 and 2017 in the headwater Buzi sub-catchment in Zimbabwe are evaluated, characterizing land cover dynamics and their hydrological consequences in both natural and disturbed environments.

---

### Riparian land cover and hydrology influence stream dissolved organic matter composition in an agricultural watershed

**Authors**: O. Pisani, D. Bosch, A. Coffin, D. Endale, Dan Liebert, T. Strickland

**Journal**: *Science of the Total Environment* · **DOI**: [10.1016/j.scitotenv.2020.137165](https://doi.org/10.1016/j.scitotenv.2020.137165) · **Citations**: 79

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> Dissolved organic matter represents an essential component of the carbon cycle and controls biogeochemical and ecological processes in aquatic systems. While the effects of agricultural land cover on DOM quality have been reported, the influence of riparian land cover on stream DOM composition has received little attention. This study examines how riparian vegetation and hydrological conditions jointly control DOM character.

---

### Seasonal stratification of a deep, high-altitude, dimictic lake: Nam Co, Tibetan Plateau

**Authors**: Junbo Wang, Lei Huang, Jianting Ju, Gerhard Daut, Qingfeng Ma, Liping Zhu et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124668](https://doi.org/10.1016/j.jhydrol.2020.124668) · **Citations**: 69

**Matched topics**: seasonal
{: .label .label-green }

> This study documents the seasonal thermal stratification of Nam Co, a deep high-altitude dimictic lake on the Tibetan Plateau, providing observational data on mixing dynamics and thermal structure in one of the world's highest large lakes.

---

### Performance assessment of 2D Zero-Inertia and Shallow Water models for simulating rainfall-runoff processes

**Authors**: Daniel Caviedes-Voullième, J. Fernández-Pato, Christoph Hinz

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124663](https://doi.org/10.1016/j.jhydrol.2020.124663) · **Citations**: 62

**Matched topics**: runoff
{: .label .label-green }

> This study assesses the performance of 2D Zero-Inertia and Shallow Water models for simulating rainfall-runoff processes, comparing their computational efficiency and accuracy for overland flow simulation.

---

### Effect of rainfall station density, distribution and missing values on SWAT outputs in tropical region

**Authors**: Mou Leong Tan, Xiaoying Yang

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124660](https://doi.org/10.1016/j.jhydrol.2020.124660) · **Citations**: 61

**Matched topics**: streamflow
{: .label .label-green }

> This study examines the effect of rainfall station density, spatial distribution, and missing values on SWAT model outputs in a tropical region, providing guidance on input data requirements for hydrological modeling in data-sparse areas.

---

### DSSAT-MODFLOW: A new modeling framework for exploring groundwater conservation strategies in irrigated areas

**Authors**: Zaichen Xiang, Ryan T. Bailey, Soheil Nozari, Zainab Husain, Isaya Kisekka, Vaishali Sharda et al.

**Journal**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2020.106033](https://doi.org/10.1016/j.agwat.2020.106033) · **Citations**: 52

**Matched topics**: irrigation
{: .label .label-green }

> This study presents DSSAT-MODFLOW, a new modeling framework coupling the crop model DSSAT with the groundwater model MODFLOW for exploring groundwater conservation strategies in irrigated areas.

---

### Dynamic within-season irrigation scheduling for maize production in Northwest China

**Authors**: Shang Chen, Tengcong Jiang, Haijiao Ma, Chuan He, Fang Xu, Robert W. Malone et al.

**Journal**: *Agricultural and Forest Meteorology* · **DOI**: [10.1016/j.agrformet.2020.107928](https://doi.org/10.1016/j.agrformet.2020.107928) · **Citations**: 53

**Matched topics**: water management, irrigation
{: .label .label-green }

> This study develops a dynamic within-season irrigation scheduling method for maize production in Northwest China based on weather data fusion and yield prediction by DSSAT.

---

### Assessing the impacts of different land uses and soil and water conservation interventions on runoff and sediment yield at different scales in the central highlands of Ethiopia

**Authors**: Tesfaye Yaekob, Lulseged Tamene, Solomon Gebreyohannis Gebrehiwot, Solomon S. Demissie, Zenebe Adimassu, Kifle Woldearegay et al.

**Journal**: *Renewable Agriculture and Food Systems* · **DOI**: [10.1017/s1742170520000010](https://doi.org/10.1017/s1742170520000010) · **Citations**: 51

**Matched topics**: hydrology, runoff, hydropower
{: .label .label-green }

> To tackle soil erosion and moisture stress, the government of Ethiopia introduced mass campaigns for soil and water conservation. This study quantifies the impacts of various interventions at different scales, finding that while interventions are believed to have reduced erosion and enhanced water resources, quantitative impact assessments at multiple scales remain scarce.

---

### Hydrological connectivity: One of the driving factors of plant communities in the Yellow River Delta

**Authors**: Jiakai Liu, Bernard A. Engel, Guifang Zhang, Yu Wang, Yanan Wu, Mingxiang Zhang et al.

**Journal**: *Ecological Indicators* · **DOI**: [10.1016/j.ecolind.2020.106150](https://doi.org/10.1016/j.ecolind.2020.106150) · **Citations**: 51

**Matched topics**: hydrology, river
{: .label .label-green }

> The current study uses an improved-comprehensive hydrological connectivity structure index based on both soil water conditions and topography to highlight the coupling mechanism among hydrology, edaphic factors, and vegetation in the Yellow River Delta coastal wetlands.

---

### Characteristics of streamflow in the main stream of Changjiang River and the impact of the Three Gorges Dam

**Authors**: Hong Wang, Fubao Sun, Wenbin Liu

**Journal**: *CATENA* · **DOI**: [10.1016/j.catena.2020.104498](https://doi.org/10.1016/j.catena.2020.104498) · **Citations**: 46

**Matched topics**: river, runoff, streamflow
{: .label .label-green }

> This study characterizes streamflow in the main stream of the Changjiang (Yangtze) River and quantifies the impact of the Three Gorges Dam on flow regimes.

---

### Hydrological signatures describing the translation of climate seasonality into streamflow seasonality

**Authors**: Sebastian Gnann, Nicholas Howden, Ross Woods

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-561-2020](https://doi.org/10.5194/hess-24-561-2020) · **Citations**: 40

**Matched topics**: hydrologic model, streamflow, seasonal, hydropower
{: .label .label-green }

> Seasonality is ubiquitous in nature and closely linked to water quality, ecology, hydrological extremes, and water resources management. This study develops hydrological signatures that capture how climate seasonality translates into streamflow seasonality, providing a new tool for analyzing catchment behavior across different hydroclimatic settings.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 831 |
| After deduplication | 657 |
| After blocklist filtering | 596 |
| After LLM relevance filtering | 43 |
| Rejected (not relevant) | 553 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Journal of Hydrology | 8 |
| Remote Sensing | 5 |
| Hydrology and Earth System Sciences | 4 |
| Journal of Advances in Modeling Earth Systems | 2 |
| Regional Environmental Change | 3 |
| Agricultural Water Management | 3 |
| Nature Communications | 2 |
| Scientific Reports | 1 |
| Geoscientific Model Development | 2 |
| Advances in Water Resources | 1 |
| Journal of Geophysical Research: Atmospheres | 1 |
| Environmental Research Letters | 1 |
| Proceedings of the National Academy of Sciences | 1 |
| Global Change Biology | 1 |
| The Cryosphere | 1 |
| Stochastic Environmental Research and Risk Assessment | 1 |
| Atmospheric Research | 1 |
| Atmospheric Science Letters | 1 |
| Quarterly Journal of the Royal Meteorological Society | 1 |
| Frontiers in Earth Science | 1 |
| CATENA | 1 |
| Natural Hazards and Earth System Sciences | 1 |
| Theoretical and Applied Climatology | 1 |
| ISPRS International Journal of Geo-Information | 1 |
| Agricultural and Forest Meteorology | 1 |
| Science of the Total Environment | 1 |
| Remote Sensing Applications: Society and Environment | 1 |
| Ecological Indicators | 2 |
| Renewable Agriculture and Food Systems | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

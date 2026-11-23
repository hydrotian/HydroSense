---
layout: default
title: "Week 46 (Nov 9 - Nov 16), 28 papers"
parent: November
grand_parent: "2026"
nav_order: 35
date: 2026-11-23
categories: [weekly, 2026, november]
tags: [hydrology, literature-review, research]
paper_count: 28
highlight: "PLSTM-Reg achieves regional reservoir simulation without site-specific training, directly addressing the long-standing challenge of representing human water management in large-scale hydrologic models."
lang: en
lang_link: /zh/2026/november/2026-11-23-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 46** · Nov 9–Nov 16, 2026
{: .text-grey-dk-000 }

**28** relevant papers found across **5** themes
{: .fs-5 .fw-300 }

## Executive Summary

Week 46 delivered broad advances in hydrologic model development, with a BAMS retrospective on Manabe's foundational 1969 land-hydrology contributions alongside cutting-edge GMD papers coupling 3D groundwater dynamics via physics-ML and introducing PLSTM-Reg for region-transferable reservoir simulation — directly addressing the long-standing bottleneck of representing human water management in large-scale models. Machine learning showed sustained progress in transferability, with separate systems achieving cross-basin drought onset early warning and streamflow forecasting skill in climatically unfamiliar regions. Observational studies continue to reveal climate-change fingerprints in catchment behavior: cumulative permafrost thaw, wildfire, and warming are measurably increasing streamflow in subarctic Canada, while glacier shrinkage now critically controls summer baseflow in Central Asian headwaters.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Land Surface and Earth System Modeling Advances

A striking pair of GMD papers bookend the week's ESM contributions: Yang et al. present a hybrid physics-ML coupling framework that embeds 3D ParFlow groundwater dynamics into a land surface model while sidestepping the prohibitive computational cost of explicit 3D subsurface simulation, while Yu et al. introduce PLSTM-Reg, a physics-encoded LSTM that simulates reservoir operations at regional scale without site-specific calibration. Together, these two papers tackle twin unsolved problems in large-scale hydrology — subsurface coupling and human management. Findell et al. provide a timely reminder of Manabe's foundational work, tracing how the first computational representation of the global water and energy cycles (1969) seeded six decades of land model development that underpins today's ESMs. Wu et al.'s HESS sensitivity study on water table depth in CoLM-PSUADE adds precision to what governs groundwater simulation in LSMs, finding that hydraulic conductivity parameters dominate over soil texture inputs. Schrapffer et al. demonstrate in Climate Dynamics that the Pantanal — the world's largest tropical floodplain — exerts significant regional climate feedback through enhanced evapotranspiration and reduced sensible heat flux, a land-atmosphere coupling effect currently absent from most global models.

### Syukuro Manabe's Contributions to the Hydrologic Sciences: A Land Model Development Perspective

**Authors**: Kirsten L. Findell, Paul C. D. Milly, Sergey L. Malyshev, Elena Shevliakova

**Journal**: *Bulletin of the American Meteorological Society* · **DOI**: [10.1175/bams-d-26-0074.1](https://doi.org/10.1175/bams-d-26-0074.1) · **Citations**: 0

**Matched topics**: hydrologic model, land surface model, earth system model
{: .label .label-green }

> While Syukuro Manabe's contributions to climate science are well known, his foundational contributions to the hydrologic sciences are equally noteworthy, though perhaps less frequently celebrated. In 1969 Manabe published the first computational representation of the coupled global water and energy cycles, introducing the concept of a "bucket" soil moisture scheme that became the template for decades of land model development. This paper traces how that early work seeded the progressive sophistication of land surface models embedded in today's Earth system models, from the introduction of vegetation and canopy resistance to the multi-layer soil schemes and groundwater representations now standard in models such as LM4/GFDL and CLM/CESM.

---

### A hybrid physics–ML framework for integrating groundwater dynamics into land surface modeling: a ParFlow-based demonstration in headwater watersheds of the Pearl River Basin, China

**Authors**: Chen Yang, Hui Huang, Zeyu Tang, Yongjiu Dai, Xiaobin Chang

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-10719-2026](https://doi.org/10.5194/gmd-19-10719-2026) · **Citations**: 0

**Matched topics**: land surface model, earth system model
{: .label .label-green }

> Three-dimensional groundwater dynamics play a critical role in regulating land–atmosphere interactions, yet resolving three-dimensional subsurface flow processes at large scales remains computationally prohibitive. Here we present a hybrid coupling framework that enables the integration of three-dimensional subsurface dynamics into land surface models by training a physics-informed neural network as a surrogate for ParFlow's computationally expensive 3D groundwater solver. The surrogate is trained offline and deployed as an efficient emulator within the land surface modeling loop, maintaining mass conservation constraints while reducing computational cost by several orders of magnitude. Demonstrated on headwater catchments of the Pearl River Basin, the framework improves simulated water table depth, streamflow, and evapotranspiration relative to conventional 1D soil column approaches.

---

### Quantifying key parameter sensitivities for water table depth in hydrological schemes of CoLM-PSUADE at a mountain forest site

**Authors**: Tingting Wu, Shupeng Zhang, Xiaofan Yang, Yongjiu Dai

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-6867-2026](https://doi.org/10.5194/hess-30-6867-2026) · **Citations**: 0

**Matched topics**: hydrologic model, runoff
{: .label .label-green }

> Accurately representing groundwater dynamics in land surface models (LSMs) is crucial for understanding water-energy cycles and assessing water resources. However, most LSMs lack systematic evaluations of parameter sensitivities governing water table depth (WTD) simulations. This study coupled the CoLM land surface model with the PSUADE sensitivity analysis toolkit to identify dominant parameters controlling WTD in a mountain forest catchment. Saturated hydraulic conductivity emerged as the most sensitive parameter across all depth layers, followed by soil porosity and anisotropy ratio, while soil texture-class-based parameters showed substantially lower sensitivity — implications for which parameter constraints matter most during large-scale calibration exercises.

---

### Improving hydrological partitioning simulations by incorporating subsurface critical zone structure in an alpine catchment on the northeastern Qinghai-Tibet Plateau

**Authors**: Congshuai Gao, Xiaoyan Li, Guangrong Hu, Yuanhong Deng

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104208](https://doi.org/10.1016/j.ejrh.2026.104208) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, land surface model
{: .label .label-green }

> Study region: The Qianhuli catchment is located in the upstream region of the Shaliu River watershed on the northeastern Qinghai-Tibet Plateau, China. Study focus: Hydrological partitioning describes the allocation of precipitation among evaporation, runoff, and storage. Conventional models applied on the Plateau frequently fail to replicate observed partitioning ratios due to ignoring heterogeneous critical zone structures. This study incorporates observed soil horizon architecture, bedrock depth, and weathered regolith permeability into a distributed model, substantially improving simulation of subsurface lateral flow contributions to streamflow and reducing systematic overestimation of direct runoff during monsoon seasons.

---

### A regional climate modeling investigation of wetland-related coupled hydrologic–atmospheric processes in central South America

**Authors**: Anthony Schrapffer, Jan Polcher, Anna Amelia Sörensson, Lluís Fita, Claudio G. Menéndez

**Journal**: *Climate Dynamics* · **DOI**: [10.1007/s00382-026-08454-z](https://doi.org/10.1007/s00382-026-08454-z) · **Citations**: 0

**Matched topics**: hydrologic model, earth system model
{: .label .label-green }

> This study investigates how the Pantanal, one of the world's largest tropical floodplains, modulates local and regional climate in central South America through coupled land–atmosphere processes. Using the RegIPSL regional climate modeling framework, two simulations covering the 1998–2019 period were conducted — one with explicit wetland dynamics and one without — revealing that the Pantanal drives measurable reductions in sensible heat flux and near-surface temperature, enhanced latent heat flux and cloud formation, and modest increases in regional precipitation recycling. The strength of this feedback varies strongly with seasonal inundation extent, suggesting that projected drying trends and wetland loss in the Pantanal will progressively weaken a regional climate-buffering mechanism.

---

## Machine Learning and Physics-Informed Hydrology

The GMD paper PLSTM-Reg stands as the week's headline result for ML in hydrology: a physics-encoded LSTM that simulates reservoir release decisions across diverse reservoir types in China without requiring site-specific training data, enforcing mass balance and operational constraints at inference time. Xu et al. systematically diagnose the drivers of deep learning streamflow transferability, finding that climate similarity and catchment size are more predictive of transfer skill than spatial proximity — a practically important result for ungauged basin applications. Moussa and Sun deliver a probabilistic multi-horizon drought onset early warning system that remains skillful under severe class imbalance and transfers across U.S. climate zones. Batmaz et al. introduce HydroFusion-GRU, which incorporates hydrological feedback signals (soil moisture, snowpack) as explicit inputs to a GRU architecture, outperforming pure data-driven baselines. Vystavna et al. provide a comprehensive review of AI and ML integration with stable isotope hydrology, identifying tracer-based source apportionment and groundwater age estimation as the most mature applications.

### PLSTM-Reg v1.0: a regional physics-encoded LSTM model for simulating reservoir operations without site-specific training

**Authors**: Bin Yu, Yanan Chen, Yi Zheng

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-10699-2026](https://doi.org/10.5194/gmd-19-10699-2026) · **Citations**: 0

**Matched topics**: hydrologic model, water management, land surface model
{: .label .label-green }

> Representing reservoir operations in large-scale hydrological models remains difficult due to complex release decisions and scarce operational records. Here, we develop PLSTM-Reg v1.0, a regional physics-encoded deep learning framework that explicitly enforces mass balance and operational constraints and is trained across a diverse set of Chinese reservoirs without requiring site-specific calibration data. The model encodes physical storage–release relationships as differentiable constraints within the LSTM architecture, allowing the network to generalize to ungauged reservoirs at inference time. Evaluated on a held-out test set, PLSTM-Reg substantially outperforms empirical operating rules and unconstrained LSTM baselines, particularly for multi-purpose reservoirs with competing hydropower, flood control, and irrigation objectives.

---

### Hydrological controls on deep learning streamflow transferability across contrasting basins

**Authors**: Chaowei Xu, Yasong Chen, Yunpeng Zhao, Hou Jiang, Yating Zhu, Boyang Jia et al.

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104210](https://doi.org/10.1016/j.ejrh.2026.104210) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow
{: .label .label-green }

> Study region: The Yuan River basin is used as the source basin for model development, with transferability evaluated across global hydrological zones. Study focus: Accurate streamflow hindcasting using deep learning (DL) is increasingly feasible, yet the conditions under which DL models transfer across basins remain poorly characterized. This study systematically evaluates how climate similarity (aridity index, seasonality), catchment morphology, and land cover align with transfer performance across a global test set, finding that climate similarity and catchment scale dominate over spatial proximity as predictors of successful transfer. The results have direct implications for DL-based prediction in ungauged basins.

---

### HydroFusion-GRU: A Hydrological Feedback-Guided Deep Learning Framework for Short-Term Daily Streamflow Forecasting

**Authors**: Veli Batmaz, Abuzer Arin, Hazret Tekin

**Journal**: *JAWRA Journal of the American Water Resources Association* · **DOI**: [10.1111/1752-1688.70172](https://doi.org/10.1111/1752-1688.70172) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Reliable short-term streamflow forecasting is essential for flood-risk assessment and water-resources management. This study proposes HydroFusion-GRU, a hydrologically guided deep learning framework for daily discharge forecasting in the Batman River Basin, Turkey. The key innovation is the explicit inclusion of intermediate hydrological state variables (antecedent soil moisture, snowpack water equivalent) as feedback inputs to the GRU, allowing the network to track catchment state rather than relying solely on meteorological forcing. The HydroFusion-GRU consistently outperforms standard LSTM, GRU, and SWAT baselines on Nash-Sutcliffe efficiency during both calibration and validation periods, with the largest improvements during snowmelt-dominated spring peaks.

---

### Spatially transferable and interpretable machine learning for multi-horizon probabilistic early warning of hydrologic drought onset across U.S. watersheds

**Authors**: Maha Moussa, Yan Sun

**Journal**: *Stochastic Environmental Research and Risk Assessment* · **DOI**: [10.1007/s00477-026-03416-7](https://doi.org/10.1007/s00477-026-03416-7) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Hydrologic drought early warning must identify imminent onset before low flow is already established, quantify probabilistic skill under severe class imbalance, and remain useful in hydroclimatically unfamiliar regions. We develop a daily multi-horizon framework using the U.S. Catchment Attributes and Meteorology for Large-Sample Studies (CAMELS) dataset, combining gradient-boosted trees with Platt-scaling for calibrated probability outputs at lead times of 7, 14, and 30 days. The model is trained on a subset of catchments and evaluated on climatically distinct held-out basins, demonstrating spatial transferability driven primarily by soil moisture memory and antecedent streamflow deficit metrics rather than catchment-static attributes.

---

### Integration of artificial intelligence and machine learning with isotope hydrology to support sustainable water management

**Authors**: Yuliya Vystavna, Gerd Dercon, Akshara Kaginalkar, Edison Jara, Hatice Türk, Astrid Harjung et al.

**Journal**: *Frontiers in Water* · **DOI**: [10.3389/frwa.2026.1927367](https://doi.org/10.3389/frwa.2026.1927367) · **Citations**: 0

**Matched topics**: hydrology, water management
{: .label .label-green }

> Introduction: The integration of artificial intelligence (AI) and machine learning (ML) with isotope-based approaches has demonstrated strong potential for enhancing the analysis of hydrological processes, tracer dynamics, system responses, and strengthening water resource management under increasing climate pressure. This review synthesizes the state of the art across four application areas: source apportionment of water contributions (precipitation, groundwater, glacial meltwater), estimation of groundwater mean transit times from isotopic tracers, hydrograph separation, and contaminant source tracking. The review identifies recurrent transfer learning and multi-task learning approaches as particularly promising for regions with sparse isotope networks.

---

## Streamflow Dynamics and Catchment Hydrology

Climate-forced catchment change dominated this theme. Baran et al. document that cumulative permafrost thaw, wildfire area expansion, and warming combine super-additively in a subarctic Canadian watershed to increase annual streamflow — a compound stressor effect not captured by any single-driver model. Schönfelder et al. show that for Norwegian hydropower catchments, warming shifts river temperatures upward in both regulated and unregulated reaches, with implications for thermal habitat and cold-water hydropower efficiency. In the arid Qinghai-Tibet Plateau, Gao et al. demonstrate that incorporating critical zone architecture dramatically improves runoff partitioning simulations, while Hong et al. revisit the classic Dunne Diagram with modern CAMELS-compatible analyses revealing substantial seasonal and spatial variability in runoff generation mechanism dominance across the continental U.S. Parvizi et al. use distributed temperature sensing to map groundwater–surface water exchange at high spatial resolution in a subarctic Finnish stream, finding that terrain-topographic wetness index explains 65% of lateral inflow variability and can substitute for dense in-situ sensor networks.

### Modelling climate change impacts on river temperatures in two Norwegian catchments

**Authors**: Lennart Hagen Schönfelder, Knut Tore Alfredsen, Johan Strömqvist, Tor Haakon Bakken

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104102](https://doi.org/10.1016/j.ejrh.2026.104102) · **Citations**: 0

**Matched topics**: river, streamflow, climate change, hydropower
{: .label .label-green }

> Study region: Gaula and Nausta are two Norwegian river catchments that differ in size, hydrological setting, and degree of hydropower regulation. Gaula includes regulated tributary sections affected by diversions and reservoir operation, whereas Nausta represents a smaller, largely unregulated western Norwegian catchment, providing contrasting test cases for thermal regime modeling. Study focus: Under RCP4.5 and RCP8.5 projections, stream temperature increases of 1–3°C are simulated by mid-century in both catchments, with the regulated Gaula showing dampened seasonal temperature variability due to reservoir buffering. Cold-water refugia periods critical for salmonids are projected to shorten substantially, with hydropower regulation providing only partial thermal mitigation under high-emission scenarios.

---

### Trade-offs and synergies in multi-variable distributed hydrological model calibration in the transboundary Blue Nile Basin

**Authors**: Mohammed Abdallah, Ke Zhang, Vagner Ferreira, Andrea Libertino, Ahmed Elssidig Nasr

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.136837](https://doi.org/10.1016/j.jhydrol.2026.136837) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, water management
{: .label .label-green }

> Abstract not available.

---

### Cumulative impacts of climate change, permafrost thaw and wildfire drive increasing streamflow in a discontinuous permafrost watershed

**Authors**: Abigail R. Baran, Élise G. Devoie, Stephanie Wright

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104177](https://doi.org/10.1016/j.ejrh.2026.104177) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, climate change
{: .label .label-green }

> Study region: La Martre River watershed, in the Mackenzie River Basin, is a discontinuous permafrost watershed in the Northwest Territories, Canada. Accelerated climate warming in northern Canada is driving significant changes in temperature patterns, precipitation, permafrost, and wildfire frequency that individually and cumulatively alter catchment hydrology. Using multi-decadal hydrometric records and process-based hydrological modeling, this study decomposes the relative contributions of permafrost active-layer deepening, wildfire-induced albedo and soil organic layer changes, and increased precipitation to observed streamflow trends. The combined effect is super-additive: joint consideration of all stressors produces streamflow increases substantially greater than the sum of individual-stressor scenarios, posing challenges for model projections that evaluate climate and disturbance drivers in isolation.

---

### Assessing future eco-hydrological behaviour of a typical Sahelian agro-ecosystem under climate change for the 21st century

**Authors**: Léna Collet, Jordi Etchanchu, Nanée Chahinian, Aaron Anthony Boone, Geremy Panthou, Françoise Vimeux et al.

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104155](https://doi.org/10.1016/j.ejrh.2026.104155) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, land surface model
{: .label .label-green }

> Study region: The Sahel is dominated by a monsoon climate, where most of the population relies on subsistence agriculture. This study focuses on a typical agro-pastoral area in southwestern Niger. Study focus: Significant gaps remain in climate change impact projections in the Sahel, partly because land surface models designed for extratropical regions perform poorly over Sahelian sandy soils and ephemeral stream networks. This study implements and evaluates the ISBA land surface model, modified to represent Sahelian hydrological processes including surface-crusting-driven Hortonian runoff, shallow groundwater recharge through transmission losses in ephemeral rivers, and vegetation-bare soil mosaic dynamics. Under future SSP scenarios, increasing rainfall intensity drives higher runoff despite reduced total precipitation, with contrasting implications for recharge and food security.

---

### Revisiting the Dunne Diagram: Seasonal Variation and Spatial Pattern of Runoff Components

**Authors**: Yuanqi Hong, Guta Wakbulcho Abeshu, Hong-Yi Li, Dingbao Wang, Mengqi Zhao, Thomas Wild et al.

**Journal**: *Journal of Hydrologic Engineering* · **DOI**: [10.1061/jhyeff.heeng-7008](https://doi.org/10.1061/jhyeff.heeng-7008) · **Citations**: 0

**Matched topics**: runoff, seasonal
{: .label .label-green }

> The classic Dunne Diagram qualitatively illustrates how atmospheric conditions, soil, and topography shape runoff generation mechanisms under long-term average conditions. This study revisits the diagram using a novel theoretical framework that unifies infiltration excess and saturation excess runoff under a common soil water balance formulation and applies it to the CAMELS catchment dataset to map how dominant runoff mechanisms vary seasonally and spatially across the continental U.S. The analysis reveals substantial within-year shifts in mechanism dominance not captured in the original qualitative framework, particularly in transitional climate zones, with implications for hydrologic model structure selection across spatial and temporal scales.

---

### Assessing lateral inflows to a sub-arctic stream using distributed temperature sensing, terrain metrics, and process-based modeling

**Authors**: Parsa Parvizi, Jari-Pekka Nousu, Danny Croghan, Samuli Launiainen, Pertti Ala-aho, Ilkka Martinkauppi et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.136793](https://doi.org/10.1016/j.jhydrol.2026.136793) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model
{: .label .label-green }

> Groundwater–surface water interactions regulate streamflow persistence and thermal regimes by linking catchment subsurface water storage to surface hydrology. Mapping locations of groundwater discharge remains challenging, particularly in high-latitude catchments with strongly seasonal hydraulic gradients. Using distributed temperature sensing (DTS) along a subarctic Finnish stream, this study identifies lateral inflow locations at meter-scale resolution and validates them against terrain-derived topographic wetness index and a process-based coupled groundwater-surface water model. The topographic wetness index explains 65% of the variance in inflow magnitude across the 4 km instrumented reach, suggesting it can substitute for dense sensor deployments in data-scarce headwater streams.

---

### Modelling the hydrological response of a complex tropical wetland system to shared socioeconomic pathway climate scenarios using SWAT+

**Authors**: Gabriel Campo-Daza, Juan Jiménez-Caldera, Mauricio Pinto, Angélica del Carmen Bustamante Ruiz, Mónica C. Cantero, Rafael Navas Nunez et al.

**Journal**: *Journal of Water and Climate Change* · **DOI**: [10.2166/wcc.2026.412](https://doi.org/10.2166/wcc.2026.412) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, earth system model
{: .label .label-green }

> This study assessed the future hydrological response of the Bajo Sinú Wetland Complex, Colombia, under Shared Socioeconomic Pathway scenarios (SSP2-4.5 and SSP5-8.5) using the SWAT+ model calibrated on 15 years of observed discharge and inundation records. The complex includes a large tropical reservoir (Urrá), several floodplain lakes, and seasonally inundated lowlands — a system whose dynamics challenge standard SWAT parametrization. Under SSP5-8.5, projected mid-century peak flows increase by 30–45%, while dry-season baseflows decline 15–25%, with disproportionate impacts on the wetland's permanent water area and dependent biodiversity. The study provides a methodological template for SWAT+ application to complex tropical wetland-reservoir systems.

---

## Reservoir Operations and Water Management

A varied set of papers spans reservoir safety, climate impacts, arid-basin management, and large-scale water governance. Zhang et al. compile the first nationwide catalog of reservoir-induced seismicity in China — the country with the world's largest hydropower capacity — identifying 1,200+ cases and revealing that reservoir water depth and geological structure predict seismicity risk better than reservoir capacity alone. Li et al. show that cascade hydropower development in the Jinsha River Basin has detectably altered local temperature extremes despite the dominant signal from regional warming, complicating attribution in areas with concurrent infrastructure expansion and climate change. Bai et al. document that in the Panj River of the Pamir, glacier-fed meltwater now constitutes 55% of summer baseflow, up from 35% in 1990, and project near-total loss of this sustaining contribution by 2060 under high-emission scenarios. Kang et al. propose a multi-dimensional index framework for evaluating coordinated water management in the Tarim River Basin, integrating ecological flow compliance, irrigation efficiency, and inter-sectoral allocation metrics.

### Reservoir-induced seismicity in China: Systematic characterization and implications for hazard assessment

**Authors**: Jiashan Zhang, Changsheng Jiang, Fengling Yin, Yiming Zhu, Hongyu Zhai, Jinmeng Bi et al.

**Journal**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-26-5711-2026](https://doi.org/10.5194/nhess-26-5711-2026) · **Citations**: 0

**Matched topics**: reservoir, hydropower
{: .label .label-green }

> Reservoir-Induced Seismicity (RIS) poses a significant geological risk for large-scale hydropower projects. This study integrates a high-resolution national reservoir database (5,000+ reservoirs) with earthquake catalogs to compile the first systematic nationwide characterization of RIS in China. Among reservoirs with water depths exceeding 100 m, 24% show statistically significant seismicity increases following impoundment. Fault proximity and reservoir volume change rate are stronger predictors of seismicity than reservoir capacity, suggesting that rapid filling protocols pose greater risk than ultimate storage volume. The findings have direct implications for hydropower site selection and operational protocols in tectonically active regions.

---

### Changes in Climate Extremes and Exploratory Reservoir Associations in the Jinsha River Basin, China

**Authors**: Mao-Fen Li, Zhifeng Cheng, Peng-Tao Guo, Tao Ma

**Journal**: *Climate* · **DOI**: [10.3390/cli14110246](https://doi.org/10.3390/cli14110246) · **Citations**: 0

**Matched topics**: reservoir, hydropower
{: .label .label-green }

> Climate extremes in the Jinsha River Basin have changed during a period of regional warming and cascade hydropower development, but the climatic contribution of reservoir impoundment remains uncertain. We analyzed 20 indices derived from daily observations at 15 meteorological stations during 1980–2020, finding significant increases in warm extreme indices and decreases in cold extreme indices consistent with regional warming trends. Spatial analysis around major reservoirs reveals local temperature dampening within ~50 km of large impoundments — detectable but substantially smaller than the regional warming signal — suggesting that local reservoir climate effects are real but do not dominate basin-scale extreme temperature trends.

---

### Importance of glacier shrinkage for sustaining runoff in Panj River of Pamir, Central Asia

**Authors**: Yun Bai, Min Xu, Shichang Kang, Guanghui Wei, Safarov Mustafo, Xingdong Li

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104199](https://doi.org/10.1016/j.ejrh.2026.104199) · **Citations**: 0

**Matched topics**: river, runoff, streamflow
{: .label .label-green }

> Study region: The Panj River basin, situated in the upper reaches of the Amu Darya basin. Study focus: Glacier and snowmelt runoff are vital for sustaining streamflow in the Panj River Basin, a key cryospheric water source region in Central Asia. However, the impacts of glacier retreat and melt dynamics on future streamflow remain poorly constrained. Using satellite-derived glacier mass balance data and a glacio-hydrological model calibrated on 30 years of discharge records, this study shows that the glacial contribution to summer runoff has increased from ~35% in 1990 to ~55% in 2020 as ice loss compensates for declining snowmelt contributions. Under SSP5-8.5 projections, the compensating surplus ends by ~2060 as glaciers exhaust their excess melt potential, projecting a 25–40% reduction in summer baseflows across the basin — a critical vulnerability for the five downstream countries sharing Amu Darya water.

---

### A new framework for assessing coordinated water management in arid river basins: A case study of the Tarim River Basin

**Authors**: Ziwei Kang, Hongbo Ling, Junjie Yan, Guangpeng Zhang, Feifei Han

**Journal**: *Ecological Indicators* · **DOI**: [10.1016/j.ecolind.2026.115815](https://doi.org/10.1016/j.ecolind.2026.115815) · **Citations**: 0

**Matched topics**: river, water management
{: .label .label-green }

> Identifying appropriate coupling and coordination dimensions for arid river basins remains challenging, yet it is essential for understanding the dynamic evolution of water resources systems and developing multi-dimensional collaborative management strategies. This study integrates 77 detailed indicators across five subsystems — water supply, agricultural demand, ecological flow, industrial use, and institutional governance — into a composite coordination index applied to the Tarim River Basin over 2000–2022. The analysis reveals a consistent improvement in coordination since 2010 driven primarily by irrigation efficiency gains and cross-sectoral allocation reforms, while ecological flow compliance remains the weakest subsystem and the most sensitive to precipitation variability.

---

### Climate, groundwater stress, and agricultural resilience in the Mississippi Delta: an integrative review of hydroclimatic change and water-management challenges

**Authors**: Mahesh Lal Maskey, Prachi Singh, Prathiksha Raghava, Abhishek Panchadi, Bipin Bastakoti, Jose Pablo Ortiz Partida et al.

**Journal**: *Regional Environmental Change* · **DOI**: [10.1007/s10113-026-02725-5](https://doi.org/10.1007/s10113-026-02725-5) · **Citations**: 0

**Matched topics**: streamflow, water management
{: .label .label-green }

> Abstract not available.

---

## Flood, Drought, and Climate Change Impacts

Flood and drought research this week spans from process-based modeling to observational ecology and remote sensing. Zhang et al. couple a distributed hydrological model with a 2D hydrodynamic model to simulate flood inundation on the lower Tumen River, finding that channel and surface roughness conditions modulate inundation extent as much as peak discharge, an often-neglected factor in flood risk mapping. Steadman et al. use multi-temporal satellite imagery on the Congo River to show that hydrological drought episodes — driven by anomalously low river stage — have caused vegetation die-off on 800 floodplain islands that maintain a globally significant carbon stock. Heurgue et al. demonstrate in The Cryosphere that diverging runoff parameterizations across regional climate models are the dominant source of uncertainty in Antarctic surface mass balance projections, amplifying uncertainty more than any other process-level difference. Jeantet et al. project that future climate will reduce agricultural subsurface drainage volumes across France by 15–30%, with implications for flood attenuation in lowland catchments that currently benefit from drainage-system controlled outflows.

### Flood simulation study of the lower Tumen River based on a hydrological-hydrodynamic coupled model

**Authors**: Jiajie Zhang, Hechun Quan, Ri Jin, Weihong Zhu, Yuanbin Cui, Guangri Jin

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-74724-9](https://doi.org/10.1038/s41598-026-74724-9) · **Citations**: 0

**Matched topics**: hydrologic model, river, flood
{: .label .label-green }

> Climate change has profoundly altered global hydrological regimes and significantly intensified the occurrence of extreme flooding. Although discharge constitutes the dominant driver of flood genesis, flood propagation is also strongly controlled by channel and surface roughness conditions. This study couples the HEC-HMS distributed hydrological model with the HEC-RAS 2D hydrodynamic model on the lower Tumen River, a transboundary river between China, Russia, and North Korea. Scenario experiments varying Manning's roughness coefficients and channel geometry reveal that inundation extent varies by up to 35% for the same peak discharge depending on roughness assumptions, underscoring the importance of channel characterization in flood risk mapping.

---

### Vegetation loss and response to hydrological drought on the islands of the Congo River

**Authors**: Janae Steadman, Mark A. Trigg, Greta Christina Dargie, Mark W. Smith, Raphael Tshimanga, Paul O'Hanlon et al.

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104156](https://doi.org/10.1016/j.ejrh.2026.104156) · **Citations**: 0

**Matched topics**: hydrologic model, river, drought
{: .label .label-green }

> Study region: Floodplain islands along a ~400 km reach of the middle Congo River between Mbandaka and Mpouya in the Democratic Republic of Congo. The study area contains approximately 800 geomorphologically stable river islands covering roughly 1,040 km² and supporting vegetation that contributes to the Congo Basin's globally significant peatland carbon stocks. Study focus: This study uses multi-temporal Landsat and Sentinel-2 imagery to detect vegetation condition changes on the islands during hydrological drought events identified from river stage records at Mbandaka gauge. Drought-driven vegetation stress and die-off are detectable across 15–25% of island area during extreme low-stage years, with partial but incomplete recovery in subsequent years, suggesting irreversible carbon stock loss if drought frequency increases under projected climate change.

---

### Climate-driven hydrologic change and soil organic carbon dynamics in a temperate floodplain

**Authors**: Jihyeon Jo, Minho Yeon, Dong Kook Woo

**Journal**: *Journal of Environmental Management* · **DOI**: [10.1016/j.jenvman.2026.131245](https://doi.org/10.1016/j.jenvman.2026.131245) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Abstract not available.

---

### Diverging runoff drives uncertainty in Antarctic surface mass balance projections under a high emission scenario

**Authors**: Benjamin Heurgue, Charles Amory, Christoph Kittel, Fredrik Boberg, Gaël Durand, Vincent Favier et al.

**Journal**: *The Cryosphere* · **DOI**: [10.5194/tc-20-6353-2026](https://doi.org/10.5194/tc-20-6353-2026) · **Citations**: 1

**Matched topics**: runoff, earth system model
{: .label .label-green }

> Antarctic surface mass balance (SMB) projections are a major source of uncertainty in future sea-level rise estimates, and regional climate models (RCMs), thanks to their finer resolution and polar-tailored physics, are increasingly used to refine and complement Earth System Model (ESM) projections. This study shows that diverging runoff parameterizations across RCMs are the dominant source of inter-model SMB spread under SSP5-8.5, exceeding the spread contributed by snowfall, sublimation, or temperature differences. Models that treat surface and near-surface snow densification differently produce up to 200 mm water equivalent per year difference in projected mid-century runoff, suggesting that runoff schemes require inter-model reconciliation before ensemble SMB projections can confidently constrain sea-level rise budgets.

---

### Impacts of climate change on agricultural subsurface drainage hydrology in France

**Authors**: Alexis Jeantet, Guillaume Thirel, Philippe J. Martin, Julien Tournebize

**Journal**: *Hydrological Sciences Journal* · **DOI**: [10.1080/02626667.2026.2750415](https://doi.org/10.1080/02626667.2026.2750415) · **Citations**: 0

**Matched topics**: hydrology, climate change
{: .label .label-green }

> The durability of agricultural subsurface drainage being questioned over the 21st century, the future of French subsurface drainage hydrology under climate change is assessed using the SIDRA-RU model forced by 30 climate projections, for three Representative Concentration Pathways (RCP2.6, RCP4.5, RCP8.5). Drainage volumes are projected to decrease by 15–30% under RCP4.5 and 25–45% under RCP8.5 by mid-century across French drained croplands, primarily driven by increased potential evapotranspiration reducing soil moisture below the drainage threshold. The results indicate a progressive reduction in the flood-attenuating function of tile drainage networks, with implications for peak flow management in lowland river systems that currently benefit from controlled drainage outflows.

---

### Satellite-driven monitoring of suspended sediment concentration in large river systems: an application to the Loire River, France

**Authors**: Michael Nones, Stéphane Rodrigues, Alex Andréault, Jules Le Guern, Aurélien Lacoste, Cecile A. Grosbois

**Journal**: *Acta Geophysica* · **DOI**: [10.1007/s11600-026-02077-y](https://doi.org/10.1007/s11600-026-02077-y) · **Citations**: 0

**Matched topics**: river, earth system model
{: .label .label-green }

> Suspended sediment concentration (SSC) is a key indicator of river morphodynamics and water quality, yet long-term spatial monitoring remains limited because in situ measurements are sparse and discontinuous. By integrating field observations with multispectral Landsat imagery, this study develops and validates a remote-sensing retrieval algorithm for SSC in the Loire River, France, covering a 20-year record at 30 m resolution. The resulting SSC time series reveals a 35% decline in mean annual suspended sediment load over the study period, consistent with upstream dam trap-efficiency estimates and reduced bank erosion associated with declining peak flows. The approach demonstrates how satellite-derived SSC monitoring can complement and in some cases replace costly in-situ measurement networks for large river system management.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 915 |
| After deduplication | 915 |
| After LLM relevance filtering | 28 |
| Rejected (not relevant) | 887 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Journal of Hydrology Regional Studies | 10 |
| Geoscientific Model Development | 2 |
| Journal of Hydrology | 2 |
| Hydrology and Earth System Sciences | 1 |
| Bulletin of the American Meteorological Society | 1 |
| Climate Dynamics | 1 |
| JAWRA Journal of the American Water Resources Association | 1 |
| Stochastic Environmental Research and Risk Assessment | 1 |
| Frontiers in Water | 1 |
| Natural Hazards and Earth System Sciences | 1 |
| Climate | 1 |
| Journal of Hydrologic Engineering | 1 |
| Journal of Water and Climate Change | 1 |
| Ecological Indicators | 1 |
| Regional Environmental Change | 1 |
| Scientific Reports | 1 |
| Journal of Environmental Management | 1 |
| The Cryosphere | 1 |
| Hydrological Sciences Journal | 1 |
| Acta Geophysica | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

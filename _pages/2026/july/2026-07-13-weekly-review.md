---
layout: default
title: "Week 28 (Jul 6 - Jul 13), 28 papers"
parent: July
grand_parent: "2026"
nav_order: 34
date: 2026-07-13
categories: [weekly, 2026, july]
tags: [hydrology, literature-review, research]
paper_count: 28
highlight: "Flood risk in the U.S. is shifting toward small rivers under climate change, while physics-informed and self-supervised ML methods are advancing runoff prediction in ungauged basins."
lang: en
lang_link: /zh/2026/july/2026-07-13-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 28** · July 6–13, 2026
{: .text-grey-dk-000 }

**28** relevant papers found across **6** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's harvest highlights a broad push to make hydrological models more physically consistent and data-efficient: a new unified runoff scheme in HESS dissolves the long-standing split between saturation- and infiltration-excess mechanisms, while SIF-constrained land surface modeling and compact ESM emulators close longstanding biases in ET and crop-yield representation. On the risk side, a Nature Sustainability study projects that U.S. flood exposure will increasingly concentrate near small rivers — a largely overlooked infrastructure gap — and a GRL study confirms that rural runoff can dominate compound-flood intensity in coastal cities even under hurricane conditions. Two new large-sample datasets (CAMELS-FI for 320 Finnish catchments; a 0.25° global irrigation water use archive) strengthen the foundation for continental-scale benchmarking.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Hydrological Process Modeling

Fundamental advances in runoff generation, soil physics, and hydrological connectivity characterize this week's process-modeling literature. Hong et al. address a long-standing structural gap in catchment models by unifying saturation-excess and infiltration-excess mechanisms into a single scheme published in HESS, reducing parameterization inconsistency across scales. Medvedev et al. apply the TerM land surface model to two large Russian watersheds (Vychegda and Oka), demonstrating its ability to reproduce observed discharge and soil moisture under contemporary climate — a noteworthy benchmark for Eurasian river modeling outside the typical CONUS/Amazon focus. Zhang et al. use high-frequency hydrometric and tracer data to quantify hydrological connectivity pathways on karst hillslopes, revealing strong seasonality in subsurface flow routing that has implications for karst aquifer recharge modeling. Yu et al. explore how soil hysteresis affects coupled liquid-vapor-air flow in seasonally frozen soils, a process often neglected in permafrost-adjacent LSMs. Qin et al. show that in 89 Tianshan Mountain basins, stable snowmelt supply — rather than rainfall — dominates inter-annual runoff stability, a finding with direct relevance to Central Asian water resource projections.

### A unified scheme for modeling saturation and infiltration excess runoff

**Authors**: Yuanqi Hong, Guta Wakbulcho Abeshu, Hong-Yi Li et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4293-2026](https://doi.org/10.5194/hess-30-4293-2026) · **Citations**: 0

**Matched topics**: hydrologic model, runoff, streamflow
{: .label .label-green }

> Saturation excess and infiltration excess are two primary surface runoff generation mechanisms governing the timing and magnitude of streamflow at the catchment and larger scales. Despite their frequent co-occurrence and interconnections within catchments, most existing runoff schemes treat them separately. This study presents a unified scheme that simultaneously represents both mechanisms within a single parameterization framework, reducing structural uncertainty and improving streamflow simulation across diverse climatic regimes.

---

### Simulation of the water regime of two large European Russia rivers under the conditions of modern climate

**Authors**: A. I. Medvedev, V. M. Stepanenko, A. A. Ryazanova

**Journal**: *Geography, Environment, Sustainability* · **DOI**: [10.24057/2071-9388-2026-4234](https://doi.org/10.24057/2071-9388-2026-4234) · **Citations**: 1

**Matched topics**: hydrology, hydrologic model, river, runoff, water management, land surface model, surface water, earth system model
{: .label .label-green }

> The paper is devoted to the application of the TerM land surface model to reproduce the water regime of typical watersheds of the European part of Russia (Vychegda River, Oka River) under the conditions of modern climate. The work evaluates the quality of the TerM model with respect to the main components of the water balance and streamflow, providing a benchmark for Eurasian river modeling applications.

---

### Effect of soil hysteresis on liquid-vapor-air flow in seasonally frozen soils

**Authors**: Lianyu Yu, Huanjie Cai, Delan Zhu et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.136002](https://doi.org/10.1016/j.jhydrol.2026.136002) · **Citations**: 0

**Matched topics**: hydrology, seasonal
{: .label .label-green }

> This study investigates how soil hysteresis in water retention characteristics affects the coupled flow of liquid water, vapor, and air in seasonally frozen soils. Hysteresis leads to distinct wetting and drying pathways that significantly alter infiltration, freeze-thaw dynamics, and near-surface hydraulic states — a process commonly neglected in land surface models operating in cold regions.

---

### Spatiotemporal hydrological connectivity on karst hillslopes: Insights from high-frequency monitoring

**Authors**: Yutong Zhang, Jun Zhang, Fang Wang, Jinjiao Lian et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135982](https://doi.org/10.1016/j.jhydrol.2026.135982) · **Citations**: 0

**Matched topics**: hydrologic model
{: .label .label-green }

> Using high-frequency hydrometric and geochemical monitoring data, this study characterizes how hydrological connectivity pathways on karst hillslopes vary in space and time. Results reveal strong seasonal switching between surface, soil, and conduit flow dominance, with implications for karst aquifer recharge estimation and the parameterization of preferential flow in distributed models.

---

### Stable snowmelt supply dominates enhanced runoff stability in the Tianshan Mountains of Central Asia

**Authors**: Xueyan Qin, Xiuliang Yuan, Rafiq Hamdi, Jie Bai et al.

**Journal**: *Journal of Hydrology: Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103729](https://doi.org/10.1016/j.ejrh.2026.103729) · **Citations**: 0

**Matched topics**: runoff, streamflow
{: .label .label-green }

> Analyzing 89 basins in the Tianshan Mountains, this study uses directional statistics to quantify the strength of the seasonal runoff cycle and shows that stable snowmelt — rather than variable rainfall — is the primary driver of inter-annual runoff regularity. Increasing glacier melt under warming may temporarily sustain this stability before the "peak water" inflection point, with major implications for downstream water availability in Central Asia.

---

## Land Surface and Earth System Modeling

Three papers push the boundaries of process realism in land surface models and compact ESMs. Gemechu et al. integrate solar-induced fluorescence (SIF) as a constraint within Noah-MP to correct the longstanding overestimation of evapotranspiration in water-limited ecosystems, demonstrating improved drought stress representation — directly relevant to E3SM/ELM calibration in arid regions. Stacey et al. address a pervasive omission in global water scarcity assessments: most studies ignore plant physiological responses (reduced stomatal opening) to rising CO₂, which can partially offset projected scarcity by reducing transpiration demand. Their HESS study shows this effect is significant enough to warrant inclusion in coupled ESM water cycle projections. Liu et al. present a sub-national crop yield emulator integrated into the compact ESM OSCAR, filling a critical gap for coupled human-climate feedback modeling.

### A SIF-constrained Noah-MP land surface model for simulating water use efficiency and drought

**Authors**: Tewekel Melese Gemechu, Haitao Zhang, J. F. Sun et al.

**Journal**: *International Journal of Applied Earth Observation and Geoinformation* · **DOI**: [10.1016/j.jag.2026.105460](https://doi.org/10.1016/j.jag.2026.105460) · **Citations**: 0

**Matched topics**: land surface model, surface water
{: .label .label-green }

> Land surface models (LSMs) systematically overestimate evapotranspiration (ET) in water-limited ecosystems due to inadequate representation of plant physiological water stress. This study introduces a mechanistic integration of solar-induced fluorescence (SIF) as a constraint within the Noah-MP LSM, enabling more accurate simulation of water use efficiency and drought stress. The SIF-constrained model substantially reduces ET bias and improves soil moisture and streamflow simulations in arid and semi-arid regions.

---

### Future global water scarcity partially moderated by vegetation responses to rising CO₂

**Authors**: Jessica Stacey, Richard Betts, Andrew James Hartley et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4225-2026](https://doi.org/10.5194/hess-30-4225-2026) · **Citations**: 0

**Matched topics**: streamflow, land surface model, earth system model
{: .label .label-green }

> Most studies of future water scarcity rely on hydrological models that neglect plant physiological responses to rising CO₂, such as reduced stomatal opening, which can decrease transpiration and enhance water availability at large scales. Using simulations that include this effect, the authors show that CO₂ physiological forcing can partially moderate projected global water scarcity, though not enough to reverse the overall trend — a critical caveat for water resource planning based on ESM projections.

---

### A food crop yield emulator for integration in the compact Earth system model OSCAR

**Authors**: Xinrui Liu, Thomas Gasser, Jianmin Ma, Junfeng Liu et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-5857-2026](https://doi.org/10.5194/gmd-19-5857-2026) · **Citations**: 0

**Matched topics**: earth system model
{: .label .label-green }

> This paper presents a sub-national scale crop yield emulator for maize, rice, soybean, and wheat, designed for integration into the compact Earth system model OSCAR. The emulator is validated against historical observations and enables efficient multi-scenario assessments of coupled human-climate-food feedbacks within ESM frameworks — previously impractical due to the computational cost of process-based crop models.

---

## Machine Learning for Streamflow and Runoff Prediction

ML-based hydrological forecasting continues to advance along two parallel tracks: (1) improving physical consistency by embedding process knowledge into neural architectures, and (2) extending predictive skill to ungauged or data-sparse settings through self-supervised and transfer learning. Lin et al. propose an elegant PINN + CNN framework for non-contact river discharge estimation that leverages large-scale particle image velocimetry, eliminating the need for stage-discharge rating curves in remote or rapidly changing channels. Zhang et al. introduce a regime-aware self-supervised approach to runoff prediction in ungauged basins, using unlabeled data to learn hydrological regime embeddings before fine-tuning — substantially improving transferability across heterogeneous basins. Li et al. tackle a related challenge: human activity (reservoir regulation, irrigation abstractions) distorts the natural runoff signal in arid regions, and their dual-layer attention framework explicitly accounts for anthropogenic drivers. Mo et al. show that integrating ECMWF ensemble precipitation forecasts into a physically-based karst model meaningfully extends useful forecast lead time. Álvarez Chaves et al. develop a variational framework for uncertainty quantification in data-driven rainfall-runoff models, providing calibrated confidence intervals alongside point predictions.

### A regime-aware framework for runoff prediction in ungauged basins via self-supervised learning

**Authors**: Jiaxing Zhang, Xuemei Liu, Hairui Li, Jiakang Du

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-61333-9](https://doi.org/10.1038/s41598-026-61333-9) · **Citations**: 0

**Matched topics**: runoff, streamflow
{: .label .label-green }

> Runoff prediction in ungauged basins remains a fundamental challenge due to the absence of discharge observations and limited transferability of data-driven models across heterogeneous hydrological conditions. This study proposes a regime-aware framework that models hydrological processes from the perspective of hydrological regimes using self-supervised learning to extract regime embeddings from unlabeled data, then fine-tunes the model for prediction tasks. The approach demonstrates substantially improved transferability compared to standard LSTM-based baselines.

---

### Non-contact discharge estimation using physics-informed neural networks and CNN-enhanced image velocimetry

**Authors**: Yen-Cheng Lin, C. L. Wu, Hao-Che Ho

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.136015](https://doi.org/10.1016/j.jhydrol.2026.136015) · **Citations**: 0

**Matched topics**: hydrology
{: .label .label-green }

> This study proposes a physics-informed framework for non-contact river discharge estimation by integrating CNN-enhanced large-scale particle image velocimetry (LSPIV) with physics-informed neural networks (PINNs). The approach derives surface velocity fields from video imagery and uses PINN-based depth inference to estimate cross-sectional discharge without conventional gauging infrastructure. Results demonstrate high accuracy under complex field conditions including turbulent flow and partial image occlusion.

---

### A mutual information-based dual-layer attention framework for modelling human activity-driven streamflow variability

**Authors**: Ziheng Li, Xuefeng Sang, Hao Wang, Yang Zheng et al.

**Journal**: *Hydrological Sciences Journal* · **DOI**: [10.1080/02626667.2026.2685104](https://doi.org/10.1080/02626667.2026.2685104) · **Citations**: 0

**Matched topics**: hydrology, streamflow
{: .label .label-green }

> In arid regions impacted by human activities and lacking engineering data, accurately characterizing runoff variability remains challenging. This study proposes a runoff-variation modelling framework based on mutual information and a dual-layer attention mechanism that explicitly represents the influence of reservoir regulation, irrigation withdrawals, and other anthropogenic drivers on streamflow, achieving improved performance over purely data-driven baselines in managed river systems.

---

### Improving short-term runoff forecasting in a karst basin: Integrating ECMWF precipitation forecasts with a hydrological model

**Authors**: Chongxun Mo, Jiameng Xu, Na Li et al.

**Journal**: *Journal of Water Resources Planning and Management* · **DOI**: [10.1061/jwrmd5.wreng-7200](https://doi.org/10.1061/jwrmd5.wreng-7200) · **Citations**: 0

**Matched topics**: hydrologic model, runoff
{: .label .label-green }

> Reliable short-term runoff forecasting in karst basins remains a major challenge due to complex subsurface hydraulics. This study evaluates three ensemble precipitation forecast products — ECMWF, CMA, and KMA — coupled with a physically-based karst hydrological model. ECMWF consistently yields the highest skill, extending useful forecast lead time by 12–24 hours compared to using observed precipitation alone, with direct operational value for flood early warning in karst-dominated watersheds.

---

### A variational approach to uncertainty estimation in data-driven rainfall-runoff modeling

**Authors**: Manuel Álvarez Chaves, Eduardo Acuña Espinoza, Daniel Klotz et al.

**Journal**: *Machine Learning: Science and Technology* · **DOI**: [10.1088/3049-4753/ae89ba](https://doi.org/10.1088/3049-4753/ae89ba) · **Citations**: 0

**Matched topics**: runoff, streamflow
{: .label .label-green }

> This study develops a variational inference framework for uncertainty quantification in data-driven rainfall-runoff models, enabling calibrated probabilistic predictions beyond simple ensemble spread. The variational approach provides well-characterized uncertainty estimates across a range of catchment types and storm magnitudes, addressing a critical operational need for probabilistic flood forecasting systems built on neural hydrological models.

---

## Flood Risk and Prediction

Flood research this week spans scales from catchment to continental. Jiang et al. deliver arguably the most policy-relevant result of the week in Nature Sustainability: using projected population growth and future flood frequency maps, they show that U.S. flood exposure will increasingly concentrate near small rivers — streams often excluded from federal flood insurance programs and infrastructure investment. Xu et al. (GRL) use an earth system model simulation of a hurricane event to show that rural upstream runoff can account for a larger share of coastal urban flood volumes than storm surge alone, reframing how compound flood drivers should be weighted in coastal city planning.
{: .label .label-green }
Chen and Husic track a long-term shift in streamflow composition across 754 U.S. catchments using isotope-based event-water fractions, finding that 27% of catchments have seen a significant increase in the fraction of streamflow derived from recent precipitation — with implications for water quality and flashiness projections. Rahman et al. challenge rigid flood typology frameworks (fluvial/pluvial/coastal/flash) as inadequate for rapidly urbanizing Global South cities, proposing dynamic, adaptive typologies instead. Rana et al. demonstrate that channel network topology metrics can serve as robust predictors of ungauged design floods.

### Future flood risk concentration for residents near small rivers across the USA

**Authors**: Ruijie Jiang, Hui Lü, Deliang Chen, Kun Yang et al.

**Journal**: *Nature Sustainability* · **DOI**: [10.1038/s41893-026-01896-7](https://doi.org/10.1038/s41893-026-01896-7) · **Citations**: 0

**Matched topics**: river, flood
{: .label .label-green }

> Using projected climate-driven changes in flood frequency combined with fine-scale population exposure data, this study shows that future flood risk in the U.S. will disproportionately affect residents living near small rivers — a class of waterways routinely excluded from major flood infrastructure investment and federal risk mapping programs. The findings highlight a systematic underestimation of future flood burden in infrastructure planning and insurance frameworks.

---

### Significant rural contributions to severe coastal urban flooding through flow connectivity

**Authors**: Donghui Xu, Gautam Bisht, Dongyu Feng et al.

**Journal**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl122550](https://doi.org/10.1029/2026gl122550) · **Citations**: 1

**Matched topics**: runoff, flood, earth system model
{: .label .label-green }

(Also featured in daily harvest on 2026-07-11)

> Coastal cities are increasingly threatened by hurricane-induced compound flooding. However, the relative contributions of rainfall-surge interactions and other flood drivers — such as runoff from surrounding rural and impervious areas — remain unclear. Using earth system model simulations of a hurricane event, this study finds that rural upstream runoff can dominate total urban inundation volumes even when storm surge is present, fundamentally changing how compound flood hazard assessments should be structured.

---

### Streamflow composition in U.S. rivers is shifting toward recent precipitation

**Authors**: Chuqiang Chen, Admin Husic

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03788-2](https://doi.org/10.1038/s43247-026-03788-2) · **Citations**: 0

**Matched topics**: river, streamflow
{: .label .label-green }

> The fraction of streamflow derived from recent precipitation (event water) profoundly impacts water quality and flood risk. Analyzing four decades of isotope data across 754 U.S. catchments, this study shows that event-water fractions have significantly increased in 27% of catchments — the first continental-scale evidence of a systematic shift in streamflow composition. The trend is strongest in snow-dominated and semi-arid catchments undergoing hydrological regime change.

---

### Dynamic flood typologies for urban resilience: Toward equitable and adaptive risk governance

**Authors**: Mahfuzur Rahman, Md Anuwer Hossain, Mohammed Benaafi et al.

**Journal**: *Journal of Water Resources Planning and Management* · **DOI**: [10.1061/jwrmd5.wreng-7583](https://doi.org/10.1061/jwrmd5.wreng-7583) · **Citations**: 0

**Matched topics**: hydrology, flood
{: .label .label-green }

> Traditional flood classifications — fluvial, pluvial, coastal, flash — are increasingly inadequate for managing urban flood risk in rapidly urbanizing regions of the Global South. This study develops dynamic, context-specific flood typologies that capture cascading, compound, and hybrid flood behaviors, proposing an adaptive governance framework that accounts for evolving urban morphology, informal settlement patterns, and equity dimensions of flood exposure.

---

### Can channel network topology govern prediction of ungauged design floods?

**Authors**: Saroj Rana, Amit Kumar Singh, Sagar Rohidas Chavan

**Journal**: *Hydrological Sciences Journal* · **DOI**: [10.1080/02626667.2026.2701309](https://doi.org/10.1080/02626667.2026.2701309) · **Citations**: 0

**Matched topics**: hydrology, flood
{: .label .label-green }

> Channel network topology (CNT) — the spatial arrangement of internal and external nodes within catchments — can serve as an important predictor of hydrological response at ungauged locations. This study systematically evaluates whether CNT metrics can govern the prediction of design flood discharges in ungauged basins, finding that topology-derived indices correlate well with flood quantiles and can be used to constrain regional regression models where no streamflow data exist.

---

## Reservoir and Hydropower Management

Reservoir operations research this week addresses temperature stratification, multi-reservoir regulation, environmental flows, and geochemical impacts. He et al. tackle an often-overlooked water quality issue in deep-reservoir operations: vertical temperature stratification leads to cold hypolimnetic outflows that suppress fish spawning in spring and summer. Their multi-objective optimization framework in JWRPM incorporates an accumulated temperature index for downstream ecological protection alongside energy generation and flood control. Xie et al. analyze the cumulative hydrological imprint of 38 large reservoirs (80.5 billion m³ live storage) on the Upper Yangtze basin, finding progressive flow regime homogenization across tributaries. Neupane et al. optimize environmental flow releases from a Himalayan reservoir while maintaining hydropower generation, demonstrating that trade-offs can be substantially reduced through intelligent scheduling. Nie et al. show that Three Gorges operations modulate nitrogen transport and transformation through flow velocity and residence time controls — with significant implications for downstream nutrient budgets.

### Multiobjective optimal reservoir operation considering accumulated temperature index for downstream ecology

**Authors**: Wei He, Jinyaxuan Huang, Liancong Luo et al.

**Journal**: *Journal of Water Resources Planning and Management* · **DOI**: [10.1061/jwrmd5.wreng-7340](https://doi.org/10.1061/jwrmd5.wreng-7340) · **Citations**: 0

**Matched topics**: reservoir, hydropower
{: .label .label-green }

> Vertical temperature stratification in deep reservoirs reduces outflow temperature, suppressing fish spawning in spring and summer downstream. This study proposes a multiobjective optimization framework incorporating an accumulated temperature index (ATI) as a biological objective alongside energy generation and flood control. Pareto-optimal solutions demonstrate that modest operational adjustments can substantially improve thermal conditions for fish reproduction without significantly compromising hydropower output.

---

### Flow regime alteration under progressive multi-reservoir development in the Upper Yangtze River

**Authors**: Zaichao Xie, Minglei Ren, Wei Xu et al.

**Journal**: *Journal of Hydrology: Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103694](https://doi.org/10.1016/j.ejrh.2026.103694) · **Citations**: 0

**Matched topics**: streamflow, reservoir
{: .label .label-green }

> The Upper Yangtze River basin contains 38 large reservoirs with 80.5 billion m³ live storage across its major tributaries. Coupling SWAT hydrological simulation with Indicators of Hydrologic Alteration (IHA) analysis, this study quantifies how progressive reservoir construction has homogenized the natural flow regime across tributary basins, with the most severe alterations in magnitude of low flows and timing of extreme events — a cumulative impact not apparent from individual dam studies.

---

### Optimizing environmental flow trade-offs for sustainable hydropower in a Himalayan reservoir

**Authors**: Yogesh Neupane, Rupesh Baniya, Mukesh Raj Kafle et al.

**Journal**: *Energy Nexus* · **DOI**: [10.1016/j.nexus.2026.100784](https://doi.org/10.1016/j.nexus.2026.100784) · **Citations**: 0

**Matched topics**: hydrology, hydropower
{: .label .label-green }

> Reservoir operations in the central Himalayas face competing demands from hydropower generation, irrigation, flood control, and downstream environmental flows. This study implements a multi-objective optimization framework for a Himalayan reservoir that explicitly balances energy generation against environmental flow requirements, demonstrating that intelligent scheduling can substantially reduce the trade-off between human and ecological water needs under climate variability.

---

### Three Gorges Reservoir operations regulate nitrogen transport and transformation via hydrodynamic control

**Authors**: Bei Nie, Yu Bai, Wei Zha, Xicheng Zhang et al.

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135996](https://doi.org/10.1016/j.jhydrol.2026.135996) · **Citations**: 0

**Matched topics**: hydrology
{: .label .label-green }

> This study examines how Three Gorges Reservoir impoundment and operational cycles regulate nitrogen transport and in-situ biogeochemical transformation in the reservoir body and downstream reach. Operating-induced changes in flow velocity, residence time, and stratification significantly alter the balance between denitrification, nitrification, and organic nitrogen mineralization — with measurable effects on the nitrogen load delivered to the middle and lower Yangtze and ultimately to the East China Sea.

---

## Water Resources, Drought, and Remote Sensing

This theme spans dataset development, drought monitoring, environmental flow assessment, and irrigation management — collectively advancing the empirical and observational foundation for large-scale water resources research. Seppä et al. publish CAMELS-FI, a major new large-sample catchment dataset covering 320 Finnish basins with hydrometeorological time series and 70+ landscape attributes, extending the CAMELS family into boreal-climate space where snowmelt and lake storage dynamics dominate. Laluet et al. present a complementary 0.25° global archive of irrigation water use (IWU) derived from multiple Earth Observation methods, addressing a critical gap in the terrestrial water cycle where IWU is the largest direct human intervention but remains poorly characterized at climate-relevant scales. Niranjannaik and Mishra quantify drought-driven shrinkage of 10,476 surface water bodies across India during 1990–2017, finding significant area losses tied to drought intensity and duration. Lueders et al. develop a modeling framework for reconstructing reference hydrology and quantifying hydrologic alteration across Texas — directly applicable to environmental flow policy. Ruffing and Freed challenge the common framing that higher irrigation efficiency necessarily improves conservation outcomes, pointing to the rebound effect where saved water is re-invested in more irrigated area. Wang et al. fill soil moisture data gaps in monitoring networks using a spatiotemporal consistency framework validated across diverse climate zones.

### CAMELS-FI: Hydrometeorological time series and landscape properties for 320 catchments in Finland

**Authors**: Iiro Seppä, Carlos Gonzales Inca, Jari Uusikivi, Petteri Alho

**Journal**: *Earth System Science Data* · **DOI**: [10.5194/essd-18-4745-2026](https://doi.org/10.5194/essd-18-4745-2026) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow
{: .label .label-green }

> Comprehensive, large-sample hydrological datasets such as CAMELS have driven major advances in hydrology by enabling cross-catchment learning and model benchmarking. CAMELS-FI extends this framework to 320 Finnish catchments, providing multi-decadal hydrometeorological time series and over 70 catchment attributes capturing boreal climate characteristics — snowmelt dynamics, lake storage, peatland coverage — that are underrepresented in existing CAMELS datasets. This dataset enables training and evaluation of hydrological models in high-latitude, snow-dominated regimes.

---

### Long-term irrigation water use datasets from multiple Earth Observation-based methods in major agricultural regions

**Authors**: Pierre Laluet, Jacopo Dari, Louise Busschaert, Zdenko Heyvaert et al.

**Journal**: *Earth System Science Data* · **DOI**: [10.5194/essd-18-4833-2026](https://doi.org/10.5194/essd-18-4833-2026) · **Citations**: 0

**Matched topics**: land surface model, irrigation, earth system model
{: .label .label-green }

> Irrigation water use (IWU) is widely considered the largest direct human intervention in the terrestrial water cycle, yet it remains poorly characterized at the spatial and temporal scales needed for climate research. This study presents a long-term archive of monthly IWU estimates at 0.25° spatial resolution derived from multiple Earth Observation methodologies, harmonized across major agricultural regions globally. The dataset provides a critical observational constraint for evaluating land surface models and ESMs that represent agricultural water demand.

---

### Drought driven shrinkage of surface water bodies in India

**Authors**: M. Niranjannaik, Vimal Mishra

**Journal**: *iScience* · **DOI**: [10.1016/j.isci.2026.116737](https://doi.org/10.1016/j.isci.2026.116737) · **Citations**: 0

**Matched topics**: drought, surface water
{: .label .label-green }

> Surface water bodies (SWBs) are vital for regional water storage, ecosystems, and human water demands. Analyzing 10,476 SWBs across India during 1990–2017 using satellite-based water extent data, this study demonstrates that drought events drive systematic shrinkage in SWB area, with larger and more severe droughts producing disproportionately greater losses. The results provide a quantitative basis for drought-SWB linkages that are largely absent from current regional water balance models.

---

### Reconstructing long-term historical hydrologic alteration to support environmental flows in Texas

**Authors**: Mark B. Lueders, Ryan A. McManamay, Jay A. Oliver, David Young et al.

**Journal**: *River Research and Applications* · **DOI**: [10.1002/rra.70172](https://doi.org/10.1002/rra.70172) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model
{: .label .label-green }

> Understanding hydrologic alteration is essential for watershed management and ecological conservation. This study develops a modeling framework to predict reference (pre-alteration) hydrology and quantify the degree of hydrologic alteration across Texas using publicly available geospatial data, providing a standardized methodology for environmental flow standard-setting that can be adapted to other regulated river systems.

---

### Irrigation efficiency and water conservation: Aligning outcomes for people and nature

**Authors**: Claire M. Ruffing, Zach Freed

**Journal**: *Frontiers in Water* · **DOI**: [10.3389/frwa.2026.1839103](https://doi.org/10.3389/frwa.2026.1839103) · **Citations**: 0

**Matched topics**: hydrology, streamflow, irrigation
{: .label .label-green }

> Agricultural water demand is the largest contributor to global water consumption. Increasing irrigation efficiency is often advocated as a path to conservation, but this study shows that efficiency gains do not automatically translate into reduced water consumption — higher efficiency frequently enables expansion of irrigated area, negating the saving through a rebound effect. The authors propose a reframing of efficiency policy to explicitly target consumptive use reduction and environmental flow maintenance.

---

### Filling data gaps in soil moisture monitoring networks via integrating spatiotemporal consistency

**Authors**: Weixuan Wang, Yizhuo Meng, Zushuai Wei, Linguang Miao et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4191-2026](https://doi.org/10.5194/hess-30-4191-2026) · **Citations**: 1

**Matched topics**: hydrologic model
{: .label .label-green }

> In situ soil moisture measurements are frequently compromised by sensor-derived data gaps that disrupt hydrological continuity. This study develops a spatiotemporal consistency framework that integrates neighboring station data, satellite soil moisture products, and land surface model outputs to reconstruct missing observations. The approach is validated across diverse climate zones and improves on existing gap-filling methods in both accuracy and gap-length tolerance, with direct utility for satellite validation campaigns.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 1,047 |
| After deduplication | 915 |
| After blocklist filtering | 869 |
| After LLM relevance filtering | 28 |
| Rejected (not relevant) | 841 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Journal of Hydrology | 4 |
| Hydrology and Earth System Sciences | 3 |
| Journal of Water Resources Planning and Management | 3 |
| Earth System Science Data | 2 |
| Hydrological Sciences Journal | 2 |
| Journal of Hydrology: Regional Studies | 2 |
| Communications Earth & Environment | 1 |
| Energy Nexus | 1 |
| Frontiers in Water | 1 |
| Geophysical Research Letters | 1 |
| Geoscientific Model Development | 1 |
| Int. Journal of Applied Earth Observation and Geoinformation | 1 |
| iScience | 1 |
| Machine Learning: Science and Technology | 1 |
| Nature Sustainability | 1 |
| River Research and Applications | 1 |
| Scientific Reports | 1 |
| Geography, Environment, Sustainability | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

---
layout: default
title: "Week 19 (May 4 - May 11), 33 papers"
parent: May
grand_parent: "2026"
nav_order: 34
date: 2026-05-18
categories: [weekly, 2026, may]
tags: [hydrology, literature-review, research]
paper_count: 33
highlight: "River channel changes can double flood exposure estimates, challenging fixed bankfull assumptions in global flood models (Comms Earth & Env)."
lang: en
lang_link: /zh/2026/may/2026-05-18-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 19** · May 4–May 11, 2026
{: .text-grey-dk-000 }

**33** relevant papers found across **6** themes
{: .fs-5 .fw-300 }

## Executive Summary

This week's literature highlights critical reassessments of how we model floods and droughts. A study in Communications Earth & Environment demonstrates that fixed bankfull capacity assumptions in global flood models systematically underestimate flood extent by up to 152%, while Nature Communications presents evidence that the post-drought runoff increase in West Africa represents a regime shift rather than a gradual recovery. Meanwhile, multiple studies advance machine learning approaches for streamflow and flood forecasting, with physics-enhanced LSTM models showing particular promise for operational early warning systems.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Flood Modeling & Risk Assessment

This week saw several important advances in flood modeling, with a particularly impactful finding that current global flood models systematically underestimate inundation by assuming a fixed two-year return period for river bankfull capacity. Hawker et al. demonstrate in the Mississippi basin that empirically-derived bankfull flows typically correspond to return periods below one year, leading to flood exposure underestimates of 15–472%. Complementing this structural critique, Voit et al. show that borrowing heavy precipitation events from hydrologically similar nearby catchments can substantially improve flood frequency analysis in data-scarce small basins. Meanwhile, two studies advance compound and pluvial flood mapping at meter-scale resolution, with Wang et al. developing a volume-conservative downscaling technique and Herpoel et al. evaluating parsimonious distributed frameworks for ungauged agricultural catchments.

### River channel change can affect flood hazard and impact substantially

**Authors**: Laurence Hawker, Stephen E. Darby, Louise Slater, Daniel R. Parsons, Richard J. Boothroyd, Philip J. Ashworth et al.

**Journal**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03517-9](https://doi.org/10.1038/s43247-026-03517-9) · **Citations**: 0

**Matched topics**: river, flood
{: .label .label-green }

> Abstract More than one billion people are exposed to flood risk globally, with this number projected to double by 2050. Global flood models underpin risk assessment and adaptation planning, yet typically assume that river bankfull capacity corresponds to a fixed two-year return period, neglecting spatial and temporal variability in channel characteristics. Here, we evaluate how inundated areas and population exposures respond when forced with empirically-derived bankfull capacities in the Mississippi basin using the Fathom Global Flood Model. We find that present-day bankfull flows generally correspond to return periods of less than one year, leading to systematic underestimation of flood extent (9–152%) and exposure (15–472%) across 5-, 20- and 100-year flood events, with the largest discrepancies for more frequent floods. We further show that historical changes in channel morphology can influence flood impacts at magnitudes comparable to projected climate change over multi-decadal timescales, depending on emission scenarios. Our work highlights a key structural limitation in current global flood modelling frameworks with implications for risk assessments.

---

### Considering rainfall events from a neighborhood improves local flood frequency analysis

**Authors**: Paul Voit, Felix Fauer, Maik Heistermann

**Journal**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-26-2189-2026](https://doi.org/10.5194/nhess-26-2189-2026) · **Citations**: 0

**Matched topics**: hydrologic model, flood
{: .label .label-green }

> Abstract. Many aspects of flood risk management require flood frequency analysis (FFA) which is, however, often limited by short observational records – especially for flash floods in small basins. In order to address this issue, we propose to extend the underlying data by local counterfactual scenarios. To that end, heavy precipitation events (HPEs) from nearby, hydrologically similar catchments are used to simulate flood peaks which are then included in the FFA for the catchment of interest. In order to demonstrate the added value of this approach, we used 23 years of radar-based precipitation and a hydrological model, fitted the Generalized Extreme Value (GEV) distribution to three different datasets – observed peaks, counterfactual peaks, and their combination –, and evaluated the resulting three GEV fits by means of the quantile skill score (QSS). For a sample of more than 13 000 German headwater catchments, we could show that local counterfactuals improved quantile estimation, with the level of improvement increasing with return period. The improvement declines when the radius of the transposition domain is extended beyond 30 km. Overall, our results provide a tangible perspective to enhance traditional FFA, producing narrower confidence intervals and more robust estimates for design floods and risk assessments.

---

### Probabilistic Flood Maps from Downscaled Compound Flood Ensembles Reveal Distinct Fluvial and Pluvial Impacts in Southeast Texas

**Authors**: Mark Wang, Paola Passalacqua, Ethan Coon, Saubhagya S. Rathore, Gabriel Perez

**Journal**: *ESSOAr* · **DOI**: [10.22541/essoar.15002812/v1](https://doi.org/10.22541/essoar.15002812/v1) · **Citations**: 0

**Matched topics**: hydrologic model, flood
{: .label .label-green }

> Flooding is one of the costliest natural hazards, and is particularly severe in Southeast Texas where low-relief terrain and intense rainfall produce compound floods driven by fluvial and pluvial processes. High-resolution compound flood modeling is computationally expensive because physically based hydrologic models must resolve groundwater–surface water interactions over large domains. To address this challenge, we develop a volume-conservative downscaling technique that refines coarse hydrologic model outputs to meter-scale inundation maps. We apply the technique to ensemble simulations from the Advanced Terrestrial Simulator (ATS), a fully distributed surface–subsurface hydrologic mode forced with 5,000 events generated with stochastic storm transposition and flood frequency analysis. The downscaling method redistributes ponded water volumes from the O(100 m) ATS unstructured mesh to a 1 m grid using terrain-based subgrid representations of fluvial and pluvial inundation. We use the resulting maps to evaluate both probabilistic flood hazard and infrastructure impacts. Compared with FEMA's 1% annual chance floodplain, the probabilistic maps show general agreement in fluvial corridors while revealing additional pluvial flooding in interior depressions. Relative to the coarse-resolution outputs, the downscaled maps reduce estimated building exposure and substantially increase detection of roadway flooding by resolving subgrid drainage patterns. Decomposing the downscaled impacts shows that fluvial flooding drives building exposure and deep roadway impacts; pluvial flooding causes widespread shallow roadway inundation. The downscaling framework enables efficient generation of probabilistic, meter-scale flood hazard maps from basin-scale hydrologic ensembles and provides a scalable pathway for improved flood risk communication and impact assessment.

---

### High-resolution mapping of pluvial flooding in ungauged agricultural catchments

**Authors**: Matthieu Herpoel, Pierre Baert, Charles Bielders, Gilles Swerts, Aurore Degré

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2511](https://doi.org/10.5194/egusphere-2026-2511) · **Citations**: 0

**Matched topics**: hydrology, runoff, flood
{: .label .label-green }

> Abstract. Accurate pluvial flood mapping in ungauged agricultural catchments is often constrained by a lack of calibration data. This study evaluates a parsimonious, high-resolution (1 m) distributed framework assessing peak discharge along concentrated flow paths, validated against 39 events in two nested experimental catchments (84 and 111 ha). The framework decouples the rainfall-runoff process to systematically compare adjusted SCS-CN formulations against two spatially explicit routing algorithms (SCS vs. SWRRB). Within this specific local context, findings demonstrate that the Jain initial abstraction method significantly reduces volumetric bias, with the distributed approach statistically outperforming lumped modelling. However, performance remains strictly regime-dependent, driven by rainfall intensity rather than total depth. This exposes the structural limits of static Curve Number (CN) parameterizations in capturing rapid Hortonian dynamics, causing the model to dampen minor events while amplifying high-intensity storms.

---

### Improving Basin‐Wide Flood Estimation From a Global Hydrological Model Through Spatiotemporal‐Pattern‐Based Machine Learning

**Authors**: Jiaqing Wang, Quan J. Wang, Jianshi Zhao

**Journal**: *Journal of Flood Risk Management* · **DOI**: [10.1111/jfr3.70224](https://doi.org/10.1111/jfr3.70224) · **Citations**: 0

**Matched topics**: hydrologic model, flood
{: .label .label-green }

> ABSTRACT When estimating future flood events using a global hydrological model (GHM), the large uncertainties associated with general circulation models (GCMs) and bias in the GHM model pose significant challenges. In the meantime, most future flood estimations are conducted only at specific gauge stations due to limited data availability and are unable to support basin‐wide water resources planning and management. To address these issues, we propose a spatiotemporal‐pattern‐based machine learning method, DSGPR‐EOF, which is a combination of Dual‐stage Sparse Gaussian Process Regression (DSGPR) and Empirical Orthogonal Function (EOF) analysis. DSGPR‐EOF is developed to improve the accuracy of basin‐wide flood estimations, including flood peak discharge, flood peak time, and flood volume. We apply the proposed method to the Brahmaputra River Basin (BRB), known for its topographical and climatic diversity, to evaluate the effectiveness and efficiency of the method. DSGPR‐EOF is shown to lead to higher accuracy in flood peak discharge estimation than the widely used multi‐GCMs ensemble mean method and several mainstream machine learning methods, including Support Vector Regression (SVR), Artificial Neural Network (ANN), and Long Short‐Term Memory (LSTM). Comprehensive comparisons reveal that DSGPR‐EOF achieves the lowest relative error of peak discharge (3.36%) among all compared methods, with particularly notable advantages in capturing higher‐order temporal patterns of flood dynamics. The errors in the estimated 10 and 100‐year flood peak discharges of DSGPR‐EOF are reduced by 68.6% and 54.5%, respectively, compared to SGPR‐EOF method.

---

## Drought Research

A striking finding this week from Peugeot et al. in Nature Communications reframes the well-known post-1970s runoff increase in West Africa's Sahel as a regime shift between alternative stable states, mediated by vegetation–runoff feedback loops, rather than a gradual trend. Belgium's 2011–2020 decade emerges as the driest since 1970 when assessed by reconstructed soil moisture rather than precipitation indices alone (Lekarkar et al.). Across the globe, Liu et al. provide a comprehensive analysis showing that drought propagation from meteorological to runoff to agricultural stages takes months and is primarily governed by temperature and evapotranspiration. In grasslands, Bai et al. document a paradox where vegetation greening actually exacerbates hydrological drought, while Cline et al. demonstrate the severe ecological consequences as streamflow drought reduces fish production by up to 90%.

### Evidence of hydrological regime shifts associated with a major decades-long drought in West Africa

**Authors**: Christophe Peugeot, Valentin Wendling, Erwan Le Roux, Gérémy Panthou, Basile Hector, Nathalie Rouché et al.

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-026-72648-6](https://doi.org/10.1038/s41467-026-72648-6) · **Citations**: 0

**Matched topics**: runoff, drought, land surface model
{: .label .label-green }

(Also featured in daily harvest on 2026-05-07)

> Using ground-based meteorological, hydrological and land cover datasets from 1950 to 2015, we provide evidence that the increase in runoff observed in the semi-arid central Sahel (West Africa) since the 1970-1995 drought is a shift between alternative stable states of low and high runoff. We propose a conceptual model, governed by feedback loops between vegetation and surface runoff, which describes the stabilising mechanisms of each state and the basin-scale impact of local shifts. While the drought was likely the trigger for the shift, land clearing and rainfall intensification may have reinforced it. Due to wetter conditions and greater resilience, other basins further south did not shift. Our study suggests that the shift towards higher runoff is due to surface processes playing a dominant role in this region, with minimal contribution from subsurface processes. This regime shift framework offers a promising perspective on understanding long-term hydrological changes.

---

### Reconstructed soil moisture droughts in Belgium reveal 2011–2020 was the driest decade since 1970

**Authors**: Katoria Lekarkar, Oldřich Rakovec, Rohini Kumar, Stefaan Dondeyne, Ann van Griensven

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2817-2026](https://doi.org/10.5194/hess-30-2817-2026) · **Citations**: 0

**Matched topics**: hydrologic model, drought, land surface model
{: .label .label-green }

> Abstract. In recent years, Belgium has experienced a sequence of intense droughts with wide-ranging impacts across multiple sectors. Determining whether these events are unprecedented or within natural variability requires indicators that properly diagnose drought. Root-zone soil moisture is a suitable indicator because it integrates meteorological forcings with land-surface processes. In Belgium, however, operational monitoring relies mainly on precipitation-based indices and lacks long-term in situ soil-moisture observations, leaving uncertainty about whether these indices capture the persistence of root-zone drought. To address this gap, we reconstructed daily root-zone soil-moisture dynamics over Belgium from 1970 to 2020 using the mesoscale Hydrologic Model (mHM), placing recent droughts in historical context and evaluating the adequacy of precipitation-based indicators for representing drought conditions. Our analysis shows that droughts in 2011–2020 were unprecedented in both duration and severity over the past five decades. Between 2011 and 2020, the country experienced a cumulative three years (non-consecutive) of drought exposure, representing 30 % of the decade. We further find that the Standardized Precipitation–Evapotranspiration Index (SPEI), currently used operationally as a proxy for agricultural droughts in Belgium, underestimates the persistence of root-zone droughts because it does not explicitly account for land-surface memory.

---

### Understanding meteorological, runoff, and agricultural drought propagation and their influencing factors in an ensemble of multiple datasets

**Authors**: Y.R. Liu, Tingting Hu, Jiawen Yang, Yu Lei

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2775-2026](https://doi.org/10.5194/hess-30-2775-2026) · **Citations**: 1

**Matched topics**: runoff, drought, land surface model
{: .label .label-green }

> Abstract. Understanding the propagation of diverse drought conditions is essential for effective drought preparedness. This study evaluated the propagation of meteorological, runoff, and agricultural droughts across global land areas from 1958 to 2024 using an ensemble of reanalysis data (ERA5), land surface model simulations (GLDAS), and merged observational datasets (TerraClimate). Two distinct methodological frameworks were employed to characterize drought propagation: time-lag correlation analysis and multi-threshold run theory. Based on standardized drought indices derived from precipitation, runoff, and soil moisture, the drought propagation characteristics of response time (RT), propagation rate (PR), and lag time (LT) were examined. Moreover, the climatic and geographical factors influencing drought propagation were quantified using the SHapley Additive exPlanations (SHAP)-based attribution method. The results demonstrate the propagation pathways of meteorological-runoff-agricultural drought at the global scale, with the average RT, PR, and LT from meteorological to runoff drought at 5.0 months, 55.3 %, and 1.23 months; from meteorological to agricultural drought at 8.7 months, 30.3 %, and 2.60 months; and from runoff to agricultural drought at 5.8 months, 35.0 %, and 2.49 months, respectively. Temperature and potential evapotranspiration are the primary factors influencing the propagation of meteorological drought to runoff drought, whereas precipitation plays a decisive role in the propagation from meteorological or runoff drought to agricultural drought.

---

### Vegetation greening drives hydrological drought: Spatiotemporal heterogeneity in a temperate grassland basin

**Authors**: Yanru Bai, Yixin Fang, Fanhao Meng, Min Luo, Hongguang Chen, Chula Sa et al.

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103514](https://doi.org/10.1016/j.ejrh.2026.103514) · **Citations**: 0

**Matched topics**: hydrology, drought
{: .label .label-green }

> The transboundary Kherlen River Basin, a temperate grassland basin spanning China and Mongolia. While recurrent droughts in recent decades have substantially altered global vegetation patterns, how these changes feed back to modulate hydrological processes, particularly hydrological drought, constitutes a critical knowledge gap. A novel Comprehensive index, the Comprehensive Hydrological Drought Assessment Index (CHDAI), was developed to bridge this gap. The CHDAI synthesizes surface runoff, soil moisture, groundwater, and snowmelt to provide a holistic measure of hydrological response. Results reveal a large-scale exacerbation of hydrological drought in the Kherlen River Basin, with 97.15% of its area experiencing a significant drying trend (P < 0.05). SEM revealed that vegetation influences hydrological drought through spatially heterogeneous pathways. At the basin scale, kNDVI exhibited a weak negative association with CHDAI, while in the middle and lower reaches, this association became more pronounced, highlighting the spatial complexity of vegetation-hydrology interactions.

---

### A comparative analysis of hydrological drought in the Rur catchment under human and natural impacts

**Authors**: You Wu, Daniel Bachmann, Holger Schüttrumpf

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103457](https://doi.org/10.1016/j.ejrh.2026.103457) · **Citations**: 0

**Matched topics**: streamflow, drought, surface water
{: .label .label-green }

> Rur river catchment, North Rhine-Westphalia (NRW), Germany. In a changing climate, the propagation of drought through coupled groundwater–surface water systems remains difficult to investigate, particularly in catchments strongly influenced by human activities. This study presents a joint analysis of groundwater and streamflow droughts in the anthropogenically influenced Rur river catchment. Standardized indices were computed for 209 groundwater wells (standardized groundwater level index, SGI) and 16 streamflow gauges (standardized streamflow index, SSI). Hierarchical clustering yielded five groundwater clusters (SGI_C1–SGI_C5) and three streamflow clusters (SSI_C1–SSI_C3). Regional groundwater droughts are strongly modulated by anthropogenic activities and local hydrogeology. Notably, SGI_C2 shows a persistent declining trend, associated with nearby lignite open-pit mining. Reservoir operations mitigate streamflow drought severity in SSI_C1 relative to SSI_C3, which more closely reflects natural flow and exhibits more pronounced droughts.

---

### Streamflow drought limits fish production across river ecosystems

**Authors**: Timothy J. Cline, Andrew B Lahr, Gregory Peterson, J Martin, David Schmetterling, Donovan Bell et al.

**Journal**: *bioRxiv* · **DOI**: [10.64898/2026.05.05.723077](https://doi.org/10.64898/2026.05.05.723077) · **Citations**: 0

**Matched topics**: river, streamflow, water management, drought
{: .label .label-green }

> Abstract River flows sustain biodiversity, ecosystem function, and human well-being, yet climate change and water extraction are driving frequent and severe low-flow conditions (i.e., streamflow droughts). Here, we show that declining streamflow constrains fish production by limiting juvenile recruitment, the dominant demographic pathway regulating population dynamics. Across populations, declining flows nonlinearly reduce carrying capacity and production, with severe drought reducing production by up to 90%. Flow–production relationships vary among rivers, revealing both drought-sensitive and drought-resilient responses shaped by ecological and hydrological context. In some systems, maintaining higher flows during average years yields greater ecological benefits than equivalent drought-year interventions. These results demonstrate that streamflow drought directly limits biological production and highlight how adaptive water management can be implemented to sustain freshwater ecosystems under increasing hydroclimatic variability.

---

## Hydrologic Modeling & Land Surface Models

Several studies this week push forward our understanding of terrestrial water storage, model forcing, and process representation. Robertson et al. assess TWS changes since the 1980s using an unprecedented multi-model ensemble, finding global TWS decline trends that remain poorly constrained (−0.72 to +0.04 mm/yr) and cautioning against artifacts in ERA5-Land. Wei et al. compare JRA-3Q and JRA-55 reanalysis datasets as land surface model forcing, while Shrestha et al. demonstrate that NOAA seasonal precipitation outlooks can be effectively downscaled for hydrologic modeling in Florida. In the Himalayas, Arora et al. integrate the VIC model with stable isotopes to show that groundwater-fed baseflow exceeds 97% of streamflow above 3000 m elevation during dry seasons. Climate projections receive attention from Boisramé et al., who argue that GCM ensembles should be selected based on locally-derived hydrologic metrics rather than purely climatic criteria.

### Assessing Terrestrial Water Storage Change Since the 1980s

**Authors**: Franklin Robertson, Michael Bosilovich, Matthew Rodell, Richard Allan, Bryant Loomis, Hiroko Beaudoing et al.

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2539](https://doi.org/10.5194/egusphere-2026-2539) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, land surface model
{: .label .label-green }

> Abstract. Water availability for societies and ecosystems depends upon Terrestrial Water Storage (TWS), yet global, spatially resolved measurements are largely unavailable before the advent of the Gravity Recovery and Climate Experiment (GRACE) gravimetric measurements in 2002. By exploiting a larger set of model and observations-based datasets than previously considered, along with statistical and machine learning techniques, we advance understanding of TWS changes since the 1980s, including accounting for human water management (HWM). A decline in TWS during 2002–2019 is identified for three global hydrologic models with HWM and bias-corrected precipitation forcing (-0.91 to -0.06 mm yr-1) with only one showing larger decreases than observed by GRACE observations (-0.80 mm y-1). We further identify a longer-term decline in TWS during 1980–2019 in these models, linked with regional precipitation decreases and the net effects of HWM through TWS drawdowns over northern India, southwest U.S. and northeastern China, yet the amplitude of the global land trends remains poorly quantified, ranging from -0.72 to +0.04 mm y-1. Our findings urge caution in inferring changes in hydroclimate variables from ERA5-Land and other reanalyses due to inhomogeneities in the assimilated observational data.

---

### Comparative analysis of JRA-3Q and JRA-55 reanalysis datasets as forcing for land surface model: implications for hydrological processes

**Authors**: Zixin Wei, Fan Bai, Zhongwang Wei, Yongjiu Dai

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135616](https://doi.org/10.1016/j.jhydrol.2026.135616) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, land surface model
{: .label .label-green }

> Abstract not available.

---

### Precipitation Forecasting for Hydrologic Modeling in West-Central Florida using Seasonal Climate Outlooks

**Authors**: Manoj Shrestha, Hui Wang, Jeffrey S. Geurink, Kshitij Parajuli, Tirusew Asefa, Fanzhang Zeng et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2703-2026](https://doi.org/10.5194/hess-30-2703-2026) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, seasonal
{: .label .label-green }

> Abstract. Seasonal precipitation forecasts play a vital role in short-term decision-making for water resources management, agriculture, and wildfire preparedness. NOAA's seasonal precipitation forecasts can be used at the local scale to further develop precipitation forecasts. This study evaluates the skill of NOAA's 3-month precipitation outlooks at a 0.5-month lead for the Alafia and Hillsborough River Basins in west-central Florida, using hindcasts from 1995 to 2019. Two non-parametric ensemble generation methods are introduced: Proportional Tercile Sampling (PTS) and Dominant Tercile Sampling (DTS). Results indicate that forecast skill peaks during the dry season (October to February), particularly for wet-tercile forecasts issued during El Niño years. Based on these findings, a hybrid strategy is recommended: apply DTS during late fall and winter to capitalize on strong climate signals and use PTS during other seasons to maintain reliability and operational value.

---

### Elevation-dependent groundwater control on baseflow in a himalayan catchment: an integrated isotopic–hydrological assessment

**Authors**: Siddharth Arora, Prosenjit Ghosh, Anil V. Kulkarni, Mao‐Chang Liang

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-49483-2](https://doi.org/10.1038/s41598-026-49483-2) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> Integrating the Variable Infiltration Capacity (VIC) hydrological model with stable isotope tracers, the study establishes a robust method for quantifying baseflow contributions, providing a reliable tool for Integrated Water Resource Management (IWRM) and allowing for cross-validation of simulated groundwater dynamics. Extensive seasonal sampling of river water, springs, and precipitation across elevation gradients was combined with calibrated hydrological simulations. Isotope-based mixing models and VIC outputs show good agreement, revealing a pronounced elevation-dependent increase in baseflow contribution during the dry season. Our study reports that baseflow is responsible for sustaining perennial streamflow, with contribution exceeding 70% at elevations above 1500 m, and up to 97.0 ± 1.5% at higher elevations (> 3000 m), thus acting as the primary water resource for supporting dry-season water demand.

---

### Think Globally, Model Locally: Complex Responses of Agricultural Water Supplies to Different Climate Projections

**Authors**: Gabrielle Boisramé, Beatrice Gordon, Christine M. Albano, Adrian Harpold, Rosemary Carroll

**Journal**: *JAWRA Journal of the American Water Resources Association* · **DOI**: [10.1111/1752-1688.70117](https://doi.org/10.1111/1752-1688.70117) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> ABSTRACT Many resource management plans use ensembles of global climate models (GCMs) to represent a range of potential future climates. Hydrologic models are used to translate these climates into projections of water resources to evaluate their long‐term vulnerability. GCM ensembles are typically selected for water resource vulnerability assessments based on their collective ability to represent the full range of projected regional changes in precipitation and temperature. However, this approach may miss potential hydrologic shifts due to the heterogenous and nonlinear impacts of climate on hydrology in snow‐dominated mountain headwaters. We demonstrate this challenge in the Walker River Basin (WRB) of California and Nevada. After comparing 32 climate projections and their associated hydrologic model (VIC) outputs we run subsets of projections through a water allocation model (MODSIM) to predict impacts on agricultural water use. Projected end‐of‐century changes in WRB precipitation vary (−20% to +40%) leading to an even greater range in projected streamflow changes (−50% to +75%). Model outputs suggest that maintaining historical levels of water supply reliability through 2100 would require > 50% greater mean annual streamflow.

---

### Detecting Land Use Change Impacts on Streamflow by Combining Field Data and Water Balance Modelling

**Authors**: İsmail Bilal Peker, Eren Dağra Sökmen, Ning Liu, Sezar Gülbaz, Ge Sun, Steven G. McNulty et al.

**Journal**: *JAWRA Journal of the American Water Resources Association* · **DOI**: [10.1111/1752-1688.70118](https://doi.org/10.1111/1752-1688.70118) · **Citations**: 0

**Matched topics**: hydrology, streamflow, land surface model
{: .label .label-green }

> ABSTRACT Over the last half‐century, land use changes, including deforestation, urban sprawl, and open‐pit surface mining, have accelerated across the Susurluk Basin in northwestern Türkiye. This study analysed how land use changes, damming and mining activities affected basin hydrology using empirical and analytical methods and the process‐based Water Supply Stress Index Model (WaSSI). The monthly WaSSI water balance model was validated using streamflow data from gaging stations between 1980 and 2005. Two of the eight subbasins exhibited streamflow reductions of about 32%–42%, with mean annual discharge decreasing between 1980–1989 and 1990–2005, primarily due to land use change rather than climate variability. The runoff coefficient (Runoff/Precipitation) dropped from 22% during 1980–1989 to 12% during 1990–2005 in one rural subbasin containing several surface‐mine ponds.

---

### A model of water extraction from the subglacial hydrologic system under idealized conditions

**Authors**: C. R. Meyer, Katarzyna Warburton, Aleah N. Sommers, Brent Minchew

**Journal**: *The Cryosphere* · **DOI**: [10.5194/tc-20-2659-2026](https://doi.org/10.5194/tc-20-2659-2026) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model
{: .label .label-green }

> Abstract. Subglacial water modulates glacier velocity across a wide range of space and time scales by influencing friction at the glacier bed. Here we consider the reverse: water extraction from the subglacial hydrologic system, which is a proposed intervention method intended to slow the flow of glaciers and reduce the associated sea-level rise. We set up these model experiments in the Subglacial Hydrology And Kinetic, Transient Interactions (SHAKTI) model coupled with the Ice-sheet and Sea-level System Model (ISSM). By analyzing the problem of an isolated borehole in a background pressure field, we find an approximate analytical solution which shows that the water pressure returns to the background value approximately as a logarithm with distance. Using the coupled SHAKTI-ISSM model, we perform transient model experiments on Helheim Glacier, Greenland and Thwaites Glacier, Antarctica, to determine the effects of water extraction on glacier velocity. With continuous pumping, we simulate a velocity decrease on the order of 1 %.

---

### Supporting climate change adaptation worldwide: A web application for exploring uncertain future changes in water resources

**Authors**: Petra Döll, Guillaume Attard, Fabian Kneier, Laura Müller

**Journal**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1829](https://doi.org/10.5194/egusphere-2026-1829) · **Citations**: 0

**Matched topics**: hydrologic model, climate change
{: .label .label-green }

> Abstract. While adaptation to changing water resources due to climate change is necessary everywhere, information about their potential future changes has not been easily accessible to most climate change adaptation processes. The free interactive web application Climate Change Impact of Water Resources (CCIWR) Explorer presents the output of a multi-model ensemble of global hydrological models. It provides state-of-the-art information to support participatory climate change adaptation processes worldwide. What makes the CCIWR Explorer unique is its ability to inform climate change adaptation decisions that account for stakeholder risk aversion. It not only shows the projected median future change in total water resources, groundwater resources, and evapotranspiration in the four seasons or annually, but also which fraction of the ensemble members project a change that stakeholders consider hazardous.

---

## Machine Learning & Deep Learning for Hydrology

This week saw a strong cluster of ML/DL applications spanning streamflow and flood forecasting. Bezerra et al. propose a physics-enhanced LSTM that incorporates inter-station lag times to improve very short-range flood forecasts, demonstrating that physically grounding neural networks improves both accuracy and interpretability. The VMD-LSTM hybrid from Shi et al. achieves 88.2% same-day flood peak detection in a high-altitude basin, compared to just 2.6% for standalone LSTM. At larger scales, the FloodSimBench dataset provides a new 1-meter resolution benchmark across 10 US metro areas for training foundation models. In urban settings, Zhang and Guo combine XGBoost with SHAP interpretability analysis for flood susceptibility mapping, while Kasaragod et al. demonstrate near-real-time soil moisture prediction using satellite thermal data and machine learning across multiple depths.

### Towards more accurate very short-range flood forecasts with physics-enhanced machine learning models

**Authors**: Rodrigo Bezerra, Julian Eleutério, Pedro Solha, Bruno Brentan, Carlos Mello, Manuel Herrera et al.

**Journal**: *Journal of Hydroinformatics* · **DOI**: [10.2166/hydro.2026.180](https://doi.org/10.2166/hydro.2026.180) · **Citations**: 0

**Matched topics**: streamflow, flood
{: .label .label-green }

> This paper proposes a physics-enhanced Long Short-Term Memory (LSTM) model to incorporate inter-station lag times into the model's feature selection and temporal configuration, improving flood forecasts. The framework is applied to a flood-prone urban basin using high-resolution (10-minute) rainfall and streamflow data, assessing both overall forecast skill and the accuracy of flood events, particularly the peak magnitude and timing errors. Results demonstrate that the physics-enhanced configuration consistently increases prediction accuracy by reducing redundancy among inputs. Moreover, it maintains the physical coherence of the hydrological processes, supporting the transition from black-box to grey-box modeling. The resulting architecture remained computationally efficient, highlighting the potential of physics-enhanced neural networks for operational and impact-based flood forecasting.

---

### Research on forecasting of diverse flood types based on the deep learning of sub-modal features in high-altitude mountainous basin

**Authors**: Xuyang Shi, J S Liu, Haidong Liang, Gonghuan Fang, Tie Liu, Xi Chen

**Journal**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103496](https://doi.org/10.1016/j.ejrh.2026.103496) · **Citations**: 0

**Matched topics**: runoff, flood
{: .label .label-green }

> This study examines the challenges in forecasting nonlinear and nonstationary flood processes in high-altitude mountainous watersheds. A hybrid model combining VMD (Variational Mode Decomposition) and LSTM (Long Short-Term Memory) was developed to flood simulate and forecast without any future reference information, and analyze the role of different sub-modal decomposition features in runoff sequence. The VMD-LSTM model significantly reduces the complexity of runoff signals by decomposing them into multiple sub-modal components across low- to high-frequency bands. Notably, the VMD-LSTM model achieves an 88.2% same-day peak discharge detection rate, substantially outperforming the standalone LSTM model, which only reaches 2.6%. Through the sub-model characteristics from low to high frequencies, the hybrid model hierarchically resolves the determinism of runoff accumulation and the uncertainty of short-term fluctuations during flood development.

---

### FloodSimBench: A Benchmark Dataset for Training Foundational Flood Inundation Models

**Authors**: Zhi Li, Songkun Yan, Mofan Zhang, Siyu Zhu, Yixin Wen, Alexander Sun et al.

**Journal**: *ESSOAr* · **DOI**: [10.22541/essoar.15002741/v1](https://doi.org/10.22541/essoar.15002741/v1) · **Citations**: 0

**Matched topics**: hydrology, flood
{: .label .label-green }

> FloodSimBench provides a 1m resolution benchmark for urban flood modeling across 10 major US metropolitan areas. Earth Observation foundation models outperform traditional CNNs in flood category segmentation, especially for extreme events. FloodSimBench enables both static flood severity mapping and continuous dynamic flood forecasting.

---

### Interpretable machine learning framework for urban flood susceptibility assessment: a multi-model comparison with spatial heterogeneity analysis in Yancheng

**Authors**: Xuan Zhang, Dongdong Guo

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-47925-5](https://doi.org/10.1038/s41598-026-47925-5) · **Citations**: 0

**Matched topics**: hydrology, flood
{: .label .label-green }

> Under the combined effects of global climate change and rapid urbanization, low-lying coastal plain cities face increasingly severe flood threats. This study developed an urban flood susceptibility assessment framework integrating multi-model comparison, SHAP interpretability analysis, and spatial heterogeneity evaluation, using Yancheng City as a case study. Based on 486 historical flood points and 10 conditioning factors, the predictive performance of Random Forest (RF), XGBoost, and Support Vector Machine (SVM) was compared. Results showed XGBoost performed best (AUC = 0.938, accuracy = 0.891), significantly outperforming RF (AUC = 0.912) and SVM (AUC = 0.876). SHAP analysis identified topographic wetness index (TWI), elevation, and impervious surface ratio as key driving factors, with a cumulative contribution of 47.6%.

---

### Deep Learning–Based Streamflow Forecasting in a Snowmelt-Dominated Basin: A Regime-Aware Evaluation

**Authors**: Roya Vazirian

**Journal**: *Journal of Hydrologic Engineering* · **DOI**: [10.1061/jhyeff.heeng-6651](https://doi.org/10.1061/jhyeff.heeng-6651) · **Citations**: 0

**Matched topics**: streamflow, water management
{: .label .label-green }

> This study provides a process-based perspective on how sequence models interact with snowmelt-driven hydrologic variability and characterizes their behavior across monthly and seasonal regimes relative to operational flow thresholds. Modeling and forecasting of discharge in the Henry's Fork basin are conducted using GRU and LSTM. Incorporating time-lagged SWE substantially improved model performance. Attribution analysis using integrated gradients reveals model-dependent driver importance, with SWE and temperature more influential in GRU and precipitation stronger in LSTM. At the overall performance level, GRU outperformed LSTM (NSE 0.87 versus 0.81). Monthly regime-disaggregated analysis confirmed GRU's advantage in most months and its stability during prolonged extremes and recession regimes, while LSTM retained an advantage in early melt-onset detection.

---

### Advanced Near Real-Time Soil Moisture Mapping using Thermal Remote Sensing and Machine Learning

**Authors**: Anush Kasaragod, Jobin Thomas, Thomas Oommen, Ryan Williams, Richard Dobson, Michael Cole et al.

**Journal**: *ESSOAr* · **DOI**: [10.22541/essoar.15002646/v2](https://doi.org/10.22541/essoar.15002646/v2) · **Citations**: 0

**Matched topics**: hydrology, land surface model
{: .label .label-green }

> Accurate soil moisture estimation is essential for agriculture, disaster management, and hydrology. In this study, a near-real-time multi-depth soil moisture prediction methodology has been developed using surface temperature data from the International Soil Moisture Network stations, along with other static (topography, soil texture) and dynamic (hydrometeorological) variables. An eXtreme Gradient Boosting (XGB) model was trained to predict soil moisture and validated, using land surface temperature (LST) from Landsat-8, Landsat-9, and ECOSTRESS datasets. Testing set performance (Pearson r: 0.901 - 0.937; ubRMSE: 0.038 - 0.047 m3/m3) across 5, 10, and 20 cm depths indicated low prediction error and minimal overfitting. Validation at independent locations using Landsat (r: 0.631 - 0.707; ubRMSE: 0.065 - 0.074 m³/m³) demonstrated transferable predictive capability.

---

## Hydropower & Reservoir Operations

Hydropower adaptation to climate change emerges as a major theme this week. Two independent studies tackle the same problem from different angles: Fidan and Bağatur propose a Francis–Pelton hybrid turbine configuration that improves energy output by 8% under drought, while Yildiz et al. introduce HyTUNE, a dynamic decision-support tool for timing turbine replacements to adapt to shifting water regimes. On the climate impacts side, Poudel and Ramtel project 30–65% increases in design flood magnitudes for small hydropower in Nepal under SSP585, highlighting urgent redesign needs. Dorthe et al. provide a nuanced assessment of hydropeaking mitigation, finding that only residual flow increases meaningfully reduce thermal threshold exceedances, but this benefit erodes under severe future climate scenarios.

### Adaptive Hybrid Turbine Switching for Drought-Resilient Hydropower Operation

**Authors**: Hüseyin Fidan, Tamer Bağatur

**Journal**: *Turkish Journal of Civil Engineering* · **DOI**: [10.18400/tjce.1806645](https://doi.org/10.18400/tjce.1806645) · **Citations**: 0

**Matched topics**: hydrology, streamflow, drought, hydropower
{: .label .label-green }

> This study evaluates hydroelectric performance under drought conditions through a scenario-based hybrid turbine operation strategy. Drought-induced hydrological variability leads to fluctuations in streamflow and consequently affects energy production continuity. In response, a Francis–Pelton hybrid configuration was assessed under five drought scenarios classified using the Streamflow Drought Index (SDI). Results indicate that the hybrid configuration improves low-flow performance and provides an additional annual energy gain of approximately 8% (4.86 GWh) compared to a single-turbine system. This corresponds to an increase in capacity factor from 49.4% to 53.3%. The study offers a methodological framework for evaluating hybrid turbine applicability under drought-induced hydrological variability.

---

### Assessing climate change impacts on design of small hydropower projects in Nepal using a process-based hydrological model with machine learning post-processor

**Authors**: Sandeep Poudel, Pradeep Ramtel

**Journal**: *Journal of Water and Climate Change* · **DOI**: [10.2166/wcc.2026.437](https://doi.org/10.2166/wcc.2026.437) · **Citations**: 0

**Matched topics**: hydrologic model, streamflow, hydropower
{: .label .label-green }

> ABSTRACT Small hydropower (SHP) projects are rapidly expanding in Nepal as a clean energy solution, yet their design typically only relies on historical streamflow records and overlooks climate-driven changes in extreme floods. This creates a risk of underestimating future flood magnitudes and infrastructure damage. This study evaluates projected changes in 25-, 50-, and 100-year design floods across four basins containing SHP in Nepal. Process-based HBV models were first calibrated for each basin, and a machine learning post-processor was developed to correct systematic residuals, improving streamflow simulation performance. The hybrid model was then forced with CMIP6 climate scenarios. Results show substantial increases in design flood magnitudes: about 10–30% under SSP245 and 30–65% under SSP585, with upper estimates exceeding 100% in some cases. These findings highlight the urgent need to integrate climate-informed flood estimates into SHP design to ensure resilient hydropower development in Nepal.

---

### Adaptive Turbine Replacement Improves Hydropower Flexibility in a Changing Climate

**Authors**: Veysel Yildiz, Nathalie Voisin, Marta Zaniolo

**Journal**: *ESSOAr* · **DOI**: [10.31223/x54b7r](https://doi.org/10.31223/x54b7r) · **Citations**: 0

**Matched topics**: hydrology, hydropower
{: .label .label-green }

> Hydropower Plants (HP) will operate under new conditions as water regimes shift, reservoir operating rules evolve, and the grid requires flexible balancing of wind and solar. This study introduces HyTUNE (Hydropower Turbine Upgrade and Next-generation Planning), a dynamic decision-support tool that integrates basin hydrology, plant hydraulics, and adaptive optimization to guide turbine replacement timing and configuration. HyTUNE shifts planning from reactive, end-of-life replacement toward proactive, information-driven strategies. Application to the Hoover Hydropower Plant demonstrates that HyTUNE's adaptive policies consistently outperformed conventional reactive strategies across diverse hydrologic futures. HyTUNE is of considerable practical relevance as hydropower systems worldwide confront the dual challenge of modernization and adaptation to future uncertainty and demand growth.

---

### Coordinated control strategy for load variations in hydropower plants cascaded by regulating reservoirs

**Authors**: Xiuwei Yang, Jiaping Gu, Jianbin Li, Yiqun Wang, Jijian Lian, Yonghong Zeng

**Journal**: *Energy* · **DOI**: [10.1016/j.energy.2026.141212](https://doi.org/10.1016/j.energy.2026.141212) · **Citations**: 0

**Matched topics**: reservoir, hydropower
{: .label .label-green }

> Abstract not available.

---

### Evaluating options to mitigate hydropower impacts on river thermal regimes in a changing climate

**Authors**: David Dorthe, Michael Pfister, Stuart N. Lane

**Journal**: *The Science of The Total Environment* · **DOI**: [10.1016/j.scitotenv.2026.181843](https://doi.org/10.1016/j.scitotenv.2026.181843) · **Citations**: 0

**Matched topics**: river, hydropower
{: .label .label-green }

> Storage hydropower alters the natural flow regime of rivers through reservoir impoundment, modified residual flows, and hydropeaking operations. These hydrological changes may also affect river temperatures and so aquatic ecosystems. This study evaluates the thermal effects of three hydropeaking mitigation strategies for a peri-Alpine river: regulation basin, diversion tunnel, and residual flow increase, under current and future climate conditions. Under current climate conditions, both regulation basins and residual flow increases significantly reduce short-term thermal rates of change (from approximately 7 to 4 °C/h), though values remain above those observed in natural rivers (around 1.5 °C/h). Only residual flow increases markedly reduce the number of days exceeding critical thermal thresholds (15 °C here), by up to 35 days. In contrast, diversion tunnels show negligible effect on thermal indicators. Under future climate scenarios, mitigation strategies maintain their relative effectiveness in limiting thermal gradients, but their ability to reduce threshold exceedances declines under the most severe climate scenarios, due to rising reservoir temperatures.

---

## Water Resources & Climate Change

A Nature Sustainability paper from Zhang et al. highlights the compound risk of amplified seasonal sediment transport for water infrastructure, bridging water scarcity and geomorphological change. In the Pan-Arctic Ob River Basin, Gan et al. discover that transient seasonal water bodies — not permafrost thaw alone — explain over 60% of the variability in runoff generation, offering a new remote-sensing-based constraint for Arctic hydrology. Climate change projections for the Oued Sebdou basin in Algeria forecast runoff reductions of 55–61% and deep aquifer recharge declines of up to 65% under SSP5-8.5, with dramatic seasonal shifts including a 205% increase in June runoff.

### Water scarcity and infrastructure risk of amplified seasonal sediment transport

**Authors**: Ting Zhang, Jim Best, Amy East, Lorenzo Rosa, Qianhan Wu, Yiyi Li et al.

**Journal**: *Nature Sustainability* · **DOI**: [10.1038/s41893-026-01829-4](https://doi.org/10.1038/s41893-026-01829-4) · **Citations**: 0

**Matched topics**: runoff, seasonal
{: .label .label-green }

> Abstract not available.

---

### Transient water bodies drive runoff variability across space and time in the Pan-Arctic Ob River Basin

**Authors**: Guojing Gan, Jinglu Wu, Ruibiao Yang, Long Ma, Jilili Abuduwaili, Galymzhan Saparov et al.

**Journal**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae692e](https://doi.org/10.1088/1748-9326/ae692e) · **Citations**: 0

**Matched topics**: runoff, land surface model
{: .label .label-green }

> Abstract Under global warming, land surface modifications have induced complex hydrological regime shifts in the Pan-Arctic region. The Ob River Basin, traversing the western Siberian lowland plains with extensive wetland systems, contributes approximately 1/6 of the Arctic Ocean's freshwater inputs. This study employs Landsat satellite imagery (1989–2017) to quantify water inundation frequency (WIF) and map permanent and seasonal water features. Contrary to conventional expectations, our analysis reveals that the normalized seasonal water area exhibits strong statistical correlations with runoff ratios across 13 watersheds with diverse aridity conditions. Applying the Budyko framework, we determine that land surface characteristic changes constitute the dominant positive driver of decadal runoff variations, with ephemeral water extent explaining over 60% of parameter variability. The observed expansion of seasonal water areas (1989–2017) enhances subsurface recharge, thereby amplifying runoff generation under permafrost degradation. Our findings underscore the need to integrate seasonal water-groundwater interactions in land surface models.

---

### ASSESSING CLIMATE CHANGE IMPACTS ON THE HYDROLOGICAL CYCLE IN OUED SEBDOU BASIN, NORTHWEST ALGERIA

**Authors**: Hachemaoui Anouar, Salhi Wafaa, M. Abbes, Nabil Beloufa, Abdelillah Otmane cherif, Fethellah Nour el houda et al.

**Journal**: *International Journal of Ecosystems and Ecology Science (IJEES)* · **DOI**: [10.31407/ijees16.241](https://doi.org/10.31407/ijees16.241) · **Citations**: 0

**Matched topics**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> This research investigates the hydrological impacts of climate change on the Oued Sebdou basin. The semi-distributed SWAT hydrological model was calibrated from 2003 to 2011 using SWAT-CUP and SUFI-2, resulting in excellent performance (NSE = 0.81, R² = 0.82, PBIAS = 8.6%). Ten CMIP6 GCMs were evaluated; EC-Earth3-CC was selected for its superior reproduction of regional temperature and rainfall. Bias-corrected forecasts under different SSP scenarios suggest a rise in potential evapotranspiration of 6.0% and 13.4%, total runoff reductions of approximately 55% and 61%, and deep aquifer recharge decreases of 55.5% and 65.0%, respectively. Pronounced seasonal shifts emerge under SSP5-8.5, with sharp runoff decreases in winter, spring, and autumn, and late-spring/early-summer peaks (up to +205% in June). These results highlight the vulnerability of semi-arid catchments to altered rainfall timing and intensity, with direct implications for the operation and reliability of the Beni Bahdel reservoir.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 1367 |
| After deduplication | 1102 |
| After LLM relevance filtering | 33 |
| Rejected (not relevant) | 1069 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Hydrology and Earth System Sciences | 4 |
| Journal of Hydrology Regional Studies | 3 |
| JAWRA Journal of the American Water Resources Association | 2 |
| Scientific Reports | 2 |
| EGUsphere | 3 |
| ESSOAr | 3 |
| Journal of Hydrology | 1 |
| Nature Communications | 1 |
| Communications Earth & Environment | 1 |
| Nature Sustainability | 1 |
| Environmental Research Letters | 1 |
| The Cryosphere | 1 |
| Journal of Flood Risk Management | 1 |
| Natural Hazards and Earth System Sciences | 1 |
| Journal of Hydroinformatics | 1 |
| Journal of Hydrologic Engineering | 1 |
| Journal of Water and Climate Change | 1 |
| Turkish Journal of Civil Engineering | 1 |
| Energy | 1 |
| The Science of The Total Environment | 1 |
| bioRxiv | 1 |
| IJEES | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

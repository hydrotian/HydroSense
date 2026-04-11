---
layout: default
title: "Week 52 (December 22 - December 28), 11 papers"
parent: December
grand_parent: "2025"
nav_order: 33
date: 2025-12-28
categories: [weekly, 2025, december]
tags: [hydrology, literature-review, research]
paper_count: 11
highlight: "A process-based crop model within an Earth system model projects less than 2% globally averaged crop production loss from drought by 2050, but identifies 62 countries facing losses above 10%."
lang: en
lang_link: /zh/2025/december/2025-12-28-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 52** · December 22–28, 2025
{: .text-grey-dk-000 }

**11** relevant papers found across **4** themes
{: .fs-5 .fw-300 }

## Executive Summary

The final week of 2025 delivered a cluster of high-impact papers on drought, land-water coupling, and deep learning for hydrology. A headline study in Nature Communications uses a process-based crop model embedded in an Earth system model to quantify how drought will shape global food security by 2050, while Nature Sustainability and Nature-Based Solutions highlight pathways for reconciling environmental and agricultural water demands through land-use and forest-management choices. Methodologically, the week showcases the maturing of deep learning for hydrology — with new vision-transformer and graph-based architectures for soil moisture, terrestrial water storage, and groundwater — alongside classic catchment-scale isotope and remote sensing studies.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Drought, Land Use, and Climate-Water Security

This week's most prominent signal concerns how climate change and land-management decisions jointly shape water availability for food and ecosystems. Carter et al. embed a process-based crop model inside an Earth system model to project that, although globally averaged drought-driven crop losses remain modest (<2% for most staples by 2050), 62 countries face maximum production losses above 10% and 24 above 20%, with South America, Africa, Eastern Europe, and Southeast Asia at greatest risk. Lester et al. move from impacts to solutions, arguing in Nature Sustainability that environmental and agricultural water demands can be simultaneously met under climate change if planning frameworks explicitly exploit their synergies. Hernández-Sosa et al. examine a complementary adaptation lever — large-scale native forest restoration in south-central Chile — and find that, under RCP8.5, native restoration in mid-to-upper basin areas buffers dry-season streamflow, while exotic plantations accelerate evapotranspiration and exacerbate flow declines.

### Impact of drought on global food security by 2050

**Authors**: V. A. Carter, K. Paff, D. Comeau, K. Solander, T. Pitts, S. Price et al.

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-025-67862-7](https://doi.org/10.1038/s41467-025-67862-7) · **Citations**: 4

**Matched topics**: drought, land surface model, earth system model
{: .label .label-green }

> Uses a process-based crop model within an Earth system model to assess drought impacts on maize, soybean, rice, and wheat production globally by 2050. Globally averaged losses are <2% (soybean up to 3.6%), but 62 countries face maximum production losses over 10% and 24 countries over 20%. A food insecurity index combining drought impacts with socio-economic factors flags large parts of South America, Africa, Eastern Europe, and Southeast Asia as the highest-risk regions.

---

### Synergies in environmental and agricultural water availability under climate change

**Authors**: R. E. Lester, D. Robertson, J. Bailey, G. Dwyer, G. Holt, S. Jalilov et al.

**Journal**: *Nature Sustainability* · **DOI**: [10.1038/s41893-025-01720-8](https://doi.org/10.1038/s41893-025-01720-8) · **Citations**: 2

**Matched topics**: water management, climate change
{: .label .label-green }

> Identifies synergies between environmental and agricultural water demand under climate change, arguing that the two needs can be simultaneously met when planning frameworks explicitly account for their overlapping benefits rather than treating them as competing uses.

---

### Assessing hydrological responses to large-scale native forest restoration as a nature-based solution in South-Central Chile

**Authors**: M. Hernández-Sosa, M. Aguayo, N. Cortes, A. Stehr, F. Frances, O. Llompart et al.

**Journal**: *Nature-Based Solutions* · **DOI**: [10.1016/j.nbsj.2025.100298](https://doi.org/10.1016/j.nbsj.2025.100298) · **Citations**: 2

**Matched topics**: hydrologic model, streamflow, climate change
{: .label .label-green }

> Simulates four forest-restoration scenarios with the TETIS hydrological model under RCP8.5 in two sub-basins of the Imperial River in Araucanía, Chile. Finds that climate change and land use together drive the largest hydrological changes; native forest restoration in mid-to-upper basins buffers streamflow during dry seasons, while exotic plantations increase evapotranspiration and accelerate flow declines.

---

## Deep Learning and Remote Sensing for Hydrology

A trio of deep-learning papers advances data-driven estimation of water states at multiple scales. Yan et al. introduce MSA-ViT, a vision-transformer framework that fuses multi-head self-attention with physical scattering theory to retrieve soil moisture from CYGNSS reflectivity, outperforming conventional regression and shallow neural networks across 3–60 day temporal aggregations. Gentner et al. present DeepRec, a CNN+LSTM architecture with ensemble-based uncertainty quantification that reconstructs monthly terrestrial water storage back to 1941 — filling the pre-GRACE gap and opening long-term hydrologic records to climate analysis. At the local scale, Zhuang et al. combine graph neural networks and recurrent networks into STGPM to predict groundwater levels in Jinan City, exploiting spatial connectivity between wells and multi-scale temporal dependencies to outperform standard time-series baselines.

### A Modified Hierarchical Vision Transformer for Soil Moisture Retrieval From CYGNSS Data

**Authors**: Q. Yan, Y. Chen, Y. Pan, S. Jin, W. Huang

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2024WR039476](https://doi.org/10.1029/2024WR039476) · **Citations**: 3

**Matched topics**: hydrologic model
{: .label .label-green }

> Introduces MSA-ViT, a multi-head self-attention vision transformer for soil moisture retrieval from CYGNSS reflectivity. The model integrates coherent-scattering physics with deep learning to capture nonlinear interactions between soil moisture, surface roughness, and vegetation attenuation. Training on 10-day averages and evaluation across 3–60 day scales show the approach outperforms linear regression, shallow neural networks, and prior DL models.

---

### DeepRec: Global Terrestrial Water Storage Reconstruction Since 1941 Using Spatiotemporal-Aware Deep Learning

**Authors**: L. Q. Gentner, J. Gou, M. J. Tourian, L. Börger, N. Sneeuw, B. Soja

**Journal**: *Journal of Geophysical Research: Machine Learning and Computation* · **DOI**: [10.1029/2025JH000889](https://doi.org/10.1029/2025JH000889) · **Citations**: 2

**Matched topics**: hydrology, hydrologic model, land surface model, earth system model
{: .label .label-green }

> Reconstructs monthly GRACE-like terrestrial water storage anomalies back to 1941 using a CNN+LSTM deep-learning architecture driven by climate reanalysis and land-use inputs. An ensemble approach quantifies both aleatoric and epistemic uncertainty. DeepRec extends the hydrological record by six decades prior to GRACE, enabling long-term climate analyses that were previously impossible.

---

### Enhancing groundwater level prediction with a hybrid deep learning model in Jinan City, China

**Authors**: C. Zhuang, L. Cui, Y. Cui

**Journal**: *Scientific Reports* · **DOI**: [10.1038/s41598-025-28200-5](https://doi.org/10.1038/s41598-025-28200-5) · **Citations**: 2

**Matched topics**: hydrology, hydrologic model
{: .label .label-green }

> Constructs a Spatio-Temporal Graph Prediction Model (STGPM) that integrates graph neural networks (for spatial relationships between monitoring wells) with recurrent networks (for temporal dynamics) to predict groundwater level fluctuations. STGPM achieves MAE = 0.039 and RMSE = 0.052 on test data, outperforming standard time-series models and addressing the challenge of nonlinear hydrogeological coupling.

---

## Hydrodynamic and Catchment-Scale Process Studies

Three papers drill into catchment-scale processes with observational and model-based approaches. Simard et al. introduce the NASA Delta-X framework — an airborne remote sensing and in situ system designed to calibrate hydrodynamic, sediment-transport, and ecogeomorphic models in the Mississippi River Delta, tackling the high spatial and temporal variability that limits spaceborne observations of coastal deltas. In the Upper Indus, Nasir et al. combine remote sensing with multi-method statistics to quantify how snow-cover variability propagates into runoff and hydropower potential, a question central to Pakistan's water security. Perry et al. use δ¹⁸O tracers in mountainous headwater streams of the Western Cascades to show how landslide and earthflow deposits sustain groundwater contributions and hydrologic connectivity even through dry seasons — a process too often missing from lumped catchment models.

### Delta-X: An airborne remote sensing framework to calibrate hydrodynamic and ecogeomorphic processes responsible for land building in coastal deltas

**Authors**: M. Simard, C. E. Jones, R. R. Twilley, E. Castañeda-Moya, S. Fagherazzi, C. G. Fichot et al.

**Journal**: *Remote Sensing of Environment* · **DOI**: [10.1016/j.rse.2025.115201](https://doi.org/10.1016/j.rse.2025.115201) · **Citations**: 3

**Matched topics**: hydrologic model, land surface model, surface water
{: .label .label-green }

> Presents the NASA Earth Venture-Suborbital Delta-X framework combining airborne radar and in situ measurements to calibrate and validate hydrodynamic, sediment-transport, morphodynamic, and ecogeomorphic models in the Mississippi River Delta. Applied to the active Atchafalaya basin (land-gaining) and the abandoned Terrebonne basin (land-losing), the framework tackles the spatial complexity and tidal-scale variability that challenge spaceborne approaches.

---

### Remote sensing and multi-method statistical analysis of snow cover variability and hydrological responses in the Upper Indus Basin

**Authors**: A. Nasir, S. Fahd, N. Wang, M. Zubair, A. A. Nadeem, Z. Zafar et al.

**Journal**: *Physics and Chemistry of the Earth* · **DOI**: [10.1016/j.pce.2025.104263](https://doi.org/10.1016/j.pce.2025.104263) · **Citations**: 4

**Matched topics**: hydrologic model, runoff, hydropower
{: .label .label-green }

> Combines remote sensing and multi-method statistical analyses to characterize snow-cover variability and its hydrological and hydropower consequences in the Upper Indus Basin, a region central to Pakistan's water and energy security.

---

### The Influence of Geomorphology on Storage and Surface Water–Groundwater Interactions in Mountainous Headwater Streams

**Authors**: Z. Perry, C. Segura, J. R. Brooks, S. Takaoka, F. J. Swanson

**Journal**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70361](https://doi.org/10.1002/hyp.70361) · **Citations**: 1

**Matched topics**: hydrology, streamflow, surface water
{: .label .label-green }

> Uses δ¹⁸O isotopic tracers in Western Cascades headwater catchments to show that landslide deposits and earthflow terrain create persistent groundwater contributions that sustain hydrologic connectivity through dry periods. Spatial isotope patterns indicate subsurface inter-catchment flow paths mediated by landslide geomorphology — processes rarely captured in standard lumped catchment models.

---

## Hydrological Knowledge and Water Management

Two papers in the Journal of Hydrology address the broader framing of hydrological science and its decision-relevance. Zwarteveen et al. open a special issue with a manifesto for a "grounded" socio-hydrology that values situated, contingent knowledge-making and methodological symmetry between hydrological and social-science traditions — pushing back against a lingering epistemic preference for detachment and replicability. Wang et al. examine the practical end of this question, diagnosing 1981–2024 multi-scale shifts in subtropical rainfall patterns and drawing out the implications for water management under nonstationarity.

### A situated proposal for a grounded approach to socio-hydrology

**Authors**: M. Zwarteveen, O. Barreteau, A. Ogilvie, M. Kuper, J.-P. Venot

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134828](https://doi.org/10.1016/j.jhydrol.2025.134828) · **Citations**: 3

**Matched topics**: hydrology
{: .label .label-green }

> Argues for a socio-hydrology that treats hydrological knowledge as contingent and situated, pursuing methodological symmetry between hydrological and critical social-science forms of knowing. Calls on hydrology to trade its epistemic preference for detachment and replicability for more modest, place-based engagement that reconnects knowledge-making to specific waters, communities, and politics.

---

### Multi-scale shifts in rainfall patterns in a subtropical region (1981–2024): challenges and implications for water management

**Authors**: H. Wang, T. Asefa, F. Getachew, Y. Zhou

**Journal**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134851](https://doi.org/10.1016/j.jhydrol.2025.134851) · **Citations**: 2

**Matched topics**: water management
{: .label .label-green }

> Examines multi-scale shifts in rainfall patterns across a subtropical region over 1981–2024, identifying the challenges that nonstationary precipitation poses for water management and supply planning.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers before dedup | 2,017 |
| Unique papers after dedup | 1,826 |
| After relevance filtering | 11 |
| Rejected (not relevant) | 1,815 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

**Sort mode**: established (citation-count-first for retrofit searches)

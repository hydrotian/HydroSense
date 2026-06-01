---
layout: default
title: "Week 21 (May 18 - May 25), 3 papers"
parent: June
grand_parent: "2026"
nav_order: 33
date: 2026-06-01
categories: [weekly, 2026, june]
tags: [hydrology, literature-review, research]
paper_count: 3
highlight: "New Love number solver in ISSM enables km-scale coupled ice-sheet/sea-level simulations; urban hydrology studies advance green infrastructure modeling and deep learning for streamflow."
lang: en
lang_link: /zh/2026/june/2026-06-01-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 21** · May 18–May 25, 2026
{: .text-grey-dk-000 }

**3** relevant papers found across **2** themes
{: .fs-5 .fw-300 }

## Executive Summary

A lighter week in the literature, with only Semantic Scholar returning results (OpenAlex experienced service issues). A notable advance in earth system modeling infrastructure comes from JPL's new Love number solver in ISSM, enabling high-resolution coupled ice-sheet and sea-level simulations. Two urban hydrology studies examine green infrastructure impacts on groundwater–surface water interactions and compare deep learning against physically based models for streamflow estimation under climate change.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Earth System Modeling Infrastructure

A significant computational advance for coupled ice-sheet and sea-level modeling: Caron et al. introduce a parallelized Love number solver within ISSM that pushes spherical harmonic resolution to degree ~10,000 and supports multiple viscoelastic rheologies (Maxwell, Burgers, Extended Burgers). The solver facilitates km-scale simulations of solid Earth response to ice mass changes, with numerical efficiency designed for large ensemble runs and uncertainty quantification — directly relevant to projecting future sea-level contributions from polar ice sheets within ESM frameworks.

### Love number computation within the Ice-sheet and Sea-level System Model (ISSM v4.24)

**Authors**: L. Caron, E. Ivins, E. Larour, S. Adhikari, L. Métivier

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-4031-2026](https://doi.org/10.5194/gmd-19-4031-2026) · **Citations**: 1

**Matched topics**: earth system model
{: .label .label-green }

> The Love number solver presented here is a new capability within the Ice-sheet and Sea-level System Model (ISSM) for computing the response of a 1D radially-symmetric solid Earth to tidal forcing and surface mass loading. This new capability allows solving zero-frequency free oscillation equations of motion decomposed into the well-known yi system and enables high wave number computations with spherical harmonic truncation degree of ~10,000 and above. It facilitates capturing the high-resolution response of the solid Earth to a step-function forcing in terms of gravity potential changes, vertical and horizontal bedrock displacement, and polar motion. The model incorporates compressible isotropic elasticity and three forms of linear viscoelasticity for mantle rheology: the Maxwell, Burgers, and Extended Burgers Materials (EBM). We detail our approach to the parallelization and numerical optimization of the solver, and report the accuracy of our results with respect to community benchmark solutions. Our main motivation is to facilitate simulations of a coupled system of surface mass transport (e.g. changes in polar ice sheets and sea level) and solid Earth models at kilometer-scale lateral resolutions with numerical efficiency that supports the exploration of large model ensembles and uncertainty quantification.

---

## Urban Hydrology and Streamflow Modeling

Two studies tackle urban water challenges from complementary angles. Masoudiashtiani and Peralta use MODFLOW with streamflow routing to quantify how grass swales can enhance aquifer recharge and surface water availability over 12-month timescales in Utah's Red Butte Creek watershed — finding that about two-thirds of green-infrastructure-induced recharge flows downgradient and 30% returns to streams. Meanwhile, Balacumaresan et al. benchmark deep learning against physically based models for urban streamflow estimation, evaluating performance under both historical and projected future climate conditions.

### Predicted Hydrologic Changes Due to Urban Green Infrastructure Implementation

**Authors**: S. Masoudiashtiani, Richard C. Peralta

**Journal**: *Environments* · **DOI**: [10.3390/environments13050279](https://doi.org/10.3390/environments13050279) · **Citations**: 0

**Matched topics**: hydrologic model
{: .label .label-green }

> Numerical simulations quantify the transient impacts of implementing green infrastructure (GI) grass swales on unconfined aquifer storage and groundwater-surface water interactions around the Red Butte Creek (RBC) of Utah, USA. The Red Butte Creek Watershed (RBCW) transitions from undeveloped mountainous National Forest land to downstream urbanized areas within Salt Lake Valley (SLV). This reconnaissance-level study demonstrates that increasing stormwater infiltration in urbanized areas during the rainy months (April-June) can, until at least the subsequent March, (a) enhance aquifer recharge and support sustainable groundwater yields; and (b) improve surface water availability. Simulations predict hydrologic impacts of aquifer recharge resulting from hypothetical grass-swale implementation within a 704-acre area located around RBC. The employed model, HyperRBC, is an adaptation of a United States Geological Survey (USGS) transient numerical flow, MODFLOW, model implementation for SLV. Adaptations involved (a) uniformly refined horizontal discretization of seven aquifer layers within a sub-area encompassing parts of RBCW and an adjacent watershed; (b) updated input data; and (c) MODFLOW's Streamflow-Routing (SFR) package to simulate RBC flow and aquifer-stream seepage. Model predictions indicated that by the end of next March: (a) about 3% of the GI-induced recharge would remain within the unconfined aquifer in the HyperRBC area; (b) 66.6% of the recharge would flow northward into the downgradient continuation of the unconfined aquifer; and (c) 30.3% would discharge to nearby stream and river.

---

### Evaluation of Deep Learning and Physically Based Models for Urban Streamflow Estimation Under Historical and Future Climate Conditions

**Authors**: Harshanth Balacumaresan, M. Imteaz, I. Hossain, Md Abdul Aziz, Tanveer Choudhury

**Journal**: *Water Resources Management* · **DOI**: [10.1007/s11269-026-04751-8](https://doi.org/10.1007/s11269-026-04751-8) · **Citations**: 0

**Matched topics**: streamflow
{: .label .label-green }

> Abstract not available.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 13 |
| After deduplication | 10 |
| After LLM relevance filtering | 3 |
| Rejected (not relevant) | 7 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Geoscientific Model Development | 1 |
| Environments | 1 |
| Water Resources Management | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

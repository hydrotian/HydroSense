---
layout: default
title: "Week 44 (Oct 26 - Nov 02), 2 papers"
parent: November
grand_parent: "2026"
nav_order: 33
date: 2026-11-09
categories: [weekly, 2026, november]
tags: [hydrology, literature-review, research]
paper_count: 2
highlight: "Mamba state-space models match Transformer accuracy for 120-h streamflow forecasting across 125 Iowa watersheds, while a new two-stage Rosenbrock solver cuts E3SM atmospheric chemistry integration time by 33%."
lang: en
lang_link: /zh/2026/november/2026-11-09-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 44** · Oct 26–Nov 02, 2026
{: .text-grey-dk-000 }

**2** relevant papers found across **2** themes
{: .fs-5 .fw-300 }

## Executive Summary

A slow week with limited coverage due to OpenAlex API rate-limiting (429 errors) during the search, leaving only Semantic Scholar results. Two notable papers emerged: one advances deep-learning streamflow forecasting using Mamba's state-space architecture for long-horizon, multi-watershed generalization, and another improves the computational efficiency of E3SMv1's atmospheric chemistry solver by 33% — directly relevant to running coupled land-atmosphere simulations at scale.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Machine Learning for Streamflow Forecasting

The application of modern sequence modeling architectures to hydrological forecasting continues to expand. Demiray and Demir evaluate the Mamba architecture — a state-space model (SSM) designed for efficient long-sequence processing — against Transformers, LSTMs, GRUs, and Seq2Seq models for 120-hour ahead streamflow prediction across 125 geographically diverse Iowa watersheds. The results show Mamba achieving accuracy comparable to Transformer models, with both significantly outperforming classical recurrent approaches. Notably, the authors apply SHAP (SHapley Additive exPlanations) to illuminate each model's internal feature utilization, revealing distinct decision patterns that enhance interpretability. For operational hydrologic forecasting, this combination of multi-step generalization and built-in explainability positions Mamba as a computationally efficient alternative worth evaluating at continental scale.

### Advancing long-horizon hydrological forecasting: a Mamba-based approach with explainable AI for generalized streamflow prediction

**Authors**: B. Demiray, Ibrahim Demir

**Journal**: *Journal of Hydroinformatics* · **DOI**: [10.2166/hydro.2026.115](https://doi.org/10.2166/hydro.2026.115) · **Citations**: 2

**Matched topics**: streamflow
{: .label .label-green }

> Accurate long-horizon streamflow forecasting is crucial for water resource management, but existing models often face efficiency and interpretability challenges. This study comprehensively evaluates the Mamba architecture, which utilizes state-space models (SSMs) for efficient sequence processing, for 120-h hourly generalized streamflow prediction across 125 diverse Iowa watersheds using 72-h historical inputs. Performance was benchmarked against Persistence, long short-term memory, gated recurrent unit, Seq2Seq, and Transformer models employing Nash–Sutcliffe efficiency, Kling–Gupta efficiency, Pearson's r, and normalized root-mean-square error. Results demonstrate that Mamba architecture achieves predictive accuracy comparable to, and in several aspects marginally exceeding, the robust Transformer baseline, with both models significantly outperforming other established methods. Critically, explainable AI using SHAP values provided insights into tested models' decision-making, revealing distinct feature utilization patterns and enhancing model transparency. This research highlights Mamba's potential as an efficient, accurate, and interpretable alternative for advancing operational long-range hydrological forecasting.

---

## Earth System Model Computational Efficiency

Improving the numerical efficiency of Earth System Models is essential for enabling higher-resolution, longer, or more ensemble-member climate simulations. Chien and Fu address one of E3SM's major computational bottlenecks — the integration of stiff atmospheric chemical systems — by implementing a semi-implicit two-stage Rosenbrock (ROS2) solver in E3SMv1. Tested across two chemical mechanisms of different complexity (chemUCI with 60 species and trop_strat_mozart_mam4 with 155 species), ROS2 reduces chemistry integration time by approximately 33% on the Cori/KNL platform relative to the original implicit solver, while maintaining numerical stability and global-mean ozone differences within 1 ppb over one-year integrations. The results support ROS2 as a production-ready alternative when E3SM chemistry is run at short timesteps, though the authors note additional benchmarking on modern CPU/GPU systems is needed to characterize performance portability.

### Using a two-stage Rosenbrock solver to increase computational efficiency in the DOE's Exascale Earth System Model version 1 (E3SMv1)

**Authors**: Rong-You Chien, Joshua S. Fu

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-10309-2026](https://doi.org/10.5194/gmd-19-10309-2026) · **Citations**: 0

**Matched topics**: earth system model
{: .label .label-green }

> The integration of stiff atmospheric chemical systems is a major computational cost in Earth System Models and poses challenges for numerical stability as chemical complexity and temporal resolution increase. In this study, we implement a semi-implicit two-stage Rosenbrock method (ROS2) in the Energy Exascale Earth System Model version 1 (E3SMv1) and evaluate it as an alternative chemistry time-integration scheme. ROS2 is tested with two interactive chemical mechanisms of substantially different size: chemUCI (60 prognostic species) and trop_strat_mozart_mam4 (155 prognostic species). Numerical experiments include short simulations to quantify computational cost, a box-model timestep-refinement analysis, and one-year integrations to examine numerical stability and solution sensitivity. At the same 180 s chemistry timestep, ROS2 requires approximately 33% less chemistry integration time than the original iterative implicit solver on the tested Cori/KNL CPU platform. The magnitude of this speedup is configuration dependent. Global-mean surface-ozone differences among the tested configurations are small (≤ 1.03 ppb), and the one-year integrations show no evidence of numerical instability. Spatial and diurnal differences in ozone, NO, NO₂, and OH are species- and mechanism-dependent, indicating sensitivity to both timestep and solver formulation rather than a common systematic bias. These results support ROS2 as a lower-cost alternative to the current implicit integrator when E3SM chemistry is operated at short timesteps; additional timestep-refinement tests and benchmarking on contemporary CPU/GPU systems are needed to quantify coupled-model convergence and performance portability.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 5 |
| After deduplication | 5 |
| After LLM relevance filtering | 2 |
| Rejected (not relevant) | 3 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Journal of Hydroinformatics | 1 |
| Geoscientific Model Development | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

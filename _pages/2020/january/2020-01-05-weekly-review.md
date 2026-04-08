---
layout: default
title: "Week 01 (December 30, 2019 – January 5, 2020), 3 papers"
parent: January
grand_parent: "2020"
nav_order: 33
date: 2020-01-05
categories: [weekly, 2020, january]
tags: [hydrology, literature-review, research]
paper_count: 3
highlight: "Early-2020 foundations: CMIP6 climate sensitivity diagnosed, the TRY plant trait database expanded, and LSTM-seq2seq rainfall-runoff modeling introduced."
lang: en
lang_link: /zh/2020/january/2020-01-05-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 01** · December 30, 2019 – January 5, 2020
{: .text-grey-dk-000 }

**3** relevant papers found across **2** themes
{: .fs-5 .fw-300 }

## Executive Summary

The opening week of 2020 delivered several highly-cited contributions that have since shaped hydrology and earth system modeling. In *Geophysical Research Letters*, Zelinka et al. diagnosed why equilibrium climate sensitivity increased substantially in CMIP6 relative to CMIP5, tracing the rise to changes in extratropical low-cloud feedback. *Global Change Biology* published a substantially expanded version of the TRY plant trait database, a foundational data resource for land-surface and earth system models. And in *Water Resources Research*, Xiang, Yan, and Demir introduced an LSTM-based sequence-to-sequence rainfall-runoff model — an early and influential demonstration of deep learning for hourly hydrologic forecasting.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Earth System Model Analysis and Data Foundations

This week brought two high-impact contributions to the data and analysis backbone of earth system modeling. Zelinka and colleagues tackled one of the most important open questions in climate science — why CMIP6 models exhibit higher equilibrium climate sensitivity than CMIP5 — tracing the increase to stronger extratropical low-cloud feedbacks driven by changes in cloud coverage and opacity. In parallel, Kattge et al. released an enlarged and openly-licensed version of TRY, the global plant trait database that underpins vegetation parameterization in land-surface and earth system models. Together the two papers illustrate the complementary roles of diagnostic analysis and shared data infrastructure in shaping the next generation of climate and land-atmosphere models.

### Causes of Higher Climate Sensitivity in CMIP6 Models

**Authors**: Mark D. Zelinka, Timothy A. Myers, Daniel T. McCoy, Stephen Po-Chedley, Peter Caldwell, Paulo Ceppi et al.

**Journal**: *Geophysical Research Letters* · **DOI**: [10.1029/2019gl085782](https://doi.org/10.1029/2019gl085782) · **Citations**: 1,757

**Matched topics**: earth system model
{: .label .label-green }

> Equilibrium climate sensitivity, the global surface temperature response to CO₂ doubling, has been persistently uncertain. This analysis shows that effective climate sensitivity has increased substantially in CMIP6 relative to CMIP5, and attributes the rise primarily to stronger extratropical low-cloud feedbacks — driven by changes in cloud fraction and opacity — rather than to tropical cloud changes. The finding has since become a reference point for interpreting the higher end of CMIP6 warming projections.

---

### TRY Plant Trait Database – Enhanced Coverage and Open Access

**Authors**: Jens Kattge, Gerhard Bönisch, Sandra Díaz, Sandra Lavorel, I. Colin Prentice, Paul Leadley et al.

**Journal**: *Global Change Biology* · **DOI**: [10.1111/gcb.14904](https://doi.org/10.1111/gcb.14904) · **Citations**: 2,005

**Matched topics**: earth system model
{: .label .label-green }

> Plant traits — morphological, anatomical, physiological, biochemical, and phenological characteristics — determine how plants respond to the environment and how they mediate ecosystem fluxes of water, carbon, and energy. This release expands TRY's coverage and moves the data to open access, broadening the data foundation for vegetation and land-surface modeling, functional ecology, biodiversity conservation, and ecosystem-scale remote-sensing work. TRY has since become the de facto global repository underpinning trait-based parameterizations in earth system models.

---

## Deep Learning for Rainfall-Runoff Modeling

A third standout paper from the week introduced one of the early canonical applications of deep sequence models to hydrologic forecasting. Xiang, Yan, and Demir applied an LSTM-based sequence-to-sequence (seq2seq) architecture to hourly rainfall-runoff prediction in two Iowa watersheds, and benchmarked it against linear regression, ridge and lasso regression, support vector regression, Gaussian process regression, and a vanilla LSTM. The seq2seq formulation — which produces multi-step forecasts while honoring long-range dependencies — outperformed every baseline, helping to cement LSTM architectures as a default building block for the deep-learning hydrology wave that followed.

### A Rainfall-Runoff Model With LSTM-Based Sequence-to-Sequence Learning

**Authors**: Zhongrun Xiang, Jun Yan, İbrahim Demir

**Journal**: *Water Resources Research* · **DOI**: [10.1029/2019wr025326](https://doi.org/10.1029/2019wr025326) · **Citations**: 738

**Matched topics**: hydrology, runoff
{: .label .label-green }

> Rainfall-runoff modeling is a complex nonlinear time-series problem. This study applies an LSTM-based sequence-to-sequence (seq2seq) architecture to hourly rainfall-runoff prediction in the Clear Creek and Upper Wapsipinicon watersheds in Iowa, using rainfall observations, rainfall forecasts, runoff observations, and monthly evapotranspiration climatology as inputs. Evaluated against linear regression, Lasso, Ridge, support vector regression, Gaussian process regression, and a vanilla LSTM, the seq2seq model outperforms every baseline on Nash-Sutcliffe efficiency, correlation, bias, and normalized RMSE — and the paper argues that seq2seq is broadly effective for hydrologic time-series prediction and short-term flood forecasting.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers before dedup | 2,167 |
| Unique papers after dedup | 2,001 |
| After LLM relevance filtering | 3 |
| Rejected (not relevant) | 1,998 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Global Change Biology | 1 |
| Geophysical Research Letters | 1 |
| Water Resources Research | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

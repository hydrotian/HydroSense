---
layout: default
title: "Week 39 (Sep 21 - Sep 28), 1 paper"
parent: September
grand_parent: "2026"
nav_order: 35
date: 2026-09-28
categories: [weekly, 2026, september]
tags: [hydrology, literature-review, research]
paper_count: 1
highlight: "Deep learning data assimilation of sun-induced fluorescence into the ISBA land surface model enables more accurate vegetation-hydrology coupling in Earth system simulations (Biogeosciences)."
lang: en
lang_link: /zh/2026/september/2026-09-28-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 39** · Sep 21–Sep 28, 2026
{: .text-grey-dk-000 }

**1** relevant paper found across **1** theme
{: .fs-5 .fw-300 }

## Executive Summary

Week 39 was unusually quiet in the hydrology and water resources literature, with Semantic Scholar returning only one qualifying paper after ISSN-based venue filtering (OpenAlex was unavailable due to rate-limiting throughout this run). The single paper advances land surface modeling methodology, applying deep learning to assimilate satellite-observed sun-induced fluorescence into the ISBA model — a technique with direct relevance to improving coupled vegetation–hydrology representation in Earth system models.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Machine Learning for Land Surface Model Data Assimilation

Data assimilation — the process of combining model states with observations — is a longstanding challenge in land surface and Earth system modeling. Vanderbecken et al. address this challenge using deep learning to incorporate sun-induced fluorescence (SIF) from the TROPOMI instrument aboard Sentinel-5P into the ISBA land surface model. SIF provides a direct, near-real-time proxy for gross primary productivity and canopy light use efficiency, and by training a neural network surrogate to bridge the model's prognostic states and the satellite-retrieved SIF signal, the authors demonstrate improved representation of vegetation dynamics in ISBA. The approach is notable for its compatibility with coupled modeling frameworks and its potential to be extended to other satellite observation streams, including those relevant to water stress and soil moisture estimation.

### Using deep learning to assimilate sun-induced fluorescence satellite observations in the ISBA land surface model

**Authors**: P. Vanderbecken, J. Vural, Oscar Rojas-Muñoz, S. Garrigues, B. Bonan, C. Bacour et al.

**Journal**: *Biogeosciences* · **DOI**: [10.5194/bg-23-6687-2026](https://doi.org/10.5194/bg-23-6687-2026) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Accurate representations of the surface and vegetation are critical for simulating the terrestrial CO₂ cycle in response to climate and meteorological conditions. To meet this challenge, an increasing number of satellite missions are being launched which can monitor vegetation conditions and biomass. One is the Copernicus Sentinel-5P mission, which carries the TROPOMI instrument and retrieves sun-induced fluorescence (SIF), a signal directly related to photosynthetic activity. We present a deep learning-based data assimilation approach to ingest TROPOMI SIF observations into the ISBA land surface model, improving its simulation of vegetation dynamics and surface–atmosphere carbon exchange. The method demonstrates strong potential for integration with coupled land–atmosphere modeling frameworks.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 1 |
| After deduplication | 1 |
| After journal filtering (blocklist) | 1 |
| After LLM relevance filtering | 1 |
| Rejected (not relevant) | 0 |

**Note**: OpenAlex returned HTTP 429 (rate limit) errors for all 16 topics this week — all results are from Semantic Scholar only. This significantly reduced coverage; the low paper count reflects API availability, not a quiet publishing week.

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Biogeosciences | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

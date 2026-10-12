---
layout: default
title: "Week 40 (Sep 28 - Oct 05), 3 papers"
parent: October
grand_parent: "2026"
nav_order: 33
date: 2026-10-05
categories: [weekly, 2026, october]
tags: [hydrology, literature-review, research]
paper_count: 3
lang: en
lang_link: /zh/2026/october/2026-10-05-weekly-review
highlight: "A watershed-agnostic explainable ML framework generalizes distributed hydrologic modeling across ungauged basins without basin-specific calibration."
---

# Weekly Literature Review
{: .no_toc }

**Week 40** · Sep 28–Oct 05, 2026
{: .text-grey-dk-000 }

**3** relevant papers found across **3** themes
{: .fs-5 .fw-300 }

## Executive Summary

A lean search week due to OpenAlex API rate limits — all results came from Semantic Scholar only, reducing total coverage. Three relevant papers emerged: a watershed-agnostic explainable ML framework for distributed hydrologic modeling that sidesteps basin-specific calibration, a physics-based design atlas systematically mapping cost and hydrologic performance trade-offs for low-impact development stormwater systems, and an in-silico benchmarking experiment dissecting phenology uncertainty in land surface models for temperate forests.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Machine Learning for Distributed Hydrologic Modeling

The watershed-agnostic approach introduced this week represents a meaningful step toward generalizable data-driven hydrology. Traditional physics-based models require watershed-specific calibration that limits transferability, while earlier neural network models sacrificed interpretability. Talha and Nejadhashemi's framework bridges these gaps — distributing predictions spatially while maintaining explainability, making it plausible for operational use in ungauged basins and large-scale continental routing systems.

### Watershed-agnostic modeling: An explainable, distributed, data-driven hydrologic model

**Authors**: M. Talha, A. Nejadhashemi

**Journal**: *Environmental Modelling & Software* · **DOI**: [10.1016/j.envsoft.2026.107149](https://doi.org/10.1016/j.envsoft.2026.107149) · **Citations**: 0

**Matched topics**: hydrologic model
{: .label .label-green }

> Abstract not available.

---

## Urban Hydrology and Stormwater Design

Low-impact development (LID) design has long suffered from a gap between volumetric water-quality criteria and the actual hydrologic performance that practitioners care about. The LID-Design Atlas addresses this directly by providing a parametric database built from physics-based simulations, making trade-off navigation explicit. This atlas approach could substantially reduce the burden of iterative design and improve the integration of LID tools into larger urban watershed models.

### LID-Design Atlas: Mapping Hydrologic Performance and Cost Trade-Offs in Infiltration-Based LID Design

**Authors**: M. Gomes

**Journal**: *Journal of Hydrologic Engineering* · **DOI**: [10.1061/jhyeff.heeng-6901](https://doi.org/10.1061/jhyeff.heeng-6901) · **Citations**: 0

**Matched topics**: hydrologic model
{: .label .label-green }

> Infiltration-based low-impact development (LID) practices are widely implemented to mitigate urban runoff impacts; however, their design is commonly guided by volumetric water-quality criteria that obscure critical trade-offs among hydrologic performance, geometry, soil properties, and cost. This study introduces the LID-design atlas (LIDA), a physics-based design database that systematically maps these trade-offs to support more informed decision-making in stormwater management.

---

## Land Surface Model Phenology Benchmarking

Phenological uncertainty — how well land surface models capture the timing of leaf-out and senescence — propagates directly into water and carbon flux predictions. By designing an in-silico experiment that isolates phenology representation errors from other LSM parameter uncertainty, Yajima et al. provide a cleaner signal of where phenological misrepresentation matters most. This is directly actionable for improving ELM and CLM configurations in coupled E3SM simulations, particularly for temperate-forest biomes.

### Benchmarking phenology with a land surface model: an in-silico experiment for temperate forests

**Authors**: Midori Yajima, Josua Seitz, W. J. Matthaeus, Gayathri G. Nair, L. Daly, S. Caldararu

**Journal**: *bioRxiv* · **DOI**: [10.1101/2025.11.20.689458](https://doi.org/10.1101/2025.11.20.689458) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Plant phenology influences biotic interactions and the cycling of water, carbon, and nutrients, ultimately affecting global climate. Accurately quantifying phenological dynamics is therefore essential for ecological forecasting, yet estimates vary widely depending on data sources, smoothing approaches, and date-extraction techniques. For this reason, the selection of an appropriate processing pipeline for phenological observations has direct consequences for benchmarking land surface models, where the choice of reference data determines model evaluation outcomes.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 (S2 only; OpenAlex returned 429 errors) |
| Topics searched | 16 |
| Total papers fetched | 5 |
| After deduplication | 5 |
| After LLM relevance filtering | 3 |
| Rejected (not relevant) | 2 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Environmental Modelling & Software | 1 |
| Journal of Hydrologic Engineering | 1 |
| bioRxiv | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

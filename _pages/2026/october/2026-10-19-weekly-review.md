---
layout: default
title: "Week 42 (Oct 12 - Oct 19), 1 paper"
parent: October
grand_parent: "2026"
nav_order: 35
date: 2026-10-19
categories: [weekly, 2026, october]
tags: [hydrology, literature-review, research]
paper_count: 1
highlight: "Noah-MP parameter scheme alternatives (RUN, SFC, INF, STC) each improve Missouri River Basin streamflow KGE by 0.14–0.44 over the default configuration."
lang: en
lang_link: /zh/2026/october/2026-10-19-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 42** · October 12–19, 2026
{: .text-grey-dk-000 }

**1** relevant paper found across **1** theme
{: .fs-5 .fw-300 }

## Executive Summary

This was a quiet week for hydrology literature, with only one relevant paper surviving both journal-blocklist filtering and LLM relevance review (OpenAlex was unavailable due to rate-limit errors, limiting results to Semantic Scholar only). The single paper — a comprehensive basin-scale evaluation of the Noah-MP land surface model in the Missouri River Basin — offers directly actionable guidance on parameterization scheme selection for improving runoff and snowmelt simulation across diverse hydroclimatic regimes.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Land Surface Modeling

A single paper this week but a substantive one: Cho et al. conduct a 50-catchment evaluation of Noah-MP's alternative parameterization schemes across the Missouri River Basin, providing concrete KGE improvements tied to specific physical processes. Their results show that the Frozen Soil Permeability (INF) and Surface Exchange Coefficient for Heat (SFC) schemes yield the largest streamflow gains (+0.44 and +0.38 KGE), while the Snow/Soil Temperature Time Scheme (STC) most effectively reduces snow water equivalent bias in snow-dominated subbasins — though improved SWE does not always translate to improved runoff. The finding that no single scheme dominates across all climates and land-cover types reinforces the need for region-specific calibration in large-scale Noah-MP deployments such as those within E3SM-ELM workflows.

### Basin-scale evaluation of the Noah-MP land surface model for runoff and snow generation in the Missouri River Basin: insights and recommendations for parameterization scheme selection

**Authors**: Eunsaem Cho, C. Vuyovich, Bai-Ling Li, Jennifer M. Jacobs

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-6359-2026](https://doi.org/10.5194/hess-30-6359-2026) · **Citations**: 1

**Matched topics**: hydrologic model, land surface model
{: .label .label-green }

> Process-based land surface models, such as the Noah-Multiparameterization (Noah-MP) model, are widely used for large-scale hydrologic simulations because of their flexibility in selecting multiple parameterization schemes. However, limited guidance on choosing appropriate configurations constrains their reliability in representing runoff and snowmelt dynamics across diverse land-cover and snow conditions. This study evaluates the default and four alternative parameterization schemes in the Noah-MP land surface model, including Runoff and Groundwater (RUN), Surface Exchange Coefficient for Heat (SFC), Frozen Soil Permeability (INF), and Snow/Soil Temperature Time Scheme (STC), across 50 Hydro-Climate Data Networks (HCDNs) in the Missouri River Basin. Model performance was evaluated using USGS streamflow observations and snow water equivalent (SWE) estimates from the University of Arizona dataset for 2014–2023. Results showed that the alternative schemes improved runoff simulation compared to the default scheme through different approaches representing key hydrological and thermodynamic processes. Specifically, the RUN, SFC, INF, and STC experiments improved the Kling–Gupta Efficiency (KGE) by 0.19, 0.38, 0.44, and 0.14, respectively in representative subbasins, through enhanced groundwater dynamics, reduced evapotranspiration bias, improved rapid runoff response, and more accurate SWE evolution. SWE evaluation further indicates that the STC experiment most effectively reduced SWE bias in snow-dominated subbasins, though improvements in SWE did not universally translate into better runoff simulation. These results highlight the importance of basin-specific parameterization schemes within Noah-MP to improve hydrological prediction and water management across diverse hydroclimatic regions.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 6 |
| After deduplication | 5 |
| After LLM relevance filtering | 1 |
| Rejected (not relevant) | 2 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Hydrology and Earth System Sciences | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

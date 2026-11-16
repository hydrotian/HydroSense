---
layout: default
title: "Week 45 (Nov 02 - Nov 09), 1 paper"
parent: November
grand_parent: "2026"
nav_order: 34
date: 2026-11-16
categories: [weekly, 2026, november]
tags: [hydrology, literature-review, research]
paper_count: 1
lang: en
lang_link: /zh/2026/november/2026-11-16-weekly-review
highlight: "Noah-MP land surface physics in a coupled ESM reproduces the Amazon-Pacific teleconnection and improves ENSO structure by strengthening land-atmosphere coupling efficiency (JGR-Atmospheres)."
---

# Weekly Literature Review
{: .no_toc }

**Week 45** · Nov 02–Nov 09, 2026
{: .text-grey-dk-000 }

**1** relevant paper found across **1** theme
{: .fs-5 .fw-300 }

## Executive Summary

A slow week for the keyword search, with OpenAlex largely unavailable due to rate-limiting (429 errors throughout the run), leaving only Semantic Scholar results. One notable paper emerged from Journal of Geophysical Research - Atmospheres: a study showing that realistic land surface parameterizations (Noah-MP versus Noah 2.7.1) substantially strengthen land-atmosphere coupling efficiency in a coupled ESM, reproducing the observed Amazon-Pacific teleconnection and improving ENSO spatial structure — findings with direct relevance to E3SM land surface model development.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Earth System Modeling: Land Surface-Atmosphere Coupling

The lone paper this week tackles a foundational question in coupled ESM development: does the choice of land surface parameterization matter for large-scale tropical climate variability, and if so, through which mechanism? Rajesh et al. answer clearly in the affirmative — the key driver is not soil moisture memory alone, but coupling efficiency: the ability of surface flux anomalies to generate spatially coherent atmospheric responses. By comparing Noah-MP and Noah 2.7.1 across century-long free-running simulations with every other component held fixed, they isolate the land surface effect cleanly. The result is striking: Noah-MP reproduces the Amazon-Pacific teleconnection entirely absent in the control, improves ENSO spatial structure, and reduces the Pacific Walker Circulation bias — all traceable to sustained tropical forest evapotranspiration enabled by better subsurface hydrology representation. For ESM developers working on land surface modules (including E3SM/ELM), this underscores that subsurface water access in tropical forests may be a first-order control on climate simulation quality.

### Enhanced Land‐Surface Processes Sustain Evapotranspiration and Improve Tropical Climate Variability in a Coupled Earth System Model

**Authors**: P. Rajesh, Rosimitha Panda, C. Gnanaseelan, A. Sharma, M. Kawsar, Bushra Y. Shaikh et al.

**Journal**: *Journal of Geophysical Research - Atmospheres* · **DOI**: [10.1029/2026jd047646](https://doi.org/10.1029/2026jd047646) · **Citations**: 0

**Matched topics**: earth system model
{: .label .label-green }

> Land surface hydrological processes influence climate predictability through soil moisture persistence and coupling efficiency, the capacity of surface flux anomalies to generate spatially coherent atmospheric forcing at large scales. We examine coupling efficiency using century‐long free‐running simulations of a fully coupled Earth system model, comparing two configurations that differ only in land surface parameterizations. The Noah‐MP configuration differs from the Noah 2.7.1 control in subsurface hydrology, vegetation physiology, and surface‐layer exchange, and produces larger‐scale and more coherent atmospheric responses despite nearly identical soil moisture memory. Because every other model component is shared, the contrast isolates the effect of the land surface formulation. The Amazon–Pacific teleconnection is absent in the control but is reproduced closely with Noah‐MP. Drought composites with nearly equal rainfall show higher latent heat flux over tropical evergreen forests with accessible subsurface water with Noah‐MP than control. Over the Amazon, sustained evapotranspiration anomalies are accompanied by a Matsuno–Gill type response and a reduction in the Pacific Walker Circulation bias. The El Niño–Southern Oscillation (ENSO) spatial structure is also more realistic, with a stronger east–west sea surface temperature gradient. Atlantic Niño variability becomes less tied to ENSO, closer to the observed relationship. These results suggest that coupling efficiency, rather than soil moisture persistence alone, governs how strongly land surface processes influence large‐scale variability, and that a more realistic representation of land surface processes can strengthen that influence with potential implications for long‐term predictability.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 3 |
| After deduplication | 3 |
| After LLM relevance filtering | 1 |
| Rejected (not relevant or duplicate) | 2 |

**Note**: OpenAlex returned 429 rate-limit errors throughout this run; results are from Semantic Scholar only.

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Journal of Geophysical Research - Atmospheres | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

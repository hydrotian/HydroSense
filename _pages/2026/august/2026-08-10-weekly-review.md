---
layout: default
title: "Week 31 (Jul 27 - Aug 03), 2 papers"
parent: August
grand_parent: "2026"
nav_order: 34
date: 2026-08-10
categories: [weekly, 2026, august]
tags: [hydrology, literature-review, research]
paper_count: 2
highlight: "A new frozen-soil infiltration scheme in Canada's operational SVS land surface model cuts severe streamflow simulation failures at cold-region stations from 33% to less than 1%; TIPMIP proposes a new CMIP7-candidate ESM protocol for probing Earth-system tipping points under controlled warming and negative-emission pathways."
lang: en
lang_link: /zh/2026/august/2026-08-10-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 31** · Jul 27–Aug 03, 2026
{: .text-grey-dk-000 }

**2** relevant papers found across **2** themes
{: .fs-5 .fw-300 }

## Executive Summary

This was a methodologically focused week with two papers carrying direct operational and modeling implications. Bouchard et al. demonstrate that a revised frozen-soil infiltration scheme in Canada's operational SVS land surface model dramatically reduces streamflow simulation errors in cold-region catchments, while Jones et al. introduce TIPMIP, a new CMIP7-candidate ESM protocol designed to probe tipping-point behavior under controlled ramp-up and negative-emission pathways. Note: OpenAlex returned no results this week due to API rate-limit errors (HTTP 429), so coverage is based on Semantic Scholar only and may underrepresent the full literature.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Land Surface Modeling in Cold Regions

Accurate representation of frozen-soil processes remains a persistent challenge for operational hydrological prediction, particularly in high-latitude and mountainous catchments where spring snowmelt drives flood risk and water supply. Bouchard et al. directly address this gap within Canada's operational prediction framework. Their revised SVS configuration achieves a 0.28 improvement in Kling-Gupta Efficiency versus the default frozen-soil treatment, while slashing the number of stations with severe performance degradation from one-third to less than 1% across a 580-station evaluation network spanning the Great Lakes–St. Lawrence domain. Crucially, the change also proves acceptable for numerical weather prediction applications, making a path toward operational implementation viable.

### Enhancing runoff-infiltration partitioning in the SVS land surface model improves streamflow simulations under frozen soil conditions

**Authors**: B. Bouchard, Vincent Vionnet, É. Gaborit, Vincent Fortin

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4823-2026](https://doi.org/10.5194/hess-30-4823-2026) · **Citations**: 0

**Matched topics**: land surface model, streamflow, runoff
{: .label .label-green }

> Soil freezing is a major cold region process that influences hydrological response of northern catchments, in particular during winter rainfall and snowmelt events. In land surface models, frozen soil infiltration is difficult to represent because soil structure and hydropedological processes vary at scales finer than the model grid. This is particularly true in operational modeling, where physical process integration must balance performance improvements against computational efficiency and complexity. In this study, we propose a new configuration of the Soil, Vegetation, and Snow (SVS) model used within the operational prediction systems of Environment and Climate Change Canada (ECCC) that enhances frozen soil infiltration by reducing both surface runoff and sub-surface lateral flow. We assessed the effects of this new configuration (Fr-Inf) on streamflow simulations at more than 580 hydrometric stations located in the Great-Lakes and Saint-Lawrence domain over a five-year period. Fr-Inf significantly improves the Kling-Gupta Efficiency (KGE) compared to the default soil freezing configuration (Fr; ΔKGE = 0.28) but slightly underperforms the configuration of SVS without frozen soil (noFr; ΔKGE = −0.07). Strong degradations relative to the no freezing configuration (ΔKGE < −0.5) are observed only at 4 stations with Fr-Inf (<1%) as opposed to 172 stations under the Fr configuration (33%), highlighting the robustness of the approach. To ensure that the proposed change is also acceptable in the context of operational numerical weather prediction, an evaluation of its impact on soil freezing depth as well as screen-level temperature and dew point temperature predictions is performed against in-situ observations. These results support the potential operational implementation of soil freezing at ECCC for numerical weather and streamflow prediction.

---

## Earth System Model Protocol Development

As the climate modeling community ramps up toward CMIP7, a major challenge is designing experiments that allow direct comparison of model behavior near potential Earth-system tipping points without the confounding influence of differing warming rates across models. Jones et al. introduce TIPMIP (Tipping Points Modelling Intercomparison Project), which addresses this by running all participating ESMs in CO₂-emission mode with a uniform 2 °C per century warming rate, then branching into zero-emission and negative-emission runs at 2 °C and 4 °C global warming levels. For hydrologists and water-resources researchers, TIPMIP's design is particularly valuable: by controlling the warming trajectory, it will enable model-ensemble analyses of potential tipping points in the water cycle — including abrupt shifts in monsoon systems, permafrost hydrology, ice-sheet contributions to sea level, and long-term freshwater availability — that are impossible to diagnose cleanly from uncoordinated single-model experiments.

### The TIPMIP Earth system model experiment protocol: phase 1

**Authors**: Colin G. Jones, Isaline Bossert, Donovan P. Dennis, Hazel A. Jeffery, Chris D. Jones, T. Koenigk et al.

**Journal**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-6941-2026](https://doi.org/10.5194/gmd-19-6941-2026) · **Citations**: 5

**Matched topics**: earth system model, climate change
{: .label .label-green }

> We describe a new Earth system model (ESM) experiment protocol, as part of the international Tipping Points Modelling Intercomparison Project (TIPMIP) project. We propose this as a protocol for the Coupled Model Intercomparison Project 7 (CMIP7). The protocol requires ESMs to run in CO₂-emission mode, with atmospheric CO₂ a predicted variable. Forcing for the protocol consists solely of a constant emission of CO₂, based on each model's transient climate response to cumulative emissions of carbon dioxide (TCRE) value, to give a common global mean surface warming rate of 2 °C per century. This positive emission (ramp-up) experiment is started from the pre-industrial state of a given model. When the ramp-up run first exceeds a specified level of global warming (2 and 4 °C) relative to the model's pre-industrial global mean surface air temperature (GMSAT), CO₂ emissions are set to zero and the positive emission run is branched into a zero-emission run. The zero-emission runs continue for 300 years. 50 years into each zero-emission run, CO₂ emissions are set to the negative of the positive emission rate and the model run until GMSAT cools below the original pre-industrial value. Using this protocol, we are able to control the rate of global warming, and potentially also the rate of cooling, across participating models. TIPMIP experiments will support a range of analyses, including: an assessment of abrupt/rapid Earth system change under net zero CO₂ emissions at a range of global warming levels, the long-term Earth system response to net zero CO₂ emissions at these warming levels, the response to net negative CO₂ emissions and the efficacy of negative emissions to drive cooling, and the reversibility of Earth system change under a pathway of positive (warming), zero, and negative (cooling) CO₂ emissions.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 (S2 only — OpenAlex returned 429 errors) |
| Topics searched | 16 |
| Total papers fetched | 14 |
| After deduplication | 13 |
| After LLM relevance filtering | 4 |
| After registry dedup (already in prior weekly) | 2 |
| Rejected (not relevant) | 9 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Hydrology and Earth System Sciences | 1 |
| Geoscientific Model Development | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

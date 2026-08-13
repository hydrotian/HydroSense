---
layout: default
title: "Aug 05, 2 papers"
parent: August
grand_parent: "2026"
nav_order: 5
date: 2026-08-05
categories: [daily, 2026, august]
tags: [hydrology, paper-harvest, research]
paper_count: 2
highlight: "CNNs invert topographic data into landscape evolution model parameters; AMOC–SST relationship operates in three state-dependent regimes in CESM simulations."
lang: en
lang_link: /zh/2026/august/2026-08-05-daily-harvest
---

# Paper Harvest Report
{: .no_toc }

**Date range**: August 05, 2026
{: .text-grey-dk-000 }

**2** top-tier papers selected out of **116** total publications
{: .fs-5 .fw-300 }

## Today's Highlights

Today's harvest yields two papers at the intersection of machine learning, Earth system modeling, and landscape science. A GRL study trains convolutional neural networks to invert topographic data into the parameters of a landscape evolution model, finding that CNNs encode geomorphically meaningful signals — particularly valley spacing and drainage density — and can accurately recover the parameter ratio governing landscape dissection. A Nature Communications multi-model study using Community Earth System Model simulations reveals that the well-known AMOC–subpolar SST dipole is not stationary: the relationship operates across three distinct state-dependent regimes tied to circulation strength, with the year of peak AMOC–SST sensitivity emerging as a physically-based predictor of the transition into a weak-AMOC state.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Top-Tier Journal Papers

### Can Neural Networks Think Like Geomorphologists?

**Authors**: J. R. Martin, G. E. Tucker

**Journal**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl124040](https://doi.org/10.1029/2026gl124040)

**Matched topics**: landscape evolution
{: .label .label-green }

> Understanding the connection between topography and the processes and properties that shape landscapes both helps us better understand landscape evolution, and use topography to infer information relevant for a wide range of human activities. Deep learning methods, like convolutional neural networks (CNNs) have been successfully applied to topographic data in geomorphic contexts but primarily for classification problems. This raises the question: could a CNN be trained to "learn" the parameters responsible for forming a particular kind of terrain? As a first test, we train a convolutional neural network to invert topography generated from a landscape evolution model into the model parameters, and interpret the model's learning. We find that the trained network is able to accurately infer the parameter ratio that governs the degree of landscape dissection, performs better when given topographic derivatives, and has encoded a meaningful relationship between the model parameters and both valley spacing and drainage density.

---

### Regime shifts of AMOC-sea surface temperature relationship

**Authors**: Yifei Fan, Duo Chan, Gokhan Danabasoglu, Who M. Kim, Pengfei Zhang, Laifang Li

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-026-76149-4](https://doi.org/10.1038/s41467-026-76149-4)

**Matched topics**: earth system model
{: .label .label-green }

![Figure](https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41467-026-76149-4/MediaObjects/41467_2026_76149_Fig1_HTML.png)

> The Atlantic Meridional Overturning Circulation (AMOC) plays critical roles in regulating climate, and subpolar North Atlantic sea-surface temperature (SST) patterns are widely used to infer changes in its strength. Yet the stationarity of their relationship remains unclear. Here, using Community Earth System Model simulations spanning various climate states and a multi-model ensemble, we show that this relationship is state-dependent. We identify three distinct regimes: strong AMOC with the typical dipole fingerprint; intermediate AMOC with amplified subpolar SST anomalies; and weak AMOC with muted North Atlantic signals. These regimes arise primarily from changes in atmospheric radiative processes, while ocean processes contribute indirectly through air–sea interactions. The year of peak AMOC–SST sensitivity emerges as a predictor of the transition into the weak-AMOC regime and associated decay of the North Atlantic warming hole, offering a physically-based constraint on model uncertainties in climate projections. Our findings also imply that SST-based AMOC indicators must account for state dependence.

---

## AI for Science

### How AI is changing research

- **[Agentic profiles for effective AI governance](https://www.nature.com/articles/s41586-026-10805-z)** (Nature, 2026-08-12) — A new framework proposes characterizing AI agents by capability profiles (autonomy, action space, memory, communication) to enable principled governance, moving beyond blanket rules; directly applicable for research teams now deploying AI agents in scientific workflows and needing structured oversight mechanisms.

### Cross-discipline sparks

- **[Cascading continental-scale floods across Europe in 1342–1343](https://www.nature.com/articles/s41586-026-10888-8)** (Nature, 2026-08-12) — A reconstruction of catastrophic medieval megafloods across Central Europe using historical chronicles, sediment records, and tree-ring proxies. Cross-discipline spark: this type of continental-scale paleoflood reconstruction was only tractable for a single, exceptionally well-documented event; AI-assisted mining of digitized historical archives (manuscripts, flood inscriptions, parish records) across dozens of languages could systematically extend this approach to build multi-century flood-frequency distributions that current hydrologic return-period estimates are missing.

## Statistics

| Metric | Count |
|:-------|------:|
| Journals searched | 11 |
| Total papers fetched | 116 |
| Passed deterministic filter | 9 |
| After LLM relevance filtering | 2 |
| Rejected (not relevant) | 7 |
| AI for Science items picked | 2 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Geophysical Research Letters | 1 |
| Nature Communications | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model, estuary, coastal, freshwater discharge, river plume, ocean biogeochemistry, marine heatwave, paleohydrology, paleoclimate, Quaternary, Holocene, Pleistocene, fluvial geomorphology, river terrace, loess, drainage network, river capture, landscape evolution, luminescence dating

**Fields**: engineering, environmental science, computer science, geology, geography

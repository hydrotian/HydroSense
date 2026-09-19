---
layout: default
title: "Sep 11, 3 papers"
parent: September
grand_parent: "2026"
nav_order: 11
date: 2026-09-11
categories: [daily, 2026, september]
tags: [hydrology, paper-harvest, research]
paper_count: 3
highlight: "SWOT satellite reveals that dual-cycle seasonal regulation dominates China's Ganjiang Basin reservoirs, and deep learning achieves 86% accuracy in classifying reservoir functions."
lang: en
lang_link: /zh/2026/september/2026-09-11-daily-harvest
---

# Paper Harvest Report
{: .no_toc }

**Date range**: September 11, 2026
{: .text-grey-dk-000 }

**3** top-tier papers selected out of **72** total publications
{: .fs-5 .fw-300 }

## Today's Highlights

Today's harvest yields three papers spanning reservoir hydrology, paleohydroclimatology, and polar freshwater dynamics. A SWOT-based study of 305 reservoirs in China's Ganjiang Basin reveals dual-cycle seasonal regulation as the dominant pattern (40%), with a TimesNet deep-learning classifier achieving 86% accuracy in identifying reservoir functions — demonstrating SWOT's potential for characterizing basin-scale water management in data-scarce regions. Reanalysis of oxygen isotope records from 46 sites across the Asian monsoon region implicates atmospheric updraft — rather than moisture advection — as the primary control on precipitation isotopic variability, revising how speleothem records are interpreted as paleoclimate proxies. In East Antarctica, a hybrid MLR–neural-network framework reconstructs three-dimensional glacier-derived freshwater discharge from the Totten and Moscow University Ice Shelves at approximately 70 and 53 Gt yr⁻¹ respectively, providing a new observational benchmark for ice-shelf–ocean interactions.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Top-Tier Journal Papers

### SWOT Observations Reveal Basin‐Scale Reservoir Operating Patterns

**Authors**: Tan Chen, Jiasheng Li, Shiteng Fang, Pengfei Zhan, Chenyu Fan, Hui Zhang et al.

**Journal**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl122626](https://doi.org/10.1029/2026gl122626)

**Matched topics**: river, reservoir, water management, seasonal, surface water
{: .label .label-green }

> The construction and operation of reservoirs have fundamentally modified the natural hydrograph globally. However, complex seasonal operating patterns remain opaque due to data scarcity, limiting the accuracy of hydrological modeling and water management. Here we show that the Surface Water and Ocean Topography satellite overcomes these challenges by providing full‐coverage water surface elevation measurements for a basin‐wide network of small reservoirs. Applying a two‐step framework to 305 reservoirs (>0.5 km²) in the Ganjiang River Basin (Yangtze), we found that single‐cycle regulation (33.4%) and dual‐cycle regulation (40.3%) patterns are dominant. Coupled with TimesNet deep learning, we predicted reservoir primary functions with an 86.0% accuracy and successfully disentangled multi‐purpose facilities. Our methodology characterizes reservoir regimes in data‐scarce basins, offering high‐resolution insights critical for understanding anthropogenic impacts on the global water cycle and supporting effective management.

---

### Reinterpreting Precipitation Isotope Records from Asian Monsoon Region through the Hidden Role of Atmospheric Updraft

**Authors**: Zhuanxia Zhang, Wusheng Yu, L. G. Thompson, Deliang Chen, Hai Cheng, Stephen Lewis et al.

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-026-77635-5](https://doi.org/10.1038/s41467-026-77635-5)

**Matched topics**: seasonal
{: .label .label-green }

![Figure](https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41467-026-77635-5/MediaObjects/41467_2026_77635_Fig1_HTML.png)

> Speleothem oxygen isotope records (δ¹⁸Oₛ) from the Asian monsoon region provide valuable insights into past hydroclimate variability, yet their interpretation relies on understanding the controls on modern precipitation isotopes (δ¹⁸Oₚ). Although numerous explanations for the spatiotemporal variability of δ¹⁸Oₚ across this region have been proposed, the primary controls remain unresolved. Here we propose a hypothesis to explain δ¹⁸Oₚ variability from δ¹⁸Oₚ records at 46 sites along a transect spanning the Asian monsoon region. Our results show that seasonally low δ¹⁸Oₚ values migrate gradually westward along the east–west transect. We further demonstrate that the corresponding westward migration of atmospheric updraft, particularly convection, controls δ¹⁸Oₚ variations along the transect. In contrast to previous interpretations emphasizing monsoon moisture advection, our findings highlight atmospheric updraft as an important control on δ¹⁸Oₚ variations across the Asian monsoon region. These findings provide an alternative perspective on interpreting the climate signals preserved in Asian δ¹⁸Oₛ records.

---

### Three-Dimensional Reconstruction of Glacier-Derived Freshwater in East Antarctica Using an End-Member-Independent Hydrographic Parameterization

**Authors**: Yutaka W. Watanabe, Daisuke Hirano, Yoshihiko Ohashi, Miyabi Sugita, Yoshiyuki Nakano, Ryosuke Makabe et al.

**Journal**: *Nature Communications* · **DOI**: [10.1038/s41467-026-77441-z](https://doi.org/10.1038/s41467-026-77441-z)

**Matched topics**: river, freshwater discharge
{: .label .label-green }

![Figure](https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41467-026-77441-z/MediaObjects/41467_2026_77441_Fig1_HTML.png)

> The melting of the Antarctic Ice Sheet contributes to global sea-level rise and widespread ocean freshening. A major driver of this process is the intrusion of warm deep water onto the continental shelf, which enhances basal melting of ice shelves and weakens their buttressing of inland ice. However, the three-dimensional distribution of glacier-derived freshwater remains poorly constrained in East Antarctica. Here we present a hybrid multiple linear regression–neural network (MLR–NN) framework that reconstructs glacier-derived freshwater from dissolved inorganic carbon (DIC) residuals without prescribing fixed freshwater end-member compositions. Applying this framework to hydrographic observations around the Totten and Moscow University Ice Shelves, we estimate freshwater discharge rates of 70 ± 7 and 53 ± 9 Gt yr⁻¹, respectively. The reconstructed freshwater signal extends across the continental shelf to approximately 64°S. We also identify differences in freshwater discharge between observations collected during the 2010s and the 2020s, although sparse temporal sampling prevents these differences from being interpreted as a robust long-term trend. Our results provide a three-dimensional observational reconstruction of glacier-derived freshwater in this sector of East Antarctica and demonstrate the potential of an end-member-independent hydrographic parameterization for investigating glacier–ocean interactions in data-limited polar environments.

---

## AI for Science

### Cross-discipline sparks

- **[AI cracked the Navier–Stokes challenge. What does that mean for physics?](https://www.nature.com/articles/d41586-026-02922-6)** (Nature, 2026-09-18) — AI has cracked a century-old challenge in solving the Navier–Stokes equations — the mathematical foundation of all fluid dynamics. For hydrology and hydraulic modeling, this matters directly: Saint-Venant equations (open-channel flow, flood routing) are a depth-averaged simplification of Navier–Stokes. If AI-native solvers can now handle the full 3D system at scale, a small earth-science team could in principle replace the simplified 1D/2D hydraulic solvers used in MOSART or HEC-RAS with physics-informed neural operators — potentially capturing complex floodplain dynamics, turbulent in-channel mixing, and river-plume behavior near estuaries that current routing models paper over.

## Statistics

| Metric | Count |
|:-------|------:|
| Journals searched | 11 |
| Total papers fetched | 72 |
| Passed deterministic filter | 12 |
| After LLM relevance filtering | 3 |
| Rejected (not relevant) | 9 |
| AI for Science items picked | 1 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Geophysical Research Letters | 1 |
| Nature Communications | 2 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model, estuary, coastal, freshwater discharge, river plume, ocean biogeochemistry, marine heatwave, paleohydrology, paleoclimate, Quaternary, Holocene, Pleistocene, fluvial geomorphology, river terrace, loess, drainage network, river capture, landscape evolution, luminescence dating

**Fields**: engineering, environmental science, computer science, geology, geography

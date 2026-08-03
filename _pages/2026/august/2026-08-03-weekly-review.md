---
layout: default
title: "Week 30 (Jul 20 - Jul 27), 5 papers"
parent: August
grand_parent: "2026"
nav_order: 33
date: 2026-08-03
categories: [weekly, 2026, august]
tags: [hydrology, literature-review, research]
paper_count: 5
highlight: "LSTM-reconstructed streamflow for 10,000+ European basins (EARLS) debuts alongside a dense urban sensor dataset, while drought studies from the North China Plain and Italian Alps reveal escalating water stress under warming."
lang: en
lang_link: /zh/2026/august/2026-08-03-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 30** · Jul 20–Jul 27, 2026
{: .text-grey-dk-000 }

**5** relevant papers found across **3** themes
{: .fs-5 .fw-300 }

## Executive Summary

Week 30 brought two major open hydrological datasets — dense urban sensor observations from Switzerland and AI-reconstructed streamflow for over 10,000 European basins — that collectively advance the data infrastructure for large-sample hydrologic science. Drought research dominated the remaining literature, with studies from the North China Plain characterizing flash drought hotspots using a new identification framework and from the Italian Alps documenting how snow droughts doubled glacier contributions to summer streamflow. Rounding out the week, a CLM-based study from India shows that incorporating seasonal irrigation maps substantially improves land surface model evapotranspiration simulation.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## New Hydrological Datasets for Large-Sample Studies

Two notable open dataset papers anchor this week's review, targeting the data scarcity that limits large-sample hydrological studies. Blumensaat et al. present the Urban Water Observatory (UWO) dataset from Fehraltorf, Switzerland — 124 sensors recording rainfall-runoff processes, wastewater, and in-sewer temperatures at 1–5 minute resolution over 2019–2021. This unusually complete, openly available urban drainage dataset fills a persistent gap and comes packaged with a validated hydrodynamic model and rich metadata, opening new avenues from anomaly detection to groundwater infiltration assessment. Klotz et al. take a complementary approach at continental scale: their EARLS dataset uses a single LSTM-based rainfall-runoff model trained on 5,000+ gauged basins to reconstruct daily streamflow for more than 10,000 European basins from 1953–2023 with uncertainty estimates. The fact that a single deep-learning model provides high-quality reconstruction across such diverse European climates and geologies confirms that machine learning has matured to where data-sparse ungauged basins can be confidently included in continental-scale hydrological analyses.

### The UWO dataset – long-term observations from a full-scale field laboratory to better understand urban hydrology at small spatio-temporal scales

**Authors**: F. Blumensaat, S. Bloem, C. Ebi, Andy Disch, C. Förster, Max Maurer et al.

**Journal**: *Earth System Science Data* · **DOI**: [10.5194/essd-18-5187-2026](https://doi.org/10.5194/essd-18-5187-2026) · **Citations**: 8

**Matched topics**: hydrology
{: .label .label-green }

> Urban drainage systems are integral infrastructural components. However, their monitoring poses considerable challenges owing to the intricate, hazardous nature of the process, necessitating substantial resources and expertise. These inherent uncertainties act as barriers, discouraging active involvement of researchers and sewer operators in the rigorous monitoring and utilization of data for a comprehensive understanding and efficient management of drainage-related processes. Consequently, a notable absence of openly available urban drainage datasets hampers exploring their potential for engineering applications, scientific analysis, and societal benefits. In this study, we present a distinctive dataset from the Urban Water Observatory (UWO) in Fehraltorf, Switzerland. This dataset is unique in terms of its completeness, consistency, extensive observation period, high spatio-temporal resolution and its availability in the public domain. The dataset comprises coherent information from 124 sensors that observe rainfall-runoff processes, wastewater and in-sewer atmosphere temperatures. Sensor data have a temporal resolution of 1–5 min and cover a period of three years from 2019–2021.

---

### EARLS: a runoff reconstruction dataset for Europe

**Authors**: Daniel Klotz, Peter Miersch, T. V. M. do Nascimento, Fabrizio Fenicia, Corinna Frank, M. Gauch et al.

**Journal**: *Earth System Science Data* · **DOI**: [10.5194/essd-18-5485-2026](https://doi.org/10.5194/essd-18-5485-2026) · **Citations**: 3

**Matched topics**: runoff
{: .label .label-green }

> Data drives our understanding of hydrological processes, supports model development, and enables anticipatory water management. This contribution introduces EARLS: European Aggregated Reconstructions for Large-sample Studies. EARLS offers daily streamflow reconstructions for more than 10,000 basins in Europe including uncertainty estimates, covering the period from 1953 to 2023. The reconstruction is derived from a single Long Short-Term Memory (LSTM) based rainfall–runoff model trained on more than 5000 basins. LSTMs represent the state of the art in rainfall–runoff modeling and are well suited to provide predictions in ungauged basins. We evaluate the quality of the reconstruction through quantitative evaluation on two held-out sets of basins and by conducting a qualitative assessment that compares EARLS-based peak flows and flood timing to previous large-scale hydrological studies. EARLS represents a new generation of datasets that harness the capabilities of Deep Learning to obtain accurate and high-resolution data.

---

## Drought Dynamics in Mountain and Agricultural Regions

This week's drought literature reveals contrasting but complementary facets of water scarcity. Zhang et al. propose a new mean-scaled evaporative stress ratio (MESR) method to characterize flash drought in the North China Plain from 1981–2022, identifying two persistent hotspots in the northeastern and southwestern NCP where flash droughts are most frequent and intense. Their multi-method comparison (RZSM, SESR, MESR) demonstrates that identification thresholds strongly control flash drought frequency estimates — a critical caveat for operational drought monitoring systems. In mountain catchments, Leone et al. document the severe 2022–2023 snow drought in the Italian Alps, where glacier melt contribution to streamflow doubled or tripled compared to the 2011–2023 historical mean through four compounding mechanisms: earlier melt onset, intensification of melt contribution, an earlier-than-usual seasonal peak, and extension of the melt season. With elevation-dependent warming amplifying the anomalies (anomalies at 4,000 m were 1–1.5 °C higher than at 2,000 m), the results emphasize that glaciers are increasingly acting as critical water buffers in alpine systems, but one that is itself under threat from accelerating glacier retreat.

### Flash drought characteristics based on three identification methods in the North China Plain, China

**Authors**: Siyao Zhang, Keke Zhou, Jianzhu Li, Ting Zhang, Ping Feng

**Journal**: *Journal of Climate* · **DOI**: [10.1175/jcli-d-25-0314.1](https://doi.org/10.1175/jcli-d-25-0314.1) · **Citations**: 4

**Matched topics**: drought
{: .label .label-green }

> Flash drought (FD) is a rapid onset and intense drought threatening ecology, economy, and agriculture. The North China Plain (NCP) suffers from frequent droughts and limited water resources. This study proposed a new FD identification method, termed mean-scaled evaporative stress ratio (MESR), to identify FD events in the NCP from 1981 to 2022. This method applied an improved standardized evaporative stress ratio (SESR) framework to identify FD by atmospheric evaporative demand. Combining root zone soil moisture (RZSM), SESR, and MESR, FD spatiotemporal characteristics were explored from agricultural and land-atmosphere perspectives. Results show that FD frequency is high in north-central NCP and low in southern NCP. Two FD hotspots with frequent, severe, and intense FDs are in northeastern and southwestern NCP. This study improves the FD understanding in the NCP, providing valuable insights for regional FD adaptation.

---

### The 2022–2023 snow drought in the Italian Alps doubled glacier contribution to summer streamflow

**Authors**: M. Leone, F. Avanzi, U. Morra di Cella, S. Gabellani, E. Cremonese, M. Isabellon et al.

**Journal**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4649-2026](https://doi.org/10.5194/hess-30-4649-2026) · **Citations**: 1

**Matched topics**: streamflow
{: .label .label-green }

> Snow droughts are increasingly affecting mountain regions, raising concerns about downstream water availability in glacierized catchments. Here, we quantified the role of glaciers in mitigating snow-drought impacts on downstream streamflow during the severe 2022–2023 event in the Italian Alps. In order to do so, we compared glacier-melt contribution to streamflow during these years with the 2011–2023 historical period in two catchments, Dora Baltea (Aosta Valley) and Adda (Lombardy). Results showed a severe snow water equivalent deficit over glaciers across both catchments and both years (between ~−45% at 4000 m in 2022 and ~−75% at 2000 m a.s.l. during both years), which was largely driven by anomalous air temperatures and seasonal-precipitation patterns (up to +2–3 °C and −73%, respectively). Glacier contribution to streamflow doubled to tripled during these snow droughts in both catchments, manifesting through four mechanisms: an earlier-than-usual onset of the glacier melt season, an intensification of glacier melt contribution to streamflow, an earlier-than-usual seasonal peak in glacier melt contribution, and an extension of the glacier melt season.

---

## Land Surface Model Improvement for Agricultural Regions

Li et al. address a key source of uncertainty in land surface modeling: the static, seasonally undifferentiated irrigation maps used in most CLM implementations over agricultural regions. By incorporating a season-specific irrigation map for India into CLM, they improved the transpiration-to-ET ratio by up to 30% in the pre-monsoon season, signaling better representation of actual irrigation efficiency. Their experiments further show that higher irrigation frequency leads to cascading increases in irrigation water amounts, evapotranspiration, and surface runoff — a finding with direct implications for how ESM simulations handle agricultural water withdrawals and their feedbacks on the regional hydrological cycle. The approach, validated against remote-sensing ET products, demonstrates that dynamic irrigation representation is essential in regions with pronounced cropping seasonality.

### Improving irrigation and evapotranspiration simulation by incorporating seasonal irrigation map into a land surface model

**Authors**: Dazhi Li, Jiaqi Sun, Xiaojun Wang, Netrananda Sahu, Qianya Yang, Jie Zhang, Zebin Zhao

**Journal**: *Geoscience Letters* · **DOI**: [10.1186/s40562-026-00500-2](https://doi.org/10.1186/s40562-026-00500-2) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Irrigation is essential for maintaining the agricultural production and supporting India's growing population. Land surface models provide an effective approach to estimate irrigation requirements and hydrological fluxes. However, the irrigation modeling tends to be affected by uncertainties related to the spatiotemporal uncertainty in irrigation map, frequency and irrigation factor. To address these uncertainties, the irrigation and hydrological fluxes over India were reconstructed by simulation experiments with the Community Land Model (CLM). Results show that using a season-specific irrigation map improved the transpiration-total evapotranspiration ratio (T/ET) by up to 30% in the pre-monsoon season, implying higher irrigation efficiency. The remote sensing-based evapotranspiration products were used to compare with simulated model results, showing a similar increasing ET-trend in the pre-monsoon season as the irrigation induced CLM. Furthermore, the results show that higher irrigation frequency leads to increased irrigation amounts, evapotranspiration, and surface runoff.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 7 |
| After deduplication | 5 |
| After LLM relevance filtering | 5 |
| Rejected (not relevant) | 0 |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Earth System Science Data | 2 |
| Journal of Climate | 1 |
| Hydrology and Earth System Sciences | 1 |
| Geoscience Letters | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

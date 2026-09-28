---
layout: default
title: "Week 38 (Sep 14 - Sep 21), 2 papers"
parent: September
grand_parent: "2026"
nav_order: 34
date: 2026-09-21
categories: [weekly, 2026, september]
tags: [hydrology, literature-review, research]
paper_count: 2
highlight: "TerM LSM projects >50% surge in Limpopo peak flows under SSP5-8.5, while ORCHIDEE gains explicit Arctic shrub PFTs that cut simulated high-latitude biomass estimates by 13.5%."
lang: en
lang_link: /zh/2026/september/2026-09-21-weekly-review
---

# Weekly Literature Review
{: .no_toc }

**Week 38** · September 14–September 21, 2026
{: .text-grey-dk-000 }

**2** relevant papers found across **2** themes
{: .fs-5 .fw-300 }

## Executive Summary

This was a notably quiet week for the search window, with OpenAlex returning no results due to service errors and only two distinct papers surviving deduplication and journal filtering from Semantic Scholar. Both papers center on land surface model development and application: Mohomi et al. project that austral summer peak flows in South Africa's Limpopo River Basin could increase by more than 50% under high-emission scenarios using the TerM LSM, signaling an intensified flood–drought cycle. Kirchner et al. demonstrate that adding explicit shrub plant functional types to ORCHIDEE substantially improves carbon balance representation across the Arctic–Boreal domain, with implications for Earth system model accuracy.

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Climate Change Impacts on Hydrology

Regional hydrologic projections using land surface models remain essential for climate adaptation planning. Mohomi et al. apply the TerM (INM RAS-MSU Terrestrial Model) to the Limpopo River Basin under CMIP6 ISIMIP forcing across SSP1-2.6 and SSP5-8.5 scenarios, revealing a notable shift toward hydrological extremes: while annual streamflow trends are not statistically significant, intra-annual seasonality intensifies dramatically, with January–February flood peaks projected to exceed historical levels by more than 50% under high emissions even as spring months become drier. This pattern of intensified temporal variability — rather than monotonic change — underscores why both flood and drought risks must be assessed simultaneously in semi-arid basins influenced by ENSO and tropical cyclones.

### Projections of hydrological changes and riverflow extremes using TerM land surface model in the Limpopo River Basin, South Africa

**Authors**: Tumelo Mohomi, V. Stepanenko, A. Medvedev, I. Dhau, M. Bopape, H. Chikoore

**Journal**: *Theoretical and Applied Climatology* · **DOI**: [10.1007/s00704-026-06579-z](https://doi.org/10.1007/s00704-026-06579-z) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Increasingly frequent hydroclimatic extremes in South Africa necessitate a robust understanding of how changing climate drivers will influence regional water balance. This study evaluates the impacts of climate change on hydrological extremes within the Limpopo River Basin, a region historically vulnerable to catastrophic flooding and prolonged droughts. The INM RAS-MSU (Terrestrial Model; TerM) Land Surface Model was used to project river flow from 2020 to 2100. The atmospheric forcing was derived from the CMIP6 ISIMIP database under the SSP1-2.6 and SSP5-8.5 scenarios. Projections for the near future (2020–2055) and far future (2065–2100) periods were compared against a 1979–2014 baseline, with high-flow events (floods) computed at the 95th percentile. Intra-annual streamflow patterns remain consistent with historical trends but are projected to peak by more than 50%, particularly under the high-emission (SSP5-8.5) scenario. Peak flow increase will likely occur during the austral summer (January-February), while a pronounced decrease is projected during spring (September-November). Climate change is expected to intensify hydroclimatic extremes in northeastern South Africa, where austral summer rainfall variability is strongly influenced by tropical cyclones, the El Niño–Southern Oscillation (ENSO), and convective rainfall. The findings provide an evidence base for strengthening climate adaptation policies and measures to reduce the impacts of hydroclimatic extremes in northeastern South Africa.

---

## Land Surface Model Development

Improving the representation of vegetation diversity in land surface models is critical for reducing biases in simulated carbon and energy cycles that feed into Earth system projections. Kirchner et al. address a long-standing gap in ORCHIDEE — the land surface component of the IPSL Earth system model — where high-latitude vegetation was effectively reduced to boreal trees and grasslands. By implementing three shrub plant functional types (tall deciduous, low deciduous, and evergreen dwarf shrubs) calibrated against pan-Arctic observations, the authors reduce total Arctic–Boreal aboveground biomass estimates from 54 to 46.7 Pg C, improving agreement with benchmarking datasets. The methodological approach — building on existing woody vegetation schemes with minimal added process complexity — is transferable to other LSMs facing similar gaps, making this a useful reference for ESM development efforts.

### Introducing shrubs enhances the representation of high-latitude vegetation and carbon cycling in the ORCHIDEE land surface model

**Authors**: A. Kirchner, Efrén López-Blanco, V. Bastrikov, S. Luyssaert, P. Peylin, A. Lansø

**Journal**: *Biogeosciences* · **DOI**: [10.5194/bg-23-6521-2026](https://doi.org/10.5194/bg-23-6521-2026) · **Citations**: 0

**Matched topics**: land surface model
{: .label .label-green }

> Arctic–Boreal terrestrial ecosystems are rapidly changing under amplified high-latitude warming, including widespread expansion of shrubs, with consequences for regional carbon and energy balances. Yet, high-latitude vegetation diversity and vegetation–climate interactions remain under-represented in many global land surface models. In ORCHIDEE, the land surface component of the IPSL Earth system model, high-latitude vegetation is represented primarily as boreal trees or grasslands, omitting explicit shrubs. Here, we implement three high-latitude shrub plant functional types (PFTs) (tall deciduous, low deciduous, and evergreen dwarf shrubs) in ORCHIDEE (revision 9269). The implementation builds on ORCHIDEE's existing woody vegetation scheme by recalibrating a targeted set of parameters controlling allometry, carbon allocation, recruitment, mortality and phenology. Parameter values are constrained using synthesised pan-Arctic observations to obtain regionally representative shrub traits. Shrub spatial distributions are prescribed with updated PFT maps that combine ESA CCI products with Arctic and regional shrub mapping information. The resulting shrub PFTs reproduce observed ranges of shrub size and biomass allocation across the Arctic–Boreal domain. Introducing shrubs reduces simulated total aboveground biomass in the Arctic–Boreal region from 54 to 46.7 Pg C (−13.5%) and mean annual gross primary productivity from 498 to 481 gCm⁻²yr⁻¹ (−3.4%) over the simulated period 1992–2020, with a stronger reduction in the tundra region (4.6 to 3 Pg C (−34.8%); and 334 to 289 gCm⁻²yr⁻¹ (−13.5%)), increasing agreement with benchmarking datasets.

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | 2 |
| Topics searched | 16 |
| Total papers fetched | 4 |
| After deduplication | 4 |
| After journal filtering (blocklist) | 2 |
| After LLM relevance filtering | 2 |
| Rejected (not relevant) | 0 |

**Note**: OpenAlex returned errors (HTTP 503) for all 16 topics this week — all results are from Semantic Scholar only.

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| Theoretical and Applied Climatology | 1 |
| Biogeosciences | 1 |

## Filtering Criteria

**Topics**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**Databases**: Semantic Scholar, OpenAlex

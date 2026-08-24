---
layout: default
title: "第33周（8月10日 - 8月17日），5篇"
nav_order: 36
nav_exclude: true
lang: zh
lang_link: /2026/august/2026-08-24-weekly-review
date: 2026-08-24
categories: [weekly-zh, 2026, august]
tags: [hydrology, literature-review, research]
paper_count: 5
highlight: "可微水文模型无需随时间变化的参数——静态MLP集成在531个流域中与LSTM性能相当，对机器学习水文学主流趋势提出挑战。"
---

# 每周文献综述
{: .no_toc }

**第33周** · 2026年8月10日–17日
{: .text-grey-dk-000 }

**5** 篇相关论文，涵盖 **3** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

本周文献聚焦于提升陆面与水文模型的模拟精度，涉及灌溉驱动的陆面模型蒸散发偏差、可微模型架构的复杂性权衡，以及陆面初始条件对E3SM次季节至季节降水预报的影响。一个贯穿始终的主题是：附加观测约束——来自野外观测和卫星产品——对减少模型不确定性的价值，尤其是在正向降雨主导转变的积雪区。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 陆面模型与地球系统模型

本周有两项研究聚焦于离线和耦合模型中陆面-大气过程的表征方式。Lunel等人量化了灌溉的"大气反馈效应"——近地表空气的冷却与湿润降低了蒸散发速率——发现基于标准再分析产品驱动的离线陆面模型（LSM）在灌溉良好的农田上系统性地高估蒸散发约25%。这一偏差并非单纯的参数率定问题，而是反映了驱动场对土地利用变化表征的结构性缺陷；对于水分亏缺作物，气孔关闭的补偿效应使该偏差消失。与此互补，Xu等人研究了大气与陆面初始条件对E3SM次季节至季节降水预报的影响，发现真实的陆面状态（土壤湿度与地表温度）通过改善海洋性大陆地区的陆-气耦合，提供了重要的次级可预报性来源。两项研究共同揭示：无论是初始条件还是边界驱动场中的陆面状态误差，都会在不同时间尺度上级联传播，造成水通量偏差。

### Systematic overestimation of evapotranspiration over irrigated areas by an offline land surface model

**作者**: Tanguy Lunel, B. Martí, Aaron A. Boone, P. Le Moigne

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-5117-2026](https://doi.org/10.5194/hess-30-5117-2026) · **引用数**: 2

**匹配主题**: land surface model, irrigation
{: .label .label-green }

> Abstract. Offline Land Surface Models (LSMs) are essential for a wide range of applications, including water resource management and agricultural planning. A critical variable in these models is evapotranspiration, but its value is easily biased in irrigated areas. In fact, irrigation fundamentally alters local atmospheric conditions – cooling and humidifying the air and reducing wind speeds – factors that contribute to reducing evapotranspiration rates. This phenomenon is called "atmospheric feedback", but is often missing or poorly represented in offline LSMs because most of the atmospheric forcings used, such as reanalyses and climate model outputs, overlook the atmospheric effect of irrigation. This leads to a tendency for offline LSMs to overestimate evapotranspiration rates over irrigated areas. In this study, the atmospheric effects of irrigation are quantified using data from the Land surface Interactions with the Atmosphere over the Iberian Semi-arid Environment (LIAISE) project field campaign. The various surface processes that influence the dynamics of evapotranspiration in response to the atmospheric feedback are then systematically investigated. The results confirm the importance of considering the atmospheric feedback in the Interactions Soil Biosphere Atmosphere (ISBA) LSM over irrigated areas in many configurations. For well irrigated crops, the average overestimation of evapotranspiration is about 25 %. Conversely, for water-stressed crops, this overestimation is negligible because of the delay in stomatal closure caused by the atmospheric feedback mechanisms, providing a compensatory effect which mitigates the overestimation. These findings highlight the need for improved representation of irrigation-related atmospheric feedback in the atmospheric forcings used as upper boundary conditions in LSMs to improve the accuracy of evapotranspiration estimates in agricultural or hydrological contexts.

---

### Dependence of subseasonal to seasonal precipitation prediction on atmospheric and land initial conditions in the Energy Exascale Earth System Model

**作者**: Dong-Yang Xu, Z. Pu, Shixuan Zhang, Jeffrey L. Anderson, L. R. Leung

**期刊**: *Climate Dynamics* · **DOI**: [10.1007/s00382-026-08320-y](https://doi.org/10.1007/s00382-026-08320-y) · **引用数**: 0

**匹配主题**: earth system model
{: .label .label-green }

> Subseasonal to seasonal (S2S) scale prediction, especially precipitation prediction, depends predominantly on initial conditions. To examine the impacts of atmospheric and land initial conditions on the predictions of the Madden-Julian Oscillation (MJO) and related S2S precipitation, we conduct a novel study using coupled atmosphere-land simulations in the Energy Exascale Earth System Model (E3SM). Our findings indicate that reanalysis-based atmospheric and land initial conditions yield improved S2S precipitation simulations compared with those using a long-term spin-up equilibrium state. The impacts of initial conditions on precipitation simulation persist for approximately 40 and 50 days in the MJO and global regions, respectively, and are strongly associated with outgoing longwave radiation in the MJO region and surface latent heat flux at the global scale. Although atmospheric initial conditions exert a dominant influence on MJO simulation, improved land initial conditions provide an important secondary source of predictability by better representing land–atmosphere coupling over the Maritime Continent. More realistic surface moisture fluxes and surface temperature can modulate boundary-layer moistening and MJO-related convection, thereby contributing to improved MJO prediction. These findings have important implications for S2S precipitation prediction and provide crucial insights for the further development of Earth system models.

---

## 水文模型架构与参数率定

两项研究从互补视角探讨了过程驱动水文模型的架构与参数率定问题。Poudel和Steinschneider对可微模型中时变参数方案的流行趋势提出质疑——通过对531个CAMELS-US流域的分析表明，静态MLP集成方案与动态LSTM集成方案性能相当，且LSTM估计的参数鲜少表现出有意义的时间变异性。他们发现仅用经纬度就能实现与完整特征集相当的空间泛化能力，这一结果对静态输入的物理意义提出了重要追问：这些输入可能更多充当空间代理，而非物理过程的编码。North等人则从模型率定角度切入，利用七种观测产品（流量、雪水当量、积雪覆盖面积、土壤湿度、蒸散发）率定科罗拉多河上游源头集水区的国家水文模型（NHM），发现蒸散发对所有集水区的径流预报均具普遍约束力，而积雪和土壤湿度数据集的约束效果则因集水区而异。

### An argument for parsimony in differentiable hydrologic models

**作者**: Sandeep Poudel, S. Steinschneider

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-5173-2026](https://doi.org/10.5194/hess-30-5173-2026) · **引用数**: 1

**匹配主题**: hydrologic model
{: .label .label-green }

> Abstract. Differentiable hydrologic models that use machine learning to infer parameters for process-based models show promise for both prediction and inference. However, these models are often developed with time-varying parameters, despite evidence that such flexibility can undermine physical consistency and yield only marginal predictive improvements over simpler static approaches. In this study, we revisit the comparison between static and dynamic differentiable models across 531 CAMELS-US basins, evaluating key architectural choices: (1) neural network type (multi-layer perceptron (MLP) vs. long short-term memory network (LSTM)); (2) process model configuration (single- versus ensemble-parameter estimation); and (3) comprehensive versus alternative input feature sets. Using the Hydrologiska Byrås Vattenbalansavdelning (HBV) conceptual model, we find that although ensemble parameterizations improve performance relative to single-parameter configurations, they also alter the conclusions about the relative value of network architecture: LSTMs outperform MLPs in single-parameter configurations, but static, MLP-based ensembles achieve performance comparable to dynamic, LSTM-based ensembles despite their simpler structure. Additionally, we find that LSTM-estimated parameters rarely exhibit meaningful temporal variability despite their time-varying inputs, and when they do, this temporal variability may reflect hydrologic model equifinality rather than process dynamics. We further show that models using only latitude and longitude as static inputs achieve spatial generalization comparable to models using comprehensive feature sets describing climate, topography, geology, soils, and land cover. Similarly, temporal generalization is retained even when comprehensive features are replaced with physically meaningless values. These results raise the possibility that static inputs may function less as direct representations of physical basin processes and more as spatial proxies for generalization in space or as site identifiers when generalizing in time. Overall, our results support reduced complexity in differentiable hydrologic modeling to provide greater transparency while retaining predictive performance.

---

### Hydrologic model parameter estimation in snow-dominated headwater catchments using multiple observation datasets

**作者**: L. North, Adrienne M. Marshall, G. Tootle, L. Davis, A. W. Wood, E. J. Anderson

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-5195-2026](https://doi.org/10.5194/hess-30-5195-2026) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> Abstract. Hydrologic models are often calibrated using streamflow alone, but increasing availability of in situ and satellite-based observations provide numerous opportunities to constrain model outputs and improve process representation. However, as new observation data emerges, it is often unclear whether calibration with additional data would inform or misinform streamflow prediction. Here, we carry out a multi-observational sensitivity and uncertainty analysis using the U.S. Geological Survey's National Hydrologic Model (NHM) in four headwater catchments in the Upper Colorado River Basin. We use seven different observational data products that pertain to discharge, snow water equivalent, snow-covered area, soil moisture, and evapotranspiration. Informative model parameters are identified using the Morris screening method across all data sets, followed by parameter estimation and streamflow performance assessment using a Latin Hypercube Sample Monte-Carlo filtering approach. Results show that an increased number of informative parameters are determined through the screening process with the use of observation data representing terms beyond streamflow, and that forcing corrections and rain-snow partitioning parameters are particularly impactful to the model fit to observations. Multi-objective Monte Carlo filtering reduces the number of behavioral parameter sets, and estimated parameter values can depend strongly on the observation data criteria. Evapotranspiration is informative for streamflow prediction across all catchments included in this study, but snow and soil moisture datasets are only informative in some. These results provide new insight into the variable value of alternative observation data for streamflow prediction and highlight challenges related to model/observation scale mismatches, compensating errors, and misinformative data.

---

## 积雪-降雨转变与径流网络动态

随着气候变化驱动水文系统从积雪主导转向降雨主导，理解河网如何响应对水资源规划至关重要。Boardman等人利用DHSVM模拟一个27 km²积雪火山流域，表明地下水滞后效应——地下水位与径流响应之间的时间滞后——会显著使流动河网长度与流量发生解耦。气候变暖导致的更强降雨脉冲预计将抑制风暴尺度上的河网扩展，同时在日至月时间尺度上显著增加L-Q滞后（p < 0.01）。预测河网长度异常与实测河流离子浓度之间的强负相关（r = -0.92）验证了模型的物理基础，表明当前标准幂律L-Q关系在变暖背景下需要修正。

### Groundwater hysteresis increasingly decouples flowing network length from streamflow as snow shifts to rain

**作者**: E. N. Boardman, M. Wigmosta, N. Fernandez, J. A. Whiting, A. Harpold

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-5145-2026](https://doi.org/10.5194/hess-30-5145-2026) · **引用数**: 1

**匹配主题**: streamflow
{: .label .label-green }

> Abstract. Flowing stream networks expand and contract in response to dynamic groundwater levels. Field studies generally associate greater flowing network length (L) with higher streamflow (Q), but this neglects potential hysteresis caused by nonequilibrium groundwater flow after rain and snowmelt. Using a new version of the Distributed Hydrology Soil Vegetation Model (DHSVM), we predict that groundwater hysteresis may decouple L from Q across large (> 100 %) variations in Q. Groundwater hysteresis contributes to the spatial reconfiguration of active flowpaths and changes to hillslope-riparian hydrological connectivity, which can manifest as a network length scaling anomaly relative to the best-fit power law. In a 27 km² snowy volcanic watershed, seasonal anomalies in measured stream ionic concentration indicate an outsized contribution from longer subsurface flowpaths during recession, supporting our L-Q hysteresis hypothesis and refining our model calibration. The model can reproduce observed stream network elasticity (from field surveys), and the predicted network length anomaly mirrors seasonal anomalies in measured stream ionic concentration (r = -0.92), suggesting that the model can capture seasonal changes in the spatial configuration of groundwater convergence and streamflow generation. A warmer climate is expected to cause a partial transition from snow to rain resulting in flashier streamflow, but our simulations predict that seasonal groundwater hysteresis would dampen storm-scale stream network elasticity, thereby significantly increasing L-Q hysteresis on daily to monthly timescales (p < 0.01). Conceptual models of stream networks should consider the potential effects of groundwater hysteresis, especially in a changing environment. More broadly, our investigation highlights how spatially distributed process-based hydrological modeling can reveal emergent hydrological behaviors that are not necessarily apparent from sparse field data.

---

## 统计信息

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 获取论文总数 | 8 |
| 去重后 | 7 |
| LLM相关性筛选后 | 5 |
| 不相关（已排除） | 2 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|------:|
| Hydrology and Earth System Sciences | 4 |
| Climate Dynamics | 1 |

## 筛选标准

**主题关键词**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

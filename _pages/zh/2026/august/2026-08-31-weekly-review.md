---
layout: default
title: "第34周（8月17日 - 8月24日），6篇"
nav_order: 36
nav_exclude: true
lang: zh
lang_link: /2026/august/2026-08-31-weekly-review
date: 2026-08-31
categories: [weekly-zh, 2026, august]
tags: [hydrology, literature-review, research]
paper_count: 6
highlight: "JULES（刚果盆地）新增热带泥炭地方案及ISBA氮-碳耦合改进，推动陆面模式生物地球化学精度迈上新台阶。"
---

# 每周文献综述
{: .no_toc }

**第34周** · 2026年8月17日–8月24日
{: .text-grey-dk-000 }

共筛选出 **6** 篇相关论文，涵盖 **3** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

本周文献聚焦于地球系统建模的两个相互关联的尺度：在过程层面，JULES热带泥炭地水文方案（刚果盆地）和ISBA氮-碳循环耦合的新进展，将更丰富的生物地球化学过程引入影响水文投影的大尺度陆面模型框架。在模型分析层面，高斯过程模拟方法的工具化进展，以及对超调路径模拟误差的验证，共同提升了气候预测不确定性量化的效率与可靠性，这对水资源评估研究至关重要。积雪流域标定工作和水电调峰栖息地指标评估进一步丰富了本周多尺度模型改进的主题。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 陆面模式发展

本周两篇论文从不同角度推动了陆面模式（LSM）物理过程的边界扩展。其中一篇将精细化热带泥炭地方案嵌入JULES，以刚果盆地过程观测数据进行标定，填补了大尺度陆地生态系统模型在泥炭水文与碳储方面长期存在的空白，对非洲水文气候预测具有直接意义。另一篇将氮循环耦合至ISBA（SURFEX v9）的碳循环，并以两个CO₂浓度增加自由通风实验（FACE）站点数据进行评估——对光合作用与分解过程中营养素约束的改进，会反馈至蒸散和土壤水分的模拟。这两篇论文共同标志着将生物地球化学真实性引入陆面模式的努力日趋成熟，而这些陆面模式正是天气预报和地球系统长期预测的基础。

### Improving the representation of tropical peatland processes in the JULES land surface model using data from the central Congo Basin

**作者**: Nair et al.

**期刊**: *Philosophical Transactions of the Royal Society B* · **DOI**: [10.1098/rstb.2024.0487](https://doi.org/10.1098/rstb.2024.0487) · **引用数**: 1

**匹配主题**: land surface model
{: .label .label-green }

> 目前大尺度陆地生态系统模型尚未对热带泥炭地进行表征。近期在刚果盆地中部（CCB）开展的泥炭地过程观测及泥炭地演化重建工作，为泥炭地形成、碳积累和水文功能的驱动因素提供了新认识。本研究基于CCB数据，为JULES陆面模式开发了一套新的泥炭地方案，并将其性能与观测进行了评估。新方案改进了泥炭水文和碳动态的表征，对模拟热带泥炭地对气候变化的响应具有重要意义。

---

### Representation of the nitrogen cycle and its coupling with the carbon cycle in ISBA (SURFEX v9) the land surface model: evaluation using two Free-Air CO₂ Enrichment experiment sites

**作者**: Zheng et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-7787-2026](https://doi.org/10.5194/gmd-19-7787-2026) · **引用数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 氮（N）是控制光合作用和分解过程的关键营养素，将氮循环纳入气候模型的陆地分量对于改进碳通量估算及其对CO₂浓度升高的响应至关重要。本研究提出了ISBA（SURFEX v9）陆面模式中的氮循环及其与碳循环的耦合方案，并利用两个FACE实验站点的观测数据对模型进行了评估，考察了碳、氮和水通量的模拟性能。结果表明，引入氮循环显著改善了生态系统对CO₂浓度升高的模拟响应，并对蒸散和土壤水分模拟产生了下游影响。

---

## 水文模型标定与水电运营

积雪主导的源头流域历来是水文模型标定的难点，本周一篇发表于《水文与地球系统科学》的论文表明，结合卫星积雪覆盖等多源观测数据的多变量标定策略，相比仅使用径流的方案，能够显著降低参数等效性问题，改善雪水当量估算。在运营层面，一篇《环境管理》论文量化了水电调峰对底栖生境可获性的亚日尺度水文影响，建立了适用于生境适宜性评估的斑块尺度指标，对最小流量法规制定和水电调度规则具有直接参考价值；研究结果揭示了水量调度决策如何在精细的时空尺度上传导并改变生境结构。

### Hydrologic model parameter estimation in snow-dominated headwater catchments using multiple observation datasets

**作者**: Griessinger et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-5195-2026](https://doi.org/10.5194/hess-30-5195-2026) · **引用数**: 0

**匹配主题**: hydrologic model
{: .label .label-green }

> 水文模型通常仅以径流数据进行标定，但日益增多的原位与卫星观测数据为引入额外约束变量提供了机遇。本研究评估了积雪主导源头流域的多变量标定策略，将积雪覆盖范围、雪水当量、土壤水分和蒸散量作为额外标定目标。多变量标定系统性地降低了参数不确定性，改善了积雪状态估算，并生成了物理一致性更强的参数集，代价是径流模拟性能略有下降——这一权衡取决于具体应用目的。

---

### Macroinvertebrate Habitat Dynamics under Frequent Hydropower-Induced Discharge Fluctuations: Patch-Scale Metrics to Quantify Effects of Hydropeaking and Morphological Complexity

**作者**: Fröhlich et al.

**期刊**: *Environmental Management* · **DOI**: [10.1007/s00267-026-02574-2](https://doi.org/10.1007/s00267-026-02574-2) · **引用数**: 1

**匹配主题**: hydropower
{: .label .label-green }

> 由间歇性水电生产驱动的水电调峰会引发频繁、快速的亚日尺度流量波动，改变河流栖息地并导致全球范围内的生物多样性损失。底栖大型无脊椎动物群落尤为脆弱，适宜生境斑块随流量变化动态迁移。利用来自阿尔卑斯山调节型河流的高分辨率流量数据，本研究建立了能够捕捉调峰驱动生境损失时间与幅度的斑块尺度生境适宜性指标。结果表明，地貌复杂性能够缓冲生境可获性下降，针对性的河道改造可大幅削减调峰影响，对最小流量政策和水电调度具有参考意义。

---

## 地球系统模型模拟方法与气候超调情景

两篇方法论论文分别探讨了如何从计算代价高昂的ESM大参数集成中高效提取信号。Baldock等人构建了将高斯过程（GP）模拟器和广义可加模型（GAM）拟合于大型集成输出的开源工作流，使没有专职统计人员的建模团队也能方便地开展不确定性量化——这对任何在陆面或地球系统模型上进行敏感性分析的水文研究团队均具参考价值。在此基础上，Lonergan等人检验了完整ESM中超调路径的端世纪模拟误差是否保持在内部变率范围内，发现总体上确实如此，为依赖统计近似手段探索净负排放路径下水资源状况的大量情景研究提供了reassuring的验证。

### Optimizing Gaussian process emulation and generalized additive model fitting for rapid, reproducible earth system model analysis

**作者**: Baldock et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-7767-2026](https://doi.org/10.5194/gmd-19-7767-2026) · **引用数**: 0

**匹配主题**: earth system model
{: .label .label-green }

> 复杂建模系统的模型不确定性成因可通过大型扰动参数集成（PPE）结合统计模拟器加以识别，以扩大样本量并实现不确定性分解。本研究提出了将高斯过程模拟器和广义可加模型拟合于PPE输出的优化工作流，在开源软件中加以实现，涵盖试验设计、模拟器训练与验证、敏感性分析及观测约束等环节。以地球系统模型PPE为例的示范表明，优化方法在计算上仍可行的前提下大幅降低了模拟误差，适合无专职统计基础设施的研究团队使用。

---

### Evidence that end-of-century emulation errors under overshoot remain largely within internal variability in an Earth system model

**作者**: Lonergan et al.

**期刊**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae9c58](https://doi.org/10.1088/1748-9326/ae9c58) · **引用数**: 0

**匹配主题**: earth system model
{: .label .label-green }

> 在温室气体减排力度不足的背景下，温控目标被短暂突破后再回落的超调排放情景日益受到关注。统计模拟器提供了一种计算高效的探索方式，但其在这类更复杂路径下的模拟误差是否仍在可接受范围内尚不明确。利用完整地球系统模型，本研究表明，超调情景下的端世纪模拟误差总体上保持在内部变率范围之内，支持将模拟器用于快速探索超调路径——对净负排放情景下的水资源预测具有参考意义。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2（仅S2有效；OpenAlex返回429错误） |
| 检索主题数 | 35 |
| 总获取论文数 | 12 |
| 去重后论文数 | 10 |
| LLM相关性筛选后 | 6 |
| 剔除（不相关） | 4 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|------:|
| Geoscientific Model Development | 2 |
| Philosophical Transactions of the Royal Society B | 1 |
| Hydrology and Earth System Sciences | 1 |
| Environmental Management | 1 |
| Environmental Research Letters | 1 |

## 筛选标准

**主题关键词**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model, estuary, coastal, freshwater discharge, river plume, ocean biogeochemistry, marine heatwave, paleohydrology, paleoclimate, Quaternary, Holocene, Pleistocene, fluvial geomorphology, river terrace, loess, drainage network, river capture, landscape evolution, luminescence dating

**数据库**: Semantic Scholar, OpenAlex

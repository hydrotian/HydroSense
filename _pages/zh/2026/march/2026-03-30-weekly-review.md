---
layout: default
title: "第13周（3月23日 - 3月30日），20篇"
nav_order: 34
nav_exclude: true
lang: zh
lang_link: /2026/march/2026-03-30-weekly-review
date: 2026-03-30
categories: [weekly-zh, 2026, march]
tags: [hydrology, literature-review, research]
paper_count: 20
highlight: "忽略植物对CO2的响应会导致对未来干旱严重程度的系统性高估。"
---

# 每周文献综述
{: .no_toc }

**第13周** · 2026年3月23日–30日
{: .text-grey-dk-000 }

在**5**个主题中发现**20**篇相关论文
{: .fs-5 .fw-300 }

## 摘要概述

本周文献在干旱预测方法和陆面模型方面取得了重要进展。发表在《Environmental Research Climate》上的一项重要发现对标准干旱预测的准确性提出了质疑，该研究表明忽略植物对升高CO₂浓度的生理响应会导致对未来干旱严重程度的系统性高估。与此同时，两个新的陆面模型——NoahPy（用于多年冻土的可微分Noah LSM）和ClimaLand（专为数据驱动参数化设计）——代表了基于物理的模型与机器学习日益融合的趋势。发表在JAMES上的一项关于ELM中地下水位深度机器学习校准的研究对E3SM社区尤为重要，该研究表明当地下水位深度表征得到校正后，水文循环可以得到显著改善。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 干旱预测与气候变化影响

气候变化下的干旱问题本周受到了广泛关注，相关研究涵盖了从大陆到流域尺度。Stagl等人利用多模型集合预测了欧洲的水文干旱变化轨迹，发现在中等和高排放情景下干旱状况均将加剧。Fowler等人通过分析季节性干旱变化来应对澳大利亚干旱预测中持续存在的不确定性，发现尽管降水预测存在分歧，但径流干旱加剧在不同模型间具有一致性。Tian等人研究了水库在调节澜沧江-湄公河流域旱涝急转中这一关键但常被忽视的作用。重要的是，Slater等人指出，大多数干旱预测由于忽略了植物对升高CO₂浓度的生理响应——即气孔导度降低从而减少实际蒸散发——而系统性地高估了干旱严重程度，这对水资源规划具有重大意义。

### Hydrological drought projections across Europe under climate change

**作者**: J. Stagl et al.

**期刊**: *npj Natural Hazards* · **DOI**: [10.1038/s44304-025-00152-w](https://doi.org/10.1038/s44304-025-00152-w) · **引用数**: 0

**匹配主题**: 水文模型、径流、水流量、干旱、气候变化
{: .label .label-green }

> 利用多模型集合在中等和高排放情景下预测了欧洲的水文干旱变化轨迹，发现整个欧洲大陆的干旱状况将加剧。

---

### Future changes in seasonal drought in Australia

**作者**: A. Ukkola, S. Thomas, E. Vogel, U. Bende-Michl, S. T. Siems, V. Matic et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-1463-2026](https://doi.org/10.5194/hess-30-1463-2026) · **引用数**: 4

**匹配主题**: 水文模型、水流量、干旱、季节性
{: .label .label-green }

> 利用国家水文预测集合评估了澳大利亚未来干旱变化，发现尽管降水预测存在分歧，但径流干旱加剧在不同模型间具有一致性。

---

### Mitigating drought-flood abrupt alternation: role of reservoirs in the Lancang-Mekong Basin

**作者**: Z. Tian et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-671-2026](https://doi.org/10.5194/hess-30-671-2026) · **引用数**: 0

**匹配主题**: 洪水、干旱
{: .label .label-green }

> 研究了水库在调节澜沧江-湄公河流域旱涝急转中的作用，表明在气候变化下水库调度可以显著缓解旱涝急转事件。

---

### Neglecting plant physiology leads to systematic overestimation of drought projections

**作者**: L. Slater et al.

**期刊**: *Environmental Research Climate* · **DOI**: [10.1088/2752-5295/ae583c](https://doi.org/10.1088/2752-5295/ae583c) · **引用数**: 0

**匹配主题**: 水文学、水流量、干旱
{: .label .label-green }

> 证明了忽略植物对升高CO₂浓度的生理响应会导致对未来干旱严重程度的系统性高估，因为气孔导度降低会减少实际蒸散发。这对气候变化下的水资源规划具有重大意义。

---

### The Future of Snowpack Drought in the Upper Colorado River Basin (USA)

**作者**: 作者未列出

**期刊**: *Hydrology* · **DOI**: [10.3390/hydrology13040100](https://doi.org/10.3390/hydrology13040100) · **引用数**: 0

**匹配主题**: 河流、径流、水流量、干旱
{: .label .label-green }

> 研究了科罗拉多河上游流域——美国西部重要的供水区域——未来的雪旱预测。

---

## 陆面模型与地球系统模型

一组论文通过机器学习集成推动了陆面模型的发展。Li等人提出了NoahPy，一个面向多年冻土热-水文过程的可微分Noah陆面模型。Wang等人推出了ClimaLand，一个专为适应数据驱动参数化而设计的新型陆面模型。对E3SM社区尤为值得关注的是，一项关于ELM中地下水位深度机器学习校准的研究表明，校正地下水位深度偏差可以显著改善陆面水文和陆-气通量。此外，Salimi等人增强了ECMWF ecLand模型中的冰川和冰盖表征。

### NoahPy: a differentiable Noah LSM for permafrost thermo-hydrology

**作者**: W. Tian, H. Yu, S. Zhao, Y. Cao, W. Yi, J. Xu et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-57-2026](https://doi.org/10.5194/gmd-19-57-2026) · **引用数**: 1

**匹配主题**: 水文学、陆面模型、地球系统模型
{: .label .label-green }

> 创建了Noah陆面模型的可微分版本，以实现将基于物理过程的模型与深度学习相结合的混合模型用于多年冻土模拟，为寒区水文的自动参数校准和物理-机器学习混合方法开辟了道路。

---

### ClimaLand: A Land Surface Model for Data-Driven Parameterizations

**作者**: K. Deck, R. K. Braghiere, A. A. Renchon, J. Sloan, G. Bozzola, E. Speer et al.

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025ms005118](https://doi.org/10.1029/2025ms005118) · **引用数**: 3

**匹配主题**: 陆面模型、地球系统模型
{: .label .label-green }

> 一个专为实现次网格过程数据驱动参数化而设计的新型陆面模型，提供了一个可以用机器学习组件替换或增强传统参数化方案的框架。

---

### ML Calibration of Groundwater Table Depth in ELM

**作者**: 作者未列出

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025MS005184](https://doi.org/10.1029/2025MS005184) · **引用数**: 0

**匹配主题**: 水文学、陆面模型
{: .label .label-green }

> 证明了使用机器学习校正地下水位深度偏差可以显著改善E3SM陆面模型(ELM)中的陆面水文和陆-气通量。

---

### Enhancing Glaciers and Ice Sheets in ecLand

**作者**: S. Salimi et al.

**期刊**: *The Cryosphere* · **DOI**: [10.5194/tc-20-1119-2026](https://doi.org/10.5194/tc-20-1119-2026) · **引用数**: 0

**匹配主题**: 水文学、陆面模型
{: .label .label-green }

> 增强了ECMWF ecLand模型中的冰川和冰盖表征，改善了跨尺度的地表能量平衡和融水水文过程。

---

### Advancing ecohydrological modelling: LPJ-GUESS with ParFlow

**作者**: Z. Jia, S. Chen, Y. H. Fu, D. Martín Belda, D. Wårlind, S. Olin et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-1727-2026](https://doi.org/10.5194/gmd-19-1727-2026) · **引用数**: 2

**匹配主题**: 水文学、水文模型
{: .label .label-green }

> 将LPJ-GUESS动态植被模型与ParFlow集成，以捕捉许多地球系统模型目前忽略的地形驱动的植被-地表-地下水相互作用。

---

## 水库调度与水资源管理

水库对水文的影响从多个角度受到了关注。Vicente-Serrano等人分析了地中海流域一个世纪的流量变化趋势(1914–2022)，发现植被绿化和水库建设——而不仅仅是气候变化——是径流减少的主要驱动因素。Li等人展示了将SWOT卫星数据与多源观测相结合实现近实时日尺度水库水位监测的方法。Wu等人量化了黄土高原水库开发中此前被低估的蒸发损失。

### Vegetation greening and reservoir construction as drivers of discharge trends in the Mediterranean

**作者**: S. M. Vicente-Serrano et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135387](https://doi.org/10.1016/j.jhydrol.2026.135387) · **引用数**: 0

**匹配主题**: 径流、水流量、水库
{: .label .label-green }

> 分析了地中海流域一个世纪的流量变化趋势(1914–2022)，发现植被绿化和水库建设与气候变化一样是径流减少的主要驱动因素。

---

### Rolling predictive optimal scheduling of reservoirs for flood control and power generation

**作者**: 作者未列出

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-43532-6](https://doi.org/10.1038/s41598-026-43532-6) · **引用数**: 0

**匹配主题**: 水文学、水文模型、水库
{: .label .label-green }

> 开发了在预测不确定性下的滚动预测最优调度方法，以平衡水库防洪和水力发电目标。

---

### Integrating SWOT for Near-Daily Reservoir Water Level Monitoring

**作者**: P. Zhan, J. Wang, T. Chen, S. Luo, K. Liu, L. Ke et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2024WR039711](https://doi.org/10.1029/2024WR039711) · **引用数**: 1

**匹配主题**: 水文模型、水库
{: .label .label-green }

> 开发了将SWOT与多源卫星观测相集成的框架，实现了近实时日尺度水库水位监测，提升了水库管理的遥感能力。

---

### Increased surface water evaporation loss from reservoir development on the Loess Plateau

**作者**: Z. Wu et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-67-2026](https://doi.org/10.5194/hess-30-67-2026) · **引用数**: 1

**匹配主题**: 水库、地表水
{: .label .label-green }

> 量化了黄土高原水库开发中此前被低估的蒸发损失，揭示了其对区域水量平衡的显著影响。

---

### Drought propagation under reservoir regulation in the Hanjiang River Basin

**作者**: 作者未列出

**期刊**: *River* · **DOI**: [10.1002/rvr2.70045](https://doi.org/10.1002/rvr2.70045) · **引用数**: 0

**匹配主题**: 水文模型、水流量、水库、干旱
{: .label .label-green }

> 研究了水库调节如何改变汉江流域的干旱传播特征，对变化气候条件下的水资源管理具有启示意义。

---

## 水文模型方法进展

多篇论文推进了水文模型方法的发展。Knoben等人评估了水文模型模拟径流极端值和旱涝转换的能力，揭示了模型在复合事件方面的重要局限性。Poncelet等人开发了一种在概念性径流模型中追踪降雨贡献的方法，表明较湿润的流域对短期降雨响应更强，而较干旱的流域则越来越依赖多年尺度的降雨。Munkhjargal等人揭示了寒区高山流域中地形和植被对流域水文过程的各自贡献。

### How well do hydrological models simulate streamflow extremes and drought-to-flood transitions?

**作者**: E. Muñoz-Castro, B. Anderson, P. C. Astagneau, D. L. Swain, P. A. Mendoza, M. I. Brunner

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-825-2026](https://doi.org/10.5194/hess-30-825-2026) · **引用数**: 4

**匹配主题**: 水流量、洪水、干旱
{: .label .label-green }

> 评估了水文模型捕捉复合极端事件——特别是干旱后快速出现洪水——的能力，识别了哪些建模决策对这些日益重要的转换过程的模拟影响最大。

---

### Tracking rainfall contribution in a conceptual runoff model

**作者**: C. Poncelet et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135366](https://doi.org/10.1016/j.jhydrol.2026.135366) · **引用数**: 0

**匹配主题**: 水文模型、径流、水流量、地表水
{: .label .label-green }

> 开发了一种在概念性径流模型中追踪降雨贡献的方法，表明较湿润的流域对短期降雨响应更强，而较干旱的流域则越来越依赖多年尺度的降雨。

---

### Revealing the influence of topography and vegetation on hydrological processes in cold alpine basins

**作者**: M. Munkhjargal et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-1585-2026](https://doi.org/10.5194/hess-30-1585-2026) · **引用数**: 0

**匹配主题**: 水文学、水文模型、径流、水流量
{: .label .label-green }

> 利用逐步建模方法揭示了寒区高山流域中地形和植被对流域水文过程的各自贡献。

---

## 统计数据

| 指标 | 数量 |
|:-------|------:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 去重前论文总数 | 2,156 |
| 去重后唯一论文数 | 1,863 |
| LLM相关性筛选后 | 20 |
| 被排除（不相关） | 1,843 |

## 筛选标准

**主题**: 水文学、水文模型、河流、径流、水流量、水库、水资源管理、洪水、干旱、季节性、陆面模型、气候变化、水力发电、地表水、灌溉、地球系统模型

**数据库**: Semantic Scholar, OpenAlex

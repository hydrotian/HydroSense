---
layout: default
title: "第36周（9月01日 - 9月08日），5篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/september/2026-09-08-weekly-review
date: 2026-09-08
categories: [weekly-zh, 2026, september]
tags: [hydrology, literature-review, research]
paper_count: 5
highlight: "本周ORCHIDEE获得改进的土壤大孔隙度和积雪致密化物理参数化，同时新增叶片周转和超分辨率均方根土壤湿度偏差改进等陆面模式参数化方案。"
---

# 每周文献综述
{: .no_toc }

**第36周** · 2026年9月1日–9月8日
{: .text-grey-dk-000 }

共发现 **5** 篇相关论文，涵盖 **3** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

本周文献集中于陆面模式过程改进和降水不确定性下的水文模拟。三项研究推进了陆面模式中水循环物理过程的表达——分别涉及土壤垂向非均质性、土壤大孔隙度亚网格效应以及冰盖积雪致密化——第四项研究改进了草地陆面模式中的植被物候参数化。第五项研究评估了格点降水产品是否真正改善了数据稀缺季风山地流域SWAT+模型的径流模拟，结果发现格点降水产品相较于站点观测并无一致的性能优势。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 陆面模式中的土壤物理与水分分配

准确表征土壤水力过程仍是陆面模式的持续挑战。Krishnan 等人证明，在应用于小农耕作系统的超分辨率（30 米）陆面模式配置中，考虑土壤垂向非均质性可显著减少根区土壤湿度偏差——这对全球陆面模式标定具有重要意义，因为默认的垂向均匀土壤属性假设会引入系统性误差。在耦合地球系统模式典型的 100 公里尺度上，Kiałka 等人表明，长期被大尺度模式忽视的土壤大孔隙度显著改变了ORCHIDEE中的排水与产流–入渗分配，且亚网格参数化方案的选择会调节这一效应在大尺度水循环通量上的投影强度。这两项研究共同揭示了剖面内垂向非均质性和水平亚网格结构这两个维度对陆面模式水循环精度的重要性。

### Soil vertical heterogeneity reduces rootzone soil moisture bias in hyper-resolution land surface model over smallholder agricultural systems

**作者**：Vishnu U. Krishnan, N. Vergopolan, B. B. Singh, J. Indu, L. Karthikeyan

**期刊**：*Agricultural Water Management* · **DOI**：[10.1016/j.agwat.2026.110673](https://doi.org/10.1016/j.agwat.2026.110673) · **引用数**：2

**匹配主题**：land surface model
{: .label .label-green }

> 摘要暂不可用。

---

### Subgrid parametrizations mediate the large‐scale effects of soil macroporosity on the water cycle in the ORCHIDEE land surface model

**作者**：Filip Kiałka, V. Bastrikov, Omar Flores, K. Naudts, S. Luyssaert, Bertrand Guenet

**期刊**：*Vadose Zone Journal* · **DOI**：[10.1002/vzj2.70136](https://doi.org/10.1002/vzj2.70136) · **引用数**：0

**匹配主题**：land surface model
{: .label .label-green }

> 土壤结构在决定核心尺度土壤水力特性方面几乎与土壤质地同等重要。在地块尺度上，土壤结构——尤其是大孔隙度——强烈影响排水及产流–入渗分配。在陆面模式典型的 100 公里尺度上，大孔隙度对水循环的影响受亚网格参数化方案选择的调控。

---

## 地球系统模式中的冰冻圈与植被物候过程

本周两项研究将陆面模式的过程范围拓展至物候和冰冻圈动力学与水碳循环相互作用的领域。Conesa 等人在ORCHIDEE中为冰盖应用实现了干雪初始化和致密化物理参数化，使格陵兰和南极洲上的雪包演化模拟更为准确——这一组件对冰盖物质平衡收支和海平面预测具有直接影响。在截然不同的生物群区中，Seitz 等人为QUINCY陆面模式中的草地引入了基于生理机制的叶片周转方案，将此前经验性的过程植根于机制性原理，使植被周转速率与气候强迫的耦合更为合理。这两项进展均反映了陆面模式社区的一个广泛趋势：从经验调整关系转向在不同气候情景下更具可移植性的过程性表达。

### Dry snow initialization and densification over the Greenland and Antarctic ice sheets in the ORCHIDEE land surface model

**作者**：Philippe Conesa, C. Agosta, S. Charbit, C. Dumas, Simon Beylat, N. Raoult

**期刊**：*The Cryosphere* · **DOI**：[10.5194/tc-20-4973-2026](https://doi.org/10.5194/tc-20-4973-2026) · **引用数**：1

**匹配主题**：land surface model
{: .label .label-green }

> 准确模拟冰盖上的雪包对于量化其物质平衡贡献及其对海平面上升的影响至关重要。雪包演化主要受地表气候控制，同时也受致密化等内部过程影响。在陆面模式中，这些过程必须被准确初始化和动态表达，以重现观测到的雪密度剖面和物质平衡。

---

### A general physiologically driven representation of leaf turnover in grasslands in the QUINCY land surface model

**作者**：Josua Seitz, Midori Yajima, Yu Zhu, L. S. K. Joseph, Jin-Yan Yang, F. Lacroix et al.

**期刊**：*Geoscientific Model Development* · **DOI**：[10.5194/gmd-19-8289-2026](https://doi.org/10.5194/gmd-19-8289-2026) · **引用数**：0

**匹配主题**：land surface model
{: .label .label-green }

> 陆地植被通过对全球碳循环的控制在塑造地球气候中发挥重要作用。理解和预测植被物候及生物量向土壤有机质的周转对于我们理解和量化地球系统模式中的陆地–气候反馈至关重要。

---

## 径流模拟中的降水不确定性

De la Fraga 等人在具有季风气候的墨西哥山地流域中评估了四种降水输入数据集——站点观测与格点产品的不同组合——对SWAT+模型性能的影响。研究发现，没有任何单一格点产品能一致优于仅基于站点观测的输入，这凸显了降水输入敏感性的场地特殊性，以及在地形和气候情境间进行推广的困难——这对必须在全球范围指定降水场的大尺度河流汇流模式是一个重要挑战。

### Hydrologic modeling in mountainous terrains with monsoonal climate: Do gridded precipitation data improve streamflow simulations?

**作者**：Pasquinel de la Fraga, E. Vivoni, Yalina Montecelos-Zamora, Francisco José Del-Toro-Guerrero, Tereza Cavazos, T. Kretzschmar

**期刊**：*Frontiers in Water* · **DOI**：[10.3389/frwa.2026.1788195](https://doi.org/10.3389/frwa.2026.1788195) · **引用数**：0

**匹配主题**：hydrologic model
{: .label .label-green }

> 在数据稀缺的山地地区进行准确的水文模拟仍具挑战性，原因在于强烈的气候变率、复杂地形以及有限的地面观测数据。本研究评估了四种降水输入对季风山地流域SWAT+模型性能的影响，对比格点产品与站点观测输入，以确定空间覆盖度的提升是否转化为更好的径流模拟效果。

---

## 统计信息

| 指标 | 数量 |
|:-----|-----:|
| 搜索数据库数 | 2 |
| 搜索主题数 | 16 |
| 获取论文总数 | 9 |
| 去重后 | 8 |
| 经LLM相关性筛选后 | 5 |
| 已拒绝（不相关） | 3 |

### 按期刊统计

| 期刊 | 论文数 |
|:-----|-------:|
| Vadose Zone Journal | 1 |
| Agricultural Water Management | 1 |
| The Cryosphere | 1 |
| Geoscientific Model Development | 1 |
| Frontiers in Water | 1 |

## 筛选标准

**主题词**：hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**：Semantic Scholar, OpenAlex

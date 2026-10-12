---
layout: default
title: "第40周（9月28日 - 10月05日），3篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/october/2026-10-05-weekly-review
date: 2026-10-05
categories: [weekly-zh, 2026, october]
tags: [hydrology, literature-review, research]
paper_count: 3
highlight: "一种无流域限制的可解释机器学习分布式水文模型，无需流域特定率定即可泛化至未测量流域。"
---

# 每周文献综述
{: .no_toc }

**第40周** · 2026年9月28日–10月05日
{: .text-grey-dk-000 }

共 **3** 篇相关论文，分布于 **3** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

本周由于OpenAlex API访问频率限制，所有结果均仅来自Semantic Scholar，整体覆盖范围有所缩减，是一个较为平淡的搜索周。本期筛选出三篇相关论文：一篇关于无流域限制的可解释机器学习分布式水文建模框架（无需流域特定率定）、一篇系统梳理低影响开发雨水设施水文性能与成本权衡的基于物理的设计图集，以及一篇针对温带森林陆面模型物候不确定性的虚拟对照基准测试研究。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 分布式水文建模中的机器学习方法

本周提出的无流域限制方法是迈向可泛化数据驱动水文学的重要一步。传统物理模型需要针对特定流域进行率定，限制了其迁移能力；而早期神经网络模型则以牺牲可解释性为代价。Talha和Nejadhashemi的框架在两者之间架起了桥梁——既在空间上实现分布式预测，同时保持可解释性，使其在未测量流域和大尺度大陆性河网路由系统中具有实际应用潜力。

### Watershed-agnostic modeling: An explainable, distributed, data-driven hydrologic model

**作者**: M. Talha, A. Nejadhashemi

**期刊**: *Environmental Modelling & Software* · **DOI**: [10.1016/j.envsoft.2026.107149](https://doi.org/10.1016/j.envsoft.2026.107149) · **引用数**: 0

**匹配主题**: hydrologic model
{: .label .label-green }

> 摘要暂不可用。

---

## 城市水文与雨水设施设计

长期以来，低影响开发（LID）设计在容积性水质标准与实际水文性能之间存在明显鸿沟。LID设计图集通过提供基于物理模拟的参数化数据库，直接弥补了这一不足，使权衡分析过程变得清晰可见。这种图集式方法有望大幅降低反复试错设计的负担，并促进LID工具更好地融入城市流域综合模型。

### LID-Design Atlas: Mapping Hydrologic Performance and Cost Trade-Offs in Infiltration-Based LID Design

**作者**: M. Gomes

**期刊**: *Journal of Hydrologic Engineering* · **DOI**: [10.1061/jhyeff.heeng-6901](https://doi.org/10.1061/jhyeff.heeng-6901) · **引用数**: 0

**匹配主题**: hydrologic model
{: .label .label-green }

> 渗透型低影响开发（LID）措施被广泛用于减缓城市径流影响，然而其设计通常以容积性水质标准为依据，掩盖了水文性能、几何形态、土壤性质与成本之间的关键权衡关系。本研究提出LID设计图集（LIDA），一种系统性映射上述权衡关系的基于物理的设计数据库，以支持雨水管理中更为科学的决策制定。

---

## 陆面模型物候基准测试

物候不确定性——即陆面模型对叶展和叶落时间的模拟精度——会直接传导至水分和碳通量预测结果。Yajima等人通过设计一项虚拟对照实验，将物候表达误差与其他陆面模型参数不确定性加以分离，从而更清晰地揭示了物候误表达在哪些方面影响最为显著。这对于改进ELM和CLM在耦合E3SM模拟中的配置——尤其是温带森林生物群区——具有直接的指导意义。

### Benchmarking phenology with a land surface model: an in-silico experiment for temperate forests

**作者**: Midori Yajima, Josua Seitz, W. J. Matthaeus, Gayathri G. Nair, L. Daly, S. Caldararu

**期刊**: *bioRxiv* · **DOI**: [10.1101/2025.11.20.689458](https://doi.org/10.1101/2025.11.20.689458) · **引用数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 植物物候影响生物相互作用以及水分、碳和养分的循环，进而对全球气候产生深远影响。准确量化物候动态因此对生态预测至关重要，然而由于数据来源、平滑方法和日期提取技术各异，估算结果差异悬殊。物候观测处理流程的选取对陆面模型基准测试具有直接影响，因为参考数据的选择决定了模型评估结果。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2（仅S2；OpenAlex返回429错误） |
| 检索主题数 | 16 |
| 获取论文总数 | 5 |
| 去重后 | 5 |
| LLM相关性筛选后 | 3 |
| 不相关（已剔除） | 2 |

### 各期刊论文数

| 期刊 | 篇数 |
|:-----|-----:|
| Environmental Modelling & Software | 1 |
| Journal of Hydrologic Engineering | 1 |
| bioRxiv | 1 |

## 筛选标准

**检索主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**检索数据库**: Semantic Scholar, OpenAlex

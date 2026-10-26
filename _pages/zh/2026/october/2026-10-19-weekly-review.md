---
layout: default
title: "第42周（10月12日 - 10月19日），1篇"
nav_order: 35
nav_exclude: true
lang: zh
lang_link: /2026/october/2026-10-19-weekly-review
date: 2026-10-19
categories: [weekly-zh, 2026, october]
tags: [hydrology, literature-review, research]
paper_count: 1
highlight: "Noah-MP参数化方案替代方案（RUN、SFC、INF、STC）分别将密苏里河流域径流KGE提升0.14–0.44。"
---

# 每周文献综述
{: .no_toc }

**第42周** · 2026年10月12日–19日
{: .text-grey-dk-000 }

共找到 **1** 篇相关论文，涵盖 **1** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

本周水文学文献数量较少，经期刊黑名单过滤和LLM相关性审查后，仅有一篇论文通过筛选（OpenAlex因请求频率限制不可用，结果仅来自Semantic Scholar）。这篇论文针对密苏里河流域开展了Noah-MP陆面模式的大流域参数化方案评估，为改善径流和融雪模拟提供了具有实际指导意义的参数化方案选择建议。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 陆面模型

本周仅一篇论文，但内容扎实：Cho等人对密苏里河流域50个流域开展了Noah-MP替代参数化方案的系统评估，量化了各方案在不同物理过程方面的KGE改进效果。结果显示，冻土渗透率（INF）和地表热交换系数（SFC）方案的径流改进幅度最大（KGE分别提升+0.44和+0.38），而积雪/土壤温度时间步长方案（STC）在以积雪为主的子流域中最有效地降低了雪水当量（SWE）偏差——尽管SWE改善并不总能转化为径流模拟的提升。研究发现，在气候和植被覆盖类型各异的流域中，没有单一最优方案，这进一步强调了在大规模Noah-MP应用（如E3SM-ELM工作流）中进行区域特定率定的必要性。

### Basin-scale evaluation of the Noah-MP land surface model for runoff and snow generation in the Missouri River Basin: insights and recommendations for parameterization scheme selection

**作者**: Eunsaem Cho, C. Vuyovich, Bai-Ling Li, Jennifer M. Jacobs

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-6359-2026](https://doi.org/10.5194/hess-30-6359-2026) · **引用数**: 1

**匹配主题**: hydrologic model, land surface model
{: .label .label-green }

> Process-based land surface models, such as the Noah-Multiparameterization (Noah-MP) model, are widely used for large-scale hydrologic simulations because of their flexibility in selecting multiple parameterization schemes. However, limited guidance on choosing appropriate configurations constrains their reliability in representing runoff and snowmelt dynamics across diverse land-cover and snow conditions. This study evaluates the default and four alternative parameterization schemes in the Noah-MP land surface model, including Runoff and Groundwater (RUN), Surface Exchange Coefficient for Heat (SFC), Frozen Soil Permeability (INF), and Snow/Soil Temperature Time Scheme (STC), across 50 Hydro-Climate Data Networks (HCDNs) in the Missouri River Basin. Model performance was evaluated using USGS streamflow observations and snow water equivalent (SWE) estimates from the University of Arizona dataset for 2014–2023. Results showed that the alternative schemes improved runoff simulation compared to the default scheme through different approaches representing key hydrological and thermodynamic processes. Specifically, the RUN, SFC, INF, and STC experiments improved the Kling–Gupta Efficiency (KGE) by 0.19, 0.38, 0.44, and 0.14, respectively in representative subbasins, through enhanced groundwater dynamics, reduced evapotranspiration bias, improved rapid runoff response, and more accurate SWE evolution. SWE evaluation further indicates that the STC experiment most effectively reduced SWE bias in snow-dominated subbasins, though improvements in SWE did not universally translate into better runoff simulation. These results highlight the importance of basin-specific parameterization schemes within Noah-MP to improve hydrological prediction and water management across diverse hydroclimatic regions.

---

## 统计信息

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 获取论文总数 | 6 |
| 去重后 | 5 |
| 经LLM相关性筛选后 | 1 |
| 判定为不相关 | 2 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|------:|
| Hydrology and Earth System Sciences | 1 |

## 筛选标准

**匹配主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

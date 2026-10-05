---
layout: default
title: "第39周（9月21日 - 9月28日），1篇"
nav_order: 35
nav_exclude: true
lang: zh
lang_link: /2026/september/2026-09-28-weekly-review
date: 2026-09-28
categories: [weekly-zh, 2026, september]
tags: [hydrology, literature-review, research]
paper_count: 1
highlight: "深度学习同化太阳诱导荧光卫星观测至ISBA陆面模型，提升地球系统模拟中植被-水文耦合精度（Biogeosciences）。"
---

# 每周文献综述
{: .no_toc }

**第39周** · 2026年9月21日–9月28日
{: .text-grey-dk-000 }

在 **1** 个主题中发现 **1** 篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

第39周水文与水资源领域文献发表量异常稀少：由于整个搜索过程中OpenAlex因速率限制（HTTP 429错误）持续不可用，Semantic Scholar在经过ISSN期刊名单过滤后仅返回一篇符合标准的论文。该论文推进了陆面建模方法论，将深度学习应用于将卫星观测的太阳诱导荧光同化到ISBA模型中——该技术对改善地球系统模型中植被-水文耦合表达具有直接意义。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 面向陆面模型数据同化的机器学习方法

数据同化——将模型状态与观测相结合的过程——是陆面和地球系统建模中的长期挑战。Vanderbecken等人利用深度学习，将Sentinel-5P卫星上TROPOMI仪器获取的太阳诱导荧光（SIF）同化到ISBA陆面模型。SIF是总初级生产力和冠层光利用效率的直接近实时代理变量；通过训练神经网络代理模型来桥接模型预报状态与卫星反演的SIF信号，作者证明ISBA中植被动态的表达得到改善。该方法与耦合建模框架具有良好兼容性，并有潜力扩展到其他卫星观测数据流，包括与水分胁迫和土壤湿度估算相关的观测。

### Using deep learning to assimilate sun-induced fluorescence satellite observations in the ISBA land surface model

**作者**: P. Vanderbecken, J. Vural, Oscar Rojas-Muñoz, S. Garrigues, B. Bonan, C. Bacour et al.

**期刊**: *Biogeosciences* · **DOI**: [10.5194/bg-23-6687-2026](https://doi.org/10.5194/bg-23-6687-2026) · **引用次数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 对地表和植被的精确表征对于模拟地球表层CO₂循环对气候和气象条件的响应至关重要。为应对这一挑战，越来越多的卫星任务被发射以监测植被状况和生物量。其中，携带TROPOMI仪器的哥白尼Sentinel-5P任务可反演太阳诱导荧光（SIF），这是一种与光合活性直接相关的信号。我们提出了一种基于深度学习的数据同化方法，将TROPOMI SIF观测同化到ISBA陆面模型中，改善其对植被动态和地表-大气碳交换的模拟。该方法展示了与耦合陆面-大气建模框架集成的强大潜力。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 获取论文总数 | 1 |
| 去重后 | 1 |
| 期刊过滤后（黑名单） | 1 |
| LLM相关性筛选后 | 1 |
| 剔除（不相关） | 0 |

**注**: OpenAlex本周对全部16个主题返回HTTP 429（速率限制）错误，所有结果均来自Semantic Scholar。这显著降低了覆盖范围；论文数量偏少反映了API可用性问题，而非发表活动的真实低迷。

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|------:|
| Biogeosciences | 1 |

## 筛选标准

**主题关键词**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

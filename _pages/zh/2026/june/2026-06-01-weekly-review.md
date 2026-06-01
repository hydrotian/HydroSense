---
layout: default
title: "第21周（5月18日 - 5月25日），3篇"
nav_exclude: true
lang: zh
lang_link: /2026/june/2026-06-01-weekly-review
date: 2026-06-01
categories: [weekly-zh, 2026, june]
tags: [hydrology, literature-review, research]
paper_count: 3
highlight: "ISSM新增Love数求解器实现公里级耦合冰盖-海平面模拟；城市水文研究推进绿色基础设施建模与深度学习径流预测。"
---

# 每周文献综述
{: .no_toc }

**第21周** · 2026年5月18日–5月25日
{: .text-grey-dk-000 }

在 **2** 个主题中筛选出 **3** 篇相关论文
{: .fs-5 .fw-300 }

## 摘要

本周文献较少，仅Semantic Scholar返回了结果（OpenAlex出现服务问题）。地球系统模型基础设施方面有一项重要进展：JPL团队在ISSM中引入了新的Love数求解器，支持高分辨率耦合冰盖与海平面模拟。另有两项城市水文研究分别考察了绿色基础设施对地下水-地表水相互作用的影响，以及在气候变化条件下深度学习与物理模型在径流估算中的对比。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 地球系统模型基础设施

一项重要的耦合冰盖-海平面模型计算进展：Caron等人在ISSM中引入了并行化Love数求解器，将球谐分辨率提升至约10,000阶，并支持多种粘弹性流变学模型（Maxwell、Burgers、扩展Burgers）。该求解器能够以公里级分辨率模拟固体地球对冰质量变化的响应，其数值效率支持大规模集合模拟和不确定性量化——直接适用于在地球系统模型框架内预测极地冰盖对未来海平面的贡献。

### Love number computation within the Ice-sheet and Sea-level System Model (ISSM v4.24)

**作者**：L. Caron, E. Ivins, E. Larour, S. Adhikari, L. Métivier

**期刊**：*Geoscientific Model Development* · **DOI**：[10.5194/gmd-19-4031-2026](https://doi.org/10.5194/gmd-19-4031-2026) · **引用数**：1

**匹配主题**：earth system model
{: .label .label-green }

> 本文介绍的Love数求解器是冰盖与海平面系统模型（ISSM）中的一项新功能，用于计算一维径向对称固体地球对潮汐强迫和地表质量载荷的响应。该功能可求解分解为yi系统的零频率自由振荡运动方程，实现球谐截断阶数约10,000及以上的高波数计算。它能够以重力势变化、垂直和水平基岩位移及极移的形式捕获固体地球对阶跃函数强迫的高分辨率响应。模型融合了可压缩各向同性弹性以及三种线性粘弹性地幔流变学模型：Maxwell材料、Burgers材料和扩展Burgers材料（EBM）。我们详细介绍了求解器的并行化和数值优化方法，并报告了与社区基准解的精度对比结果。主要目标是以支持大规模集合模拟和不确定性量化的数值效率，实现公里级横向分辨率下地表质量输运（如极地冰盖和海平面变化）与固体地球模型的耦合模拟。

---

## 城市水文与径流模型

两项研究从互补角度探讨城市水问题。Masoudiashtiani和Peralta使用带河流径流模块的MODFLOW量化了犹他州红溪流域中草沟对含水层补给和地表水可用性的12个月影响——发现约三分之二的绿色基础设施诱发补给向下游流动，30%回归河流。与此同时，Balacumaresan等人将深度学习与物理模型在城市径流估算中进行对比，评估了在历史和未来气候条件下的模型表现。

### Predicted Hydrologic Changes Due to Urban Green Infrastructure Implementation

**作者**：S. Masoudiashtiani, Richard C. Peralta

**期刊**：*Environments* · **DOI**：[10.3390/environments13050279](https://doi.org/10.3390/environments13050279) · **引用数**：0

**匹配主题**：hydrologic model
{: .label .label-green }

> 数值模拟量化了在美国犹他州红溪（RBC）周围实施绿色基础设施（GI）草沟对非承压含水层蓄水量及地下水-地表水相互作用的瞬态影响。红溪流域从未开发的国家森林山地过渡到盐湖谷内的下游城市化地区。本初步研究表明，在雨季（4-6月）增加城市化地区的雨水入渗，至少到次年3月可以：(a)增强含水层补给，支持地下水可持续产量；(b)改善地表水可用性。模拟预测了在RBC周围704英亩区域内假设实施草沟带来的含水层补给水文影响。所用模型HyperRBC是美国地质调查局（USGS）瞬态数值流模型MODFLOW在盐湖谷实施的改编版本。模型预测表明，到次年3月底：(a)约3%的GI诱发补给将留在HyperRBC区域的非承压含水层中；(b)66.6%的补给将向北流入非承压含水层的下游延伸段；(c)30.3%将排入附近的溪流和河流。

---

### Evaluation of Deep Learning and Physically Based Models for Urban Streamflow Estimation Under Historical and Future Climate Conditions

**作者**：Harshanth Balacumaresan, M. Imteaz, I. Hossain, Md Abdul Aziz, Tanveer Choudhury

**期刊**：*Water Resources Management* · **DOI**：[10.1007/s11269-026-04751-8](https://doi.org/10.1007/s11269-026-04751-8) · **引用数**：0

**匹配主题**：streamflow
{: .label .label-green }

> 摘要暂无。

---

## 统计

| 指标 | 数量 |
|:-------|------:|
| 搜索数据库数 | 2 |
| 搜索主题数 | 16 |
| 获取论文总数 | 13 |
| 去重后 | 10 |
| LLM相关性筛选后 | 3 |
| 被拒绝（不相关） | 7 |

### 按期刊分类

| 期刊 | 论文数 |
|:--------|-------:|
| Geoscientific Model Development | 1 |
| Environments | 1 |
| Water Resources Management | 1 |

## 筛选标准

**主题**：hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**：Semantic Scholar, OpenAlex

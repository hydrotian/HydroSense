---
layout: default
title: "第01周（2019年12月30日 - 2020年1月5日），3篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2020/january/2020-01-05-weekly-review
date: 2020-01-05
categories: [weekly-zh, 2020, january]
tags: [hydrology, literature-review, research]
paper_count: 3
highlight: "2020年开端的三项标志性成果：CMIP6气候敏感度诊断、TRY植物性状数据库扩展，以及基于LSTM序列到序列的降雨径流建模。"
---

# 每周文献综述
{: .no_toc }

**第01周** · 2019年12月30日至2020年1月5日
{: .text-grey-dk-000 }

在**2**个主题中发现**3**篇相关论文
{: .fs-5 .fw-300 }

## 摘要总结

2020年的开篇一周出现了数篇影响深远、被大量引用的成果，为此后多年的水文学与地球系统建模奠定了基础。在《Geophysical Research Letters》上，Zelinka等人诊断了CMIP6模式相对于CMIP5平衡气候敏感度显著升高的原因，将其归因于中高纬低云反馈的增强。《Global Change Biology》发布了TRY植物性状数据库的扩展版本——这一数据资源是陆面模式与地球系统模式植被参数化的基石。《Water Resources Research》则刊载了Xiang、Yan和Demir的工作，引入了基于LSTM序列到序列（seq2seq）结构的降雨径流模型，是深度学习在小时尺度水文预报中的早期代表作之一。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 地球系统模式分析与数据基础

本周在地球系统建模的数据与分析基础方面涌现了两项高影响力成果。Zelinka等人针对气候科学中最核心的未决问题之一——为什么CMIP6模式的平衡气候敏感度高于CMIP5——进行了系统诊断，指出主要驱动力来自中高纬低云反馈的增强，具体表现为云量与云光学厚度的变化，而非热带云反馈。与此同时，Kattge等人发布了TRY数据库的扩展版本并迁移至开放访问协议，TRY是全球植物性状数据的核心资源，支撑着陆面模式与地球系统模式中的植被参数化工作。两篇论文共同说明了诊断性分析与共享数据基础设施在驱动下一代气候与陆面模式发展中的互补作用。

### Causes of Higher Climate Sensitivity in CMIP6 Models

**作者**: Mark D. Zelinka, Timothy A. Myers, Daniel T. McCoy, Stephen Po-Chedley, Peter Caldwell, Paulo Ceppi et al.

**期刊**: *Geophysical Research Letters* · **DOI**: [10.1029/2019gl085782](https://doi.org/10.1029/2019gl085782) · **引用数**: 1,757

**匹配主题**: earth system model
{: .label .label-green }

> 平衡气候敏感度（即全球地表温度对CO₂浓度加倍的响应）长期以来存在较大不确定性。本文指出CMIP6模式中的有效气候敏感度相对于CMIP5显著升高，并将这一升高主要归因于中高纬低云反馈的增强——即云量与云光学厚度的变化，而非热带云反馈。该研究已成为解读CMIP6高端增暖情景的重要参考。

---

### TRY Plant Trait Database – Enhanced Coverage and Open Access

**作者**: Jens Kattge, Gerhard Bönisch, Sandra Díaz, Sandra Lavorel, I. Colin Prentice, Paul Leadley et al.

**期刊**: *Global Change Biology* · **DOI**: [10.1111/gcb.14904](https://doi.org/10.1111/gcb.14904) · **引用数**: 2,005

**匹配主题**: earth system model
{: .label .label-green }

> 植物性状——形态、解剖、生理、生化与物候特征——决定了植物对环境的响应，并调节生态系统的水、碳、能量通量。本次发布显著扩展了TRY数据库的覆盖范围并迁移至开放访问协议，拓宽了植被与陆面建模、功能生态学、生物多样性保护以及生态系统尺度遥感研究的数据基础。TRY此后已成为地球系统模式中基于性状的植被参数化事实上的全球数据标准。

---

## 深度学习驱动的降雨径流建模

本周的第三篇代表作引入了深度序列模型在水文预报中的早期经典应用之一。Xiang、Yan和Demir将基于LSTM的序列到序列（seq2seq）结构应用于爱荷华州两个流域的小时尺度降雨径流预测，并与线性回归、岭回归、Lasso、支持向量回归、高斯过程回归以及普通LSTM进行了系统对比。seq2seq结构能够同时兼顾长期依赖建模与多步输出，在所有指标上均优于基线方法，奠定了LSTM类结构成为此后深度学习水文学浪潮中默认构件的地位。

### A Rainfall-Runoff Model With LSTM-Based Sequence-to-Sequence Learning

**作者**: Zhongrun Xiang, Jun Yan, İbrahim Demir

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2019wr025326](https://doi.org/10.1029/2019wr025326) · **引用数**: 738

**匹配主题**: hydrology, runoff
{: .label .label-green }

> 降雨径流建模是一个复杂的非线性时序问题。本文将基于LSTM的序列到序列（seq2seq）结构应用于爱荷华州Clear Creek与Upper Wapsipinicon两个流域的小时尺度降雨径流预测，输入包括降雨观测、降雨预报、径流观测以及月尺度蒸散发气候态。与线性回归、Lasso、岭回归、支持向量回归、高斯过程回归以及普通LSTM等基线相比，seq2seq模型在Nash-Sutcliffe效率、相关系数、偏差和归一化均方根误差等所有指标上均表现最佳，论文据此指出seq2seq是水文时序预测与短期洪水预报中一个普遍有效的结构。

---

## 统计数据

| 指标 | 数量 |
|:-------|------:|
| 搜索数据库数 | 2 |
| 搜索主题数 | 16 |
| 去重前论文总数 | 2,167 |
| 去重后唯一论文数 | 2,001 |
| LLM相关性筛选后 | 3 |
| 被排除（不相关） | 1,998 |

### 各期刊论文数

| 期刊 | 论文数 |
|:--------|-------:|
| Global Change Biology | 1 |
| Geophysical Research Letters | 1 |
| Water Resources Research | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

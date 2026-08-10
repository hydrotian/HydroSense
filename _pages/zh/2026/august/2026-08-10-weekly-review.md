---
layout: default
title: "第31周（7月27日 - 8月3日），2篇"
nav_order: 34
nav_exclude: true
lang: zh
lang_link: /2026/august/2026-08-10-weekly-review
date: 2026-08-10
categories: [weekly-zh, 2026, august]
tags: [hydrology, literature-review, research]
paper_count: 2
highlight: "加拿大业务化SVS陆面模式的新冻土入渗方案将寒区流域严重模拟失效站点比例从33%降至1%以下；TIPMIP提出新的CMIP7候选ESM实验协议，用于在受控升温与负排放情景下探测地球系统临界点行为。"
---

# 每周文献综述
{: .no_toc }

**第31周** · 2026年7月27日–8月3日
{: .text-grey-dk-000 }

在 **2** 个主题中筛选出 **2** 篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

本周文献以方法论为主，两篇论文均具有直接的业务化与建模应用价值。Bouchard等人证明，加拿大业务化SVS陆面模式中经修订的冻土入渗方案可显著减少寒区流域的流量模拟误差；Jones等人则介绍了TIPMIP——一项拟纳入CMIP7的地球系统模式实验协议，旨在受控升温与负排放路径下探测临界点行为。注：本周OpenAlex因API速率限制（HTTP 429错误）未返回任何结果，文献覆盖范围仅基于Semantic Scholar，可能低估了实际发表量。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 寒区陆面水文模拟

精确表征冻土过程是业务化水文预报的长期挑战，尤其在高纬度和山地流域，春季融雪主导着洪水风险和水资源供给。Bouchard等人在加拿大业务化预报框架内直接解决了这一问题。与默认冻土方案相比，其修订的SVS配置在Kling-Gupta效率（KGE）上提升了0.28，同时将严重性能退化站点的比例从大湖区–圣劳伦斯流域580个评估站中的三分之一骤降至不足1%。关键在于，该改进方案在数值天气预报应用中同样表现可接受，为业务化实施奠定了可行基础。

### Enhancing runoff-infiltration partitioning in the SVS land surface model improves streamflow simulations under frozen soil conditions

**作者**: B. Bouchard, Vincent Vionnet, É. Gaborit, Vincent Fortin

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4823-2026](https://doi.org/10.5194/hess-30-4823-2026) · **引用数**: 0

**匹配主题**: land surface model, streamflow, runoff
{: .label .label-green }

> 土壤冻结是影响北方流域水文响应的重要寒区过程，尤其在冬季降雨和融雪事件期间。在陆面模式中，冻土入渗难以准确表征，因为土壤结构和水文土壤学过程的变化尺度细于模型网格。在业务化建模中，物理过程集成必须在性能提升与计算效率和复杂性之间取得平衡。本研究提出SVS（土壤-植被-积雪）模式的新配置方案（Fr-Inf），通过减少地表径流和次表层侧流来增强冻土入渗能力，该模型被用于加拿大环境与气候变化部（ECCC）的业务预报系统。研究在大湖区–圣劳伦斯流域580余个水文站对该方案进行了五年期评估。与默认冻土配置（Fr）相比，Fr-Inf显著提升了KGE（ΔKGE = 0.28），但略逊于不含冻土的SVS配置（noFr；ΔKGE = −0.07）。在Fr-Inf方案下，相对于无冻土配置出现严重退化（ΔKGE < −0.5）的站点仅为4个（<1%），而默认Fr方案则高达172个站（33%），充分体现了新方案的稳健性。研究还评估了该方案对土壤冻结深度及近地面温度和露点温度预报的影响，结果表明其在业务化数值天气预报中同样可接受，支持ECCC将冻土方案纳入业务化数值天气与流量预报系统。

---

## 地球系统模式实验协议开发

随着气候模拟界推进CMIP7，如何设计实验以直接比较不同模式在潜在地球系统临界点附近的行为——同时排除各模式升温速率差异的干扰——是一大挑战。Jones等人提出TIPMIP（临界点模式比较计划），通过要求所有参与ESM以CO₂排放模式运行（大气CO₂为预测量），并统一设定每世纪2°C的升温速率来应对这一挑战。之后在2°C和4°C全球升温水平上分支为零排放和负排放情景。对于水文和水资源研究者而言，TIPMIP的设计具有特殊价值：通过控制升温轨迹，该实验将支持对水循环中潜在临界点（包括季风系统突变、多年冻土水文、冰盖对海平面的贡献及长期淡水可用性变化）的多模式集成分析，而这些在非协调的单模式实验中难以清晰诊断。

### The TIPMIP Earth system model experiment protocol: phase 1

**作者**: Colin G. Jones, Isaline Bossert, Donovan P. Dennis, Hazel A. Jeffery, Chris D. Jones, T. Koenigk 等

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-6941-2026](https://doi.org/10.5194/gmd-19-6941-2026) · **引用数**: 5

**匹配主题**: earth system model, climate change
{: .label .label-green }

> 本文介绍了国际临界点模式比较计划（TIPMIP）第一阶段的新型地球系统模式（ESM）实验协议，并建议将其作为耦合模式比较计划7（CMIP7）的协议。该协议要求ESM以CO₂排放模式运行，大气CO₂为预测变量。强迫仅由恒定CO₂排放量构成，基于各模式的累积碳排放瞬态气候响应（TCRE）值设定，使全球平均地表升温速率保持每世纪2°C。正排放（升温）实验从给定模式的前工业状态启动。当升温运行首次超过相对于前工业全球平均地表气温（GMSAT）的指定升温水平（2°C和4°C）时，CO₂排放设为零，正排放运行分支为零排放运行，持续300年。在各零排放运行开始50年后，CO₂排放设为负值（与正排放速率相同），模式持续运行直至GMSAT冷却至低于原始前工业值。利用该协议，可在参与模式间控制全球升温速率及潜在的冷却速率。TIPMIP实验将支持一系列分析，包括：在不同全球升温水平下净零CO₂排放时地球系统的突变/快速变化评估、净零CO₂排放时地球系统的长期响应、净负CO₂排放的响应及负排放驱动冷却的有效性，以及在正排放（升温）、零排放和负排放（冷却）路径下地球系统变化的可逆性。

---

## 统计信息

| 指标 | 数量 |
|:-----|-----:|
| 搜索数据库 | 2（仅S2——OpenAlex返回429错误） |
| 搜索主题数 | 16 |
| 抓取论文总数 | 14 |
| 去重后 | 13 |
| LLM相关性筛选后 | 4 |
| 注册表去重后（已在前期每周综述中收录） | 2 |
| 被排除（不相关） | 9 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|-------:|
| Hydrology and Earth System Sciences | 1 |
| Geoscientific Model Development | 1 |

## 筛选标准

**搜索主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

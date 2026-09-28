---
layout: default
title: "第38周（9月14日 - 9月21日），2篇"
nav_order: 34
nav_exclude: true
lang: zh
lang_link: /2026/september/2026-09-21-weekly-review
date: 2026-09-21
categories: [weekly-zh, 2026, september]
tags: [hydrology, literature-review, research]
paper_count: 2
highlight: "TerM陆面模式预测SSP5-8.5情景下林波波河峰值流量将增加50%以上；ORCHIDEE新增北极灌木植被功能型后，模拟高纬度生物量估算下降13.5%。"
---

# 每周文献综述
{: .no_toc }

**第38周** · 2026年9月14日–9月21日
{: .text-grey-dk-000 }

在 **2** 个主题中发现 **2** 篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

本周的检索窗口相当平静——OpenAlex因服务错误未能返回任何结果，仅有2篇独立论文在去重和期刊过滤后保留。两篇论文均聚焦于陆面模式的开发与应用：Mohomi等人利用TerM陆面模式预测，在高排放情景下，南非林波波河流域的夏季峰值流量到2100年将超历史水平50%以上，预示洪旱循环将趋于极端。Kirchner等人则证明，在ORCHIDEE中加入显式灌木植被功能型后，北极-亚北极地区的碳平衡模拟显著改善，模拟地上生物量估算下降13.5%，与观测数据更为吻合。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 气候变化对水文的影响

区域水文预测对于气候适应规划至关重要。Mohomi等人将TerM（INM RAS-MSU地表模式）应用于林波波河流域，基于CMIP6 ISIMIP强迫数据在SSP1-2.6和SSP5-8.5情景下开展预测，结果揭示了显著的水文极端化趋势：尽管年均径流趋势统计上不显著，但年内季节性极端明显加剧——高排放情景下1–2月洪峰流量预计超历史水平50%以上，而春季（9–11月）则明显偏干。这种时间变异性增强（而非单调变化）的规律，凸显了在受ENSO和热带气旋影响的半干旱流域中，洪水与干旱风险须同步评估的必要性。

### Projections of hydrological changes and riverflow extremes using TerM land surface model in the Limpopo River Basin, South Africa

**作者**: Tumelo Mohomi, V. Stepanenko, A. Medvedev, I. Dhau, M. Bopape, H. Chikoore

**期刊**: *Theoretical and Applied Climatology* · **DOI**: [10.1007/s00704-026-06579-z](https://doi.org/10.1007/s00704-026-06579-z) · **引用数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 南非日益频繁的水文气候极端事件亟需深入理解气候驱动变化对区域水平衡的影响。本研究评估了气候变化对历史上易遭受洪涝和持续干旱的林波波河流域水文极端事件的影响。研究采用INM RAS-MSU地表模式（TerM）对2020至2100年的河流流量进行预测，大气强迫数据来自CMIP6 ISIMIP数据库的SSP1-2.6和SSP5-8.5情景。以1979–2014年为基准期，分析了近期（2020–2055年）和远期（2065–2100年）预测，高流量事件（洪水）以第95百分位数计算。年内径流模式与历史趋势一致，但在高排放（SSP5-8.5）情景下，峰值流量预计增加超过50%。峰值流量增加可能发生在南半球夏季（1–2月），而春季（9–11月）则预计明显下降。气候变化预计将加剧南非东北部的水文气候极端事件，该地区南半球夏季降雨变率受热带气旋、厄尔尼诺-南方涛动（ENSO）和对流降雨的强烈影响。研究结论为加强气候适应政策提供了证据基础。

---

## 陆面模式发展

改进陆面模式中植被多样性的表征对于减少地球系统预测中碳和能量循环模拟偏差至关重要。Kirchner等人针对ORCHIDEE（IPSL地球系统模式的陆面分量）中高纬度植被仅以北方树木和草地表示的不足，实施了三种灌木植被功能型（高大落叶灌木、矮小落叶灌木和常绿矮灌木），并利用泛北极观测数据进行参数约束。结果使北极-亚北极地上总生物量估算从54降至46.7 Pg C，与基准数据集的吻合度明显提升。该方法在现有木本植被框架上的最小改动和良好可移植性，为其他存在类似不足的陆面模式提供了有益参考。

### Introducing shrubs enhances the representation of high-latitude vegetation and carbon cycling in the ORCHIDEE land surface model

**作者**: A. Kirchner, Efrén López-Blanco, V. Bastrikov, S. Luyssaert, P. Peylin, A. Lansø

**期刊**: *Biogeosciences* · **DOI**: [10.5194/bg-23-6521-2026](https://doi.org/10.5194/bg-23-6521-2026) · **引用数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 北极-亚北极陆地生态系统在高纬度增温放大的背景下正在迅速变化，灌木扩张趋势明显，对区域碳和能量收支产生显著影响。然而，许多全球陆面模式对高纬度植被多样性及植被-气候相互作用的表征仍显不足。在ORCHIDEE（IPSL地球系统模式的陆面分量）中，高纬度植被主要以北方树木或草地表示，缺乏显式灌木。本研究在ORCHIDEE（修订版9269）中引入三种高纬度灌木植被功能型（高大落叶灌木、矮小落叶灌木和常绿矮灌木）。实施方案在现有木本植被框架基础上，重新标定了控制异速生长、碳分配、更新、死亡率和物候的参数集，利用泛北极综合观测数据约束参数值。模拟结果显示，引入灌木后北极-亚北极地区模拟总地上生物量从54降至46.7 Pg C（−13.5%），年均总初级生产力从498降至481 gCm⁻²yr⁻¹（−3.4%），与基准数据集的吻合度显著提升。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 获取论文总数 | 4 |
| 去重后 | 4 |
| 期刊过滤后 | 2 |
| LLM相关性筛选后 | 2 |
| 拒绝（不相关） | 0 |

**注**：本周OpenAlex对全部16个主题均返回HTTP 503错误，所有结果均来自Semantic Scholar。

### 按期刊统计

| 期刊 | 论文数 |
|:-----|------:|
| Theoretical and Applied Climatology | 1 |
| Biogeosciences | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

---
layout: default
title: "第23周（6月1日 - 6月8日），7篇"
nav_order: 35
nav_exclude: true
lang: zh
lang_link: /2026/june/2026-06-15-weekly-review
date: 2026-06-15
categories: [weekly-zh, 2026, june]
tags: [hydrology, literature-review, research]
paper_count: 7
highlight: "Noah-MP因雪压实和反照率物理过程不足，在美国西部系统性低估雪水当量，直接影响融雪主导流域的季节性供水预测。"
---

# 每周文献综述
{: .no_toc }

**第23周** · 2026年6月1日–6月8日
{: .text-grey-dk-000 }

在 **3** 个主题下共找到 **7** 篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

本周综述涵盖陆面模式参数化与偏差、气候和城镇化对径流的影响，以及工程设施和非正规居住区水管理挑战三大方向。三篇发表于《Water Resources Research》的论文共同推进了对陆面模式结构局限性的认识——从Noah-MP雪水当量偏差到地下水参数化敏感性，再到洪水模型中长期忽视的非正规居住区水文过程。与此同时，新的计算方法也在水电水库优化和降雨-径流模拟领域取得进展。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 陆面模式参数化与偏差

本周三项研究深入探讨了陆面模式和地球系统模式在结构与参数方面的局限性。Abolafia‐Rosenzweig等人系统评估了广泛使用的Noah-MP陆面模式在美国西部的雪水当量偏差，将持续性低估归因于雪压实和反照率表示不足——这一发现直接影响融雪主导流域的季节性供水预测。Mbarak与Yang则解析了空间分辨率选择、地下水参数化深度和包气带厚度如何共同影响模拟的土壤湿度和温度偏差，证明粗分辨率配置会系统性地放大中纬度大陆地区已记录的暖干偏差。Cheng等人将这一研究延伸至城市环境，在JAMES中证明采用空间连续的精细城市地表属性数据集能显著减少城市热、降水和地表能量通量的模拟误差——揭示输入数据质量与模式物理过程同等重要。

### Revisiting Snow Water Equivalent Bias in the Noah‐MP Land Surface Model in the Western U.S.

**作者**: R. Abolafia‐Rosenzweig, Cenlin He, Kyoko Ikeda, Changhai Liu, Tzu‐Shun Lin, Michael Barlage, Lulin Xue, K. Rasouli, Yongxin Zhang, A. Newman et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042586](https://doi.org/10.1029/2025wr042586) · **引用次数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 陆面模式（LSM）被广泛用于生成支持水资源研究与管理的积雪记录、预报和预测。LSM中复杂的不确定性来源促使研究者开展评估，以更好地理解偏差特征并识别指导模式发展和用户解读的根本原因。本研究重新审视Noah-MP陆面模式在美国西部的雪水当量偏差，检验了雪压实、反照率及其他关键过程对融雪主导流域系统性低估的贡献。

---

### Impacts of Spatial Resolution, Groundwater Parameterizations, and Vadose Zone Thickness on Land Surface Simulations

**作者**: Mahmoud Mbarak, Zong‐liang Yang

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr040135](https://doi.org/10.1029/2025wr040135) · **引用次数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 公里尺度的陆地过程精确模拟对改进天气和气候预报至关重要。然而，中纬度地区有据可查的暖温干燥偏差等持续性偏差仍构成挑战。本研究探讨了地下水参数化、包气带厚度和空间分辨率对陆面模拟的影响，为减少土壤湿度和地表能量收支系统误差的模式配置选择提供指导。

---

### Importance of Spatially Continuous Urban Surface Properties in Urban‐Resolving Earth System Modeling

**作者**: Yifan Cheng, Lei Zhao, K. Oleson, T. Chakraborty, Keer Zhang, Cenlin He, Joyce Yang

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025ms005573](https://doi.org/10.1029/2025ms005573) · **引用次数**: 0

**匹配主题**: earth system model
{: .label .label-green }

> 在全球模拟系统中以更高分辨率准确表征城市属性和过程，对于提升捕捉城市系统复杂性、支撑有效韧性策略的能力至关重要。然而，粗分辨率全球城市属性的使用会在城市热效应、降水和地表能量通量模拟中引入显著误差。本研究证明，采用空间连续的精细城市地表属性数据集能显著减少城市解析地球系统模拟中的这些偏差。

---

## 径流模拟与流域对土地利用变化的响应

两项研究考察了降雨-径流动力学的刻画方式及其在土地利用和气候变化下的演变。Sepahvand等人将遗传规划与HEC-HMS概念模型在降雨-径流模拟中进行对比，发现遗传规划在精度上可与HEC-HMS媲美甚至超越，同时提供透明可解释的方程——介于黑盒机器学习与人工率定物理模型之间的实用中间道路。Ariano与Murfitt通过长序列水文站记录分析，解析了气候变化和城镇化并发下的数十年径流趋势，结果表明城市扩张对洪峰流量的放大效应超出了单一气候模型或单一土地利用模型的预测范围，对流域综合管理规划具有直接启示。

### Comparison of Genetic Programming and HEC-HMS as a Conceptual Model in Simulating Rainfall-Runoff Time Series

**作者**: R. Sepahvand, Mehrdad Khoshoei, M. Golmohammadi

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-55529-2](https://doi.org/10.1038/s41598-026-55529-2) · **引用次数**: 1

**匹配主题**: runoff
{: .label .label-green }

> 摘要暂不可用。本研究比较了遗传规划与HEC-HMS概念模型在降雨-径流时间序列模拟中的表现，评估数据驱动方法与物理模型在流域尺度径流预测中的精度与可解释性。

---

### Characterizing the Role of Climate and Urbanization on Multi-Decade Stream Hydrology: Implications for Watershed Management

**作者**: S. Ariano, Justin Murfitt

**期刊**: *Environmental Management* · **DOI**: [10.1007/s00267-026-02522-0](https://doi.org/10.1007/s00267-026-02522-0) · **引用次数**: 0

**匹配主题**: hydrology
{: .label .label-green }

> 摘要暂不可用。本研究刻画气候变率与城市土地利用变化在驱动数十年径流趋势中的相对作用，通过长序列水文站分析解耦这两种并发驱动因素，并评估其对流域综合管理策略的影响。

---

## 水资源管理与城市水文盲区

本主题突出了工程调度优化与城市水文科学缺口两个方向的进展。Liu等人提出一种信息驱动的早停优化准则，作为无代理模型的水电水库多目标不确定性运行优化方法，以更少的模型评估次数获得具有竞争力的帕累托前沿——对于全仿真计算代价高昂的系统具有实用价值。另一方面，Getirana在《Water Resources Research》中的视角论文有力论证了非正规居住区水文过程——全球逾十亿人的家园——在洪水模拟和排水评估中仍是重大盲区；这些社区独特的不透水格局、排水路径和用水行为被系统性地排除在城市水文模型之外，为全球最脆弱群体的洪水风险和水资源配置带来误差。

### Information-Driven Early Stopping Optimization: A Surrogate Model-Free Method for Expensive Multi-Objective Uncertainty Operation Optimization of Hydropower Reservoirs

**作者**: Dong Liu, Tao Bai, Xiaoting Wei

**期刊**: *Expert Systems with Applications* · **DOI**: [10.1016/j.eswa.2026.131422](https://doi.org/10.1016/j.eswa.2026.131422) · **引用次数**: 1

**匹配主题**: hydropower
{: .label .label-green }

> 摘要暂不可用。本研究提出一种信息驱动的早停优化框架，作为无代理模型方法用于计算代价高昂的水电水库多目标不确定性运行优化，减少逼近帕累托最优前沿所需的仿真调用次数。

---

### Urban Waters, Unseen: The Hydrology of Informal Settlements Must Not Be Ignored

**作者**: Augusto Getirana

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042912](https://doi.org/10.1029/2025wr042912) · **引用次数**: 0

**匹配主题**: hydrology
{: .label .label-green }

> 非正规居住区——全球逾十亿人的家园——在城市水文科学中几乎隐而不见。尽管这些社区人口密集、结构复杂、水文路径独特，却被常规排除于洪水模型、排水评估和水资源规划之外。本视角文章呼吁将非正规居住区水文过程系统性地纳入城市水科学、洪水风险评估和水资源管理框架。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题数 | 20 |
| 获取论文总数 | 12 |
| 去重后 | 12 |
| LLM相关性筛选后 | 7 |
| 已拒绝（不相关） | 5 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|-------:|
| Water Resources Research | 3 |
| Journal of Advances in Modeling Earth Systems | 1 |
| Scientific Reports | 1 |
| Environmental Management | 1 |
| Expert Systems with Applications | 1 |

## 筛选标准

**主题关键词**: hydrology, streamflow, runoff, river routing, flood, drought, reservoir operations, water management, land surface model, earth system model, climate change hydrology, remote sensing hydrology, machine learning hydrology, groundwater, irrigation, hydropower, surface water, watershed

**数据库**: Semantic Scholar, OpenAlex

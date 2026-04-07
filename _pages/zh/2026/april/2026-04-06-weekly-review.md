---
layout: default
title: "第13周（3月23日 - 3月30日），12篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/april/2026-04-06-weekly-review
date: 2026-04-06
categories: [weekly-zh, 2026, april]
tags: [hydrology, literature-review, research]
paper_count: 12
highlight: "干旱胁迫下水-能耦合管理与机器学习径流预报成为本周焦点。"
---

# 每周文献综述
{: .no_toc }

**第13周** · 2026年3月23日–30日
{: .text-grey-dk-000 }

在**5**个主题中发现**12**篇相关论文
{: .fs-5 .fw-300 }

## 摘要概述

本周文献凸显了学界对干旱胁迫下水-能耦合系统日益增长的关注，相关研究提出了协调电力网络与流域系统的新方法。气候变化对灌溉、河川径流及森林水文的影响仍是核心议题，与此同时，用于径流预测的机器学习方法和用于水库监测的遥感技术持续推动该领域走向更加数据驱动的业务化工具。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 水库与水-能耦合系统

干旱等极端事件下的水-能耦合管理成为本周的关键焦点。Guo等人提出了一种分层应急调度策略，可在干旱期间协调电力与流域网络中的灵活性资源，并在一个真实的143节点配电网上验证表明，该方法可显著降低电力短缺与水资源削减。与此同时，Liu等人量化了黄土高原水库开发中常被忽视的蒸发损失，发现中小型水库的扩张已导致总蒸发量大幅增加，尽管单纯气候效应下的蒸发率略有下降。

### Hierarchical Aggregation-Embedded Emergency Scheduling of Coupled Electricity-Watershed Networks With Heterogeneous Flexibility Resources Under Extreme Drought Events

**作者**: Siyuan Guo, Bin Zhou, C. Chung, Siqi Bu, Zhihao Hua, Jun Liu

**期刊**: *IEEE Transactions on Sustainable Energy* · **DOI**: [10.1109/TSTE.2025.3635922](https://doi.org/10.1109/TSTE.2025.3635922) · **引用数**: 6

**匹配主题**: 干旱
{: .label .label-green }

> 提出了一种动态聚合嵌入式应急调度策略，用于协调电力与流域网络中的大规模异构灵活性资源，以缓解干旱事件下的电力短缺。研究构建了水-电耦合网络的热力学模型，刻画了高温气候下电力短缺与水量削减的风险相互依赖关系。所采用的超立方体多方向内逼近投影方法可评估随水量变化的可调度发电区间。该策略已在一个143节点配电网与14节点流域系统耦合的实际系统上得到充分验证。

---

### Increased Surface Water Evaporation Loss Induced by Reservoir Development on the Loess Plateau

**作者**: Yao Liu, Xianhong Xie, Yibing Wang, Arken Tursun, Dawei Peng, Xinran Wu et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-67-2026](https://doi.org/10.5194/hess-30-67-2026) · **引用数**: 1

**匹配主题**: 水库、地表水
{: .label .label-green }

> 全球范围内的水库建设显著增强了当地的生产生活供水能力，但这些水体的蒸发损失仍未得到充分认识。利用改进的Penman模型与黄土高原长期遥感水体数据(2000–2018)，作者发现总蒸发量达到4.16 × 10⁶ m³ d⁻¹并呈上升趋势。中小型水库与淤地坝的发展是蒸发损失增加的主要驱动因素，其量级与该地区的地表水取用量相当。

---

## 气候变化对水资源的影响

气候适应及其水文后果本周引起了广泛关注。Taylor提供了令人信服的全球证据，表明农民通过扩大地下水灌溉来应对气候变暖，观测到的升温可解释全球灌溉增长的9%——但代价是含水层压力与土壤盐渍化。在山区流域，Casirati等人利用SWAT+模型表明，加州Kings River流域的大规模森林恢复可抵消最多48%的气候变暖驱动的径流减少；Gorsevski则将TOPMODEL与CLIGEN相结合，预测了数据稀缺的地中海流域径流对气候变化的敏感性。Calvo-Sancho等人发表在Nature Communications上的关于Valencia暴洪的研究及时提醒人们，气候变化正在放大极端降水事件，并造成毁灭性后果。

### Irrigation and Climate Change: Long-run Adaptation and its Externalities

**作者**: Charles A. Taylor

**期刊**: *Journal of the Association of Environmental and Resource Economists* · **DOI**: [10.1086/741141](https://doi.org/10.1086/741141) · **引用数**: 5

**匹配主题**: 气候变化、灌溉
{: .label .label-green }

> 灌溉农业作为全球最大的用水部门，占全球耕地的20%和粮食产量的40%。本文发现，农民通过在变得更干、更热的地区增加地下水灌溉来适应气候变化。观测到的近期升温可解释全球灌溉增长的9%。GRACE卫星数据显示，气候驱动的灌溉加剧了含水层压力与土壤盐渍化，构成了气候适应的重大负外部性，并对未来粮食安全构成潜在威胁。

---

### Hydrological Response to Compounding Impacts of Climate Change and Forest Management in the Upper Kings River Basin, CA, USA

**作者**: Stefano Casirati, Martha Conklin, M. Safeeq

**期刊**: *Ecohydrology* · **DOI**: [10.1002/eco.70157](https://doi.org/10.1002/eco.70157) · **引用数**: 1

**匹配主题**: 河流、气候变化
{: .label .label-green }

> 利用SWAT+模型，作者研究了在升温情景下森林处理对Kings River上游流域蒸散发与径流的单独及叠加影响。大规模森林恢复在+1.5 °C和+3.0 °C升温情景下分别有可能将径流的升温影响最多减轻48%和36%。处理后的第一年效益最为显著，并可持续长达10年。

---

### Predicted Streamflow Sensitivity to Climate Change Using TOPMODEL with CLIGEN Weather Generator in a Data-Sparse Medium-Sized Mediterranean Watershed

**作者**: P. Gorsevski

**期刊**: *Water Resources Management* · **DOI**: [10.1007/s11269-026-04540-3](https://doi.org/10.1007/s11269-026-04540-3) · **引用数**: 1

**匹配主题**: 水流量、气候变化
{: .label .label-green }

> 摘要暂缺。

---

### Human-Induced Climate Change Amplification on Storm Dynamics in Valencia's 2024 Catastrophic Flash Flood

**作者**: C. Calvo-Sancho, J. Díaz-Fernández, J. J. González-Alemán, A. Halifa-Marín, M. Miglietta, C. Azorin-Molina et al.

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-026-68929-9](https://doi.org/10.1038/s41467-026-68929-9) · **引用数**: 3

**匹配主题**: 气候变化
{: .label .label-green }

> 摘要暂缺。

---

## 洪水研究与复合事件

洪水危险评估方法与旱涝复合事件备受关注。Angkanasirikul等人分析了越南北部45年间70次热带气旋事件，建立了一套系统化的洪水易发性制图方法，将热带气旋特征与流域水文驱动因素相联系。Li等人研究了西南中国近六十年间旱涝急转事件的时空变化，强调了此类复合极端事件出现频率的不断增加。

### Key Factors Influencing Flood Severity and Mapping of Flood Susceptibility in Northern Vietnam and Its Red River Delta From Landfalling Tropical Cyclones

**作者**: Warinthorn Angkanasirikul, Wei Jian, Edmond Yatman Lo

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70372](https://doi.org/10.1002/hyp.70372) · **引用数**: 1

**匹配主题**: 河流、洪水
{: .label .label-green }

> 利用1979至2023年间70次热带气旋事件的数据，作者研究了越南北部的热带气旋特征、流域属性与观测到的洪水响应之间的相互作用。严重程度指标与热带气旋属性(尤其是日均降水量)及流域固有特征(高程、径流系数、前期土壤含水量)相关。通过层次分析法结合模糊综合评价法生成洪水易发性图，并以历史洪水范围数据为基准进行了对比验证。

---

### Spatiotemporal Variability of Drought-Flood Abrupt Alternation Events in Southwest China During 1961 to 2024

**作者**: Xiehui Li, Shang-zhong Li, Lei Wang, Xuejia Wang, Jian Huang

**期刊**: *Theoretical and Applied Climatology* · **DOI**: [10.1007/s00704-026-06024-1](https://doi.org/10.1007/s00704-026-06024-1) · **引用数**: 2

**匹配主题**: 洪水、干旱
{: .label .label-green }

> 摘要暂缺。

---

## 机器学习径流预测

两项独立研究推进了用于日尺度径流预报的机器学习架构。Yang等人开发了一种两阶段LSTM方法，将新安江概念模型与集合经验模态分解相结合，将基于过程的理解与深度学习相融合。Xu等人提出了一种创新架构，将黑翼鸢优化算法与Mamba2-Transformer模型耦合用于日径流预测，探索了超越标准LSTM的更新颖的注意力架构。

### Development of a Two-Stage LSTM for Multi-Step Runoff Forecasting Using a XAJ Model and EEMD

**作者**: Zihao Yang, Q. Dong, Xu Zhang, Hongyu Zhu, Zhetao Cheng

**期刊**: *Water Resources Management* · **DOI**: [10.1007/s11269-025-04420-2](https://doi.org/10.1007/s11269-025-04420-2) · **引用数**: 3

**匹配主题**: 径流
{: .label .label-green }

> 摘要暂缺。

---

### Innovative Daily Runoff Prediction Model Integrating Black-Winged Kite Algorithm and Mamba2-Transformer Architecture

**作者**: Dong Xu, Xiao-xue Hu, Wen-chuan Wang, Jun Wang, Can-can Shi, Hong-fei Zang

**期刊**: *Ecological Informatics* · **DOI**: [10.1016/j.ecoinf.2025.103565](https://doi.org/10.1016/j.ecoinf.2025.103565) · **引用数**: 3

**匹配主题**: 径流
{: .label .label-green }

> 摘要暂缺。

---

## 河川径流建模与监测

Zipper等人通过将河道断流纳入解析径流耗减函数，针对地下水抽取对河川径流影响的估算这一实际问题进行了研究。其方法揭示，夏季河道断流会导致显著的径流耗减滞后至秋冬季河网重新湿润时期出现——这是季节性水资源管理的一个关键见解。Patel等人对遥感与GIS在流域水文中的应用进展进行了系统综述，梳理了该领域数据驱动工具的演变。

### Lagged Streamflow Depletion Due to Pumping-Induced Stream Drying: Incorporation Into Analytical Streamflow Depletion Estimation Methods

**作者**: S. Zipper, Ian Gambill, Monty Schmitt, Claire Kouba, Leland Scantlebury, Thomas Harter et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.134909](https://doi.org/10.1016/j.jhydrol.2026.134909) · **引用数**: 1

**匹配主题**: 水文模型、水流量
{: .label .label-green }

> 水资源管理常需考虑地下水抽取所导致的径流减少。作者提出了一种将河道断流纳入解析耗减函数(ADF)的方法。以加州Scott Valley为例，纳入断流的ADF与观测径流及基于过程的数值模型结果高度吻合。关键的是，纳入断流的ADF能够模拟出径流耗减的时间滞后现象——当夏季河道断流导致河网断开后，相当一部分耗减会被推迟到秋冬季节河网重新湿润时才出现。

---

### Advances in Remote Sensing and GIS Applications in Watershed Hydrology: A Systematic Review

**作者**: R. K. Patel, Prasoon Soni, Pushpraj Singh

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134459](https://doi.org/10.1016/j.jhydrol.2025.134459) · **引用数**: 2

**匹配主题**: 水文学
{: .label .label-green }

> 摘要暂缺。

---

## 统计数据

| 指标 | 数量 |
|:-------|------:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 去重前论文总数 | 2,288 |
| 去重后唯一论文数 | 1,971 |
| LLM相关性筛选后 | 12 |
| 被排除（不相关） | 1,959 |

### 各期刊论文数

| 期刊 | 论文数 |
|:--------|-------:|
| Hydrology and Earth System Sciences | 1 |
| Journal of Hydrology | 3 |
| IEEE Transactions on Sustainable Energy | 1 |
| Journal of the Association of Environmental and Resource Economists | 1 |
| Nature Communications | 1 |
| Ecohydrology | 1 |
| Water Resources Management | 2 |
| Hydrological Processes | 1 |
| Theoretical and Applied Climatology | 1 |
| Ecological Informatics | 1 |

## 筛选标准

**主题**: 水文学、水文模型、河流、径流、水流量、水库、水资源管理、洪水、干旱、季节性、陆面模型、气候变化、水力发电、地表水、灌溉、地球系统模型

**数据库**: Semantic Scholar, OpenAlex

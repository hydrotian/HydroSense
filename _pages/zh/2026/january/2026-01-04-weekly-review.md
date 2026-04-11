---
layout: default
title: "第01周（12月29日 - 1月4日），12篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/january/2026-01-04-weekly-review
date: 2026-01-04
categories: [weekly-zh, 2026, january]
tags: [hydrology, literature-review, research]
paper_count: 12
highlight: "一项基于152,000余篇论文的文献计量综述勾勒出百年干旱研究脉络,与此同时深度学习正成为径流与水库建模的一等工具。"
---

# 每周文献综述
{: .no_toc }

**第01周** · 2025年12月29日 – 2026年1月4日
{: .text-grey-dk-000 }

发现 **12** 篇相关论文,归为 **4** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

2026年第一个ISO周——跨越新年——呈现出一批罕见地聚焦于干旱科学、深度学习径流模拟以及寒区与水塔水文的论文。《水资源研究》上一篇基于152,000余篇论文的百年尺度文献计量综述梳理干旱研究的发展脉络,而两篇《Earth's Future》分别揭示了基流干旱的气候与地下驱动因子以及破纪录复合干旱-热浪事件的动力学。方法学上最突出的是一篇WRR论文,采用水文专用的可解释AI框架打开LSTM黑箱,检验深度径流模型的内部推理是否在物理上可靠——这是ML-水文深度融合下一阶段的核心议题。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 干旱科学:百年、复合与基流

三篇论文从互补的视角重塑我们对干旱的认识。Sabut与Mishra采用文献计量方法分析1900–2023年间超过152,000篇干旱研究论文,勾勒出从统计建模、卫星遥感到机器学习的方法学演进,以及人为影响归因这一新兴前沿。Ghaneei等人转向一个较少被研究但至关重要的组分——基流——使用DeepBase数据集和可解释机器学习揭示美国西部四十年间基流干旱持续加剧,主要受大气水量平衡异常和土壤属性驱动,而东部整体呈下降趋势。Li等人聚焦干旱最危险的尾部——破纪录复合干旱-热浪事件,其九成员集合预测在SSP5-8.5情景下此类事件的年发生概率将于2015–2040年间翻倍,北美南部、南美北部和欧洲南部受影响最严重。

### A Century of Drought Research (1900–2023): Scientific Developments, Methodological Innovations, and Emerging Frontiers

**作者**: A. Sabut, A. Mishra

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025WR041987](https://doi.org/10.1029/2025WR041987) · **引用数**: 4

**匹配主题**: hydrologic model, drought, land surface model
{: .label .label-green }

> 通过对超过152,000篇同行评审论文的文献计量分析,综合1900–2023年间的干旱研究进展。从古代气候重建、统计与概率建模,到机器学习与深度学习、卫星遥感、水文与陆面建模,再到人为影响归因等新兴前沿,梳理学科发展的整体脉络和方法学里程碑。

---

### Four Decades of Baseflow Drought Analysis Reveals Varying Contributions of Climatic Drivers and Physical Controls

**作者**: P. Ghaneei, E. Foroumandi, K. Stahl, H. Ajami, N. Wanders, H. Moradkhani

**期刊**: *Earth's Future* · **DOI**: [10.1029/2025EF006934](https://doi.org/10.1029/2025EF006934) · **引用数**: 2

**匹配主题**: hydrology, hydrologic model, streamflow, drought, earth system model
{: .label .label-green }

> 使用长期DeepBase基流数据集与可解释机器学习方法,量化美国本土四十年间基流干旱(BFD)特征的演变。西部(尤其是西南地区)BFD发生频率和持续时间显著增加,东部多数地区呈下降趋势。BFD频率主要由大气水量平衡异常和土壤属性控制,而持续时间主要由水文地质特性决定——这表明地下控制因子在干旱归因中不可忽视。

---

### Understanding the Dynamics of Record-Shattering Compound Drought-Heatwave Events and Their Impacts on Ecosystems

**作者**: B. Li, K. Y. Liu, M. Wang, Y. Yang, M. He, Y. Wang 等

**期刊**: *Earth's Future* · **DOI**: [10.1029/2024EF005714](https://doi.org/10.1029/2024EF005714) · **引用数**: 2

**匹配主题**: drought, land surface model, earth system model
{: .label .label-green }

> 采用九成员集合在三种未来情景下预测破纪录复合干旱-热浪(CDHW)事件——即超出历史严重度两个标准差以上的事件——在SSP5-8.5情景下年发生概率将于2015–2040年间翻倍。识别北美南部、南美北部和欧洲南部为最脆弱区域,破纪录CDHW事件相较常规事件水汽输送更弱、对流活动更低、对生态系统冲击更大。

---

## 可解释深度学习:降雨径流与水库调度

三篇深度学习论文将讨论从预测精度推进到可解释性与运行集成。Bayati等人构建了一个水文专用的可解释AI框架,从训练好的LSTM中提取非线性、随时滞变化、随时间变化的脉冲响应函数,揭示模型如何内化降水、温度与潜在蒸散发对径流的影响,并首次提供一种结构化方法来检验其推理是否物理上可靠。Yang等人将新安江(XAJ)概念模型与两阶段LSTM以及EEMD信号分解结合,用于多步径流预报,将物理先验与数据驱动灵活性相融合。Zhu等人把深度学习与改进的多目标优化算法整合,用于级联水库调度,明确纳入生态溶解氧约束——这是ML在水文中从"预测"迈向"决策支持"的一个运营化应用。

### Evaluating the Functional Realism of Deep Learning Rainfall-Runoff Models Using Catchment Hydrology Principles

**作者**: A. Bayati, A. Ameli, S. Razavi

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025WR040076](https://doi.org/10.1029/2025WR040076) · **引用数**: 5

**匹配主题**: hydrology, hydrologic model, runoff, streamflow, land surface model
{: .label .label-green }

> 提出水文专用的可解释AI(XAI)框架,从训练好的LSTM中提取非线性、随时滞变化、随时间变化的脉冲响应函数,量化降水、温度与潜在蒸散发对模拟径流的独立影响。该框架首次提供一种结构化方法来检验深度降雨径流模型的内部推理是否与可辩护的流域水文机制一致——这是将机器学习负责任地集成到运行水文中的基石。

---

### Development of a Two-Stage LSTM for Multi-Step Runoff Forecasting Using a XAJ Model and EEMD

**作者**: Z. Yang, Q. Dong, X. Zhang, H. Zhu, Z. Cheng

**期刊**: *Water Resources Management* · **DOI**: [10.1007/s11269-025-04420-2](https://doi.org/10.1007/s11269-025-04420-2) · **引用数**: 4

**匹配主题**: hydrologic model, runoff, water management
{: .label .label-green }

> 将新安江(XAJ)概念水文模型、两阶段LSTM架构和集合经验模态分解(EEMD)结合,用于多步径流预报。混合方法融合XAJ的物理先验与LSTM的数据驱动灵活性,以提升多时段径流预报精度。

---

### Integration of deep learning and improved multi-objective algorithm to optimize cascade reservoirs operation with consideration of ecological dissolved oxygen needs

**作者**: Z. Zhu, H. Li, Z. Wang, X. Zhang, Z. Tan

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134899](https://doi.org/10.1016/j.jhydrol.2025.134899) · **引用数**: 2

**匹配主题**: hydrology, reservoir, hydropower
{: .label .label-green }

> 将深度学习与改进的多目标优化算法整合,用于级联水库调度,并在水电和防洪目标之外显式纳入生态溶解氧需求。将ML在水文中的应用从预测推进到多目标水资源运行决策支持。

---

## 水塔、径流驱动因子与土壤水–径流耦合

三篇论文深化了径流生成及其驱动因子的量化研究。Yue等人基于100个树轮采样点的树轮年代学网络,将中国中部水塔(CCWT)径流重构回溯至1595 CE,并与六个太平洋沿岸水塔区域的记录对比,发现CCWT提供最稳定的水源,而青藏高原对极端径流事件最为敏感;21世纪预测显示多数太平洋水塔径流将上升,但北落基山脉将大幅下降。Palumbo等人对上科罗拉多河流域历史数据进行因果推断,发现径流效率在降水量大、积雪多、春季凉爽且植被物候延迟的年份升高;夏季温度——常被视为干旱驱动因子——在统计上并不显著。Feng等人采用校准路径,将基于秩相关的土壤水分校准方法从流域尺度扩展至VIC模型的逐格点校准,在无地表径流观测的资料稀缺区实现径流模拟。

### Runoff Reconstructions and Future Projections Indicate Highly Variable Water Supply From Pacific Rim Water Towers

**作者**: W. Yue, M. C. A. Torbenson, F. Chen, F. Reinig, J. Esper, E. Martínez del Castillo 等

**期刊**: *AGU Advances* · **DOI**: [10.1029/2025AV002053](https://doi.org/10.1029/2025AV002053) · **引用数**: 2

**匹配主题**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> 使用包含100个树轮采样点的树轮年代学网络将中国中部水塔径流深度重构回溯至1595 CE,并与蒙古高原、青藏高原、大分水岭、南北落基山脉、安第斯山脉等六个太平洋沿岸水塔的记录对比。CCWT提供最稳定的水源,青藏高原最易出现极端径流;21世纪预测显示多数太平洋水塔径流将上升,但北落基山脉将大幅下降。

---

### Precipitation, moderated by spring temperature and vegetation, drives runoff efficiency in the Upper Colorado River Basin

**作者**: D. Palumbo, S. Gangopadhyay, U. Lall

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-025-03136-w](https://doi.org/10.1038/s43247-025-03136-w) · **引用数**: 1

**匹配主题**: river, runoff, streamflow
{: .label .label-green }

> 对上科罗拉多河流域历史数据进行因果推断,识别地表径流效率的驱动因子。降水量大、积雪多、春季凉爽以及植被物候延迟的年份径流效率上升;降水少或春季偏暖、植被活动加速时径流效率下降。夏季温度——常被视为干旱驱动因子——在统计上并不显著。降水极端相位与特定大气环流和海温异常相关。

---

### Optimizing Soil Moisture-Runoff Coupling Strength With Remotely Sensed Soil Moisture for Improved Hydrological Modeling

**作者**: H. Feng, J. Zhou, Z. Wu, J. Dong, L. Brocca, L. Zhao

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2024WR039571](https://doi.org/10.1029/2024WR039571) · **引用数**: 0

**匹配主题**: hydrologic model, runoff, streamflow
{: .label .label-green }

> 将基于秩相关、利用遥感土壤水分的校准方法从流域尺度扩展至VIC模型的逐格点参数校准,并结合汇流方案进行径流模拟。在无地表径流观测的资料稀缺区实现水文模型校准。

---

## 过程基础:寒区、模型参数与流域养分

三篇论文将水文建模锚定在其过程基础。Zhao等人在《Reviews of Geophysics》发表冻土水文综述,涵盖冻融动力学、优先流、地下水-多年冻土相互作用(包括融化层发展)以及由此引起的径流季节性变化,并为尚存的尺度化和参数化挑战提出分层建模路线图。Clerc-Schwarzenbach等人审视了一个令人不适的建模习惯:让水通过降水、蒸发、径流之外的额外路径进出桶式流域模型的"扫描参数"。他们并未谴责这种做法,反而指出这类参数可以合法地代表真实过程,只要公开透明,往往能同时改善鲁棒性和性能。Jiang等人将过程化流域模型(HYPE)应用于中国亚热带流域,发现气候变化对水文的影响大于土地利用变化,但气候变化会放大土地利用对溶解无机氮输出的影响——这说明水质预测必须在耦合气候–土地利用情景下进行。

### Frozen Soil Hydrological Processes and Their Effects: A Review and Synthesis

**作者**: Y. Zhao, C. Zheng, A. Gelfan, K. Watanabe, H. Liu, S. Wright 等

**期刊**: *Reviews of Geophysics* · **DOI**: [10.1029/2024RG000839](https://doi.org/10.1029/2024RG000839) · **引用数**: 1

**匹配主题**: hydrology, hydrologic model, streamflow, land surface model
{: .label .label-green }

> 综合冻土水文在物理、观测与建模方面的最新进展,涵盖冻融动力学、优先流、地下水-多年冻土相互作用(包括融化层发展和对流热传输)以及随之而来的径流季节性变化。梳理原位传感、地球物理、遥感以及陆面与示踪辅助水文模型对相变、大孔隙绕流和蒸气输送的表征进展,并指出尺度化、冰阻水力学和突发融化等持续性挑战,提出分层建模路线图。

---

### Cheeky Cheating or a Sensible Strategy? 'Sweep Parameters' in Bucket-Type Hydrological Models

**作者**: F. Clerc-Schwarzenbach, P. C. Astagneau, E. Muñoz Castro, I. van Meerveld, J. Seibert, V. Andréassian

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70375](https://doi.org/10.1002/hyp.70375) · **引用数**: 1

**匹配主题**: hydrology, hydrologic model, streamflow, land surface model
{: .label .label-green }

> 审视桶式水文模型中的"扫描参数"——即允许水通过降水、蒸发、径流之外的额外路径进出流域的参数。作者认为,尽管这类参数可视为"走后门"修补水量平衡,它们却是无处不在且在公开时透明的,有时还能代表真实物理过程。经验结果表明,这些参数并不必然降低模型在气象扰动下的鲁棒性,且常能改善径流模拟。

---

### Climate change expected to amplify land-use change impacts on nitrogen export from a subtropical catchment in China

**作者**: S. Jiang, A. D. Werner, L. Gao, M. Rode

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134888](https://doi.org/10.1016/j.jhydrol.2025.134888) · **引用数**: 2

**匹配主题**: hydrology, hydrologic model, runoff, streamflow, climate change
{: .label .label-green }

> 使用PEST和差分进化Markov链算法校准HYPE水文模型,应用于中国亚热带宜丰河流域研究溶解无机氮(DIN)输出。发现气候变化对水文的驱动作用大于土地利用变化,但气候变化会放大土地利用变化对DIN输出的影响——强调水质预测必须在耦合气候–土地利用情景下开展。

---

## 统计信息

| 指标 | 数量 |
|:-------|------:|
| 检索数据库 | 2 |
| 检索主题 | 16 |
| 去重前论文数 | 2,238 |
| 去重后唯一论文 | 2,040 |
| 相关性过滤后 | 12 |
| 剔除(不相关) | 2,028 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

**排序模式**: established(回填式检索采用引用数优先)

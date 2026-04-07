---
layout: default
title: "第12周（3月16日 - 3月23日），30篇"
nav_order: 33
date: 2026-03-23
categories: [weekly-zh, 2026, march]
tags: [hydrology, literature-review, research]
paper_count: 30
highlight: "可微分水文建模的进展以及NextGen水资源建模框架的发布。"
nav_exclude: true
lang: zh
lang_link: /2026/march/2026-03-23-weekly-review
---

# 每周文献综述
{: .no_toc }

**第12周** · 2026年3月16日至23日
{: .text-grey-dk-000 }

在**5**个主题中发现**30**篇相关论文
{: .fs-5 .fw-300 }

## 摘要总结

本周在可微分和新一代水文建模方面取得了显著进展，包括面向极端事件的物理信息机器学习框架、用于冻土模拟的可微分Noah陆面模型，以及NextGen水资源建模框架的发布。复合洪水建模在方法论上取得了重要贡献，比较了基于事件和基于响应的方法。一项具有里程碑意义的Nature研究以前所未有的分辨率量化了全球河流三角洲的沉降，同时Nature Water上的新研究将文本生成AI应用于水文参数估计。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 可微分与新一代水文建模

本周，物理过程模型与机器学习方法在水文学中的融合进一步加速。Song等人证明，结合机器学习与过程方程的可微分水文模型能够泛化到未见过的极端洪水事件；两个新的陆面模型——ClimaLand（专为数据驱动参数化设计）和NoahPy（用于冻土模拟的可微分Noah陆面模型）——代表了向机器学习兼容模型架构的转变。NextGen水资源建模框架引入了大陆尺度预测的社区平台，Feigl等人展示了文本生成AI可以从自然地理属性中推导水文参数。

### Physics-Informed, Differentiable Hydrologic Models for Capturing Unseen Extreme Events

**作者**: Yalan Song, Kamlesh Sawadekar, Jonathan M. Frame, Ming Pan, Martyn P. Clark, Wouter J. M. Knoben et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025WR040414](https://doi.org/10.1029/2025WR040414) · **引用数**: 9

**匹配主题**: hydrology, streamflow, flood
{: .label .label-green }

> 评估了一种结合机器学习和过程方程的混合框架（可微分建模）在训练数据之外的极端洪水事件上的泛化能力。研究考察了针对极端事件的优化是否能提升模型性能和鲁棒性，发现可微分模型相比纯机器学习方法具有更好的可解释性和空间泛化能力。

---

### ClimaLand: A Land Surface Model Designed to Enable Data-Driven Parameterizations

**作者**: Katherine Deck, R. K. Braghiere, Alexandre A. Renchon, Julia Sloan, G. Bozzola, E. Speer et al.

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025ms005118](https://doi.org/10.1029/2025ms005118) · **引用数**: 3

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 一个专门设计用于实现子网格过程数据驱动参数化的新陆面模型。ClimaLand解决了在气候模型尺度（约10-100公里）上参数化水、能量和碳通量的挑战，提供了一个可以用机器学习组件替换或增强传统参数化方案的框架。

---

### NoahPy: A Differentiable Noah Land Surface Model for Simulating Permafrost Thermo-Hydrology

**作者**: W. Tian, Hu Yu, Shuping Zhao, Yuhe Cao, Wenjun Yi, Jiwei Xu et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-57-2026](https://doi.org/10.5194/gmd-19-57-2026) · **引用数**: 1

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 创建了Noah陆面模型的可微分版本，使混合模型能够将过程物理与深度学习协同用于冻土模拟。这克服了传统不可微分陆面模型与现代AI工作流不兼容的根本障碍，为寒区水文的自动参数校准和物理-机器学习混合方法打开了大门。

---

### Distilling Hydrological and Land-Surface Model Parameters from Physio-Geographical Properties Using Text-Generating AI

**作者**: Moritz Feigl, M. Herrnegger, K. Schulz

**期刊**: *Nature Water* · **DOI**: [10.1038/s44221-026-00583-3](https://doi.org/10.1038/s44221-026-00583-3) · **引用数**: 2

**匹配主题**: hydrology, land surface model
{: .label .label-green }

> 将文本生成AI应用于直接从自然地理属性推导水文和陆面模型参数，为无观测流域参数区域化这一长期挑战提供了新方法。

---

### The NextGen Water Resources Modeling Framework: Community Innovation at the Intersection of Hydrologic, Data and Computer Sciences

**作者**: F. Ogden, Keith S. Jennings, E. Clark, E. Coon, B. Cosgrove, Luciana K. Cunha et al.

**期刊**: *JAWRA Journal of the American Water Resources Association* · **DOI**: [10.1111/1752-1688.70089](https://doi.org/10.1111/1752-1688.70089) · **引用数**: 1

**匹配主题**: hydrology, water management
{: .label .label-green }

> 介绍了用于大陆尺度水文和水力预测的NextGen框架，认为聚焦于当地主导过程的区域模型拼接可能优于单一通用模型。该框架处于水文科学、数据科学和计算机科学的交汇点，促进水资源预测的社区创新。

---

### Advancing Ecohydrological Modelling: Coupling LPJ-GUESS with ParFlow for Integrated Vegetation and Surface-Subsurface Hydrology Simulations

**作者**: Zitong Jia, Shouzhi Chen, Yongshuo H. Fu, David Martín Belda, D. Wårlind, Stefan Olin et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-1727-2026](https://doi.org/10.5194/gmd-19-1727-2026) · **引用数**: 2

**匹配主题**: earth system model, climate change, hydrology
{: .label .label-green }

> 将LPJ-GUESS动态植被模型与ParFlow整合，以捕捉许多地球系统模型目前忽略的地形驱动的植被-地表-地下水相互作用。填补了气候-水文反馈表征方面的关键空白。

---

### DeepDiscover: Towards Autonomous Discovery of Bucket-Type Conceptual Models – A Proof of Concept Applied to Hydrology

**作者**: Adoubi Vincent De Paul Adombi

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135249](https://doi.org/10.1016/j.jhydrol.2026.135249) · **引用数**: 1

**匹配主题**: hydrology, hydrologic model
{: .label .label-green }

> 利用深度学习自主发现桶式概念水文模型的概念验证，推动了自动模型结构识别的前沿。

---

## 洪水建模、预测与风险评估

复合洪水灾害评估在方法论上受到了重点关注。Santamaria-Aguilar等人揭示了基于事件和基于响应的复合洪水估计之间的巨大差异，Maduwantha等人开发了复合洪水模型的概率边界条件。GPU加速的物理模型实现了柏林城市尺度的实时洪水预报，FIER框架也被评估用于大尺度洪水淹没预测。

### Probabilistic Hierarchical Interpolation and Interpretable Neural Network Configurations for Flood Prediction

**作者**: Mostafa Saberian, Vidya Samadi, Ioana Popescu

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-371-2026](https://doi.org/10.5194/hess-30-371-2026) · **引用数**: 5

**匹配主题**: flood, streamflow, runoff
{: .label .label-green }

> 利用概率分层插值开发了可解释的神经网络配置用于水文洪水预测。解决了在保持模型可解释性的同时学习复杂降雨-径流过程的挑战。

---

### How Well Do Hydrological Models Simulate Streamflow Extremes and Drought-to-Flood Transitions?

**作者**: Eduardo Muñoz-Castro, Bailey Anderson, Paul C. Astagneau, Daniel L. Swain, Pablo A. Mendoza, Manuela I. Brunner

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-825-2026](https://doi.org/10.5194/hess-30-825-2026) · **引用数**: 4

**匹配主题**: streamflow, drought, flood, hydrologic model
{: .label .label-green }

> 评估了水文模型捕捉复合极端事件的能力——特别是干旱之后紧接发生的洪水。识别了哪些建模决策对模拟这些日益重要的旱涝急转事件影响最大。

---

### Large Discrepancies Between Event- and Response-Based Compound Flood Hazard Estimates

**作者**: S. Santamaria-Aguilar, Pravin Maduwantha, A. Enriquez, Thomas I. Wahl

**期刊**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-26-571-2026](https://doi.org/10.5194/nhess-26-571-2026) · **引用数**: 4

**匹配主题**: flood, compound flood
{: .label .label-green }

> 揭示了传统基于事件的洪水灾害评估（假设洪水概率近似于洪水驱动因子概率）与基于响应的方法（考虑洪水过程的时空变异性）之间的显著差异。对复合洪水风险评估具有重要的方法论意义。

---

### Generating Boundary Conditions for Compound Flood Modeling in a Probabilistic Framework

**作者**: Pravin Maduwantha, Thomas Wahl, S. Santamaria-Aguilar, R. Jane, S. Dangendorf, Hanbeen Kim et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-401-2026](https://doi.org/10.5194/hess-30-401-2026) · **引用数**: 4

**匹配主题**: flood, compound flood
{: .label .label-green }

> 解决了为复合洪水模型生成概率边界条件的挑战，以捕捉洪水驱动因子变异性的完整范围。推进了综合复合洪水风险评估的计算方法。

---

### Evaluating the Feasibility of Scaling the FIER Framework for Large-Scale Flood Inundation Prediction

**作者**: K. Markert, Hyongki Lee, Gus Williams, E. Nelson, Daniel P. Ames, Robert E. Griffin et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-459-2026](https://doi.org/10.5194/hess-30-459-2026) · **引用数**: 2

**匹配主题**: flood, remote sensing
{: .label .label-green }

> 评估了FIER（洪水淹没估算程序）框架在大地理范围内的可扩展性，解决了传统洪水预报方法在计算和数据需求方面的挑战。

---

### Enabling Real-Time High-Resolution Flood Forecasting for the Entire State of Berlin Through Multi-GPU Accelerated Physics-Based Modeling

**作者**: Shahin Khosh Bin Ghomash, Siqi Deng, Heiko Apel

**期刊**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-26-85-2026](https://doi.org/10.5194/nhess-26-85-2026) · **引用数**: 2

**匹配主题**: flood, climate change
{: .label .label-green }

> 展示了使用多GPU加速的物理水动力模型进行城市尺度实时洪水预报，覆盖整个柏林州。表明GPU计算的进步可以使高分辨率城市洪水建模在业务运行中变得可行。

---

## 径流与河流流量的机器学习预测

本周多种机器学习架构被应用于径流和河流流量预报。Jia等人将混合密度网络与保形推断相结合用于澳大利亚的概率径流预测，Yuan和Yan在Transformer模型中引入因果滞后注意力机制用于多尺度径流预测。混合深度学习降雨-径流预报方法和可解释的河流流量预测方法完善了这一主题。

### A Novel Hybrid Predictive Model Based on Mixture Density Networks With Weighted Conformal Inference Strategy for Runoff Interval Prediction Across Australia

**作者**: Yubo Jia, Xiaoling Su, Vijay P. Singh, Bin Zhao, T. Zhang, Jiangdong Chu et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2024WR039807](https://doi.org/10.1029/2024WR039807) · **引用数**: 3

**匹配主题**: runoff, flood, drought
{: .label .label-green }

> 开发了结合加权保形推断的混合密度网络用于澳大利亚的概率径流区间预测。通过整合保形推断策略解决了混合密度网络易受偏差影响的问题，改善了水安全应用的不确定性量化。

---

### A Hybrid Deep Learning Rainfall-Runoff Forecasting Model Incorporating Spatiotemporal Information from Multi-Source Data

**作者**: Wan Liu, Li Mo, Xiaodong Li, Wenjing Xiao, Haodong Huang, Yongchuan Zhang

**期刊**: *Expert Systems with Applications* · **DOI**: [10.1016/j.eswa.2025.129974](https://doi.org/10.1016/j.eswa.2025.129974) · **引用数**: 3

**匹配主题**: runoff, rainfall-runoff
{: .label .label-green }

> 一种融合多源数据时空信息的混合深度学习降雨-径流预报模型，以提高预报精度。

---

### Enhancing Runoff Prediction with Causal Lag-Aware Attention and Multi-Scale Fusion in Transformer Models

**作者**: Weiheng Yuan, Hua Yan

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134369](https://doi.org/10.1016/j.jhydrol.2025.134369) · **引用数**: 2

**匹配主题**: runoff
{: .label .label-green }

> 在Transformer模型中引入因果滞后注意力机制和多尺度融合以改进径流预测，解决了在多个尺度上捕捉时间依赖性的挑战。

---

### Interpretable Deep Learning Hybrid Streamflow Prediction Modeling Based on Multi-Source Data Fusion

**作者**: Zhaocai Wang, Cheng Ding, Nannan Xu, Weilong Wang, Xingxing Zhang

**期刊**: *Environmental Modelling & Software* · **DOI**: [10.1016/j.envsoft.2025.106796](https://doi.org/10.1016/j.envsoft.2025.106796) · **引用数**: 2

**匹配主题**: streamflow, deep learning
{: .label .label-green }

> 将深度学习与可解释性技术相结合用于混合河流流量预测，融合多源数据以提高预报可靠性和可理解性。

---

## 干旱、气候变化与复合事件

干旱研究涵盖了从季节预测到复合事件动力学的广泛领域。Ukkola等人利用澳大利亚国家水文预测集合评估未来季节干旱变化，Sabut和Mishra提供了干旱科学的百年文献计量综述。Li等人研究了破纪录的复合干旱-热浪事件，Kim等人表明用观测数据约束气候预测会放大预测的径流下降。

### Future Changes in Seasonal Drought in Australia

**作者**: Anna Ukkola, Steven Thomas, Elisabeth Vogel, Ulrike Bende-Michl, Steven T. Siems, Vjekoslav Matic et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-1463-2026](https://doi.org/10.5194/hess-30-1463-2026) · **引用数**: 4

**匹配主题**: drought, climate change, hydrology
{: .label .label-green }

> 利用国家水文预测集合评估澳大利亚——最干旱的有人居住大陆——未来的干旱变化。解决了模型对降水变化预测缺乏一致性所带来的持续不确定性，发现了具有季节和区域特异性的干旱趋势，为水资源管理规划提供参考。

---

### A Century of Drought Research (1900–2023): Scientific Developments, Methodological Innovations, and Emerging Frontiers

**作者**: Amitesh Sabut, A. Mishra

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025WR041987](https://doi.org/10.1029/2025WR041987) · **引用数**: 3

**匹配主题**: drought, water resources
{: .label .label-green }

> 基于超过152,000篇文献的文献计量分析，综合了一个世纪的干旱研究。追溯了从历史干旱记录到现代监测技术以及干旱科学新兴前沿的演变历程。

---

### Understanding the Dynamics of Record-Shattering Compound Drought-Heatwave Events and Their Impacts on Ecosystems

**作者**: Bohao Li, Kai Liu, Ming Wang, Yuanhang Yang, Mingzhu He, Yanfang Wang et al.

**期刊**: *Earth's Future* · **DOI**: [10.1029/2024EF005714](https://doi.org/10.1029/2024EF005714) · **引用数**: 2

**匹配主题**: drought, climate change
{: .label .label-green }

> 利用九成员集合模拟预测，在未来情景下破纪录的复合干旱-热浪事件将急剧增加。研究了这些前所未有的复合极端事件的动力学、形成机制及其对生态系统的影响。

---

### Constraining Climate Model Projections with Observations Amplifies Future Runoff Declines

**作者**: Hanjun Kim, Flavio Lehner, K. Dagon, D. Lawrence, Sean Swenson, A. W. Wood

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03213-8](https://doi.org/10.1038/s43247-026-03213-8) · **引用数**: 1

**匹配主题**: runoff, climate change
{: .label .label-green }

> 证明用观测数据约束气候模型预测会放大未来径流下降的预估，对水资源规划和气候影响评估具有重要意义。

---

## 水库、水储量与流域水文

水库监测和大尺度观测取得了重要进展。An等人利用卫星测高重建了亚洲7,433个湖泊和水库的月度水位，Zhan等人整合SWOT与多源观测实现近日尺度水库监测。一项Nature研究首次提供了全球河流三角洲沉降的高分辨率量化。在流域方面，van Tiel等人分析了2022年欧洲干旱期间冰川对河流流量的贡献，Ryu等人应用3D U-Net进行次季节降水预报。

### Water Storage Changes of Lakes and Reservoirs Across Asia (2018–2023) and Their Effects in Flood Control

**作者**: Zhiyuan An, Zhao Li, T. Jin, Weiping Jiang, Peng Yuan, Kai Liu et al.

**期刊**: *Geophysical Research Letters* · **DOI**: [10.1029/2025GL119131](https://doi.org/10.1029/2025GL119131) · **引用数**: 2

**匹配主题**: reservoir, flood, water management
{: .label .label-green }

> 整合Sentinel-3A/B和ICESat-2测高数据重建了亚洲7,433个湖泊和水库的2018-2023年月度水位。发现水库的年水位变化中值为0.36米/年，远超天然湖泊的0.05米/年，凸显了人类管理在水储量动态和防洪中的作用。

---

### Integrating SWOT With Multi-Source Satellite Observations for Near-Daily Reservoir Water Level Monitoring

**作者**: P. Zhan, Jida Wang, Tan Chen, Shuangxiao Luo, Kai Liu, L. Ke et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2024WR039711](https://doi.org/10.1029/2024WR039711) · **引用数**: 1

**匹配主题**: reservoir, water management
{: .label .label-green }

> 开发了整合SWOT与多源卫星观测的框架，实现近日尺度水库水位监测，解决了传统卫星测高在水库高频监测中的局限性，对水资源管理至关重要。

---

### Integrated Artificial Intelligence and Physics-Based Modeling for Long-Term Cascaded Hydropower Scheduling Under Extreme Heat Events

**作者**: Maryam Baghkarvasef, M. Parvania

**期刊**: *IEEE Transactions on Sustainable Energy* · **DOI**: [10.1109/TSTE.2025.3584176](https://doi.org/10.1109/TSTE.2025.3584176) · **引用数**: 4

**匹配主题**: hydropower, reservoir
{: .label .label-green }

> 整合AI和物理模型用于极端热浪事件下梯级水电系统的长期调度，推导水资源价值以实现水电站面对高温运行挑战时的有效战略规划。

---

### Advancing Climate Change Impact Assessment on Global Hydropower Systems: Methodologies, Models, and Recommendations

**作者**: Raja Fara Raja Abd Jalil, K. L. Chong, Y. F. Huang, Marlinda Abdul Malek, Mohamed Elkollaly, Mohsen Sherif et al.

**期刊**: *Renewable & Sustainable Energy Reviews* · **DOI**: [10.1016/j.rser.2025.116364](https://doi.org/10.1016/j.rser.2025.116364) · **引用数**: 2

**匹配主题**: hydropower, climate change
{: .label .label-green }

> 全面综述了评估气候变化对全球水电系统影响的方法和模型，并提出了改进评估框架的建议。

---

### Global Subsidence of River Deltas

**作者**: L. Ohenhen, M. Shirzaei, J. L. Davis, A. Tiwari, R. Nicholls, O. Dasho et al.

**期刊**: *Nature* · **DOI**: [10.1038/s41586-025-09928-6](https://doi.org/10.1038/s41586-025-09928-6) · **引用数**: 8

**匹配主题**: river, climate change
{: .label .label-green }

> 首次提供了全球河流三角洲沉降的当代高分辨率量化，发现海平面上升与土地沉降的叠加威胁着全球三角洲景观的可持续性。该研究填补了这些人口密集区域脆弱性评估中的关键空白。

---

### Swiss Glacier Mass Loss During the 2022 Drought: Persistent Streamflow Contributions Amid Declining Melt Water Volumes

**作者**: Marit van Tiel, M. Huss, M. Zappa, T. Jonas, D. Farinotti

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-23-2026](https://doi.org/10.5194/hess-30-23-2026) · **引用数**: 3

**匹配主题**: streamflow, drought, glacier
{: .label .label-green }

> 分析了2022年严重欧洲干旱期间瑞士88个冰川化流域中冰川对河流流量的贡献。表明极端冰川融化部分补偿了干旱导致的河流流量减少，但随着冰川缩小，这种缓冲能力正在下降——这是对欧洲"水塔"的关键发现。

---

### Controls on Runoff Processes in Forested Catchments Worldwide

**作者**: D. Penna

**期刊**: *Nature Water* · **DOI**: [10.1038/s44221-025-00547-z](https://doi.org/10.1038/s44221-025-00547-z) · **引用数**: 1

**匹配主题**: runoff, catchment
{: .label .label-green }

> 在全球尺度上研究了森林流域产流过程的关键控制因素，为理解森林如何调节水循环做出了基础性贡献。

---

### Regionalization of Hydrologic Behavior and Pothole Water Storage Dynamics in the Prairie Pothole Region

**作者**: J. Rahmani, Chaopeng Shen, A. Ameli

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025WR040280](https://doi.org/10.1029/2025WR040280) · **引用数**: 1

**匹配主题**: hydrology, hydrologic model
{: .label .label-green }

> 解决了草原坑洼区域以坑洼主导的流域建模挑战，该区域复杂的填充-溢出-连接机制、无观测条件以及缺乏高分辨率坑洼清单对传统和数据驱动模型均构成挑战。

---

### Increasing Resolution and Accuracy in Sub-Seasonal Forecasting Through 3D U-Net: The Western US

**作者**: Jihun Ryu, Hisu Kim, Simon Wang, Jin-Ho Yoon

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-27-2026](https://doi.org/10.5194/gmd-19-27-2026) · **引用数**: 2

**匹配主题**: precipitation, seasonal forecast
{: .label .label-green }

> 使用3D U-Net架构对美国西部的次季节降水预报进行高空间分辨率后处理，解决了传统数值天气预报模型在更精细尺度上难以捕捉复杂模式和极端事件的挑战。

---

## 统计数据

| 指标 | 数量 |
|:-------|------:|
| 搜索数据库数 | 2 |
| 搜索主题数 | 16 |
| 去重前论文总数 | 2,193 |
| 去重后唯一论文数 | 1,919 |
| LLM相关性筛选后 | 30 |
| 被排除（不相关） | 1,889 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

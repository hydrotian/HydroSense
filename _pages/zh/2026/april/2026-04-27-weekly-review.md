---
layout: default
title: "第17周（4月20日 - 4月27日），33篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/april/2026-04-27-weekly-review
date: 2026-04-27
categories: [weekly-zh, 2026, april]
tags: [hydrology, literature-review, research]
paper_count: 33
highlight: "E3SM第三版耦合自旋启动过程已记录；谱分析揭示水库调节流量变化的隐藏复杂性。"
---

# 每周文献综述
{: .no_toc }

**第17周** · 2026年4月20日–4月27日
{: .text-grey-dk-000 }

在 **6** 个主题中发现 **33** 篇相关论文
{: .fs-5 .fw-300 }

## 摘要总结

本周是地球系统建模的重要一周，E3SM第三版耦合自旋启动过程已完整记录，一项新的基准研究揭示了16个CMIP6模型中系统性的土壤水分偏差。水库研究激增，GRL发表了一项利用谱分析揭示流量调节隐藏复杂性的研究，以及多个面向多目标运行和极端条件下水电灵活性的新优化框架。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 地球系统建模与陆面过程

本周在地球系统和陆面建模方面有重要贡献。Zhang等人记录了E3SM第三版标准分辨率下的完整耦合自旋启动过程，为社区提供了海洋、海冰、陆地和大气各组件的特征平衡时间尺度。Massoud等人对16个CMIP6地球系统模型的土壤水分进行了基准测试，发现表层和根区水分表征存在显著的模型间差异，对生态水文耦合具有重要影响。Zhou等人对使用大语言模型进行地球系统模型分析时的静默失败提出了重要警告。在陆面方面，Wu等人推进了通用陆面模型中地下水动力学的参数敏感性分析，而Bechtold等人发布了一个对次日尺度影响评估至关重要的全球逐小时气候强迫数据集。

### Overview of Coupled Earth System Model spin-up for E3SM Version 3 at Standard Resolution

**作者**: Shixuan Zhang, Luke Van Roekel, Carolyn Begeman, Wuyin Lin, Xue Zheng, Mathew Maltrud et al.

**期刊**: *ESSOAr* · **DOI**: [10.22541/essoar.15002235/v1](https://doi.org/10.22541/essoar.15002235/v1) · **引用**: 0

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 完全耦合地球系统模型的自旋启动对于建立稳定且物理一致的初始条件至关重要，但它仍然是建模工作流程中计算量最大的步骤之一。本文评估并记录了能量百亿亿次地球系统模型第三版（E3SMv3）标准分辨率下的耦合自旋启动行为和特征平衡时间尺度，为更广泛的建模社区提供参考。

---

### Can We Trust LLMs for Complex Earth System Model Analysis? Silent Failure and Evidence from Module-Grounded Benchmarking

**作者**: Tian Zhou, Yun Qian, L. Ruby Leung

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2237](https://doi.org/10.5194/egusphere-2026-2237) · **引用**: 0

**匹配主题**: hydrology, streamflow, land surface model, earth system model
{: .label .label-green }

> 大语言模型（LLM）在复杂科学脚本编写方面日益强大，但这种日益增长的可靠性造成了一个悖论：其输出越可信，科学错误的结果就越容易被忽视。在地球系统模型（ESM）分析中，这种静默失败比可见崩溃更加危险，因为它们会产生看似合理的图表和统计数据，研究人员可能未经验证就接受。

---

### Benchmarking soil moisture and its relationship to ecohydrologic variables in Earth System Models

**作者**: Elias Massoud, Nathan Collier, Yaoping Wang, Jiafu Mao, Adrian Harpold, Steven A Kannenberg et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-3427-2026](https://doi.org/10.5194/gmd-19-3427-2026) · **引用**: 1

**匹配主题**: earth system model
{: .label .label-green }

> 土壤水分（SM）是生态系统生物地球物理的关键调节因子，影响植物水分关系和陆-气能量交换。本研究使用国际陆面模型基准测试（ILAMB）框架评估了CMIP6中16个地球系统模型对土壤水分的表征，重点关注全球生物群落中的表层（0–5、0–10厘米）和根区（0–100厘米）深度。

---

### Quantifying key parameter sensitivities for water table depth in hydrological schemes of CoLM-PSUADE

**作者**: Tingting Wu, Shupeng Zhang, Xiaofan Yang, Yongjiu Dai

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2275](https://doi.org/10.5194/egusphere-2026-2275) · **引用**: 0

**匹配主题**: hydrologic model, runoff, land surface model, surface water
{: .label .label-green }

> 在陆面模型（LSM）中准确表征地下水动力学对于理解水-能量循环和评估水资源至关重要。然而，大多数LSM缺乏对控制地下水位深度（WTD）参数的系统敏感性分析。本研究将通用陆面模型（CoLM）与PSUADE耦合，以识别和量化控制WTD模拟的关键参数敏感性。

---

### A global hourly ISIMIP3 climate forcing dataset for impact modeling

**作者**: Michel Bechtold, Benjamin Poschlod, Christian Otto, Jan Volkholz, Matthias Büchner, Florian Zabel

**期刊**: *ESSD* · **DOI**: [10.5194/essd-2026-227](https://doi.org/10.5194/essd-2026-227) · **引用**: 0

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 次日尺度气候数据对气候影响评估越来越重要，因为许多过程（如热应激、水文极端事件、陆面能量平衡和可再生能源生产）对日内变化具有非线性响应。日数据会遗漏短时事件并模糊次日变量间的相互作用，导致影响估计偏差。本文提出了全球逐小时ISIMIP3气候强迫数据集。

---

### High-resolution land surface modeling of climate and CO2 effects on ecosystem carbon-water coupling across the Qinghai-Tibet Plateau

**作者**: Xiazhen Xi, Xing Yuan, Yi Hao

**期刊**: *Agricultural and Forest Meteorology* · **DOI**: [10.1016/j.agrformet.2026.111195](https://doi.org/10.1016/j.agrformet.2026.111195) · **引用**: 0

**匹配主题**: hydrologic model, land surface model, surface water
{: .label .label-green }

> 摘要暂不可用。

---

### Dynamic Parameterization of Priestley-Taylor Coefficient for a More Accurate Potential Evapotranspiration Estimation in Ungauged Regions

**作者**: Pushpendra Raghav, Mukesh Kumar

**期刊**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae6464](https://doi.org/10.1088/1748-9326/ae6464) · **引用**: 0

**匹配主题**: hydrologic model, land surface model
{: .label .label-green }

> 潜在蒸散发（PET）定义为完全饱和条件下某区域的蒸散发通量，是水文建模、水分胁迫评估和理解生态系统对气候响应的关键变量。广泛使用的Priestley-Taylor方法提供了一种简单、低数据需求的PET估算方法，但其使用固定系数（α = 1.26），可能无法捕捉区域或季节变化。本研究提出了Priestley-Taylor系数的动态参数化框架。

---

## 水文建模进展与机器学习

本周水文建模在方法论上成果丰富。Ruzzante等人在HESS中证明，高NSE分数可能掩盖季节性流域中年际方差模拟的不足——这对模型评估实践是一个值得警惕的发现。深度学习继续推动边界：Heudorfer等人测试了更好的训练数据还是改进的架构对无观测流域预测更重要；Rosati和Lim揭示了LSTM记忆状态如何在Rio Hondo流域编码基流和融雪特征。物理信息方法也有进展，Mo等人开发了用于喀斯特盆地径流预测的可解释混合ML框架，Tashie等人提出了一个面向全球的流域感知地表水淹没预测框架。

### Technical note: High Nash–Sutcliffe Efficiencies conceal poor simulations of interannual variance in seasonal regimes

**作者**: Sacha Ruzzante, Wouter Knoben, Thorsten Wagener, Tom Gleeson, Markus Schnorbus

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2337-2026](https://doi.org/10.5194/hess-30-2337-2026) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, streamflow, seasonal
{: .label .label-green }

> 在高度季节性的流域中，水文模型通常在Nash-Sutcliffe效率（NSE）和Kling-Gupta效率（KGE）等常用性能指标上取得高分。然而，径流时间序列的方差由季节性、年际和不规则方差组成，NSE和KGE并未区分这些成分。本研究探讨了多个模型结构和流域中这些方差成分的性能差异。

---

### Better data or better architecture? Improving deep-learning-based prediction in ungauged basins

**作者**: Benedikt Heudorfer, Hoshin Gupta, Alexander Dölich, Ralf Loritz

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1965](https://doi.org/10.5194/egusphere-2026-1965) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 大样本水文学近年来由两个关键发展推动：一是CAMELS-US和CARAVAN等水文基准数据集的引入，二是深度学习建模框架的出现，特别是基于LSTM的区域模型。本研究探讨了更好的训练数据还是改进的模型架构对无观测流域预测技能的贡献更大。

---

### Climate change-driven runoff variations in alpine catchments: Quantitative attribution using three innovative methods coupled with cryospheric processes

**作者**: Zhenliang Yin, Chunshuang Fang, Jianan Shan, Zexia Chen, Rui Zhu, Qi Feng

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135566](https://doi.org/10.1016/j.jhydrol.2026.135566) · **引用**: 0

**匹配主题**: hydrologic model, runoff, streamflow, land surface model
{: .label .label-green }

> 摘要暂不可用。

---

### Interpretable residual-informed hybrid physics-informed machine learning framework for runoff prediction in a typical karst basin in southwest China

**作者**: Chongxun Mo, Changhao Jiang, Jiameng Xu, Yi Huang, Gang Tang, Lingling Tang et al.

**期刊**: *Environmental Modelling & Software* · **DOI**: [10.1016/j.envsoft.2026.106986](https://doi.org/10.1016/j.envsoft.2026.106986) · **引用**: 0

**匹配主题**: hydrologic model, runoff, hydropower
{: .label .label-green }

> 摘要暂不可用。

---

### Revealing Baseflow and Hydrologic Process Signatures in LSTM Memory: Insights from the Rio Hondo, New Mexico

**作者**: Michael A. Rosati, Yeo H. Lim

**期刊**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.019](https://doi.org/10.1061/9780784486931.019) · **引用**: 0

**匹配主题**: hydrologic model, surface water
{: .label .label-green }

> 本研究探讨了长短期记忆（LSTM）模型如何内部编码与基流动力学相关的水文行为。以新墨西哥州Sangre de Cristo山脉的Rio Hondo为研究对象，评估了日流量表现，并将LSTM记忆状态激活与双水库概念模型生成的水文变量进行了比较。

---

### A Basin-Aware Global Framework for Computationally Efficient Surface Water Inundation Prediction

**作者**: Arik M. Tashie, Isaac D. Gerg, Evan Koester, Carlos D. Hoyos, Eduardo Galindo, David Farnham

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1527](https://doi.org/10.5194/egusphere-2026-1527) · **引用**: 0

**匹配主题**: streamflow, surface water
{: .label .label-green }

> 在区域到全球尺度预测地表水淹没面临根本性矛盾：定制化局部模型精度高但需要专有数据且难以扩展，而全球训练系统覆盖广但需要大量计算基础设施。本研究提出了一个兼顾覆盖范围和计算效率的流域感知全球淹没框架。

---

## 径流预报与分析

径流预测和预报是本周的活跃主题。Sauquet等人发表了本周被引次数最多的论文（10次引用），描述了法国未来径流和地下水的大型瞬态多情景集合预测，为水资源规划提供了丰富且空间一致的信息。在美国西部，Özcan和Kavvas比较了加州上Feather河流域季节性预报的物理模型和数据驱动方法；Cabezas-Nivin等人解决了上Rio Grande流域的非平稳性挑战。Foley等人重建了阿拉巴马州Black Warrior河超过400年的径流记录，揭示了对流量极值的双重大气控制。

### A large transient multi-scenario multi-model ensemble of future streamflow and groundwater projections in France

**作者**: E. Sauquet, G. Évin, Sonia Siauve, Rym Aissat, Patrick Arnaud, Maud Bérel et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2277-2026](https://doi.org/10.5194/hess-30-2277-2026) · **引用**: 10

**匹配主题**: streamflow
{: .label .label-green }

> 在法国Explore2国家项目中开发的未来径流和地下水的大型瞬态多情景多模型集合预测近期已公开。Explore2的主要目标是为法国水文（地表水和地下水）资源及极端事件的未来演变提供丰富且空间一致的信息，以支持适应政策。

---

### Comparing Physically Based and Data-Driven Approaches for Seasonal Streamflow Forecasting in California's Upper Feather River Basin

**作者**: Z. Özcan, M. L. Kavvas

**期刊**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.002](https://doi.org/10.1061/9780784486931.002) · **引用**: 0

**匹配主题**: hydrology, streamflow
{: .label .label-green }

> 季节性径流预报对水库运行、洪水管理和灌溉规划至关重要，特别是在气候驱动极端事件挑战平稳性方法的积雪主导流域。本研究评估了上Feather河流域（UFRB）——加州州水工程上游Oroville大坝的关键水源——的两种互补预报范式。

---

### Ensemble streamflow forecasting with diverse loss functions

**作者**: Kshitij Dahal, Atharva Gupta, Laxman Bokati, Saurav Kumar

**期刊**: *Applied Soft Computing* · **DOI**: [10.1016/j.asoc.2026.115276](https://doi.org/10.1016/j.asoc.2026.115276) · **引用**: 0

**匹配主题**: hydrology, streamflow
{: .label .label-green }

> 摘要暂不可用。

---

### Non-Stationary Streamflow Analysis under Climate Change in the Upper Rio Grande Basin

**作者**: Oscar M Cabezas-Nivin, Eusebio Ingol-Blanco, Alessandro Apolinario

**期刊**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.080](https://doi.org/10.1061/9780784486931.080) · **引用**: 0

**匹配主题**: streamflow, climate change
{: .label .label-green }

> 气候变化正在从根本上侵蚀美国西南部水资源规划的基本原则，特别是在以积雪为主导的上Rio Grande流域。传统基础设施设计依赖于平稳性假设，即过去的水文模式将持续存在——这一前提在新条件下越来越站不住脚。本研究开发了一个综合的非平稳框架来应对这一挑战。

---

### Dual Atmospheric Controls Amplify Streamflow Extremes in Alabama

**作者**: Zachary W. Foley, G. Harley, R. Thaxton, M. Therrell, Charles Jones, Meng Zhao et al.

**期刊**: *Environmental Research Communications* · **DOI**: [10.1088/2515-7620/ae6399](https://doi.org/10.1088/2515-7620/ae6399) · **引用**: 0

**匹配主题**: streamflow
{: .label .label-green }

> 美国东南部近几十年经历了人口增长和城市化加速，凸显了水管理和水资源可用性的重要性。Black Warrior河流域位于降水趋势增加的地区，此前无径流重建记录。本研究重建了超过400年（1550-2023 CE）的5-7月径流，揭示了对流量极值的双重大气控制。

---

## 水库运行与水电

水库研究本周活动激增。Zhang等人在GRL中对205个美国水库应用谱分析，将调节效应分解为运行模式和运行强度，揭示了水库在不同时间尺度上选择性地改变流量变化——这种复杂性此前被时域方法所掩盖。在优化方面，Chen等人为龙滩水库开发了平衡洪水风险、蓄水量和水电的多目标水库蓄水模型；Khandaker等人使用动态规划进行Lewisville湖的多目标运行。Son等人首次系统量化了25年数据中极端温度事件期间的水电灵活性。Dell'Aira和Cancelliere探索了SEAS5季节预报在自适应运行中的应用，Huang等人则解决了旱涝急转对水库管理的新兴挑战。

### Hidden Complexity in Reservoir Flow Regulation Revealed by Spectral Analysis

**作者**: Fenghe Zhang, Peirong Lin, Tongbi Tu

**期刊**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl121654](https://doi.org/10.1029/2026gl121654) · **引用**: 0

**匹配主题**: hydrologic model, streamflow, reservoir
{: .label .label-green }

> 理解水库对径流的调节对水文建模和生态水文评估至关重要，但我们对水库如何优先改变不同时间尺度流量变化的认识仍然有限。本文对205个美国水库的日入流-出流数据应用谱分析，将调节效应分解为运行模式（水库如何改变流量变化）和运行强度（改变程度如何）。

---

### Quantifying hydropower flexibility during extreme temperature events

**作者**: Kyongho Son, Cameron Bracken, Erfaneh Sharifi, Sohom Datta, Abhishek Somani

**期刊**: *ESSOAr* · **DOI**: [10.31223/x5bf4h](https://doi.org/10.31223/x5bf4h) · **引用**: 0

**匹配主题**: streamflow, hydropower
{: .label .label-green }

> 极端天气事件会给电网带来巨大压力。水电提供独特的运行灵活性，增强电网的韧性和可靠性。尽管灵活性价值重要，但对水电灵活性的系统评估——特别是在极端事件期间——仍然有限。本研究首次利用25年观测数据量化了水电运行灵活性。

---

### Developing an Optimization Model for Multipurpose Reservoir Operations at Lewisville Lake

**作者**: Nabila Khandaker, Mohammad Moradi, Afiya Narzis, Qazi Ashique Mowla

**期刊**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.023](https://doi.org/10.1061/9780784486931.023) · **引用**: 0

**匹配主题**: hydrologic model, reservoir, hydropower
{: .label .label-green }

> 本研究开发了一个优化模型，用于评估德克萨斯州Denton县Lewisville湖（Garza-Little Elm水库）的改进运行策略。该水库建于1954年，服务于多种用途，包括防洪、城市和工业供水、休闲和小型水电发电。采用离散动态规划方法平衡竞争目标。

---

### Multi-objective optimization of reservoir refill operate considering energy storage and hydrological conditions

**作者**: Lihua Chen, Kaipeng Yang, Yunyao Chen, Xi Zhang, Xuefang Li

**期刊**: *River* · **DOI**: [10.1002/rvr2.70050](https://doi.org/10.1002/rvr2.70050) · **引用**: 0

**匹配主题**: hydrologic model, reservoir, hydropower
{: .label .label-green }

> 优化水库蓄水运行规则对于提高水库可持续性和韧性至关重要。本研究提出了一种蓄水运行模型，通过考虑防洪风险、最大蓄水位以及水电发电和储能的综合效益来推导最优蓄水引导曲线。该模型应用于龙滩水库。

---

### Assessing water resources service value through simulation of a water supply–hydropower generation–ecosystem photosynthesis nexus system

**作者**: Yue Feng, Dedi Liu, Hanxu Liang, 张嘉裕 Zhang Jiayu

**期刊**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2026.110365](https://doi.org/10.1016/j.agwat.2026.110365) · **引用**: 0

**匹配主题**: hydrologic model, streamflow, hydropower
{: .label .label-green }

> 水资源通过供水（S）、水电发电（H）和生态系统光合作用（E）产生服务价值，形成支持可持续水资源管理的SHE枢纽系统。然而，这些服务价值通常被孤立评估，忽略了SHE枢纽系统内的复杂交互作用。

---

### How Increasingly Frequent Drought-Flood Abrupt Alternation Events Affect Reservoir Operation?

**作者**: Y Huang, Jianyu Fu, Xuejin Tan, Zhihong Deng, Haibo Peng, Wenzhi Zhang et al.

**期刊**: *Water Resources Management* · **DOI**: [10.1007/s11269-026-04634-y](https://doi.org/10.1007/s11269-026-04634-y) · **引用**: 0

**匹配主题**: reservoir, flood, drought
{: .label .label-green }

> 摘要暂不可用。

---

### Use of SEAS5 Seasonal Forecast Products for Adaptive Reservoir Operations

**作者**: Francesco Dell'Aira, Antonino Cancelliere

**期刊**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.038](https://doi.org/10.1061/9780784486931.038) · **引用**: 0

**匹配主题**: reservoir, seasonal
{: .label .label-green }

> 水库运行在确保水资源可用性和可靠性方面发挥着关键作用，尤其是在易旱地区。传统上，供水水库使用历史气候数据和短期天气预报进行管理。然而，这些传统方法往往缺乏实施主动措施（如对冲释放策略）所需的预测能力来缓解缺水风险。本研究探索了SEAS5季节预报产品在自适应水库管理中的应用。

---

## 洪水与干旱研究

洪水和干旱研究跨越了不同的地理区域和方法。Emamjomehzadeh和Wani在Communications Earth & Environment中开发了一个可扩展的洪水风险框架，评估了纽约州2300个涵洞服务流域，揭示了基础设施脆弱性的依赖模式。Kuntla和Saharia首次提供了印度全国观测洪水严重程度的综合时空评估。在干旱方面，Ogunrinde等人发现非洲气象干旱出现了新的重组和持续性增加。Gupta和Arrighi提出了将洪水驱动因素与内陆水文资产损害联系起来的新概念框架，而Jamal等人推进了树枝状河道网络的动态洪水演算方法。

### Scalable flood-risk analysis for New York State culvert infrastructure reveals patterns of dependence

**作者**: Omid Emamjomehzadeh, Omar Wani

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03550-8](https://doi.org/10.1038/s43247-026-03550-8) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 洪水漫过道路会扰乱交通、威胁公共安全并损害结构稳定性。涵洞——将水引导通过道路下方的结构——对防洪至关重要，但全州修复将耗资数十亿美元。本研究通过量化纽约州2300个流域的大型涵洞水力容量超越概率来评估可靠性，揭示了洪水风险的依赖模式。

---

### Observed Riverine Flood Severity in India

**作者**: Sai Kiran Kuntla, Manabendra Saharia

**期刊**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0213.1](https://doi.org/10.1175/jhm-d-25-0213.1) · **引用**: 0

**匹配主题**: streamflow, flood
{: .label .label-green }

> 印度洪水频繁且具有破坏性，每年造成重大经济损失和人员伤亡。洪水的严重程度和影响因流域地貌、气候、局部暴露度、脆弱性和现有防洪措施而异。然而，印度全国范围内观测洪水严重程度的综合时空评估一直缺失。本文提出了全面分析以填补这一空白。

---

### Emergent reorganization and increased persistence of meteorological drought across Africa

**作者**: Akinwale T. Ogunrinde, Paul Adigun, Koji Diaraku, Xian Xue, Ebiendele Precious, Ermias Sisay Brhane

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03528-6](https://doi.org/10.1038/s43247-026-03528-6) · **引用**: 0

**匹配主题**: streamflow, drought
{: .label .label-green }

> 非洲干旱正变得更加频繁和严重，但其潜在行为是否也在改变仍不清楚。本研究将气候研究单位的观测气候数据与CMIP6的16个气候模型集合相结合，检验了四个非洲区域的干旱动态。使用干旱事件特征、持续性指标和转移概率，发现了新的重组模式。

---

### From drivers to damage: A conceptual framework for integrated flood risk assessment of inland hydrological assets

**作者**: Kunal Gupta, Chiara Arrighi

**期刊**: *The Science of The Total Environment* · **DOI**: [10.1016/j.scitotenv.2026.181813](https://doi.org/10.1016/j.scitotenv.2026.181813) · **引用**: 0

**匹配主题**: streamflow, flood
{: .label .label-green }

> 内陆水文系统中的洪水风险源于驱动因素、暴露路径和脆弱性之间的动态交互。然而，现有评估方法将这些维度孤立处理，未能捕捉级联和复合效应。本研究开发了一个新的综合洪水风险评估概念框架，建立了从驱动因素到内陆水文资产损害的系统联系。

---

### Performance Analysis of Iteration-Based Dynamic Flood Routing Model for Dendritic Channel Networks

**作者**: Jani Fathima Jamal, Erfan Goharian, Jasim Imran, M. Hanif Chaudhry

**期刊**: *Journal of Hydraulic Engineering* · **DOI**: [10.1061/jhend8.hyeng-14381](https://doi.org/10.1061/jhend8.hyeng-14381) · **引用**: 0

**匹配主题**: hydrologic model, flood
{: .label .label-green }

> 有效的洪水预报系统需要动态演算来准确预测从缓慢上涨到快速上涨等多种条件下的洪水。然而，对于业务预报，动态演算计算量大，特别是对于大型河道网络，需要高效的求解方法。本研究分析了基于迭代的动态洪水演算模型在树枝状河道网络中的性能。

---

## 气候变化对水资源的影响

不同环境下的气候变化水资源影响研究得到了探索。Shafeeque等人调查了高山亚洲喀喇昆仑地区动态碎屑覆盖变化与冰川融水之间的相互作用，量化了预测气候情景下对下游淡水可用性的影响。Hermosillo等人研究了变暖如何改变寒冷地区的冻融动态和地下水-热通量，对入渗和含水层补给具有重要意义。Huang等人在全球多个城市评估了城市气候模型中水文过程的增强表征，强调了将城市水文与气候预测耦合的重要性。

### Investigating Effects of Dynamic Debris Cover Variations on Glacio-Hydrology under Projected Climate Change in High Mountain Asia

**作者**: Muhammad Shafeeque, Arfan Arshad, Amna Bibi, Tahira Khurshid, Abid Sarwar, T. Tran et al.

**期刊**: *Earth Systems and Environment* · **DOI**: [10.1007/s41748-026-01125-3](https://doi.org/10.1007/s41748-026-01125-3) · **引用**: 0

**匹配主题**: hydrology, hydrologic model
{: .label .label-green }

> 高山亚洲（HMA）冰川上的碎屑覆盖在塑造冰川演化和下游淡水可用性方面起着关键作用。在喀喇昆仑，冰川融水显著影响河流径流，但气候变化与冰面碎屑覆盖之间的相互作用仍未被充分量化。本研究使用水文空间过程模型开发了动态碎屑覆盖框架来评估这些相互作用。

---

### Effects of Climate Change on Water and Heat Fluxes in the Shallow Subsurface in Cold Regions

**作者**: Joaquin Sainz Hermosillo, R. M. Neupauer, Jarkko Okkonen

**期刊**: *ASCE Proceedings* · **DOI**: [10.1061/9780784486931.017](https://doi.org/10.1061/9780784486931.017) · **引用**: 0

**匹配主题**: land surface model, surface water
{: .label .label-green }

> 寒冷地区浅层地下的水冻融在地表（如降水、入渗）与地下（如含水层补给）之间的水交换中起着重要作用。气候变暖将导致冻结事件时间和持续时间的变化，影响近地表水和热通量。

---

### Enhanced representation of hydrological processes in urban climate modeling: A multi-city global assessment

**作者**: Yuqi Huang, Chenghao Wang, Zhi-Hua Wang

**期刊**: *Urban Climate* · **DOI**: [10.1016/j.uclim.2026.102908](https://doi.org/10.1016/j.uclim.2026.102908) · **引用**: 0

**匹配主题**: hydrologic model, runoff
{: .label .label-green }

> 摘要暂不可用。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 搜索数据库数 | 2 |
| 搜索主题数 | 16 |
| 获取论文总数 | 1350 |
| 去重后 | 1106 |
| 黑名单过滤后 | 1040 |
| 经LLM相关性筛选后 | 33 |
| 拒绝（不相关） | 1007 |

### 按期刊分类

| 期刊 | 论文数 |
|:-----|-------:|
| EGUsphere / ESSOAr | 5 |
| ASCE Proceedings | 5 |
| Geophysical Research Letters | 1 |
| Hydrology and Earth System Sciences | 2 |
| Communications Earth & Environment | 2 |
| Geoscientific Model Development | 1 |
| Journal of Hydrology | 1 |
| Environmental Research Letters | 1 |
| Environmental Modelling & Software | 1 |
| Agricultural and Forest Meteorology | 1 |
| Applied Soft Computing | 1 |
| Environmental Research Communications | 1 |
| Journal of Hydrometeorology | 1 |
| The Science of The Total Environment | 1 |
| Journal of Hydraulic Engineering | 1 |
| Water Resources Management | 2 |
| Agricultural Water Management | 1 |
| River | 1 |
| Earth Systems and Environment | 1 |
| Urban Climate | 1 |
| ESSD | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

---
layout: default
title: "第18周（4月27日 - 5月4日），30篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/may/2026-05-04-weekly-review
date: 2026-05-04
categories: [weekly-zh, 2026, may]
tags: [hydrology, literature-review, research]
paper_count: 30
highlight: "加州在升温情景下面临前所未有的水文变化；新型物理-AI框架推进梯级水库调度。"
---

# 每周文献综述
{: .no_toc }

**第18周** · 2026年4月27日–5月4日
{: .text-grey-dk-000 }

跨 **6** 个主题发现 **30** 篇相关论文
{: .fs-5 .fw-300 }

## 摘要总结

水文建模领域本周进展显著，多篇WRR论文探讨了模型组合策略、空间显式参数化以及无测站流域预测方法。加州水资源未来的详细预测显示在0.5至3.5°C升温情景下出现前所未有的水文变化。机器学习与水文学的融合持续深化，物理-AI混合框架应用于水库调度和卫星嵌入融合用于河网流量重建。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 大尺度水文建模与地球系统模型

本周多项研究推进了对全球和区域水文模型关键过程表征的理解。Bass等人利用降尺度的地球系统模型集合预测了升温情景下加州水文的前所未有变化，而Ralhan和Liang开发了基于物理信息的机器学习方法来改进地球系统模型中的地表反照率参数化。在陆面模型尺度上，Raghav和Kumar提出了一种校正涡度协方差测量中地表能量不平衡的新方法，Bender等人通过CLM5的动态耦合图块方法解决了热融沉陷过程的表征问题。

### Unprecedented Shifts in Hydrology Are Emerging Across California's Critical Basins: An Evaluation From 0.5 to 3.5°C

**作者**: B. Bass, L. Su, D. Pierce et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041338](https://doi.org/10.1029/2025wr041338) · **引用**: 0

**匹配主题**: hydrology, runoff, earth system model
{: .label .label-green }

> 随着气候模型和降尺度技术的进步，利益相关者期待高分辨率分析为区域到地方水管理变化提供信息。本研究利用经过筛选和降尺度处理的地球系统模型集合，为支持加州第五次气候变化评估生成水文预测。结果揭示了加州关键流域在0.5至3.5°C升温情景下出现的前所未有的水文变化。

---

### Capturing Spatiotemporal and Subgrid Variability in Global Land Surface Albedo Parameterization

**作者**: Akarsh Ralhan, Xin‐Zhong Liang

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025ms005436](https://doi.org/10.1029/2025ms005436) · **引用**: 0

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 准确的地表反照率参数化对模拟地球能量平衡至关重要。然而，许多方案依赖于静态查找表或半经验公式，无法捕捉时空变化和复杂的辐射相互作用。本研究利用19年（2003–2021年）的MODIS双向反射分布函数数据和基于过程的预测因子，开发了一种基于物理信息的机器学习参数化方法。

---

### PULSE: A Novel Potential Underlying Water Use Efficiency‐Based Method for Latent Heat and Surface Energy Imbalance Correction

**作者**: Pushpendra Raghav, Mukesh Kumar

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042766](https://doi.org/10.1029/2025wr042766) · **引用**: 0

**匹配主题**: land surface model, surface water, earth system model
{: .label .label-green }

> 蒸散发（ET）在陆面水分和能量收支中发挥关键作用。涡度协方差（EC）是生态系统尺度上最广泛使用的ET测量技术，为了解陆气相互作用和作为地球系统模型的基准提供依据。然而EC测量经常存在能量平衡不闭合问题。本研究提出PULSE方法，利用潜在水分利用效率概念来分配和校正地表能量不平衡。

---

### Modeling Ice Rich Permafrost Landscapes with CLM5 Using Dynamically Coupled Tiles

**作者**: Esther Karin Bender, Matvey V. Debolskiy, Kjetil Aas et al.

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1039](https://doi.org/10.5194/egusphere-2026-1039) · **引用**: 0

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 多年冻土区大量地下冰的融化可导致快速、大规模的地貌变化（即热融沉陷），显著改变土壤和陆面的热、水文和生物地球化学状态。这些热融沉陷过程由过量地下冰和多年冻土微地形驱动。然而大尺度陆面模型无法表征这些过程。本研究在CLM5中提出动态耦合图块方法来表征热融沉陷景观演变。

---

### Advancing Understanding of Parameterization Effects in Global Hydrologic Models Through Multi-Model, Multi-Variable Evaluation

**作者**: Junho Kim, Jonghun Kam, Daeryong Park et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135208](https://doi.org/10.1016/j.jhydrol.2026.135208) · **引用**: 1

**匹配主题**: hydrologic model
{: .label .label-green }

> 摘要暂无。

---

## 流量预测与水文模型开发

本周在改进流量预测方面取得了显著进展，特别是针对无测站和数据稀缺流域。Thébault等人证明，在时空维度上变化模型组合优于固定的单模型方法；Zheng等人表明空间显式参数化结合多站校准能显著改进分布式水文建模。Lin等人的卫星嵌入融合流量重建将Google卫星嵌入集成到河段尺度的残差学习框架中。Argentin等人解决了阿尔卑斯冰川化集水区日尺度流量降尺度到亚日尺度的独特挑战。

### Varying the Combination of Hydrological Models in Time and Space: Toward a More Accurate Representation of Streamflow

**作者**: C. Thébault, W. J. M. Knoben, N. Addor

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042272](https://doi.org/10.1029/2025wr042272) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 准确的流量预测对水资源管理、洪水风险评估以及支持农业和工业至关重要。许多水文研究依赖于在空间上统一应用、在时间上固定不变的单一模型结构和参数集，限制了其捕捉流量产生过程复杂性和变异性的能力。本研究探索了在时空维度上变化水文模型组合能否改善流量预测。

---

### What Can Hydrological Modelling Gain From Spatially Explicit Parameterization and Multi-Gauge Calibration?

**作者**: Xudong Zheng, Dengfeng Liu, Hao Wang

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2493-2026](https://doi.org/10.5194/hess-30-2493-2026) · **引用**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 传统水文建模面临来自数据驱动方法兴起和建模真实性需求提升的变革压力。随着数据可用性的提升，空间显式参数化和多站校准为增强过程模型的物理一致性和空间可迁移性提供了有前景的路径。

---

### A Comparative Assessment of Cluster-Based Regionalization Approaches Using Conceptual Rainfall–Runoff Models

**作者**: Jamal Hassan Ougahi, John S. Rowan

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-49424-z](https://doi.org/10.1038/s41598-026-49424-z) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> 无测站集水区的准确流量预测仍然是水文学的核心挑战。本研究考察了区域化方法的实用性，探索了水文信息聚类如何影响不同径流模型在全国范围集水区上的参数迁移性和性能。

---

### Improving Streamflow Predictions in Data-Scarce Nested Basins Through Residual Transfer and Post-Processing

**作者**: Kue Bum Kim, Dawei Han, Hyun‐Han Kwon

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-49028-7](https://doi.org/10.1038/s41598-026-49028-7) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 数据稀缺和部分设站河流流域的可靠流量预测仍然是水文建模的重大挑战。即使经过校准，概念性降雨-径流模型由于结构限制，在中低流量状态下仍存在系统性误差。本研究提出了一种残差迁移和后处理方法来改进嵌套流域的预测。

---

### Fusing Satellite Embeddings to Improve Streamflow Reconstruction Across River Networks

**作者**: Haomei Lin, Peirong Lin, Fenghe Zhang

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1834](https://doi.org/10.5194/egusphere-2026-1834) · **引用**: 0

**匹配主题**: river, streamflow, land surface model
{: .label .label-green }

> 在地表条件深度改变的背景下，河网流量重建面临日益严峻的挑战。本文提出了卫星嵌入数据集成模型（DISE），一个河段尺度的残差学习框架，将Google卫星嵌入与过程模型输出集成，以改进河网流量重建。

---

### Downscaling Daily Discharge to Sub‐Daily Scales for Alpine Glacierized Catchments

**作者**: A.-L. Argentin, M. Gianini, B. Schaefli

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr040699](https://doi.org/10.1029/2025wr040699) · **引用**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 阿尔卑斯冰川化集水区的水文动态受温度驱动过程（包括冰雪融化和降水）的影响，产生在季节内和季节间变化的日流量周期。在夏季融化期间，这些亚日变化的幅度可以与暴雨事件相当或超过。本研究开发了将冰川化集水区日流量降尺度到亚日尺度的方法。

---

### SWATtunR: A Transparent and Reproducible Workflow for Scripted SWAT+ Calibration in R

**作者**: Svajūnas Plunge, Christoph Schürz, Michael Strauch

**期刊**: *Environmental Modelling & Software* · **DOI**: [10.1016/j.envsoft.2026.107014](https://doi.org/10.1016/j.envsoft.2026.107014) · **引用**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 摘要暂无。

---

## 机器学习与人工智能在水资源中的应用

物理-AI混合方法在水资源领域持续获得动力。Zhu等人提出了一个优化-学习-仿真框架用于梯级水库调度，弥合了历史运行与未来气候情景之间的差距。Rittima等人比较了机器学习和深度学习方法在水库入库流量预测中的应用，发现多变量LSTM模型显著优于单变量方法。Zhou等人引入了一种异构多图时空网络，捕捉径流预报中的复杂空间依赖关系。

### Physics‐AI Synergized Optimization‐Learning‐Simulation Framework for Robust Cascade Reservoir Scheduling Under Future Hydrological Scenarios

**作者**: Zhaoyang Zhu, Haotian Wu, Zhaocai Wang et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042149](https://doi.org/10.1029/2025wr042149) · **引用**: 0

**匹配主题**: runoff, hydropower
{: .label .label-green }

> 梯级水库协调优化对于最大化流域经济、社会和生态效益至关重要。然而传统水电调度缺乏对复杂未来情景的适应性，受限于季节水文变异性和不确定入流。虽然AI算法为水库运行提供了新途径，但弥合历史优化策略与预测水文条件之间的差距仍然是一个挑战。

---

### Predictive Performances of Machine Learning– and Deep Learning–Based Univariate and Multivariate Reservoir Inflow Prediction Models

**作者**: A. Rittima, Jidapa Kraisangka, Pheeranat Dornpunya et al.

**期刊**: *Modeling Earth Systems and Environment* · **DOI**: [10.1007/s40808-026-02795-8](https://doi.org/10.1007/s40808-026-02795-8) · **引用**: 2

**匹配主题**: river, streamflow, reservoir
{: .label .label-green }

> 本研究展示了基于机器学习和深度学习的单变量和多变量水库入库流量预测的可预测性，以湄南河流域的两座主要大坝（普密蓬和诗琳通）为研究对象。评估了XGBoost（基于树的集成方法）和LSTM（深度神经网络模型）在不同预见期和输入配置下的性能。

---

### A Heterogeneous Multi-Graph Spatio-Temporal Network for Runoff Forecasting

**作者**: Xuerui Zhou, Baowei Yan, J Zhang

**期刊**: *Engineering Applications of Artificial Intelligence* · **DOI**: [10.1016/j.engappai.2026.114967](https://doi.org/10.1016/j.engappai.2026.114967) · **引用**: 0

**匹配主题**: hydrology, runoff
{: .label .label-green }

> 摘要暂无。

---

## 洪水过程与风险评估

本周洪水研究涵盖了从过程理解到风险管理。Kritidou等人揭示了降水递减率如何显著影响山区径流模拟和洪水频率估计。Collins等人展示了环境示踪剂如何降低自然洪水管理建模的不确定性，Porhemmat等人分析了大气河如何驱动新西兰2021-2022年韦斯特波特极端洪水。在基础设施层面，Perks等人量化了河道重整的水力效应，Dasari等人系统研究了前期土壤湿度在多个印度流域洪水生成中的作用。

### How Precipitation Lapse Rates Shape Runoff Simulations and Flood Frequency Estimates in Mountainous Regions

**作者**: Eleni Kritidou, Martina Kauzlaric, Maria Staudinger

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2338](https://doi.org/10.5194/egusphere-2026-2338) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, runoff, streamflow, flood
{: .label .label-green }

> 降水递减率（PLR）在山区集水区的水文模拟中发挥关键作用。然而它们在降水估计中的表征往往不够充分，在水文模型中通常被简化为常数正值。本研究结合观测和基于模型的分析，考察不同PLR表征如何影响径流模拟和洪水频率估计。

---

### Using Environmental Tracers to Reduce Uncertainty in Natural Flood Management Modeling

**作者**: Sarah L. Collins, Leo Peskett, Andrew R. Black

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041145](https://doi.org/10.1029/2025wr041145) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, streamflow, flood
{: .label .label-green }

> 自然洪水管理（NFM）是一种基于自然的解决方案，在过去二十年中在洪水风险政策和管理中日益重要。然而关于基于自然解决方案有效性的证据有限，且缺乏预测其性能的公认最佳实践。本研究应用示踪剂辅助方法来约束NFM建模的不确定性。

---

### Atmospheric Rivers and Flood Variability in a Maritime Catchment: Lessons from the 2021–2022 Westport Floods, New Zealand

**作者**: Rasool Porhemmat, Céline Cattoën, Jono Conway

**期刊**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0168.1](https://doi.org/10.1175/jhm-d-25-0168.1) · **引用**: 0

**匹配主题**: hydrologic model, runoff, flood
{: .label .label-green }

> 大气河日益被认识为全球许多地区极端降水和洪水的主要驱动因素。在新西兰西海岸，布勒集水区近年来经历了数次严重洪水，引发了关于大气河特征如何影响海洋性集水区洪水变异性的迫切问题。

---

### Hydraulic Effects of Channel Realignment and Floodplain Reconnection in a Headwater Stream

**作者**: MT Perks, N. Barber, G. L. Heritage

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041858](https://doi.org/10.1029/2025wr041858) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 河道重整和洪泛区重连日益被用作洪水管理的基于自然的解决方案，但其水力效应在中等坡度小型河道的野外环境中仍缺乏充分量化。本研究考察了此类干预措施对源头溪流水力条件的影响。

---

### Understanding Flood Behaviour: The Role of Antecedent Soil Moisture, Rainfall and Catchment Attributes Across Multiple Basins

**作者**: Indhu Dasari, Vamsi Krishna Vema, Bharathsagar Jajolla

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70565](https://doi.org/10.1002/hyp.70565) · **引用**: 0

**匹配主题**: hydrologic model, flood
{: .label .label-green }

> 本研究旨在利用HEC-HMS模型中的土壤水分核算（SMA）方法，理解前期土壤湿度（ASM）条件对九个印度流域洪水特征的影响。在不同ASM条件下模拟假设降雨情景，以评估事件前土壤湿度状态如何影响洪峰流量、洪量和洪水时间。

---

## 水资源管理、干旱与气候影响

本周水资源管理研究涵盖多篇WRR发表的关于气候变化与水资源规划交叉领域的论文。Zheng等人表明年际降水变异性增加会在平均干旱化之外进一步加剧水资源压力。Yan等人引入了大流域适应性水管理的顺序干预框架，Han等人开发了捕捉水资源分配中连续人类决策过程的社会水文模型。在干旱方面，Jackson等人推导了用于业务干旱监测的互补关系蒸散发，Xue等人（Nature Communications）重建了过去千年欧洲水文气候，揭示了斯堪的纳维亚大气模式如何塑造夏季干旱。

### How Will Higher Interannual Precipitation Variability Intensify Water Stress Under a Drying Climate?

**作者**: Hongxing Zheng, Francis Chiew, David Post et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042767](https://doi.org/10.1029/2025wr042767) · **引用**: 0

**匹配主题**: hydrologic model, runoff, streamflow
{: .label .label-green }

> 气候变化预计将改变降水的均值和变异性。降水变异性增加的水文后果仍不如降水均值变化引起的后果被理解。本研究通过综合建模框架评估了年降水均值和变异性变化对澳大利亚东南部径流和供水系统的综合影响。

---

### Evaluate Sequential Interventions for Adaptive Water Management in Large River Basins

**作者**: Yuhan Yan, Tingju Zhu, Zhenxing Zhang et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042451](https://doi.org/10.1029/2025wr042451) · **引用**: 0

**匹配主题**: hydrologic model, river, water management
{: .label .label-green }

> 综合流域管理（IRBM）和适应性水管理（AWM）已被广泛推广为指导原则，但其在流域尺度的实际实现仍然困难且利用不足。顺序干预（SI）——在预定决策点按预定顺序逐步实施的行动，为实施AWM提供了实用且适应性的方法。

---

### A Socio‐Hydrological Model for Adaptive Water Allocation in the Heihe River Basin

**作者**: Ziyan Han, Yongping Wei, Jijun Meng et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr040623](https://doi.org/10.1029/2025wr040623) · **引用**: 0

**匹配主题**: hydrologic model, river
{: .label .label-green }

> 流域可持续管理需要理解水资源分配如何响应驱动它的人类决策，以及随后的经济和生态后果。当前模型通常将水资源分配决策视为单一和不连续的事件，忽略了人类决策过程的连续性和适应性。本研究开发了一个社会水文模型，捕捉黑河流域水资源分配和人类适应的协同演变。

---

### A Method to Implement Natural Flow Regimes for Regulated Rivers

**作者**: Nicholas A. Som, Seth W. Naman

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041095](https://doi.org/10.1029/2025wr041095) · **引用**: 0

**匹配主题**: hydrology, river, hydropower
{: .label .label-green }

> 世界各地的河流已被筑坝用于防洪、灌溉、水力发电和蓄水数百年。大坝服务于社会的经济和发展需求，但会退化河流生态。为保护日益减少的水生物种及其栖息地，需要帮助管理者实施具有与水生群落相关时间尺度和模式的流量释放方法。

---

### Probabilistic Agro‐Hydrology: A Stochastic Framework for Irrigation Risk Assessment and Water Management

**作者**: D. D. Chiarelli, E. Volpi, A. Fiori

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041844](https://doi.org/10.1029/2025wr041844) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, water management, irrigation
{: .label .label-green }

> 灌溉在日益增加的气候变异性下稳定农业生产力方面发挥着关键作用。然而干旱和极端天气事件的加剧暴露了灌溉系统的脆弱性，尤其是用水高峰需求与供水可用性之间的不匹配。本研究提出了一个将水文不确定性纳入水管理决策的随机灌溉风险评估框架。

---

### Fielding Floods for Flourishing Farms: A Framework for Assessing the Reuse of Small Flood Reservoirs as Irrigation Reservoirs

**作者**: Sarah Ho, Jacob Bernhardt, Kerstin Stahl

**期刊**: *Earth's Future* · **DOI**: [10.1029/2025ef006841](https://doi.org/10.1029/2025ef006841) · **引用**: 0

**匹配主题**: streamflow, reservoir, flood, irrigation
{: .label .label-green }

> 由于全球变暖下干旱的强度和频率增加，农业灌溉需求（AID）在世界许多地区可能增加——不仅在半干旱和干旱地区，也在温带地区。小型水库常被视为地方水管理的分散解决方案。本研究开发了评估现有小型防洪水库作为灌溉水库再利用潜力的框架。

---

### Complementary Relationship-Derived Actual Evapotranspiration for Operational Drought Monitoring

**作者**: Darren L. Jackson, Mike Hobbins, Mimi Rose Abel

**期刊**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0169.1](https://doi.org/10.1175/jhm-d-25-0169.1) · **引用**: 0

**匹配主题**: streamflow, drought, land surface model
{: .label .label-green }

> 为开发用于业务干旱监测的实际蒸散发（ETa）数据集，本研究使用了基于互补关系中平流-干旱方法的模型，结合北美陆面数据同化系统第二阶段（NLDAS-2）大气强迫数据。

---

### Hyperspectral Constraints Reduce Bias in ECOSTRESS Evapotranspiration and Drought Indicators

**作者**: M. Marshall, Monica Pepe, Giulia Tagliabue

**期刊**: *Remote Sensing of Environment* · **DOI**: [10.1016/j.rse.2026.115453](https://doi.org/10.1016/j.rse.2026.115453) · **引用**: 0

**匹配主题**: drought, land surface model, earth system model
{: .label .label-green }

> 非洲旱地的干旱威胁区域粮食安全和全球农业市场。预警系统日益依赖地球观测（EO），但基于降水的指标往往无法检测到新出现的植被水分胁迫。随着新型低地球轨道任务的出现，来自热红外的蒸散发提供了有前景的补充。本研究证明高光谱约束可以减少ECOSTRESS蒸散发反演的偏差并提高干旱指标的准确性。

---

### Scandinavian Pattern and Temperature Changes Shape European Summer Droughts Over the Past Millennium

**作者**: Huihong Xue, H Goosse, Quentin Dalaiden et al.

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-026-72385-w](https://doi.org/10.1038/s41467-026-72385-w) · **引用**: 0

**匹配主题**: drought, earth system model
{: .label .label-green }

（同时发表于2026年4月27日每日采集）

> 近几十年欧洲水文气候发生了显著变化，包括夏季广泛干旱，但其时空变异性和潜在驱动因素仍不确定。本文提出了欧洲末千年数据同化（EULMDA），一种涵盖过去千年的欧洲水文气候及其主要驱动因素的新重建。EULMDA整合了五个地球系统模型模拟和古气候代用记录，揭示了斯堪的纳维亚大气模式和温度变化如何塑造欧洲夏季干旱。

---

## 河流过程、数据集与冰冻圈

新数据集和方法学进展为本周出版物增色。Gagliano等人发布了基于Sentinel-1 SAR的2015–2024年全球高分辨率融雪径流起始时间数据集，填补了冰冻圈监测的关键空白。Jones等人贡献了Caravan-Qual，将河流水质观测整合到广泛使用的Caravan大样本水文数据集中。Legleiter和Kinzel利用全国横截面数据库评估了常见的河道几何近似方法，对大尺度河流汇流和水力建模具有重要意义。

### A Global High-Resolution Dataset of Snowmelt Runoff Onset Timing from Sentinel-1 SAR, 2015–2024

**作者**: Eric Gagliano, David Shean, Scott Henderson

**期刊**: *ESSD* · **DOI**: [10.5194/essd-2026-216](https://doi.org/10.5194/essd-2026-216) · **引用**: 0

**匹配主题**: runoff, streamflow
{: .label .label-green }

> 融雪径流起始时间是一个关键的水文参数，尤其在山区，季节性积雪作为下游水资源的天然水库。尽管如此，复杂地形上融雪径流起始的高分辨率观测仍然有限。本研究利用Sentinel-1 SAR生成了2015–2024年全球高分辨率数据集。

---

### Caravan-Qual: A Global Scale Integration of Stream Water Quality Observations into a Large-Sample Hydrology Dataset

**作者**: Edward R Jones, Frederik Kratzert, Michelle T H van Vliet

**期刊**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07352-7](https://doi.org/10.1038/s41597-026-07352-7) · **引用**: 0

**匹配主题**: hydrology, streamflow, surface water
{: .label .label-green }

> 保护和改善地表水质量取决于理解物理、生物和化学条件的趋势、空间格局及其潜在驱动因素。这需要跨越多种水质成分的观测数据，以及流域属性的背景信息。Caravan-Qual在全球尺度上将河流水质观测整合到Caravan大样本水文数据集中。

---

### Evaluating Approximations of River Channel Shape Using a National Cross‐Section Database

**作者**: C.J. Legleiter, P. J. Kinzel

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041177](https://doi.org/10.1029/2025wr041177) · **引用**: 0

**匹配主题**: river, streamflow
{: .label .label-green }

> 许多水文应用需要河道大小和形状的基本信息，但野外或遥感测量横截面几何既昂贵又常常只能提供部分覆盖。鉴于这些挑战，本研究利用46,971个测站横截面的现有数据集，评估了各种河道形状近似方法，对河流汇流和水力建模具有重要意义。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库 | 2 |
| 检索主题 | 16 |
| 获取论文总数 | 1427 |
| 去重后 | 1206 |
| 屏蔽期刊过滤后 | 1149 |
| LLM相关性筛选后 | 30 |
| 拒绝（不相关） | 1119 |

### 各期刊论文数

| 期刊 | 篇数 |
|:-----|-----:|
| Water Resources Research | 13 |
| Hydrological Processes | 2 |
| Scientific Reports | 2 |
| Journal of Hydrology | 2 |
| EGUsphere | 3 |
| Journal of Hydrometeorology | 2 |
| Nature Communications | 1 |
| Earth's Future | 1 |
| Remote Sensing of Environment | 1 |
| Journal of Advances in Modeling Earth Systems | 1 |
| Hydrology and Earth System Sciences | 1 |
| Environmental Modelling & Software | 1 |
| Modeling Earth Systems and Environment | 1 |
| Engineering Applications of Artificial Intelligence | 1 |
| Scientific Data | 1 |
| ESSD | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

---
layout: default
title: "第26周（6月23日 - 6月30日），29篇"
nav_order: 37
nav_exclude: true
lang: zh
lang_link: /2026/june/2026-06-30-weekly-review
date: 2026-06-30
categories: [weekly-zh, 2026, june]
tags: [hydrology, literature-review, research]
paper_count: 29
highlight: "提示词条件化的大语言模型径流预测框架与SWOT+SMAP融合无资料流域率定，引领本周人工智能驱动水文学前沿。"
---

# 每周文献综述
{: .no_toc }

**第26周** · 2026年6月23日–6月30日
{: .text-grey-dk-000 }

跨 **6** 个主题共找到 **29** 篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

本周关键词检索（2026年6月23–30日）跨Semantic Scholar和OpenAlex两个数据库，共筛选出29篇高质量论文，涵盖机器学习、水文模型评估、陆面模型、洪旱灾害及观测数据集等方向。最值得关注的方法进展是一种提示词条件化多模态框架，将大语言模型骨架与径流预测轻量化适配相结合。同样显著的是，一项全美大陆尺度研究揭示雨雪混合事件对洪峰径流的贡献远超以往认知；Water Resources Research还发表了一项利用SWOT河道流量与SMAP土壤湿度协同约束陆面模型的方法，在无资料流域实现了有效参数率定。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 人工智能与机器学习径流预测

本周深度学习论文从三个方向推进前沿：径流不确定性量化、面向水文的基础模型及利用径流空间相关性改进数据同化。Arganis-Juárez与Preciado系统梳理了从早期ANN/SVM到现代物理信息深度学习与符号回归的方法演进。Timilsina与Passalacqua（WRR）发现径流空间相关长度在暴雨事件中系统性增大，并将这一物理先验纳入数据同化框架，显著提升了河网预测精度。Li等（J. Hydrology）提出最具创新性的架构：利用自然语言提示词对输入元数据进行条件化，使单一模型能够以极低成本适配不同流域与季节。

### A methodological review of AI/ML and evolutionary computation in hydrology and hydraulics: from ANN/SVM to deep learning, symbolic regression, and physics-informed models

**作者**: M. Arganis-Juárez, M. Preciado

**期刊**: *Water Science & Technology* · **DOI**: [10.2166/wst.2026.304](https://doi.org/10.2166/wst.2026.304) · **引用数**: 0

**匹配主题**: hydrology, streamflow
{: .label .label-green }

> 本文展示了水文数据输入、预处理、人工智能模型及结合水文知识与机器学习的物理信息混合模块工作流程示意图。综述追溯了从传统ANN/SVM方法到集成学习、深度学习（LSTM、Transformer）、符号回归及物理信息神经网络的演进历程，评估了各方法在业务水文中的优势、局限与开放挑战。

---

### Improving Daily Runoff Prediction Using a Novel Two‐Step Post‐Processing Method of Frequency Distribution Curve Correction

**作者**: Xiaochuan LUO, Yongyong Zhang, Tongtiegang Zhao, Xiaoyan Zhai, Junxu Chen, Bo Han et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041637](https://doi.org/10.1029/2025wr041637) · **引用数**: 0

**匹配主题**: runoff
{: .label .label-green }

> 水文模型的系统偏差和频率分布不匹配是日径流预测精度下降的两大主要误差源。本文提出两步后处理方法：首先校正频率分布曲线中的系统偏差，再进行残差修正，在多个不同气候区流域的日径流预测中均取得明显改善。

---

### Streamflow Spatial Correlation Length Increases During Storms and Its Application in Data Assimilation Improves Streamflow Predictions

**作者**: Sujana Timilsina, Paola Passalacqua

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr043053](https://doi.org/10.1029/2025wr043053) · **引用数**: 0

**匹配主题**: streamflow
{: .label .label-green }

> 径流空间相关性反映了河网中不同位置流量的相互关联及下游响应规律。本研究分析了径流的空间相关结构，发现相关长度在暴雨事件中系统性增大。将这一动态空间结构引入数据同化框架后，河网整体径流预测精度显著提升。

---

### A deep learning-based probabilistic framework for streamflow prediction and water quality assessment

**作者**: Alberto Mena, Rafael J. Bergillos, Javier Paredes-Arquiola, Gerald Corzo, Abel Solera, Joaquín Andreu

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135934](https://doi.org/10.1016/j.jhydrol.2026.135934) · **引用数**: 0

**匹配主题**: streamflow
{: .label .label-green }

> 本文提出一套支持河流盆地水质评估与监管合规分析的综合建模框架，将基于深度学习的概率径流预测与下游水质建模相结合，在数据匮乏环境中实现不确定性感知的监管决策支持。

---

### A prompt-conditioned multimodal framework for streamflow prediction with lightweight task adaptation

**作者**: Xudong Li, Senchang Hu, Wei Zhang, Wuyou Xiao, Wenzhuo Shi, Jiaqi Ruan et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135915](https://doi.org/10.1016/j.jhydrol.2026.135915) · **引用数**: 0

**匹配主题**: streamflow
{: .label .label-green }

> 暂无摘要。

---

## 水文模型开发与评估

本周多模型集成与比较研究占据重要位置。Thébault等（HESS）开展了迄今最系统的全美大陆径流模拟比较，发现多模型组合策略在各气候区均优于"拼图"式单一最优模型选取。Weligamage等（HESS）引入"实际蒸散发特征值"概念，为遥感ET产品偏差诊断提供了与流量特征值体系类比的新工具。Kong等（ERL）揭示陆地水分可利用量预估对模型分辨率高度敏感，这种敏感性通过径流与土壤水两条独立路径传导，对干旱风险评估具有重要方法论意义。Yassin等（Hydrological Processes）量化了降水相态划分方法对寒冷地区大尺度水文预估的影响——这一方法论盲区在多模型集成研究中长期被忽视。

### Navigating Climate Adaptation Boundaries for the World's Largest Inter‐Basin Water Transfer Projects

**作者**: Yu Li, Xiang Fu, Zhipeng Fan, Zhao Xiaodan, Yi Zheng

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041103](https://doi.org/10.1029/2025wr041103) · **引用数**: 0

**匹配主题**: hydrology, streamflow
{: .label .label-green }

> 随着全球气候变化与人类活动影响加剧，对径流的影响日益成为水安全的关键问题。本研究分析了未来情景预测对跨流域调水工程的水文影响，识别出现有设计失效的"适应边界"阈值，并评估了长期水安全保障的替代策略。

---

### Assessing deficiencies in remotely sensed actual evapotranspiration (AET): introducing AET signatures

**作者**: Hansini Gardiya Weligamage, Keirnan Fowler, Margarita Saft, Tim Peterson, Dongryeol Ryu, Murray Peel

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4057-2026](https://doi.org/10.5194/hess-30-4057-2026) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 水文特征值是量化和推断水文过程行为的统计指标，但非径流变量（尤其是实际蒸散发）的特征值研究尚不充分。本文引入AET特征值体系，并将其应用于多种遥感ET产品的系统评估，揭示了现有产品在季节动态和水分限制区表征方面的系统性缺陷。

---

### Comparing multi-model mosaic and multi-model combination methods to simulate streamflow across the contiguous USA

**作者**: Cyril Thébault, Wouter Knoben, Nans Addor, Andrew J. Newman, Diana Spieler, Nicolás Vasquéz et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-3945-2026](https://doi.org/10.5194/hess-30-3945-2026) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 准确预测径流是水资源管理、洪水防御和行业规划的基础。传统方法通常依赖专家判断或区域性能选取单一模型。本研究在全美大陆系统比较了多模型拼图策略与集成组合方法，发现组合方法在各气候区均优于拼图策略及任何单一模型。

---

### Variability of land water availability sensitivity to model resolution: Disentangling the influences of runoff and soil water

**作者**: Xianghui Kong, Aihui Wang, He Zhang, Kece Fei, Nan Wei, Duoying Ji et al.

**期刊**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae83cd](https://doi.org/10.1088/1748-9326/ae83cd) · **引用数**: 0

**匹配主题**: runoff, land surface model
{: .label .label-green }

> 陆地水分可利用量（降水与蒸散发之差）的波动可增加干旱风险并广泛影响水资源管理。本研究分离了径流和土壤水两条路径对陆地水分可利用量对模型分辨率敏感性的独立贡献，证明分辨率选择会在干旱风险预估中引入具有空间结构的系统性偏差。

---

### Sensitivity of Large‐Scale Hydrological Predictions to Precipitation Phase Partitioning Methods Under a Changing Climate

**作者**: Fuad Yassin, John W. Pomeroy, Alain Pietroniro, Bruce Davison, Mohamed Elshamy, Zelalem Tesemma

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70608](https://doi.org/10.1002/hyp.70608) · **引用数**: 0

**匹配主题**: streamflow
{: .label .label-green }

> 降水相态（雨雪）划分的准确性是寒冷地区水文预估的主要不确定性来源之一。本研究量化了四种降水相态划分方法对气候变化情景下大尺度水文预估的影响，揭示方法选择可导致径流未来轨迹出现显著差异，而这一误差源在多模型集成研究中长期被忽视。

---

## 陆面模型与地球系统模型

遥感与陆面建模进展本周涵盖无资料流域率定、模型-观测分歧诊断、碳循环反馈及植被强迫数据集等方向。Crow等（WRR）首次证明联合同化SWOT河道流量与SMAP表层土壤湿度能有效约束陆面模型中的系统性偏差。Tavakoli等诊断了MPAS-NoahMP在不同土壤湿度区间的蒸发模拟与观测的系统性分歧，对使用MPAS耦合构型的研究者具有直接参考价值。Tiengou等（ESD）利用IPSL耦合气候模式（ICOLMDZ-ORCHIDEE）在伊比利亚半岛开展显式灌溉模拟，量化了局地大气反馈和对下游水量平衡的扰动——为在E3SM或ELM框架下开展类似实验提供了清晰参照。Bauer等（GMD）正式发布MESMER v1.0.0，作为具有版本管理的研究软件包提供给社区使用。

### Streamflow Calibration in Ungauged Basins Using SWOT Discharge and SMAP Surface Soil Moisture Products

**作者**: Wade T. Crow, Michael Durand, Stephen Coss, Rolf H. Reichle

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041875](https://doi.org/10.1029/2025wr041875) · **引用数**: 0

**匹配主题**: streamflow, land surface model
{: .label .label-green }

> 利用陆地遥感降低陆面模型随机误差的研究已取得重要进展，但处理系统性偏差方面进展有限。本研究证明，联合同化SWOT流量与SMAP表层土壤湿度能有效约束陆面模型在无资料流域中的系统性偏差，为全球尺度水文预测开辟了新路径。

---

### Diagnosis of Evaporation–Soil Moisture Regimes in MPAS-NoahMP: What conditions lead to disagreement with observations?

**作者**: Nazanin Tavakoli, Paul A. Dirmeyer, Zhe Zhang, Cenlin He, Megan D. Fowler

**期刊**: *ESSOAr预印本* · **DOI**: [10.22541/essoar.15005158/v1](https://doi.org/10.22541/essoar.15005158/v1) · **引用数**: 0

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 多项研究利用地球系统模型刻画土壤湿度区间——陆气相互作用的重要指示量，但模型与观测之间仍存在显著的空间偏差。本研究诊断了MPAS-NoahMP蒸发与土壤湿度区间分类偏离观测的条件，定位了模型耦合假设的失效边界。

---

### Northern high latitudes could become a net carbon source below 2 °C global warming

**作者**: Rebecca Varney, Daniel Hooke, Norman Julius Steinert, T. Luke Smallman, Camilla Mathison, Eleanor Burke

**期刊**: *Earth System Dynamics* · **DOI**: [10.5194/esd-17-913-2026](https://doi.org/10.5194/esd-17-913-2026) · **引用数**: 0

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 历史增温期间，北半球高纬度陆地生态系统一直是净碳汇，为缓解人为CO₂排放提供了重要支撑。然而本研究预测，即使全球升温低于2°C，北高纬陆地生态系统也可能因土壤碳分解速率超过植被吸收而转变为净碳源——对陆面模型碳循环参数化具有直接影响。

---

### Global Snow-free Leaf Area Index Dataset 1985–2020 for Earth System Modeling

**作者**: Wanyi Lin, Hua Yuan, Wenzong Dong, Zhuo Liu, Jiayi Xiang, Yongjiu Dai

**期刊**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07677-3](https://doi.org/10.1038/s41597-026-07677-3) · **引用数**: 0

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 叶面积指数（LAI）是连接植被结构与地球系统模型中地表能量和碳交换的基本参数，但积雪污染导致LAI低估问题长期存在。本数据集提供1985–2020年全球逐年去积雪污染LAI时间序列，分辨率一致，适用于地球系统模型强迫与评估。

---

### Regional impacts of irrigation on the atmospheric and terrestrial water cycle of the Iberian Peninsula in a climate model

**作者**: Pierre Tiengou, Agnès Ducharne, Frédérique Cheruy

**期刊**: *Earth System Dynamics* · **DOI**: [10.5194/esd-17-843-2026](https://doi.org/10.5194/esd-17-843-2026) · **引用数**: 0

**匹配主题**: land surface model, irrigation
{: .label .label-green }

> 本研究利用IPSL气候模式的大气（ICOLMDZ）和陆面（ORCHIDEE）耦合组件，对伊比利亚半岛2010–2022年进行区域显式灌溉模拟。结果显示，灌溉在局地产生可测量的大气降温和增湿效应，同时减少地下水补给并改变灌溉流域河道流量的季节节律。

---

### MESMER v1.0.0: consolidating the modular Earth system model emulator into a sustainable research software package

**作者**: Victoria M. Bauer, M. Hauser, Y. Quilcaille, Sarah Schöngart, L. Gudmundsson, S. Seneviratne

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-5669-2026](https://doi.org/10.5194/gmd-19-5669-2026) · **引用数**: 1

**匹配主题**: earth system model
{: .label .label-green }

> 本文发布MESMER v1.0.0——模块化地球系统模型空间解析输出模拟器的正式版本。MESMER是基于统计模式缩放的空间解析气候模拟综合软件包，能够以远低于完整ESM运算的代价快速生成情景一致的气候实现集合。

---

## 洪水过程与风险

本周洪水研究从过程理解到风险量化均有重要进展。Reis等（WRR）揭示雨雪混合事件驱动洪峰的地理范围远超以往认知，对历史上忽视此机制而率定的洪水频率分析和基础设施设计标准具有重要影响。Tramblay等（J. Hydrology）利用法国逐小时流量记录，分离了洪峰与洪量趋势并归因于不同产流机制——这是日数据分析无法实现的区分。Baer等（npj Natural Hazards）证明标准设计暴雨假设因忽视降雨时空结构而系统性错估洪水风险，且该误差沿风险评估链逐级放大。Varghese等（Hydrological Processes）追踪了季风变率与半干旱流域洪水产流之间的水文路径。

### Monsoon‐Driven Hydrological Pathways of Flood Generation in Semi‐Arid River Basins

**作者**: Roma Varghese, Jasti S. Chowdary, C. Gnanaseelan

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70622](https://doi.org/10.1002/hyp.70622) · **引用数**: 0

**匹配主题**: river, flood
{: .label .label-green }

> 半干旱河流系统的流域尺度洪水产流过程尚不明确，制约了在季风气候日益多变背景下的有效流域管理。本研究追踪了印度半干旱河流流域从季风降雨到流域尺度洪水响应的主导水文路径，识别了饱和产流、超渗产流与直接降水产流各自的主导区域及其随前期条件的变化规律。

---

### Rain‐on‐Snow Events Frequently Drive Peak Streamflow Across the Contiguous United States

**作者**: Wyatt Reis, Jeremy Giovando, Michael Bartles, Travis Dahl

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042253](https://doi.org/10.1029/2025wr042253) · **引用数**: 0

**匹配主题**: streamflow
{: .label .label-green }

> 雨雪混合事件是指降雨落在成熟积雪上，引发迅速融雪并可能导致极端洪水的过程。本研究发现，雨雪混合事件驱动洪峰在全美大陆的发生频率远超以往记录，对传统洪水频率分析和以往假定以降雨为主的地区基础设施设计标准具有重要影响。

---

### Impact of floods on surface water quality: a systematic review and comprehensive assessment

**作者**: Apoorva Bamal, Galal Uddin, Reza Ahmadian, Marcelo Gomes Miguez, Agnieszka I. Olbert

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135916](https://doi.org/10.1016/j.jhydrol.2026.135916) · **引用数**: 0

**匹配主题**: flood, surface water
{: .label .label-green }

> 洪水作为极端流量事件，是代价最高且破坏性最强的自然灾害之一。在洪水影响的众多领域中，地表水水质恶化受到的系统性关注有限。本综述系统梳理洪水对地表水水质在化学、微生物和物理维度影响的证据，识别知识空白并总结新兴监测方法。

---

### Neglecting spatiotemporal rainfall variability misrepresents flood hazard and risk

**作者**: John Baer, Antonia Sebastian, Lauren Grimley, James Doss-Gollin, Daniel B. Wright, Mohammad Ashar Hussain et al.

**期刊**: *npj Natural Hazards* · **DOI**: [10.1038/s44304-026-00208-5](https://doi.org/10.1038/s44304-026-00208-5) · **引用数**: 0

**匹配主题**: flood
{: .label .label-green }

> 洪水风险评估是全球洪水管理（包括土地利用规划、基础设施设计和保险需求）的基础。许多评估依赖将降雨视为空间均匀、时间简化的设计暴雨。本研究证明，忽视降雨时空变异性会系统性错估洪水危害和下游风险，且误差沿整个风险评估链传播放大。

---

### Regional process-based analysis of trends in flood peaks and volumes using hourly data

**作者**: Yves Tramblay, Patrick Arnaud, Pierre Javelle

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135949](https://doi.org/10.1016/j.jhydrol.2026.135949) · **引用数**: 0

**匹配主题**: flood
{: .label .label-green }

> 大多数洪水趋势研究依赖站点尺度的日流量数据，限制了其区分不同产流机制中相互对立趋势的能力，在地中海气候区尤为突出（短历时强降水驱动大多数洪峰）。本研究利用法国逐小时流量数据，将洪峰趋势与洪量趋势分离并归因于不同过程变化，揭示了日数据分析中无法识别的对立趋势。

---

## 干旱与气候变化对径流的影响

干旱研究本周涵盖全球数据集、归因研究与冰川流域水文学。Šťovíček等（Scientific Data）发布了迄今最全面的全球干旱事件数据集——以时空聚类事件而非点位为基本单元——为趋势检测和模型评估提供了社区共享资源。Zahedi等（WRR）探究干旱后降雨-径流关系为何在部分流域发生且永久不恢复，发现前期流域湿润程度是决定响应路径的状态变量，揭示了模型处理水文迟滞性时的深层挑战。Wang等（ERL）将2024–2025年华南创纪录冬春干旱归因于特定环流异常，展示了高分辨率过程理解如何为近期干旱预测提供支撑。

### A global dataset of spatiotemporal drought events from reanalysis and hydrological model data for 1980–2024

**作者**: Vít Šťovíček, Martin Hanel, Rohini Kumar, Vojtěch Moravec, Yannis Markonis, Carmelo Cammalleri et al.

**期刊**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07750-x](https://doi.org/10.1038/s41597-026-07750-x) · **引用数**: 0

**匹配主题**: hydrology, hydrologic model, runoff
{: .label .label-green }

> 本文发布1980–2024年全球时空聚类干旱事件数据集，基于逐日降水、潜在蒸散发、土壤湿度和地表径流数据生成。干旱事件被识别为空间连续且时间持续的异常体，能够追踪干旱的起始、传播与消退过程——相对传统点位干旱指数是重要方法进步。

---

### Warming-driven runoff increase and shifted seasonality in the glacierized Hotan Basin in Central Asia

**作者**: Xiaoqian Xu, Wen Wang, Pinxuan Zhou

**期刊**: *Global and Planetary Change* · **DOI**: [10.1016/j.gloplacha.2026.105579](https://doi.org/10.1016/j.gloplacha.2026.105579) · **引用数**: 0

**匹配主题**: runoff, seasonal
{: .label .label-green }

> 暂无摘要。

---

### Does Antecedent Catchment Wetness Explain the Timing of Rainfall‐Runoff Relationship Shifts?

**作者**: Sina Zahedi, Tim Peterson, Murray Peel

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2024wr039750](https://doi.org/10.1029/2024wr039750) · **引用数**: 0

**匹配主题**: runoff
{: .label .label-green }

> 已有研究表明年降雨-径流关系在干旱期间发生偏移，且在许多流域难以恢复，导致单位降水产流量低于干旱前水平。本研究探究前期流域湿润程度是否能解释偏移发生的时机，发现从更干燥前期状态进入干旱的流域更可能经历永久性产流变化——表明初始条件决定了难以恢复的迟滞路径。

---

### Mechanisms of the Record-Breaking Winter-Spring Drought over South China in 2024-2025

**作者**: Leying Wang, Wen Chen, Shangfeng Chen, Zhibiao Wang

**期刊**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae8461](https://doi.org/10.1088/1748-9326/ae8461) · **引用数**: 0

**匹配主题**: drought
{: .label .label-green }

> 华南地区经历了2024/2025年前所未有的冬春持续干旱，从11月延续至4月，是过去六十年最严重的干旱事件。本研究识别了维持跨季节过渡期干旱的主导大尺度环流型与SST异常，为改进华南季节干旱预测提供了机制基础。

---

### Assessing structural uncertainty in water–human systems: A multi-model ensemble approach for agricultural water management

**作者**: Héctor González-López, Arthur Hrast Essenfelder, Francesco Sapino, David Rivas-Tabares, Jose María Bodoque, Dioni Perez-Blanco

**期刊**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2026.110582](https://doi.org/10.1016/j.agwat.2026.110582) · **引用数**: 0

**匹配主题**: hydrologic model, water management
{: .label .label-green }

> 水文-经济耦合模型日益广泛用于支持农业水管理决策，但模型结果对人类系统和水系统组分中的结构（模型形式）选择高度敏感。本研究通过多模型集成显式量化结构不确定性，证明其在某些情形下可与参数不确定性相当，并对灌溉用水分配政策结论产生实质影响。

---

## 观测数据集、遥感与水资源管理

本周新发布三个高分辨率数据集，分别填补了强迫场与评估基础设施的不同空缺。Madakumbura等（Scientific Data）发布WHiLD-HM——覆盖美国西部74年、4公里分辨率逐日水文气象数据集，是迄今能分辨山区流域过程的最长时间序列。Xu等（Scientific Data）发布3DVAR-MF-XJ，通过站点观测同化显著修正了ERA5等全球再分析产品在新疆复杂地形上的系统偏差。Arnold等（Nature Water）将Atkinson福利函数直接纳入跨境水资源优化目标，证明跨境河流系统中公平与效率的权衡可以得到更显式的量化与调控。*(注：本文同时收录于2026-06-24每日采集。)*

### A 4-km long-term (1952–2025) daily hydrometeorological dataset for the western United States

**作者**: Gavin D. Madakumbura, Ronnie Abolafia‐Rosenzweig, Cenlin He, Jacob Jones, Qian He, Menaka Revel et al.

**期刊**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07642-0](https://doi.org/10.1038/s41597-026-07642-0) · **引用数**: 0

**匹配主题**: streamflow, land surface model
{: .label .label-green }

> 本研究发布美国西部高分辨率长时序水文气象数据集（WHiLD-HM），提供1952–2025年4公里分辨率、时空连续的逐日数据。数据集融合动力降尺度与观测校正，提供适用于水文建模、陆面模型强迫和气候变化归因的降水、气温、风速、湿度和辐射场。

---

### A high-resolution near-surface meteorological forcing dataset for arid Xinjiang (3DVAR-MF-XJ)

**作者**: Yan Xu, Liang Zhang, Hui Wang, Dongge Ning, Mengxin Bai, Xueping Cong et al.

**期刊**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07573-w](https://doi.org/10.1038/s41597-026-07573-w) · **引用数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 新疆水文气候评估受稀疏观测、复杂地形和广泛使用网格化再分析产品系统偏差的制约。本文发布三维变分新疆气象强迫数据集（3DVAR-MF-XJ），通过将站点观测同化入区域模式框架，与ERA5和CMFD相比显著降低了高程相关偏差。

---

### Balancing equity and efficiency in transboundary water systems with Atkinson's welfare function

**作者**: Wyatt Arnold, Matteo Giuliani, Andrea Castelletti

**期刊**: *Nature Water* · **DOI**: [10.1038/s44221-026-00671-4](https://doi.org/10.1038/s44221-026-00671-4) · **引用数**: 0

**匹配主题**: hydropower
{: .label .label-green }

*(同时收录于2026-06-24每日采集)*

> 水资源优化传统上以系统整体效率为目标，将分配公平置于次要地位。本文提出一个将公平性通过Atkinson福利函数直接纳入优化目标的框架，证明跨境河流系统中公平与效率的权衡可以更显式地量化——且在多数情形下，实现公平改善所需的效率牺牲相当有限。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 搜索数据库数 | 2 |
| 搜索主题数 | 16 |
| 获取论文总数 | 907 |
| 去重后 | 771 |
| LLM相关性筛选后 | 29 |
| 被拒绝（不相关） | 742 |

### 按期刊分类

| 期刊 | 论文数 |
|:-----|-------:|
| Water Resources Research | 7 |
| Scientific Data | 5 |
| Journal of Hydrology | 3 |
| Hydrology and Earth System Sciences | 2 |
| Hydrological Processes | 2 |
| Earth System Dynamics | 2 |
| Environmental Research Letters | 2 |
| Global and Planetary Change | 1 |
| Agricultural Water Management | 1 |
| Geoscientific Model Development | 1 |
| Nature Water | 1 |
| npj Natural Hazards | 1 |
| Water Science & Technology | 1 |
| ESSOAr预印本 | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

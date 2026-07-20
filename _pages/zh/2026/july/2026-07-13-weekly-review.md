---
layout: default
title: "第28周（7月6日 - 7月13日），28篇"
nav_order: 34
nav_exclude: true
lang: zh
lang_link: /2026/july/2026-07-13-weekly-review
date: 2026-07-13
categories: [weekly-zh, 2026, july]
tags: [hydrology, literature-review, research]
paper_count: 28
highlight: "美国洪水风险正向小型河流转移，而物理信息神经网络和自监督机器学习方法正推动无资料流域径流预测取得新进展。"
---

# 每周文献综述
{: .no_toc }

**第28周** · 2026年7月6日—13日
{: .text-grey-dk-000 }

在 **6** 个主题中发现 **28** 篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

本周综述涵盖了使水文模型物理一致性更强、数据利用效率更高的系列进展：HESS上发表的统一径流方案消弭了饱和超渗与入渗超渗机制之间的长期分隔，基于SIF约束的陆面建模和紧凑地球系统模拟器则弥合了蒸散发与作物产量代表性的系统偏差。在风险层面，一项刊登于Nature Sustainability的研究预测，美国洪水暴露风险将日益集中于小型河流附近——这是当前联邦洪水保险和基础设施投资中极度被忽视的盲区；而GRL的一项研究证实，即使在飓风情景下，城市以外的农村径流对沿海城市复合洪水的贡献也可能超过风暴潮本身。两个新的大样本数据集（CAMELS-FI，覆盖320个芬兰流域；基于地球观测的全球0.25°灌溉用水量档案）为大尺度水文模型基准测试奠定了更坚实的基础。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 水文过程模拟

本周过程模拟文献以径流产生机制、土壤物理过程和水文连通性的基础性进展为特色。Hong等发表于HESS的研究通过统一参数化框架将饱和超渗和入渗超渗两种机制整合为一，减少了跨尺度模型的结构性不确定性。Medvedev等将TerM陆面模型应用于俄罗斯欧洲部分的两条大型河流（维切格达河和奥卡河），验证了其在当代气候条件下模拟主要水量平衡分量和径流的能力，为欧亚河流模型提供了重要基准。Zhang等利用高频水文和示踪剂数据量化喀斯特坡面的水文连通性路径，揭示了地下流路由的强烈季节性，对喀斯特含水层补给模拟具有重要意义。Yu等探讨了土壤滞后性对季节性冻土中液态水-气态水-空气耦合流动的影响，这是寒区陆面模型中通常被忽略的过程。Qin等证明，在89个天山山地流域中，稳定的融雪补给（而非降雨变率）主导了年际径流稳定性，对中亚水资源预估有直接意义。

### A unified scheme for modeling saturation and infiltration excess runoff

**作者**: Yuanqi Hong, Guta Wakbulcho Abeshu, Hong-Yi Li et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4293-2026](https://doi.org/10.5194/hess-30-4293-2026) · **引用次数**: 0

**匹配主题**: hydrologic model, runoff, streamflow
{: .label .label-green }

> 饱和超渗和入渗超渗是控制流域及更大尺度径流时序和量级的两种主要地表产流机制。尽管二者在流域内频繁共存并相互关联，现有产流方案大多将其分开处理。本研究提出了一种统一方案，在单一参数化框架内同时表征两种机制，减少了结构性不确定性，并在不同气候区均提升了径流模拟精度。

---

### Simulation of the water regime of two large European Russia rivers under the conditions of modern climate

**作者**: A. I. Medvedev, V. M. Stepanenko, A. A. Ryazanova

**期刊**: *Geography, Environment, Sustainability* · **DOI**: [10.24057/2071-9388-2026-4234](https://doi.org/10.24057/2071-9388-2026-4234) · **引用次数**: 1

**匹配主题**: hydrology, hydrologic model, river, runoff, water management, land surface model, surface water, earth system model
{: .label .label-green }

> 本文将TerM陆面模型应用于俄罗斯欧洲部分的典型流域（维切格达河、奥卡河），以当代气候条件再现其水文情势。研究评估了TerM模型对水量平衡主要分量和径流过程的模拟质量，为欧亚河流建模应用提供了参考基准。

---

### Effect of soil hysteresis on liquid-vapor-air flow in seasonally frozen soils

**作者**: Lianyu Yu, Huanjie Cai, Delan Zhu et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.136002](https://doi.org/10.1016/j.jhydrol.2026.136002) · **引用次数**: 0

**匹配主题**: hydrology, seasonal
{: .label .label-green }

> 本研究探讨土壤水分保持特性中的滞后效应如何影响季节性冻土中液态水、气态水和空气的耦合运动。滞后效应导致湿润和干燥路径存在差异，显著改变入渗、冻融动态和近地表水力状态——这一过程在寒区陆面模型中普遍被忽视。

---

### Spatiotemporal hydrological connectivity on karst hillslopes: Insights from high-frequency monitoring

**作者**: Yutong Zhang, Jun Zhang, Fang Wang, Jinjiao Lian et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135982](https://doi.org/10.1016/j.jhydrol.2026.135982) · **引用次数**: 0

**匹配主题**: hydrologic model
{: .label .label-green }

> 利用高频水文和地球化学监测数据，本研究刻画了喀斯特坡面水文连通性路径在时空上的变化规律。结果揭示了地表流、土壤流与管道流主导性的强烈季节性切换，对喀斯特含水层补给估算和分布式模型中优先流参数化具有重要意义。

---

### Stable snowmelt supply dominates enhanced runoff stability in the Tianshan Mountains of Central Asia

**作者**: Xueyan Qin, Xiuliang Yuan, Rafiq Hamdi, Jie Bai et al.

**期刊**: *Journal of Hydrology: Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103729](https://doi.org/10.1016/j.ejrh.2026.103729) · **引用次数**: 0

**匹配主题**: runoff, streamflow
{: .label .label-green }

> 对天山山地89个流域的分析表明，稳定的融雪补给（而非降雨变率）是年际径流规律性的主要驱动因素。在全球变暖情境下，冰川消融的增加可能在"峰值水"拐点到来之前暂时维持这种稳定性，这对中亚下游水资源保障具有重大影响。

---

## 陆面与地球系统模拟

本周三篇论文分别在陆面模型过程真实性和紧凑型地球系统模拟方面取得重要进展。Gemechu等将太阳诱导荧光（SIF）作为约束集成到Noah-MP中，纠正了陆面模型在水分限制生态系统中系统性高估蒸散发的问题，显著改善了干旱胁迫表征——与E3SM/ELM在干旱区的率定直接相关。Stacey等指出，全球水资源短缺评估中普遍存在一个疏漏：大多数研究忽视了植物对CO₂浓度升高的生理响应（气孔导度降低），而这一机制可在大尺度上减少蒸腾需求，部分抵消预估的水资源短缺。Liu等则提出一个集成于紧凑型地球系统模型OSCAR的次国家尺度作物产量模拟器，填补了耦合人类-气候反馈建模中的关键缺口。

### A SIF-constrained Noah-MP land surface model for simulating water use efficiency and drought

**作者**: Tewekel Melese Gemechu, Haitao Zhang, J. F. Sun et al.

**期刊**: *International Journal of Applied Earth Observation and Geoinformation* · **DOI**: [10.1016/j.jag.2026.105460](https://doi.org/10.1016/j.jag.2026.105460) · **引用次数**: 0

**匹配主题**: land surface model, surface water
{: .label .label-green }

> 由于植物生理水分胁迫表征不足，陆面模型在水分限制生态系统中系统性高估蒸散发。本研究将太阳诱导荧光（SIF）作为机理性约束集成到Noah-MP陆面模型中，使模型能够更准确地模拟水分利用效率和干旱胁迫。SIF约束模型在干旱和半干旱地区显著降低了蒸散发偏差，并改善了土壤湿度和径流模拟性能。

---

### Future global water scarcity partially moderated by vegetation responses to rising CO₂

**作者**: Jessica Stacey, Richard Betts, Andrew James Hartley et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4225-2026](https://doi.org/10.5194/hess-30-4225-2026) · **引用次数**: 0

**匹配主题**: streamflow, land surface model, earth system model
{: .label .label-green }

> 大多数未来水资源短缺研究所依赖的水文模型忽略了植物对CO₂浓度升高的生理响应（如气孔导度降低），而这种响应可在大尺度上减少蒸腾、增加水分有效性。通过纳入这一效应的模拟，作者表明CO₂生理强迫可部分缓解预估的全球水资源短缺，但不足以逆转整体趋势——这对基于地球系统模型预测的水资源规划具有重要警示意义。

---

### A food crop yield emulator for integration in the compact Earth system model OSCAR

**作者**: Xinrui Liu, Thomas Gasser, Jianmin Ma, Junfeng Liu et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-5857-2026](https://doi.org/10.5194/gmd-19-5857-2026) · **引用次数**: 0

**匹配主题**: earth system model
{: .label .label-green }

> 本文提出一个次国家尺度的作物产量模拟器，模拟玉米、水稻（两个生长季）、大豆和小麦的产量，设计用于集成到紧凑型地球系统模型OSCAR中。该模拟器经历史观测验证，使耦合人类-气候-粮食反馈的高效多情景评估成为可能——这在以往受限于过程模型的计算成本而难以实现。

---

## 机器学习在径流和流量预测中的应用

本周机器学习水文预测研究沿两条平行路径持续推进：（1）通过将过程知识嵌入神经网络架构提升物理一致性；（2）通过自监督和迁移学习将预测能力延伸至无资料或数据稀缺流域。Lin等为非接触式河道流量估算提出了一种优雅的PINN+CNN框架，将大尺度粒子图像测速（LSPIV）与物理信息神经网络结合，无需传统率定曲线。Zhang等提出一种面向无资料流域的态势感知自监督径流预测方法，利用无标注数据学习水文情势嵌入，再进行细调，显著提升了异质性流域间的可迁移性。Li等解决了一个相关挑战：水库调度和灌溉引水等人类活动在干旱区扭曲了自然径流信号，其双层注意力框架明确纳入了人为驱动因素。Mo等证明，将ECMWF集合降水预报集成到喀斯特流域物理模型中可有效延长有用预报时长。Álvarez Chaves等则提出数据驱动降雨-径流模型的变分不确定性量化框架，可在点预测之外提供标定的置信区间。

### A regime-aware framework for runoff prediction in ungauged basins via self-supervised learning

**作者**: Jiaxing Zhang, Xuemei Liu, Hairui Li, Jiakang Du

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-61333-9](https://doi.org/10.1038/s41598-026-61333-9) · **引用次数**: 0

**匹配主题**: runoff, streamflow
{: .label .label-green }

> 无资料流域径流预测因缺乏流量观测和数据驱动模型在异质水文条件下可迁移性有限而长期面临挑战。本研究提出一种态势感知框架，从水文情势视角利用自监督学习从无标注数据中提取情势嵌入表示，然后针对预测任务进行细调。与标准LSTM基线相比，该方法的跨流域可迁移性显著提升。

---

### Non-contact discharge estimation using physics-informed neural networks and CNN-enhanced image velocimetry

**作者**: Yen-Cheng Lin, C. L. Wu, Hao-Che Ho

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.136015](https://doi.org/10.1016/j.jhydrol.2026.136015) · **引用次数**: 0

**匹配主题**: hydrology
{: .label .label-green }

> 本研究通过将CNN增强的大尺度粒子图像测速（LSPIV）与物理信息神经网络（PINN）相结合，提出了一种非接触式河道流量估算的物理信息框架。该方法从视频图像中提取表面流速场，利用PINN推断水深截面，无需传统率定基础设施即可估算流量，在湍流和图像局部遮挡等复杂野外条件下均表现出高精度。

---

### A mutual information-based dual-layer attention framework for modelling human activity-driven streamflow variability

**作者**: Ziheng Li, Xuefeng Sang, Hao Wang, Yang Zheng et al.

**期刊**: *Hydrological Sciences Journal* · **DOI**: [10.1080/02626667.2026.2685104](https://doi.org/10.1080/02626667.2026.2685104) · **引用次数**: 0

**匹配主题**: hydrology, streamflow
{: .label .label-green }

> 在受人类活动影响且缺乏工程数据的干旱区，准确刻画径流变异性颇具挑战。本研究基于互信息和双层注意力机制提出一种径流变异模拟框架，明确表征水库调节、灌溉取水等人为驱动因素对径流的影响，在受控河流系统中优于纯数据驱动基线。

---

### Improving short-term runoff forecasting in a karst basin: Integrating ECMWF precipitation forecasts with a hydrological model

**作者**: Chongxun Mo, Jiameng Xu, Na Li et al.

**期刊**: *Journal of Water Resources Planning and Management* · **DOI**: [10.1061/jwrmd5.wreng-7200](https://doi.org/10.1061/jwrmd5.wreng-7200) · **引用次数**: 0

**匹配主题**: hydrologic model, runoff
{: .label .label-green }

> 由于喀斯特流域地下水力过程复杂，可靠的短期径流预报长期面临挑战。本研究系统评估了ECMWF、中国气象局（CMA）和韩国气象厅（KMA）三种集合降水预报产品与物理喀斯特水文模型的耦合性能。ECMWF整体表现最优，与仅使用实测降水相比，有效预报时长延长12—24小时，对喀斯特地区洪水预警具有直接业务价值。

---

### A variational approach to uncertainty estimation in data-driven rainfall-runoff modeling

**作者**: Manuel Álvarez Chaves, Eduardo Acuña Espinoza, Daniel Klotz et al.

**期刊**: *Machine Learning: Science and Technology* · **DOI**: [10.1088/3049-4753/ae89ba](https://doi.org/10.1088/3049-4753/ae89ba) · **引用次数**: 0

**匹配主题**: runoff, streamflow
{: .label .label-green }

> 本研究针对数据驱动降雨-径流模型提出了变分推断不确定性量化框架，在点预测之外提供标定的概率预测。该变分方法在不同流域类型和风暴量级下均给出良好的不确定性估计，解决了基于神经水文模型的概率洪水预报系统的关键业务需求。

---

## 洪水风险与预测

本周洪水研究横跨从流域到大陆的多个尺度。Jiang等在Nature Sustainability发表了本周政策相关性最高的研究：利用预估人口增长和未来洪水频率图，证明美国洪水暴露风险将日益集中于小型河流附近——这些河流通常被排除在联邦洪水保险计划和基础设施投资之外。Xu等（GRL）利用地球系统模型对飓风事件的模拟表明，即使存在风暴潮，农村上游径流对沿海城市洪水总量的贡献也可能超过风暴潮本身，从根本上改变了复合洪水驱动因素在沿海城市规划中的权重。Chen和Husic利用同位素数据追踪了美国754个流域四十年来径流组成的系统性转变，发现27%的流域近期降水来源的事件水比例显著增加——这对水质和洪水短促性预估具有深远影响。Rahman等质疑了刚性洪水分类框架（河道洪水/城市积涝/海岸洪水/山洪）在快速城镇化的全球南方城市中的适用性，提出动态、适应性的洪水类型学。Rana等证明，河道网络拓扑指标可作为无资料流域设计洪水的可靠预测因子。

### Future flood risk concentration for residents near small rivers across the USA

**作者**: Ruijie Jiang, Hui Lü, Deliang Chen, Kun Yang et al.

**期刊**: *Nature Sustainability* · **DOI**: [10.1038/s41893-026-01896-7](https://doi.org/10.1038/s41893-026-01896-7) · **引用次数**: 0

**匹配主题**: river, flood
{: .label .label-green }

> 利用气候驱动的洪水频率变化预估与精细人口暴露数据，本研究表明未来美国洪水风险将不成比例地影响小型河流附近居民——这类水道长期被排除在主要洪水基础设施投资和联邦风险制图之外。研究结果揭示了当前基础设施规划和保险框架中对未来洪水负担的系统性低估。

---

### Significant rural contributions to severe coastal urban flooding through flow connectivity

**作者**: Donghui Xu, Gautam Bisht, Dongyu Feng et al.

**期刊**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl122550](https://doi.org/10.1029/2026gl122550) · **引用次数**: 1

**匹配主题**: runoff, flood, earth system model
{: .label .label-green }

（亦收录于2026-07-11每日采集）

> 沿海城市日益受到飓风诱发复合洪水的威胁。然而，降雨-风暴潮耦合与其他洪水驱动因素（如来自周边农村和不透水面的径流）在城市洪水中的相对贡献尚不明确。利用地球系统模型对飓风事件的模拟，本研究发现农村上游径流即便在风暴潮存在的情况下也可主导城市内涝总量，从根本上改变了复合洪水风险评估的构建方式。

---

### Streamflow composition in U.S. rivers is shifting toward recent precipitation

**作者**: Chuqiang Chen, Admin Husic

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03788-2](https://doi.org/10.1038/s43247-026-03788-2) · **引用次数**: 0

**匹配主题**: river, streamflow
{: .label .label-green }

> 近期降水对径流的贡献比例（事件水分数）对水质和洪水风险有深远影响。通过分析754个美国流域近四十年的同位素数据，本研究表明27%的流域事件水比例显著增加——这是首个大陆尺度上径流组成系统性转变的证据。这一趋势在积雪主导和半干旱流域中最为突出，这些流域正经历水文情势转变。

---

### Dynamic flood typologies for urban resilience: Toward equitable and adaptive risk governance

**作者**: Mahfuzur Rahman, Md Anuwer Hossain, Mohammed Benaafi et al.

**期刊**: *Journal of Water Resources Planning and Management* · **DOI**: [10.1061/jwrmd5.wreng-7583](https://doi.org/10.1061/jwrmd5.wreng-7583) · **引用次数**: 0

**匹配主题**: hydrology, flood
{: .label .label-green }

> 传统的洪水分类（河道洪水、城市积涝、海岸洪水、山洪）在应对快速城镇化的全球南方城市洪水风险管理中日益显示出局限性。本研究提出动态、情境特定的洪水类型学，能够捕捉级联、复合和混合洪水行为，并构建了一个适应性治理框架，考虑了城市形态演变、非正规居住模式以及洪水暴露的公平性维度。

---

### Can channel network topology govern prediction of ungauged design floods?

**作者**: Saroj Rana, Amit Kumar Singh, Sagar Rohidas Chavan

**期刊**: *Hydrological Sciences Journal* · **DOI**: [10.1080/02626667.2026.2701309](https://doi.org/10.1080/02626667.2026.2701309) · **引用次数**: 0

**匹配主题**: hydrology, flood
{: .label .label-green }

> 河道网络拓扑（CNT）——流域内部与外部节点的空间布置——可作为无资料地点水文响应的重要预测因子。本研究系统评估CNT指标能否主导无资料流域设计洪水的预测，发现拓扑衍生指标与洪水分位数高度相关，可用于约束没有流量数据地区的区域回归模型。

---

## 水库与水电管理

本周水库运行研究涉及热分层、多水库调度、环境流量和地球化学影响等多个议题。He等在JWRPM提出了深水水库运行中常被忽视的水质问题：垂向热分层导致底层低温出流，抑制鱼类在春夏季的产卵繁殖。其多目标优化框架将积累温度指数纳入生态保护目标，与发电和防洪并列优化。Xie等分析了长江上游38座大型水库（调节库容805亿立方米）对干流和支流径流情势的累积影响，揭示了多水库建设导致的流态均一化趋势。Neupane等为一座喜马拉雅水库优化了环境流量与水电发电的权衡方案，表明智能调度可大幅降低人类与生态用水的冲突。Nie等则证明三峡水库通过流速和停留时间控制调节氮素输送与生物地球化学转化，对下游营养盐收支具有重要意义。

### Multiobjective optimal reservoir operation considering accumulated temperature index for downstream ecology

**作者**: Wei He, Jinyaxuan Huang, Liancong Luo et al.

**期刊**: *Journal of Water Resources Planning and Management* · **DOI**: [10.1061/jwrmd5.wreng-7340](https://doi.org/10.1061/jwrmd5.wreng-7340) · **引用次数**: 0

**匹配主题**: reservoir, hydropower
{: .label .label-green }

> 深水水库的垂向热分层导致出流温度偏低，在春夏两季抑制下游鱼类繁殖。本研究提出将积累温度指数（ATI）作为生物学目标纳入多目标优化框架，与发电量和防洪并列求解帕累托最优解。结果表明，适度的运行调整可在不显著降低水电出力的情况下大幅改善鱼类繁殖的热力条件。

---

### Flow regime alteration under progressive multi-reservoir development in the Upper Yangtze River

**作者**: Zaichao Xie, Minglei Ren, Wei Xu et al.

**期刊**: *Journal of Hydrology: Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103694](https://doi.org/10.1016/j.ejrh.2026.103694) · **引用次数**: 0

**匹配主题**: streamflow, reservoir
{: .label .label-green }

> 长江上游流域主要支流中共建有38座大型水库，调节库容达805亿立方米。本研究将SWAT水文模拟与水文改变指标（IHA）分析相结合，定量评估水库建设对各支流自然水文情势的渐进式影响，发现低流量量级改变和极端事件时序变化最为显著——这些累积影响在单一水坝研究中并不显现。

---

### Optimizing environmental flow trade-offs for sustainable hydropower in a Himalayan reservoir

**作者**: Yogesh Neupane, Rupesh Baniya, Mukesh Raj Kafle et al.

**期刊**: *Energy Nexus* · **DOI**: [10.1016/j.nexus.2026.100784](https://doi.org/10.1016/j.nexus.2026.100784) · **引用次数**: 0

**匹配主题**: hydrology, hydropower
{: .label .label-green }

> 喜马拉雅中部地区水库运行面临水电发电、灌溉、防洪和下游环境流量的多重需求竞争。本研究针对一座喜马拉雅水库实施多目标优化框架，明确平衡发电量与环境流量需求，表明在气候变率下，智能调度可大幅降低人类用水与生态需水之间的权衡代价。

---

### Three Gorges Reservoir operations regulate nitrogen transport and transformation via hydrodynamic control

**作者**: Bei Nie, Yu Bai, Wei Zha, Xicheng Zhang et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135996](https://doi.org/10.1016/j.jhydrol.2026.135996) · **引用次数**: 0

**匹配主题**: hydrology
{: .label .label-green }

> 本研究探讨三峡水库蓄水运行如何通过流速、停留时间和分层变化调控库区及下游河段的氮素输送与原位生物地球化学转化。运行引发的水动力变化显著改变了反硝化、硝化和有机氮矿化之间的平衡，对长江中下游乃至东海的氮通量具有可量化的影响。

---

## 水资源、干旱与遥感

本主题涵盖数据集建设、干旱监测、环境流量评估与灌溉管理，共同推进了大尺度水资源研究的实测与观测基础。Seppä等发布CAMELS-FI——覆盖320个芬兰流域的大型流域数据集，提供多年代际水文气象时间序列和70余项流域属性，将CAMELS数据集家族延伸至北方气候区。Laluet等提出一个从多种地球观测方法融合的全球0.25°月灌溉用水量（IWU）档案，弥补了陆地水循环中这一最大人为干扰的关键数据缺口。Niranjannaik和Mishra量化了1990—2017年干旱驱动的印度10,476个地表水体面积萎缩规律。Lueders等开发了重建德克萨斯州参考水文和水文改变程度的建模框架，可直接应用于环境流量政策制定。Ruffing和Freed质疑"更高灌溉效率必然促进节水"的惯常思维，指出节水往往被再投入灌溉面积扩大，通过反弹效应抵消节约量。Wang等利用时空一致性框架在多气候区填补土壤湿度监测网络的数据缺口。

### CAMELS-FI: Hydrometeorological time series and landscape properties for 320 catchments in Finland

**作者**: Iiro Seppä, Carlos Gonzales Inca, Jari Uusikivi, Petteri Alho

**期刊**: *Earth System Science Data* · **DOI**: [10.5194/essd-18-4745-2026](https://doi.org/10.5194/essd-18-4745-2026) · **引用次数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 大样本水文数据集（如CAMELS）通过支撑跨流域学习和模型基准测试，推动了水文研究的诸多进展。CAMELS-FI将这一框架扩展至320个芬兰流域，提供数十年水文气象时间序列和70余项流域属性，涵盖北方气候特征——融雪动态、湖泊调蓄、泥炭地覆盖——这些特征在现有CAMELS数据集中代表性不足，为高纬度积雪主导水文情势下的模型训练与评估提供了重要数据支撑。

---

### Long-term irrigation water use datasets from multiple Earth Observation-based methods in major agricultural regions

**作者**: Pierre Laluet, Jacopo Dari, Louise Busschaert, Zdenko Heyvaert et al.

**期刊**: *Earth System Science Data* · **DOI**: [10.5194/essd-18-4833-2026](https://doi.org/10.5194/essd-18-4833-2026) · **引用次数**: 0

**匹配主题**: land surface model, irrigation, earth system model
{: .label .label-green }

> 灌溉用水量（IWU）被认为是陆地水循环中最大的人为直接干扰，但在气候研究所需的空间和时间尺度上仍缺乏良好表征。本研究基于多种地球观测方法提供全球主要农业区的长期月尺度IWU估算（空间分辨率0.25°），为评估表征农业需水的陆面模型和地球系统模型提供了关键观测约束。

---

### Drought driven shrinkage of surface water bodies in India

**作者**: M. Niranjannaik, Vimal Mishra

**期刊**: *iScience* · **DOI**: [10.1016/j.isci.2026.116737](https://doi.org/10.1016/j.isci.2026.116737) · **引用次数**: 0

**匹配主题**: drought, surface water
{: .label .label-green }

> 地表水体对区域水储量、生态系统和人类用水至关重要。利用卫星水面面积数据分析1990—2017年印度10,476个地表水体，本研究表明干旱事件导致水体面积系统性萎缩，且更大、更严重的干旱产生不成比例的更大损失。研究结果为当前区域水量平衡模型中普遍缺失的干旱—地表水体联系提供了定量依据。

---

### Reconstructing long-term historical hydrologic alteration to support environmental flows in Texas

**作者**: Mark B. Lueders, Ryan A. McManamay, Jay A. Oliver, David Young et al.

**期刊**: *River Research and Applications* · **DOI**: [10.1002/rra.70172](https://doi.org/10.1002/rra.70172) · **引用次数**: 0

**匹配主题**: hydrology, hydrologic model
{: .label .label-green }

> 理解和量化水文改变对流域管理和生态保育至关重要。本研究基于公开地理空间数据开发建模框架，预测德克萨斯州的参考（人为扰动前）水文状态并评估水文改变程度，为环境流量标准制定提供了可推广至其他受调控河流系统的标准化方法。

---

### Irrigation efficiency and water conservation: Aligning outcomes for people and nature

**作者**: Claire M. Ruffing, Zach Freed

**期刊**: *Frontiers in Water* · **DOI**: [10.3389/frwa.2026.1839103](https://doi.org/10.3389/frwa.2026.1839103) · **引用次数**: 0

**匹配主题**: hydrology, streamflow, irrigation
{: .label .label-green }

> 农业需水是全球最大的耗水来源。提高灌溉效率通常被视为节水途径，但本研究表明效率提升不能自动转化为耗水减少——更高效率往往促进灌溉面积扩大，通过反弹效应抵消节水成效。作者建议将效率政策重新定位为明确针对消耗性用水减少和环境流量维护。

---

### Filling data gaps in soil moisture monitoring networks via integrating spatiotemporal consistency

**作者**: Weixuan Wang, Yizhuo Meng, Zushuai Wei, Linguang Miao et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4191-2026](https://doi.org/10.5194/hess-30-4191-2026) · **引用次数**: 1

**匹配主题**: hydrologic model
{: .label .label-green }

> 原位土壤湿度观测常因传感器故障产生数据缺口，中断水文连续性。本研究开发了一个集成邻近站点数据、卫星土壤湿度产品和陆面模型输出的时空一致性框架，用于重建缺失观测值。该方法在不同气候区均经过验证，在精度和可处理缺口长度方面均优于现有插补方法，对卫星验证活动具有直接应用价值。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题词数 | 16 |
| 获取论文总数 | 1,047 |
| 去重后 | 915 |
| 排除屏蔽期刊后 | 869 |
| LLM相关性筛选后 | 28 |
| 拒绝（不相关） | 841 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|------:|
| Journal of Hydrology | 4 |
| Hydrology and Earth System Sciences | 3 |
| Journal of Water Resources Planning and Management | 3 |
| Earth System Science Data | 2 |
| Hydrological Sciences Journal | 2 |
| Journal of Hydrology: Regional Studies | 2 |
| Communications Earth & Environment | 1 |
| Energy Nexus | 1 |
| Frontiers in Water | 1 |
| Geophysical Research Letters | 1 |
| Geoscientific Model Development | 1 |
| Int. Journal of Applied Earth Observation and Geoinformation | 1 |
| iScience | 1 |
| Machine Learning: Science and Technology | 1 |
| Nature Sustainability | 1 |
| River Research and Applications | 1 |
| Scientific Reports | 1 |
| Geography, Environment, Sustainability | 1 |

## 筛选标准

**主题关键词**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

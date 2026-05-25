---
layout: default
title: "第20周（5月11日 - 5月18日），27篇"
nav_order: 35
nav_exclude: true
lang: zh
lang_link: /2026/may/2026-05-25-weekly-review
date: 2026-05-25
categories: [weekly-zh, 2026, may]
tags: [hydrology, literature-review, research]
paper_count: 27
highlight: "新河道汇流模型C-CWatM实现与地球系统模型/陆面模型的直接耦合；Science记录气候变暖下喜马拉雅河流加速演变。"
---

# 每周文献综述
{: .no_toc }

**第20周** · 2026年5月11日–5月18日
{: .text-grey-dk-000 }

在 **5** 个主题中发现 **27** 篇相关论文
{: .fs-5 .fw-300 }

## 摘要总结

本周在水资源模型与地球系统模型的耦合方面取得重大进展，C-CWatM v1.0实现了高分辨率河道汇流和人类用水管理在地球系统模型中的直接集成。气候变化对河流的影响是本周文献的主导主题，Science的一篇标志性论文记录了喜马拉雅河流蜿蜒速率因气候变暖而加速，Nature Communications则揭示了亚洲水塔融水难以弥补下游城市水资源短缺。水文领域的机器学习应用持续增长，物理约束的神经算子和半监督方法正在解决数据稀缺流域的预测难题。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 大尺度水文与地球系统建模

本周的重大进展是C-CWatM v1.0，一个专为与地球系统模型和陆面模型直接耦合而设计的河道汇流和水资源模型，弥补了气候建模与人类用水管理之间长期存在的断层。与此同时，O'Donnell等人对密西西比河流域水文剧变的研究利用地球系统模型预估揭示了干湿快速转换的驱动机制，Green等人在Nature Communications中证明植被对大气干燥的响应形成正反馈环加剧了陆面增温——这对陆面模型发展至关重要。在更精细的尺度上，Sun等人在GRL中关于土壤裂缝动力学的研究为优先流入渗参数化提供了机理基础，Indrawati等人的因果分析揭示了变暖条件下土壤水分控制的变化对当前陆-气耦合假设提出了挑战。

### C-CWatM v1.0: A high-resolution water resources and river routing model enabling direct linkage to state-of-the-art Earth-system and land‑surface models

**作者**: Peter Greve, Amelie U. Schmitt, Sina Jasmin Schreiber, Augustin Clédat, Peter Burek

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2366](https://doi.org/10.5194/egusphere-2026-2366) · **引用次数**: 0

**匹配主题**: hydrologic model, runoff, streamflow, water management, land surface model, earth system model
{: .label .label-green }

> 摘要：河道汇流和人类用水管理在许多地球系统模型和陆面模型中的表达能力不足，无法对人类-水-气候的交互作用进行一致性评估。本研究介绍了C-CWatM v1.0（Climate-CWatM v1.0），这是社区水模型（CWatM）的陆面驱动版本，可与先进的地球系统和陆面模型直接耦合。C-CWatM v1.0提供高分辨率的河道汇流和人类用水管理能力，包括水库调度、灌溉和水资源分配。文章展示了模型架构、耦合接口以及在全球流域再现观测径流和水库蓄水量方面的性能。

---

### Hydrologic Whiplash in the Mississippi River Basin: Mechanisms and Projections

**作者**: Michelle O'Donnell, S. G. Dee, J. Doss-Gollin, Samuel E. Munoz

**期刊**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl122807](https://doi.org/10.1029/2026gl122807) · **引用次数**: 0

**匹配主题**: hydrologic model, river, streamflow, earth system model
{: .label .label-green }

（同时出现在2026-05-12每日采集中）

> 水文气候系统的波动性和不可预测性给规划和风险管理带来压力。特别是，高低流量之间的快速转换——即水文剧变——正在全球范围内引起关注。然而，驱动水文剧变事件的具体机制及其未来变化趋势仍知之甚少。本文分析了密西西比河流域的观测和预估径流，以表征水文剧变的驱动因素和未来轨迹。

---

### Vegetation responses to air dryness amplify future land surface warming

**作者**: Julia K. Green, Trevor F. Keenan, Xu Lian, David J. P. Moore, Philippe Ciais

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-026-73063-7](https://doi.org/10.1038/s41467-026-73063-7) · **引用次数**: 0

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 温度对植被光合作用和蒸腾有第一性控制作用。然而大多数研究依赖近地面气温而非冠层温度——植物实际感受的温度。由于冠层温度直接影响气孔导度和蒸腾，植被功能变化会反馈到地表能量平衡。研究表明，植被对大气干燥度增加的响应减少了蒸腾并加剧了陆面增温，形成了当前地球系统模型中代表不足的正反馈环。

---

### Causal analyses reveal changing land-atmosphere patterns and soil moisture control under warming

**作者**: Dian Indrawati, Somnath Mondal, Poulomi Ganguli, Auroop Ganguly

**期刊**: *ESSOAr* · **DOI**: [10.31223/x53b62](https://doi.org/10.31223/x53b62) · **引用次数**: 0

**匹配主题**: runoff, earth system model
{: .label .label-green }

> 气候变化预计将改变全球水循环和陆-气交互作用。然而，变暖引起的多变量依赖关系变化仍未得到充分探索。本文利用因果发现方法分析再分析数据和CMIP6预估，研究温度、可降水量、降水、蒸发、土壤水分和径流之间的相互依赖关系。结果表明，在变暖情景下，土壤水分对陆-气耦合的控制作用日益增强。

---

### Soil Crack Width Controls Preferential Flow Velocity Through Drag Partitioning

**作者**: Chang Sun, Chao‐Sheng Tang, Farshid Vahedifard, Ao Dong, Zhan‐Ming Yang, Bin Shi

**期刊**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl122866](https://doi.org/10.1029/2026gl122866) · **引用次数**: 0

**匹配主题**: hydrologic model, land surface model
{: .label .label-green }

> 土壤裂缝中的优先流影响陆面水文过程，但直接量化优先流速度仍然具有挑战性。本文利用光频域反射计开发了一种高分辨率监测和量化土壤裂缝中优先流速度的方法。结果表明，裂缝宽度通过阻力分配机制对优先流速度起主要控制作用，为陆面模型中的优先流参数化提供了物理基础。

---

## 气候变化对河流和水资源的影响

气候驱动的河流系统变化是本周的主导主题。Lin等人在Science上发表的标志性论文记录了与气候变暖相关的喜马拉雅河流蜿蜒速率加速，Li等人在Nature Communications中显示亚洲水塔的融水潜力有限，难以弥补下游城市水资源短缺——这对适应规划是一个警醒。刘等人的预估表明，第三极冰川化最严重流域的洪水正变得越来越不可预测。在高纬度地区，北极河流深度学习预估显示到本世纪末径流增加6-15%，永久冻土退化正在改变主导气候驱动因素。在北美西部，夏季干旱正威胁河流生态系统和关键洄游鲑鱼种群，全球分析揭示了降水和融雪时序变化驱动的洪水季节性系统性转变。

### Accelerated Himalayan river meandering and dynamics due to climate change

**作者**: Zhipeng Lin, Zhongpeng Han, David R. Montgomery, Waqas Ul Hussan, Lars Lønsmann Iversen, Mette Bendixen et al.

**期刊**: *Science* · **DOI**: [10.1126/science.adg8401](https://doi.org/10.1126/science.adg8401) · **引用次数**: 1

**匹配主题**: river, climate change
{: .label .label-green }

（同时出现在2026-05-14每日采集中）

> 河流蜿蜒和迁移是全球性的基本过程，高喜马拉雅地区提供了检验河流形态动力学是否因快速变化的气候而发生转变的机会。研究利用遥感影像和野外观测，量化了数十年来主要喜马拉雅河流的蜿蜒及其相关动态。结果揭示了与冰川融化加剧和季风降水增强相关的河流蜿蜒速率的统计显著加速。

---

### Limited meltwater potential in the Asian Water Tower to mitigate downstream urban scarcity

**作者**: Lei Li, Chunyang He, Tao Qi, Kaiyu Zhao, Arthur Lutz, Bruno Merz

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-026-73245-3](https://doi.org/10.1038/s41467-026-73245-3) · **引用次数**: 0

**匹配主题**: hydrology, streamflow
{: .label .label-green }

> 作为数十亿下游人口的重要淡水来源，亚洲水塔正在气候变化下快速转变。加速的冰川和融雪正在重塑融水格局，威胁快速人口增长下的城市供水安全。利用高分辨率冰冻圈-水文模型耦合城市用水需求预估，研究表明即使在乐观的融化情景下，融水贡献也不足以抵消下游城市日益增长的水资源短缺。融水时序与城市需求峰值的不匹配进一步限制了适应选择。

---

### More unpredictable river floods at the most glacierized Third Pole basin

**作者**: Hu Liu, Lei Wang, Deliang Chen, Tandong Yao, Ahmad Bashir

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03623-8](https://doi.org/10.1038/s43247-026-03623-8) · **引用次数**: 0

**匹配主题**: hydrology, hydrologic model, river, flood
{: .label .label-green }

> 极端洪水对土石坝和下游社区构成威胁，尤其是在洪水可预测性不明确的冰川化流域。本研究结合高分辨率冰冻圈-水文模型与观测数据，预估罕萨流域（第三极冰川化最严重的流域）的洪水频率和强度将显著增加。随着冰川融化改变季节性径流格局，洪水事件变得更加不可预测，对现有大坝安全和预警系统提出挑战。

---

### Projected hydrological responses to climate change in a high-mountain river basin based on RCM simulations

**作者**: Adnan Khan, Fiza Gul, Muhammad Fahad Ullah, Hassan Ayaz, Mahmood Ahmad, Feezan Ahmad et al.

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-52852-6](https://doi.org/10.1038/s41598-026-52852-6) · **引用次数**: 0

**匹配主题**: hydrology, hydrologic model, river, runoff, streamflow, climate change
{: .label .label-green }

> 本研究评估了巴基斯坦北部奇特拉尔河流域（一个高山冰川补给集水区）在气候变化下的未来水文响应。利用SWAT模型和三个CORDEX区域气候模型的偏差校正输出进行驱动。结果显示，在高排放情景下，季节性径流格局将发生显著变化，春季峰值提前，夏季流量减少，对下游水资源可用性和洪水风险管理具有重要意义。

---

### Projected changes in Arctic river streamflow and shifting climatic drivers: A linear ensemble deep learning approach

**作者**: Shiqi Liu, Renjie Zhou, Ping Wang, Jingjie Yu, Vahid Nourani

**期刊**: *Geoscience Frontiers* · **DOI**: [10.1016/j.gsf.2026.102350](https://doi.org/10.1016/j.gsf.2026.102350) · **引用次数**: 0

**匹配主题**: hydrology, river, streamflow, earth system model
{: .label .label-green }

> 本文提出了一种线性集成深度学习方法用于北极河流径流预测。预计到2080-2100年，六个北极流域的径流将增加6.1%-15.3%。北极河流径流在永久冻土退化早期阶段对变暖更为敏感。冬季径流增加由永久冻土解冻后增强的地下水流驱动，夏季峰值提前。该方法结合多个CMIP6地球系统模型输出和观测径流数据，生成稳健的集成预估。

---

### Drying summers threaten western North American river ecosystems and a keystone migratory fish

**作者**: Sacha W. Ruzzante, Tom Gleeson, Jonathan W. Moore, Marta Ulaski, Todd Hatfield, Markus Schnorbus et al.

**期刊**: *ESSOAr* · **DOI**: [10.31223/x5sv1j](https://doi.org/10.31223/x5sv1j) · **引用次数**: 0

**匹配主题**: river, streamflow
{: .label .label-green }

> 气候变化通过改变水生物种已适应的季节性径流格局而威胁河流生态系统，包括北美西部的关键物种奇努克鲑鱼。奇努克鲑鱼对当地水文条件表现出多样的生活史适应，这有助于物种整体的恢复力。研究预估了北美西部河流未来夏季径流的下降，显示夏季干燥化对鲑鱼栖息河流构成系统性威胁。

---

### Shifts in global flood seasonality and their drivers

**作者**: Sixiang Wang, Yansong Guan, Xihui Gu, Shuangyu Wang

**期刊**: *Hydrological Sciences Journal* · **DOI**: [10.1080/02626667.2026.2661882](https://doi.org/10.1080/02626667.2026.2661882) · **引用次数**: 0

**匹配主题**: flood, seasonal
{: .label .label-green }

> 摘要不可用。

---

## 水库调度与水资源管理

全球尺度的水库分析表明，灌溉水库面临不成比例的高缺水风险，Shah等人在Communications Earth & Environment中指出气候变率和需求增长是水库干旱的双重驱动因素。Okiria等人利用卫星数据系统性验证了全球水文模型中的水库蓄水模拟——鉴于当前全球水文模型对管理水系统的表达能力不足，这是关键的一步。在中国，对河北省灌溉用地下水置换地表水的政策评估突显了供水侧适应含水层耗竭的有效性和局限性。

### Global irrigation reservoirs are at a higher risk of water shortages

**作者**: Deep Shah, Vimal Mishra, Huilin Gao

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03571-3](https://doi.org/10.1038/s43247-026-03571-3) · **引用次数**: 0

**匹配主题**: streamflow, reservoir, irrigation
{: .label .label-green }

> 水库干旱引发的缺水对全球粮食、水和能源安全构成重大威胁。然而，水库干旱的全球尺度评估、高风险水库的识别以及主导驱动因素（气候vs.人类活动）仍未被充分探索。本文分析了全球7,000多座水库，发现灌溉水库面临的干旱风险系统性高于水力发电或防洪水库，气候变率和需求增长形成叠加驱动。

---

### Using satellite observations to validate and improve reservoir storage simulations in global hydrological models

**作者**: Emmanuel Okiria, Naota Hanasaki, Simon N. Gosling, Emmanuel Nyenah, Peter Burek, Yusuke Satoh et al.

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2043](https://doi.org/10.5194/egusphere-2026-2043) · **引用次数**: 0

**匹配主题**: hydrology, hydrologic model, reservoir
{: .label .label-green }

> 全球水文模型越来越多地纳入通用水库调度方案来模拟大坝对河流的调节作用。然而，由于历史上缺乏开放的实测数据，这些方案的可靠性在全球尺度上基本未经验证。本文利用卫星获取的水库蓄水量估算，系统性评估和改进多个全球水文模型的水库模拟。结果揭示了当前通用方案中的显著偏差，特别是灌溉主导型水库，并展示了卫星观测如何约束模型参数。

---

### Substituting Groundwater With Surface Water for Irrigation in Northern China: Current Status, Effectiveness and Challenges

**作者**: Tianhe Sun, Baozhu Guan, Baozhu Guan, Huang Chen, Yì Wáng, Wei Chao et al.

**期刊**: *Australian Journal of Agricultural and Resource Economics* · **DOI**: [10.1111/1467-8489.70108](https://doi.org/10.1111/1467-8489.70108) · **引用次数**: 0

**匹配主题**: surface water, irrigation
{: .label .label-green }

> 中国灌溉核心区面临含水层耗竭和粮食安全的双重压力。本文利用县级面板数据和渐进双重差分框架，评估了河北省灌溉用地下水置换地表水（SGSWI）项目。结果表明该项目在减少地下水开采方面成效显著，但在干旱年份面临地表水可用性不足和基础设施维护成本方面的可持续性挑战。

---

## 水文领域的机器学习预测

机器学习在水文预测中的应用持续加速，明显转向物理约束和不确定性感知方法。Behroozi等人（沈超鹏团队）提出了物理锚定的多分辨率神经算子用于洪水淹没预测，在保持物理一致性的同时实现了相比水动力模型的数量级加速。多篇论文解决了数据稀缺的关键挑战：Jia等人提出利用无标签气象数据的半监督深度学习，Zhang等人开发了提示引导的可微物理模型。Peng等人解决了深度学习径流预测中数据和模型不确定性联合量化这一尚未充分探索的问题。在流域尺度，Manoli等人证明深度学习误差后处理可显著改善随机流域模型输出，数据驱动的SWE估算在Sierra Nevada表现出与运行中SNOW-17模型的竞争性能。

### Physically Anchored Multi-Resolution Neural Operator Framework for Flood Inundation Prediction

**作者**: Abdolmehdi Behroozi, Kathryn Lawson, Chaopeng Shen

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1982](https://doi.org/10.5194/egusphere-2026-1982) · **引用次数**: 0

**匹配主题**: hydrology, streamflow, flood
{: .label .label-green }

> 使用高分辨率水动力模拟进行精确洪水淹没建模计算需求巨大，限制了其在大尺度分析和快速情景评估中的应用。虽然已开发了机器学习替代模型，但许多模型难以在保持物理一致性的同时再现洪水淹没的完整时空演变。本文提出一种物理锚定的多分辨率神经算子框架，在保持质量守恒和地形约束的同时，实现了相比传统水动力模型的数量级计算加速。

---

### Streamflow prediction in data-scarce regions with semi-supervised deep learning

**作者**: Tianlong Jia, Guoding Chen, Yao Li, Xinyu Chang, Uwe Ehret

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1637](https://doi.org/10.5194/egusphere-2026-1637) · **引用次数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 深度学习方法在径流预测中表现出色。然而，它们通常需要大量"标记"数据进行监督学习，包括气象强迫数据与相应径流观测的配对。许多地区径流观测数据的稀缺使精度较低的卫星估算成为唯一选择。本文提出一种半监督深度学习框架，利用丰富的无标签气象数据与稀疏的径流观测，相比纯监督方法显著提高了数据稀缺流域的预测能力。

---

### A prompt-guided differentiable physics model for flood forecasting in data-scarce basins

**作者**: Jiru Zhang, Jun Feng, Runliang Xia, Pingping Shao, Xin Chi

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135671](https://doi.org/10.1016/j.jhydrol.2026.135671) · **引用次数**: 0

**匹配主题**: hydrology, hydrologic model
{: .label .label-green }

> 摘要不可用。

---

### Quantification of Data and Model Uncertainty for Deep Learning-based Streamflow Prediction

**作者**: Kaidi Peng, Daniel Benjamin Wright, Lei Yan, G. Aaron Alexander, Yagmur Derin

**期刊**: *ESSOAr* · **DOI**: [10.22541/essoar.176677052.23567555/v2](https://doi.org/10.22541/essoar.176677052.23567555/v2) · **引用次数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 准确及时的洪水预警对减少洪水风险至关重要。实现这一目标需要准确的数据和精心的模型参数化。许多地区缺乏高分辨率地面降水观测，精度较低的卫星降水估算成为主要输入。本文提出一个框架，用于联合量化深度学习径流预测中的数据不确定性（来自卫星降水误差）和模型不确定性，证明同时考虑两种不确定性来源可显著提高概率预报可靠性。

---

### Deep learning error post-processing improves stochastic watershed modeling

**作者**: Benjamin Manoli, Sandeep Poudel, David K. Koval, S. Y. Murphy, Scott Steinschneider, Jonathan Lamontagne

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135663](https://doi.org/10.1016/j.jhydrol.2026.135663) · **引用次数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 摘要不可用。

---

### Evaluating data-driven models to estimate snow water equivalent in the Sierra Nevada

**作者**: Engela Sthapit, Mimi Rose Abel, William Ryan Currier, Rob Cifelli, Peter Fickenscher

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103481](https://doi.org/10.1016/j.ejrh.2026.103481) · **引用次数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 研究区域：Sierra Nevada的Tuolumne、Merced、American和Feather流域。研究重点：探索数据驱动模型和运行中的过程模型SNOW-17估算历史雪水当量（SWE）的能力。加州-内华达河流预报中心目前使用SNOW-17模拟的SWE发布业务径流预报。三种不同复杂度的机器学习方法——多元线性回归、随机森林回归和长短期记忆网络——在多个流域和海拔带进行了评估。结果显示机器学习模型达到了具有竞争力或更优的SWE估算精度。

---

### Integrating lumped hydrological modelling with GIS-based flow accumulation for spatiotemporal streamflow estimation

**作者**: Sri Priyanka Kommula, Dongryeol Ryu, Bharat Lohani, Stephan Winter

**期刊**: *Environmental Modelling & Software* · **DOI**: [10.1016/j.envsoft.2026.107026](https://doi.org/10.1016/j.envsoft.2026.107026) · **引用次数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 摘要不可用。

---

## 水文数据产品、监测与过程研究

新数据产品和过程层面的研究丰富了本周文献。Sun等人发布了青藏高原雅鲁藏布江流域63年逐日水文气象数据集，填补了这一敏感高海拔系统的关键数据空白。Uthayakumar等人发表了基于河网连通性的全美水系分类，纳入了现有分类框架中基本缺失的河网拓扑维度。Aqui-FR平台的地下水数据同化取得进展，而高山冻融径流过程和干旱区河流动力学的野外研究为模型发展提供了有价值的机理认识。

### A 1961–2024 daily hydrometeorological dataset for the Yarlung Zangbo basin of the southern Tibetan Plateau from high-resolution observation and model integration

**作者**: He Sun, Tandong Yao, Fengge Su, Bowen Zheng, Yi Zhang

**期刊**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07442-6](https://doi.org/10.1038/s41597-026-07442-6) · **引用次数**: 0

**匹配主题**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> 理解雅鲁藏布江流域的径流变化对青藏高原水资源管理至关重要，但一直受到数据稀缺的制约。本研究提供了1961-2024年雅鲁藏布江流域的综合水文气象数据集，包括逐日气象强迫（降水、温度、辐射）和模拟水文变量（径流、蒸散发、雪水当量）。数据集整合了高分辨率观测和过程模型输出，并通过可用站点记录进行了验证。

---

### Network Connectivity-based stream classification for the Conterminous United States

**作者**: Haripriyan Uthayakumar, Brandon K. Peoples, Julian D. Olden, Stephen Midway, Shweta Singh

**期刊**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07199-y](https://doi.org/10.1038/s41597-026-07199-y) · **引用次数**: 0

**匹配主题**: hydrology, streamflow
{: .label .label-green }

> 水系分类在淡水生态系统研究和管理中发挥重要作用。现有分类方案主要关注物理栖息地、水文和温度特征，但很少有框架明确纳入河网连通性。由于河网结构从根本上塑造了生态和水文过程，本文为美国本土所有NHDPlus河段开发并提出了基于河网连通性的水系分类。

---

### A data assimilation scheme to improve groundwater state estimation in the Aqui-FR modelling platform

**作者**: Adrien Manlay, Jean‐Pierre Vergnes, Simon Munier, Florence Habets

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1504](https://doi.org/10.5194/egusphere-2026-1504) · **引用次数**: 0

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 地下水是人类活动的关键资源，提前数月预测其演变是利益相关方面临的重大挑战。地下潜流水文模型可用于地下水位预报。然而，由于模型强迫和参数的不确定性，预报质量随时间下降。本文在Aqui-FR建模平台内开发并评估了一种数据同化方案，通过同化观测地下水位来改善地下水状态估算和季节性预报技能。

---

### Integrated analysis of climate and human drivers of streamflow and sediment load in a dryland river

**作者**: Shihua Yin, Yatong Wu, Enhang Liang, Anqi Huang, Lishan Ran, Guangyao Gao

**期刊**: *CATENA* · **DOI**: [10.1016/j.catena.2026.110210](https://doi.org/10.1016/j.catena.2026.110210) · **引用次数**: 0

**匹配主题**: river, streamflow
{: .label .label-green }

> 摘要不可用。

---

### Mechanisms driving hydrologic regime shifts in small catchments underlain by continuous permafrost during prolonged warming

**作者**: Ruixin Wang, Liudmila S. Lebedeva, Ping Wang, Qiwei Huang, Vladimir V. Shamov, Shiqi Liu et al.

**期刊**: *CATENA* · **DOI**: [10.1016/j.catena.2026.110197](https://doi.org/10.1016/j.catena.2026.110197) · **引用次数**: 0

**匹配主题**: runoff, streamflow
{: .label .label-green }

> 摘要不可用。

---

## 统计信息

| 指标 | 数量 |
|:-------|------:|
| 搜索数据库数 | 2 |
| 搜索主题数 | 16 |
| 获取论文总数 | 1271 |
| 去重后 | 1001 |
| 经LLM相关性筛选后 | 27 |
| 排除（不相关） | 974 |

### 按期刊分布

| 期刊 | 论文数 |
|:--------|-------:|
| EGUsphere | 5 |
| Journal of Hydrology | 3 |
| Nature Communications | 2 |
| Communications Earth & Environment | 2 |
| Scientific Data | 2 |
| CATENA | 2 |
| Geophysical Research Letters | 2 |
| ESSOAr | 2 |
| Scientific Reports | 1 |
| Science | 1 |
| Geoscience Frontiers | 1 |
| Hydrological Sciences Journal | 1 |
| Journal of Hydrology Regional Studies | 1 |
| Environmental Modelling & Software | 1 |
| Australian Journal of Agricultural and Resource Economics | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

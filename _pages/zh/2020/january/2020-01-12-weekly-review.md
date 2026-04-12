---
layout: default
title: "第02周（1月6日 - 1月12日），31篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2020/january/2020-01-12-weekly-review
date: 2020-01-12
categories: [weekly-zh, 2020, january]
tags: [hydrology, literature-review, research]
paper_count: 31
highlight: "CMIP6地球系统模式开发里程碑期，CESM2、NorESM2、GFDL-ESM4.1和MIROC-ES2L相继发布，同时深度学习径流预测和综合干旱预估研究取得突破。"
---

# 每周文献综述
{: .no_toc }

**第02周** · 2020年1月6日–12日
{: .text-grey-dk-000 }

**31** 篇相关论文，涵盖 **5** 个主题
{: .fs-5 .fw-300 }

## 摘要

2020年初是地球系统模式开发的里程碑时期，五个主要CMIP6级别模式（CESM2、NorESM2、GFDL-ESM 4.1、ACCESS-ESM1.5和MIROC-ES2L）的文档相继发布。干旱研究激增，多项基于CMIP6的预估研究识别了全球未来干旱热点地区，而深度学习方法——特别是LSTM变体——在径流预测和洪水预报方面展现出日益增强的能力。Milly和Dunne在Science上关于科罗拉多河流量下降的论文凸显了理解变暖对水资源影响的紧迫性。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 地球系统模式开发

2020年是地球系统模式开发的里程碑之年，多个主要的CMIP6级别地球系统模式相继发布文档。Danabasoglu等人全面介绍了第二版社区地球系统模式（CESM2），Emmons等人详细描述了其化学机制。挪威（NorESM2，Seland等）、美国（GFDL-ESM 4.1，Dunne等）、澳大利亚（ACCESS-ESM1.5，Ziehn等）和日本（MIROC-ES2L，Hajima等）的建模中心均发表了各自CMIP6贡献的描述。Deser等人从地球系统模式初始条件大集合中获得了重要见解，展示了集合方法在区分强迫响应与内部变率方面的价值。

### The Community Earth System Model Version 2 (CESM2)

**作者**: G. Danabasoglu, J. Lamarque, J. Bacmeister, D. A. Bailey, A. K. DuVivier, J. Edwards et al.

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2019MS001916](https://doi.org/10.1029/2019MS001916) · **被引次数**: 1901

**匹配主题**: earth system model
{: .label .label-green }

> 本文概述了第二版社区地球系统模式（CESM2），包括其开发过程中遇到的挑战及解决方案。此外，对CESM2的长期工业化前控制模拟和历史集合模拟进行了评估。

---

### Insights from Earth system model initial-condition large ensembles and future prospects

**作者**: C. Deser, F. Lehner, K. Rodgers, T. Ault, T. Delworth, P. DiNezio et al.

**期刊**: *Nature Climate Change* · **DOI**: [10.1038/s41558-020-0731-2](https://doi.org/10.1038/s41558-020-0731-2) · **被引次数**: 738

**匹配主题**: earth system model
{: .label .label-green }

> 本文从地球系统模式初始条件大集合中获得见解，并探讨了未来前景。展示了集合方法在区分强迫响应与内部变率方面的重要价值。

---

### Overview of the Norwegian Earth System Model (NorESM2) and key climate response of CMIP6 DECK, historical, and scenario simulations

**作者**: Ø. Seland, M. Bentsen, D. Oliviè, T. Toniazzo, A. Gjermundsen, L. S. Graff et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-13-6165-2020](https://doi.org/10.5194/gmd-13-6165-2020) · **被引次数**: 651

**匹配主题**: earth system model
{: .label .label-green }

> 介绍并评估了第二版耦合挪威地球系统模式（NorESM2）。NorESM2基于CESM2，共享代码基础设施和许多地球系统模式组件，但在大气、海洋和海冰方面有独特的挪威贡献。

---

### The GFDL Earth System Model Version 4.1 (GFDL‐ESM 4.1): Overall Coupled Model Description and Simulation Characteristics

**作者**: J. Dunne, L. Horowitz, A. Adcroft, P. Ginoux, I. Held, J. John et al.

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2019MS002015](https://doi.org/10.1029/2019MS002015) · **被引次数**: 547

**匹配主题**: earth system model
{: .label .label-green }

> 描述了GFDL地球系统模式4.1版（GFDL-ESM 4.1）的基准耦合模式配置和模拟特征，该模式建立在GFDL 2013-2018年间的组件和耦合模式开发基础之上，用于CMIP6的耦合碳-化学-气候模拟。

---

### The Australian Earth System Model: ACCESS-ESM1.5

**作者**: T. Ziehn, M. Chamberlain, R. Law, A. Lenton, R. Bodman, M. Dix et al.

**期刊**: *Journal of Southern Hemisphere Earth Systems Science* · **DOI**: [10.1071/es19035](https://doi.org/10.1071/es19035) · **被引次数**: 465

**匹配主题**: earth system model
{: .label .label-green }

> 澳大利亚社区气候和地球系统模拟器（ACCESS）已扩展纳入陆地和海洋碳循环组件，形成地球系统模式。当前版本ACCESS-ESM1.5主要为澳大利亚参与CMIP6而开发。

---

### Development of the MIROC-ES2L Earth system model and the evaluation of biogeochemical processes and feedbacks

**作者**: T. Hajima, Michio Watanabe, A. Yamamoto, H. Tatebe, Maki A. Noguchi, M. Abe et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-13-2197-2020](https://doi.org/10.5194/gmd-13-2197-2020) · **被引次数**: 460

**匹配主题**: earth system model
{: .label .label-green }

> 本文描述了新的地球系统模式MIROC-ES2L，使用最先进的气候模式作为物理核心，嵌入了陆地生物地球化学组件，并评估了生物地球化学过程和反馈。

---

### The Chemistry Mechanism in the Community Earth System Model Version 2 (CESM2)

**作者**: L. Emmons, R. Schwantes, J. Orlando, G. Tyndall, D. Kinnison, J. Lamarque et al.

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2019MS001882](https://doi.org/10.1029/2019MS001882) · **被引次数**: 333

**匹配主题**: earth system model
{: .label .label-green }

> CESM2包含了大气化学的详细表征。本文描述了社区大气模式化学配置和全球大气社区气候模式配置中的化学机制。

---


## 干旱预估与评估

大量研究利用最新的CMIP6预估分析了未来干旱风险。Cook等人分析了整个水文循环中的21世纪干旱预估，Ukkola等人证明了尽管降水存在不确定性，气象干旱变化仍具有稳健性。区域研究聚焦于中国（Su等）、地中海地区（Tramblay等）和中欧（Hari等），后者表明2018-2019年的极端干旱在全球变暖下将更加频繁。Spinoni等人利用CORDEX数据识别了未来全球干旱热点地区。Ault在Science上发表综述，综合阐述了变化气候中干旱的物理学和统计学。

### Twenty‐First Century Drought Projections in the CMIP6 Forcing Scenarios

**作者**: B. Cook, J. Mankin, K. Marvel, A. P. Williams, J. Smerdon, K. Anchukaitis

**期刊**: *Earth's Future* · **DOI**: [10.1029/2019EF001461](https://doi.org/10.1029/2019EF001461) · **被引次数**: 626

**匹配主题**: drought
{: .label .label-green }

> 有充分证据表明气候变化将增加干旱风险和严重程度，但这些结论取决于所考虑的区域、季节和干旱指标。本研究分析了CMIP6预估中水文循环各环节（降水、土壤水分和径流）的干旱变化。

---

### On the essentials of drought in a changing climate

**作者**: T. Ault

**期刊**: *Science* · **DOI**: [10.1126/science.aaz5492](https://doi.org/10.1126/science.aaz5492) · **被引次数**: 471

**匹配主题**: drought
{: .label .label-green }

> 未来的干旱可能比近几十年更加频繁、严重和持久，但如果大幅削减温室气体排放，干旱风险将会降低。本综述介绍了理解干旱统计学、物理学和未来变化趋势所需的工具。

---

### Challenges for drought assessment in the Mediterranean region under future climate scenarios

**作者**: Y. Tramblay, A. Koutroulis, L. Samaniego, S. Vicente‐Serrano, F. Volaire, A. Boone et al.

**期刊**: *Earth-Science Reviews* · **DOI**: [10.1016/j.earscirev.2020.103348](https://doi.org/10.1016/j.earscirev.2020.103348) · **被引次数**: 455

**匹配主题**: drought
{: .label .label-green }

> 干旱可能对地中海地区产生强烈的环境和社会经济影响，特别是对依赖雨养农业生产的国家。本文讨论了未来气候情景下地中海地区干旱评估面临的挑战。

---

### Robust Future Changes in Meteorological Drought in CMIP6 Projections Despite Uncertainty in Precipitation

**作者**: A. Ukkola, M. D. De Kauwe, M. Roderick, G. Abramowitz, A. Pitman

**期刊**: *Geophysical Research Letters* · **DOI**: [10.1029/2020GL087820](https://doi.org/10.1029/2020GL087820) · **被引次数**: 362

**匹配主题**: drought
{: .label .label-green }

> 量化气候变化如何驱动干旱是为政策和适应规划提供信息的优先事项。本研究表明最新的CMIP6模拟预估了两种排放情景下到2100年的区域气象干旱一致模式。

---

### Insight from CMIP6 SSP-RCP scenarios for future drought characteristics in China

**作者**: Buda Su, Jinlong Huang, Sanjit Kumar Mondal, J. Zhai, Yanjun Wang, Shanshan Wen et al.

**期刊**: *Atmospheric Research* · **DOI**: [10.1016/j.atmosres.2020.105375](https://doi.org/10.1016/j.atmosres.2020.105375) · **被引次数**: 338

**匹配主题**: drought
{: .label .label-green }

> 本文利用CMIP6四个气候模式在七个SSP-RCP情景下分析了中国未来干旱特征（频率、持续时间和强度）。

---

### Future Global Meteorological Drought Hot Spots: A Study Based on CORDEX Data

**作者**: J. Spinoni, P. Barbosa, E. Bucchignani, J. Cassano, Tereza Cavazos, J. Christensen et al.

**期刊**: *Journal of Climate* · **DOI**: [10.1175/jcli-d-19-0084.1](https://doi.org/10.1175/jcli-d-19-0084.1) · **被引次数**: 336

**匹配主题**: drought
{: .label .label-green }

> 本研究探讨了两个问题：1）21世纪气象干旱是否会更加频繁和严重？2）在预估的全球温度上升背景下，干旱指标中纳入温度（除降水外）在多大程度上发挥作用？

---

### Increased future occurrences of the exceptional 2018–2019 Central European drought under global warming

**作者**: Vittal Hari, O. Rakovec, Y. Markonis, M. Hanel, Rohini Kumar

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-020-68872-9](https://doi.org/10.1038/s41598-020-68872-9) · **被引次数**: 331

**匹配主题**: drought
{: .label .label-green }

> 自2018年春季以来，欧洲大部分地区经历了创纪录的干旱。利用长期观测数据，本研究证明2018-2019年连续夏季干旱在过去250年中前所未有，并分析了其在全球变暖下的未来频率变化。

---


## 洪水研究与监测

该时期的洪水研究涵盖了灾害评估、遥感监测和机器学习方法。Tabari证明了气候变化对洪水和极端降水的影响随水资源可用性增加而增大。多项研究采用集成方法推进了基于机器学习的洪水易发性制图（Islam等、Gudiyangada Nachappa等、Shahabi等）。遥感进展包括基于Google Earth Engine的Sentinel-1和Landsat洪水监测（DeVries等）。Kao等人提出了用于多步洪水预报的基于LSTM的编码器-解码器框架，Menéndez等人量化了红树林在全球洪水防护中的效益。

### Climate change impact on flood and extreme precipitation increases with water availability

**作者**: H. Tabari

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-020-70816-2](https://doi.org/10.1038/s41598-020-70816-2) · **被引次数**: 1228

**匹配主题**: flood, climate change
{: .label .label-green }

> 全球变暖预计将加强水文循环，从而增加极端降水事件的强度和洪水风险。然而，这些变化往往与大气中水汽含量随温度升高而增加的理论预期有所不同。本研究分析了气候变化对洪水和极端降水的影响如何随水资源可用性变化。

---

### Flood susceptibility modelling using advanced ensemble machine learning models

**作者**: A. Islam, Swapan Talukdar, Susanta Mahato, Sonali Kundu, K. Eibek, Q. Pham et al.

**期刊**: *Geoscience Frontiers* · **DOI**: [10.1016/j.gsf.2020.09.006](https://doi.org/10.1016/j.gsf.2020.09.006) · **被引次数**: 451

**匹配主题**: flood
{: .label .label-green }

> 由于对财产、基础设施的巨大破坏和人员伤亡，洪水是自然界最具破坏性的灾害之一。本研究采用先进的集成机器学习模型进行洪水易发性建模。

---

### The Global Flood Protection Benefits of Mangroves

**作者**: Pelayo Menéndez, I. Losada, Saúl Torres-Ortega, S. Narayan, M. Beck

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-020-61136-6](https://doi.org/10.1038/s41598-020-61136-6) · **被引次数**: 390

**匹配主题**: flood
{: .label .label-green }

> 沿海洪水风险正在迅速上升。本研究在全球范围内每20公里提供红树林对降低洪水风险的经济价值的高分辨率估计，开发了基于概率和过程的红树林防洪效益评估方法。

---

### Rapid and robust monitoring of flood events using Sentinel-1 and Landsat data on the Google Earth Engine

**作者**: B. DeVries, Chengquan Huang, J. Armston, Wenli Huang, John W. Jones, M. Lang

**期刊**: *Remote Sensing of Environment* · **DOI**: [10.1016/j.rse.2020.111664](https://doi.org/10.1016/j.rse.2020.111664) · **被引次数**: 379

**匹配主题**: flood
{: .label .label-green }

> 合成孔径雷达传感器是洪水灾害规划和应对的不可或缺的数据来源。本研究利用Google Earth Engine平台，使用Sentinel-1和Landsat数据进行快速稳健的洪水事件监测。

---

### Flood susceptibility mapping with machine learning, multi-criteria decision analysis and ensemble using Dempster Shafer Theory

**作者**: Thimmaiah Gudiyangada Nachappa, Sepideh Tavakkoli Piralilou, Khalil Gholamnia, O. Ghorbanzadeh, Omid Rahmati, T. Blaschke

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.125275](https://doi.org/10.1016/j.jhydrol.2020.125275) · **被引次数**: 330

**匹配主题**: flood
{: .label .label-green }

> 洪水是全球最广泛的自然灾害之一。本研究提出了一种新的洪水易发性制图技术，采用基于Dempster-Shafer理论的机器学习、多准则决策分析和集成方法。

---

### Exploring a Long Short-Term Memory based Encoder-Decoder framework for multi-step-ahead flood forecasting

**作者**: I-Feng Kao, Yanlai Zhou, Li-Chiu Chang, F. Chang

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124631](https://doi.org/10.1016/j.jhydrol.2020.124631) · **被引次数**: 328

**匹配主题**: flood
{: .label .label-green }

> 实际洪水控制系统依赖于具有适当提前期的可靠准确预报。本研究首次提出了基于LSTM的编码器-解码器模型用于多步洪水预报。

---

### Flood Detection and Susceptibility Mapping Using Sentinel-1 Remote Sensing Data and a Machine Learning Approach: Hybrid Intelligence of Bagging Ensemble Based on K-Nearest Neighbor Classifier

**作者**: H. Shahabi, A. Shirzadi, K. Ghaderi, E. Omidvar, N. Al‐Ansari, J. Clague et al.

**期刊**: *Remote Sensing* · **DOI**: [10.3390/rs12020266](https://doi.org/10.3390/rs12020266) · **被引次数**: 319

**匹配主题**: flood
{: .label .label-green }

> 洪水易发区域制图是洪水灾害管理的关键活动。本研究提出了基于Sentinel-1遥感数据和机器学习方法的新型洪水检测和易发性制图技术。

---


## 水文预测中的机器学习

深度学习在水文学中的应用在此期间快速发展。Xiang等人在Water Resources Research上发表了基于LSTM序列到序列学习的降雨-径流模型研究，Gao等人解决了GRU和LSTM径流预测中的时间步优化问题。Ding等人引入了可解释的时空注意力LSTM洪水预报模型，在精度和可解释性之间取得平衡。Sit等人对水资源领域的深度学习应用进行了全面综述，涵盖降水、径流、水质和地下水等方面。

### Short-term runoff prediction with GRU and LSTM networks without requiring time step optimization during sample generation

**作者**: Shuai Gao, Yuefei Huang, Shuo Zhang, Jingcheng Han, Guangqian Wang, Meixin Zhang et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.125188](https://doi.org/10.1016/j.jhydrol.2020.125188) · **被引次数**: 553

**匹配主题**: runoff
{: .label .label-green }

> 径流预报是减轻洪水灾害的重要方法。本研究提出了一种使用GRU和LSTM网络进行短期径流预测的方法，无需在样本生成过程中优化时间步长。

---

### A Rainfall‐Runoff Model With LSTM‐Based Sequence‐to‐Sequence Learning

**作者**: Z. Xiang, June Yan, I. Demir

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2019WR025326](https://doi.org/10.1029/2019WR025326) · **被引次数**: 551

**匹配主题**: runoff
{: .label .label-green }

> 降雨-径流建模是一个复杂的非线性时间序列问题。本研究采用基于LSTM的序列到序列学习框架进行降雨-径流建模，展示了深度学习在水文预测中的潜力。

---

### A Comprehensive Review of Deep Learning Applications in Hydrology and Water Resources

**作者**: M. Sit, B. Demiray, Z. Xiang, Gregory Ewing, Y. Sermet, I. Demir

**期刊**: *Water Science and Technology* · **DOI**: [10.31223/osf.io/xs36g](https://doi.org/10.31223/osf.io/xs36g) · **被引次数**: 450

**匹配主题**: hydrology
{: .label .label-green }

> 到2025年，全球数字数据量预计将达到175泽字节。与水相关的数据量、种类和速度因大规模传感器网络而不断增加。本文全面综述了深度学习在水文和水资源领域的应用。

---

### Interpretable spatio-temporal attention LSTM model for flood forecasting

**作者**: Yukai Ding, Yuelong Zhu, Jun Feng, Pengcheng Zhang, Zirun Cheng

**期刊**: *Neurocomputing* · **DOI**: [10.1016/j.neucom.2020.04.110](https://doi.org/10.1016/j.neucom.2020.04.110) · **被引次数**: 354

**匹配主题**: flood
{: .label .label-green }

> 为洪水预报建立可解释的人工智能模型是一项严峻挑战：准确性和可解释性缺一不可。本研究提出了一种可解释的时空注意力LSTM模型用于洪水预报。

---


## 河流系统与水资源

多项重要研究探讨了河流系统和更广泛的水资源挑战。Milly和Dunne在Science上发表了具有里程碑意义的论文，表明变暖驱动的雪盖减少增强蒸发导致科罗拉多河流量持续减少。Maavara等人综述了河流大坝对生物地球化学循环的影响。Tickner等人提出了全球淡水生物多样性紧急恢复计划。Mariotti等人探讨了与水资源管理相关的次季节到季节预报的技巧窗口。Minhas等人综述了灌溉农业中应对盐碱化的策略，Asadollah等人比较了河流水质指数预测的机器学习模型。

### Bending the Curve of Global Freshwater Biodiversity Loss: An Emergency Recovery Plan

**作者**: David Tickner, Jeffrey J. Opperman, Robin Abell, Mike Acreman, Angela H. Arthington, Stuart E. Bunn et al.

**期刊**: *BioScience* · **DOI**: [10.1093/biosci/biaa002](https://doi.org/10.1093/biosci/biaa002) · **被引次数**: 1110

**匹配主题**: hydrology, land surface model, hydropower, irrigation
{: .label .label-green }

> 尽管淡水生态系统空间范围有限，但拥有显著的生物多样性，包括三分之一的脊椎动物物种。全球范围内，湿地消失速度是森林的三倍，淡水脊椎动物种群已大幅下降。本文提出了扭转全球淡水生物多样性损失趋势的紧急恢复计划。

---

### River dam impacts on biogeochemical cycling

**作者**: T. Maavara, Qiuwen Chen, K. V. Van Meter, L. Brown, Jianyun Zhang, J. Ni et al.

**期刊**: *Nature Reviews Earth & Environment* · **DOI**: [10.1038/s43017-019-0019-0](https://doi.org/10.1038/s43017-019-0019-0) · **被引次数**: 642

**匹配主题**: river
{: .label .label-green }

> 河流大坝对碳、氮、磷和硅的生物地球化学循环产生重大影响。本文综述了大坝对这些循环的影响机制。

---

### Colorado River flow dwindles as warming-driven loss of reflective snow energizes evaporation

**作者**: P. Milly, K. Dunne

**期刊**: *Science* · **DOI**: [10.1126/science.aay9187](https://doi.org/10.1126/science.aay9187) · **被引次数**: 329

**匹配主题**: river
{: .label .label-green }

> 干旱和变暖多年来一直在减少科罗拉多河流量。本研究利用水文模型和历史观测表明，这种减少主要是由于雪盖减少导致反照率降低、蒸散发增加所致。

---

### Coping with salinity in irrigated agriculture: Crop evapotranspiration and water management issues

**作者**: P. Minhas, T. Ramos, Alon Ben-Gal, L. S. Pereira

**期刊**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2019.105832](https://doi.org/10.1016/j.agwat.2019.105832) · **被引次数**: 322

**匹配主题**: water management
{: .label .label-green }

> 土壤和水体盐碱化及相关问题是全球粮食生产的重大挑战。本文综述了应对盐碱化的策略，包括更好地理解盐度时空动态对蒸散发和水管理的影响。

---

### Windows of Opportunity for Skillful Forecasts Subseasonal to Seasonal and Beyond

**作者**: Annarita Mariotti, Cory Baggett, Elizabeth A. Barnes, Emily Becker, Amy H. Butler, Dan C. Collins et al.

**期刊**: *Bulletin of the American Meteorological Society* · **DOI**: [10.1175/bams-d-18-0326.1](https://doi.org/10.1175/bams-d-18-0326.1) · **被引次数**: 318

**匹配主题**: water management, seasonal, land surface model, earth system model
{: .label .label-green }

> 对环境条件预测的需求日益增长，预报范围从0-14天天气预报扩展到一个或多个季节及更长时间尺度。本文探讨了次季节到季节预报的技巧窗口。

---

### River water quality index prediction and uncertainty analysis: A comparative study of machine learning models

**作者**: S. Asadollah, A. Sharafati, D. Motta, Z. Yaseen

**期刊**: *Journal of Environmental Chemical Engineering* · **DOI**: [10.1016/j.jece.2020.104599](https://doi.org/10.1016/j.jece.2020.104599) · **被引次数**: 307

**匹配主题**: river
{: .label .label-green }

> 水质指数（WQI）是表征地表水质的最常用指标。本研究引入了一种新的集成机器学习模型用于预测月度水质指数值，并与多种机器学习方法进行了比较。

---


## 统计信息

| 指标 | 数量 |
|:-------|------:|
| 检索数据库 | 2 |
| 检索主题 | 16 |
| 获取论文总数 | 1828 |
| 去重后 | 1509 |
| LLM相关性筛选后 | 31 |
| 排除（不相关） | 1478 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

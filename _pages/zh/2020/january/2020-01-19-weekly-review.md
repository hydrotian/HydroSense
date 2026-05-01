---
layout: default
title: "第03周（1月13日 - 1月19日），31篇"
nav_order: 34
nav_exclude: true
lang: zh
lang_link: /2020/january/2020-01-19-weekly-review
date: 2020-01-19
categories: [weekly-zh, 2020, january]
tags: [hydrology, literature-review, research]
paper_count: 31
highlight: "CESM2模型文档引领本周，同时涌现洪水风险机器学习、干旱监测框架和灌溉—气候反馈等重要进展，首次从全球尺度证明灌溉可显著抑制极端高温。"
---

# 每周文献综述
{: .no_toc }

**第03周** · 2020年1月13日–19日
{: .text-grey-dk-000 }

**31** 篇相关论文，涵盖 **6** 个主题
{: .fs-5 .fw-300 }

## 摘要

CESM2的里程碑式文档是本周最受关注的论文，同时气候—水文相互作用研究也取得重要进展，包括基于机器学习的洪水风险制图和实时雨水管理系统等。干旱研究在多个方向取得突破——从基于GRACE的干旱指标到跨越六个世纪的欧洲俄罗斯干旱重建。灌溉研究揭示了扩大灌溉面积可在全球范围内显著抑制极端高温。水文建模领域则涌现了生态系统服务模型的对比评估，以及冰川融水对中亚河流径流贡献的新证据。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 地球系统模型与气候建模

CESM2——最广泛使用的地球系统模型之一——的详细文档是本周引用最高的论文，全面介绍了其大气-海洋-陆面-冰盖耦合组件及开发过程中的挑战。与此同时，NorESM2的海洋生物地球化学模块也得到详细描述，将CMIP6时代的模型文档扩展到碳循环领域。HighResMIP多模式分析表明，将大气分辨率提高到约25公里可以显著改善热带气旋模拟，对极端降水预估具有直接意义。

### The Community Earth System Model Version 2 (CESM2)

**作者**: Gökhan Danabasoglu, Jean‐François Lamarque, Julio T. Bacmeister, David A. Bailey, Alice K. DuVivier, James Edwards et al.

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2019ms001916](https://doi.org/10.1029/2019ms001916) · **引用**: 3126

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 本文全面介绍了CESM2（社区地球系统模型第2版），讨论了开发过程中遇到的挑战及其解决方案。除描述各组件模型及其耦合外，还重点介绍了陆面、海冰和海洋生物地球化学方面的显著改进。

---

### Ocean biogeochemistry in the Norwegian Earth System Model version 2 (NorESM2)

**作者**: J. Tjiputra, J. Schwinger, M. Bentsen, A. Morée, Shuang Gao, I. Bethke et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-2019-347](https://doi.org/10.5194/gmd-2019-347) · **引用**: 119

**匹配主题**: earth system model
{: .label .label-green }

> 海洋碳循环通过调节大气二氧化碳浓度在气候系统中发挥关键作用。本研究描述了NorESM2的海洋生物地球化学组件，并对关键生物地球化学示踪物和通量进行了评估。

---

### Impact of Model Resolution on Tropical Cyclone Simulation Using the HighResMIP–PRIMAVERA Multimodel Ensemble

**作者**: Malcolm Roberts, Joanne Camp, Jon Seddon, Pier Luigi Vidale, Kevin I. Hodges, Benoît Vannière et al.

**期刊**: *Journal of Climate* · **DOI**: [10.1175/jcli-d-19-0639.1](https://doi.org/10.1175/jcli-d-19-0639.1) · **引用**: 316

**匹配主题**: hydrologic model, land surface model, earth system model
{: .label .label-green }

> 基于CMIP6 HighResMIP通用强迫协议，六个建模团队完成了1950-2014年的多模式多分辨率模拟。分析表明，将分辨率从约100公里提高到约25公里可显著改善热带气旋强度、路径和季节循环的模拟效果。

---

## 洪水风险评估与预报

本周洪水研究涵盖了观测、建模和管理多个方面。Hunt和Menon将2018年喀拉拉邦灾难性洪水归因于气候变暖加剧的三个天气系统罕见交汇。在美国，Khajehei等人首次完成了全国范围的空间显式山洪脆弱性评估。Sadler等人证明了实时控制城市雨水系统可在海平面上升情景下有效降低洪水风险。Thanh等人在湄公河三角洲的研究揭示了上游堤坝建设如何将洪峰重新分配到下游未保护区域。

### The 2018 Kerala floods: a climate change perspective

**作者**: Kieran M. R. Hunt, Arathy Menon

**期刊**: *Climate Dynamics* · **DOI**: [10.1007/s00382-020-05123-7](https://doi.org/10.1007/s00382-020-05123-7) · **引用**: 252

**匹配主题**: hydrology, hydrologic model, streamflow, flood, land surface model, climate change, earth system model
{: .label .label-green }

> 2018年8月，印度喀拉拉邦因月初低压系统随后数天内两条大气河流的影响而遭受持续强降雨。本研究从气候变化角度分析该事件，发现人为变暖将此类极端降水的发生概率提高了1.2至3.2倍。

---

### A Place-based Assessment of Flash Flood Hazard and Vulnerability in the Contiguous United States

**作者**: Sepideh Khajehei, Ali Ahmadalipour, Wanyun Shao, Hamid Moradkhani

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-019-57349-z](https://doi.org/10.1038/s41598-019-57349-z) · **引用**: 135

**匹配主题**: hydrologic model, streamflow, flood
{: .label .label-green }

> 山洪是最具破坏性的自然灾害之一。本研究开发了一个基于地点的评估框架，将山洪危险性与社会脆弱性指标相结合，识别出美国东南部和阿巴拉契亚地区的高风险热点。

---

### Exploring real-time control of stormwater systems for mitigating flood risk due to sea level rise

**作者**: Jeffrey M. Sadler, Jonathan L. Goodall, Madhur Behl, Benjamin D. Bowes, Mohamed M. Morsy

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124571](https://doi.org/10.1016/j.jhydrol.2020.124571) · **引用**: 89

**匹配主题**: water management, flood
{: .label .label-green }

> 本研究探索了实时控制雨水基础设施在应对海平面上升引起的沿海城市洪水风险中的潜力。结果表明，在多种海平面上升情景下，动态管理的蓄洪池和排水闸可显著减少洪水量。

---

### Flooding in the Mekong Delta: the impact of dyke systems on downstream hydrodynamics

**作者**: Vo Quoc Thanh, Dano Roelvink, Mick van der Wegen, Johan Reyns, Herman Kernkamp, Giap Van Vinh et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-189-2020](https://doi.org/10.5194/hess-24-189-2020) · **引用**: 50

**匹配主题**: hydrology, streamflow, water management, flood, hydropower
{: .label .label-green }

> 建设高堤是越南湄公河三角洲应对洪水和管理农业的常见措施。然而，高堤建设导致下游地区水动力发生显著变化，将洪峰重新分配到未受保护的区域，增加了下游的洪水风险。

---

### InSAR Maps of Land Subsidence and Sea Level Scenarios to Quantify the Flood Inundation Risk in Coastal Cities: The Case of Singapore

**作者**: João Catalão, Durairaju Raju, Giovanni Nico

**期刊**: *Remote Sensing* · **DOI**: [10.3390/rs12020296](https://doi.org/10.3390/rs12020296) · **引用**: 57

**匹配主题**: flood, land surface model
{: .label .label-green }

> 与全球变暖相关的全球平均海平面上升对沿海地区产生重大影响。本研究将InSAR地面沉降速率与海平面上升预测相结合，量化新加坡的洪水淹没风险，表明地面沉降会放大低洼沿海地区的有效海平面上升威胁。

---

## 干旱分析与监测

干旱研究在不同空间尺度和时间范围内均取得了进展。Gerdener等人提出了将GRACE总水储量异常系统性转化为业务化干旱指标的框架，填补了卫星重力测量与水文干旱监测之间的空白。Wu等人分析了中国干热复合事件的联合特征，发现自20世纪90年代以来显著加剧。Cook等人编制的六百年欧洲俄罗斯干旱图谱扩展了树轮干旱重建的空间覆盖范围。Diaz等人提出了新方法来表征干旱事件的时空演变动态。

### Evaluation of severity changes of compound dry and hot events in China based on a multivariate multi-index approach

**作者**: Xinying Wu, Zengchao Hao, Xuan Zhang, Chong Li, Fanghua Hao

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124580](https://doi.org/10.1016/j.jhydrol.2020.124580) · **引用**: 139

**匹配主题**: drought
{: .label .label-green }

> 本研究采用多变量多指标方法评估中国干热复合事件的严重程度变化，捕捉温度和降水极值的联合行为。结果显示自20世纪90年代以来复合事件显著加剧，华北地区增幅最大。

---

### An approach to characterise spatio-temporal drought dynamics

**作者**: Vitali Diaz, Gerald A. Corzo Perez, H.A.J. van Lanen, Dimitri Solomatine, Emmanouil Α. Varouchakis

**期刊**: *Advances in Water Resources* · **DOI**: [10.1016/j.advwatres.2020.103512](https://doi.org/10.1016/j.advwatres.2020.103512) · **引用**: 115

**匹配主题**: drought
{: .label .label-green }

> 干旱的时空监测是一项复杂任务。本研究提出了一种表征干旱事件时空动态的新方法，从静态快照转向追踪干旱的发生、传播和消退过程，将其作为连续的时空对象进行跟踪。

---

### Harmonization of Landsat and Sentinel 2 for Crop Monitoring in Drought Prone Areas: Case Studies of Ninh Thuan (Vietnam) and Bekaa (Lebanon)

**作者**: Minh Nguyen, Oscar M. Baez‐Villanueva, Duong Du Bui, Phong Nguyen, Lars Ribbe

**期刊**: *Remote Sensing* · **DOI**: [10.3390/rs12020281](https://doi.org/10.3390/rs12020281) · **引用**: 106

**匹配主题**: drought, land surface model
{: .label .label-green }

> 农场级别的卫星作物监测通常需要中高空间分辨率的近日常影像。本研究展示了Landsat 8和Sentinel 2数据的融合应用于越南和黎巴嫩干旱易发地区的作物监测，实现了对干旱影响评估至关重要的近日常时间分辨率。

---

### The European Russia Drought Atlas (1400–2016 CE)

**作者**: Edward R. Cook, Olga N Solomina, Vladimir V Matskovsky, Benjamin I. Cook, Leonid Agafonov, A. A. Tkach et al.

**期刊**: *Climate Dynamics* · **DOI**: [10.1007/s00382-019-05115-2](https://doi.org/10.1007/s00382-019-05115-2) · **引用**: 83

**匹配主题**: drought
{: .label .label-green }

> 本研究基于树轮年表，呈现了1400年至2016年欧洲俄罗斯夏季干旱变率的网格化重建——欧洲俄罗斯干旱图谱。该图谱填补了全球干旱图谱网络中的关键空间空白，揭示了与大尺度气候模态相关的多年代际干旱振荡。

---

### A framework for deriving drought indicators from the Gravity Recovery and Climate Experiment (GRACE)

**作者**: Helena Gerdener, Olga Engels, Jürgen Kusche

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-227-2020](https://doi.org/10.5194/hess-24-227-2020) · **引用**: 59

**匹配主题**: hydrology, hydrologic model, streamflow, drought, land surface model
{: .label .label-green }

> 回顾性地识别和量化干旱对于更好地理解干旱条件及其在水文循环中的传播至关重要。本研究提出了一个从GRACE卫星重力数据推导干旱指标的系统框架，展示了如何将总水储量异常分解为地下水、土壤水分和地表水干旱信号。

---

## 水资源管理与灌溉

Thiery等人在Nature Communications上发表的研究首次提供了多模式全球证据，表明灌溉扩张可显著抑制极端高温，量化了此前假设但约束不足的陆-气反馈。中亚在1.5°C和2.0°C变暖目标下的农业需水量预测显示灌溉需求将大幅增加。Zohaib和Choi利用卫星数据绘制了全球灌溉用水趋势。政策导向的研究则探讨了灌溉用水再利用的安全监管、跨流域调水的可持续性，以及浮式太阳能在水电站水库上的运行权衡。

### Warming of hot extremes alleviated by expanding irrigation

**作者**: Wim Thiery, A.J. Visser, Erich Fischer, Mathias Hauser, Annette L. Hirsch, David M. Lawrence et al.

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-019-14075-4](https://doi.org/10.1038/s41467-019-14075-4) · **引用**: 237

**匹配主题**: hydrology, hydrologic model, land surface model, irrigation, earth system model
{: .label .label-green }

> 灌溉影响全球多个地区的气候条件，尤其是极端高温。本研究利用多个地球系统模型表明，灌溉扩张在局地尺度上使最热日降温0.78°C，并在区域尺度上产生可测量的降温效应。

---

### Regulating water reuse for agricultural irrigation: risks related to organic micro-contaminants

**作者**: Manuela Helmecke, Elke Fries, Christoph Schulte

**期刊**: *Environmental Sciences Europe* · **DOI**: [10.1186/s12302-019-0283-0](https://doi.org/10.1186/s12302-019-0283-0) · **引用**: 237

**匹配主题**: land surface model, irrigation
{: .label .label-green }

> 越来越多的国家将再生水灌溉视为保障和增强农业生产的机会。尽管水的再利用有诸多好处，但科学界对再生水中有机微污染物及其作物吸收的潜在风险提出了关注，需要建立基于风险的监管框架。

---

### Floating photovoltaic plants: Ecological impacts versus hydropower operation flexibility

**作者**: Jannik Haas, J. Khalighi, Alberto de la Fuente, Sabine U. Gerbersdorf, Wolfgang Nowak, Po-Jung Chen

**期刊**: *Energy Conversion and Management* · **DOI**: [10.1016/j.enconman.2019.112414](https://doi.org/10.1016/j.enconman.2019.112414) · **引用**: 162

**匹配主题**: water management, hydropower
{: .label .label-green }

> 本研究评估了在水电站水库上部署浮式光伏装置的生态影响和运行权衡。结果表明，太阳能-水电混合系统可增加总发电量并减少蒸发损失，但对水库分层和光照穿透的生态影响需要谨慎管理。

---

### Agricultural water demands in Central Asia under 1.5 °C and 2.0 °C global warming

**作者**: Zhi Li, Gonghuan Fang, Yaning Chen, Weili Duan, Yerbolat Mukanov

**期刊**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2020.106020](https://doi.org/10.1016/j.agwat.2020.106020) · **引用**: 109

**匹配主题**: irrigation
{: .label .label-green }

> 本研究预测了中亚在《巴黎协定》1.5°C和2.0°C变暖目标下的农业需水量。结果显示，受蒸散发增加驱动，灌溉用水需求将大幅增长，咸海流域在两种情景下均面临最严重的水资源压力。

---

### Satellite-based global-scale irrigation water use and its contemporary trends

**作者**: Muhammad Zohaib, Minha Choi

**期刊**: *The Science of The Total Environment* · **DOI**: [10.1016/j.scitotenv.2020.136719](https://doi.org/10.1016/j.scitotenv.2020.136719) · **引用**: 92

**匹配主题**: irrigation
{: .label .label-green }

> 本研究利用卫星遥感数据估算全球灌溉用水量并分析其当代趋势。基于卫星的方法提供了灌溉耗水量的空间显式估计，揭示了南亚和东亚的增长趋势以及美国西部部分地区的下降趋势。

---

### Are intra- and inter-basin water transfers a sustainable policy intervention for addressing water scarcity?

**作者**: Logan Purvis, Ariel Dinar

**期刊**: *Water Security* · **DOI**: [10.1016/j.wasec.2019.100058](https://doi.org/10.1016/j.wasec.2019.100058) · **引用**: 67

**匹配主题**: water management
{: .label .label-green }

> 本研究批判性地审视了跨流域调水作为应对水资源短缺的政策手段，评估了全球主要调水工程的经济、环境和社会可持续性。分析表明，虽然调水可以缓解局部缺水，但往往在水源流域造成新的脆弱性，且很少解决需求侧的根本驱动因素。

---

## 水文建模与流域过程

模型对比与评估是本主题的主线。Cong等人对SWAT和InVEST进行了并排比较，量化水文生态系统服务。Cook等人证明，在为气候变化更新IDF曲线时，建模选择引入的不确定性可能大于气候信号本身。Li等人分离了塔里木河源区冰川融水与降水对径流的贡献，发现冰川融水占1971-2010年增量的40%。Nguyen等人通过将多变量频率偏差校正与水库蓄水可靠性评估相结合，推进了水库运行建模。

### Comparison of the SWAT and InVEST models to determine hydrological ecosystem service spatial patterns, priorities and trade-offs in a complex basin

**作者**: Wencui Cong, Xiaoyin Sun, Hongwei Guo, Ruifeng Shan

**期刊**: *Ecological Indicators* · **DOI**: [10.1016/j.ecolind.2020.106089](https://doi.org/10.1016/j.ecolind.2020.106089) · **引用**: 251

**匹配主题**: hydrologic model, water management
{: .label .label-green }

> 生态系统服务评估模型是决策者和研究人员的重要工具。本研究比较了SWAT和InVEST在水文生态系统服务制图方面的表现，包括产水量、水质净化和泥沙拦截，发现空间格局存在显著差异，对确定保护投资优先级具有重要意义。

---

### The effect of modeling choices on updating intensity-duration-frequency curves and stormwater infrastructure designs for climate change

**作者**: Lauren M. Cook, Seth McGinnis, Constantine Samaras

**期刊**: *Climatic Change* · **DOI**: [10.1007/s10584-019-02649-6](https://doi.org/10.1007/s10584-019-02649-6) · **引用**: 98

**匹配主题**: hydrology, hydrologic model, climate change
{: .label .label-green }

> 暴雨强度-历时-频率（IDF）曲线常用于雨水基础设施设计中表征极端降雨特征，正逐步更新以反映预期的降水变化。本研究表明，降尺度方法、极值分布和偏差校正的选择可引入与气候变化信号相当甚至更大的不确定性。

---

### Neural network modeling for groundwater-level forecasting in coastal aquifers

**作者**: Thendiyath Roshni, Madan K. Jha, J. Drisya

**期刊**: *Neural Computing and Applications* · **DOI**: [10.1007/s00521-020-04722-z](https://doi.org/10.1007/s00521-020-04722-z) · **引用**: 92

**匹配主题**: hydrologic model
{: .label .label-green }

> 本研究将LSTM和小波耦合架构等神经网络模型应用于印度沿海含水层的地下水位预测。结果表明，小波-LSTM混合模型优于传统方法，能够捕捉受潮汐和补给信号影响的地下水动态中的季节性模式和长期趋势。

---

### Impacts of future climate and land use change on water yield in a semiarid basin in Iran

**作者**: Bagher Shirmohammadi Chelan, Arash Malekian, Ali Salajegheh, Bahram Taheri, Hossein Azarnivand, Žiga Malek et al.

**期刊**: *Land Degradation and Development* · **DOI**: [10.1002/ldr.3554](https://doi.org/10.1002/ldr.3554) · **引用**: 78

**匹配主题**: hydrology, hydrologic model, streamflow, water management, land surface model, irrigation
{: .label .label-green }

> 研究水文、土地利用和气候变化之间的相互作用对于支持可持续水资源管理至关重要。本研究模拟了伊朗半干旱流域气候和土地利用变化对产水量的综合影响，发现在干旱化条件下的农业扩张可能导致产水量减少高达35%。

---

### Partitioning the contributions of glacier melt and precipitation to the 1971–2010 runoff increases in a headwater basin of the Tarim River

**作者**: Zehua Li, Xiaogang Shi, Qiuhong Tang, Yongqiang Zhang, Huilin Gao, Xicai Pan et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124579](https://doi.org/10.1016/j.jhydrol.2020.124579) · **引用**: 73

**匹配主题**: hydrologic model, river, runoff
{: .label .label-green }

> 本研究分离了冰川融水和降水对塔里木河源区库玛拉克河1971-2010年径流增加的贡献。结果表明，冰川融水约占径流增量的40%，降水变化贡献了其余部分。

---

### Assessment of Climate Change Impacts on Reservoir Storage Reliability, Resilience, and Vulnerability Using a Multivariate Frequency Bias Correction Approach

**作者**: Ha H. Nguyen, Rajeshwar Mehrotra, Ashish Sharma

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2019wr026022](https://doi.org/10.1029/2019wr026022) · **引用**: 65

**匹配主题**: hydrologic model, runoff, streamflow, reservoir, climate change
{: .label .label-green }

> 全球或区域气候模式的原始模拟很少直接用于流域尺度的水文影响评估或水库蓄水变化研究。本研究开发了一种多变量频率偏差校正方法，并将其应用于评估澳大利亚某流域水库蓄水可靠性、恢复力和脆弱性受气候变化的影响。

---

### Mapping groundwater resiliency under climate change scenarios: A case study of Kathmandu Valley, Nepal

**作者**: Sangam Shrestha, Sanjiv Neupane, S. Mohanasundaram, Vishnu Prasad Pandey

**期刊**: *Environmental Research* · **DOI**: [10.1016/j.envres.2020.109149](https://doi.org/10.1016/j.envres.2020.109149) · **引用**: 59

**匹配主题**: hydrologic model, water management, climate change
{: .label .label-green }

> 本研究在快速城市化的加德满都谷地，对多种气候变化情景下的地下水恢复力进行了制图。利用地表水-地下水耦合模型，预测在大多数情景下地下水位将下降，到2050年代季风降水变化将导致补给减少15-30%。

---

### Improvement of seasonal runoff and soil loss predictions by the MMF (Morgan-Morgan-Finney) model after wildfire and soil treatment in Mediterranean forest ecosystems

**作者**: Demetrio Antonio Zema, João Pedro Nunes, Manuel Esteban Lucas‐Borja

**期刊**: *CATENA* · **DOI**: [10.1016/j.catena.2019.104415](https://doi.org/10.1016/j.catena.2019.104415) · **引用**: 59

**匹配主题**: hydrology, hydrologic model, runoff, water management, seasonal, land surface model
{: .label .label-green }

> 本研究改进了Morgan-Morgan-Finney（MMF）模型，用于预测受野火影响的地中海森林生态系统的季节性径流和土壤流失。对包括覆盖在内的火后土壤处理进行了评估，表明改进后的模型能够捕捉火灾后径流增加及恢复处理后径流减少的过程。

---

## 气候对水资源与河流系统的影响

河流系统成为气候与人类压力的重要指标。Hackney等人在Nature Sustainability上发表的研究记录了湄公河不可持续的采砂活动如何以远超自然侵蚀的速率破坏河岸稳定性，威胁基础设施和生计。Norris等人发现局地山地环流放大是喜马拉雅中部加速变暖和干旱化的驱动机制，对下游供水产生级联影响。Liu和Wang分析了38年的登陆热带气旋降水数据，发现沿海地区洪水风险正在重塑。

### River bank instability from unsustainable sand mining in the lower Mekong River

**作者**: Christopher Hackney, Stephen E. Darby, Daniel R. Parsons, Julian Leyland, Jim Best, R. E. Aalto et al.

**期刊**: *Nature Sustainability* · **DOI**: [10.1038/s41893-019-0455-3](https://doi.org/10.1038/s41893-019-0455-3) · **引用**: 313

**匹配主题**: hydrology, river, hydropower
{: .label .label-green }

> 本研究记录了湄公河下游不可持续的采砂活动如何导致远超自然背景速率的河岸侵蚀。利用数十年的卫星影像和水深测量数据，作者表明采砂使河床降低了多达1.4米，引发河岸后退，威胁沿河社区和基础设施。

---

### Evaluating the effects of climate change on precipitation and temperature for Iran using RCP scenarios

**作者**: Shahab Doulabian, Saeed Golian, Amirhossein Shadmehri Toosi, Conor Murphy

**期刊**: *Journal of Water and Climate Change* · **DOI**: [10.2166/wcc.2020.114](https://doi.org/10.2166/wcc.2020.114) · **引用**: 130

**匹配主题**: hydrology, hydrologic model, climate change
{: .label .label-green }

> 气候变化已导致全球水文过程和气候条件发生诸多变化。本研究评估了RCP情景下伊朗降水和温度的预测变化，发现空间响应具有异质性——北部地区冬季降水增加，而南部地区面临加剧的干旱化，对水资源规划具有直接意义。

---

### Warming and drying over the central Himalaya caused by an amplification of local mountain circulation

**作者**: Jesse Norris, Leila M. V. Carvalho, Charles Jones, Forest Cannon

**期刊**: *npj Climate and Atmospheric Science* · **DOI**: [10.1038/s41612-019-0105-5](https://doi.org/10.1038/s41612-019-0105-5) · **引用**: 95

**匹配主题**: hydrology, hydrologic model, land surface model, hydropower
{: .label .label-green }

> 喜马拉雅中部的气候变化对下游数亿人口的水资源至关重要。本研究将局地山地环流放大确定为喜马拉雅中部加速变暖和干旱化的机制，对冰川物质平衡和季风补给的河流系统具有重要影响。

---

### Trends in Landfalling Tropical Cyclone–Induced Precipitation over China

**作者**: Lu Liu, Yuqing Wang

**期刊**: *Journal of Climate* · **DOI**: [10.1175/jcli-d-19-0693.1](https://doi.org/10.1175/jcli-d-19-0693.1) · **引用**: 87

**匹配主题**: land surface model
{: .label .label-green }

> 本研究分析了1980-2017年登陆中国的热带气旋降水趋势。结果表明，虽然热带气旋频率有所下降，但每次热带气旋产生的降水强度增加，与变暖条件下的热力学预期一致。这种增强在中国东南部最为显著，正在重塑区域洪水风险。

---

### Global satellite-based river gauging and the influence of river morphology on its application

**作者**: Jiawei Hou, Albert I. J. M. van Dijk, Hylke E. Beck

**期刊**: *Remote Sensing of Environment* · **DOI**: [10.1016/j.rse.2019.111629](https://doi.org/10.1016/j.rse.2019.111629) · **引用**: 55

**匹配主题**: hydrologic model, river, drought
{: .label .label-green }

> 本研究利用卫星测高评估全球基于卫星的河流水位测量，并展示河流形态特征如何影响流量估算的准确性。分析确定了河道几何形状、坡度和洪泛平原连通性是决定卫星测量能否补充或替代实地观测的关键因素。

---

## 统计信息

| 指标 | 数量 |
|:-------|------:|
| 搜索数据库 | 2 |
| 搜索主题 | 16 |
| 获取论文总数 | 1128 |
| 去重后 | 721 |
| LLM相关性筛选后 | 31 |
| 排除（不相关） | 690 |

### 各期刊论文数

| 期刊 | 论文数 |
|:--------|-------:|
| Journal of Hydrology | 3 |
| Journal of Climate | 3 |
| Climate Dynamics | 2 |
| Remote Sensing | 3 |
| Nature Communications | 1 |
| Nature Sustainability | 1 |
| Hydrology and Earth System Sciences | 2 |
| Water Resources Research | 1 |
| Scientific Reports | 1 |
| Energy Conversion and Management | 1 |
| Agricultural Water Management | 1 |
| Climatic Change | 1 |
| Advances in Water Resources | 1 |
| Environmental Sciences Europe | 1 |
| Ecological Indicators | 1 |
| Journal of Advances in Modeling Earth Systems | 1 |
| Geoscientific Model Development | 1 |
| Land Degradation and Development | 1 |
| CATENA | 1 |
| Neural Computing and Applications | 1 |
| Water Security | 1 |
| Journal of Water and Climate Change | 1 |
| npj Climate and Atmospheric Science | 1 |
| Remote Sensing of Environment | 1 |
| Environmental Research | 1 |
| The Science of The Total Environment | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

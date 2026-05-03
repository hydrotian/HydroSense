---
layout: default
title: "第06周（2月3日 - 2月9日），43篇"
nav_order: 34
nav_exclude: true
lang: zh
lang_link: /2020/february/2020-02-09-weekly-review
date: 2020-02-09
categories: [weekly-zh, 2020, february]
tags: [hydrology, literature-review, research]
paper_count: 43
highlight: "World-Wide HYPE全球流域模型和英国CMIP6地球系统模型的里程碑式发布，以及多冻土水文模型对比揭示主流陆面模型对土壤水分预测的显著分歧。"
---

# 每周文献综述
{: .no_toc }

**第06周** · 2020年2月3日–2月9日
{: .text-grey-dk-000 }

在**6**个主题中发现**43**篇相关论文
{: .fs-5 .fw-300 }

## 摘要

全球尺度水文建模在本周取得重大进展：World-Wide HYPE（WWH）模型首次实现了流域建模技术在全球尺度上对河流流量的验证，英国地球系统模型为CMIP6完成正式文档化，JULES-GL7陆面配置也同步发布。一项多模型冻土水文对比研究揭示，尽管降水量预计增加，大多数陆面模型仍预测表层土壤将长期干燥，突出了高纬度水循环预测中的关键不确定性。同时，机器学习方法在卫星-站点降水融合和基于LSTM的径流预报中持续推进，一项全球评估量化了约一万种鱼类因水坝造成的栖息地连通性影响。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 全球水文与地球系统建模

本周涌现出大量推进全球尺度建模能力的论文。英国地球系统模型HadGEM3-GC3.1和UKESM1为CMIP6正式发布文档，其配套的JULES-GL7陆面配置也同步发布。一项开创性的冻土区模型对比研究揭示，尽管降水预计增加，大多数陆面模型仍预测表层土壤长期干燥，且各模型在径流和蒸散发分配上存在显著分歧。WWH全球流域模型证明了利用开放数据和逐步参数估计进行全球流域建模的可行性，同时相关研究分别考察了高分辨率大气模型的有效分辨率及陆地生物圈模型对降雨操控实验的模拟能力。ORCHIDEE陆面模型完成了灌溉方案改进，一种动态模型数据平均方法被提出用于将全球水文模型与GRACE观测结合。

### Implementation of U.K. Earth System Models for CMIP6

**作者**: Alistair Sellar, Jeremy Walton, Colin Jones, Richard Wood, Nathan Luke Abraham, Mirosław Andrejczuk et al.

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2019ms001946](https://doi.org/10.1029/2019ms001946) · **引用次数**: 299

**匹配主题**: earth system model
{: .label .label-green }

> 本文描述了为CMIP6核心实验集贡献的两个模型的科学和技术实现。所使用的模型包括物理大气-陆地-海洋-海冰模型HadGEM3-GC3.1和在其基础上增加碳氮循环及大气化学的地球系统模型UKESM1。

---

### Soil moisture and hydrology projections of the permafrost region – a model intercomparison

**作者**: C. Andresen, D. Lawrence, C. Wilson, A. McGuire, C. Koven, K. Schaefer et al.

**期刊**: *The Cryosphere* · **DOI**: [10.5194/TC-14-445-2020](https://doi.org/10.5194/TC-14-445-2020) · **引用次数**: 178

**匹配主题**: hydrology, hydrologic model, runoff, land surface model, surface water, earth system model
{: .label .label-green }

> 本研究调查和比较了具有冻土过程的主流陆面模型的土壤水分和水文预测。气候模型预测更高的温度和降水量，这将加强陆面模型中的蒸散发和径流。然而，大多数模型预测冻土区表层土壤（0-20厘米）将长期干燥，尽管深层会变湿。

---

### Global catchment modelling using World-Wide HYPE (WWH), open data, and stepwise parameter estimation

**作者**: Berit Arheimer, Rafael Pimentel, Kristina Isberg, Louise Crochemore, Jafet Andersson, Abdulghani Hasan et al.

**期��**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-535-2020](https://doi.org/10.5194/hess-24-535-2020) · **引用次数**: 177

**匹配主题**: hydrology, hydrologic model, streamflow, land surface model, hydropower
{: .label .label-green }

> 流域水文学的最新进展使得在大范围内对无测站流域应用流域模型成为可能。本文首次展示了在全球尺度上应用流域建模技术并对河流流量进行验证的前沿案例研��。

---

### Effective resolution in high resolution global atmospheric models for climate studies

**作者**: Remko Klaver, Rein Haarsma, Pier Luigi Vidale, Wilco Hazeleger

**期刊**: *Atmospheric Science Letters* · **DOI**: [10.1002/asl.952](https://doi.org/10.1002/asl.952) · **引用次数**: 103

**匹配主题**: earth system model
{: .label .label-green }

> 本研究基于动能谱估算了CMIP6新一代全球气候模型中大气模型能够解析的空间尺度范围（即有效分辨率），对六个最先进的全球气候模型在至少两种水平分辨率下的模拟结果进行了分析。

---

### Rainfall manipulation experiments as simulated by terrestrial biosphere models: Where do we stand?

**作者**: Athanasios Paschalis, Simone Fatichi, Jakob Zscheischler, Philippe Ciais, Michael Bahn, Lena Boysen et al.

**期刊**: *Global Change Biology* · **DOI**: [10.1111/gcb.15024](https://doi.org/10.1111/gcb.15024) · **引用次数**: 91

**匹配主题**: earth system model
{: .label .label-green }

> 降雨量和降雨模式的变化已被观测到并预计将在近期持续。本文展示了一项新的模型-数据对比项目，测试了10个陆地生物圈模型再现生态系统生产力对降雨变化敏感性的能力。

---

### JULES-GL7: the Global Land configuration of the Joint UK Land Environment Simulator version 7.0 and 7.2

**作者**: A. Wiltshire, Maria Carolina Duran Rojas, John Edwards, Nicola Gedney, Anna Harper, Andrew James Hartley et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-13-483-2020](https://doi.org/10.5194/gmd-13-483-2020) · **��用次数**: 60

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 本文介绍了JULES模型在CMIP6中使用的最新全球陆面配置，包括JULES-GL7.0（CMIP6基准配置）和JULES-GL7.2（用于业务天气预报的改进版本）。

---

### Improvement of the Irrigation Scheme in the ORCHIDEE Land Surface Model and Impacts of Irrigation on Regional Water Budgets Over China

**作者**: Zun Yin, Xuhui Wang, Catherine Ottlé, Feng Zhou, Matthieu Guimberteau, Jan Polcher et al.

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2019ms001770](https://doi.org/10.1029/2019ms001770) · **引用次数**: 54

**匹配主题**: land surface model, surface water, irrigation
{: .label .label-green }

> 本研究改进了ORCHIDEE陆面模型中的灌溉方案，并评估了灌溉在水资源限制条件下对中国区域水量平衡的影响。

---

### Comparing global hydrological models and combining them with GRACE by dynamic model data averaging (DMDA)

**作者**: Nooshin Mehrnegar, Owen Jones, Michael Bliss Singer, Maike Schumacher, Paul Bates, Ehsan Forootan

**期刊**: *Advances in Water Resources* · **DOI**: [10.1016/j.advwatres.2020.103528](https://doi.org/10.1016/j.advwatres.2020.103528) · **引用次数**: 32

**匹配��题**: hydrologic model, land surface model, surface water
{: .label .label-green }

> 本研究比较了全球水文模型，并提出了一种动态模型数据平均方法，将全球水文模型与GRACE卫星观测结合，以改进陆地水储量估算。

---

## 水文学中的机器学习与数据驱动方法

机器学习方法在水文应用中取得重要进展。一个时空深度融合模型在中国范围内实现了卫星与站点降水数据的高精度融合，改进的LSTM网络在长江上游径流预报中表现出色。此外，基于深度学习的社交媒体洪水照片筛选系统原型展示了人工智能在水文学中不断拓展的应用范围。

### A spatiotemporal deep fusion model for merging satellite and gauge precipitation in China

**作者**: Hongcai Wu, Qinli Yang, Jiaming Liu, Guoqing Wang

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124664](https://doi.org/10.1016/j.jhydrol.2020.124664) · **引用次数**: 236

**匹配主题**: water management
{: .label .label-green }

> 本研究开发了一个时空深度融合模型，用于在中国范围内融合卫星和地面站点降水数据，利用深度学习捕获降水场的复杂时空模式。

---

### An improved long short-term memory network for streamflow forecasting in the upper Yangtze River

**作者**: Shuang Zhu, Xiangang Luo, Xiaohui Yuan, Zhanya Xu

**期刊**: *Stochastic Environmental Research and Risk Assessment* · **DOI**: [10.1007/s00477-020-01766-4](https://doi.org/10.1007/s00477-020-01766-4) · **引用次数**: 139

**匹配主题**: river, streamflow
{: .label .label-green }

> 本研究提出了一种改进的长短期记忆（LSTM）网络用于长江上游径流预报，与传统方法相比显著提升了预测性能。

---

### Prototyping a Social Media Flooding Photo Screening System Based on Deep Learning

**作者**: Huan Ning, Zhenlong Li, Michael E. Hodgson, Cuizhen Wang

**期刊**: *ISPRS International Journal of Geo-Information* �� **DOI**: [10.3390/ijgi9020104](https://doi.org/10.3390/ijgi9020104) · **引用次数**: 50

**匹��主题**: flood
{: .label .label-green }

> 本文实现了一个基于深度学习的原型筛选系统，用于从社交媒体中识别洪水相关照片。该系统包括推文/图片下载、洪水照片检测和用于人工验证的WebGIS应用，可为决策者提供免费、及时、可靠的洪水事件视觉信息。

---

## 遥感与卫星水文学

卫星遥感持续拓展水文科学的观测基础。一系列GRACE相关研究推进了陆地水储量数据降尺度方法和中国流域尺度蒸散发评估，GIEMS-2数据集将全球地表水面积监测扩展至25年记录。聚焦青藏高原的研究量化了长期土壤水分动态和陆地水储量对气候变化的响应，凸显了卫星观测在数据稀缺区域的关键作用。多种遥感干旱指数被比较用于长白山地区干旱监测。

### Statistical Applications to Downscale GRACE-Derived Terrestrial Water Storage Data and to Fill Temporal Gaps

**作者**: Hossein Sahour, Mohamed Sultan, Mehdi Vazifedan, Karem Abdelmohsen, Sita Karki, John A. Yellich et al.

**期刊**: *Remote Sensing* · **DOI**: [10.3390/rs12030533](https://doi.org/10.3390/rs12030533) · **引用次数**: 121

**匹配主题**: hydrologic model, streamflow, land surface model
{: .label .label-green }

> GRACE已被成功用于监测陆地水储量和地下水储量变化，但在局部尺度上受限于有限的空间分辨率。本研究开发了最优降尺度程序，使用聚类分析和机器学习技术对GRACE Release-06月度mascon数据进行降尺度处理。

---

### Satellite-Derived Global Surface Water Extent and Dynamics Over the Last 25 Years (GIEMS-2)

**作者**: Catherine Prigent, Carlos Jimenez, Philippe Bousquet

**期刊**: *Journal of Geophysical Research: Atmospheres* · **DOI**: [10.1029/2019JD030711](https://doi.org/10.1029/2019JD030711) · **引用次数**: 90

**匹配主题**: surface water
{: .label .label-green }

> GIEMS-2提供了1992年至2015年约25公里分辨率的月度地表水面积估算，包括开阔水域、湿地和季节性淹没区域，构建了25年全球地表水动态记录。

---

### Evaluation of Evapotranspiration for Exorheic Catchments of China during the GRACE Era: From a Water Balance Perspective

**作者**: Yulong Zhong, Min Zhong, Yuna Mao, Bing Ji

**期刊**: *Remote Sensing* · **DOI**: [10.3390/rs12030511](https://doi.org/10.3390/rs12030511) · **引用次数**: 76

**匹配主题**: runoff, streamflow, land surface model
{: .label .label-green }

> 本研究利用水量平衡方程，结合降水、径流和GRACE陆地水储量变化观测，计算了中国九个外流流域的区域蒸散发，比较了考虑和不考虑GRACE水储量变化的蒸散发估算。

---

### Quantifying Long-Term Land Surface and Root Zone Soil Moisture over Tibetan Plateau

**作者**: Ruodan Zhuang, Yijian Zeng, Salvatore Manfreda, Zhongbo Su

**��刊**: *Remote Sensing* · **DOI**: [10.3390/rs12030509](https://doi.org/10.3390/rs12030509) · **引用次数**: 69

**匹配主题**: land surface model
{: .label .label-green }

> 鉴于青藏高原在陆气相互作用和气候系统（如东亚夏季风）中的重要作用，监测其土壤水分动态至关重要。本研究利用长期数据集量化了地表和根区土壤水分，为揭示十年尺度的水分动态提供了重要见解。

---

### Responses of terrestrial water storage to climate variation in the Tibetan Plateau

**作者**: Jiarong Wang, Xi Chen, Qi Hu, Jintao Liu

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124652](https://doi.org/10.1016/j.jhydrol.2020.124652) · **引用次数**: 68

**匹配主题**: runoff, streamflow, surface water
{: .label .label-green }

> 本研究分析了青藏高原陆地水储量对气候变化的响应，探讨了降水、温度与水储量变化在这一关键高海拔区域的关系。

---

### Monitoring Droughts in the Greater Changbai Mountains Using Multiple Remote Sensing-Based Drought Indices

**作者**: Yang Han, Ziying Li, Chang Huang, Yuyu Zhou, Shengwei Zong, Tianyi Hao et al.

**期刊**: *Remote Sensing* · **DOI**: [10.3390/rs12030530](https://doi.org/10.3390/rs12030530) · **��用次数**: 64

**匹配主题**: drought
{: .label .label-green }

> 六种常用干旱指数——降水条件指数、温度条件指数、植被条件指数、植被健康指数、尺度干旱条件指数和温度-植被干旱指数——被用于监测长白山地区的干旱状况，评估了这些指数在不同环境条件下的适用性和一致性。

---

## 气候变化对水资源的影响

气候变化对水资源的影响成为本周的主导主题。一项综合脆弱性评估将五个北非国家的物理气候暴露与水资源影响和社会后果联系起来，巴塔哥尼亚北部面临水资源的严重减少。Mann-Kendall检验——水文气象趋势检测的核心工具——其统计功效得到了严格的重新评估，一种新的动力系统框架揭示了欧洲和北美东部复合湿-风极端事件的特征。未来变暖条件下热带气旋增强被预测将加剧珠江三角洲的风暴潮。

### Climate change vulnerability, water resources and social implications in North Africa

**作者**: Janpeter Schilling, Elke Hertig, Yves Tramblay, Jürgen Scheffran

**期刊**: *Regional Environmental Change* · **DOI**: [10.1007/s10113-020-01597-7](https://doi.org/10.1007/s10113-020-01597-7) · **引用次数**: 402

**匹配主题**: hydrologic model, climate change
{: .label .label-green }

> 北非被认为是气候变化热点地区。本文评估和比较了阿尔及利亚、埃及、利比亚、摩洛哥和突尼斯的气候变化脆弱性，并将其与社会影响联系起来，重点关注气候变化暴露、水资源、敏感性和适应能力。

---

### Re-evaluation of the Power of the Mann-Kendall Test for Detecting Monotonic Trends in Hydrometeorological Time Series

**作者**: F. Wang, Wei Shao, Haijun Yu, Guangyuan Kan, Xiaoyan He, Dawei Zhang et al.

**期刊**: *Frontiers in Earth Science* · **DOI**: [10.3389/feart.2020.00014](https://doi.org/10.3389/feart.2020.00014) · **引用次数**: 398

**匹配主题**: hydropower
{: .label .label-green }

> Mann-Kendall统计检验被广泛应用于水文气象趋势检测。以往研究主要关注"第一类错误"，但很少研究MK检验成功识别趋势的能力。本研究重新评估了该检验的统计功效（第二类错误），这在检验与水电站设计、洪水风险评估和水质评价联合应用时至关重要。

---

### Impacts of climate change on tropical cyclones and induced storm surges in the Pearl River Delta region using pseudo-global-warming method

**作者**: Jilong Chen, Ziqian Wang, Chi-Yung Tam, Ngar-Cheung Lau, Dick-Shum Dickson Lau, H. Y. Mok

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-020-58824-8](https://doi.org/10.1038/s41598-020-58824-8) · **引用次数**: 123

**匹配主题**: river, land surface model, climate change
{: .label .label-green }

> 本研究使用伪全球变暖技术研究了气候变暖条件下西北太平洋登陆热带气旋特征的变化。使用WRF模型对三个登陆珠江三角洲的强热带气旋进行历史模拟，然后在近未来（2015-2039）和远未来（2075-2099）变暖情景下重新模拟。

---

### On the relationship of climatic and monsoon teleconnections with monthly precipitation over meteorologically homogenous regions in India

**作者**: Jew Das, Srinidhi Jha, Manish Kumar Goyal

**期刊**: *Atmospheric Research* · **DOI**: [10.1016/j.atmosres.2020.104889](https://doi.org/10.1016/j.atmosres.2020.104889) · **引用次数**: 117

**匹配主题**: hydrology
{: .label .label-green }

> 本研究使用小波分析和全球相干性方法，探讨了气候和季风遥相关与印度气象均质区月降水量之间的关系。

---

### Climate change in northern Patagonia: critical decrease in water resources

**作者**: Natalia Pessacg, Silvia Flaherty, Solman Silvina, Pascual Miguel

**期刊**: *Theoretical and Applied Climatology* · **DOI**: [10.1007/s00704-020-03104-8](https://doi.org/10.1007/s00704-020-03104-8) · **引用次数**: 97

**匹配主题**: hydrologic model, climate change
{: .label .label-green }

> 本研究记录了气候变化驱动的巴塔哥尼亚北部水资源的严重减少，分析了该地区降水和温度模式的观测趋势和预测变化。

---

### Dynamical systems theory sheds new light on compound climate extremes in Europe and Eastern North America

**作者**: Paolo De Luca, Gabriele Messori, Flavio Pons, Davide Faranda

**期刊**: *Quarterly Journal of the Royal Meteorological Society* · **DOI**: [10.1002/qj.3757](https://doi.org/10.1002/qj.3757) · **引��次数**: 91

**匹配主题**: hydrology
{: .label .label-green }

> 本文提出了一种基于动力系统理论的复合极端事件研究新方法。共递归比率通过量化变量的联合递归来阐明变量间的依赖结构。该方法应用于1979-2018年期间的日气候极端事件，重点分析欧洲和北美东部同时发生的湿-风极端事件。

---

## 洪水、干旱与极端事件

本周在干旱、洪水与人类脆弱性的相互关联方面产出了重要成果。一项关键研究量化了亚马逊地区干旱与森林砍伐之间的正反馈——降雨减少促进森林砍伐，而森林砍伐进一步减少水分循环。对孟加拉国贾木纳河堤防与人口密度相互作用的研究揭示了"堤防效应"——防洪设施通过吸引居民定居在洪泛区，反而增加了洪水死亡风险。一种新的"显著性"框架利用社交媒体定义了具有本地意义的沿海洪水阈值，同时在比利牛斯山对洪水预报集合策略进行了评估。

### Feedback between drought and deforestation in the Amazon

**作者**: Arie Staal, Bernardo M. Flores, Ana Paula Aguiar, Joyce Bosmans, Ingo Fetzer, Obbe A. Tuinenburg

**��刊**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ab738e](https://doi.org/10.1088/1748-9326/ab738e) · **引用次数**: 215

**匹配主题**: hydrology, hydrologic model, drought
{: .label .label-green }

> 森林砍伐和干旱是亚马逊雨林面临的最大环境压力，可能破坏森林-气候系统的稳定性。森林砍伐在区域范围内减少降雨，而干旱又被报道会促进森林砍伐。本研究对21世纪初亚马逊地区干旱与森林砍伐之间的相互作用进行了空间量化。

---

### Impacts of drought, food security policy and climate change on performance of irrigation schemes in Sub-saharan Africa: The case of Sudan

**作者**: Shamseddin Musa Ahmed

**期刊**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2020.106064](https://doi.org/10.1016/j.agwat.2020.106064) · **引用次数**: 91

**匹配主���**: water management, drought, climate change, irrigation
{: .label .label-green }

> 本研究以苏丹为案例，考察了干旱、粮食安全政策和气候变化对撒哈拉以南非洲灌溉方案绩效的复合影响。

---

### The interplay between structural flood protection, population density, and flood mortality along the Jamuna River, Bangladesh

**作者**: Md Ruknul Ferdous, Giuliano Di Baldassarre, Luigia Brandimarte, Anna Wesselink

**期刊**: *Regional Environmental Change* · **DOI**: [10.1007/s10113-020-01600-1](https://doi.org/10.1007/s10113-020-01600-1) · **引用��数**: 77

**匹配主题**: hydrology, river, flood
{: .label .label-green }

> 堤防保护洪泛区免受频繁洪水侵袭，但也可能矛盾地导致更严重的洪水损失。堤防建设会吸引更多资产和人口进入洪水易发区域，当堤防最终溃决时反而增加潜在损害。本研究在孟加拉国贾木纳河洪泛区探讨了这些现象。

---

### Using remarkability to define coastal flooding thresholds

**作者**: Frances C. Moore, Nick Obradovich

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-019-13935-3](https://doi.org/10.1038/s41467-019-13935-3) · **引用次数**: 76

**匹配主��**: flood
{: .label .label-green }

> 沿海洪水在许多地区日益频繁。本研究利用社交媒体上与洪水相关的帖子衡量洪水事件的"显著性"，为美国海岸沿线各县估算了具有本地意义的洪水阈���。

---

### Evaluation of two hydrometeorological ensemble strategies for flash-flood forecasting over a catchment of the eastern Pyrenees

**作者**: Hélène Roux, A. Amengual, R. Romero, Ernest Bladé, Marcos Sanz-Ramos

**期刊**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-20-425-2020](https://doi.org/10.5194/nhess-20-425-2020) · **引��次数**: 33

**匹配主题**: runoff, streamflow, flood
{: .label .label-green }

> 本研究评估了确定性和集合气象预报系统生成的山洪预报性能。水文气象建模链包括WRF驱动的降雨径流模型MARINE，分别评估了基于扰动边界条件和中尺度模型物理参数化的两种集合预报系统。

---

## 流域水文、水资源管理与土地利用变化

本周流域尺度水文和水资源管理研究内容广泛。一项全球评估发现约40,000座现有大坝碎片化了约一万种淡水鱼类的栖息地，规划中的未来水坝威胁进一步恶化连通性。在区域尺度上，黄土高原"退耕还林"工程被证明显著改变了区域水量平衡，而美国东南部的研究模拟了土地利用和气候变化对生态流量的影响。长江干流研究量化了三峡大坝对径流特征的影响，黄河三角洲的水文连通性与植物群落结构相关联，津巴布韦布济子流域揭示了土地覆盖变化的水量平衡后果。建模工具方面的进展包括DSSAT-MODFLOW地下水-灌溉交互框架的评估、SWAT对降雨站网的敏感性测试，以及二维陆面流模型的性能比较。

### Impacts of current and future large dams on the geographic range connectivity of freshwater fish worldwide

**作者**: Valerio Barbarossa, Rafael Schmitt, Mark A. J. Huijbregts, Christiane Zarfl, Henry King, Aafke M. Schipper

**期刊**: *Proceedings of the National Academy of Sciences* · **DOI**: [10.1073/pnas.1912776117](https://doi.org/10.1073/pnas.1912776117) · **��用次数**: 459

**匹���主题**: streamflow, water management, flood, hydropower
{: .label .label-green }

> 水坝有助于水安全、能源供应和防洪，但也碎片化了淡水物种的栖息地。本研究评估了全球约40,000座现有大坝和约3,700座规划中的未来大型水电站对约一万种河流鱼类分布范围连通性的影响。

---

### Impact of revegetation of the Loess Plateau of China on the regional growing season water balance

**作者**: Jun Ge, A. J. Pitman, Weidong Guo, Beilei Zan, Congbin Fu

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-515-2020](https://doi.org/10.5194/hess-24-515-2020) · **引用次数**: 159

**��配主题**: hydrology, runoff, streamflow, land surface model
{: .label .label-green }

> 在"退耕还林"工程实施后，黄土高原呈现显著绿化趋势，减少了土壤侵蚀。然而，该工程也影响了黄土高原的水文过程，引发了关于该工程是否应继续、修改或推广到中国其他地区的讨论。

---

### Impact of land use and urbanization on river water quality and ecology in a dam dominated basin

**作者**: Zengliang Luo, Quanxi Shao, Qiting Zuo, Yaokui Cui

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124655](https://doi.org/10.1016/j.jhydrol.2020.124655) �� **引用次数**: 146

**���配主题**: river, streamflow, water management
{: .label .label-green }

> 本研究探讨了土地利用和城市化对水坝主导流域中河流水质和生态的影响，考察了人为变化如何改变大型水利基础设施下游的水生生态系统。

---

### Potential impacts of land use/cover and climate changes on ecologically relevant flows

**作者**: Furkan Dosdogru, Latif Kalin, Ruoyu Wang, Haw Yen

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124654](https://doi.org/10.1016/j.jhydrol.2020.124654) · **引用次数**: 112

**匹配���题**: streamflow, climate change
{: .label .label-green }

> 本研究评估了土地利用/覆盖和气候变化对生态相关流量的潜在影响，考察了人为和气候驱动因素的综合作用如何改变对水生生态系统健康至关重要的流量体制。

---

### The impact of land-use/land cover changes on water balance of the heterogeneous Buzi sub-catchment, Zimbabwe

**作者**: Abel Chemura, Donald Tendayi Rwasoka, Onisimo Mutanga, Timothy Dube, Terence Darlington Mushore

**期刊**: *Remote Sensing Applications: Society and Environment* · **DOI**: [10.1016/j.rsase.2020.100292](https://doi.org/10.1016/j.rsase.2020.100292) · **引用次数**: 87

**匹配主题**: hydrology
{: .label .label-green }

> 本研究评估了津巴布韦布济子流域源区2009年至2017年间水通量的时空动态及其与土地覆盖变化的关系，揭示了自然和人为干扰环境中土地覆盖动态的水文后果。

---

### Riparian land cover and hydrology influence stream dissolved organic matter composition in an agricultural watershed

**作者**: O. Pisani, D. Bosch, A. Coffin, D. Endale, Dan Liebert, T. Strickland

**期刊**: *Science of the Total Environment* · **DOI**: [10.1016/j.scitotenv.2020.137165](https://doi.org/10.1016/j.scitotenv.2020.137165) · **引用���数**: 79

**匹配���题**: hydrology, streamflow
{: .label .label-green }

> 溶解有机质是碳循环的重要组成部分，控制着水系统中的生物地球化学和生态过程。虽然农业土地覆盖对DOM质量的影响已有报道，但河岸带土地覆盖对河流DOM组成的影响却鲜少关注。本研究探讨了河岸带植被和水文条件如何共同控制DOM特征。

---

### Seasonal stratification of a deep, high-altitude, dimictic lake: Nam Co, Tibetan Plateau

**作者**: Junbo Wang, Lei Huang, Jianting Ju, Gerhard Daut, Qingfeng Ma, Liping Zhu et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124668](https://doi.org/10.1016/j.jhydrol.2020.124668) · **引用次数**: 69

**匹配��题**: seasonal
{: .label .label-green }

> 本研究记录了青藏高原深水高海拔双混合湖泊纳木错的季节性热分层，为世界上最高大型湖泊之一的混合动力学和热结构提供了观测数据��

---

### Performance assessment of 2D Zero-Inertia and Shallow Water models for simulating rainfall-runoff processes

**作者**: Daniel Caviedes-Voullième, J. Fernández-Pato, Christoph Hinz

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124663](https://doi.org/10.1016/j.jhydrol.2020.124663) · **引用次数**: 62

**匹配主题**: runoff
{: .label .label-green }

> 本研究评估了二维零惯性模型和浅水模型在模拟降雨径流过程中的性能，比较了它们在陆面流模拟中的计算效率和精度。

---

### Effect of rainfall station density, distribution and missing values on SWAT outputs in tropical region

**作者**: Mou Leong Tan, Xiaoying Yang

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124660](https://doi.org/10.1016/j.jhydrol.2020.124660) · **引用���数**: 61

**匹配主题**: streamflow
{: .label .label-green }

> 本研究考察了热带地区降雨站密度、空间分布和缺测值对SWAT模型输出的影响，为数据稀缺区域的水文建模输入数据需求提供了指导。

---

### DSSAT-MODFLOW: A new modeling framework for exploring groundwater conservation strategies in irrigated areas

**作者**: Zaichen Xiang, Ryan T. Bailey, Soheil Nozari, Zainab Husain, Isaya Kisekka, Vaishali Sharda et al.

**期刊**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2020.106033](https://doi.org/10.1016/j.agwat.2020.106033) · **引用次数**: 52

**匹配主题**: irrigation
{: .label .label-green }

> 本研究提出了DSSAT-MODFLOW新建模框架，将作物模型DSSAT与地下水模型MODFLOW耦合，用于探索灌溉区地下水保护策略。

---

### Dynamic within-season irrigation scheduling for maize production in Northwest China

**作者**: Shang Chen, Tengcong Jiang, Haijiao Ma, Chuan He, Fang Xu, Robert W. Malone et al.

**期刊**: *Agricultural and Forest Meteorology* · **DOI**: [10.1016/j.agrformet.2020.107928](https://doi.org/10.1016/j.agrformet.2020.107928) · **引用次数**: 53

**匹配主题**: water management, irrigation
{: .label .label-green }

> 本研究基于气象数据融合和DSSAT产量预测，为中国西北地区玉米生产开发了动态季内灌溉调度方法。

---

### Assessing the impacts of different land uses and soil and water conservation interventions on runoff and sediment yield at different scales in the central highlands of Ethiopia

**作者**: Tesfaye Yaekob, Lulseged Tamene, Solomon Gebreyohannis Gebrehiwot, Solomon S. Demissie, Zenebe Adimassu, Kifle Woldearegay et al.

**期刊**: *Renewable Agriculture and Food Systems* · **DOI**: [10.1017/s1742170520000010](https://doi.org/10.1017/s1742170520000010) · **引用次数**: 51

**匹配主题**: hydrology, runoff, hydropower
{: .label .label-green }

> 为应对土壤侵蚀和水分胁迫问题，埃塞俄比亚政府推行了水土保持群众运动。本研究量化了不同尺度下各种干预措施的影响，发现虽然干预措施被认为减少了侵蚀并增强了水资源，但多尺度定量影响评估仍然稀缺。

---

### Hydrological connectivity: One of the driving factors of plant communities in the Yellow River Delta

**作者**: Jiakai Liu, Bernard A. Engel, Guifang Zhang, Yu Wang, Yanan Wu, Mingxiang Zhang et al.

**期刊**: *Ecological Indicators* · **DOI**: [10.1016/j.ecolind.2020.106150](https://doi.org/10.1016/j.ecolind.2020.106150) · **引用次数**: 51

**匹配主题**: hydrology, river
{: .label .label-green }

> 本研究基于土壤含水量和地形的改进综合水文连通性结构指数，揭示了黄河三角洲沿海湿地中水文、土壤因子和植被的耦合机制。

---

### Characteristics of streamflow in the main stream of Changjiang River and the impact of the Three Gorges Dam

**作者**: Hong Wang, Fubao Sun, Wenbin Liu

**期刊**: *CATENA* · **DOI**: [10.1016/j.catena.2020.104498](https://doi.org/10.1016/j.catena.2020.104498) · **引用���数**: 46

**匹配主题**: river, runoff, streamflow
{: .label .label-green }

> 本研究表征了长江干流径流特征，并量化了三峡大坝对流量体制的影响。

---

### Hydrological signatures describing the translation of climate seasonality into streamflow seasonality

**作者**: Sebastian Gnann, Nicholas Howden, Ross Woods

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-561-2020](https://doi.org/10.5194/hess-24-561-2020) · **引用次数**: 40

**匹配���题**: hydrologic model, streamflow, seasonal, hydropower
{: .label .label-green }

> 季节性在自然界中无处不在，与水质、生态、水文极值和水资源管理密切相关。本研究开发了描述气候季节性如何转化为径流季节性的水文特征值，为分析不同水文气候条件下的流域行为提供了新工具。

---

## 统计信息

| 指标 | 数量 |
|:-------|------:|
| 检索数据库 | 2 |
| 检索主题 | 16 |
| 获取论文总数 | 831 |
| 去重后 | 657 |
| 黑名单过滤后 | 596 |
| LLM相关性筛选后 | 43 |
| 排除（不相关） | 553 |

### 按期刊分布

| 期刊 | 论文数 |
|:--------|-------:|
| Journal of Hydrology | 8 |
| Remote Sensing | 5 |
| Hydrology and Earth System Sciences | 4 |
| Journal of Advances in Modeling Earth Systems | 2 |
| Regional Environmental Change | 3 |
| Agricultural Water Management | 3 |
| Nature Communications | 2 |
| Scientific Reports | 1 |
| Geoscientific Model Development | 2 |
| Advances in Water Resources | 1 |
| Journal of Geophysical Research: Atmospheres | 1 |
| Environmental Research Letters | 1 |
| Proceedings of the National Academy of Sciences | 1 |
| Global Change Biology | 1 |
| The Cryosphere | 1 |
| Stochastic Environmental Research and Risk Assessment | 1 |
| Atmospheric Research | 1 |
| Atmospheric Science Letters | 1 |
| Quarterly Journal of the Royal Meteorological Society | 1 |
| Frontiers in Earth Science | 1 |
| CATENA | 1 |
| Natural Hazards and Earth System Sciences | 1 |
| Theoretical and Applied Climatology | 1 |
| ISPRS International Journal of Geo-Information | 1 |
| Agricultural and Forest Meteorology | 1 |
| Science of the Total Environment | 1 |
| Remote Sensing Applications: Society and Environment | 1 |
| Ecological Indicators | 2 |
| Renewable Agriculture and Food Systems | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

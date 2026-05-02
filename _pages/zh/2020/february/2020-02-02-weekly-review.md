---
layout: default
title: "第05周（1月27日 - 2月2日），36篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2020/february/2020-02-02-weekly-review
date: 2020-02-02
categories: [weekly-zh, 2020, february]
tags: [hydrology, literature-review, research]
paper_count: 36
highlight: "CESM2配套SPEAR系统首发，同时发表关于地球系统模型中土壤结构缺失和中国污染驱动水资源短缺的里程碑研究，多篇论文推进了从千年干旱到飓风哈维的水文模型评估。"
---

# 每周文献综述
{: .no_toc }

**第05周** · 2020年1月27日–2月2日
{: .text-grey-dk-000 }

**36** 篇相关论文，涵盖 **6** 个主题
{: .fs-5 .fw-300 }

## 摘要

地球系统建模方面，GFDL发布了SPEAR预测系统，Nature Communications的一项研究揭示地球系统模型中遗漏土壤结构会使径流和排水偏差高达50%。研究表明，当纳入污染约束时，中国的水资源短缺程度加倍，高山亚洲获得了首次高分辨率系统性冰川物质平衡评估。机器学习持续向水文学渗透，CNN-LSTM水质模型（539次引用）和VMD-SVM径流预测器表现突出，多项研究在干旱、气候变化和极端降水条件下对水文模型进行了压力测试。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 地球系统建模与季节至十年预测

本周在地球系统预测基础设施方面取得了重大进展。GFDL发布了SPEAR——一个耦合AM4、MOM6、LM4和SIS2的无缝预测系统，可跨越季节至多年代时间尺度。Merryfield等人的综合评述梳理了亚季节至十年（S2D）预测的最新进展，确定了陆面初始化和海气耦合为关键前沿。Fatichi等人证明了地球系统模型中系统性遗漏土壤结构会在模拟入渗和径流中引入大的偏差，而Goodwell等人探索了信息论方法在诊断水文和地球系统组分间因果相互作用方面的应用。

### SPEAR: The Next Generation GFDL Modeling System for Seasonal to Multidecadal Prediction and Projection

**作者**: Thomas L. Delworth, William Cooke, Alistair Adcroft, Mitchell Bushuk, Jan‐Huey Chen, K. A. Dunne et al.

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2019ms001895](https://doi.org/10.1029/2019ms001895) · **引用**: 288

**匹配主题**: seasonal, land surface model
{: .label .label-green }

> 本文记录了地球物理流体动力学实验室（GFDL）下一代季节至十年预测和投影建模系统的开发和模拟特征。SPEAR（无缝预测和地球系统研究系统）由GFDL近期开发的组件模型构建——AM4大气模型、MOM6海洋代码、LM4陆面模型和SIS2海冰模型。SPEAR模型专门设计了预测模型所需的属性，包括运行大型集合的能力、相对较快的模型吞吐量以及初始化和恢复到观测值的能力。

---

### Current and Emerging Developments in Subseasonal to Decadal Prediction

**作者**: William J. Merryfield, Johanna Baehr, Lauriane Batté, Emily Becker, Amy H. Butler, Caio A. S. Coelho et al.

**期刊**: *Bulletin of the American Meteorological Society* · **DOI**: [10.1175/bams-d-19-0037.1](https://doi.org/10.1175/bams-d-19-0037.1) · **引用**: 305

**匹配主题**: hydrologic model, streamflow, flood, land surface model, earth system model
{: .label .label-green }

> 亚季节至十年时间尺度上的天气和气候变率可能产生巨大的社会、经济和环境影响，使这些时间尺度上的熟练预测成为决策者的宝贵工具。因此，科学界、业务界和应用界对开发预报以改善对极端事件的预知能力越来越感兴趣。

---

### Soil structure is an important omission in Earth System Models

**作者**: Simone Fatichi, Dani Or, R. L. Walko, Harry Vereecken, Michael H. Young, Teamrat A. Ghezzehei et al.

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-020-14411-z](https://doi.org/10.1038/s41467-020-14411-z) · **引用**: 261

**匹配主题**: hydrology, hydrologic model, runoff, land surface model, earth system model
{: .label .label-green }

> 地球系统模型（ESM）中使用的大多数土壤水力信息来自土壤转换函数，该函数使用易于测量的土壤属性来估计水力参数。这种参数化严重依赖于土壤质地，但忽略了由土壤生物物理活动产生的土壤结构的关键作用。本文展示了系统性纳入关键土壤结构特征——大孔隙度和层界面——如何显著改变土壤-植物-大气连续体中通量的分布，包括全球入渗和排水模式。

---

### Debates—Does Information Theory Provide a New Paradigm for Earth Science? Causality, Interaction, and Feedback

**作者**: Allison E. Goodwell, Peishi Jiang, Benjamin L. Ruddell, Praveen Kumar

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2019wr024940](https://doi.org/10.1029/2019wr024940) · **引用**: 76

**匹配主题**: hydrology, hydrologic model, earth system model
{: .label .label-green }

> 组分间因果相互作用的概念是水文学和地球系统科学的重要组成部分。建模者、决策者、科学家和其他水资源利益相关者都利用某种因果关系概念来理解过程、做出决策并推断系统如何对变化做出反应。

---

## 水文模型开发与评估

本周在水文建模的极限和前沿方面贡献丰富。Fowler等人证明了五种常用的桶模型无法复制澳大利亚千年干旱期间自然系统表现出的多年地下水趋势，引发了对气候变化预测的关注。Marsh等人发布了加拿大水文模型（CHM）作为寒区水文学的开源可变复杂度平台，而Meili等人引入了UT&C——一个将植物生理学与城市能量平衡耦合的城市生态水文模型。Viterbo等人评估了NOAA国家水模型对2018年Ellicott City事件的暴洪预报，Baek等人将SWMM与HYDRUS耦合模拟绿色屋顶性能。

### An urban ecohydrological model to quantify the effect of vegetation on urban climate and hydrology (UT&C v1.0)

**作者**: Naika Meili, Gabriele Manoli, Paolo Burlando, Elie Bou‐Zeid, Winston Chow, Andrew Coutts et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-13-335-2020](https://doi.org/10.5194/gmd-13-335-2020) · **引用**: 178

**匹配主题**: hydrology, hydrologic model, runoff, land surface model
{: .label .label-green }

> 城市化加剧可能会强化城市热岛效应、降低室外热舒适度并增强城市径流产生。城市绿地常被提议作为应对这些不利影响的缓解策略，许多城市气候模型的最新发展关注于纳入绿色和蓝色基础设施以指导城市规划。

---

### Many Commonly Used Rainfall‐Runoff Models Lack Long, Slow Dynamics: Implications for Runoff Projections

**作者**: Keirnan Fowler, Wouter Knoben, Murray Peel, Tim Peterson, Dongryeol Ryu, Margarita Saft et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2019wr025286](https://doi.org/10.1029/2019wr025286) · **引用**: 172

**匹配主题**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> 证据表明，流域状态变量（如地下水）可以表现出多年趋势。这意味着它们的状态可能不仅反映近期气候条件，还反映过去数年甚至数十年的气候条件。本文证明了五种常用的概念性"桶"降水-径流模型无法复制自然系统在澳大利亚东南部"千年干旱"期间表现出的多年趋势。

---

### A Multiscale, Hydrometeorological Forecast Evaluation of National Water Model Forecasts of the May 2018 Ellicott City, Maryland, Flood

**作者**: Francesca Viterbo, Kelly Mahoney, Laura Read, F. Salas, Bradford Bates, Jason Elliott et al.

**期刊**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-19-0125.1](https://doi.org/10.1175/jhm-d-19-0125.1) · **引用**: 85

**匹配主题**: hydrology, hydrologic model, streamflow, flood, land surface model
{: .label .label-green }

> NOAA国家水模型（NWM）于2016年8月投入业务运行，首次在美国大陆范围内产生实时、分布式、连续的水文预报。本项目使用综合水文气象评估方法，调查NWM在预测2018年5月27-28日马里兰州Ellicott City极端降雨相关灾难性洪水方面的效用。

---

### The Canadian Hydrological Model (CHM) v1.0: a multi-scale, multi-extent, variable-complexity hydrological model – design and overview

**作者**: Christopher B. Marsh, John W. Pomeroy, H. S. Wheater

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-13-225-2020](https://doi.org/10.5194/gmd-13-225-2020) · **引用**: 83

**匹配主题**: hydrology, hydrologic model, runoff, streamflow, land surface model
{: .label .label-green }

> 尽管降水-径流水文学文献中关于基于物理和空间分布式模型的优点存在争论，但寒区水文学的大量工作表明，通过纳入基于物理的过程表示、相对高分辨率的半分布和全分布离散化以及使用需要有限校准的物理可识别参数，可以改善预测能力。

---

### Assessment of a green roof practice using the coupled SWMM and HYDRUS models

**作者**: Sang‐Soo Baek, Mayzonee Ligaray, Yakov Pachepsky, Jong Ahn Chun, Kwang‐Sik Yoon, Yongeun Park et al.

**期刊**: *Journal of Environmental Management* · **DOI**: [10.1016/j.jenvman.2019.109920](https://doi.org/10.1016/j.jenvman.2019.109920) · **引用**: 74

**匹配主题**: hydrologic model, runoff, water management
{: .label .label-green }

> 绿色屋顶被认为是城市雨水管理的有效低影响开发（LID）实践。本研究耦合了SWMM和HYDRUS模型来模拟绿色屋顶的水文性能，提供了一种基于物理的方法来评估不同降雨情景下的径流减少和水质改善。

---

### Interpolated or satellite-based precipitation? Implications for hydrological modeling in a meso-scale mountainous watershed on the Qinghai-Tibet Plateau

**作者**: Ling Zhang, Dong Ren, Zhuotong Nan, Weizhen Wang, Yi Zhao, Yanbo Zhao et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124629](https://doi.org/10.1016/j.jhydrol.2020.124629) · **引用**: 67

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 本研究比较了站点插值和卫星降水产品及其对青藏高原山区流域水文建模的影响，该地区雨量站网稀疏、地形梯度陡峭。

---

### Is Past Variability a Suitable Proxy for Future Change? A Virtual Catchment Experiment

**作者**: Clare Stephens, Lucy Marshall, Fiona Johnson, Laurence Lin, Lawrence E. Band, Hoori Ajami

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2019wr026275](https://doi.org/10.1029/2019wr026275) · **引用**: 55

**匹配主题**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> 为了估计水文模型在预测未来气候变化下的稳健性，研究人员测试了模型在气候对比观测期之间的可转移性。这种方法只能评估由降水变化和相关环境动态引起的性能变化，因为仪器记录不包含与未来气候变化预测相似的温度或二氧化碳水平。

---

### Sensitivity analysis and uncertainty assessment in water budgets simulated by the variable infiltration capacity model for Canadian subarctic watersheds

**作者**: Rajtantra Lilhare, Scott Pokorny, Stephen J. Déry, Tricia Stadnyk, Kristina Koenig

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.13711](https://doi.org/10.1002/hyp.13711) · **引用**: 52

**匹配主题**: hydrology, hydrologic model, streamflow, land surface model
{: .label .label-green }

> 本研究使用可变入渗容量（VIC）模型评估了不同气候数据集在加拿大北部马尼托巴省10个亚北极流域的季节和年度水文模拟中传播的不确定性，并使用基于响应面变异函数分析（VARS）技术进行了全面的敏感性和不确定性分析。

---

## 气候变化对水资源的影响

研究表明，当纳入水质约束时，中国的淡水短缺程度加倍，华北和华东受影响最严重（Ma等，Nature Communications）。在欧洲阿尔卑斯山，Mastrotheodoros等人发现较暖的夏季将水分平衡转向蒸散发（"绿水"）而非径流和补给（"蓝水"），对下游供水产生影响。大陆尺度研究量化了气候驱动的南美洲水分平衡和上伊洛瓦底江径流变化，区域研究则涉及孟加拉国干旱严重性和中国黑河流域径流预测。Mentaschi等人证明欧洲河流径流的预测变化在很大程度上与达到给定变暖水平的排放路径无关。

### Pollution exacerbates China's water scarcity and its regional inequality

**作者**: Ting Ma, Siao Sun, Guangtao Fu, Jim W. Hall, Yong Ni, Lihuan He et al.

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-020-14532-5](https://doi.org/10.1038/s41467-020-14532-5) · **引用**: 670

**匹配主题**: hydrologic model, water management, land surface model, hydropower
{: .label .label-green }

> 不充分的水质可能意味着水不适合各种人类用途，从而加剧淡水短缺。以往的大规模水资源短缺评估主要关注充足淡水数量的可用性以提供供给，但忽略了水可用性的质量约束。本文报告了中国全国范围内的综合水资源短缺评估，明确纳入了人类用水的质量要求。

---

### More green and less blue water in the Alps during warmer summers

**作者**: Theodoros Mastrotheodoros, Christoforos Pappas, Péter Molnár, Paolo Burlando, Gabriele Manoli, Juraj Párajka et al.

**期刊**: *Nature Climate Change* · **DOI**: [10.1038/s41558-019-0676-5](https://doi.org/10.1038/s41558-019-0676-5) · **引用**: 295

**匹配主题**: runoff, surface water
{: .label .label-green }

> 欧洲阿尔卑斯山较暖的夏季将降水分配从径流和地下水补给（蓝水）转向蒸散发（绿水），对下游水资源和生态系统服务产生重大影响。本研究使用长期观测和基于过程的建模来量化阿尔卑斯流域这一转变的幅度和空间变异性。

---

### Analysis of Streamflow Response to Changing Climate Conditions Using SWAT Model

**作者**: Han Thi Oo, Win Win Zin, Cho Cho Thin Kyi

**期刊**: *Civil Engineering Journal* · **DOI**: [10.28991/cej-2020-03091464](https://doi.org/10.28991/cej-2020-03091464) · **引用**: 124

**匹配主题**: hydrology, hydrologic model, streamflow, flood, hydropower
{: .label .label-green }

> 了解气候变化对河流流域水文条件的安全至关重要，利用水文模型分析不同气候情景对径流的气候变化影响非常重要。本研究的主要目的是使用SWAT模型在低和高代表性浓度路径情景下预测上伊洛瓦底江流域的未来气候对径流的影响。

---

### Climate change impacts on South American water balance from a continental-scale hydrological model driven by CMIP5 projections

**作者**: João Paulo Lyra Fialho Brêda, Rodrigo Cauduro Dias de Paiva, Walter Collischon, Juan Martín Bravo, Vinícius Alencar Siqueira, Elisa Bolzan Steinke

**期刊**: *Climatic Change* · **DOI**: [10.1007/s10584-020-02667-9](https://doi.org/10.1007/s10584-020-02667-9) · **引用**: 121

**匹配主题**: hydrologic model, runoff, water management, climate change
{: .label .label-green }

> 本研究使用CMIP5气候预测驱动的大陆尺度水文模型评估气候变化对南美洲水分平衡的影响，量化了多种排放情景下主要河流流域降水、蒸散发和径流的变化。

---

### Evaluating severity–area–frequency (SAF) of seasonal droughts in Bangladesh under climate change scenarios

**作者**: Mahiuddin Alamgir, Najeebullah Khan, Shamsuddin Shahid, Zaher Mundher Yaseen, Ashraf Dewan, Quazi K. Hassan et al.

**期刊**: *Stochastic Environmental Research and Risk Assessment* · **DOI**: [10.1007/s00477-020-01768-2](https://doi.org/10.1007/s00477-020-01768-2) · **引用**: 90

**匹配主题**: drought, seasonal, climate change
{: .label .label-green }

> 本研究评估了多种气候变化情景下孟加拉国季节性干旱的严重程度-面积-频率特征，提供了与农业水管理和粮食安全规划相关的空间明确干旱风险评估框架。

---

### Impacts of projected climate change on runoff in upper reach of Heihe River basin using climate elasticity method and GCMs

**作者**: Zhanling Li, Qiuju Li, Jie Wang, Yaru Feng, Quanxi Shao

**期刊**: *The Science of The Total Environment* · **DOI**: [10.1016/j.scitotenv.2020.137072](https://doi.org/10.1016/j.scitotenv.2020.137072) · **引用**: 81

**匹配主题**: hydrologic model, river, runoff, climate change
{: .label .label-green }

> 本研究使用气候弹性方法结合GCM预测，量化了中国西北部黑河流域上游预测气候变化对径流的影响，评估了降水和温度变化的相对贡献。

---

### Independence of Future Changes of River Runoff in Europe from the Pathway to Global Warming

**作者**: Lorenzo Mentaschi, Lorenzo Alfieri, Francesco Dottori, Carmelo Cammalleri, Berny Bisselink, Ad de Roo et al.

**期刊**: *Climate* · **DOI**: [10.3390/cli8020022](https://doi.org/10.3390/cli8020022) · **引用**: 31

**匹配主题**: hydrology, river, runoff, streamflow
{: .label .label-green }

> 2015年巴黎协定的成果促使许多气候影响评估关注与达到特定全球变暖水平相对应的未来时间框架。本研究比较了不同温室气体浓度路径下欧洲年均、极端高和极端低河流流量的预测变化，发现水文响应在很大程度上与达到给定变暖水平的排放路径无关。

---

### Integrated Water Management Approach for Adaptation to Climate Change in Highly Water Stressed Basins

**作者**: Elpida Kolokytha, Dimitrios Malamataris

**期刊**: *Water Resources Management* · **DOI**: [10.1007/s11269-020-02492-w](https://doi.org/10.1007/s11269-020-02492-w) · **引用**: 27

**匹配主题**: hydrology, water management, land surface model
{: .label .label-green }

> 本研究提出了一种针对高度缺水流域气候变化适应的综合水管理方法，结合供给侧和需求侧策略来评估其在预测未来条件下的有效性。

---

## 冰川与山地水文

高山亚洲获得了迄今最全面的冰川物质平衡评估：Shean等人从卫星立体影像生成了近6000个高分辨率DEM，揭示了该区域异质性质量损失。在格陵兰冰盖上，Cook等人量化了冰川藻类如何使冰面变暗并加速融化，估计了生物贡献对海平面上升的影响。Rounce等人应用贝叶斯推断使用大地测量物质平衡数据校准了高山亚洲的大尺度冰川演化模型，Baudouin等人交叉验证了印度河流域的降水数据集以减少下游水文建模的主要不确定性来源。

### A Systematic, Regional Assessment of High Mountain Asia Glacier Mass Balance

**作者**: David Shean, Shashank Bhushan, Paul Montesano, David R. Rounce, A. A. Arendt, Batuhan Osmanoğlu

**期刊**: *Frontiers in Earth Science* · **DOI**: [10.3389/feart.2019.00363](https://doi.org/10.3389/feart.2019.00363) · **引用**: 659

**匹配主题**: hydrologic model, runoff, water management
{: .label .label-green }

> 高山亚洲（HMA）是地球极地以外最大的冰川化区域。尽管可用观测有限，长期记录表明自约1850年以来HMA冰川持续质量损失，近几十年损失加速。我们从卫星立体影像生成了5797个高分辨率数字高程模型，以解决空间分辨率粗糙和区域质量损失估计不一致的问题。

---

### Glacier algae accelerate melt rates on the south-western Greenland Ice Sheet

**作者**: Joseph M. Cook, Andrew Tedstone, Christopher J. Williamson, Jenine McCutcheon, Andy Hodson, Archana Dayal et al.

**期刊**: *The Cryosphere* · **DOI**: [10.5194/tc-14-309-2020](https://doi.org/10.5194/tc-14-309-2020) · **引用**: 162

**匹配主题**: hydrology, runoff, land surface model
{: .label .label-green }

> 格陵兰冰盖（GrIS）的融化是真正海平面上升的最大单一贡献者，冰面上色素藻类的生长增加了太阳辐射吸收，放大了融化。这种生物反照率降低效应及其对海平面上升的影响此前未被量化。本文结合野外光谱测量、辐射传输模型、无人机和卫星遥感数据的监督分类以及区域气候模型输出，估计了藻类对GrIS径流的贡献。

---

### Quantifying parameter uncertainty in a large-scale glacier evolution model using Bayesian inference: application to High Mountain Asia

**作者**: David R. Rounce, Tushar Khurana, Margaret Short, Regine Hock, David Shean, Douglas Brinkerhoff

**期刊**: *Journal of Glaciology* · **DOI**: [10.1017/jog.2019.91](https://doi.org/10.1017/jog.2019.91) · **引用**: 82

**匹配主题**: hydrology, hydrologic model, runoff
{: .label .label-green }

> 冰川对气候变化的响应对全球海平面变化和水资源具有重大影响。大尺度冰川演化模型用于预测冰川径流和质量损失，但受到有限观测的约束，导致模型过度参数化。近期系统性的大地测量物质平衡观测为改善冰川演化模型的校准提供了机会。

---

### Cross-validating precipitation datasets in the Indus River basin

**作者**: Jean‐Philippe Baudouin, Michael Herzog, Cameron A. Petrie

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-427-2020](https://doi.org/10.5194/hess-24-427-2020) · **引用**: 82

**匹配主题**: hydrology, river, land surface model
{: .label .label-green }

> 印度河流域的降水量仍存在很大不确定性，特别是在更多山区的北部。虽然雨量计测量通常被视为参考，但它们仅提供特定、通常稀疏位置的信息（点观测），并且容易在山区低估。卫星观测和再分析数据可以改善我们的认知，但验证其结果往往困难。

---

## 机器学习与数据驱动水文预测

机器学习在水文预测领域取得了显著进展。Barzegar等人使用混合CNN-LSTM架构在短期水质预测方面取得了高精度，已获得539次引用。Feng等人将变分模态分解与量子行为粒子群优化的SVM结合用于月径流预测。在业务方面，Quedi和Fan评估了大尺度流域的亚季节径流预报技巧，Totaro等人研究了水文时间序列分析中常用趋势检测方法的统计功效。

### Short-term water quality variable prediction using a hybrid CNN–LSTM deep learning model

**作者**: Rahim Barzegar, Mohammad Taghi Aalami, Jan Adamowski

**期刊**: *Stochastic Environmental Research and Risk Assessment* · **DOI**: [10.1007/s00477-020-01776-2](https://doi.org/10.1007/s00477-020-01776-2) · **引用**: 539

**匹配主题**: water management
{: .label .label-green }

> 本研究提出了一种混合CNN-LSTM深度学习模型用于短期水质变量预测，证明卷积层有效地从多变量输入数据中提取空间特征，而LSTM层捕获时间依赖性，优于独立的CNN、LSTM和传统机器学习方法。

---

### Monthly runoff time series prediction by variational mode decomposition and support vector machine based on quantum-behaved particle swarm optimization

**作者**: Zhong-kai Feng, Wenjing Niu, Zhengyang Tang, Zhiqiang Jiang, Xu Yang, Yi Liu et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124627](https://doi.org/10.1016/j.jhydrol.2020.124627) · **引用**: 242

**匹配主题**: runoff, streamflow, water management, hydropower
{: .label .label-green }

> 本研究提出了一种结合变分模态分解（VMD）和量子行为粒子群优化（QPSO）支持向量机（SVM）的混合模型用于月径流时间序列预测。VMD-QPSO-SVM框架将非线性和非平稳径流信号分解为固有模态函数，实现了与水库运行和水电调度相关的更准确预测。

---

### Satellite-Based Evapotranspiration in Hydrological Model Calibration

**作者**: Lulu Jiang, Huan Wu, Jing Tao, John S. Kimball, Lorenzo Alfieri, Xiuwan Chen

**期刊**: *Remote Sensing* · **DOI**: [10.3390/rs12030428](https://doi.org/10.3390/rs12030428) · **引用**: 59

**匹配主题**: hydrology, hydrologic model, streamflow, land surface model
{: .label .label-green }

> 水文模型通常根据观测径流进行校准，这不适用于无监测河流流域。本文研究了遥感蒸散发在广泛使用的陆面模型水文校准中的应用，该模型耦合了源汇汇流方案和全局优化算法，覆盖28个具有不同气候和自然地理条件的自然河流流域。

---

### Sub seasonal streamflow forecast assessment at large-scale basins

**作者**: Erik Quedi, Fernando Mainardi Fan

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2020.124635](https://doi.org/10.1016/j.jhydrol.2020.124635) · **引用**: 48

**匹配主题**: hydrologic model, streamflow, seasonal, hydropower
{: .label .label-green }

> 本研究评估了大尺度流域的亚季节径流预报技巧，评估了延伸期水文预测在水电运行和水资源管理中跨多个预报提前期和流域特征的潜力。

---

### Numerical investigation on the power of parametric and nonparametric tests for trend detection in annual maximum series

**作者**: Vincenzo Totaro, Andrea Gioia, Vito Iacobellis

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-24-473-2020](https://doi.org/10.5194/hess-24-473-2020) · **引用**: 29

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 近年来，拟合具有趋势或变化点特征的时间序列需要，激发了对非平稳概率分布研究的兴趣。本研究对水文学中年最大值序列常用的参数和非参数趋势检测方法的统计功效进行了数值研究。

---

## 洪水、干旱与水资源管理

通过基于自然的解决方案进行城市洪水管理引起了极大关注，Hobbie和Grimm综述了绿色基础设施如何缓解不透水面和气候变暖的综合影响。Hellwig等人首次在欧洲范围内大规模评估了地下水对干旱的延迟响应，发现干旱传播时间尺度从数月到数年不等。Chen等人测试了遥感降水产品应对飓风哈维极端降雨和洪水级联的能力，而Tunas等人记录了地震引发的滑坡如何加剧了苏拉威西的暴洪。Tranmer等人从耦合水库-河流系统中总结了生态系统管理经验，Ramaswamy和Saleh开发了基于集合的水库泄洪优化用于洪水控制。

### Nature-based approaches to managing climate change impacts in cities

**作者**: Sarah E. Hobbie, Nancy B. Grimm

**期刊**: *Philosophical Transactions of the Royal Society B Biological Sciences* · **DOI**: [10.1098/rstb.2019.0124](https://doi.org/10.1098/rstb.2019.0124) · **引用**: 293

**匹配主题**: runoff, flood, climate change
{: .label .label-green }

> 随着城市人口增长，管理和适应城市地区气候变化将变得越来越重要，尤其是因为城市的独特特征放大了气候变化影响。高不透水覆盖通过城市热岛效应加剧气候变暖的影响，并通过放大径流和洪水加剧暴雨的影响。

---

### Large‐Scale Assessment of Delayed Groundwater Responses to Drought

**作者**: Jost Hellwig, Inge de Graaf, Markus Weiler, Kerstin Stahl

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2019wr025441](https://doi.org/10.1029/2019wr025441) · **引用**: 135

**匹配主题**: hydrology, hydrologic model, streamflow, drought
{: .label .label-green }

> 地下水是长期干旱期间淡水供应的重要资源，也是控制干旱通过水文循环传播的关键储存。当前的干旱监测缺乏地下水干旱的大尺度估计，但近年来国家到全球尺度模型的进展表明，它们现在可以成为研究和监测长期干旱期间水资源可用性的有价值工具。

---

### Can Remote Sensing Technologies Capture the Extreme Precipitation Event and Its Cascading Hydrological Response? A Case Study of Hurricane Harvey Using EF5 Modeling Framework

**作者**: Mengye Chen, Soumaya Nabih, Noah S. Brauer, Shang Gao, Jonathan J. Gourley, Zhen Hong et al.

**期刊**: *Remote Sensing* · **DOI**: [10.3390/rs12030445](https://doi.org/10.3390/rs12030445) · **引用**: 39

**匹配主题**: hydrology, hydrologic model, streamflow, flood
{: .label .label-green }

> 新一代降水测量产品已经出现，如国家强风暴实验室的多雷达多传感器系统（MRMS）和NASA的全球降水测量任务（GPM）。本研究统计评估了MRMS和GPM产品，并研究了2017年8月飓风哈维期间它们的级联水文响应。

---

### Impact of Landslides Induced by the 2018 Palu Earthquake on Flash Flood in Bangga River Basin, Sulawesi, Indonesia

**作者**: I Gede Tunas, Arody Tanga, Siti Oktavia

**期刊**: *Journal of Ecological Engineering* · **DOI**: [10.12911/22998993/116325](https://doi.org/10.12911/22998993/116325) · **引用**: 36

**匹配主题**: hydrology, hydrologic model, river, flood
{: .label .label-green }

> 2018年帕卢地震后，中苏拉威西省一些地区多次发生高强度暴洪，其中之一在印度尼西亚锡吉县的邦加河。洪水造成了巨大影响，如破坏农业和种植园区域、淹没公共设施和基础设施甚至造成人员伤亡。洪水携带各种物质，特别是高浓度沉积物，被认为来源于地震引发的滑坡导致的土壤侵蚀。

---

### Coupled reservoir-river systems: Lessons from an integrated aquatic ecosystem assessment

**作者**: Andrew W. Tranmer, Dana E. Weigel, Clelia L. Marti, Dmitri Vidergar, Rohan Benjankar, Daniele Tonina et al.

**期刊**: *Journal of Environmental Management* · **DOI**: [10.1016/j.jenvman.2020.110107](https://doi.org/10.1016/j.jenvman.2020.110107) · **引用**: 36

**匹配主题**: hydrologic model, river, reservoir, water management, hydropower
{: .label .label-green }

> 本研究提供了耦合水库-河流系统的综合水生生态系统评估，从多学科监测和建模中总结经验教训，以改善平衡水电运行与生态流量需求和下游栖息地质量的管理策略。

---

### Ensemble Based Forecasting and Optimization Framework to Optimize Releases from Water Supply Reservoirs for Flood Control

**作者**: V. Ramaswamy, Firas Saleh

**期刊**: *Water Resources Management* · **DOI**: [10.1007/s11269-019-02481-8](https://doi.org/10.1007/s11269-019-02481-8) · **引用**: 28

**匹配主题**: hydrologic model, streamflow, reservoir, water management, flood
{: .label .label-green }

> 本研究开发了一个基于集合的预报和优化框架，用于优化供水水库的泄洪以控制洪水，将水文集合预报与水库运行优化耦合，以平衡洪水风险降低与供水目标。

---

### Water balance modeling of Tandula (India) reservoir catchment using SWAT

**作者**: R. K. Jaiswal, Ram Narayan Yadav, A. K. Lohani, H. L. Tiwari, Shalini Yadav

**期刊**: *Arabian Journal of Geosciences* · **DOI**: [10.1007/s12517-020-5092-7](https://doi.org/10.1007/s12517-020-5092-7) · **引用**: 24

**匹配主题**: hydrologic model, runoff, reservoir
{: .label .label-green }

> 本研究应用土壤和水评估工具（SWAT）对印度坦杜拉水库流域进行水分平衡建模，评估模型模拟径流、蒸散发和地下水补给组分的能力，以改善水库入流预测和水资源规划。

---

## 统计

| 指标 | 数量 |
|:-------|------:|
| 搜索数据库 | 2 |
| 搜索主题 | 16 |
| 获取论文总数 | 1123 |
| 去重后 | 815 |
| LLM相关性筛选后 | 36 |
| 排除（不相关） | 779 |

### 各期刊论文数

| 期刊 | 论文数 |
|:--------|-------:|
| Water Resources Research | 5 |
| Journal of Hydrology | 4 |
| Nature Communications | 2 |
| Geoscientific Model Development | 2 |
| Hydrology and Earth System Sciences | 2 |
| Remote Sensing | 2 |
| Journal of Environmental Management | 2 |
| Water Resources Management | 2 |
| Stochastic Environmental Research and Risk Assessment | 2 |
| Journal of Advances in Modeling Earth Systems | 2 |
| Nature Climate Change | 1 |
| Bulletin of the American Meteorological Society | 1 |
| Philosophical Transactions of the Royal Society B | 1 |
| The Cryosphere | 1 |
| Journal of Glaciology | 1 |
| Frontiers in Earth Science | 1 |
| The Science of The Total Environment | 1 |
| Climatic Change | 1 |
| Civil Engineering Journal | 1 |
| Journal of Hydrometeorology | 1 |
| Hydrological Processes | 1 |
| Climate | 1 |
| Journal of Ecological Engineering | 1 |
| Arabian Journal of Geosciences | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

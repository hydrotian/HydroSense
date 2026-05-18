---
layout: default
title: "第19周（5月4日 - 5月11日），33篇"
nav_order: 34
nav_exclude: true
lang: zh
lang_link: /2026/may/2026-05-18-weekly-review
date: 2026-05-18
categories: [weekly-zh, 2026, may]
tags: [hydrology, literature-review, research]
paper_count: 33
highlight: "河道变化可使洪水暴露估算翻倍，挑战全球洪水模型中的固定满岸流量假设（Comms Earth & Env）。"
---

# 每周文献综述
{: .no_toc }

**第19周** · 2026年5月4日–5月11日
{: .text-grey-dk-000 }

在 **6** 个主题中发现 **33** 篇相关论文
{: .fs-5 .fw-300 }

## 摘要综述

本周文献聚焦于洪水和干旱建模方式的关键性重新评估。Communications Earth & Environment上的一项研究表明，全球洪水模型中固定满岸容量假设系统性地低估洪水范围达152%，而Nature Communications发表的证据表明西非干旱后径流增加代表的是状态跃迁而非渐进恢复。与此同时，多项研究推进了用于径流和洪水预报的机器学习方法，其中物理增强的LSTM模型在业务化预警系统中表现尤为突出。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 洪水建模与风险评估

本周在洪水建模方面取得了多项重要进展。Hawker等人在密西西比河流域证明，经验推导的满岸流量通常对应不到一年的重现期，导致洪水暴露低估15–472%。Voit等人展示了从水文相似的邻近流域借用暴雨事件可以显著改善小流域洪水频率分析。Wang等人开发了体积守恒降尺度技术，Herpoel等人评估了无监测农业流域的简约分布式框架。

### River channel change can affect flood hazard and impact substantially

**作者**: Laurence Hawker, Stephen E. Darby, Louise Slater, Daniel R. Parsons, Richard J. Boothroyd, Philip J. Ashworth et al.

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03517-9](https://doi.org/10.1038/s43247-026-03517-9) · **引用**: 0

**匹配主题**: river, flood
{: .label .label-green }

> 全球超过10亿人面临洪水风险，预计到2050年这一数字将翻倍。全球洪水模型支撑着风险评估和适应规划，但通常假设河流满岸容量对应固定的两年重现期，忽略了河道特征的时空变异性。本研究使用Fathom全球洪水模型评估了密西西比河流域中经验推导满岸容量对淹没面积和人口暴露的影响。研究发现，当前满岸流量通常对应不到一年的重现期，导致5年、20年和100年洪水事件的洪水范围系统性低估（9–152%）和暴露低估（15–472%）。研究进一步表明，河道形态的历史变化对洪水影响的量级可与多十年尺度的预测气候变化相当。

---

### Considering rainfall events from a neighborhood improves local flood frequency analysis

**作者**: Paul Voit, Felix Fauer, Maik Heistermann

**期刊**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-26-2189-2026](https://doi.org/10.5194/nhess-26-2189-2026) · **引用**: 0

**匹配主题**: hydrologic model, flood
{: .label .label-green }

> 洪水风险管理的许多方面需要洪水频率分析（FFA），但往往受限于较短的观测记录。本研究提出利用邻近水文相似流域的暴雨事件模拟洪峰来扩展基础数据。利用23年雷达降水数据和水文模型，对超过13,000个德国源头流域进行了评估，结果表明局部反事实方法改善了分位数估计，且改善程度随重现期增加而增大。

---

### Probabilistic Flood Maps from Downscaled Compound Flood Ensembles Reveal Distinct Fluvial and Pluvial Impacts in Southeast Texas

**作者**: Mark Wang, Paola Passalacqua, Ethan Coon, Saubhagya S. Rathore, Gabriel Perez

**期刊**: *ESSOAr* · **DOI**: [10.22541/essoar.15002812/v1](https://doi.org/10.22541/essoar.15002812/v1) · **引用**: 0

**匹配主题**: hydrologic model, flood
{: .label .label-green }

> 洪水是最昂贵的自然灾害之一，在德克萨斯州东南部尤为严重。本研究开发了体积守恒降尺度技术，将粗分辨率水文模型输出精细化为米级淹没图。该方法应用于高级陆面模拟器（ATS）的集合模拟，对比FEMA百年一遇洪泛区，概率图在河流走廊显示一致性，同时揭示了内陆洼地的额外积水洪水。河流洪水驱动建筑暴露和深度道路影响；积水洪水造成广泛的浅层道路淹没。

---

### High-resolution mapping of pluvial flooding in ungauged agricultural catchments

**作者**: Matthieu Herpoel, Pierre Baert, Charles Bielders, Gilles Swerts, Aurore Degré

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2511](https://doi.org/10.5194/egusphere-2026-2511) · **引用**: 0

**匹配主题**: hydrology, runoff, flood
{: .label .label-green }

> 无监测农业流域的精确积水洪水制图常受限于缺乏校准数据。本研究评估了一个简约的高分辨率（1 m）分布式框架，基于39个事件进行了验证。研究发现Jain初始损失方法显著降低了体积偏差，但性能严格依赖于降雨强度而非总量，暴露了静态曲线数（CN）参数化在捕捉快速霍顿动力学方面的结构性限制。

---

### Improving Basin‐Wide Flood Estimation From a Global Hydrological Model Through Spatiotemporal‐Pattern‐Based Machine Learning

**作者**: Jiaqing Wang, Quan J. Wang, Jianshi Zhao

**期刊**: *Journal of Flood Risk Management* · **DOI**: [10.1111/jfr3.70224](https://doi.org/10.1111/jfr3.70224) · **引用**: 0

**匹配主题**: hydrologic model, flood
{: .label .label-green }

> 本研究提出了基于时空模式的机器学习方法DSGPR-EOF，结合双阶段稀疏高斯过程回归和经验正交函数分析，改善全流域洪水估计。应用于布拉马普特拉河流域，DSGPR-EOF的洪峰流量估计相对误差最低（3.36%），10年和100年洪峰流量估计误差分别降低68.6%和54.5%。

---

## 干旱研究

本周来自Nature Communications的Peugeot等人的显著发现将西非萨赫勒地区1970年代后径流增加重新定义为替代稳态之间的状态跃迁，由植被-径流反馈环驱动。比利时2011-2020年十年在土壤水分重建评估中被确认为1970年以来最干旱的十年（Lekarkar等）。Liu等人提供了全面分析，表明干旱从气象传播到径流再到农业阶段需数月时间，主要受温度和蒸散驱动。Bai等人记录了植被绿化实际加剧水文干旱的矛盾现象，Cline等人证实径流干旱使鱼类产量减少高达90%。

### Evidence of hydrological regime shifts associated with a major decades-long drought in West Africa

**作者**: Christophe Peugeot, Valentin Wendling, Erwan Le Roux, Gérémy Panthou, Basile Hector, Nathalie Rouché et al.

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-026-72648-6](https://doi.org/10.1038/s41467-026-72648-6) · **引用**: 0

**匹配主题**: runoff, drought, land surface model
{: .label .label-green }

（也发表于2026年5月7日每日采集）

> 利用1950年至2015年的地面气象、水文和土地覆盖数据集，研究提供了证据表明半干旱萨赫勒中部（西非）自1970-1995年干旱以来观察到的径流增加是低径流和高径流替代稳态之间的跃迁。提出了由植被和地表径流之间反馈环驱动的概念模型。干旱可能是跃迁的触发因素，而土地清理和降雨强化可能加强了这一过程。

---

### Reconstructed soil moisture droughts in Belgium reveal 2011–2020 was the driest decade since 1970

**作者**: Katoria Lekarkar, Oldřich Rakovec, Rohini Kumar, Stefaan Dondeyne, Ann van Griensven

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2817-2026](https://doi.org/10.5194/hess-30-2817-2026) · **引用**: 0

**匹配主题**: hydrologic model, drought, land surface model
{: .label .label-green }

> 利用中尺度水文模型（mHM）重建了比利时1970年至2020年的日根区土壤水分动态。分析表明2011-2020年的干旱在过去五十年中持续时间和严重程度均前所未有。该十年中，全国累计经历了三年（非连续）的干旱暴露，占十年的30%。研究还发现，目前业务化使用的SPEI低估了根区干旱的持续性，因为它未明确考虑陆面记忆效应。

---

### Understanding meteorological, runoff, and agricultural drought propagation and their influencing factors in an ensemble of multiple datasets

**作者**: Y.R. Liu, Tingting Hu, Jiawen Yang, Yu Lei

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2775-2026](https://doi.org/10.5194/hess-30-2775-2026) · **引用**: 1

**匹配主题**: runoff, drought, land surface model
{: .label .label-green }

> 利用ERA5再分析数据、GLDAS陆面模型模拟和TerraClimate合并观测数据集评估了1958年至2024年全球陆地的气象、径流和农业干旱传播。结果表明，从气象到径流干旱的平均响应时间为5.0个月，传播率为55.3%；从气象到农业干旱为8.7个月，传播率为30.3%。温度和潜在蒸散是影响气象干旱向径流干旱传播的主要因素，而降水在气象或径流干旱向农业干旱传播中起决定性作用。

---

### Vegetation greening drives hydrological drought: Spatiotemporal heterogeneity in a temperate grassland basin

**作者**: Yanru Bai, Yixin Fang, Fanhao Meng, Min Luo, Hongguang Chen, Chula Sa et al.

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103514](https://doi.org/10.1016/j.ejrh.2026.103514) · **引用**: 0

**匹配主题**: hydrology, drought
{: .label .label-green }

> 对跨中蒙边境的克鲁伦河流域进行研究，开发了综合水文干旱评估指数（CHDAI），综合地表径流、土壤水分、地下水和融雪。结果显示97.15%的区域呈显著干旱趋势。结构方程模型揭示植被通过空间异质性路径影响水文干旱，在中下游这种影响更为显著。

---

### A comparative analysis of hydrological drought in the Rur catchment under human and natural impacts

**作者**: You Wu, Daniel Bachmann, Holger Schüttrumpf

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103457](https://doi.org/10.1016/j.ejrh.2026.103457) · **引用**: 0

**匹配主题**: streamflow, drought, surface water
{: .label .label-green }

> 对鲁尔河流域的地下水和径流干旱进行联合分析。对209口地下水井和16个径流测站计算了标准化指数。区域地下水干旱受人为活动和局部水文地质条件强烈调控。水库运营减轻了部分测站的径流干旱严重程度。

---

### Streamflow drought limits fish production across river ecosystems

**作者**: Timothy J. Cline, Andrew B Lahr, Gregory Peterson, J Martin, David Schmetterling, Donovan Bell et al.

**期刊**: *bioRxiv* · **DOI**: [10.64898/2026.05.05.723077](https://doi.org/10.64898/2026.05.05.723077) · **引用**: 0

**匹配主题**: river, streamflow, water management, drought
{: .label .label-green }

> 研究表明径流下降通过限制幼鱼补充来约束鱼类产量。严重干旱可将产量减少高达90%。在某些系统中，在平均年份维持较高流量比等量的干旱年干预产生更大的生态效益。这些结果表明径流干旱直接限制生物产量，并强调了适应性水管理在维持淡水生态系统中的重要性。

---

## 水文建模与陆面模型

Robertson等人利用前所未有的多模型集合评估了1980年代以来的陆地水储量变化，发现全球TWS下降趋势仍然定量不确定（−0.72至+0.04 mm/yr），并警告ERA5-Land中的人工偏差。Wei等人比较了JRA-3Q和JRA-55作为陆面模型强迫的效果。在喜马拉雅地区，Arora等人整合VIC模型与稳定同位素，发现3000米以上高程干季基流贡献超过97%。Boisramé等人提出应基于局部水文指标而非纯气候标准选择GCM集合。

### Assessing Terrestrial Water Storage Change Since the 1980s

**作者**: Franklin Robertson, Michael Bosilovich, Matthew Rodell, Richard Allan, Bryant Loomis, Hiroko Beaudoing et al.

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-2539](https://doi.org/10.5194/egusphere-2026-2539) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, land surface model
{: .label .label-green }

> 利用比以往更多的模型和观测数据集，结合统计和机器学习技术，推进了对1980年代以来陆地水储量变化的理解。2002-2019年间三个包含人类水管理的全球水文模型识别出TWS下降（-0.91至-0.06 mm/yr），1980-2019年间长期下降趋势与区域降水减少和人类水管理净效应有关。研究发现ERA5-Land中TWS的更强下降与2000-2002年左右ERA5降水的人工下降有关，呼吁谨慎使用再分析数据推断水文气候变量变化。

---

### Comparative analysis of JRA-3Q and JRA-55 reanalysis datasets as forcing for land surface model: implications for hydrological processes

**作者**: Zixin Wei, Fan Bai, Zhongwang Wei, Yongjiu Dai

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135616](https://doi.org/10.1016/j.jhydrol.2026.135616) · **引用**: 0

**匹配主题**: hydrologic model, streamflow, land surface model
{: .label .label-green }

> 摘要暂无。

---

### Precipitation Forecasting for Hydrologic Modeling in West-Central Florida using Seasonal Climate Outlooks

**作者**: Manoj Shrestha, Hui Wang, Jeffrey S. Geurink, Kshitij Parajuli, Tirusew Asefa, Fanzhang Zeng et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-2703-2026](https://doi.org/10.5194/hess-30-2703-2026) · **引用**: 0

**匹配主题**: hydrologic model, streamflow, seasonal
{: .label .label-green }

> 评估了NOAA三个月降水展望在佛罗里达中西部流域尺度的预报技巧。引入了两种非参数集合生成方法：比例三分位抽样（PTS）和主导三分位抽样（DTS）。结果表明预报技巧在干季（10月至2月）达到峰值，特别是在厄尔尼诺年份。建议采用混合策略：在秋冬季使用DTS利用强气候信号，其他季节使用PTS保持可靠性。

---

### Elevation-dependent groundwater control on baseflow in a himalayan catchment: an integrated isotopic–hydrological assessment

**作者**: Siddharth Arora, Prosenjit Ghosh, Anil V. Kulkarni, Mao‐Chang Liang

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-49483-2](https://doi.org/10.1038/s41598-026-49483-2) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 整合VIC水文模型与稳定同位素示踪剂，建立了定量基流贡献的方法。同位素混合模型和VIC输出显示良好一致性，揭示了干季基流贡献随海拔增加而显著增加。1500米以上基流贡献超过70%，3000米以上高达97.0 ± 1.5%，是维持干季水需求的主要水资源。

---

### Think Globally, Model Locally: Complex Responses of Agricultural Water Supplies to Different Climate Projections

**作者**: Gabrielle Boisramé, Beatrice Gordon, Christine M. Albano, Adrian Harpold, Rosemary Carroll

**期刊**: *JAWRA Journal of the American Water Resources Association* · **DOI**: [10.1111/1752-1688.70117](https://doi.org/10.1111/1752-1688.70117) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 在加利福尼亚和内华达州的Walker河流域比较了32个气候预测及其VIC模型输出。预测世纪末降水变化（−20%至+40%）导致更大范围的径流变化（−50%至+75%）。研究表明维持历史水平的供水可靠性到2100年需要年均径流增加超过50%。建议基于局部水文指标而非纯气候指标选择GCM集合。

---

### Detecting Land Use Change Impacts on Streamflow by Combining Field Data and Water Balance Modelling

**作者**: İsmail Bilal Peker, Eren Dağra Sökmen, Ning Liu, Sezar Gülbaz, Ge Sun, Steven G. McNulty et al.

**期刊**: *JAWRA Journal of the American Water Resources Association* · **DOI**: [10.1111/1752-1688.70118](https://doi.org/10.1111/1752-1688.70118) · **引用**: 0

**匹配主题**: hydrology, streamflow, land surface model
{: .label .label-green }

> 分析了土耳其Susurluk流域土地利用变化对水文的影响。两个子流域径流减少32%–42%，主要由土地利用变化而非气候变异驱动。径流系数从1980-1989年的22%降至1990-2005年的12%。

---

### A model of water extraction from the subglacial hydrologic system under idealized conditions

**作者**: C. R. Meyer, Katarzyna Warburton, Aleah N. Sommers, Brent Minchew

**期刊**: *The Cryosphere* · **DOI**: [10.5194/tc-20-2659-2026](https://doi.org/10.5194/tc-20-2659-2026) · **引用**: 0

**匹配主题**: hydrology, hydrologic model
{: .label .label-green }

> 在SHAKTI模型与ISSM冰盖模型耦合下研究冰下水提取。研究发现水压随距离近似对数恢复到背景值。在格陵兰Helheim冰川和南极Thwaites冰川进行瞬态实验，持续抽水模拟速度下降约1%，响应时间为数小时至数天。

---

### Supporting climate change adaptation worldwide: A web application for exploring uncertain future changes in water resources

**作者**: Petra Döll, Guillaume Attard, Fabian Kneier, Laura Müller

**期刊**: *EGUsphere* · **DOI**: [10.5194/egusphere-2026-1829](https://doi.org/10.5194/egusphere-2026-1829) · **引用**: 0

**匹配主题**: hydrologic model, climate change
{: .label .label-green }

> 气候变化影响水资源（CCIWR）探索器是一个免费交互式网络应用，展示全球水文模型多模型集合输出。其独特之处在于能够为考虑利益相关者风险厌恶的气候变化适应决策提供信息，显示预测中认为存在危害性变化的集合成员比例。

---

## 水文领域机器学习与深度学习

本周机器学习/深度学习在径流和洪水预报方面形成了强劲的研究集群。Bezerra等人提出的物理增强LSTM引入站间滞后时间改善极短期洪水预报。Shi等人的VMD-LSTM混合模型在高海拔流域实现88.2%的当日洪峰检测率，远超独立LSTM的2.6%。FloodSimBench数据集为10个美国大都市区提供1米分辨率洪水建模基准。Kasaragod等人展示了利用卫星热数据和机器学习实现近实时多深度土壤水分预测。

### Towards more accurate very short-range flood forecasts with physics-enhanced machine learning models

**作者**: Rodrigo Bezerra, Julian Eleutério, Pedro Solha, Bruno Brentan, Carlos Mello, Manuel Herrera et al.

**期刊**: *Journal of Hydroinformatics* · **DOI**: [10.2166/hydro.2026.180](https://doi.org/10.2166/hydro.2026.180) · **引用**: 0

**匹配主题**: streamflow, flood
{: .label .label-green }

> 提出物理增强的LSTM模型，将站间滞后时间纳入模型的特征选择和时间配置。应用于洪水易发城市流域的高分辨率（10分钟）数据，结果表明物理增强配置通过减少输入冗余持续提高预测精度，同时保持水文过程的物理一致性，支持从黑盒向灰盒建模的转变。

---

### Research on forecasting of diverse flood types based on the deep learning of sub-modal features in high-altitude mountainous basin

**作者**: Xuyang Shi, J S Liu, Haidong Liang, Gonghuan Fang, Tie Liu, Xi Chen

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103496](https://doi.org/10.1016/j.ejrh.2026.103496) · **引用**: 0

**匹配主题**: runoff, flood
{: .label .label-green }

> 结合VMD和LSTM的混合模型用于高海拔山区流域洪水模拟和预报。VMD-LSTM模型将径流信号分解为从低频到高频的多个子模态分量，实现88.2%的当日洪峰检测率，远超独立LSTM模型的2.6%。在1、5、10和15天四个预报时段均表现出低于单一LSTM的累积误差。

---

### FloodSimBench: A Benchmark Dataset for Training Foundational Flood Inundation Models

**作者**: Zhi Li, Songkun Yan, Mofan Zhang, Siyu Zhu, Yixin Wen, Alexander Sun et al.

**期刊**: *ESSOAr* · **DOI**: [10.22541/essoar.15002741/v1](https://doi.org/10.22541/essoar.15002741/v1) · **引用**: 0

**匹配主题**: hydrology, flood
{: .label .label-green }

> FloodSimBench提供了覆盖10个美国主要大都市区的1米分辨率城市洪水建模基准。地球观测基础模型在洪水类别分割方面优于传统CNN，特别是对极端事件。FloodSimBench支持静态洪水严重程度制图和连续动态洪水预报。

---

### Interpretable machine learning framework for urban flood susceptibility assessment: a multi-model comparison with spatial heterogeneity analysis in Yancheng

**作者**: Xuan Zhang, Dongdong Guo

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-47925-5](https://doi.org/10.1038/s41598-026-47925-5) · **引用**: 0

**匹配主题**: hydrology, flood
{: .label .label-green }

> 开发了整合多模型比较、SHAP可解释性分析和空间异质性评估的城市洪水易感性评估框架。XGBoost表现最佳（AUC = 0.938），SHAP分析识别出地形湿度指数、高程和不透水面比率为关键驱动因素。19.2%的研究区域处于高至极高风险水平。

---

### Deep Learning–Based Streamflow Forecasting in a Snowmelt-Dominated Basin: A Regime-Aware Evaluation

**作者**: Roya Vazirian

**期刊**: *Journal of Hydrologic Engineering* · **DOI**: [10.1061/jhyeff.heeng-6651](https://doi.org/10.1061/jhyeff.heeng-6651) · **引用**: 0

**匹配主题**: streamflow, water management
{: .label .label-green }

> 在Henry's Fork流域使用GRU和LSTM进行径流建模和预报。纳入时间滞后SWE显著提高了模型性能。GRU整体优于LSTM（NSE 0.87对0.81），在大多数月份和持续极端及退水期间表现更稳定，而LSTM在早期融化检测方面保持优势。

---

### Advanced Near Real-Time Soil Moisture Mapping using Thermal Remote Sensing and Machine Learning

**作者**: Anush Kasaragod, Jobin Thomas, Thomas Oommen, Ryan Williams, Richard Dobson, Michael Cole et al.

**期刊**: *ESSOAr* · **DOI**: [10.22541/essoar.15002646/v2](https://doi.org/10.22541/essoar.15002646/v2) · **引用**: 0

**匹配主题**: hydrology, land surface model
{: .label .label-green }

> 开发了利用地表温度数据的近实时多深度土壤水分预测方法。XGB模型在5、10和20厘米深度的测试集性能（r: 0.901-0.937; ubRMSE: 0.038-0.047 m³/m³）表明低预测误差。在独立站点的Landsat验证（r: 0.631-0.707）证明了可转移的预测能力。

---

## 水电与水库运营

水电适应气候变化是本周的一个主要主题。两项独立研究从不同角度解决同一问题：Fidan和Bağatur提出Francis-Pelton混合水轮机配置在干旱条件下提高8%的能量产出，而Yildiz等人引入HyTUNE动态决策支持工具指导水轮机更换时机。Poudel和Ramtel预测尼泊尔小水电在SSP585下设计洪水量级增加30-65%。Dorthe等人评估了水电调峰缓解措施，发现仅增加残余流量能有效减少热阈值超标天数。

### Adaptive Hybrid Turbine Switching for Drought-Resilient Hydropower Operation

**作者**: Hüseyin Fidan, Tamer Bağatur

**期刊**: *Turkish Journal of Civil Engineering* · **DOI**: [10.18400/tjce.1806645](https://doi.org/10.18400/tjce.1806645) · **引用**: 0

**匹配主题**: hydrology, streamflow, drought, hydropower
{: .label .label-green }

> 通过基于情景的混合水轮机运行策略评估干旱条件下的水电性能。Francis-Pelton混合配置在五种干旱情景下评估，结果表明混合配置改善了低流量性能，额外年发电量约8%（4.86 GWh），容量因子从49.4%提升至53.3%。

---

### Assessing climate change impacts on design of small hydropower projects in Nepal using a process-based hydrological model with machine learning post-processor

**作者**: Sandeep Poudel, Pradeep Ramtel

**期刊**: *Journal of Water and Climate Change* · **DOI**: [10.2166/wcc.2026.437](https://doi.org/10.2166/wcc.2026.437) · **引用**: 0

**匹配主题**: hydrologic model, streamflow, hydropower
{: .label .label-green }

> 评估了尼泊尔四个流域小水电设计洪水的预计变化。HBV模型结合机器学习后处理器改善了径流模拟。CMIP6气候情景下设计洪水量级显著增加：SSP245下约10-30%，SSP585下30-65%，部分情况超过100%。

---

### Adaptive Turbine Replacement Improves Hydropower Flexibility in a Changing Climate

**作者**: Veysel Yildiz, Nathalie Voisin, Marta Zaniolo

**期刊**: *ESSOAr* · **DOI**: [10.31223/x54b7r](https://doi.org/10.31223/x54b7r) · **引用**: 0

**匹配主题**: hydrology, hydropower
{: .label .label-green }

> 引入HyTUNE（水力涡轮机升级和下一代规划）动态决策支持工具，整合流域水文、电站水力学和自适应优化，指导水轮机更换时机和配置。应用于胡佛水电站表明HyTUNE的自适应策略在多种水文未来中持续优于传统被动策略。

---

### Coordinated control strategy for load variations in hydropower plants cascaded by regulating reservoirs

**作者**: Xiuwei Yang, Jiaping Gu, Jianbin Li, Yiqun Wang, Jijian Lian, Yonghong Zeng

**期刊**: *Energy* · **DOI**: [10.1016/j.energy.2026.141212](https://doi.org/10.1016/j.energy.2026.141212) · **引用**: 0

**匹配主题**: reservoir, hydropower
{: .label .label-green }

> 摘要暂无。

---

### Evaluating options to mitigate hydropower impacts on river thermal regimes in a changing climate

**作者**: David Dorthe, Michael Pfister, Stuart N. Lane

**期刊**: *The Science of The Total Environment* · **DOI**: [10.1016/j.scitotenv.2026.181843](https://doi.org/10.1016/j.scitotenv.2026.181843) · **引用**: 0

**匹配主题**: river, hydropower
{: .label .label-green }

> 评估了阿尔卑斯河流三种水电调峰缓解策略的热效应。当前气候条件下，调节水库和残余流量增加均显著降低短期热变化率（从约7降至4°C/h）。但只有残余流量增加显著减少超过临界热阈值的天数（减少35天）。在未来严重气候情景下，缓解措施减少阈值超标的能力因水库温度升高而下降。

---

## 水资源与气候变化

Nature Sustainability上Zhang等人的论文强调了季节性泥沙输运增强对水基础设施的复合风险。在泛北极鄂毕河流域，Gan等人发现瞬态季节性水体而非单纯冻土融化解释了超过60%的径流生成变异性。阿尔及利亚Oued Sebdou流域的气候变化预测显示SSP5-8.5下径流减少55-61%，深层含水层补给下降65%。

### Water scarcity and infrastructure risk of amplified seasonal sediment transport

**作者**: Ting Zhang, Jim Best, Amy East, Lorenzo Rosa, Qianhan Wu, Yiyi Li et al.

**期刊**: *Nature Sustainability* · **DOI**: [10.1038/s41893-026-01829-4](https://doi.org/10.1038/s41893-026-01829-4) · **引用**: 0

**匹配主题**: runoff, seasonal
{: .label .label-green }

> 摘要暂无。

---

### Transient water bodies drive runoff variability across space and time in the Pan-Arctic Ob River Basin

**作者**: Guojing Gan, Jinglu Wu, Ruibiao Yang, Long Ma, Jilili Abuduwaili, Galymzhan Saparov et al.

**期刊**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae692e](https://doi.org/10.1088/1748-9326/ae692e) · **引用**: 0

**匹配主题**: runoff, land surface model
{: .label .label-green }

> 利用Landsat卫星影像（1989-2017）量化鄂毕河流域水淹没频率。研究发现归一化季节性水面积与13个流域的径流比表现出强统计相关性。利用Budyko框架确定陆面特征变化是年代际径流变化的主要正向驱动因素，短暂水体面积解释了超过60%的参数变异性。季节性水面积的扩展增强了地下补给，在冻土退化条件下放大了径流生成。

---

### ASSESSING CLIMATE CHANGE IMPACTS ON THE HYDROLOGICAL CYCLE IN OUED SEBDOU BASIN, NORTHWEST ALGERIA

**作者**: Hachemaoui Anouar, Salhi Wafaa, M. Abbes, Nabil Beloufa, Abdelillah Otmane cherif, Fethellah Nour el houda et al.

**期刊**: *International Journal of Ecosystems and Ecology Science (IJEES)* · **DOI**: [10.31407/ijees16.241](https://doi.org/10.31407/ijees16.241) · **引用**: 0

**匹配主题**: hydrology, hydrologic model, runoff, streamflow
{: .label .label-green }

> 利用SWAT模型和CMIP6气候预测研究阿尔及利亚Oued Sebdou流域的水文响应。SSP情景下潜在蒸散增加6.0%和13.4%，总径流减少约55%和61%，深层含水层补给减少55.5%和65.0%。SSP5-8.5下出现显著季节性变化，6月径流增加高达205%。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 搜索数据库数 | 2 |
| 搜索主题数 | 16 |
| 获取论文总数 | 1367 |
| 去重后 | 1102 |
| LLM相关性筛选后 | 33 |
| 拒绝（不相关） | 1069 |

### 按期刊分布

| 期刊 | 论文数 |
|:-----|-------:|
| Hydrology and Earth System Sciences | 4 |
| Journal of Hydrology Regional Studies | 3 |
| JAWRA Journal of the American Water Resources Association | 2 |
| Scientific Reports | 2 |
| EGUsphere | 3 |
| ESSOAr | 3 |
| Journal of Hydrology | 1 |
| Nature Communications | 1 |
| Communications Earth & Environment | 1 |
| Nature Sustainability | 1 |
| Environmental Research Letters | 1 |
| The Cryosphere | 1 |
| Journal of Flood Risk Management | 1 |
| Natural Hazards and Earth System Sciences | 1 |
| Journal of Hydroinformatics | 1 |
| Journal of Hydrologic Engineering | 1 |
| Journal of Water and Climate Change | 1 |
| Turkish Journal of Civil Engineering | 1 |
| Energy | 1 |
| The Science of The Total Environment | 1 |
| bioRxiv | 1 |
| IJEES | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

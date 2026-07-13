---
layout: default
title: "第27周（6月29日 - 7月06日），28篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/july/2026-07-13-weekly-review
date: 2026-07-13
categories: [weekly-zh, 2026, july]
tags: [hydrology, literature-review, research]
paper_count: 28
highlight: "AI智能体可从自然语言请求中自动配置水文模型（GRL），CaMa-Flood-GPU实现全球洪水模拟百倍加速。"
---

# 每周文献综述
{: .no_toc }

**第27周** · 2026年6月29日–7月6日
{: .text-grey-dk-000 }

共发现 **28** 篇相关论文，涵盖 **7** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

本周文献反映了水文建模技术栈的广泛进展，从基础AI工具到冰冻圈过程表达。最突出的方法论贡献是一个六级AI智能体自主水文建模框架（GRL），计算层面则有CaMa-Flood-GPU实现全球洪泛模拟的数量级加速。与此同时，多个全球新数据集——GLORIF1（1979–2019年月径流）和时空干旱事件目录（1980–2024年）——正在填补长期数据空白。水库管理和冰冻圈-水文反馈均是活跃前沿，相关论文涵盖基于预报的水库调度、多年冻土融化对径流时序的影响，以及干旱压力下科罗拉多河流域的积雪-土壤水分耦合。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 水文建模中的AI与机器学习

本周有三篇互补的AI/ML论文推动了水文建模向更高自主性和效率的方向发展。Yan等人为水文建模定义了正式的六级AI智能体层次结构，并展示了一种Level-4智能体，可将自然语言指令转化为完整的模型配置——代表着水文模拟民主化的质变。Jin等人从截然不同的角度解决降雨观测问题，利用轻量级ML模型从日常监控和行车记录仪视频中提取雨痕特征，为数据稀缺地区提供机会性传感手段。Hammad等人通过依赖水文状态的残差后处理方法解决"遗留模型"问题，在湿润和干旱条件下均优于统一残差方法。

### AI Agent for Hydrologic Modeling: Definition, Development, and Application

**作者**: Songkun Yan, Mengye Chen, Zhi Li, Yixin Wen, Siyu Zhu, Mofan Zhang et al.

**期刊**: *Geophysical Research Letters* · **DOI**: [10.1029/2025gl119814](https://doi.org/10.1029/2025gl119814) · **引用数**: 1

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

（亦见于2026-07-04日度采集）

> 水文建模支撑洪水预报和水资源管理，但复杂的预处理、参数化和配置限制了其广泛应用。本研究定义了水文建模AI智能体自主性的六级框架，并开发了由大型语言模型驱动的Level-4智能体，可将自然语言请求转化为数据检索、预处理、模型配置和结果分析，无需人工干预。该框架在全球671个流域的概念性水文模型上进行了演示，性能与专家率定相当，所需用户输入极少。

---

### Video‐Based Rainfall Opportunistic Sensing in Hydrology: A Lightweight Machine Learning Approach

**作者**: Yongcheng Jin, Zhe Zhu, Xinwei Xue, Guangtao Fu, Chi Zhang, Yu Li

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041953](https://doi.org/10.1029/2025wr041953) · **引用数**: 0

**匹配主题**: hydrology
{: .label .label-green }

> 基于视频的降雨测量是机会性传感的前沿课题，然而从动态视频中快速、准确、鲁棒地识别雨痕特征仍是关键挑战，尤其对计算资源有限的监测设备而言。为解决测量精度与效率之间的权衡，本研究提出了一种基于ShuffleNetV2主干网络的轻量级机器学习方法，以低计算开销从视频帧中区分降雨事件和强度，可在真实水文监测网络中的边缘设备上部署。

---

### Can State‐Dependant Residual Modeling Improve Legacy Hydrological Model Simulations?

**作者**: Muhammad Hammad, Rajeshwar Mehrotra, Ashish Sharma

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2026wr044285](https://doi.org/10.1029/2026wr044285) · **引用数**: 0

**匹配主题**: hydrologic model
{: .label .label-green }

> 传统残差后处理方法已在模拟水文响应方面取得实质改进，然而这些方法通常将多种不确定性来源汇总为单一残差，并对所有水文条件进行统一统计处理。这种统一处理忽视了误差特征在湿润和干旱条件下存在系统性差异的事实。状态依赖残差建模根据当前土壤湿度和前期条件来调整误差修正，在对比气候区的径流模拟技能方面均取得一致提升。

---

## 全球河流径流建模与陆面模式

本周有五篇论文共同推动了全球尺度水循环模拟的前沿进展。Işık等人发布了GLORIF1——一个通过融合过程基础路由模型与机器学习偏差校正生成的40年全球月径流数据集。Kang等人将CaMa-Flood移植到GPU架构，实现了最高100倍加速，使以往难以实现的集合全球洪水预测成为可能。Yuan等人提出CSSPv3，一个在单一全球框架中明确耦合自然生态水文过程与人类用水活动的陆面模式。Nan等人证明，在寒区山地流域的水文模型中忽略冻土会显著偏估增温背景下的径流敏感性——这对E3SM/ELM在高纬度和高山地区的应用构成直接风险。Wu等人表明，将静态植被和辐射参数替换为动态卫星观测输入，可显著改善中国大陆尺度径流模拟，为其他大域模型的类似升级提供了依据。

### GLORIF1, a global river flow dataset created by integrating process-based modelling and machine learning

**作者**: Sümeyye Büşra Işık, Oriol Pomarol Moya, Michele Magni, Madlene Nussbaum, Derek Karssenberg, Edwin H. Sutanudjaja

**期刊**: *Scientific Data* · **DOI**: [10.1038/s41597-026-07658-6](https://doi.org/10.1038/s41597-026-07658-6) · **引用数**: 0

**匹配主题**: hydrology, hydrologic model, streamflow
{: .label .label-green }

> 准确的径流数据对于全球水资源管理和增强气候韧性至关重要。然而，现有全球径流数据集往往精度不足或依赖稀疏观测。为应对这些挑战，本研究提出GLORIF1（GLObal RIver Flow第1版），一个覆盖1979–2019年的综合月径流数据集。GLORIF1采用混合建模方法，将PCR-GLOBWB过程基础路由与机器学习后处理相结合，显著减少了未量测地区相对于现有产品的偏差。

---

### CaMa-Flood-GPU: a GPU-based hydrodynamic model implementation for scalable global simulations

**作者**: Shengyu Kang, Jiabo Yin, Dai Yamazaki

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-5623-2026](https://doi.org/10.5194/gmd-19-5623-2026) · **引用数**: 0

**匹配主题**: hydrology, flood
{: .label .label-green }

> 洪水是代价最高昂的自然灾害之一，需要可扩展模型在全球尺度模拟河道和洪泛平原动力学过程。基于流域的宏观尺度洪泛平原（CaMa-Flood）模型是实现这一目的的领先系统，但其基于CPU的实现计算量巨大。本文介绍了CaMa-Flood-GPU——采用CUDA进行GPU并行计算的根本性重构版本，相比CPU版本实现50–100倍加速，使在实际时间窗口内的精细分辨率集合全球洪水模拟成为可能。

---

### Development and Evaluation of the Conjunctive Surface‐Subsurface Process Model Version 3 (CSSPv3) at Global Scale

**作者**: Xing Yuan, Chenyuan Li, Peng Ji, Xiazhen Xi, Shuwen Li, Yang Jiao et al.

**期刊**: *Journal of Advances in Modeling Earth Systems* · **DOI**: [10.1029/2025ms005440](https://doi.org/10.1029/2025ms005440) · **引用数**: 0

**匹配主题**: streamflow, land surface model
{: .label .label-green }

> 全球陆地水循环和碳循环在近几十年发生了快速演变，尤其是在人类活动密集干预和脆弱生态水文系统的地区。然而，现有陆面模式（LSMs）和全球水文模型（GHMs）通常将自然生态水文过程与人类用水行为孤立处理，留下了水循环整体表达的关键空白。CSSPv3通过在单一陆面框架内明确耦合自然和人类管理的水通量，填补了这一空白，并通过全球尺度的径流和陆地储水量观测进行了评估。

---

### Omitting Frozen‐Soil Effects in Hydrological Models Introduces Biases in Estimated Runoff Sensitivity to Climate Change in Cold Basins

**作者**: Yi Nan, Fuqiang Tian, Ying Zhao

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041331](https://doi.org/10.1029/2025wr041331) · **引用数**: 0

**匹配主题**: hydrologic model, runoff, streamflow
{: .label .label-green }

> 冰冻圈过程的合理表达对于寒区山地流域精确水文模拟至关重要。冻土作为关键冰冻圈要素，在水文模型中有时被忽略，其水文影响仍未得到充分探索。本研究在青藏高原流域对比了THREW-T模型中包含和不含冻土动力学的两个版本。忽略冻土会对增温背景下径流敏感性的估算产生实质性偏差，偏差的大小和符号随海拔和融化季节性而变化。

---

### Dynamic Satellite-Derived Vegetation and Radiation Inputs Advance Continental-Scale Hydrological Simulation Across China

**作者**: Xinran Wu, Dawei Peng, Xianhong Xie, Y P Wang, Arken Tursun, Yao Liu et al.

**期刊**: *EGUSphere（预印本）* · **DOI**: [10.5194/egusphere-2026-2505](https://doi.org/10.5194/egusphere-2026-2505) · **引用数**: 0

**匹配主题**: hydrologic model, runoff
{: .label .label-green }

> 全球植被变绿正在重塑水循环和能量循环，对陆面水文建模构成挑战。卫星遥感提供了植被和辐射的动态观测，为改进模拟提供了路径。然而，模型通常依赖静态参数，无法捕捉关键的瞬时生物地球物理反馈。本研究在VIC陆面模型中，用动态卫星叶面积指数和短波辐射输入替换静态参数，显著改善了中国大陆尺度径流模拟，湿润南方流域的改善最为明显。

---

## 模型率定、不确定性与观测约束

本周五篇论文推进了参数估计和降水不确定性表达的研究。Xu等人提出了一种序贯蒙特卡洛算法，在高维生态水文模型中实现了比标准MCMC更高效的后验探索。Mangukiya等人对47个概念模型在159个流域进行基准测试，为大样本水文预测中的模型选择提供了严格依据。Wright等人主张将集合降水不确定性量化作为可靠大尺度水文预测的前提条件。Rateb等人揭示了CESM2-LENS2和IPSL-CM6A-LR单模型大集合的结构性缺陷——系统性低估陆地储水量内部变率，损害了归因研究。Zhang等人通过地基被动微波和原位观测，为陆-气反馈在风雨间歇期提供了直接观测约束。

### A Novel Sequential Monte Carlo Algorithm for Parameter Estimation in Eco‐Hydrological Models

**作者**: Cong Xu, Kun Zhang, Gaofeng Zhu, Xin Li, Chuang Wei

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr040933](https://doi.org/10.1029/2025wr040933) · **引用数**: 0

**匹配主题**: hydrologic model, land surface model
{: .label .label-green }

> 贝叶斯推断为生态水文模型的参数估计和不确定性量化提供了灵活框架。然而，对于多模态、高维、计算密集型目标，同时实现稳健的后验探索和高计算效率对广泛使用的MCMC和SMC算法仍是挑战。本研究引入具有自适应退火和并行链管理的改进SMC算法，在多变量生态水文率定中展示了优于标准DREAM和粒子滤波方法的收敛性和效率。

---

### Benchmarking and Selecting Optimal Hydrological Models for Large‐Sample Applications Considering Complexity and Uncertainty

**作者**: Nikunj K. Mangukiya, Gopeshwar Sahu, Sagar Gupta, Ashutosh Sharma

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2026wr044753](https://doi.org/10.1029/2026wr044753) · **引用数**: 0

**匹配主题**: hydrologic model
{: .label .label-green }

> 可靠的大样本水文预测需要系统的基准测试和谨慎的模型选择。然而，由于模型间的结构不确定性、高计算需求以及区域气候和地貌多样性，这一过程颇具挑战。本研究使用MARRMoT工具箱在印度半岛159个流域对47个概念降雨-径流模型进行基准测试，发现在未量测流域中，结构更简单的模型往往能与复杂结构相媲美——模型复杂性权衡随气候干旱程度变化显著。

---

### Ensemble‐Based Uncertainty Quantification Can Improve Large‐Scale Precipitation Data for Hydrologic Prediction

**作者**: Daniel B. Wright, Yagmur Derin, Kaidi Peng, Viviana Maggioni

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70635](https://doi.org/10.1002/hyp.70635) · **引用数**: 0

**匹配主题**: hydrologic model
{: .label .label-green }

> 来自卫星、再分析和"融合"数据集的大尺度降水数据中的大量不确定性阻碍了其在水文应用中的应用。虽然可以通过量化不确定性并将其传播到水文模型来解决这一问题，但关于需要何种形式的不确定性信息尚无共识。本评论将降水不确定性定义为概率集合属性，并论证集合产品——而非单产品不确定性范围——是在各尺度上忠实传播观测不确定性至水文预测的必要条件。

---

### Structural deficits in large ensembles limit detection and attribution of terrestrial water storage

**作者**: Ashraf Rateb, Bridget R. Scanlon, Brett Buzzanga

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03772-w](https://doi.org/10.1038/s43247-026-03772-w) · **引用数**: 0

**匹配主题**: earth system model
{: .label .label-green }

> 判断陆地储水量趋势和极端事件是否反映外部强迫或内部气候变率，需要可信的反事实基准。本研究通过对比GRACE-FO观测，测试CESM2-LENS2和IPSL-CM6A-LR两个广泛使用的单模型大集合档案是否提供了这样的基准，发现两个集合均系统性低估了陆地储水量内部变率的量级，限制了其在人类活动引起陆地储水量变化的正式归因研究中的实用性。

---

### Observed Land Surface Influence on Atmospheric Heat and Moisture Profiles During Interstorms

**作者**: Michelle S. Zhang, David D. Turner, Dara Entekhabi

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr043166](https://doi.org/10.1029/2025wr043166) · **引用数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 陆-气反馈历来通过模型研究，模型结构和参数化影响研究结论。仅基于观测表达陆-气反馈对于理解边界层发展和降水仍是持续挑战。为填补这一空白，本研究利用地基被动遥感和原位观测，表征风雨间歇期地表能量分配如何塑造大气水汽和温度廓线，为数值天气预报和气候模型中的陆面参数化提供观测基准。

---

## 洪水动力学

本周两篇高影响力论文从两端涵盖了洪水主题：Komma等人对2024年9月多瑙河特大洪水进行了详细的水文气象事后分析——这是奥地利下奥地利州器测记录以来最大洪水——并将其置于降水格局变化的背景下。Bai等人在《Earth-Science Reviews》上综述了旱地洪水的新兴科学，认为干旱地区的山洪和间歇性河道洪水在全球模型中代表性不足，并在气候变暖背景下日益频繁。

### The September 2024 Danube flood compared to the 1899, 2002, and 2013 events: a hydrometeorological analysis in a changing climate

**作者**: Jürgen Komma, Peter Valent, Miriam Bertola, Juraj Párajka, Klaus Haslinger, Benedikt Bica et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4075-2026](https://doi.org/10.5194/hess-30-4075-2026) · **引用数**: 1

**匹配主题**: runoff, flood, climate change
{: .label .label-green }

> 2024年9月，奥地利多瑙河流域发生了特大洪水，部分地区出现了器测记录以来最高洪峰流量。本研究分析了2024年事件的气象和水文驱动因素，并与三次历史洪水（1899年、2002年、2013年）进行比较，以厘清前期土壤湿度、降水强度和流域状态在产生极端流量中的相对作用。2024年事件的显著特征是：前期湿润条件导致土壤饱和，叠加持续时间长且区域广泛的降水事件，超越了流域的典型调蓄能力。

---

### Emerging dryland flooding

**作者**: Yu Bai, Te Zhang, Stephen E. Darby, Bruno Merz, Albert J. Kettner, Katerina Michaelides et al.

**期刊**: *Earth-Science Reviews* · **DOI**: [10.1016/j.earscirev.2026.105612](https://doi.org/10.1016/j.earscirev.2026.105612) · **引用数**: 0

**匹配主题**: streamflow, flood
{: .label .label-green }

> 摘要暂不可用。

---

## 干旱与径流恢复

四篇论文共同推进了对干旱驱动水文变化的理解。Avesani等人揭示，在Alpine受调节流域的水文干旱指数中忽略水电基础设施会从根本上歪曲干旱统计特征。Khan等人解决了澳大利亚东南部的水文非平稳性问题，证明许多受1997–2009年千年干旱影响的流域，在降水恢复正常后仍未恢复其旱前降雨-径流关系——这与持续性植被变化和土壤结构改变有关，而非气象异常。Nguyen等人利用模型推导的地下水对地表土壤水分异常响应时间作为山洪干旱发生的新诊断指标。Yu等人仅利用水量平衡约束，开发了一种贝叶斯框架将流域径流分解为地表、基流和地下水三个组分。

### Grasping Hydrological Droughts in Highly Hydropower Regulated Alpine Watersheds

**作者**: Diego Avesani, Carlo De Michele, Anna Paola Lonardi, Andrea Galletti, Bruno Majone

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042323](https://doi.org/10.1029/2025wr042323) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow, drought, hydropower
{: .label .label-green }

> Alpine地区的水文干旱越来越多地受到人类调节影响，水电运行在改变其统计特征方面发挥着核心作用。本研究考察了水电系统在水文模型中的表达如何影响干旱的识别和统计特征。使用HYPERstreamHS水文模型，作者表明忽略运行水库会导致意大利Alpine源头区干旱事件的系统性误识别和持续时间-严重性统计的扭曲。

---

### Why Does Runoff From Some Catchments Not Recover After a Prolonged Drought?

**作者**: Zaved Khan, David Robertson, Francis Chiew, Jorge L. Peña‐Arancibia

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70632](https://doi.org/10.1002/hyp.70632) · **引用数**: 0

**匹配主题**: runoff, streamflow, drought
{: .label .label-green }

> 1997–2009年千年干旱改变了澳大利亚东南部维多利亚州大部分地区的降雨-径流响应。本研究利用水量平衡分析和建模实验，结合1982–2020年120个流域的观测水文气候和遥感数据，调查维多利亚州的水文非平稳性。维多利亚州大多数流域在千年干旱后呈现水文非平稳性，即使降水恢复后，径流相对旱前水平仍然受到抑制——这与持续性植被变化和土壤结构改变有关，而非气象异常。

---

### Dynamics of model-based groundwater-land surface response times as a dryland flash drought diagnostic

**作者**: Hoang Hai Nguyen, Di Long, S.-Y. Simon Wang, Jinho Yoon, Yulong Zhong, Hyunglok Kim

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03783-7](https://doi.org/10.1038/s43247-026-03783-7) · **引用数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 地下水对地表土壤水分异常的延迟响应（T_opt）反映了地表信号传播到含水层的速度，在不同湿润条件下存在差异。理解其时空变率有助于诊断山洪干旱，但目前仍缺乏探索。本研究利用动态指数滤波器检验全球模型推导的T_opt与山洪干旱之间的关系，发现在旱地地区，较短的地下水响应时间与更高的山洪干旱频率和严重性相关，提供了一种新的物理基础预警指标。

---

### Estimating the composition of basin runoff based on water balance analysis and Bayesian uncertainty analysis

**作者**: Xiaohan Yu, Xiankui Zeng, Dongwei GUI, Dong Wang, Jichun Wu

**期刊**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0218.1](https://doi.org/10.1175/jhm-d-25-0218.1) · **引用数**: 0

**匹配主题**: runoff, streamflow
{: .label .label-green }

> 流域径流由三个组分构成：地表径流、基流径流和地下水径流。准确估算径流组分可加深我们对水文过程的理解，增强水量平衡分析的可靠性。然而，在地面观测稀疏的大型流域估算径流组分仍是挑战，尤其在非稳态气候条件下。本研究在水量平衡框架内应用贝叶斯不确定性分析分解径流组分，在中国河流流域进行了验证，并量化了基流分数对土地利用和气候变率的响应。

---

## 冰冻圈与积雪-径流动力学

四篇论文探讨冰冻圈变化如何重塑不同山地系统的径流时序和量级。Li等人重建了青藏高原流域四十年的径流组分演变，发现冰川和多年冻土融化贡献增加引起总径流呈上升趋势，2009年后抵消了降水驱动的径流减少。Ghimire等人证明，在干旱压力下的科罗拉多河流域，秋季土壤湿度——而非积雪量——是春季径流的关键调制因子，对季节性水供应预报具有重要意义。Rezaei等人利用CESM集合评估平流层气溶胶注入（太阳地球工程）相对于增温基准将如何改变积雪-径流动力学，发现水文响应与温度信号存在显著背离。Wan等人在青藏高原采用以空间换时间框架，表明海拔依赖的多年冻土融化延迟了季节径流峰值，并威胁下游水资源可用性。

### Four‐Decade Evolution of Runoff Components and Cryospheric Contributions in an Alpine Inland River Basin, Tibetan Plateau

**作者**: G L Li, Zongxing Li, Baoqing Zhang, Juan Gui

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70630](https://doi.org/10.1002/hyp.70630) · **引用数**: 0

**匹配主题**: runoff, streamflow
{: .label .label-green }

> 本研究利用过程基础THREW-T水文模型，调查了1982–2022年青藏高原布哈河流域（青海湖最大支流）径流组分演变及其驱动因素。研究发现年径流呈波动上升趋势，2009年前后出现从下降到增加的明显转折。模型归因表明，2009年后冰川融化和多年冻土融化贡献增加，抵消了降水驱动径流的减少，冰冻圈融化成为近几十年年际变率的主导驱动因素。

---

### Fall Soil Moisture Modulates Snow‐Streamflow Dynamics in the Colorado River Basin

**作者**: Swastik Ghimire, Enrique R. Vivoni, Zhaocheng Wang

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042871](https://doi.org/10.1029/2025wr042871) · **引用数**: 0

**匹配主题**: streamflow
{: .label .label-green }

> 科罗拉多河流域（CRB）自2000年以来持续干旱，近年来积雪量与径流之间的关系减弱。本研究利用VIC模型数值实验，考察了秋季土壤湿度和春季天气在调制CRB及其子流域积雪-径流动力学中的作用。结果表明，秋季土壤湿度前期条件解释了春季径流方差的相当大一部分，通常超过积雪当量的预报价值——对季节性水供应预报具有重要意义。

---

### Hydrologic Sensitivity of Snow and Streamflow Dynamics to Climate Forcing With and Without Stratospheric Aerosol Intervention

**作者**: Abolfazl Rezaei, John C. Moore, Simone Tilmes, Daniele Visioni

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042658](https://doi.org/10.1029/2025wr042658) · **引用数**: 0

**匹配主题**: streamflow
{: .label .label-green }

> 积雪的积累和融化关键性地调节许多地区的淡水可用性。在全球变暖背景下，积雪变率的主导控制因素从冷季降水转向冷季温度，改变了降雨-降雪分配、融雪时序和径流产生。利用CESM1和CESM2集合，本研究评估了平流层气溶胶注入相对于无减缓增温基准将如何改变这些动力学，发现气溶胶注入虽然部分恢复了积雪，但产生了不能简单逆转增温信号的独特区域水文响应。

---

### Elevation‐Dependent Permafrost Thaw on the Tibetan Plateau Delays Seasonal Discharge and Poses a Risk of Reduction in Downstream Water Availability

**作者**: Chengwei Wan, J. J. Gibson, Peng Yi, Xicai Pan, Chenghao Chen, Grzegorz Skrzypek

**期刊**: *Earth's Future* · **DOI**: [10.1029/2025ef007809](https://doi.org/10.1029/2025ef007809) · **引用数**: 0

**匹配主题**: streamflow
{: .label .label-green }

> 全球变暖和多年冻土融化显著改变了冻土地区的景观和水文条件。虽然针对地点的过程研究已描述了融化过程中的水文变化，但由于景观异质性和复杂相互作用，流域尺度影响评估和径流建模仍面临挑战。本研究在青藏高原海拔梯度上引入以空间换时间框架，利用同位素和水文测量数据推断渐进多年冻土融化如何延迟季节径流峰值并减少晚季水资源可用性——对依赖水资源的下游社区和生态系统具有重要影响。

---

## 水库调度与水资源管理

五篇论文涵盖了水库和灌溉管理挑战的全谱。Albano等人对美国西部多种水库系统进行了首次系统性流域-水库运行灵活性表征，这是实施基于预报的水库调度（FIRO）的前提条件。Upadhyay等人预测，美国西部水库低库容条件在21世纪气候变化下将变得更加频繁，对水电可用性具有关键影响。Zaniolo等人提出了一个新框架，联合优化水库和水利基础设施管理的信息选择（监测什么信号）和策略学习（如何响应）。Abbas等人开发了基于MODFLOW的方法，检测在灌溉流域中被地表流量站网系统性忽略的具有环境意义的地下水驱动径流改变。Rizwan等人将农民灌溉采用决策的经济模型与水文模型（SWAT+）结合，预测气候变化背景下大规模灌溉扩张将如何重塑区域水量平衡。

### Characterizing Watershed Responses and Reservoir Operational Flexibilities: Analyses to Support Forecast‐Informed Reservoir Operations (FIRO) Planning

**作者**: Christine M. Albano, E. J. Shearer, J. C. Forbis, E. M. Yeates, Julie Kalansky, C. A. Painter et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042131](https://doi.org/10.1029/2025wr042131) · **引用数**: 0

**匹配主题**: reservoir
{: .label .label-green }

> 天气预报技能的最新进展为使用基于预报的水库调度（FIRO）等策略更灵活地管理水库提供了机遇。这在气候、人口和土地利用变化使得平衡水库用途以最小化洪水风险和最大化水资源可用性愈发困难之际尤为关键。FIRO的可行性取决于预报入流并将该信息转化为运行决策的能力。本研究表征了美国西部多种水库系统的流域水文响应类型和运行灵活性指标，识别了FIRO策略具有最大潜在收益的地区。

---

### Evaluating Frequency of Low Reservoir Storage in the Western U.S. over the 21st Century

**作者**: Surabhi Upadhyay, Adrienne Marshall, Nathalie Voisin, Daniel Broman

**期刊**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae84ed](https://doi.org/10.1088/1748-9326/ae84ed) · **引用数**: 0

**匹配主题**: reservoir
{: .label .label-green }

> 近年来，美国西部多个水库在干旱条件下接近或超过临界低库容；若此类事件在区域内广泛分布或被气候变化加剧，则对水资源和能源可用性的影响尤为显著。利用多模型水文预测，本研究发现在21世纪中后期增温情景下，临界低库容事件将显著增多，多个流域同时发生的情况对区域水电系统构成不成比例的风险。

---

### Toward Joint Information Selection and Policy Learning in Water Resources Management

**作者**: Marta Zaniolo, Matteo Giuliani, Jonathan D. Herman

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr042745](https://doi.org/10.1029/2025wr042745) · **引用数**: 0

**匹配主题**: streamflow, water management
{: .label .label-green }

> 水资源文献在基础设施管理计算工具方面取得重大进展，开发了越来越复杂的自适应和多目标控制框架，改善了在不确定性和变化下的决策优化。然而，大多数水利基础设施运行策略仍以有限信息集（通常仅限水库蓄量和入流预报）为条件。本研究开发了一个框架，同时学习监测哪些信号和采用何种策略，在多目标水库管理性能方面相较于专家定义信息集取得提升。

---

### Detecting Hidden Environmental Flow Alteration in Groundwater‐Irrigated Basins

**作者**: Salam A. Abbas, Gerardo Castellanos-Osorio, Jeremy T. White, Javier Senent‐Aparicio, Ryan T. Bailey

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70626](https://doi.org/10.1002/hyp.70626) · **引用数**: 0

**匹配主题**: streamflow, irrigation
{: .label .label-green }

> 在地下水灌溉流域有效平衡经济和环境关切是全球性挑战。环境流量修改越来越受地下水支撑灌溉的影响，但由于缺乏直接观测方法，严格量化地下水灌溉对生态地表水流影响的能力仍然有限。利用基于MODFLOW的框架，本研究识别了常规流量站网无法探测的隐性环境流量改变，揭示了密集地下水灌溉流域存在系统性低流量耗竭。

---

### Irrigation Use in a Changing Landscape: A Combined Economic and Hydrologic Approach

**作者**: Noormah Rizwan, Jamshid Jahali, Molly Sears, S. Woznicki, Tao Liu, Oskar Marko et al.

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2025wr041530](https://doi.org/10.1029/2025wr041530) · **引用数**: 0

**匹配主题**: hydrologic model, irrigation
{: .label .label-green }

> 温度升高和不稳定降水格局正在威胁全球水资源可用性。灌溉是关键的风险缓解策略，有助于在气候压力下维持作物产量。由于获取农场尺度经济数据存在挑战，以往较少研究农民在气候变化下灌溉的可能性，或大规模灌溉扩张对未来水资源可用性的影响。本研究将农民采用决策的经济模型与水文模型（SWAT+）结合，预测增温情景下灌溉扩张如何重塑区域水量平衡，发现大规模采用产生反馈循环，降低了每个农场的灌溉收益。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题数 | 15 |
| 获取论文总数 | 1008 |
| 去重后 | 868 |
| LLM相关性筛选后 | 28 |
| 被拒绝（不相关） | 840 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|-------:|
| Water Resources Research | 12 |
| Hydrological Processes | 4 |
| Scientific Data | 1 |
| Geoscientific Model Development | 1 |
| Journal of Advances in Modeling Earth Systems | 1 |
| Geophysical Research Letters | 1 |
| Hydrology and Earth System Sciences | 1 |
| Communications Earth & Environment | 2 |
| Earth's Future | 1 |
| Environmental Research Letters | 1 |
| Earth-Science Reviews | 1 |
| Journal of Hydrometeorology | 1 |
| EGUSphere（预印本） | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, streamflow, flood, drought, reservoir, water management, runoff, land surface model, earth system model, climate change, hydropower, surface water, irrigation

**数据库**: Semantic Scholar, OpenAlex

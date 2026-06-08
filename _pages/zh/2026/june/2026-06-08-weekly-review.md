---
layout: default
title: "第22周（5月25日 - 6月1日），26篇"
nav_order: 34
nav_exclude: true
lang: zh
lang_link: /2026/june/2026-06-08-weekly-review
date: 2026-06-08
categories: [weekly-zh, 2026, june]
tags: [hydrology, literature-review, research]
paper_count: 26
highlight: "人为气候变暖使全球年洪水时间每升温0.5°C提前0.43天，各地区呈分化趋势，导致基础设施与实际洪水发生时间错位加剧；新型机器学习框架致力于解决数据稀缺流域的径流预测难题。"
---

# 每周文献综述
{: .no_toc }

**第22周** · 2026年5月25日–6月1日
{: .text-grey-dk-000 }

在 **4** 个主题中共发现 **26** 篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

一项发表于Nature Communications的重要研究定量分析了人为变暖对全球洪水时间的影响，结果显示洪水时间在积雪融化主导和季风主导的流域中每升温0.5°C平均提前0.43天——这一趋势导致现有按历史洪水时间设计的防洪基础设施日益失效。在模型开发方面，本周涌现了多个新工具，包括非饱和带的双求解器表达方法、积雪截留参数化方案，以及包含冰川演化模块的雪-冰-径流模型，同时还有一项对18000多个流域24套格网降水数据集的全球基准评估。机器学习方法在水文领域的应用持续深入，新型迁移学习、知识蒸馏和模型互操作性框架正针对数据稀缺条件下的预测难题提供系统性解决方案。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 气候变化与洪水动态

本周气候-水文文献传递出一个核心信号：洪水时间、量级及其驱动因素的变化速度已超出现有基础设施和预报系统的适应能力。Qi等人对人为因素导致的洪水时间偏移进行了全球首次定量评估；Makhmudova等人深入分析了哈萨克斯坦极端春季洪水的复合驱动机制；Dykman等人则着力解决反向问题——如何针对历史记录之外的极端洪水进行模型参数校准；Meng等人证明ENSO对区域洪水风险的影响可以在SWAT模型中实现参数化。此外还有两项研究从不同角度完善了这一图景：一项探究干旱-火灾交互如何重塑降雨-径流关系，另一项评估了冰川供水流域在CMIP6变暖情景下的响应。

### Anthropogenic climate change accelerates the onset of global flood timing

**作者**：Wei Qi, Ying Liu, Xin Jiang, Junguo Liu

**期刊**：*Nature Communications* · **DOI**: [10.1038/s41467-026-73839-x](https://doi.org/10.1038/s41467-026-73839-x) · **引用数**：0

**匹配主题**：hydrology, streamflow, flood
{: .label .label-green }

（同见2026-05-29每日采集）

> 洪水是地球上最具破坏性的自然灾害之一，具有广泛的社会和生态级联影响。洪水时间偏移因干扰防洪准备工作而加剧风险，但其全球模式至今尚未充分量化。本研究利用多模型集合，对1.5°C–4.0°C渐进变暖情景下全球洪水时间变化进行了系统评估。结果表明，人为强迫使全球洪水时间平均提前0.43 ± 0.25天/每升温0.5°C，且各地区呈分化趋势：原本偏早的洪水进一步提前，原本偏晚的洪水则进一步推迟。在1.5°C变暖情景下，全球约52%的河流流域洪水时间出现统计显著的提前；在4.0°C情景下，这一比例上升至74%。这些时间偏移超过了按历史洪水时间设计的防洪基础设施的适应能力。

---

### Compound Drivers of Extreme Spring Floods in a Changing Climate: The Esil River Case, Kazakhstan

**作者**：Lyazzat Makhmudova, Sayat Alimkulov, Ainur Mussina, Harris Vangelis, Elmira Talipova, Oirat Alzhanov 等

**期刊**：*Earth Systems and Environment* · **DOI**: [10.1007/s41748-026-01219-y](https://doi.org/10.1007/s41748-026-01219-y) · **引用数**：1

**匹配主题**：hydrology, hydrologic model, river, runoff, water management, flood, climate change
{: .label .label-green }

> 在气候变化、水文变异性增强以及季节性水分积累和径流形成过程改变的共同驱动下，全球极端洪水的频率和强度持续增加。近几十年来，春季洪水时空特征的变化导致设计水位超限频率增加，水利设施、基础设施和农业受损加剧。以融雪为主的河流区域尤为脆弱——冬季水分积累与春季融雪加速之间的失衡造成复合洪水风险。本研究以哈萨克斯坦伊希姆河（Esil River）为研究对象，通过分析气象和水文历史记录，阐明冬季降水增加、气温驱动融雪加速以及土壤含水量前期条件如何共同造成极端春季洪峰。

---

### Robust Calibration of Hydrological Models for Simulating Unseen Flood Extremes

**作者**：Caleb Dykman, Conrad Wasko, Rory Nathan, Ashish Sharma

**期刊**：*Water Resources Research* · **DOI**: [10.1029/2025wr040134](https://doi.org/10.1029/2025wr040134) · **引用数**：0

**匹配主题**：hydrologic model, flood
{: .label .label-green }

> 当历史数据有限且目标事件超出校准记录范围时，对概念性降雨-径流模型进行参数率定以预测极端降雨事件下流域响应是一个重大挑战。Nash-Sutcliffe效率等标准评价指标对极端事件的权重相对于平均状况偏低，导致模型系统性地低估尾部行为。本研究提出了一种校准框架，通过基于分位数的损失函数并结合区域频率分析的暴雨缩放约束，明确针对未见过的极端洪水进行表达。在澳大利亚大量流域的应用验证中，该方法显著降低了极端流量的系统性低估，同时保持了对中值条件的合理预测性能。

---

### Fire can explain rainfall-runoff shifts during and after drought

**作者**：Sreelakshmi Cherampatta Mana, Tim Peterson, Barry Croke, Takuya Iwanaga, Steven J. Lade

**期刊**：*Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135776](https://doi.org/10.1016/j.jhydrol.2026.135776) · **引用数**：0

**匹配主题**：runoff, drought
{: .label .label-green }

> 摘要暂不可用。

---

### A three-layer parameterization framework for ENSO-runoff coupling: Enhanced flood risk in the Huaihe River Basin under climate change

**作者**：Xianyong Meng, Zhenfei Ge, Jianli Ding, Guoqing Wang, Yiping Wu, Chengbin Chu 等

**期刊**：*Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103562](https://doi.org/10.1016/j.ejrh.2026.103562) · **引用数**：0

**匹配主题**：runoff, streamflow
{: .label .label-green }

> 研究区域：中国淮河流域，该区域受ENSO事件影响显著。研究重点：本研究在SWAT模型内构建了三层参数化框架，以定量表达ENSO对流域径流过程的影响。该框架将ENSO的水文影响分解为三个机制路径：降水变率、气温驱动的蒸散发变化，以及融雪时间调整。在预计的ENSO强化和气候变暖情景下，淮河流域厄尔尼诺年的洪水风险显著升高，峰值流量相较历史基准可能增加15%至30%。

---

### CMIP6 multi-model projections and glacier-explicit hydrological modelling for seasonal runoff shifts in the Hunza River Basin

**作者**：Hafsah Batool, Jamal Hassan Ougahi, Amir Ali, Ameer Faisal, Maira Malik, Syed Mahmood 等

**期刊**：*Meteorology and Atmospheric Physics* · **DOI**: [10.1007/s00703-026-01149-4](https://doi.org/10.1007/s00703-026-01149-4) · **引用数**：0

**匹配主题**：hydrologic model, runoff, streamflow, seasonal, hydropower
{: .label .label-green }

> 摘要暂不可用。

---

## 水文模型开发与参数率定

本周模型开发涵盖从地下物理机制到冠层过程、再到全球尺度强迫评估的完整范围。Kootanoor Sheshadrivasan与Langhammer提出了GWSWEX v1.0双求解器方法，在物理机制完备的地下水表达与计算可行的分布式建模之间架起桥梁。Cebulski等人对多种森林类型的积雪截留参数化方案进行了系统评估，填补了覆盖全球23%陆地面积的地表能量收支研究空白。Ruelland等人提出了集成冰川演化模块的雪-冰-径流模型，并采用多指标约束校准。HESS上的一项里程碑式工作（Abbas等人）在18428个流域中对24套降水格网数据集进行了权威基准评估。此外，两篇发表于Journal of Hydrology Regional Studies的论文分别展示了针对岩溶流域的机器学习校准技术和基于梯度提升的径流率定方法。

### GWSWEX v1.0: a dual-solver 1D unsaturated zone model for mass-conservative groundwater recharge and runoff computation in distributed hydrological modelling

**作者**：Veethahavya Kootanoor Sheshadrivasan, Jakub Langhammer

**期刊**：*Geoscientific Model Development（预印本）* · **DOI**: [10.5194/egusphere-2026-2941](https://doi.org/10.5194/egusphere-2026-2941) · **引用数**：0

**匹配主题**：hydrology, hydrologic model, runoff
{: .label .label-green }

> 在区域尺度集成水文建模中，地下水、非饱和带与地表水耦合动态的精确数值表达一直是持续性挑战。三维求解Richards方程的物理过程模型可以严格描述垂直通量，但其计算成本高、参数不确定性强，且倾向于在优先流和非平衡流情形下过度强调毛管力，限制了其作为分布式模型中独立非饱和带模块的适用性。GWSWEX v1.0通过双求解器策略解决上述问题：在常规条件下采用快速运动波求解器，在近饱和状态下切换为Richards方程求解器。该模型在设计上保证质量守恒，并已通过解析解和渗漏计实验进行基准验证。

---

### An Evaluation of New Snow Interception and Ablation Parameterisations in Continental, Subarctic and Maritime Needleleaf Forests

**作者**：Alex C. Cebulski, John W. Pomeroy, William C. Floyd

**期刊**：*Hydrological Processes* · **DOI**: [10.1002/hyp.70573](https://doi.org/10.1002/hyp.70573) · **引用数**：0

**匹配主题**：hydrology, hydrologic model, land surface model
{: .label .label-green }

> 森林冠层对积雪的截留发生在全球约23%的陆地面积上，显著影响冠层下的积雪积累和地表能量交换。积雪截留过程受气象条件和冠层密度的强烈影响，在不同气候带、季节和森林类型中呈现不同的过程特征。近期研究揭示了一批新的积雪截留和冠层融雪参数化方案，有望在更广泛的冠层结构和气候条件下适用。本研究在三种典型森林环境中对三种新参数化方案与现有方案进行了对比评估：加拿大萨斯喀彻温省的大陆性针叶林、芬兰北部的亚北极针叶林，以及加拿大不列颠哥伦比亚省的海洋性针叶林。新参数化方案在三种环境中均表现出更好的适应性。

---

### Representing glacier evolution for modelling hydrological responses to climate change in mountainous catchments

**作者**：Denis Ruelland, Florian Antoine, Antoine Rabatel

**期刊**：*Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135769](https://doi.org/10.1016/j.jhydrol.2026.135769) · **引用数**：0

**匹配主题**：hydrologic model, runoff, streamflow
{: .label .label-green }

> 集成冰川演化模块的简约型雪-冰-径流模型。采用流量、积雪和冰川数据的多指标约束校准。冰川退缩在不同阿尔卑斯流域引发了对比鲜明的径流响应轨迹。未来预测显示，大多数研究流域的峰值水量出现在2026–2055年之间。

---

### Comprehensive Global Assessment of 24 Gridded Precipitation Datasets Across 18,428 Catchments Using Hydrological Modeling

**作者**：A. Abbas, Y. Yang, M. Pan, Y. Tramblay, C. Shen, H. Ji 等

**期刊**：*Hydrology and Earth System Sciences (HESS)* · **DOI**: [10.5194/hess-30-3399-2026](https://doi.org/10.5194/hess-30-3399-2026) · **引用数**：0

**匹配主题**：hydrologic model, streamflow
{: .label .label-green }

> 为满足不同需求和应对不同挑战，众多格网降水数据集相继开发，但用户难以选择最适合的数据集。本研究利用水文模型对24套格网降水数据集在18428个流域中进行评估，提供了全球降水产品性能基准。结果显示，各数据集的表现具有强烈的区域和气候依赖性，没有任何单一产品在全球范围内均优于其他产品。将表现最优的数据集组合为集合的方法在所有区域均优于任何单一数据集，在雨量站网稀疏地区尤为突出。

---

### Modelling multi-component lagged hydrological responses in karst basins using a Bayesian-optimized dual-branch LSTM

**作者**：Hang Chen, Yu Bao Li, Lihua Chen

**期刊**：*Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103594](https://doi.org/10.1016/j.ejrh.2026.103594) · **引用数**：0

**匹配主题**：hydrologic model, runoff, streamflow
{: .label .label-green }

> 研究区域：中国西南部清江流域（QJB）。研究重点：由于岩溶流域独特的双流结构，精确预测日径流仍具有挑战性。为此，提出一种贝叶斯优化双分支LSTM，以同时表达以管道为主的快速流和以扩散基质为主的慢速流。双分支结构明确模拟了这两种流动路径的对比性滞后响应，贝叶斯优化则无需人工调参即可高效搜索超参数空间。应用于清江岩溶系统后，该模型在低流量、平均流量和高流量条件下均优于标准LSTM和基于过程的岩溶模型。

---

### Basin runoff calibration using gradient boosting decision trees: Impact of dual gridded potential evapotranspiration sources on model performance

**作者**：Ali Amiri, Feza Örüç

**期刊**：*Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103574](https://doi.org/10.1016/j.ejrh.2026.103574) · **引用数**：0

**匹配主题**：runoff, streamflow
{: .label .label-green }

> 研究区域：土耳其布尔萨半湿润地区的伊兹尼克盆地（Iznik Basin），一个具有显著人为影响和水文敏感性的内流集水区。研究重点：利用梯度提升决策树（GBDT）进行流域径流率定，系统评估两套格网潜在蒸散发（PET）数据——基于ERA5和基于GLEAM的估算——对率定性能的影响敏感性。PET公式的差异在率定性能上产生了显著差异，凸显了数据驱动水文率定中PET数据集选择的重要性。

---

### Assessing Hydrological Responses to Land Use Type Transition in Watershed with Reservoir Operation Using SWAT Model

**作者**：Hiyaw Hatiya Ware, Il-Moon Chung, Ju-Young Shin, Myoung-Jin Um

**期刊**：*Water Resources Management* · **DOI**: [10.1007/s11269-026-04766-1](https://doi.org/10.1007/s11269-026-04766-1) · **引用数**：0

**匹配主题**：hydrology, hydrologic model, streamflow, reservoir
{: .label .label-green }

> 摘要暂不可用。

---

## 机器学习与深度学习径流预测

本周机器学习水文应用领域同时呈现了前沿模型架构创新和基础设施建设两方面进展。FlowGATFormer（Liu等人）将图注意力网络与时序注意力机制结合，用于时空径流预测；Hagen等人证明LSTM可以将GCM信号转化为挪威日径流，用于洪水预估。Jahangir等人引入知识蒸馏框架，在压缩大型水文深度学习模型的同时保留其预测性能。在基础设施方面，Singh等人提出HydroModelSpec——一种标准化交换格式，有望为机器学习水文模型做到NetCDF对格网数据所做的贡献；Gao等人则提出多源自适应融合迁移学习方法，专门针对数据稀缺流域的预测难题。Liu等人通过整合深度学习与过程机制模型完成了60天径流预报框架，贡献了最后一项研究。

### FlowGATFormer: A streamflow prediction model based on spatiotemporal dual attention

**作者**：Feng Liu, Zhigang Han, J H, Peiqing Xiao, Pan Zhang, Fengrui Chen 等

**期刊**：*Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135771](https://doi.org/10.1016/j.jhydrol.2026.135771) · **引用数**：0

**匹配主题**：hydrologic model, streamflow
{: .label .label-green }

> 实现高精度长期河流径流预测对模拟陆地水文循环和水资源管理至关重要。然而，传统水文模型难以捕捉复杂的非线性关系，现有深度学习模型也无法有效整合水文站点间的空间依赖性与时序动态。本文提出FlowGATFormer，一种结合图注意力网络（GAT）与具有双注意力机制的Transformer编码器的径流预测模型。空间注意力模块通过学习得到的邻接图捕捉站点间水文关系，时序注意力模块则根据各历史时间步对预测目标的相关性进行加权。在多个中国河流流域的基准测试中，FlowGATFormer在1–30天预见期的表现达到当前最优水平。

---

### Using sequential and non-sequential LSTM neural networks with global climate model forcing for daily streamflow reconstruction and flood projection

**作者**：J. S. Hagen, D. Lawrence, A. Sorteberg

**期刊**：*Hydrology research* · **DOI**: [10.1016/j.hydrch.2026.100017](https://doi.org/10.1016/j.hydrch.2026.100017) · **引用数**：0

**匹配主题**：hydrologic model, streamflow, flood
{: .label .label-green }

> 气候变化正在改变高纬度流域的洪水特征。本研究评估了LSTM神经网络将大尺度大气模式变化转化为两个具有不同洪水机制的挪威流域日径流的能力——一个为降雨主导的沿海流域，一个为融雪主导的内陆流域。对序列型（标准LSTM）和非序列型（并行）两种架构均采用ERA5校正的GCM输出作为驱动。非序列方法在降雨主导流域表现更优，但在融雪主导流域的附加价值有限。在RCP8.5情景下，两个流域均预测秋季洪峰增大，其中沿海流域的相对变化幅度更大。

---

### Knowledge Distillation for Improving Deep Learning-Based Hydrological Prediction and Fine-Tuning

**作者**：M. S. Jahangir, J. Quilty, S. Steinschneider, J. Adamowski

**期刊**：*Journal of Geophysical Research Machine Learning and Computation* · **DOI**: [10.1029/2025jh001081](https://doi.org/10.1029/2025jh001081) · **引用数**：0

**匹配主题**：hydrologic model, streamflow
{: .label .label-green }

> 本文将知识蒸馏（KD）引入深度学习水文预测领域。深度学习模型（包括LSTM及相关架构）的预测性能往往受限于训练数据不足、高维参数空间以及过拟合风险。KD将大型、训练充分的教师模型的知识迁移到更小的学生模型中，产生的紧凑模型在保留教师模型精度的同时更易于微调应用到新流域。在CAMELS流域集的多样化流域上应用后，KD训练的学生模型以少40%至60%的参数量达到或超过基准LSTM的性能，在数据稀缺和水文复杂流域中的提升尤为显著。

---

### AI-driven seasonal streamflow prediction in Victoria: a focus on ENSO climate predictor

**作者**：Sabrina Bani, I. Hossain, M. Imteaz, Patrick Ryan Morrison

**期刊**：*Stochastic Environmental Research and Risk Assessment* · **DOI**: [10.1007/s00477-026-03256-5](https://doi.org/10.1007/s00477-026-03256-5) · **引用数**：0

**匹配主题**：streamflow, seasonal
{: .label .label-green }

> 季节性径流预测在澳大利亚东南部水资源调配中发挥着关键作用，该地区的水文气候变率受大尺度海气相互作用主导。本研究对多种基于人工智能的季节性径流预测模型（LSTM、随机森林、XGBoost）在维多利亚流域中有无ENSO指数作为预测因子的情况进行了对比评估。ENSO信息输入的模型在秋季和冬季预测中显著优于无ENSO信息的模型，反映了厄尔尼诺-南方涛动对维多利亚降雨的主导遥相关模式。最优配置在预见期达四个月的季节预测中Nash-Sutcliffe效率超过0.75。

---

### Multi-Source Adaptive-Fusion Transfer Learning for Streamflow Forecasting in Data-Scarce Catchments

**作者**：Yuxuan Gao, Dongfang Liang, Edoardo Borgomeo, Hiroshi Cho

**期刊**：*ESSOAr（预印本）* · **DOI**: [10.22541/essoar.15004149/v1](https://doi.org/10.22541/essoar.15004149/v1) · **引用数**：0

**匹配主题**：hydrology, streamflow
{: .label .label-green }

> 许多地区的流量测站记录稀缺，限制了水文预测能力。迁移学习（TL）利用数据丰富的源域知识改善数据稀缺目标流域的预测，已成为颇具前景的方法。然而，现有迁移学习方法通常依赖单一源域，忽略了多个候选源流域之间的知识异质性。本文提出多源自适应融合迁移学习（MSAFTL）框架，根据各源流域的水文相似性和知识可迁移性自适应加权其贡献。在亚洲和非洲数据稀缺流域的广泛评估中，MSAFTL显著优于单源迁移学习和从头训练的LSTM，数据最匮乏的场景中提升幅度最大。

---

### HydroModelSpec: Toward Standardized Machine Learning Model Exchange in Hydrology

**作者**：Nikhil Singh, Ramteja Sajja, Yusuf Sermet, Ibrahim Demir

**期刊**：*EarthArXiv（预印本）* · **DOI**: [10.31223/x53v1b](https://doi.org/10.31223/x53v1b) · **引用数**：0

**匹配主题**：hydrology, streamflow
{: .label .label-green }

> 水文预报深度学习模型（CNN、LSTM、Transformer等）的快速增长催生了一个碎片化生态系统，训练好的模型与其原始框架、训练数据集和预处理流程深度绑定，阻碍了可重复性、基准测试和业务化部署。HydroModelSpec提出了一种标准化交换格式——类似于通用机器学习模型的ONNX——专为水文模型定制：不仅编码模型权重和架构，还包括驱动变量定义、流域元数据、归一化方案和率定历史。针对基于PyTorch的模型提供了参考实现，并为常用水文深度学习框架提供了转换工具。

---

### Enhancing hydrological hazard early warning: a 60 d streamflow forecasting framework integrating deep learning and process-based modeling

**作者**：Zhijie Liu, Hanbo Yang, Dawen Yang

**期刊**：*Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-26-2353-2026](https://doi.org/10.5194/nhess-26-2353-2026) · **引用数**：0

**匹配主题**：hydrologic model, streamflow, hydropower
{: .label .label-green }

> 可靠的中长期径流预报是水文灾害早期预警和水资源管理的核心，但在足够预见期内实现高精度预测仍具挑战。本文提出混合框架，将过程机制水文模型（提供物理约束和状态变量）与深度学习后处理器（纠正系统误差并捕捉非线性动态）结合，实现60天径流预报。框架在跨越多种水文气候区的中国河流流域进行了评估。混合方法在超过30天预见期时一致优于纯过程机制模型和纯数据驱动基准，在具有强烈季节性动态和年际变率的流域中相对提升最大。

---

## 水资源与水文气候动态

最后这一主题涵盖不同空间尺度和区域背景下的应用与观测水文研究。Wang等人发现印度河上游流域降雪比例的下降已在改变径流季节性——对全球冰川供水流域具有重要预警意义。Luan等人构建了人类活动驱动下河岸带地表水-地下水交互过程的高分辨率日尺度模型。Zou等人利用遥感技术记录了黄河流域38年的水库水面动态，而Huang等人则揭示了青藏高原湖泊从内流向外流排水的类临界点转变。另有两项研究分别探讨了气候湿润化背景下湿地-农业流域的水文变化，以及Bago河流域对气候变化的径流响应。

### Streamflow seasonality responds to changes in snowfall fraction in the Upper Indus Basin

**作者**：Yixuan Wang, Yan-Jun Shen, Xiaolong Zhang, Muhammad H. Zaman, Muhammad Attique Khan

**期刊**：*Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.135773](https://doi.org/10.1016/j.jhydrol.2026.135773) · **引用数**：0

**匹配主题**：streamflow, seasonal
{: .label .label-green }

> 摘要暂不可用。

---

### Daily-Resolution Modelling of Surface Water–Groundwater Interaction Under Multiple Human Activities in a Riparian Zone

**作者**：Qinghua Luan, Yuhara Yamamoto, Qingyan Sun, Chuiyu Lu, Weichen Wu, Chu Wu 等

**期刊**：*Hydrological Processes* · **DOI**: [10.1002/hyp.70578](https://doi.org/10.1002/hyp.70578) · **引用数**：0

**匹配主题**：streamflow, surface water
{: .label .label-green }

> 地表水-地下水相互作用（SGI）是水循环的重要过程，其显著的异质性受到日益加剧的人类活动影响。在多种人类活动下以日分辨率理解SGI仍是一项重要的建模挑战。本研究为一个受灌溉抽水、河流调控和土地利用变化影响的河岸带构建了地表水-地下水耦合模型，以日分辨率解析河流-含水层界面的交换通量，并利用测压水位记录和流量观测进行验证。结果表明，灌溉抽水和河流调控操作共同解释了超过60%的日SGI通量时间变率，凸显了人类管理相对于气候变率在河岸带水文中的主导作用。

---

### Long-term reservoir surface water dynamics in the Yellow River Basin (1986–2024)

**作者**：Yebin Zou, Peiyu Cong, Shuaijuan Zhang, Xiying Wang, Pan Pan, Guoce Gao 等

**期刊**：*Journal of Arid Environments* · **DOI**: [10.1016/j.jaridenv.2026.105656](https://doi.org/10.1016/j.jaridenv.2026.105656) · **引用数**：0

**匹配主题**：reservoir, surface water
{: .label .label-green }

> 摘要暂不可用。

---

### From endorheic to exorheic: Tibetan lake hydrodynamics driven by global change and hydrological reorganization and implications to Mars

**作者**：Chang Huang, Zikang Li, Gaia Stucky de Quay, Zhongping Lai

**期刊**：*Global and Planetary Change* · **DOI**: [10.1016/j.gloplacha.2026.105546](https://doi.org/10.1016/j.gloplacha.2026.105546) · **引用数**：0

**匹配主题**：hydrology, earth system model
{: .label .label-green }

> 摘要暂不可用。

---

### Hydrological Changes to Climate Wetting in a Wetland-Dominated Agricultural Watershed

**作者**：Sharhad Wainty, Taufique H. Mahmood

**期刊**：*Hydrological Processes* · **DOI**: [10.1002/hyp.70589](https://doi.org/10.1002/hyp.70589) · **引用数**：0

**匹配主题**：hydrology, streamflow
{: .label .label-green }

> 理解降水输入通量如何分配为蒸散发（ET）和径流（Q）输出通量，对于认识气候变化下的水文响应至关重要。本研究以美国/加拿大红河流域的一个湿地主导型农业流域为研究区。研究定量描述了历史气候湿润化趋势下的水文响应，并评估Budyko框架是否能够捕捉观测到的变化。结果显示，在气候湿润化背景下，由于湿地蓄水填充和饱和-超渗产流机制，产流系数非线性增大，需要对标准Budyko参数化进行扩展。

---

### Streamflow response to climate change in the Bago River Basin using SWAT+ hydrological model

**作者**：Cho Cho Tun, Zin Mar Lar Tin San, Win Win Zin

**期刊**：*Journal of Water and Climate Change* · **DOI**: [10.2166/wcc.2026.092](https://doi.org/10.2166/wcc.2026.092) · **引用数**：0

**匹配主题**：hydrologic model, streamflow
{: .label .label-green }

> 利用QGIS处理DEM、土壤和土地覆盖数据推导径流；SWAT+模型经过观测数据率定，采用偏差校正的GCM输入进行未来气候和影响评估。将多个CMIP6模型的气候变化预测应用于缅甸Bago河流域，评估年际和季节性径流的未来变化。结果表明，在所有变暖情景下，雨季峰值流量普遍增加，旱季基流减少，对该流域水资源管理基础设施的水电和灌溉功能产生影响。

---

## 统计信息

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题词数 | 16 |
| 获取论文总数 | 1,232 |
| 去重后 | 1,045 |
| LLM相关性筛选后 | 26 |
| 已拒绝（不相关） | 1,019 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|------:|
| Journal of Hydrology | 4 |
| Hydrological Processes | 4 |
| Journal of Hydrology Regional Studies | 4 |
| Nature Communications | 1 |
| Water Resources Research | 1 |
| Natural Hazards and Earth System Sciences | 1 |
| Hydrology and Earth System Sciences | 1 |
| Earth Systems and Environment | 1 |
| Hydrology research | 1 |
| Journal of Geophysical Research Machine Learning | 1 |
| Stochastic Environmental Research and Risk Assessment | 1 |
| Water Resources Management | 1 |
| Global and Planetary Change | 1 |
| Journal of Arid Environments | 1 |
| Journal of Water and Climate Change | 1 |
| Meteorology and Atmospheric Physics | 1 |
| 预印本（ESSOAr/EarthArXiv/GMD） | 3 |

## 筛选标准

**主题词**：hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**：Semantic Scholar, OpenAlex

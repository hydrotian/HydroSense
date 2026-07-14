---
layout: default
title: "第27周（6月30日 - 7月7日），19篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/july/2026-07-07-weekly-review
date: 2026-07-07
categories: [weekly-zh, 2026, july]
tags: [hydrology, literature-review, research]
paper_count: 19
highlight: "一个自主AI智能体在无人工干预的条件下完成了水文模型的率定与模拟闭环，标志着自动化模型开发新范式的到来。"
---

# 每周文献综述
{: .no_toc }

**第27周** · 2026年6月30日–7月7日
{: .text-grey-dk-000 }

发现 **19** 篇相关论文，涵盖 **6** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

本周最突出的成果是一个概念验证AI智能体，它能自主率定并运行水文模型，填补了模型开发中"人在回路"的缺口（GRL）。此外，本周在陆面模型参数估算与状态依赖误差结构方面取得新进展，将机器学习进一步深入到洪水预报和水电预测领域，并为多年冻土和冰川流域的冰冻圈–水文耦合带来了新的观测和模拟证据。水库调度与干旱监测研究以决策支持框架和混合时间序列模型收尾，可直接应用于业务实践。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 大尺度水文与陆面模型

本周在大尺度水文模型的过程表达与参数估算方面从多个角度取得进展。Wang等人发表了CSSPv3——社区简单随机水库模型的重大修订版（JAMES），重构了地下侧向流并改进了积雪与冻土物理过程，显著降低了CONUS全年径流季节性偏差。此外，WRR发表的新型参数传递路径能量最小化方案（PATPEMS）算法提供了一种计算效率高的方式，在遵守地形约束的前提下将率定参数从有资料流域转移至无资料流域——这是走向大陆尺度参数区域化的关键一步。另外两篇WRR论文关注模型结构不确定性：Jiang等人表明冻土参数化方案显著改变了寒冷地区径流季节性模拟，揭示了ESM陆面分量中哪些过程表达值得重点关注；一篇新WRR论文证明，将模型残差视为状态依赖而非常数可同时改善概念性降雨-径流模型的参数可识别性与不确定性量化。

### CSSPv3: A Major Revision of the Community Simple Stochastic Pool Model With Improved Subsurface and Snow Processes

**作者**：Yan Wang, L. Ruby Leung, Teklu K. Tesfa et al.

**期刊**：*Journal of Advances in Modeling Earth Systems* · **DOI**：[10.1029/2025ms005440](https://doi.org/10.1029/2025ms005440) · **引用数**：3

**匹配主题**：hydrologic model, land surface model, earth system model, runoff, streamflow
{: .label .label-green }

> 我们提出CSSPv3——社区简单随机水库模型的重大修订版，具有重构的地下侧向流、改进的积雪与冻土物理过程以及更新的参数估算方法。在CONUS河流流域的评估表明，与CSSPv2相比，季节性径流和雪水当量偏差显著减小，尤其是在冷季表现有所改善。CSSPv3专为与E3SM陆面和河流分量集成用于大陆尺度模拟而设计。

---

### A Parameter Transmission Path Energy Minimization Scheme (PATPEMS) for Hydrologic Model Regionalization

**作者**：Lihua Xiong, Linyang Min, Chongyu Xu et al.

**期刊**：*Water Resources Research* · **DOI**：[10.1029/2025wr040933](https://doi.org/10.1029/2025wr040933) · **引用数**：2

**匹配主题**：hydrologic model, runoff, streamflow, river
{: .label .label-green }

> 将率定参数从有资料流域转移至无资料流域仍是区域水文学的核心挑战。我们提出PATPEMS，通过最小化兼顾水文相似性与沿地形流路空间连续性的能量泛函来实现这一目标。在中国200余个流域的应用中，PATPEMS在再现无资料流域径流季节性和洪峰流量方面优于克里金法和最近邻方法。

---

### Effects of Frozen Soil Parameterizations on Simulated Streamflow Seasonality in Cold-Region Basins

**作者**：Libo Jiang, Zhenghui Xie, Yongkang Xue et al.

**期刊**：*Water Resources Research* · **DOI**：[10.1029/2025wr041331](https://doi.org/10.1029/2025wr041331) · **引用数**：1

**匹配主题**：hydrologic model, land surface model, streamflow, seasonal
{: .label .label-green }

> 冻土控制着寒冷地区的水分入渗与产流，但不同陆面模型中的参数化方案差异显著。我们使用多方案陆面模型对30个北极和高山流域的四种冻土方案进行评估。不同方案模拟的春季洪峰流量相差高达40%，且方案选择影响了若干流域未来径流变化的符号，凸显了ESM中改进过程表达的必要性。

---

### State-Dependent Residual Structures for Improved Parameter Identifiability in Rainfall–Runoff Models

**作者**：Florian Ulrich Jehn, Lena Katharina Schmidt, Till Francke et al.

**期刊**：*Water Resources Research* · **DOI**：[10.1029/2026wr044285](https://doi.org/10.1029/2026wr044285) · **引用数**：0

**匹配主题**：hydrologic model, runoff, streamflow
{: .label .label-green }

> 水文模型率定中的标准似然函数假设残差具有同方差性，但降雨-径流模型的误差通常是状态依赖的。我们在贝叶斯框架内对50个CAMELS流域实施并比较了五种残差误差模型——从常方差到完全异方差形式。状态依赖形式在所有情况下均能改善参数可识别性，并生成更好率定的预测不确定性，尤其在低流量时期表现突出。

---

## AI与机器学习在水文学中的应用

本周机器学习应用取得显著进展：一篇里程碑论文展示了自主AI驱动的水文模型率定，一个专为深度学习设计的新全球河网数据集问世，两篇关于物理-ML混合洪水预报的论文，以及一篇将LSTM应用于径流式水电的研究。Feng等人（GRL）提出的AI智能体框架整合了LLM推理、Python代码执行与迭代反馈，在无人工干预的条件下完成HBV率定——该智能体自主提出参数范围、运行模拟、评估性能并持续优化直至收敛。这一概念验证将模型率定重新定义为AI任务而非人工监督优化。GLORIF1数据集（Scientific Data）以1公里分辨率提供全球河网属性，专为深度学习训练策划，填补了机器学习水文输入数据长期缺失的空白。在洪水方面，一个可微分混合模型（EGUSphere）将基于物理的淹没核心与可学习参数耦合，在保持物理可解释性的同时达到黑盒ML精度；一个堆叠HBV-VMD-att-BiLSTM模型（JHM）将小波分解与注意力机制集成用于流域尺度洪水预报。此外，《Renewable Energy》的一篇论文表明，基于气候再分析数据训练的LSTM模型能够在季节提前量下以经济上有用的技巧预测径流式水电发电量。

### An AI Agent Framework for Autonomous Hydrologic Model Calibration

**作者**：Yalan Song, Chaopeng Shen, Tadd Bindas et al.

**期刊**：*Geophysical Research Letters* · **DOI**：[10.1029/2025gl119814](https://doi.org/10.1029/2025gl119814) · **引用数**：8

**匹配主题**：hydrologic model, streamflow, earth system model
{: .label .label-green }

（亦收录于2026-07-04每日采集）

> 我们提出一个AI智能体，通过将大型语言模型（LLM）与迭代模拟-评估循环相结合，自主率定水文模型（HBV）。该智能体提出参数范围、执行Python模拟、诊断性能指标并优化方法直至收敛——无需人工监督。在50个CAMELS流域测试中，智能体达到了与人工专家调参相当的率定性能，为全自动模型开发流程开辟了新路径。

---

### GLORIF1: A Global River Network Dataset for Deep Learning Applications in Hydrology

**作者**：Soren Rasmussen, Ethan Yang, Jens Hesselbjerg Christensen et al.

**期刊**：*Scientific Data* · **DOI**：[10.1038/s41597-026-07658-6](https://doi.org/10.1038/s41597-026-07658-6) · **引用数**：1

**匹配主题**：hydrologic model, river, streamflow, flood
{: .label .label-green }

> GLORIF1是一个新的1公里分辨率全球河流属性数据集，专为水文深度学习训练编制。它整合了250万条河段的地形、气候、土壤和土地覆盖属性，并包含数据来源的质量标志。基准测试表明，在GLORIF1属性上训练的LSTM模型在无资料流域径流预测方面优于使用传统数据集训练的模型，在数据稀缺地区尤为突出。

---

### A Differentiable Hybrid Flood Inundation Model Coupling Physics and Deep Learning

**作者**：Qian Zhu, Dongkun Wang, Florian Pappenberger et al.

**期刊**：*EGUSphere (HESS preprint)* · **DOI**：[10.5194/egusphere-2026-3781](https://doi.org/10.5194/egusphere-2026-3781) · **引用数**：0

**匹配主题**：hydrologic model, flood, streamflow
{: .label .label-green }

> 我们开发了一个可微分混合洪水淹没模型，将浅水方程物理过程嵌入可微分计算框架中，允许通过梯度下降同时优化物理参数和可学习修正量。在15个欧洲洪水事件中应用，混合模型在匹配黑盒深度学习精度的同时保留了物理可解释参数，且对分布外事件的泛化能力更强。

---

### A Stacked HBV-VMD-Attention-BiLSTM Framework for Basin-Scale Flood Forecasting

**作者**：Yunzhu Liu, Xiang Zhang, Changming Li et al.

**期刊**：*Journal of Hydrometeorology* · **DOI**：[10.1175/jhm-d-25-0166.1](https://doi.org/10.1175/jhm-d-25-0166.1) · **引用数**：0

**匹配主题**：hydrologic model, flood, streamflow, seasonal
{: .label .label-green }

> 我们提出一个堆叠框架，将HBV概念模型、变分模态分解（VMD）、注意力机制和双向LSTM相结合，用于多步洪水预报。VMD将模型残差分解为频率分量，att-BiLSTM分别对各分量进行修正，在六个中国流域中将洪峰预报误差降低18–35%（相对于独立HBV）。

---

### Seasonal Prediction of Run-of-River Hydropower Generation Using Long Short-Term Memory Networks

**作者**：Eduardo Álvarez, María Bermúdez, Félix Francés et al.

**期刊**：*Renewable Energy* · **DOI**：[10.1016/j.renene.2026.126147](https://doi.org/10.1016/j.renene.2026.126147) · **引用数**：0

**匹配主题**：hydrologic model, hydropower, streamflow, seasonal, climate change
{: .label .label-green }

> 我们在ERA5再分析输入上训练LSTM模型，以30天至90天提前量预报西班牙40座水电站的月度径流式发电量。基于30年再分析数据训练的模型在30天提前量下大多数电站的纳什效率系数>0.70，90天提前量下降至0.55。该方法无需局地流量观测，为电网规划提供了业务上可用的季节预报。

---

## 洪水与极端事件

本周两篇论文从不同视角研究了洪水动态：对2024年9月多瑙河大洪水的详细法证分析，以及全球河流流量季节性的综合研究。Pöschl等人结合雷达定量降水估算、高分辨率水动力演算和洪后调查重建了2024年中欧洪水的水文链，将60%的史无前例洪峰归因于前期土壤饱和状态——这一发现与早期预警系统直接相关。《Science Bulletin》刊登的Liu等人论文分析了1200个全球河流的70年日径流记录，识别出积雪主导流域年洪峰提前的稳健趋势（每10年提前4–8天）以及季风主导流域夏季低流量的放大趋势，对持续变暖下的洪水季节性预测具有重要意义。

### Hydrological Analysis of the September 2024 Danube Flood: Causes, Dynamics, and Early Warning Implications

**作者**：Ulrich Pöschl, Stephan Thober, Oldrich Rakovec et al.

**期刊**：*Hydrology and Earth System Sciences* · **DOI**：[10.5194/hess-30-4075-2026](https://doi.org/10.5194/hess-30-4075-2026) · **引用数**：5

**匹配主题**：flood, hydrologic model, river, runoff, streamflow
{: .label .label-green }

> 我们使用高分辨率雷达降水、中尺度气象模型输出和率定的多瑙河流域水动力演算模型重建了2024年9月中欧洪水。前期连续多周降水导致的土壤水分饱和使洪峰流量比干燥前期情景高估60%。分析表明，3–5天提前量的有效预警需要准确的土壤水分初始化，而不仅仅是降水预报。

---

### Changing Seasonality of Global River Flow Over Seven Decades

**作者**：Yuanfang Liu, Fang Zhao, Bing Xu et al.

**期刊**：*Science Bulletin* · **DOI**：[10.1016/j.scib.2026.07.035](https://doi.org/10.1016/j.scib.2026.07.035) · **引用数**：2

**匹配主题**：river, streamflow, seasonal, climate change, flood, drought
{: .label .label-green }

> 利用1200个全球分布河流测站的日流量记录（1950–2023年），我们记录了流量季节性的显著趋势。积雪主导流域的春季洪峰以每10年4–8天的速率提前，而季风主导流域的夏季低流量放大。这些季节性变化已在35%分析流域中改变了洪水频率曲线，预计在未来变暖情景下将进一步加剧。

---

## 冰冻圈与气候变化对水资源的影响

本周三篇论文深化了对气候变化下冰冻圈对河流径流贡献的认识。Walvoord等人（Earth's Future）使用冻土-地下水-径流耦合模型表明，变暖多年冻土中活动层加深和穿透融区的形成使北极河流洪峰径流时机延迟数周至数月——这一反直觉响应挑战了"融化越多=径流越多"的简单叙事。《Hydrological Processes》刊登的Chen等人论文综合了高亚洲40年的径流、融雪量和冰川质量平衡记录，发现尽管冰川退缩加速，许多流域总冰冻圈径流贡献自1990年代峰值以来一直下降，原因是融雪量贡献的减少速度快于冰川融水增加速度。《Hydrological Processes》的另一篇Kling等人论文记录了阿尔卑斯流域干旱后径流非平稳性：严重干旱后3–5年内土壤结构改变和地下水储量减少导致径流-降水关系显著偏移，这对率定模型的可迁移性具有重要影响。

### Permafrost Thaw Delays Peak Discharge in Arctic Rivers: Evidence From a Coupled Permafrost–Streamflow Model

**作者**：Michelle A. Walvoord, Barret L. Kurylyk, Scott Lamoureux et al.

**期刊**：*Earth's Future* · **DOI**：[10.1029/2025ef007809](https://doi.org/10.1029/2025ef007809) · **引用数**：4

**匹配主题**：hydrologic model, river, runoff, streamflow, climate change
{: .label .label-green }

> 我们将CryoGrid-MODFLOW-径流耦合模型应用于三个北极河流流域，模拟多年冻土退化的水文响应。在RCP 8.5情景下，到2100年活动层加深和穿透融区的形成将洪峰径流时机延迟2–6周。延迟在穿透融区连通此前孤立地下水流路的连续多年冻土区最为明显，放大基流的同时抑制春季洪峰。

---

### Four Decades of Cryospheric Runoff Trends in High Mountain Asia: Declining Snow Offset by Increasing Glacier Melt

**作者**：Longxi Chen, Tao Che, Xin Li et al.

**期刊**：*Hydrological Processes* · **DOI**：[10.1002/hyp.70630](https://doi.org/10.1002/hyp.70630) · **引用数**：1

**匹配主题**：river, runoff, streamflow, climate change, seasonal, hydrologic model
{: .label .label-green }

> 我们综合了85个高亚洲流域40年的径流、融雪量估算和冰川质量平衡数据。尽管冰川退缩加速，大多数流域的总冰冻圈径流自1990年代以来一直下降，原因是历史上占主导地位的融雪量贡献下降速度快于冰川融水增加速度。大多数流域的交叉点（冰川融水开始因冰川缩小而下降）预计在2040至2060年间出现，之后总冰冻圈径流将急剧下降。

---

### Post-Drought Hydrological Non-Stationarity in Alpine Catchments

**作者**：Harald Kling, Gregor Laaha, Juraj Parajka et al.

**期刊**：*Hydrological Processes* · **DOI**：[10.1002/hyp.70632](https://doi.org/10.1002/hyp.70632) · **引用数**：0

**匹配主题**：drought, hydrologic model, runoff, streamflow, seasonal
{: .label .label-green }

> 我们通过分析40个阿尔卑斯流域2003、2015和2018年欧洲干旱前后的流量，检验严重干旱是否造成径流-降水关系的持久性偏移。大多数流域干旱后3–5年内径流系数存在结构性断点，由土壤大孔隙结构改变和地下水补给能力下降驱动。基于干旱前数据率定的模型对干旱后径流高估15–25%，凸显了长期干旱后重新率定或采用非平稳模型结构的必要性。

---

## 水库调度与水资源管理

本周三篇WRR论文在气候变化与不确定性决策交叉点上推进了水库与水资源管理研究。Engström等人分析了2021–2022年阿尔卑斯水电干旱对400座瑞士水库发电量的影响，分离了低于正常值的积雪量、高温和多月降水亏缺的贡献，并表明针对平均条件优化的运行策略比自适应策略多损失25%的发电量。Guo等人的方法论贡献开发了一个联合信息选择框架，识别水库放水决策所需气候和需求预测因子的最小集合，在保持预报精度的同时减少实时运行的计算负担。Yin等人的第三篇WRR研究评估了1.5°C和2°C变暖情景下12个主要灌溉区的灌溉需水量，发现即便调整播种历，作物需水量也增加8–15%，南亚（+18%）和中东（+22%）增幅最大。

### Alpine Hydropower Drought 2021–2022: Causes, Impacts, and the Role of Adaptive Operations

**作者**：Johanna Engström, Manuela Brunner, Lukas Gudmundsson et al.

**期刊**：*Water Resources Research* · **DOI**：[10.1029/2025wr042323](https://doi.org/10.1029/2025wr042323) · **引用数**：3

**匹配主题**：hydropower, reservoir, water management, drought, climate change, seasonal
{: .label .label-green }

> 2021–2022年阿尔卑斯干旱严重影响了瑞士及邻国的水电发电量。我们将400座水库的发电异常分解为积雪亏缺、温度异常和降水亏缺的贡献。自适应运行（基于更新入流预报的动态再优化）相对于气候学规则最多减少25%的发电损失。研究结果量化了季节性水文预报对水电规划在干旱频率增加背景下的经济价值。

---

### Joint Information Selection for Reservoir Release Decision-Making Under Climate and Demand Uncertainty

**作者**：Rong Guo, Vincent Sitzenfrei, Jan Kwakkel et al.

**期刊**：*Water Resources Research* · **DOI**：[10.1029/2025wr042745](https://doi.org/10.1029/2025wr042745) · **引用数**：1

**匹配主题**：reservoir, water management, seasonal, flood, drought
{: .label .label-green }

> 水库放水决策同时依赖气候预报和需求预测，但使用所有可用预测因子会导致过拟合和计算开销。我们提出一个联合信息选择框架，利用互信息和条件独立性检验识别在给定计算预算下最大化预报精度的最小预测因子集合。应用于五座瑞士水库，该框架在预报技巧损失不超过5%的情况下将预测因子空间缩减60%，实现了实时业务应用。

---

### Irrigation Water Demand Under 1.5°C and 2°C Warming: Global Assessment With Planting-Calendar Adaptation

**作者**：Shiqiang Yin, Camille Rodes Bachs, Yoshihide Wada et al.

**期刊**：*Water Resources Research* · **DOI**：[10.1029/2025wr041530](https://doi.org/10.1029/2025wr041530) · **引用数**：2

**匹配主题**：irrigation, water management, climate change, seasonal, land surface model
{: .label .label-green }

> 我们使用与CMIP6气候预测耦合的全球作物-水模型，在有无播种历调整适应的情景下估算1.5°C和2°C变暖下的灌溉需水量。即使播种日期优化，2°C变暖下总灌溉需水量也增加8–15%，南亚（+18%）和中东（+22%）增幅最大。地下水灌溉系统同时面临需求增加和补给减少的双重压力，本世纪中叶可能在若干地区超过可持续开采限制。

---

## 干旱监测与预测

本周两篇论文提供了互补的干旱分析方法。Christian等人（Communications Earth & Environment）开发了一个基于物理的骤发干旱诊断框架，使用ERA5和GLEAM数据的标准化异常指标分离降水亏缺、大气需求和土壤水分消耗的贡献，在全球尺度上以3–5天技巧识别骤发干旱起始。第二篇论文引入了一个混合Prophet-LSTM-BPNN模型用于季节性干旱预测，将Prophet的趋势分解能力与深度学习的非线性模式识别相结合；在10个中国流域1–3月提前量上优于独立LSTM和基于SPI的基准模型。

### A Physically Based Flash Drought Diagnostic Framework Using ERA5 and GLEAM

**作者**：Jordan I. Christian, Jeffrey B. Basara, Nathaniel Burke et al.

**期刊**：*Communications Earth & Environment* · **DOI**：[10.1038/s43247-026-03783-7](https://doi.org/10.1038/s43247-026-03783-7) · **引用数**：6

**匹配主题**：drought, hydrologic model, land surface model, seasonal
{: .label .label-green }

> 骤发干旱在数周内从正常状态迅速发展为严重水分胁迫，对传统干旱监测系统构成挑战。我们使用ERA5和GLEAM再分析产品开发了一个基于物理的诊断框架，分离来自降水亏缺、大气蒸发需求升高和前期土壤水分消耗的贡献。在1981–2024年全球应用中，框架以3–5天技巧识别骤发干旱起始，并揭示自2000年以来骤发干旱频率在大陆内部增加12%。

---

### A Hybrid Prophet-LSTM-BPNN Model for Seasonal Drought Prediction at Multiple Time Scales

**作者**：Linyan Bai, Hao Wang, Yongchuan Zhang et al.

**期刊**：*AI in Geosciences* · **DOI**：[10.1016/j.aiig.2026.100251](https://doi.org/10.1016/j.aiig.2026.100251) · **引用数**：0

**匹配主题**：drought, hydrologic model, seasonal, streamflow
{: .label .label-green }

> 我们开发了一个三阶段混合模型，结合Facebook Prophet（用于趋势和季节性分解）、LSTM（用于非线性残差模式学习）和BPNN（用于最终集成），以1、3和6个月提前量预测SPEI干旱指数。在10个中国流域的评估中，混合模型相对于独立LSTM将NSE提高0.08–0.15，相对于SPI线性模型提高0.12–0.20，在捕捉骤发干旱起始和结束事件方面技巧尤为突出。

---

## 统计信息

| 指标 | 数量 |
|:-----|-----:|
| 搜索数据库数 | 2 |
| 搜索主题数 | 28 |
| 获取论文总数 | 871 |
| 去重后 | 871 |
| 经LLM相关性筛选后 | 19 |
| 已拒绝（不相关） | 852 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|------:|
| Water Resources Research | 6 |
| Hydrological Processes | 2 |
| Geophysical Research Letters | 1 |
| Journal of Advances in Modeling Earth Systems | 1 |
| Hydrology and Earth System Sciences | 1 |
| Earth's Future | 1 |
| Science Bulletin | 1 |
| Scientific Data | 1 |
| Journal of Hydrometeorology | 1 |
| Renewable Energy | 1 |
| EGUSphere | 1 |
| Communications Earth & Environment | 1 |
| AI in Geosciences | 1 |

## 筛选标准

**主题关键词**：hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model, estuary, coastal, freshwater discharge, river plume, ocean biogeochemistry, marine heatwave, paleohydrology, paleoclimate, Quaternary, Holocene, Pleistocene, fluvial geomorphology, river terrace, loess, drainage network, river capture, landscape evolution, luminescence dating

**数据库**：Semantic Scholar, OpenAlex

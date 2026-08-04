---
layout: default
title: "第30周（7月21日 - 7月27日），19篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/august/2026-08-04-weekly-review
date: 2026-08-04
categories: [weekly-zh, 2026, august]
tags: [hydrology, literature-review, research]
paper_count: 19
highlight: "基于LSTM的混合模型在外推至更暖气候时优于纯过程模型和纯数据驱动方法；对大尺度模型中四种水库调度方案的基准测试表明，只有在辅助数据可用时，增加复杂度才有收益。"
---

# 每周文献综述
{: .no_toc }

**第30周** · 2026年7月21日–7月27日
{: .text-grey-dk-000 }

在**5**个主题下共找到**19**篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

本周文献的主线是将机器学习在水文学中的实际应用推向落地，同时不牺牲物理可解释性：混合LSTM模型在升温情景下表现出优越的分布外泛化能力；全球日径流预测模型和欧洲径流重建数据集进一步扩展了训练与基准测试生态系统。在建模方面，对大尺度模型中四种水库调度方案进行的罕见横向对比发现，复杂度的提升并非没有代价——只有在辅助库容数据可用时，增加参数化才能带来收益；利用高分辨率季节性灌溉图对CLM灌溉模块的更新将蒸散发偏差降低了约10%。洪水–干旱主题则凸显了观测选择如何左右结论：日均流量系统性地偏斜洪水季节性指标，格点降水产品的选择导致热带气旋径流预测存在15–40%的不确定性，而低成本积雪传感器网络可将SWE空间分辨率提高一倍以上。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 水文学中的机器学习与混合模型

过程模型与数据驱动水文建模之间的张力正在向中间路径收敛：将物理约束嵌入神经网络的混合架构。Kraft等人证明，这种混合设计并非表面文章——在基于古气候重建的分布外升温情景下评估时，混合模型优于纯LSTM和概念性过程模型，且随着气候偏离率定范围程度的增加，性能差距不断扩大。与此互补，AIFL全球径流预测模型通过迁移学习将基于LSTM的日径流预测扩展到全球21,428个站点，在无资料地区表现出强劲性能。在数据方面，EARLS数据集提供了5,030个欧洲流域73年（1951–2023）的日径流重建——填补了大陆尺度大样本水文学的关键空白。Beusch等人的AI降尺度研究增添了一个警示：在对大集合气候预测进行降尺度时，内部变率在小区域和短时间段内可能主导强迫信号，而这种效应在历史统计降尺度中被掩盖。最后，Slater等人对美国河流悬浮沉积物输移的分析发现，河流总体上携带了更多沉积物，但越来越集中在更短暂、更极端的事件中——这是历史记录训练的机器学习模型在没有明确趋势编码的情况下可能无法捕捉的非平稳性。

### Hybrid models generalize better to warmer climate conditions than process-based or LSTM models

**作者**: Kraft, B., Besnard, S., Reichstein, M., et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4667-2026](https://doi.org/10.5194/hess-30-4667-2026) · **引用数**: 1

**匹配主题**: hydrologic model, streamflow, climate change
{: .label .label-green }

> 结合过程知识与机器学习的混合模型在水文学中已显示出潜力；然而，它们超越率定范围进行泛化的能力——特别是在更暖气候下——仍未得到充分检验。我们在数百个流域中利用古气候重建推导的分布外升温情景，评估了三类模型（概念性过程模型、纯LSTM和混合LSTM）。混合模型在升温条件下始终优于两类替代方案，且随着温度偏离率定期的程度增大，性能差距也随之扩大。我们的结果表明，在神经网络架构中嵌入物理约束为气候外推提供了有意义的归纳偏置，超越了纯数据驱动或纯过程模型所能实现的效果。

---

### EARLS: a runoff reconstruction dataset for 5,030 European catchments (1951–2023)

**作者**: Tramblay, Y., Garambois, P.-A., Labarthe, B., et al.

**期刊**: *Earth System Science Data* · **DOI**: [10.5194/essd-18-5485-2026](https://doi.org/10.5194/essd-18-5485-2026) · **引用数**: 3

**匹配主题**: hydrologic model, runoff, streamflow
{: .label .label-green }

> 我们发布EARLS（欧洲大样本水文年径流与日径流）数据集，包含1951–2023年间5,030个欧洲流域的日径流重建。重建采用在有资料流域率定的区域化水文模型，通过参数空间插值推广至无资料站点。数据集包含流域属性（面积、坡度、土地覆被、地质、土壤）及气象驱动数据。EARLS旨在支持欧洲大陆的大样本水文学、模型基准测试和气候影响研究，填补长期有资料记录空间分布不均的缺口。

---

### AIFL: A global daily streamflow forecasting model using LSTM at 21,428 stations

**作者**: Liu, Y., Jiang, S., Zhou, L., Ren, L., et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.136064](https://doi.org/10.1016/j.jhydrol.2026.136064) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow, runoff
{: .label .label-green }

> 我们开发了AIFL，一个基于LSTM的全球日径流预测框架，覆盖全球21,428个站点。模型在有资料流域训练，通过基于流域属性的迁移学习推广至无资料地区。在不同气候带的评估表明，有资料和无资料站点均表现出强劲性能，大多数站点的纳什–苏克利夫效率超过0.7。AIFL为水资源规划、洪水预警和气候影响评估提供了可扩展的全球尺度径流预测基础设施。

---

### U.S. rivers transporting more suspended sediment, often in less time

**作者**: Slater, L. J., Singer, M. B., Feld, C. K., et al.

**期刊**: *Communications Earth & Environment* · **DOI**: [10.1038/s43247-026-03847-8](https://doi.org/10.1038/s43247-026-03847-8) · **引用数**: 0

**匹配主题**: river, streamflow, climate change
{: .label .label-green }

> 对美国河流悬浮沉积物输移的长期趋势分析揭示，许多站点的年输沙量在增加，但这些沉积物越来越集中于更少、更极端的洪水事件中。对多年代水文测站记录的分析表明，流量–输沙关系已发生非平稳变化，洪水事件期间峰值浓度更高，但基流贡献减少。这些趋势对河流碳输出、水库淤积和水生生境具有重要影响，并表明历史水位–沙量关系曲线可能低估了在降水制度改变下的未来输沙量。

---

### Downscaling with AI reveals large role of internal variability in regional climate projections

**作者**: Beusch, L., Gudmundsson, L., Seneviratne, S. I., et al.

**期刊**: *Climate Dynamics* · **DOI**: [10.1007/s00382-026-08269-y](https://doi.org/10.1007/s00382-026-08269-y) · **引用数**: 2

**匹配主题**: climate change, hydrologic model
{: .label .label-green }

> 利用深度学习对全球气候模式大集合模拟进行统计降尺度，以量化内部气候变率对区域降水和温度预测的贡献。在次大陆尺度和年代际时间尺度上，内部变率在中纬度地区可能主导强迫信号。这些发现警示不应将单集成成员的降尺度结果解读为可靠的区域信号。AI降尺度方法实现了对完整集合的高效采样，首次在高空间分辨率下使不确定性分解在计算上可行。

---

## 陆面模式与地球系统模式

本周三篇论文改进了陆面和地球系统模式对水分分配的模拟方式。Sinha等人将CLM的静态默认灌溉图替换为源自遥感的高分辨率季节性灌溉图，将年均蒸散发偏差降低约10%，并提升了模式捕捉年内灌溉脉冲的能力——与耦合地球系统模式中的水分胁迫诊断直接相关。冰冻圈刊发的论文将ISBA积雪水当量模拟与土地覆被变率进行基准对比，表明森林冠层截留和冠层遮荫能够解释当前典型地球系统模式网格尺度下无法分解的大部分区域SWE偏差。GRL论文关于CLM/CESM中的跨季节滞回现象（在7月22日日报中交叉引用）揭示，在湿润与干燥半年期间，地表能量和土壤水分通量遵循不同的相空间轨迹——这种记忆效应若模式假设对称的季节响应则会偏斜多年趋势归因。

### Improving irrigation and evapotranspiration simulation in CLM using a seasonal irrigation map

**作者**: Sinha, E., Bisht, G., Leung, L. R., et al.

**期刊**: *Geoscience Letters* · **DOI**: [10.1186/s40562-026-00500-2](https://doi.org/10.1186/s40562-026-00500-2) · **引用数**: 0

**匹配主题**: land surface model, irrigation, earth system model
{: .label .label-green }

> 我们评估了将CLM静态、粗分辨率灌溉范围图替换为源自遥感的高分辨率季节性灌溉图对模拟蒸散发和土壤水分的影响。更新后的图件捕捉了默认静态表示所缺失的灌溉面积年内变率。与FLUXNET和GRACE观测对比，季节性图件在美国、南亚和东亚主要灌区将年均蒸散发偏差降低约10%。改进在灌溉需求最高的生长季旺期最为显著。这些结果表明，真实的灌溉表征对于准确描述地球系统模式中陆气耦合至关重要。

---

### Assessing land cover effect on ISBA snow water equivalent simulation over Europe

**作者**: Decharme, B., Delire, C., Martin, E., et al.

**期刊**: *The Cryosphere* · **DOI**: [10.5194/tc-20-4099-2026](https://doi.org/10.5194/tc-20-4099-2026) · **引用数**: 0

**匹配主题**: land surface model, seasonal
{: .label .label-green }

> 我们评估了ISBA陆面模式积雪水当量模拟对欧洲山区土地覆被表示的敏感性。通过比较默认和高分辨率土地覆被数据集的模拟结果，量化了森林冠层截留和冠层短波遮荫对SWE偏差的作用。林区流域在积累峰值期表现出系统性SWE高估，区域偏差可达30%。亚网格异质性参数化方案在无需完全提高分辨率的情况下显著减小了这些误差。研究结果对改进用于季节预报和气候预测的地球系统模式中积雪参数化具有直接意义。

---

### Interseasonal Hysteresis in CLM/CESM surface energy and soil water across North America

**作者**: Li, H., Leung, L. R., Huang, M., et al.

**期刊**: *Geophysical Research Letters* · **DOI**: [10.1029/2026gl121975](https://doi.org/10.1029/2026gl121975) · **引用数**: 0

**匹配主题**: land surface model, earth system model, seasonal
{: .label .label-green }

（同时收录于2026年7月22日日报）

> 我们记录了CLM/CESM模拟的北美地表能量平衡和土壤水分中显著的跨季节滞回现象：湿润（春夏）和干燥（秋冬）季节轨迹在地表能量–土壤水分相空间中遵循不同路径。这种滞回行为源于植被物候、土壤热惯性以及土壤水分与蒸散发非线性关系的不对称反馈。滞回幅度因生态系统类型而异，在湿润与干旱气候过渡带最强。忽略这种不对称性会偏斜多年趋势归因以及耦合模式输出中年际变率的解读。

---

## 水库运行与水-能源纽带

本周的水库主题涵盖从长期热力结构监测到多目标可再生能源调度的广泛内容。Yassin等人迄今最为严格地对四种水库调度方案进行了基准测试——固定库容目标、调度曲线、优化调度和深度学习模拟器——在679个全球水库中发现，只有在辅助库容观测数据可用于率定的情况下，更复杂方案才能优于简单方案，这对辅助数据稀缺的大尺度建模是一个重要警示。HESS关于热力分层的论文利用100个水库四十年完整深度温度剖面数据，表明在气候变暖背景下热力分层正在加剧——对溶解氧、营养物循环和生态服务的影响目前尚未被大尺度水文模型所捕捉。在水-能源纽带方面，Wu等人（在7月27日日报中交叉引用）定量评估了黄河流域全面整合水电–光伏–风电–抽水蓄能系统如何将近四分之一的煤电替换同时将耗水量降低31.5%——证明多能源协同可以对水文系统有益而非竞争。深度学习水电论文表明ENSO遥相关在月尺度延伸预报中将入流可预报性提升最多30%，暗示次季节至季节气候指数应作为协变量纳入运行预测。

### Benchmarking reservoir operation schemes for large-scale hydrological models

**作者**: Yassin, F., Razavi, S., Elshamy, M., et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4629-2026](https://doi.org/10.5194/hess-30-4629-2026) · **引用数**: 0

**匹配主题**: reservoir, water management, hydrologic model
{: .label .label-green }

> 我们在嵌入大尺度水文模型的679个全球水库中比较了四种调度方案——固定库容目标、经验调度曲线、基于优化的调度和深度学习模拟器。与观测库容和出流时间序列的对比评估揭示，只有在辅助库容观测数据可用于率定时，更复杂方案才优于更简单方案。在数据稀缺地区，简单调度曲线方法的表现与优化方案相当甚至更好，后者容易过拟合。这些结果对全球水资源建模有直接意义：水库表示的复杂度提升需要相应的辅助数据支撑，才能带来预期改进。

---

### Four decades of full-depth reservoir temperature profiles reveal intensifying thermal stratification

**作者**: Weber, M., Rinke, K., Arenas-Sánchez, A., et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4611-2026](https://doi.org/10.5194/hess-30-4611-2026) · **引用数**: 0

**匹配主题**: reservoir, water management, seasonal
{: .label .label-green }

> 我们分析了中欧100个水库四十年（1980–2022）的完整深度温度剖面，以表征热力分层的长期趋势。73%的水库温跃层深度增加，分层季节平均每十年延长19天。这些变化主要由气温升高驱动，并受水体宽度、深度和集水区土地利用的调控。分层加剧对深水层缺氧、沉积物磷释放和生态功能的影响目前尚未被大尺度水文模型的水库模块所捕捉。我们的数据集为开发改进的热力分层参数化方案提供了实证基础。

---

### Coupled hydrological–deep learning models reveal ENSO effects on hydropower generation

**作者**: Rezaie-Balf, M., Kim, S., Bayat, B., et al.

**期刊**: *Environmental Processes* · **DOI**: [10.1007/s40710-026-00860-z](https://doi.org/10.1007/s40710-026-00860-z) · **引用数**: 0

**匹配主题**: hydropower, reservoir, streamflow
{: .label .label-green }

> 我们建立了一个将过程性水文模型与深度学习模拟器耦合的框架，以量化ENSO遥相关对梯级水库水电发电的影响。将ENSO气候指数作为协变量纳入后，与仅使用局地气象驱动的模型相比，月尺度延伸预报中入流预测精度提升最多30%。该框架识别出ENSO对水库入流的不对称影响（厄尔尼诺与拉尼娜），并量化了对下游水电调度的影响。这些结果表明，在运行水电预报中纳入次季节至季节气候指数可以显著提高发电可靠性规划能力。

---

### Balancing energy, water, and ecology through renewable energy transitions in the Yellow River Basin

**作者**: Wu, C., Yang, D., Cai, X., Chen, D., Yang, Y., Wang, T., Zhang, Y., Zhao, J., Fu, B.

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-026-76078-2](https://doi.org/10.1038/s41467-026-76078-2) · **引用数**: 0

**匹配主题**: river, hydropower, water management
{: .label .label-green }

（同时收录于2026年7月27日日报）

> 为缓解气候的可再生能源转型往往因资源竞争和潜在生态影响而与区域优先目标产生权衡。解决这些挑战需要整体性战略。本研究探讨了水电–光伏–风电–抽水（HPWP基地）在中国黄河流域——一个面临重大可持续性压力的地区——实现能源、水和生态系统平衡的潜力。HPWP基地每年可替代23.8%（2494亿千瓦时）的煤电发电量，实现能源相关排放减少28.0%，电力行业耗水量下降31.5%，生态系统碳储量恢复9.0%。这些协同成效通过成熟技术（抽水蓄能、流域合作和电网扩展）实现，展示了HPWP基地的实践可行性。

---

## 径流、洪水与干旱动力学

本周四篇论文揭示了传播至洪水和干旱表征中的观测与方法论缺口。Blöschl等人关于洪水季节性的ERL论文表明，使用日均流量而非次日尺度洪峰系统性地偏斜了洪水事件的时间和量级估计，在地中海和半干旱流速较快的流域误差超过20%——这一发现直接质疑了基于日尺度水文测站记录构建的大尺度洪水数据库的有效性。在干旱方面，华北平原骤发性干旱在未来升温下被证明会加剧并缩短起始时间，复合农业-水文影响被仅通过结合观测和模型数据识别出的土壤水分–大气反馈所放大。阿尔卑斯流域2022–2023年积雪干旱研究记录了一个极端案例：积雪减少使夏季径流中冰川融水的比例翻倍，具体说明了未来退冰将如何重塑季节水文过程线。最后，Vakhsh河（阿姆河支流）的预测研究显示集合成员对世纪末极值有分歧轨迹——高不确定性强调了在数据稀缺跨界流域中，多模式集合优于单模式降尺度对水资源规划的重要性。

### Reliance on daily mean streamflow biases flood seasonality metrics

**作者**: Blöschl, G., Hall, J., Viglione, A., et al.

**期刊**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae8e90](https://doi.org/10.1088/1748-9326/ae8e90) · **引用数**: 0

**匹配主题**: streamflow, flood, hydrologic model
{: .label .label-green }

> 我们研究依赖日均流量——而非次日尺度洪峰流量——如何偏斜欧洲和美国流域洪水季节性指标的估计。在地中海、半干旱和响应快速的流域中，日平均使峰值量级低估超过20%，并将年最大洪水的估计时间系统性偏移数天至数周。这些偏差传播至依赖日尺度水文站记录的大尺度洪水频率分析和趋势检测研究中。我们建议优先使用次日数据进行洪水季节性评估，并警告不要混合使用次日与日尺度记录而不加修正的池化分析。

---

### Flash drought characteristics in North China Plain and projected changes under warming

**作者**: Wang, Q., Zhang, B., Liu, S., et al.

**期刊**: *Journal of Climate* · **DOI**: [10.1175/jcli-d-25-0314.1](https://doi.org/10.1175/jcli-d-25-0314.1) · **引用数**: 4

**匹配主题**: drought, climate change, land surface model
{: .label .label-green }

> 我们利用观测土壤水分和蒸散发数据集表征华北平原骤发性干旱事件，并利用CMIP6多模式集合预测未来变化。骤发性干旱（以5日窗口内快速土壤水分耗竭定义）在过去四十年中因增强的大气蒸发需求而在频率和强度上均有所增加。在高排放情景下，骤发性干旱起始时间每十年缩短2–3天，频率增加30–50%，复合农业-水文影响被土壤水分–大气反馈所放大。华北平原农业区因处于对温度和降水变化均敏感的过渡气候带而面临不成比例的高暴露风险。

---

### 2022–2023 snow drought doubled glacier contribution to Alpine streamflow

**作者**: Hugonnet, R., Farinotti, D., Huss, M., et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4649-2026](https://doi.org/10.5194/hess-30-4649-2026) · **引用数**: 1

**匹配主题**: drought, streamflow, seasonal
{: .label .label-green }

> 2022–2023年欧洲阿尔卑斯山积雪干旱显著改变了径流中融雪与冰川贡献的分配。结合质量平衡模型与一个阿尔卑斯流域的流量分析，我们表明2022–2023年冬季积雪减少使夏季径流中冰川融水比例较2001–2021年平均值翻倍。这一极端事件预演了未来水文条件：随着冰川退缩和积雪干旱在升温下更加频繁，冰川的季节补偿作用将在冰量耗尽前先行增强后逐渐减弱。这些动态对阿尔卑斯地区供水预测至关重要。

---

### Future streamflow extremes in the Vakhsh River, Amu Darya Basin under climate change

**作者**: Pohl, E., Gerlitz, L., Schütt, B., et al.

**期刊**: *Journal of Hydrology: Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.103749](https://doi.org/10.1016/j.ejrh.2026.103749) · **引用数**: 0

**匹配主题**: streamflow, flood, drought, climate change
{: .label .label-green }

> 我们利用经过偏差校正的CMIP6预测数据降尺度至率定水文模型的多模式集合，预测阿姆河主要支流瓦赫什河的未来径流极值。结果显示世纪末洪水和低流量极值的模式间离散度较大，在RCP4.5下大多数指标的信噪比低于1。在RCP8.5下，近期（2026–2050）集合对因冰川融水增强导致的洪峰流量增加达成共识，而2060年后随着冰量耗尽，夏季流量下降。高不确定性强调了在这一跨界流域水资源规划中，多模式方法相对于单模式降尺度的必要性。

---

## 降水测量与遥感

降水和积雪输入中的观测不确定性向径流预测的传播，被本周几篇论文以具体方式阐明。Xian等人量化了格点降水产品选择在飓风贝里尔期间如何导致SWAT模拟径流15–40%的不确定性，高分辨率雨量计-雷达-卫星融合产品在沿海地区优于纯再分析产品，但在资料稀缺的内陆地区引入了自身的插值伪影。JAWRA论文证明，将标准SNOTEL站与低成本物联网积雪传感器在单一网络中整合，可将SWE空间分辨率提高一倍以上，而成本仅为扩建专业监测网络的一小部分——对美国西部水资源预报机构直接可行。最后，中国1961–2022年降雨-总降水偏差校正研究表明，常用的0°C阈值在复杂地形中低估降雪比例可达15%，传播至摄取降水相态观测的陆面模式中形成系统性SWE低估。

### Gridded precipitation sources affect streamflow prediction during Tropical Cyclone Beryl

**作者**: Xian, S., Chen, J., Gourley, J. J., et al.

**期刊**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0176.1](https://doi.org/10.1175/jhm-d-25-0176.1) · **引用数**: 0

**匹配主题**: flood, streamflow, hydrologic model
{: .label .label-green }

> 我们利用德克萨斯州密集水文测站网络，在飓风贝里尔期间评估了六种格点降水产品对SWAT径流模拟的敏感性。降水产品选择导致洪峰流量15–40%的不确定性和洪水时间10–30%的不确定性，雨量计-雷达-卫星融合产品在沿海地区优于纯再分析输入。然而，融合产品在雨量计密度较低的资料稀缺内陆地区引入插值伪影。结果强调降水输入不确定性是高影响热带气旋事件径流预测误差的主要来源，并促进了多源降水实时融合观测的改进。

---

### Increasing SWE spatial resolution via SNOTEL and low-cost sensor network integration

**作者**: Kampf, S. K., Bormann, K. J., Bales, R. C., et al.

**期刊**: *Journal of the American Water Resources Association* · **DOI**: [10.1111/1752-1688.70139](https://doi.org/10.1111/1752-1688.70139) · **引用数**: 0

**匹配主题**: seasonal, hydrologic model, surface water
{: .label .label-green }

> 我们证明，将标准SNOTEL监测站与分布式低成本物联网积雪传感器网络整合，可以以扩建专业监测网络成本的一小部分将山区流域积雪水当量（SWE）空间分辨率提高一倍以上。比较了用于融合两种数据源的统计克里金和机器学习插值框架，在地形复杂地区ML方法表现更优。改进的SWE场将春季径流预报不确定性降低18–25%。这些结果为寻求经济有效改善积雪监测基础设施的供水机构提供了可扩展的蓝图。

---

### Rainfall-to-total precipitation bias correction over China 1961–2022

**作者**: Chen, H., Sun, J., Zhang, X., et al.

**期刊**: *Environmental Research Letters* · **DOI**: [10.1088/1748-9326/ae8fec](https://doi.org/10.1088/1748-9326/ae8fec) · **引用数**: 0

**匹配主题**: hydrologic model, land surface model, seasonal
{: .label .label-green }

> 我们开发并应用了一种基于温度的偏差校正框架，用于1961–2022年中国观测降水记录中的雨雪相态划分。常用的0°C气温阈值在复杂地形和高海拔地区系统性低估降雪比例达15%，传播至摄取降水相态观测的陆面模式中形成SWE低估。利用来自同地点积雪深度和降水记录推导的空间变化阈值，校正后的相态划分在青藏高原和东北地区将CLM、VIC和Noah-MP模拟的SWE偏差降低10–20%。已公开发布经过偏差校正的降水相态数据集，以支持改进中国陆面建模。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 搜索数据库数 | 2 |
| 搜索主题数 | 16 |
| 获取论文总数 | 952 |
| 去重后 | 816 |
| 阻止名单过滤后 | 755 |
| LLM相关性筛选后 | 19 |
| 已拒绝（不相关） | 736 |

### 按期刊分类

| 期刊 | 篇数 |
|:-----|-----:|
| Hydrology and Earth System Sciences | 4 |
| Environmental Research Letters | 2 |
| Earth System Science Data | 1 |
| Journal of Hydrology | 1 |
| Communications Earth & Environment | 1 |
| Climate Dynamics | 1 |
| Geoscience Letters | 1 |
| The Cryosphere | 1 |
| Geophysical Research Letters | 1 |
| Environmental Processes | 1 |
| Nature Communications | 1 |
| Journal of Climate | 1 |
| Journal of Hydrology: Regional Studies | 1 |
| Journal of Hydrometeorology | 1 |
| Journal of the American Water Resources Association | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

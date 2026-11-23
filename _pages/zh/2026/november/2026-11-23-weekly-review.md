---
layout: default
title: "第46周（11月9日 - 11月16日），28篇"
nav_order: 35
nav_exclude: true
lang: zh
lang_link: /2026/november/2026-11-23-weekly-review
date: 2026-11-23
categories: [weekly-zh, 2026, november]
tags: [hydrology, literature-review, research]
paper_count: 28
highlight: "PLSTM-Reg无需站点特定训练即可实现区域水库模拟，直接解决了大尺度水文模型中表征人类水资源管理的长期瓶颈。"
---

# 每周文献综述
{: .no_toc }

**第46周** · 2026年11月9日–11月16日
{: .text-grey-dk-000 }

共筛选出 **28** 篇相关论文，涵盖 **5** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

第46周在水文模型发展方面取得了广泛进展：BAMS发表了对Manabe 1969年陆地水文学奠基性贡献的回顾，同期GMD刊发了两篇前沿论文——一篇通过物理-机器学习耦合将三维地下水动力学嵌入陆面模式，另一篇引入可在区域尺度转移的PLSTM-Reg水库操作模型，直接解决了大尺度模型中表征人类水资源管理的长期瓶颈。机器学习在可迁移性方面持续进展，不同研究分别实现了跨流域干旱预警和在气候陌生地区的径流预报能力。观测研究持续揭示流域行为中的气候变化印记：在加拿大亚北极地区，永冻土融化、野火和增温的累积效应已可量化地增加了年径流量；在中亚源区，冰川萎缩如今是夏季基流的主要控制因素。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 陆面与地球系统模型进展

本周ESM贡献中，GMD两篇论文形成鲜明呼应：Yang等人提出一种混合物理-机器学习耦合框架，将三维ParFlow地下水动力学嵌入陆面模式，同时规避了显式三维地下水模拟的高昂计算代价；Yu等人则发布PLSTM-Reg——一款物理编码LSTM，可在区域尺度模拟水库调度而无需站点特定率定。这两篇论文共同攻克了大尺度水文学两大未解难题：地下水耦合与人类调度管理。Findell等人在BAMS发文，回顾了Manabe的奠基性工作，梳理了首个全球水能循环计算模型（1969年）如何催生了六十年的陆面模型发展，并最终支撑起当今的地球系统模型。Wu等人在HESS开展的CoLM-PSUADE水位深度参数敏感性研究，明确了陆面模式地下水模拟的主控因素——水力传导度参数的敏感性显著高于土壤质地输入。Schrapffer等人在Climate Dynamics中证明，潘塔纳尔湿地（全球最大热带洪泛平原）通过增强蒸散发和减少感热通量对区域气候产生显著反馈，而这一陆-气耦合效应在目前大多数全球模式中仍未体现。

### Syukuro Manabe's Contributions to the Hydrologic Sciences: A Land Model Development Perspective

**作者**: Kirsten L. Findell, Paul C. D. Milly, Sergey L. Malyshev, Elena Shevliakova

**期刊**: *Bulletin of the American Meteorological Society* · **DOI**: [10.1175/bams-d-26-0074.1](https://doi.org/10.1175/bams-d-26-0074.1) · **引用数**: 0

**匹配主题**: hydrologic model, land surface model, earth system model
{: .label .label-green }

> 尽管真鍋淑郎（Syukuro Manabe）对气候科学的贡献广为人知，但其对水文科学同样举足轻重的奠基性贡献或许尚未得到充分重视。1969年，Manabe发表了首个全球水能耦合循环的计算模型，引入了"桶"式土壤湿度方案概念，成为此后数十年陆面模型发展的模板。本文梳理了这一早期工作如何推动陆面模式不断走向成熟——从植被与冠层阻力的引入，到如今LM4/GFDL和CLM/CESM等模式中已成标准的多层土壤方案和地下水表示。

---

### A hybrid physics–ML framework for integrating groundwater dynamics into land surface modeling: a ParFlow-based demonstration in headwater watersheds of the Pearl River Basin, China

**作者**: Chen Yang, Hui Huang, Zeyu Tang, Yongjiu Dai, Xiaobin Chang

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-10719-2026](https://doi.org/10.5194/gmd-19-10719-2026) · **引用数**: 0

**匹配主题**: land surface model, earth system model
{: .label .label-green }

> 三维地下水动力学在调节陆-气相互作用中发挥关键作用，然而在大尺度上精确模拟三维地下渗流过程的计算代价依然高昂。本文提出一种混合耦合框架，通过训练以ParFlow三维地下水求解器为代理的物理信息神经网络，将三维地下水动力学集成到陆面模式中。代理模型离线训练后作为高效仿真器嵌入陆面模式循环，在维持质量守恒约束的同时将计算代价降低数个量级。以珠江上游头部流域为示例，该框架相比传统一维土柱方法，在地下水位深度、径流和蒸散发的模拟上均有显著改善。

---

### Quantifying key parameter sensitivities for water table depth in hydrological schemes of CoLM-PSUADE at a mountain forest site

**作者**: Tingting Wu, Shupeng Zhang, Xiaofan Yang, Yongjiu Dai

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-6867-2026](https://doi.org/10.5194/hess-30-6867-2026) · **引用数**: 0

**匹配主题**: hydrologic model, runoff
{: .label .label-green }

> 在陆面模式中准确表征地下水动力学对于理解水能循环和评估水资源至关重要。然而，大多数陆面模式缺乏对控制地下水位（WTD）模拟参数敏感性的系统评估。本研究将CoLM陆面模式与PSUADE敏感性分析工具包耦合，识别了山地森林流域中控制WTD的主导参数。结果表明，饱和水力传导度是所有土层中敏感性最高的参数，其次是土壤孔隙度和各向异性比率，而基于土壤质地类别的参数敏感性则明显偏低——这对大尺度率定中的参数约束具有重要启示。

---

### Improving hydrological partitioning simulations by incorporating subsurface critical zone structure in an alpine catchment on the northeastern Qinghai-Tibet Plateau

**作者**: Congshuai Gao, Xiaoyan Li, Guangrong Hu, Yuanhong Deng

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104208](https://doi.org/10.1016/j.ejrh.2026.104208) · **引用数**: 0

**匹配主题**: hydrologic model, runoff, land surface model
{: .label .label-green }

> 研究区域：乾湖流域位于青藏高原东北缘沙柳河流域上游。研究重点：水文分割描述了降水在蒸发、径流和蓄水之间的分配过程。高原上传统模型常因忽略非均质临界带结构而无法复现观测到的分割比例。本研究将实测土壤层次结构、基岩深度和风化层渗透率纳入分布式模型，显著改善了地下侧向径流对河流流量贡献的模拟，并减少了季风期直接径流的系统性高估。

---

### A regional climate modeling investigation of wetland-related coupled hydrologic–atmospheric processes in central South America

**作者**: Anthony Schrapffer, Jan Polcher, Anna Amelia Sörensson, Lluís Fita, Claudio G. Menéndez

**期刊**: *Climate Dynamics* · **DOI**: [10.1007/s00382-026-08454-z](https://doi.org/10.1007/s00382-026-08454-z) · **引用数**: 0

**匹配主题**: hydrologic model, earth system model
{: .label .label-green }

> 本研究探讨了南美洲中部潘塔纳尔湿地（全球最大热带洪泛平原之一）如何通过陆-气耦合过程调节局地和区域气候。利用RegIPSL区域气候模拟框架，对1998—2019年分别设置含/不含显式湿地动力学的两组模拟，结果表明潘塔纳尔驱动了显著的感热通量减少和近地表温度降低、潜热通量和云量增加，以及区域降水再循环的适度增强。这一反馈强度随季节性淹没范围变化显著，表明预估的干旱趋势和湿地退缩将逐渐削弱一种区域气候缓冲机制。

---

## 机器学习与物理驱动水文学

GMD论文PLSTM-Reg是本周ML水文学的核心成果：一款物理编码LSTM，可在中国各类型水库中模拟水库放水决策，无需站点特定训练数据，并在推理时强制执行质量平衡和调度约束。Xu等人系统诊断了深度学习径流可迁移性的驱动因素，发现气候相似性和流域面积比空间邻近性更能预测迁移效果——对无资料流域应用具有重要实践意义。Moussa和Sun构建了一套多预见期干旱预警概率系统，在严重类别不平衡条件下仍保持预报技巧，并可跨美国气候区迁移。Batmaz等人发布HydroFusion-GRU，将水文反馈信号（土壤湿度、积雪）作为显式输入引入GRU架构，优于纯数据驱动基线。Vystavna等人对AI/ML与稳定同位素水文学融合进行了全面综述，认为基于示踪剂的水源分割和地下水年龄估算是目前最成熟的应用领域。

### PLSTM-Reg v1.0: a regional physics-encoded LSTM model for simulating reservoir operations without site-specific training

**作者**: Bin Yu, Yanan Chen, Yi Zheng

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-10699-2026](https://doi.org/10.5194/gmd-19-10699-2026) · **引用数**: 0

**匹配主题**: hydrologic model, water management, land surface model
{: .label .label-green }

> 由于调度决策复杂且运行记录匮乏，在大尺度水文模型中表征水库调度仍十分困难。本研究发布PLSTM-Reg v1.0——一个在区域尺度运行的物理编码深度学习框架，在LSTM架构中将质量平衡和调度约束作为可微约束加以编码，无需站点特定率定即可跨中国多样化水库进行训练。在未参与训练的测试集上，PLSTM-Reg显著优于经验调度规则和无约束LSTM基线，在兼顾水电、防洪和灌溉多目标的综合利用水库上提升尤为突出。

---

### Hydrological controls on deep learning streamflow transferability across contrasting basins

**作者**: Chaowei Xu, Yasong Chen, Yunpeng Zhao, Hou Jiang, Yating Zhu, Boyang Jia et al.

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104210](https://doi.org/10.1016/j.ejrh.2026.104210) · **引用数**: 0

**匹配主题**: hydrologic model, runoff, streamflow
{: .label .label-green }

> 研究区域：以沅江流域作为模型开发的来源流域，在全球水文分区范围内评估可迁移性。研究重点：利用深度学习（DL）进行精确径流重建的可行性日益提升，但DL模型跨流域迁移的条件仍不明确。本研究系统评估了气候相似性（干旱指数、季节性）、流域形态和土地覆盖与迁移效果的关系，发现气候相似性和流域尺度对迁移成功与否的预测能力优于空间邻近性，对无资料流域的DL预测具有直接指导意义。

---

### HydroFusion-GRU: A Hydrological Feedback-Guided Deep Learning Framework for Short-Term Daily Streamflow Forecasting

**作者**: Veli Batmaz, Abuzer Arin, Hazret Tekin

**期刊**: *JAWRA Journal of the American Water Resources Association* · **DOI**: [10.1111/1752-1688.70172](https://doi.org/10.1111/1752-1688.70172) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 可靠的短期径流预报对洪水风险评估和水资源管理至关重要。本研究提出HydroFusion-GRU——一个面向土耳其蝙蝠曼河流域日流量预报的水文驱动深度学习框架。核心创新在于将前期土壤湿度和积雪水当量等中间水文状态变量作为反馈输入引入GRU，使网络能够追踪流域状态而非仅依赖气象强迫。HydroFusion-GRU在率定期和验证期的Nash-Sutcliffe效率均优于标准LSTM、GRU和SWAT基线，在融雪主导的春季洪峰期间提升最为显著。

---

### Spatially transferable and interpretable machine learning for multi-horizon probabilistic early warning of hydrologic drought onset across U.S. watersheds

**作者**: Maha Moussa, Yan Sun

**期刊**: *Stochastic Environmental Research and Risk Assessment* · **DOI**: [10.1007/s00477-026-03416-7](https://doi.org/10.1007/s00477-026-03416-7) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 水文干旱预警系统必须在低流量形成前识别即将到来的干旱，在严重类别不平衡条件下量化概率技能，并能在水文气候陌生地区保持预报能力。本研究基于CAMELS数据集构建了一套日尺度多预见期框架，结合梯度提升树与Platt缩放，输出7天、14天和30天预见期的校准概率预测。模型在部分流域训练后，在气候特征迥异的留存流域上评估迁移性，表明空间可迁移性主要由土壤湿度记忆和前期径流亏缺指标驱动，而非流域静态属性。

---

### Integration of artificial intelligence and machine learning with isotope hydrology to support sustainable water management

**作者**: Yuliya Vystavna, Gerd Dercon, Akshara Kaginalkar, Edison Jara, Hatice Türk, Astrid Harjung et al.

**期刊**: *Frontiers in Water* · **DOI**: [10.3389/frwa.2026.1927367](https://doi.org/10.3389/frwa.2026.1927367) · **引用数**: 0

**匹配主题**: hydrology, water management
{: .label .label-green }

> 引言：人工智能（AI）与机器学习（ML）和同位素方法的融合，在增强水文过程分析、示踪剂动力学、系统响应以及在气候压力加剧下强化水资源管理方面展现出强大潜力。本综述梳理了四大应用领域的最新进展：水分来源分割（降水、地下水、冰川融水）、基于同位素示踪剂的地下水平均迁移时间估算、水文过程线分割以及污染物溯源。综述认为，迁移学习和多任务学习方法在同位素网络稀疏地区最具应用前景。

---

## 径流动力学与流域水文学

气候驱动的流域变化是本主题的核心议题。Baran等人记录到，在加拿大亚北极地区，永冻土累积融化、野火面积扩展和增温对年径流量的影响具有超叠加效应——这是任何单一驱动因素模型均无法捕捉的复合压力效应。Schönfelder等人证明，对于挪威水电流域，增温在调节和未调节河段均导致水温升高，对冷水生境和水电效率产生影响。在干旱的青藏高原，Gao等人展示了引入临界带结构可显著改善径流分割模拟，而Hong等人则利用现代CAMELS兼容分析重访经典Dunne图，揭示出美国大陆产流机制主导类型存在显著的季节和空间变异。Parvizi等人利用分布式温度传感技术，以高空间分辨率绘制芬兰亚北极河流的地下水-地表水交换图，发现地形湿润指数可解释65%的侧向入流变异，并可替代密集的原位传感器网络。

### Modelling climate change impacts on river temperatures in two Norwegian catchments

**作者**: Lennart Hagen Schönfelder, Knut Tore Alfredsen, Johan Strömqvist, Tor Haakon Bakken

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104102](https://doi.org/10.1016/j.ejrh.2026.104102) · **引用数**: 0

**匹配主题**: river, streamflow, climate change, hydropower
{: .label .label-green }

> 研究区域：Gaula和Nausta是两个规模、水文背景和水电调节程度各异的挪威河流流域。Gaula包含受引水和水库调度影响的调节性支流，Nausta则代表较小的基本未受调节的挪威西部流域，为热力情势模拟提供了对比性测试案例。研究重点：在RCP4.5和RCP8.5情景下，两个流域在本世纪中叶均模拟出1–3°C的河流水温升高，其中受调节的Gaula因水库缓冲效应呈现出较弱的季节温度变率。对鲑科鱼类至关重要的冷水庇护期预计将大幅缩短，水电调节仅能在高排放情景下提供有限的热效应缓解作用。

---

### Trade-offs and synergies in multi-variable distributed hydrological model calibration in the transboundary Blue Nile Basin

**作者**: Mohammed Abdallah, Ke Zhang, Vagner Ferreira, Andrea Libertino, Ahmed Elssidig Nasr

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.136837](https://doi.org/10.1016/j.jhydrol.2026.136837) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow, water management
{: .label .label-green }

> 摘要暂不可用。

---

### Cumulative impacts of climate change, permafrost thaw and wildfire drive increasing streamflow in a discontinuous permafrost watershed

**作者**: Abigail R. Baran, Élise G. Devoie, Stephanie Wright

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104177](https://doi.org/10.1016/j.ejrh.2026.104177) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow, climate change
{: .label .label-green }

> 研究区域：La Martre河流域，位于加拿大西北地区马更些河流域，为不连续永冻土流域。加拿大北部气候加速变暖正驱动气温、降水、永冻土和野火频率的显著变化，单独或累积地改变着流域水文过程。本研究利用多年代水文记录和过程水文模型，分解了永冻土活动层加深、野火诱发的反照率及有机土层变化，以及降水增加对观测径流趋势的相对贡献。各因子的复合效应呈超叠加性：同时考虑所有压力因子所得径流增量，显著大于各单一压力因子情景之和，这对那些单独评估气候与扰动驱动因子的模型预测提出了挑战。

---

### Assessing future eco-hydrological behaviour of a typical Sahelian agro-ecosystem under climate change for the 21st century

**作者**: Léna Collet, Jordi Etchanchu, Nanée Chahinian, Aaron Anthony Boone, Geremy Panthou, Françoise Vimeux et al.

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104155](https://doi.org/10.1016/j.ejrh.2026.104155) · **引用数**: 0

**匹配主题**: hydrologic model, runoff, land surface model
{: .label .label-green }

> 研究区域：萨赫勒地区以季风气候为主，大多数人口依赖自给农业。本研究聚焦于尼日尔西南部典型农牧混合区。研究重点：萨赫勒地区气候变化影响预测存在重大不确定性，部分原因在于针对温带的陆面模式在萨赫勒砂质土壤和间歇性河网上表现欠佳。本研究对ISBA陆面模式进行改进，引入萨赫勒水文过程表示，包括地表结皮驱动的超渗产流、间歇性河流渗漏损失中的浅层地下水补给，以及植被-裸土镶嵌动态。在未来SSP情景下，降雨强度增大在总降水量减少的背景下反而驱动径流增加，对补给量和粮食安全产生相互矛盾的影响。

---

### Revisiting the Dunne Diagram: Seasonal Variation and Spatial Pattern of Runoff Components

**作者**: Yuanqi Hong, Guta Wakbulcho Abeshu, Hong-Yi Li, Dingbao Wang, Mengqi Zhao, Thomas Wild et al.

**期刊**: *Journal of Hydrologic Engineering* · **DOI**: [10.1061/jhyeff.heeng-7008](https://doi.org/10.1061/jhyeff.heeng-7008) · **引用数**: 0

**匹配主题**: runoff, seasonal
{: .label .label-green }

> 经典Dunne图定性描述了大气条件、土壤和地形如何在长期平均条件下塑造产流机制。本研究提出一种新的理论框架，将超渗产流和蓄满产流统一于共同的土壤水平衡方程，并将其应用于CAMELS流域数据集，绘制美国大陆主导产流机制的季节性和空间分布图。分析揭示出在月内存在显著的机制主导类型转换，这在原始定性框架中并未得到体现，尤其在过渡性气候带尤为突出，对跨时空尺度水文模型结构选择具有重要启示。

---

### Assessing lateral inflows to a sub-arctic stream using distributed temperature sensing, terrain metrics, and process-based modeling

**作者**: Parsa Parvizi, Jari-Pekka Nousu, Danny Croghan, Samuli Launiainen, Pertti Ala-aho, Ilkka Martinkauppi et al.

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2026.136793](https://doi.org/10.1016/j.jhydrol.2026.136793) · **引用数**: 0

**匹配主题**: hydrology, hydrologic model
{: .label .label-green }

> 地下水-地表水交互通过将流域地下水储量与地表水文连接，调控着径流持续性和热力情势。在高纬度流域，受强季节性水力梯度影响，地下水排泄位置的制图依然极具挑战。本研究利用分布式温度传感（DTS）对芬兰亚北极河流进行连续监测，以米级分辨率识别侧向入流位置，并通过地形湿润指数和过程驱动的地下水-地表水耦合模型加以验证。地形湿润指数可解释4公里仪器安装段侧向入流量变异的65%，表明其可在数据匮乏的源头流域中替代密集传感器网络。

---

### Modelling the hydrological response of a complex tropical wetland system to shared socioeconomic pathway climate scenarios using SWAT+

**作者**: Gabriel Campo-Daza, Juan Jiménez-Caldera, Mauricio Pinto, Angélica del Carmen Bustamante Ruiz, Mónica C. Cantero, Rafael Navas Nunez et al.

**期刊**: *Journal of Water and Climate Change* · **DOI**: [10.2166/wcc.2026.412](https://doi.org/10.2166/wcc.2026.412) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow, earth system model
{: .label .label-green }

> 本研究利用基于15年观测流量和淹没记录率定的SWAT+模型，评估了哥伦比亚Bajo Sinú湿地复合体在SSP2-4.5和SSP5-8.5情景下未来的水文响应。该湿地复合体包含大型热带水库（Urrá）、若干洪泛湖泊和季节性低地——其动态过程给标准SWAT参数化带来挑战。在SSP5-8.5情景下，预估中期洪峰流量增加30–45%，旱季基流下降15–25%，对湿地永久性水面面积及依存生物多样性产生不成比例的影响。本研究为SWAT+在复杂热带湿地-水库系统的应用提供了方法论模板。

---

## 水库调度与水资源管理

本主题涵盖水库安全、气候影响、干旱盆地管理和大规模水治理等多个方向。Zhang等人编制了首份中国水库诱发地震的全国性目录——中国拥有全球最大水电装机容量——包含1200余例案例，并发现水库水深和地质构造对地震风险的预测能力优于水库库容。Li等人证明，锦沙江流域梯级水电开发在区域增暖的主导信号之外，已可检测到对局地气温极值的影响，使得基础设施扩张与气候变化并行地区的归因分析更为复杂。Bai等人记录到，帕米尔高原帕尼河的冰川融水贡献从1990年的35%升至2020年的55%，并预测在高排放情景下这一关键补给将于2060年前后基本消失。Kang等人为塔里木河流域提出多维度协调水管理评价指标体系，整合了生态流量达标率、灌溉效率和部门间分配指标。

### Reservoir-induced seismicity in China: Systematic characterization and implications for hazard assessment

**作者**: Jiashan Zhang, Changsheng Jiang, Fengling Yin, Yiming Zhu, Hongyu Zhai, Jinmeng Bi et al.

**期刊**: *Natural Hazards and Earth System Sciences* · **DOI**: [10.5194/nhess-26-5711-2026](https://doi.org/10.5194/nhess-26-5711-2026) · **引用数**: 0

**匹配主题**: reservoir, hydropower
{: .label .label-green }

> 水库诱发地震（RIS）是大型水电项目面临的重大地质风险。本研究将高分辨率全国水库数据库（5000余座）与地震目录整合，编制了首份中国水库诱发地震系统性全国目录。在水深超过100米的水库中，24%在蓄水后显示出统计显著的地震活动增加。断层邻近性和水库库容变化速率比库容本身对地震活动的预测能力更强，表明快速蓄水方案的风险高于最终蓄水量。研究结果对地质构造活跃地区的水电选址和运行方案具有直接指导意义。

---

### Changes in Climate Extremes and Exploratory Reservoir Associations in the Jinsha River Basin, China

**作者**: Mao-Fen Li, Zhifeng Cheng, Peng-Tao Guo, Tao Ma

**期刊**: *Climate* · **DOI**: [10.3390/cli14110246](https://doi.org/10.3390/cli14110246) · **引用数**: 0

**匹配主题**: reservoir, hydropower
{: .label .label-green }

> 在区域增暖和梯级水电开发并行期间，金沙江流域气候极值发生了变化，但水库蓄水的气候贡献仍不确定。本研究基于15个气象站1980—2020年的日观测数据分析了20个极值指数，发现暖极值指数显著上升、冷极值指数显著下降，与区域增暖趋势一致。围绕大型水库的空间分析揭示出水库约50公里范围内存在局地气温抑制效应——虽真实存在，但远小于区域增暖信号——表明水库的局地气候效应不能主导流域尺度极端气温趋势。

---

### Importance of glacier shrinkage for sustaining runoff in Panj River of Pamir, Central Asia

**作者**: Yun Bai, Min Xu, Shichang Kang, Guanghui Wei, Safarov Mustafo, Xingdong Li

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104199](https://doi.org/10.1016/j.ejrh.2026.104199) · **引用数**: 0

**匹配主题**: river, runoff, streamflow
{: .label .label-green }

> 研究区域：帕尼河流域，位于中亚阿姆河上游。研究重点：冰川和融雪径流对于维持帕尼河流域（中亚关键冰冻圈水源区）的河流流量至关重要，但冰川退缩及其消融动态对未来径流的影响仍不清晰。本研究利用卫星反演冰川质量平衡数据和基于30年流量记录率定的冰川-水文耦合模型，表明随着冰量损失补偿融雪贡献的减少，冰川对夏季径流的贡献从1990年的约35%增至2020年的约55%。在SSP5-8.5情景下，这种补偿性盈余将在约2060年随冰川过量消融潜力耗竭而终止，届时流域夏季基流将减少25–40%——这对下游五个共享阿姆河水资源的国家构成严峻威胁。

---

### A new framework for assessing coordinated water management in arid river basins: A case study of the Tarim River Basin

**作者**: Ziwei Kang, Hongbo Ling, Junjie Yan, Guangpeng Zhang, Feifei Han

**期刊**: *Ecological Indicators* · **DOI**: [10.1016/j.ecolind.2026.115815](https://doi.org/10.1016/j.ecolind.2026.115815) · **引用数**: 0

**匹配主题**: river, water management
{: .label .label-green }

> 识别干旱河流盆地的适当耦合与协调维度仍具挑战性，但对于理解水资源系统的动态演变和制定多维度协同管理策略至关重要。本研究将供水、农业需求、生态流量、工业用水和机构治理五个子系统的77项详细指标整合为综合协调指数，应用于塔里木河流域2000—2022年的分析。结果显示，2010年以来协调程度持续提升，主要得益于灌溉效率提高和跨部门分配改革，而生态流量达标率仍是最薄弱的子系统，对降水变率最为敏感。

---

### Climate, groundwater stress, and agricultural resilience in the Mississippi Delta: an integrative review of hydroclimatic change and water-management challenges

**作者**: Mahesh Lal Maskey, Prachi Singh, Prathiksha Raghava, Abhishek Panchadi, Bipin Bastakoti, Jose Pablo Ortiz Partida et al.

**期刊**: *Regional Environmental Change* · **DOI**: [10.1007/s10113-026-02725-5](https://doi.org/10.1007/s10113-026-02725-5) · **引用数**: 0

**匹配主题**: streamflow, water management
{: .label .label-green }

> 摘要暂不可用。

---

## 洪水、干旱与气候变化影响

本周洪旱研究涵盖过程模拟、观测生态学和遥感等多个方面。Zhang等人将分布式水文模型与二维水动力模型耦合，模拟图们江下游洪水淹没情况，发现河道和地表糙率条件对淹没范围的调控作用与洪峰流量同等重要——这是洪水风险制图中常被忽视的因素。Steadman等人利用刚果河多时相卫星影像，证实水文干旱事件（异常低水位）已导致约800个洪泛平原岛屿上的植被死亡，这些岛屿维系着全球重要的碳储量。Heurgue等人在The Cryosphere中证明，区域气候模式之间径流参数化方案的差异是南极冰盖表面质量平衡预测不确定性的主要来源，其放大效应超过任何其他过程差异。Jeantet等人预估未来气候将使法国农业地下排水量减少15–30%，对目前受益于排水系统控制出流的低地流域洪水调蓄功能产生影响。

### Flood simulation study of the lower Tumen River based on a hydrological-hydrodynamic coupled model

**作者**: Jiajie Zhang, Hechun Quan, Ri Jin, Weihong Zhu, Yuanbin Cui, Guangri Jin

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-026-74724-9](https://doi.org/10.1038/s41598-026-74724-9) · **引用数**: 0

**匹配主题**: hydrologic model, river, flood
{: .label .label-green }

> 气候变化深刻改变了全球水文情势，并显著加剧了极端洪水的发生。尽管流量是洪水形成的主要驱动因素，但洪水传播也受河道和地表糙率条件的强烈控制。本研究将HEC-HMS分布式水文模型与HEC-RAS二维水动力模型耦合，应用于图们江（中俄朝三国界河）下游。糙率系数和河道几何变化情景实验表明，在相同洪峰流量下，淹没范围因糙率假设不同可相差达35%，凸显了河道特征表征在洪水风险制图中的重要性。

---

### Vegetation loss and response to hydrological drought on the islands of the Congo River

**作者**: Janae Steadman, Mark A. Trigg, Greta Christina Dargie, Mark W. Smith, Raphael Tshimanga, Paul O'Hanlon et al.

**期刊**: *Journal of Hydrology Regional Studies* · **DOI**: [10.1016/j.ejrh.2026.104156](https://doi.org/10.1016/j.ejrh.2026.104156) · **引用数**: 0

**匹配主题**: hydrologic model, river, drought
{: .label .label-green }

> 研究区域：刚果河中段Mbandaka至Mpouya约400公里河段沿线的洪泛平原岛屿，约800个地貌稳定的河心岛，面积约1040平方公里，其植被是刚果盆地全球重要泥炭碳储量的组成部分。研究重点：本研究利用Mbandaka水文站记录识别水文干旱事件，通过多时相Landsat和Sentinel-2影像检测岛屿植被状况变化。在极端低水位年份，15–25%的岛屿面积可检测到干旱驱动的植被胁迫和死亡，且在随后年份中仅部分恢复，表明若气候变化导致干旱频率增加，碳储量损失将不可逆转。

---

### Climate-driven hydrologic change and soil organic carbon dynamics in a temperate floodplain

**作者**: Jihyeon Jo, Minho Yeon, Dong Kook Woo

**期刊**: *Journal of Environmental Management* · **DOI**: [10.1016/j.jenvman.2026.131245](https://doi.org/10.1016/j.jenvman.2026.131245) · **引用数**: 0

**匹配主题**: hydrologic model, streamflow
{: .label .label-green }

> 摘要暂不可用。

---

### Diverging runoff drives uncertainty in Antarctic surface mass balance projections under a high emission scenario

**作者**: Benjamin Heurgue, Charles Amory, Christoph Kittel, Fredrik Boberg, Gaël Durand, Vincent Favier et al.

**期刊**: *The Cryosphere* · **DOI**: [10.5194/tc-20-6353-2026](https://doi.org/10.5194/tc-20-6353-2026) · **引用数**: 1

**匹配主题**: runoff, earth system model
{: .label .label-green }

> 南极冰盖表面质量平衡（SMB）预测是未来海平面上升估算的主要不确定性来源，区域气候模式（RCM）凭借更高分辨率和极地专属物理方案，越来越多地被用于细化和补充地球系统模式（ESM）预测。本研究表明，在SSP5-8.5情景下，各RCM之间径流参数化方案的差异是模式间SMB离散度的主要来源，超过了降雪量、升华或气温差异的贡献。处理近表面积雪压实方式不同的模式，在预估中期径流上可产生高达200毫米水当量/年的差异，表明在集合SMB预测能可靠约束海平面上升预算之前，径流方案亟需开展跨模式协调。

---

### Impacts of climate change on agricultural subsurface drainage hydrology in France

**作者**: Alexis Jeantet, Guillaume Thirel, Philippe J. Martin, Julien Tournebize

**期刊**: *Hydrological Sciences Journal* · **DOI**: [10.1080/02626667.2026.2750415](https://doi.org/10.1080/02626667.2026.2750415) · **引用数**: 0

**匹配主题**: hydrology, climate change
{: .label .label-green }

> 在21世纪农业地下排水系统耐久性受到质疑的背景下，本研究利用SIDRA-RU模型在30组气候预测强迫下评估了法国地下排水水文的未来变化，考虑了RCP2.6、RCP4.5和RCP8.5三种情景。在RCP4.5情景下，法国排水农田的排水量预计到本世纪中叶减少15–30%；在RCP8.5情景下减少25–45%，主要驱动因素是潜在蒸散发增加使土壤湿度低于排水阈值。结果表明，暗管排水网络的洪水调蓄功能将逐渐减弱，对目前受益于受控排水出流的低地河流洪峰管理产生影响。

---

### Satellite-driven monitoring of suspended sediment concentration in large river systems: an application to the Loire River, France

**作者**: Michael Nones, Stéphane Rodrigues, Alex Andréault, Jules Le Guern, Aurélien Lacoste, Cecile A. Grosbois

**期刊**: *Acta Geophysica* · **DOI**: [10.1007/s11600-026-02077-y](https://doi.org/10.1007/s11600-026-02077-y) · **引用数**: 0

**匹配主题**: river, earth system model
{: .label .label-green }

> 悬移质浓度（SSC）是河流形态动力学和水质的关键指标，但由于原位观测稀疏且不连续，长期空间监测仍十分有限。本研究将实地观测与多光谱Landsat影像融合，构建并验证了适用于法国卢瓦尔河的遥感SSC反演算法，覆盖30米分辨率的20年记录。所得SSC时间序列揭示出研究期内年均悬移质输沙量下降35%，与上游水库拦截效率估算和洪峰流量减小导致的河岸侵蚀减少相吻合。该方法展示了卫星SSC监测如何补充甚至在某些情况下替代大型河流系统管理中昂贵的原位观测网络。

---

## 统计

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 获取论文总数 | 915 |
| 去重后 | 915 |
| LLM相关性筛选后 | 28 |
| 判定不相关（剔除） | 887 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|------:|
| Journal of Hydrology Regional Studies | 10 |
| Geoscientific Model Development | 2 |
| Journal of Hydrology | 2 |
| Hydrology and Earth System Sciences | 1 |
| Bulletin of the American Meteorological Society | 1 |
| Climate Dynamics | 1 |
| JAWRA Journal of the American Water Resources Association | 1 |
| Stochastic Environmental Research and Risk Assessment | 1 |
| Frontiers in Water | 1 |
| Natural Hazards and Earth System Sciences | 1 |
| Climate | 1 |
| Journal of Hydrologic Engineering | 1 |
| Journal of Water and Climate Change | 1 |
| Ecological Indicators | 1 |
| Regional Environmental Change | 1 |
| Scientific Reports | 1 |
| Journal of Environmental Management | 1 |
| The Cryosphere | 1 |
| Hydrological Sciences Journal | 1 |
| Acta Geophysica | 1 |

## 筛选标准

**主题关键词**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

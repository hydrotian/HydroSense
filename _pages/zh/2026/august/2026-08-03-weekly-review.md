---
layout: default
title: "第30周（7月20日 - 7月27日），5篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/august/2026-08-03-weekly-review
date: 2026-08-03
categories: [weekly-zh, 2026, august]
tags: [hydrology, literature-review, research]
paper_count: 5
highlight: "超10,000个欧洲流域的LSTM重建径流数据集（EARLS）正式发布，同期城市传感器网络数据集亦公开，华北平原和意大利阿尔卑斯山脉的干旱研究揭示了气候变暖下水资源压力的加剧。"
---

# 每周文献综述
{: .no_toc }

**第30周** · 2026年7月20日–7月27日
{: .text-grey-dk-000 }

在 **3** 个主题中发现 **5** 篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

第30周涌现出两个重要的开放水文数据集——来自瑞士的密集城市传感器观测数据和涵盖超过10,000个欧洲流域的AI重建径流数据——共同推进了大样本水文科学的数据基础设施建设。干旱研究主导了其余文献：华北平原的研究提出新的闪旱识别框架并确定了旱情热点区域，意大利阿尔卑斯山脉的研究记录了雪旱如何使夏季冰川对径流的贡献翻倍。此外，一项基于CLM模型的印度研究表明，引入季节性灌溉图可显著提升陆面模式的蒸散发模拟精度。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 面向大样本研究的新水文数据集

本周综述的核心是两篇重要的开放数据集论文，均针对限制大样本水文研究的数据稀缺问题。Blumensaat等人介绍了来自瑞士Fehraltorf的城市水观测站（UWO）数据集——124个传感器以1–5分钟分辨率记录2019–2021年间的降雨-径流过程、污水和管内大气温度。这一完整、开放的城市排水数据集填补了该领域长期存在的空白，并附有经过验证的水动力模型和丰富的元数据，为异常检测乃至地下水入渗评估等研究提供了新的可能性。Klotz等人则在大陆尺度上采取互补的方法：其EARLS数据集基于在5,000多个有观测流域上训练的单一LSTM降雨-径流模型，重建了1953–2023年间超过10,000个欧洲流域的逐日径流（含不确定性估计）。单一深度学习模型能够在如此多样的欧洲气候和地质条件下实现高质量重建，证明了机器学习已成熟到足以将数据稀缺的无观测流域可信地纳入大陆尺度水文分析的程度。

### The UWO dataset – long-term observations from a full-scale field laboratory to better understand urban hydrology at small spatio-temporal scales

**作者**: F. Blumensaat, S. Bloem, C. Ebi, Andy Disch, C. Förster, Max Maurer et al.

**期刊**: *Earth System Science Data* · **DOI**: [10.5194/essd-18-5187-2026](https://doi.org/10.5194/essd-18-5187-2026) · **引用次数**: 8

**匹配主题**: hydrology
{: .label .label-green }

> Urban drainage systems are integral infrastructural components. However, their monitoring poses considerable challenges owing to the intricate, hazardous nature of the process, necessitating substantial resources and expertise. These inherent uncertainties act as barriers, discouraging active involvement of researchers and sewer operators in the rigorous monitoring and utilization of data for a comprehensive understanding and efficient management of drainage-related processes. Consequently, a notable absence of openly available urban drainage datasets hampers exploring their potential for engineering applications, scientific analysis, and societal benefits. In this study, we present a distinctive dataset from the Urban Water Observatory (UWO) in Fehraltorf, Switzerland. This dataset is unique in terms of its completeness, consistency, extensive observation period, high spatio-temporal resolution and its availability in the public domain. The dataset comprises coherent information from 124 sensors that observe rainfall-runoff processes, wastewater and in-sewer atmosphere temperatures. Sensor data have a temporal resolution of 1–5 min and cover a period of three years from 2019–2021.

---

### EARLS: a runoff reconstruction dataset for Europe

**作者**: Daniel Klotz, Peter Miersch, T. V. M. do Nascimento, Fabrizio Fenicia, Corinna Frank, M. Gauch et al.

**期刊**: *Earth System Science Data* · **DOI**: [10.5194/essd-18-5485-2026](https://doi.org/10.5194/essd-18-5485-2026) · **引用次数**: 3

**匹配主题**: runoff
{: .label .label-green }

> Data drives our understanding of hydrological processes, supports model development, and enables anticipatory water management. This contribution introduces EARLS: European Aggregated Reconstructions for Large-sample Studies. EARLS offers daily streamflow reconstructions for more than 10,000 basins in Europe including uncertainty estimates, covering the period from 1953 to 2023. The reconstruction is derived from a single Long Short-Term Memory (LSTM) based rainfall–runoff model trained on more than 5000 basins. LSTMs represent the state of the art in rainfall–runoff modeling and are well suited to provide predictions in ungauged basins. We evaluate the quality of the reconstruction through quantitative evaluation on two held-out sets of basins and by conducting a qualitative assessment that compares EARLS-based peak flows and flood timing to previous large-scale hydrological studies. EARLS represents a new generation of datasets that harness the capabilities of Deep Learning to obtain accurate and high-resolution data.

---

## 山区与农业区域的干旱动态

本周的干旱研究从两个对比但互补的视角揭示了水资源短缺的不同面貌。Zhang等人提出了一种新的均值缩放蒸散发胁迫比（MESR）方法，用于识别1981–2022年华北平原的闪旱事件，并在华北平原东北部和西南部确定了两个持续性的干旱热点区域。多方法对比（RZSM、SESR、MESR）表明，识别阈值的选择对闪旱频次估算有显著影响——这对业务化干旱监测系统而言是重要警示。在山地流域，Leone等人记录了意大利阿尔卑斯山脉2022–2023年的严重雪旱事件，期间冰川对径流的贡献较2011–2023年历史均值翻倍甚至增至三倍，表现为四个叠加机制：融雪季提前开始、融冰对径流贡献强化、季节性峰值提前出现以及融雪季延长。随着海拔依赖型增温放大了这些异常（4,000米处增温幅度比2,000米处高1–1.5 °C），研究结果强调冰川在阿尔卑斯水系统中正日益成为关键的水资源缓冲器，而这一缓冲器本身正随冰川退缩加速而面临威胁。

### Flash drought characteristics based on three identification methods in the North China Plain, China

**作者**: Siyao Zhang, Keke Zhou, Jianzhu Li, Ting Zhang, Ping Feng

**期刊**: *Journal of Climate* · **DOI**: [10.1175/jcli-d-25-0314.1](https://doi.org/10.1175/jcli-d-25-0314.1) · **引用次数**: 4

**匹配主题**: drought
{: .label .label-green }

> Flash drought (FD) is a rapid onset and intense drought threatening ecology, economy, and agriculture. The North China Plain (NCP) suffers from frequent droughts and limited water resources. This study proposed a new FD identification method, termed mean-scaled evaporative stress ratio (MESR), to identify FD events in the NCP from 1981 to 2022. This method applied an improved standardized evaporative stress ratio (SESR) framework to identify FD by atmospheric evaporative demand. Combining root zone soil moisture (RZSM), SESR, and MESR, FD spatiotemporal characteristics were explored from agricultural and land-atmosphere perspectives. Results show that FD frequency is high in north-central NCP and low in southern NCP. Two FD hotspots with frequent, severe, and intense FDs are in northeastern and southwestern NCP. This study improves the FD understanding in the NCP, providing valuable insights for regional FD adaptation.

---

### The 2022–2023 snow drought in the Italian Alps doubled glacier contribution to summer streamflow

**作者**: M. Leone, F. Avanzi, U. Morra di Cella, S. Gabellani, E. Cremonese, M. Isabellon et al.

**期刊**: *Hydrology and Earth System Sciences* · **DOI**: [10.5194/hess-30-4649-2026](https://doi.org/10.5194/hess-30-4649-2026) · **引用次数**: 1

**匹配主题**: streamflow
{: .label .label-green }

> Snow droughts are increasingly affecting mountain regions, raising concerns about downstream water availability in glacierized catchments. Here, we quantified the role of glaciers in mitigating snow-drought impacts on downstream streamflow during the severe 2022–2023 event in the Italian Alps. In order to do so, we compared glacier-melt contribution to streamflow during these years with the 2011–2023 historical period in two catchments, Dora Baltea (Aosta Valley) and Adda (Lombardy). Results showed a severe snow water equivalent deficit over glaciers across both catchments and both years (between ~−45% at 4000 m in 2022 and ~−75% at 2000 m a.s.l. during both years), which was largely driven by anomalous air temperatures and seasonal-precipitation patterns (up to +2–3 °C and −73%, respectively). Glacier contribution to streamflow doubled to tripled during these snow droughts in both catchments, manifesting through four mechanisms: an earlier-than-usual onset of the glacier melt season, an intensification of glacier melt contribution to streamflow, an earlier-than-usual seasonal peak in glacier melt contribution, and an extension of the glacier melt season.

---

## 农业区陆面模式改进

Li等人针对大多数CLM实现中使用静态、季节均一化灌溉图这一关键不确定性来源展开研究。通过将印度的季节性灌溉图引入CLM，他们在季风前期将蒸腾-蒸散发比（T/ET）提高了最高30%，表明灌溉效率的表达得到显著改善。实验还表明，更高的灌溉频率会导致灌溉水量、蒸散发和地表径流的级联增加——这对ESM模拟中农业用水抽取及其对区域水文循环的反馈具有直接影响。该方法经遥感蒸散发产品验证，证明在具有显著作物季节性的地区，动态灌溉表达对陆面建模至关重要。

### Improving irrigation and evapotranspiration simulation by incorporating seasonal irrigation map into a land surface model

**作者**: Dazhi Li, Jiaqi Sun, Xiaojun Wang, Netrananda Sahu, Qianya Yang, Jie Zhang, Zebin Zhao

**期刊**: *Geoscience Letters* · **DOI**: [10.1186/s40562-026-00500-2](https://doi.org/10.1186/s40562-026-00500-2) · **引用次数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> Irrigation is essential for maintaining the agricultural production and supporting India's growing population. Land surface models provide an effective approach to estimate irrigation requirements and hydrological fluxes. However, the irrigation modeling tends to be affected by uncertainties related to the spatiotemporal uncertainty in irrigation map, frequency and irrigation factor. To address these uncertainties, the irrigation and hydrological fluxes over India were reconstructed by simulation experiments with the Community Land Model (CLM). Results show that using a season-specific irrigation map improved the transpiration-total evapotranspiration ratio (T/ET) by up to 30% in the pre-monsoon season, implying higher irrigation efficiency. The remote sensing-based evapotranspiration products were used to compare with simulated model results, showing a similar increasing ET-trend in the pre-monsoon season as the irrigation induced CLM. Furthermore, the results show that higher irrigation frequency leads to increased irrigation amounts, evapotranspiration, and surface runoff.

---

## 统计数据

| 指标 | 数量 |
|:-------|------:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 获取论文总数 | 7 |
| 去重后 | 5 |
| 经LLM相关性筛选后 | 5 |
| 已拒绝（不相关） | 0 |

### 各期刊论文数

| 期刊 | 论文数 |
|:--------|-------:|
| Earth System Science Data | 2 |
| Journal of Climate | 1 |
| Hydrology and Earth System Sciences | 1 |
| Geoscience Letters | 1 |

## 筛选标准

**主题关键词**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

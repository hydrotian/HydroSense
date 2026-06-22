---
layout: default
title: "第24周（6月8日 - 6月15日），6篇"
nav_order: 36
nav_exclude: true
lang: zh
lang_link: /2026/june/2026-06-22-weekly-review
date: 2026-06-22
categories: [weekly-zh, 2026, june]
tags: [hydrology, literature-review, research]
paper_count: 6
highlight: "在Noah-MP陆面模式中加入坡面流物理过程后，WRF成功重现了原方案完全无法模拟的珠江流域极端洪水。"
---

# 每周文献综述
{: .no_toc }

**第24周** · 2026年6月8日–6月15日
{: .text-grey-dk-000 }

在 **3** 个主题下共找到 **6** 篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

本周综述规模明显偏小：本次运行期间OpenAlex检索接口对所有查询均返回HTTP 429（速率限制）错误，因此全部结果仅来自Semantic Scholar——6篇的数量应视为本周实际发表论文数的下限，而非"本周文献稀少"的结论。在已获取的结果中，两篇陆面模式论文推进了与洪水相关的过程刻画精度（Noah-MP/WRF中的坡面流方案重现珠江流域极端洪水；基于陆面模式的林波波河流域径流模拟），同时一项新的通用耦合库为水文模式与地球系统模式的集成提供了基础设施支持。在管理层面，灌溉遥感综述与社会水文多智能体建模则指向将人类决策与地球观测更好地融入水资源规划的方向。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 陆面与水文模式耦合

本周三项研究推进了耦合水文与陆面模拟的技术基础。Qiu等人在通用Noah-MP陆面模式中加入了显式坡面流方案，并将其与WRF耦合，应用于2024年4月珠江流域一次极端降水事件——改进方案重现的淹没范围与卫星观测一致，而原始WRF配置完全无法模拟此次洪水，且水文过程刻画的改进甚至通过陆气相互作用反馈提升了降水模拟效果。Mohomi等人针对南非林波波河流域采取了类似思路，应用陆面模式模拟这一跨境、半干旱且观测数据稀缺流域的河流径流。在基础设施层面，Abele等人解决了此类耦合模拟背后的"管道"问题：他们基于preCICE耦合库开发的新适配器将冰盖与海平面系统模式（ISSM）与冰下水文模式CUAS-MPI连接起来，提供了一种通用、可复用的双向耦合层，其应用范围超越冰盖场景，可扩展至任何涉及水文子模式的多物理场地球系统模式耦合。

### Incorporating Overland Flow into the WRF Noah-MP Land Surface Scheme and Applying to a Record Flood Simulation in the Pearl River Basin

**作者**: Shengyuan Qiu, H. Ren, Ping Zhao, Yuhao Wang, Weiteng Qiu, Yinghan Sang

**期刊**: *Journal of Hydrometeorology* · **DOI**: [10.1175/jhm-d-25-0081.1](https://doi.org/10.1175/jhm-d-25-0081.1) · **引用次数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 随着全球变暖加剧洪水强度和频率，作者在Noah-MP陆面模式中加入坡面流方案并与WRF耦合，应用于2024年4月珠江流域一次极端降水事件。改进方案模拟的淹没范围与卫星观测一致，土壤湿度误差也有所降低，而原始WRF配置则完全无法重现此次洪水——水文过程刻画的改进还通过陆气耦合提升了降水模拟能力。

---

### Simulating riverflow in South Africa's Limpopo River Basin using term land surface model

**作者**: Tumelo Mohomi, V. Stepanenko, A. Medvedev, I. Dhau, Hector Chikoore, M. Bopape

**期刊**: *Theoretical and Applied Climatology* · **DOI**: [10.1007/s00704-026-06337-1](https://doi.org/10.1007/s00704-026-06337-1) · **引用次数**: 0

**匹配主题**: land surface model
{: .label .label-green }

> 摘要暂不可用。根据标题推断，本研究应用陆面模式模拟林波波河流域的河流径流，该流域为跨境半干旱流域，覆盖南非、博茨瓦纳、津巴布韦和莫桑比克。

---

### New generic coupling adapters for ice sheet and subglacial hydrology models (ISSM-preCICE Adapter 0.4, CUAS-MPI 0.1)

**作者**: Daniel Abele, T. Kleiner, Yannic Fischler, B. Uekermann, G. Chourdakis, M. Morlighem et al.

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-5019-2026](https://doi.org/10.5194/gmd-19-5019-2026) · **引用次数**: 0

**匹配主题**: hydrology
{: .label .label-green }

> 作者利用preCICE耦合库将冰盖与海平面系统模式（ISSM）与冰下水文模式CUAS-MPI连接起来，构建了通用适配器以在模式间传递网格和耦合变量，无需依赖庞大、临时拼接的耦合代码。在高性能计算集群上的性能测试表明，单向和双向耦合均具有较低的计算开销和稳定的可扩展性，该适配器设计为可复用，适用于冰-水文耦合之外的场景，包括全球地球系统模式或其他过程模式。

---

## 水资源管理与灌溉

两项研究从人类决策和地球观测的角度探讨水资源管理。Zhang与Chui提出了一种双层多智能体框架来刻画社会水文动力学，明确建模策略驱动的行为主体如何与流域水资源系统的不确定性相互作用——这是将人类决策表示为动态策略过程而非静态边界条件的一步进展。Rossi等人综述了83篇同行评审研究（2002–2025年），探讨遥感技术在灌溉水管理中的应用，总结了多传感器融合、无人机监测以及机器学习增强的灌溉调度和土壤湿度估算方面的进展，同时指出模式可迁移性、地面验证以及将遥感产出转化为可操作决策支持系统等方面仍存在差距——为灌溉与农业水文建模研究提供了有价值的现状参考。

### Modeling Strategy-Driven Socio-Hydrologic Dynamics in Uncertain Watershed Water Resource Systems Using a Bi-level Multiagent Framework

**作者**: Mengxiang Zhang, T. M. Chui

**期刊**: *Water Resources Management* · **DOI**: [10.1007/s11269-026-04770-5](https://doi.org/10.1007/s11269-026-04770-5) · **引用次数**: 0

**匹配主题**: hydrologic model
{: .label .label-green }

> 摘要暂不可用。根据标题推断，本研究提出一种双层多智能体建模框架，以刻画策略驱动的行为主体如何在不确定性条件下塑造流域水资源系统的社会水文动力学。

---

### Remote Sensing for Irrigation Water Management Under Climate Change: Advances, Challenges, and Future Directions

**作者**: Hala Rossi, E. Cherif, El Mustapha Azzirgue, Hamza El Azhari, Hakim Boulaassal, O. E. Kharki

**期刊**: *Climate* · **DOI**: [10.3390/cli14060124](https://doi.org/10.3390/cli14060124) · **引用次数**: 0

**匹配主题**: climate change
{: .label .label-green }

> 灌溉农业占全球淡水取用量的70%，本综述总结了83篇同行评审研究（2002–2025年）关于光学、热红外和微波遥感监测土壤湿度、蒸散发、作物生长和灌溉效能的进展。文章重点介绍了多传感器融合、无人机监测以及机器学习方法在灌溉调度和作物水分胁迫检测方面的进展，同时指出数据融合、模式可迁移性、地面验证以及政策层面仍存在制约其实际应用的差距。

---

## 气候变化对水资源的影响与复合灾害

Mohammadi与Mostafazadeh对92项研究（1999–2025年）的范围综述，梳理了伊朗城市地区的极端与复合气候灾害，发现该国正经历"水文气候剧变"——干旱与洪水之间的急剧转换——并叠加城镇化导致的不透水面与地表径流增加，以及沿海地区面临的海平面上升风险。这是一项有价值的区域案例研究，进一步印证了气候变暖背景下水文气候极端事件非平稳性的广泛文献结论。

### Intensification of Extreme and Compound Hazards in Urban Areas Under Climate Change in Iran: A Scoping Review

**作者**: Niloofar Mohammadi, R. Mostafazadeh

**期刊**: *Climate* · **DOI**: [10.3390/cli14060126](https://doi.org/10.3390/cli14060126) · **引用次数**: 0

**匹配主题**: climate change
{: .label .label-green }

> 本范围综述总结了92项研究（1999–2025年），涉及伊朗城市地区的极端与复合气候灾害，涵盖热浪、干旱、暴雨、海平面上升及复合事件。伊朗西部面临因城镇化导致径流增加而加剧的暴雨风险，沿海地区则因海平面上升和风暴叠加而极易遭受复合洪水，整个国家正经历由全球变暖驱动的"水文气候剧变"——干旱与洪水之间的急剧转换。

---

## 统计数据

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 获取论文总数 | 14 |
| 去重后 | 10 |
| LLM相关性筛选后 | 6 |
| 已拒绝（不相关） | 4 |

**说明**：本次运行期间，OpenAlex检索接口对所有查询均返回HTTP 429（速率限制）错误，14篇获取论文全部来自Semantic Scholar。本周的覆盖范围应视为下限，而非6月8日至15日发表文献的完整图景。

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|-------:|
| Climate | 2 |
| Geoscientific Model Development | 1 |
| Journal of Hydrometeorology | 1 |
| Theoretical and Applied Climatology | 1 |
| Water Resources Management | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

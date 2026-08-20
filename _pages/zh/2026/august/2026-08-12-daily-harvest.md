---
layout: default
title: "8月12日，7篇"
nav_exclude: true
lang: zh
lang_link: /2026/august/2026-08-12-daily-harvest
date: 2026-08-12
categories: [daily-zh, 2026, august]
tags: [hydrology, paper-harvest, research]
paper_count: 7
highlight: "中世纪欧洲1341–1343年连环特大洪水——两年内16次重大洪水，四次达500–1000年重现期——揭示当前洪水风险管理体系对极端洪水序列毫无准备（Nature）。"
---

# 论文采集报告
{: .no_toc }

**日期范围**：2026年8月12日
{: .text-grey-dk-000 }

从 **115** 篇总发表中筛选出 **7** 篇顶级期刊论文
{: .fs-5 .fw-300 }

## 今日亮点

一项里程碑式的Nature研究重建了1341–1343年欧洲16次重大洪水事件——其中四次重现期达500–1000年——表明连环特大洪水序列是气候系统的真实特征，而当前风险管理框架对此类多次极端事件的连发严重准备不足。在机器学习水文领域，一项GRL研究显示，来自AlphaEarth和StefaLand的地理空间基础模型嵌入可替代或补充深度学习降雨-径流模型中的传统流域属性，在有数据流域达到同等精度，在无资料流域显著提升预测效果。与此同时，另一篇Nature论文发布了HydroGym——一个面向流体动力学控制问题的强化学习基准平台，大幅降低了小型地球科学团队尝试水资源系统RL优化的技术门槛。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 顶级期刊论文

### Cascading continental-scale floods across Europe in 1342–1343

**作者**：Andrea Kiss, Alberto Viglione, Mariano Barriendos, Silvia Enzi, Martin Bauch, Kris Decker 等

**期刊**：*Nature* · **DOI**：[10.1038/s41586-026-10888-8](https://doi.org/10.1038/s41586-026-10888-8)

**匹配主题**：flood
{: .label .label-green }

![Figure](https://media.springernature.com/m685/springer-static/image/art%3A10.1038%2Fs41586-026-10888-8/MediaObjects/41586_2026_10888_Fig1_HTML.png)

> 近几十年来，欧洲经历了多次极端洪水。然而，更大规模的洪水仍有可能发生，必须纳入洪水风险管理考量。分析有据可查的最大历史洪水有助于揭示其特征。在中欧，1342年7月的"抹大拉洪水"通常被视为过去千年中规模最大的洪水，但其特征的认识仍不完整。本研究表明，1341年底至1343年间，欧洲大部分地区共发生16次重大洪水事件，其中四次（抹大拉、巴塞洛缪、圣烛节和雅各布洪水）的重现期达500–1000年。尽管抹大拉洪水此前被认为是1342年唯一的欧洲极端洪水，但新的文献数据集表明它是更广泛洪水序列的组成部分。过去700年中极端洪水次数最多的年份是1342年，1343年则跻身前十。这一异常洪水序列对社会经济造成了巨大影响，并促成了欧洲洪水防御理念的范式转变。一系列火山爆发叠加北极海冰多年退缩是这一洪水序列的可能成因。在短短几个月内聚集的极端洪水群在风险管理中鲜少被考虑，迫切需要能够应对此类情景的快速主动应对策略。

---

### Geospatial Foundation Embeddings as Transferable Catchment Descriptors

**作者**：Jiangtao Liu, Chaopeng Shen, Yuan Yang, Haoyu Ji, Kathryn Lawson, Nicholas Kraabel

**期刊**：*Geophysical Research Letters* · **DOI**：[10.1029/2026gl122814](https://doi.org/10.1029/2026gl122814)

**匹配主题**：runoff
{: .label .label-green }

> 深度学习水文模型依赖静态流域属性来表征流域异质性，但传统属性存在区域不一致性和时间代表性不足的问题。本研究以AlphaEarth和StefaLand地理空间基础模型嵌入作为可迁移流域描述符，评估其在降雨-径流建模中的应用。在531个CAMELS流域的时间验证中，仅使用AlphaEarth嵌入训练的深度学习模型与使用传统属性的模型性能相当（中位NSE分别为0.779和0.781）。在涵盖3434个流域的全球无资料流域预测（PUB）场景中，将嵌入与传统属性结合使中位NSE从0.683提升至0.720。双路径门控模型揭示了结构化的时空依赖模式：模型在融雪转换期和湿润流域中优先利用嵌入，而在干旱流域中依赖度有限。StefaLand嵌入的独立验证结果一致，支持将学习嵌入广泛应用为可迁移流域描述符。

---

### The Portrait of Flood Risk in Italy: Past, Present and Future, From 1870 to 2100

**作者**：Luciano Pavesi, Jose Luis Salinas, Stefano Zanardo, Maximiliano Sassi, Arno Hilberts, Elena Volpi 等

**期刊**：*Geophysical Research Letters* · **DOI**：[10.1029/2026gl122987](https://doi.org/10.1029/2026gl122987)

**匹配主题**：river, flood, climate change
{: .label .label-green }

> 在欧洲各国中，意大利是洪水风险最高的国家之一。气候变化和洪泛区快速城镇化被认为是进一步增加风险人口的两大主要驱动因素。本研究利用大尺度洪水风险模型RESCUE-FR，对意大利230年（1870–2100年）洪水风险的两大驱动因素进行全面评估，重点分析二者如何交互作用以放大风险。研究基于200年重现期情景评估风险人口规模的历史演变及未来预测。结果表明，历史上意大利洪水风险的增加主要受人口增长和向洪泛区迁移驱动，而未来预测显示气候变化将成为洪水风险的主导驱动力。

---

### Positive Association Between Coastal Sea Surface Temperatures and Humid Heat Stress on Nearby Land

**作者**：Noel V. A. Siegert, Radley M. Horton

**期刊**：*Geophysical Research Letters* · **DOI**：[10.1029/2026gl122646](https://doi.org/10.1029/2026gl122646)

**匹配主题**：coastal, marine heatwave
{: .label .label-green }

> 地球沿海地区人口密集，面临包括极端湿热在内的多种气候风险。随着近岸海洋增温和海洋热浪（MHW）活动增强，本研究探究近岸海表温度（SST）与邻近陆地热湿条件之间的关联。通过分析1990–2023年全球1474个沿海站点的近岸SST与陆地热特征，研究发现MHW发生与各季节陆地热湿正异常相关，近岸SST偏高与陆地高温/极端湿热事件频率增加相关。结果还揭示了许多地区海洋与陆地（THW）热浪并发天数的增加，这主要由MHW趋势驱动。MHW、THW及并发事件具有相似的积累特征，但并发事件和MHW比THW更为湿润，且温度异常峰值出现在近地面而非高空。

---

### Dipole in North African Dust Deposition at the Last Glacial Maximum Explained by Shifted Wind Direction Under Steepened Meridional Temperature Gradients

**作者**：Fangjingcheng Zhu, Peter O. Hopcroft, Samuel Albani, Minmin Fu, Anya J. Crocker, Chuang Xuan 等

**期刊**：*Geophysical Research Letters* · **DOI**：[10.1029/2026gl121937](https://doi.org/10.1029/2026gl121937)

**匹配主题**：earth system model
{: .label .label-green }

> 地质记录表明，末次盛冰期（LGM）全球大气尘埃含量远高于现今，但解释仍存争议，干旱加剧、风速增强/阵风增多和干燥大气洗涤效率降低均被援引为可能原因。然而，沙尘沉积在空间上可呈现复杂分布。北大西洋和地中海均接受来自全球主要来源地——北非的沙尘，但二者呈现出LGM沙尘输入增减相反的偶极模式。本研究利用两个地球系统模型的工业前和LGM模拟探究这一偶极格局。研究表明，非洲沙尘向西输出至大西洋受北大西洋经向热力梯度陡峭和亚速尔高压增强的驱动，而向北输送至地中海则在温度梯度和亚速尔高压较弱时占优。研究结果表明，风向能够强烈影响古沙尘和古气候记录的解读。

---

### CROCUS Urban Canyons

**作者**：Scott Collis, Paytsar Muradyan, Robert Jackson, Bhupendra A. Raut, Joseph R. O'Brien, Matthew E. Tuftedal 等

**期刊**：*Bulletin of the American Meteorological Society* · **DOI**：[10.1175/bams-d-24-0263.1](https://doi.org/10.1175/bams-d-24-0263.1)

**匹配主题**：earth system model
{: .label .label-green }

![Figure](https://journals.ametsoc.org/cover/journals/bams/bams_cover.jpg)

> CROCUS是美国能源部整合城市野外实验室，致力于改进地球系统模型中对城市地球系统过程的表达，研究聚焦芝加哥。CROCUS观测策略的核心组成部分是一系列野外观测试验。首次野外观测于2024年7月开展，聚焦城市下垫面与中西部及大湖地区大气的耦合过程。观测活动旨在研究城市热岛效应，但由于一股气候异常的冷气团盘踞该地区，科学目标随之调整。CROCUS城市峡谷观测共从三个站点施放43个探空气球和17个风流探空仪，以研究包括湖风在内的边界层流场。此外，SPARC观测拖车部署于芝加哥市中心边缘，采集了罕见的多频LiDAR和辐射计数据集。在作为重点研究对象的城市峡谷附近UIC校园，还开展了全面的大气化学测量；在两个为期两天的集中观测时段内收集了逾400项便携式气象、空气化学和颗粒物测量数据。社区合作、宣传和公众参与是本次城市野外观测不可或缺的组成部分，有效提升了芝加哥市民对气象观测的认知。

---

### The HydroGym reinforcement learning platform for fluid dynamics

**作者**：Christian Lagemann, Sajeda Mokbel, Miro Gondrum, Mario Rüttgers, Yuning Wang, Pol Suárez 等

**期刊**：*Nature* · **DOI**：[10.1038/s41586-026-10917-6](https://doi.org/10.1038/s41586-026-10917-6)

**匹配主题**：fluid dynamics, reinforcement learning
{: .label .label-green }

> 暂无摘要。

---

## AI 与科研

### 跨学科启发

- **[Computational 'gym' trains AI models to control turbulence](https://www.nature.com/articles/d41586-026-02375-x)** (Nature, 2026-08-19) — Nature发布了HydroGym——一个专为流体动力学控制问题设计的强化学习基准环境（涵盖槽道流、钝体尾迹、腔体流等场景）。对于地球科学团队而言，这是一个可直接迁移至水资源管理系统的现成RL训练框架——水库泄洪优化、灌溉渠闸门控制或地下水人工补给调度——底层物理（大尺度Navier-Stokes方程）面临同样的挑战，1–2人的小型团队现在无需从头搭建环境即可尝试闭环控制。

## 统计信息

| 指标 | 数量 |
|:-----|-----:|
| 检索期刊数 | 11 |
| 抓取论文总数 | 115 |
| 通过确定性筛选 | 16 |
| LLM相关性筛选后 | 7 |
| 被排除（不相关） | 10 |
| AI与科研条目 | 1 |

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|------:|
| Nature | 2 |
| Geophysical Research Letters | 4 |
| Bulletin of the American Meteorological Society | 1 |

## 筛选标准

**主题**：hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model, estuary, coastal, freshwater discharge, river plume, ocean biogeochemistry, marine heatwave, paleohydrology, paleoclimate, Quaternary, Holocene, Pleistocene, fluvial geomorphology, river terrace, loess, drainage network, river capture, landscape evolution, luminescence dating

**领域**：engineering, environmental science, computer science, geology, geography

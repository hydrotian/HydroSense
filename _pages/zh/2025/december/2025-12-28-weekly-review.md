---
layout: default
title: "第52周（12月22日 - 12月28日），11篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2025/december/2025-12-28-weekly-review
date: 2025-12-28
categories: [weekly-zh, 2025, december]
tags: [hydrology, literature-review, research]
paper_count: 11
highlight: "嵌入地球系统模式的过程化作物模型预测到2050年全球粮食作物平均旱灾损失小于2%,但有62个国家最大损失超过10%。"
---

# 每周文献综述
{: .no_toc }

**第52周** · 2025年12月22日–28日
{: .text-grey-dk-000 }

发现 **11** 篇相关论文,归为 **4** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

2025年最后一周发表了一批关于干旱、土地–水耦合以及水文深度学习的高影响论文。《自然-通讯》的一项重磅研究在地球系统模式中嵌入过程化作物模型,定量评估干旱对2050年全球粮食安全的影响;《自然-可持续发展》和《基于自然的解决方案》则分别从土地利用和森林管理角度探讨了如何同时满足生态与农业用水需求。方法学上,本周展示了水文深度学习的成熟——针对土壤水分、陆地水储量和地下水的新一代视觉Transformer和图神经网络架构,以及经典的流域尺度同位素和遥感研究。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 干旱、土地利用与气候–水安全

本周最突出的信号是气候变化与土地管理决策如何共同塑造粮食与生态用水。Carter等人将过程化作物模型嵌入地球系统模式,预测到2050年全球主要作物的平均旱灾损失不超过2%,但有62个国家最大产量损失超过10%、24个国家超过20%,其中南美、非洲、东欧和东南亚风险最高。Lester等人在《自然-可持续发展》上提出,若规划框架显式利用协同效应,气候变化下生态用水与农业用水可以同时得到保障。Hernández-Sosa等人检验了另一个互补杠杆——智利中南部大规模本土森林恢复:在RCP8.5情景下,将本土森林恢复布置在流域中上游区域可在旱季缓冲河川径流,而外来人工林则会因蒸散发增强进一步加剧流量衰减。

### Impact of drought on global food security by 2050

**作者**: V. A. Carter, K. Paff, D. Comeau, K. Solander, T. Pitts, S. Price 等

**期刊**: *Nature Communications* · **DOI**: [10.1038/s41467-025-67862-7](https://doi.org/10.1038/s41467-025-67862-7) · **引用数**: 4

**匹配主题**: drought, land surface model, earth system model
{: .label .label-green }

> 在地球系统模式中耦合过程化作物模型,评估干旱对2050年玉米、大豆、水稻和小麦全球产量的影响。全球平均损失小于2%(大豆最高达3.6%),但62个国家最大损失超过10%、24个国家超过20%。结合社会经济因素构建的粮食不安全指数识别出南美、非洲、东欧和东南亚为最高风险区。

---

### Synergies in environmental and agricultural water availability under climate change

**作者**: R. E. Lester, D. Robertson, J. Bailey, G. Dwyer, G. Holt, S. Jalilov 等

**期刊**: *Nature Sustainability* · **DOI**: [10.1038/s41893-025-01720-8](https://doi.org/10.1038/s41893-025-01720-8) · **引用数**: 2

**匹配主题**: water management, climate change
{: .label .label-green }

> 识别气候变化下生态用水与农业用水之间的协同效应,主张在规划框架中显式考虑二者的重叠收益,即可同时满足两类需求,而非将其作为相互竞争的用途。

---

### Assessing hydrological responses to large-scale native forest restoration as a nature-based solution in South-Central Chile

**作者**: M. Hernández-Sosa, M. Aguayo, N. Cortes, A. Stehr, F. Frances, O. Llompart 等

**期刊**: *Nature-Based Solutions* · **DOI**: [10.1016/j.nbsj.2025.100298](https://doi.org/10.1016/j.nbsj.2025.100298) · **引用数**: 2

**匹配主题**: hydrologic model, streamflow, climate change
{: .label .label-green }

> 采用TETIS水文模型在RCP8.5情景下模拟智利Araucanía大区Imperial河两个子流域的四种森林恢复情景。结果显示气候与土地利用变化共同驱动最大水文变化;将本土森林恢复布置于流域中上游在旱季对河川径流有缓冲作用,而外来人工林则因蒸散发增加而加剧流量衰减。

---

## 水文深度学习与遥感

本周三篇深度学习论文推进了多尺度水量状态的数据驱动估计。Yan等人提出MSA-ViT,一种融合多头自注意力与物理散射理论的视觉Transformer框架,用于从CYGNSS反射率反演土壤水分,在3–60天多时间尺度上均优于传统回归和浅层神经网络。Gentner等人提出DeepRec,采用CNN+LSTM架构并结合集成不确定性量化,将月尺度陆地水储量反演回溯至1941年——填补了GRACE之前的数据空白,为长期气候分析打开水文记录。在局地尺度,Zhuang等人将图神经网络与循环神经网络融合为STGPM,利用监测井之间的空间连通性和多尺度时间依赖性预测济南市地下水位,显著优于标准时间序列基线。

### A Modified Hierarchical Vision Transformer for Soil Moisture Retrieval From CYGNSS Data

**作者**: Q. Yan, Y. Chen, Y. Pan, S. Jin, W. Huang

**期刊**: *Water Resources Research* · **DOI**: [10.1029/2024WR039476](https://doi.org/10.1029/2024WR039476) · **引用数**: 3

**匹配主题**: hydrologic model
{: .label .label-green }

> 提出MSA-ViT——一个融合多头自注意力的视觉Transformer,用于从CYGNSS反射率反演土壤水分。模型将相干散射物理机制与深度学习结合,捕捉土壤水分、表面粗糙度和植被衰减之间的非线性相互作用。使用10天平均数据训练并在3–60天尺度上验证,性能超越线性回归、浅层神经网络和现有DL模型。

---

### DeepRec: Global Terrestrial Water Storage Reconstruction Since 1941 Using Spatiotemporal-Aware Deep Learning

**作者**: L. Q. Gentner, J. Gou, M. J. Tourian, L. Börger, N. Sneeuw, B. Soja

**期刊**: *Journal of Geophysical Research: Machine Learning and Computation* · **DOI**: [10.1029/2025JH000889](https://doi.org/10.1029/2025JH000889) · **引用数**: 2

**匹配主题**: hydrology, hydrologic model, land surface model, earth system model
{: .label .label-green }

> 使用以气候再分析变量和土地利用为输入、结合CNN与LSTM的深度学习架构,将类GRACE月尺度陆地水储量异常反演至1941年。集成方法同时量化数据不确定性和模型不确定性。DeepRec将水文记录延长至GRACE之前六十余年,为长期气候分析提供前所未有的数据支撑。

---

### Enhancing groundwater level prediction with a hybrid deep learning model in Jinan City, China

**作者**: C. Zhuang, L. Cui, Y. Cui

**期刊**: *Scientific Reports* · **DOI**: [10.1038/s41598-025-28200-5](https://doi.org/10.1038/s41598-025-28200-5) · **引用数**: 2

**匹配主题**: hydrology, hydrologic model
{: .label .label-green }

> 构建时空图预测模型(STGPM),融合图神经网络(刻画监测井之间的空间关系)与循环神经网络(建模时间动态),预测地下水位波动。在测试集上取得MAE = 0.039、RMSE = 0.052,优于标准时间序列模型,应对复杂水文地质耦合的非线性挑战。

---

## 水动力与流域尺度过程研究

三篇论文深入流域尺度过程,涵盖观测与模型。Simard等人介绍NASA Delta-X框架——一个结合机载遥感与原位观测的系统,用于校准密西西比河三角洲的水动力、泥沙输运及生态地貌模型,弥补天基观测在高时空变率上的不足。在上印度河流域,Nasir等人结合遥感与多方法统计分析,量化积雪变率如何传播到径流与水电潜力,这是巴基斯坦水与能源安全的核心议题。Perry等人利用δ¹⁸O同位素示踪剂在西卡斯卡德山脉的山地源头流研究发现,滑坡与地滑堆积物在旱季仍能持续供给地下水并维持水文连通性——这一过程在标准集总流域模型中常被忽略。

### Delta-X: An airborne remote sensing framework to calibrate hydrodynamic and ecogeomorphic processes responsible for land building in coastal deltas

**作者**: M. Simard, C. E. Jones, R. R. Twilley, E. Castañeda-Moya, S. Fagherazzi, C. G. Fichot 等

**期刊**: *Remote Sensing of Environment* · **DOI**: [10.1016/j.rse.2025.115201](https://doi.org/10.1016/j.rse.2025.115201) · **引用数**: 3

**匹配主题**: hydrologic model, land surface model, surface water
{: .label .label-green }

> 介绍NASA Earth Venture-Suborbital Delta-X框架,结合机载雷达与原位观测,校准与验证密西西比河三角洲的水动力、泥沙输运、形态演化与生态地貌模型。框架应用于活跃的Atchafalaya盆地(陆地增长)和已废弃的Terrebonne盆地(陆地流失),应对天基遥感在高时空复杂度下的局限。

---

### Remote sensing and multi-method statistical analysis of snow cover variability and hydrological responses in the Upper Indus Basin

**作者**: A. Nasir, S. Fahd, N. Wang, M. Zubair, A. A. Nadeem, Z. Zafar 等

**期刊**: *Physics and Chemistry of the Earth* · **DOI**: [10.1016/j.pce.2025.104263](https://doi.org/10.1016/j.pce.2025.104263) · **引用数**: 4

**匹配主题**: hydrologic model, runoff, hydropower
{: .label .label-green }

> 结合遥感与多方法统计分析,刻画上印度河流域积雪变率及其水文与水电响应。该流域是巴基斯坦水资源与能源安全的关键区域。

---

### The Influence of Geomorphology on Storage and Surface Water–Groundwater Interactions in Mountainous Headwater Streams

**作者**: Z. Perry, C. Segura, J. R. Brooks, S. Takaoka, F. J. Swanson

**期刊**: *Hydrological Processes* · **DOI**: [10.1002/hyp.70361](https://doi.org/10.1002/hyp.70361) · **引用数**: 1

**匹配主题**: hydrology, streamflow, surface water
{: .label .label-green }

> 在西卡斯卡德山脉源头集水区使用δ¹⁸O同位素示踪剂,揭示滑坡与地滑堆积物形成的持续地下水贡献如何在旱季维持水文连通性。空间同位素模式表明滑坡地貌驱动的亚地表跨流域水流路径,这些过程在标准集总流域模型中鲜被表征。

---

## 水文知识与水资源管理

《水文学报》两篇论文讨论了水文科学本身的框架及其决策相关性。Zwarteveen等人在一个特刊开篇中提出"基于场景"的社会水文学宣言,倡导重视情境化、建构性的知识生产,推动水文与社会科学方法论的对称,以挑战长期以来对"超然、可复现"的认识论偏好。Wang等人则聚焦实际应用端,诊断1981–2024年亚热带地区多尺度降水模式变化,并讨论其对非平稳条件下水资源管理的启示。

### A situated proposal for a grounded approach to socio-hydrology

**作者**: M. Zwarteveen, O. Barreteau, A. Ogilvie, M. Kuper, J.-P. Venot

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134828](https://doi.org/10.1016/j.jhydrol.2025.134828) · **引用数**: 3

**匹配主题**: hydrology
{: .label .label-green }

> 倡导一种将水文知识视为情境性和建构性的社会水文学,追求水文与批判性社会科学知识生产方法的对称。呼吁水文学放弃对"超然、可复现"的认识论偏好,转向更谦逊、以地方为基础的介入式研究,使知识生产重新连接到具体的水域、社区与政治语境。

---

### Multi-scale shifts in rainfall patterns in a subtropical region (1981–2024): challenges and implications for water management

**作者**: H. Wang, T. Asefa, F. Getachew, Y. Zhou

**期刊**: *Journal of Hydrology* · **DOI**: [10.1016/j.jhydrol.2025.134851](https://doi.org/10.1016/j.jhydrol.2025.134851) · **引用数**: 2

**匹配主题**: water management
{: .label .label-green }

> 考察1981–2024年亚热带地区多尺度降水模式变化,指出非平稳降水对水资源管理和供水规划提出的挑战。

---

## 统计信息

| 指标 | 数量 |
|:-------|------:|
| 检索数据库 | 2 |
| 检索主题 | 16 |
| 去重前论文数 | 2,017 |
| 去重后唯一论文 | 1,826 |
| 相关性过滤后 | 11 |
| 剔除(不相关) | 1,815 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

**排序模式**: established(回填式检索采用引用数优先)

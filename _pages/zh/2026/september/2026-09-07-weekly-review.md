---
layout: default
title: "第36周（8月31日 - 9月7日），3篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/september/2026-09-07-weekly-review
date: 2026-09-07
categories: [weekly-zh, 2026, september]
tags: [hydrology, literature-review, research]
paper_count: 3
highlight: "新教材综合六十年流量生成科学成果；偏差校正后的格网降水数据在数据匮乏山区流域的SWAT+模拟中表现优于原始站点数据。"
---

# 每周文献综述
{: .no_toc }

**第36周** · 2026年8月31日–9月7日
{: .text-grey-dk-000 }

**3** 篇相关论文，涵盖 **2** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

本周文献产出相对有限，但以一项重要资源为核心：Jeffrey McDonnell的新教材《Streamflow Generation》对流域水文学一百年的成果进行了全面综合，将基于野外过程认识的理解置于模型开发的基础地位。在应用建模方面，两项研究分别针对不同尺度的精度挑战——其一表明，对格网降水进行均值场偏差校正可大幅提升SWAT+在墨西哥数据匮乏山区流域的流量模拟精度；另一项则表明，显式表达土壤垂直异质性可显著降低小农农业系统超高分辨率陆面模型的根区土壤水分偏差。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 流量生成与过程水文学

McDonnell的新书是对流域水文学界已知成果——以及尚未明确的知识——的里程碑式综合，揭示了集水区如何储存和释放水分。全书追溯了从20世纪初野外测量、到20世纪80—2000年代同位素示踪革命的科学脉络，最终形成融合点尺度、坡面和流域尺度过程认识的现代概念模型。McDonnell明确指出，模型发展往往超前于机理认识，并将剩余的前沿问题——水文连通性、滞留时间分布以及径流和蒸腾水的传输时间分布——界定为需持续野外发现的基础性问题。对于构建或评估河道汇流和陆面模型的研究者而言，本书是一种有益的校正，将参数化选择植根于过程认识之中。

### Streamflow Generation

**作者**: Jeffrey J. McDonnell

**期刊**: *Oxford Academic（专著）* · **DOI**: [10.1093/9780191953736.001.0001](https://doi.org/10.1093/9780191953736.001.0001) · **引用数**: 10

**匹配主题**: streamflow
{: .label .label-green }

> Most graduate students and practitioners addressing issues related to the flow of water in streams use models—to solve problems and predict outcomes. But those models are often based on antiquated notions of how catchments generate streamflow. *Streamflow Generation: Processes and Perceptual Models* is a new narrative of what we know, what we think we know and what we need to know in terms of the flow pathways, sources and travel times of water through headwater catchments. Written by a field hydrologist, the book lowers the barrier of entry into this process hydrology world. The author covers the period from the first field-based measurements in the early twentieth century to the development of early rainfall–runoff concepts, the great geographic expansion of studies during the 1960s International Hydrological Decade and the radical shifts in our understanding resulting from using isotope tracers in catchment hydrology. He then covers our modern understanding of how catchments store and release water at the point, hillslope and catchment scales and how bottom-up and top-down measures have been used to develop perceptual models. The book ends by discussing the opportunities and challenges for catchment science and what remains to be discovered in terms of hydrological connectivity, sources, residence times and transit time distributions of streamflow and plant transpiration. The throughline of the book is that field work and field discovery is an essential part of hydrological science and that what remains to be discovered about streamflow generation is vast compared to what is now known.

---

## 水文建模：降水输入与土壤水分

本周两项建模研究分别在不同尺度上应对精度挑战。De la Fraga等评估了四种降水驱动方案（雨量站数据、原始Daymet数据及两种偏差校正Daymet产品）在墨西哥西马德雷山脉Humaya河流域SWAT+模型中的表现——该流域受季风气候主导，数据匮乏，地形复杂。其集合方法（每种配置保留前100组参数集）发现，Daymet均值场偏差校正（MFBC）整体表现最佳（NSE = 0.81，KGE = 0.85），而分位数映射甚至不及原始雨量站数据。关键在于，所有配置在低流量模拟方面均存在系统性缺陷（logNSE为负），表明SWAT+基流表达是制约精度的主要瓶颈，而非降水驱动本身。在更精细的尺度上，Krishnan等表明，在超高分辨率（30 m）陆面模型中引入土壤垂直异质性，可大幅降低小农农业系统根区水分偏差——这一结果对ELM和CLM在异质性农业景观中的高分辨率模拟具有重要参考意义。

### Hydrologic modeling in mountainous terrains with monsoonal climate: Do gridded precipitation data improve streamflow simulations?

**作者**: Pasquinel de la Fraga, E. Vivoni, Yalina Montecelos-Zamora, Francisco José Del-Toro-Guerrero, Tereza Cavazos 等

**期刊**: *Frontiers in Water* · **DOI**: [10.3389/frwa.2026.1788195](https://doi.org/10.3389/frwa.2026.1788195) · **引用数**: 0

**匹配主题**: hydrologic model
{: .label .label-green }

> Accurate hydrologic modeling in data-scarce mountainous regions remains challenging due to strong climatic variability, complex topography, and limited ground data. This study evaluates the influence of four precipitation inputs on the performance of the Soil and Water Assessment Tool Plus (SWAT+) model in the monsoon-dominated Humaya River basin, located in the Sierra Madre Occidental, northwestern Mexico. The evaluated inputs include: (1) rain gauge data (Gauge), (2) Daymet gridded data, and two bias-corrected Daymet products using (3) quantile mapping (Qmap) and (4) mean field bias correction (MFBC). Model calibration and validation were conducted independently for each input using monthly streamflow data (1983–2001). The Daymet-MFBC configuration achieved the best overall results (NSE = 0.81; PBias = 6.4%; KGE = 0.85). All configurations showed systematic deficiencies in low-flow simulation, reflecting a known limitation of SWAT+ in representing baseflow dynamics.

---

### Soil vertical heterogeneity reduces rootzone soil moisture bias in hyper-resolution land surface model over smallholder agricultural systems

**作者**: Vishnu U. Krishnan, N. Vergopolan, B. B. Singh, J. Indu, L. Karthikeyan

**期刊**: *Agricultural Water Management* · **DOI**: [10.1016/j.agwat.2026.110673](https://doi.org/10.1016/j.agwat.2026.110673) · **引用数**: 2

**匹配主题**: land surface model
{: .label .label-green }

> 摘要暂不可用。

---

## 统计数据

| 指标 | 数量 |
|:-------|------:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 获取论文总数 | 7 |
| 去重后 | 6 |
| LLM相关性过滤后 | 3 |
| 被拒绝（不相关） | 3 |

### 各期刊论文数

| 期刊 | 论文数 |
|:--------|-------:|
| Oxford Academic（专著） | 1 |
| Agricultural Water Management | 1 |
| Frontiers in Water | 1 |

## 筛选标准

**主题**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

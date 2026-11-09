---
layout: default
title: "第44周（10月26日 - 11月02日），2篇"
nav_order: 33
nav_exclude: true
lang: zh
lang_link: /2026/november/2026-11-09-weekly-review
date: 2026-11-09
categories: [weekly-zh, 2026, november]
tags: [hydrology, literature-review, research]
paper_count: 2
highlight: "Mamba状态空间模型在125个爱荷华流域120小时径流预测中达到与Transformer相当的精度，同时新型两阶段Rosenbrock求解器将E3SM大气化学积分时间缩短了33%。"
---

# 每周文献综述
{: .no_toc }

**第44周** · 2026年10月26日–11月02日
{: .text-grey-dk-000 }

在 **2** 个主题中共找到 **2** 篇相关论文
{: .fs-5 .fw-300 }

## 执行摘要

本周由于检索期间OpenAlex API频繁触发频率限制（429错误），数据来源受限，仅有Semantic Scholar的结果。尽管如此，仍有两篇值得关注的论文：一篇利用Mamba状态空间架构推进了深度学习长时程流量预测及多流域泛化能力，另一篇将E3SMv1大气化学求解器的计算效率提升了33%，对于在更大规模上运行耦合陆面-大气模拟具有直接意义。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 机器学习在径流预测中的应用

现代序列建模架构在水文预测领域的应用持续拓展。Demiray和Demir评估了Mamba架构——一种为高效处理长序列设计的状态空间模型（SSM）——在125个地理多样的爱荷华流域120小时前瞻径流预测中的表现，对比基准包括Transformer、LSTM、GRU和Seq2Seq模型。结果表明，Mamba的精度与Transformer相当，两者均显著优于经典循环神经网络方法。作者还采用SHAP（Shapley加性解释）方法揭示了各模型的内部特征利用模式，增强了模型可解释性。对于业务化水文预测而言，Mamba兼具多步泛化能力与内置可解释性，是在大陆尺度上值得进一步评估的高效替代方案。

### Advancing long-horizon hydrological forecasting: a Mamba-based approach with explainable AI for generalized streamflow prediction

**作者**: B. Demiray, Ibrahim Demir

**期刊**: *Journal of Hydroinformatics* · **DOI**: [10.2166/hydro.2026.115](https://doi.org/10.2166/hydro.2026.115) · **引用数**: 2

**匹配主题**: streamflow
{: .label .label-green }

> Accurate long-horizon streamflow forecasting is crucial for water resource management, but existing models often face efficiency and interpretability challenges. This study comprehensively evaluates the Mamba architecture, which utilizes state-space models (SSMs) for efficient sequence processing, for 120-h hourly generalized streamflow prediction across 125 diverse Iowa watersheds using 72-h historical inputs. Performance was benchmarked against Persistence, long short-term memory, gated recurrent unit, Seq2Seq, and Transformer models employing Nash–Sutcliffe efficiency, Kling–Gupta efficiency, Pearson's r, and normalized root-mean-square error. Results demonstrate that Mamba architecture achieves predictive accuracy comparable to, and in several aspects marginally exceeding, the robust Transformer baseline, with both models significantly outperforming other established methods. Critically, explainable AI using SHAP values provided insights into tested models' decision-making, revealing distinct feature utilization patterns and enhancing model transparency. This research highlights Mamba's potential as an efficient, accurate, and interpretable alternative for advancing operational long-range hydrological forecasting.

---

## 地球系统模式计算效率

提升地球系统模式（ESM）的数值效率，对于在更高分辨率、更长时间段或更多集合成员下开展气候模拟至关重要。Chien和Fu针对E3SM的主要计算瓶颈之一——刚性大气化学系统的时间积分——在E3SMv1中实现了半隐式两阶段Rosenbrock（ROS2）求解器。在两种复杂度各异的化学机制（chemUCI含60个物种，trop_strat_mozart_mam4含155个物种）下测试，ROS2相比原始隐式求解器在Cori/KNL平台上将化学积分时间缩短约33%，同时在一年积分中保持数值稳定性，全球平均臭氧偏差在1 ppb以内。结果支持ROS2作为E3SM短时步长化学积分的生产级替代方案，但作者指出仍需在现代CPU/GPU系统上开展进一步基准测试以评估性能可移植性。

### Using a two-stage Rosenbrock solver to increase computational efficiency in the DOE's Exascale Earth System Model version 1 (E3SMv1)

**作者**: Rong-You Chien, Joshua S. Fu

**期刊**: *Geoscientific Model Development* · **DOI**: [10.5194/gmd-19-10309-2026](https://doi.org/10.5194/gmd-19-10309-2026) · **引用数**: 0

**匹配主题**: earth system model
{: .label .label-green }

> The integration of stiff atmospheric chemical systems is a major computational cost in Earth System Models and poses challenges for numerical stability as chemical complexity and temporal resolution increase. In this study, we implement a semi-implicit two-stage Rosenbrock method (ROS2) in the Energy Exascale Earth System Model version 1 (E3SMv1) and evaluate it as an alternative chemistry time-integration scheme. ROS2 is tested with two interactive chemical mechanisms of substantially different size: chemUCI (60 prognostic species) and trop_strat_mozart_mam4 (155 prognostic species). Numerical experiments include short simulations to quantify computational cost, a box-model timestep-refinement analysis, and one-year integrations to examine numerical stability and solution sensitivity. At the same 180 s chemistry timestep, ROS2 requires approximately 33% less chemistry integration time than the original iterative implicit solver on the tested Cori/KNL CPU platform. The magnitude of this speedup is configuration dependent. Global-mean surface-ozone differences among the tested configurations are small (≤ 1.03 ppb), and the one-year integrations show no evidence of numerical instability. Spatial and diurnal differences in ozone, NO, NO₂, and OH are species- and mechanism-dependent, indicating sensitivity to both timestep and solver formulation rather than a common systematic bias. These results support ROS2 as a lower-cost alternative to the current implicit integrator when E3SM chemistry is operated at short timesteps; additional timestep-refinement tests and benchmarking on contemporary CPU/GPU systems are needed to quantify coupled-model convergence and performance portability.

---

## 统计信息

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 获取论文总数 | 5 |
| 去重后 | 5 |
| LLM相关性筛选后 | 2 |
| 不相关（已拒绝） | 3 |

### 各期刊论文数

| 期刊 | 篇数 |
|:-----|-----:|
| Journal of Hydroinformatics | 1 |
| Geoscientific Model Development | 1 |

## 筛选标准

**主题关键词**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

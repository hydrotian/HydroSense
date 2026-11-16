---
layout: default
title: "第45周（11月02日 - 11月09日），1篇"
nav_order: 34
nav_exclude: true
lang: zh
lang_link: /2026/november/2026-11-16-weekly-review
date: 2026-11-16
categories: [weekly-zh, 2026, november]
tags: [hydrology, literature-review, research]
paper_count: 1
highlight: "耦合地球系统模式中，Noah-MP陆面参数化方案通过增强陆-气耦合效率，重现了亚马逊-太平洋遥相关并改善了ENSO空间结构（JGR-大气）。"
---

# 每周文献综述
{: .no_toc }

**第45周** · 2026年11月02日–11月09日
{: .text-grey-dk-000 }

共发现 **1** 篇相关论文，涵盖 **1** 个主题
{: .fs-5 .fw-300 }

## 执行摘要

本周关键词搜索结果较少，OpenAlex因频繁触发限流（全程返回429错误）而基本不可用，仅有Semantic Scholar的结果。《地球物理研究快报-大气》中有一篇值得关注的论文：研究表明在耦合地球系统模式中，真实的陆面参数化方案（Noah-MP与Noah 2.7.1对比）显著增强了陆-气耦合效率，重现了观测到的亚马逊-太平洋遥相关并改善了ENSO空间结构——这一发现对E3SM陆面模块的开发具有直接意义。

---

## 目录
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## 地球系统模式：陆面-大气耦合

本周唯一一篇论文探讨了耦合地球系统模式开发中的一个基础性问题：陆面参数化方案的选择是否影响大尺度热带气候变率？若影响，机制是什么？Rajesh等人给出了明确的肯定答案——关键驱动因素不单是土壤水分记忆，而是耦合效率：即地面通量异常产生空间相干大气强迫的能力。通过对比Noah-MP与Noah 2.7.1在百年自由积分模拟中的表现（其他所有模块保持一致），他们清晰地分离出陆面效应。结果令人瞩目：Noah-MP重现了对照组完全缺失的亚马逊-太平洋遥相关，改善了ENSO空间结构，并减小了太平洋Walker环流偏差——这些均可追溯至热带森林在更好的地下水文表达支撑下的持续蒸散发。对致力于陆面模块开发（包括E3SM/ELM）的研究者而言，这项工作表明热带森林的次表层水分获取可能是影响气候模拟质量的一阶控制因子。

### Enhanced Land‐Surface Processes Sustain Evapotranspiration and Improve Tropical Climate Variability in a Coupled Earth System Model

**作者**：P. Rajesh, Rosimitha Panda, C. Gnanaseelan, A. Sharma, M. Kawsar, Bushra Y. Shaikh et al.

**期刊**：*Journal of Geophysical Research - Atmospheres* · **DOI**: [10.1029/2026jd047646](https://doi.org/10.1029/2026jd047646) · **被引**: 0

**匹配主题**: earth system model
{: .label .label-green }

> Land surface hydrological processes influence climate predictability through soil moisture persistence and coupling efficiency, the capacity of surface flux anomalies to generate spatially coherent atmospheric forcing at large scales. We examine coupling efficiency using century‐long free‐running simulations of a fully coupled Earth system model, comparing two configurations that differ only in land surface parameterizations. The Noah‐MP configuration differs from the Noah 2.7.1 control in subsurface hydrology, vegetation physiology, and surface‐layer exchange, and produces larger‐scale and more coherent atmospheric responses despite nearly identical soil moisture memory. Because every other model component is shared, the contrast isolates the effect of the land surface formulation. The Amazon–Pacific teleconnection is absent in the control but is reproduced closely with Noah‐MP. Drought composites with nearly equal rainfall show higher latent heat flux over tropical evergreen forests with accessible subsurface water with Noah‐MP than control. Over the Amazon, sustained evapotranspiration anomalies are accompanied by a Matsuno–Gill type response and a reduction in the Pacific Walker Circulation bias. The El Niño–Southern Oscillation (ENSO) spatial structure is also more realistic, with a stronger east–west sea surface temperature gradient. Atlantic Niño variability becomes less tied to ENSO, closer to the observed relationship. These results suggest that coupling efficiency, rather than soil moisture persistence alone, governs how strongly land surface processes influence large‐scale variability, and that a more realistic representation of land surface processes can strengthen that influence with potential implications for long‐term predictability.

---

## 统计信息

| 指标 | 数量 |
|:-----|-----:|
| 检索数据库数 | 2 |
| 检索主题数 | 16 |
| 获取论文总数 | 3 |
| 去重后 | 3 |
| LLM相关性筛选后 | 1 |
| 已拒绝（不相关或重复） | 2 |

**注**：本次运行中OpenAlex全程返回429限流错误，结果仅来自Semantic Scholar。

### 各期刊论文数

| 期刊 | 论文数 |
|:-----|------:|
| Journal of Geophysical Research - Atmospheres | 1 |

## 筛选标准

**主题关键词**: hydrology, hydrologic model, river, runoff, streamflow, reservoir, water management, flood, drought, seasonal, land surface model, climate change, hydropower, surface water, irrigation, earth system model

**数据库**: Semantic Scholar, OpenAlex

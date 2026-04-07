---
layout: default
title: "首页"
permalink: /zh/
nav_exclude: true
lang: zh
lang_link: /
---

# HydroSense — 智能论文采集

面向水文学与水资源研究的自动化文献追踪工具。HydroSense 自动从顶级期刊与学术数据库获取最新论文，进行筛选与组织，帮助研究人员紧跟领域前沿。

## 最新动态

### 每日采集

{% assign daily_posts = site.pages | where_exp: "page", "page.lang == 'zh'" | where_exp: "page", "page.categories contains 'daily-zh'" | sort: "date" | reverse %}
{% for post in daily_posts limit:5 %}
- **[{{ post.date | date: "%m月%-d日" }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

### 每周文献综述

{% assign weekly_posts = site.pages | where_exp: "page", "page.lang == 'zh'" | where_exp: "page", "page.categories contains 'weekly-zh'" | sort: "date" | reverse %}
{% for post in weekly_posts limit:5 %}
- **[{{ post.title }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## 关于 HydroSense

HydroSense 通过两种互补的工作模式监测水文学、气候科学与地球系统模拟领域的最新发表：

- **每日采集**：覆盖 11 种顶级期刊（Nature、Science、PNAS、GRL、Nature Water、Nature Climate Change 等），按主题关键词与领域分类自动筛选。
- **每周综述**：跨学术数据库进行关键词检索（不限期刊），并按主题方向进行综合分析。

每篇文章都经过 Claude 大语言模型的相关性评估与摘要生成，以减少关键词检索带来的误报。

## 主要功能

- **多源数据整合**：CrossRef、Semantic Scholar、OpenAlex 三大学术数据源协同检索
- **LLM 智能筛选**：Claude 模型评估论文与水文研究的相关性，并自动生成日报与周报综述
- **论文登记表**：跨越每日与每周流程的全局 DOI 登记，自动去重，并标记多源出现的"重要论文"
- **双语发布**：每篇报告同时发布中英文版本
- **自动推送**：日报自动同步至 X (Twitter) 等社交渠道

## 关注的研究方向

- 大尺度水文建模（E3SM、MOSART、ELM 等）
- 水库调度与水资源管理
- 河道汇流与径流模拟
- 陆面模型与地球系统模型
- 气候变化对水资源的影响
- 洪水与干旱预测
- 水力发电与灌溉系统
- 遥感水文与机器学习水文应用

## 数据来源

- **CrossRef**：期刊级别论文元数据
- **Semantic Scholar**：领域分类、摘要与关键词检索
- **OpenAlex**：补充摘要与关键词检索

**搜索：** 使用侧边栏中的搜索框，可按作者、期刊、关键词或主题查找论文。

---

*由 CrossRef、Semantic Scholar、OpenAlex 与 Claude 共同驱动*

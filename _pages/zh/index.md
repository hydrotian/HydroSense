---
layout: default
title: "首页"
nav_exclude: true
lang: zh
lang_link: /
---

# HydroSense - 智能论文采集

水文学与水资源研究的自动文献追踪。

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

## 关于

HydroSense 通过两种互补模式监测水文学、气候科学和地球系统模拟领域的发表文献：

- **每日采集**：11种顶级期刊（Nature、Science、GRL等），按主题相关性筛选
- **每周综述**：基于关键词搜索所有学术数据库，主题式综合分析

---

*由 CrossRef、Semantic Scholar、OpenAlex 和 Claude 驱动*

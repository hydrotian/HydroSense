---
layout: default
title: "十二月"
permalink: /zh/2022/december/
nav_exclude: true
lang: zh
lang_link: /2022/december/
---

# 2022年十二月

## 每日采集

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily-zh'" | where_exp: "p", "p.categories contains 'december'" | where_exp: "p", "p.categories contains '2022'" | sort: "date" | reverse %}
{% for post in daily %}
- **[{{ post.date | date: "%m月%-d日" }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## 每周文献综述

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly-zh'" | where_exp: "p", "p.categories contains 'december'" | where_exp: "p", "p.categories contains '2022'" | sort: "date" | reverse %}
{% for post in weekly %}
- **[{{ post.title }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

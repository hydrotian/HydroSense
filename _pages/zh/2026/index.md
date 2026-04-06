---
layout: default
title: "2026"
permalink: /zh/2026/
nav_exclude: true
lang: zh
---

# 2026

## 每日采集

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily-zh'" | sort: "date" | reverse %}
{% for post in daily limit:10 %}
- **[{{ post.date | date: "%m月%-d日" }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## 每周文献综述

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly-zh'" | sort: "date" | reverse %}
{% for post in weekly limit:10 %}
- **[{{ post.title }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

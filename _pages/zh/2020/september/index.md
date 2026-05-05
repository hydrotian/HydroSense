---
layout: default
title: "九月"
permalink: /zh/2020/september/
nav_exclude: true
lang: zh
lang_link: /2020/september/
---

# 2020年九月

## 每日采集

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily-zh'" | where_exp: "p", "p.categories contains 'september'" | sort: "date" | reverse %}
{% for post in daily %}
- **[{{ post.date | date: "%m月%-d日" }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## 每周文献综述

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly-zh'" | where_exp: "p", "p.categories contains 'september'" | sort: "date" | reverse %}
{% for post in weekly %}
- **[{{ post.title }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

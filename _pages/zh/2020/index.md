---
layout: default
title: "2020"
permalink: /zh/2020/
nav_exclude: true
lang: zh
lang_link: /2020/
---

# 2020

## 每日采集

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily-zh'" | where_exp: "p", "p.categories contains '2020'" | sort: "date" | reverse %}
{% for post in daily limit:10 %}
- **[{{ post.date | date: "%m月%-d日" }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## 每周文献综述

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly-zh'" | where_exp: "p", "p.categories contains '2020'" | sort: "date" | reverse %}
{% for post in weekly limit:10 %}
- **[{{ post.title }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

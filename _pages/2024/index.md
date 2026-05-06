---
layout: default
title: "2024"
has_children: true
nav_order: 1
permalink: /2024/
lang: en
lang_link: /zh/2024/
---

# 2024

## Daily Harvests

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily'" | where_exp: "p", "p.categories contains '2024'" | sort: "date" | reverse %}
{% for post in daily limit:10 %}
- **[{{ post.date | date: "%B %-d" }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## Weekly Literature Reviews

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly'" | where_exp: "p", "p.categories contains '2024'" | sort: "date" | reverse %}
{% for post in weekly limit:10 %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

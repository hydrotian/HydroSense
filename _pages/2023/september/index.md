---
layout: default
title: "September"
parent: "2023"
has_children: true
nav_order: 9
permalink: /2023/september/
lang: en
lang_link: /zh/2023/september/
---

# September 2023

## Daily Harvests

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily'" | where_exp: "p", "p.categories contains 'september'" | where_exp: "p", "p.categories contains '2023'" | sort: "date" | reverse %}
{% for post in daily %}
- **[{{ post.date | date: "%B %-d" }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## Weekly Literature Reviews

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly'" | where_exp: "p", "p.categories contains 'september'" | where_exp: "p", "p.categories contains '2023'" | sort: "date" | reverse %}
{% for post in weekly %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

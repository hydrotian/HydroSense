---
layout: default
title: "February"
parent: "2024"
has_children: true
nav_order: 2
permalink: /2024/february/
lang: en
lang_link: /zh/2024/february/
---

# February 2024

## Daily Harvests

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily'" | where_exp: "p", "p.categories contains 'february'" | where_exp: "p", "p.categories contains '2024'" | sort: "date" | reverse %}
{% for post in daily %}
- **[{{ post.date | date: "%B %-d" }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## Weekly Literature Reviews

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly'" | where_exp: "p", "p.categories contains 'february'" | where_exp: "p", "p.categories contains '2024'" | sort: "date" | reverse %}
{% for post in weekly %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

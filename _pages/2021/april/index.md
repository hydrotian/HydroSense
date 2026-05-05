---
layout: default
title: April
parent: "2021"
nav_order: 4
has_children: true
permalink: /2021/april/
lang: en
lang_link: /zh/2021/april/
---

# April 2021

## Daily Harvest

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily'" | where_exp: "p", "p.grand_parent == '2021'" | where_exp: "p", "p.parent == 'April'" | sort: "date" | reverse %}
{% for post in daily %}
- **[{{ post.date | date: "%b %-d" }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## Weekly Literature Review

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly'" | where_exp: "p", "p.grand_parent == '2021'" | where_exp: "p", "p.parent == 'April'" | sort: "date" | reverse %}
{% for post in weekly %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

{% assign monthly = site.pages | where_exp: "p", "p.categories contains 'monthly'" | where_exp: "p", "p.grand_parent == '2021'" | where_exp: "p", "p.parent == 'April'" | sort: "date" | reverse %}
{% if monthly.size > 0 %}
## Monthly Review

{% for post in monthly %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}
{% endif %}

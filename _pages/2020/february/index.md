---
layout: default
title: February
parent: "2020"
nav_order: 2
has_children: true
permalink: /2020/february/
lang: en
lang_link: /zh/2020/february/
---

# February 2020

## Daily Harvest

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily'" | where_exp: "p", "p.grand_parent == '2020'" | where_exp: "p", "p.parent == 'February'" | sort: "date" | reverse %}
{% for post in daily %}
- **[{{ post.date | date: "%b %-d" }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## Weekly Literature Review

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly'" | where_exp: "p", "p.grand_parent == '2020'" | where_exp: "p", "p.parent == 'February'" | sort: "date" | reverse %}
{% for post in weekly %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

{% assign monthly = site.pages | where_exp: "p", "p.categories contains 'monthly'" | where_exp: "p", "p.grand_parent == '2020'" | where_exp: "p", "p.parent == 'February'" | sort: "date" | reverse %}
{% if monthly.size > 0 %}
## Monthly Review

{% for post in monthly %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}
{% endif %}

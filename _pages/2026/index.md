---
layout: default
title: "2026"
nav_order: 3
has_children: true
---

# 2026

{% assign yearly = site.pages | where_exp: "p", "p.categories contains 'yearly'" | where_exp: "p", "p.parent == '2026'" | sort: "date" | reverse %}
{% if yearly.size > 0 %}
## Annual Review

{% for post in yearly %}
- [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
{% endif %}

## Daily Harvest

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily'" | where_exp: "p", "p.grand_parent == '2026'" | sort: "date" | reverse %}
{% for post in daily limit:10 %}
- [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

## Weekly Literature Review

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly'" | where_exp: "p", "p.grand_parent == '2026'" | sort: "date" | reverse %}
{% for post in weekly limit:10 %}
- [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}

{% assign monthly = site.pages | where_exp: "p", "p.categories contains 'monthly'" | where_exp: "p", "p.grand_parent == '2026'" | sort: "date" | reverse %}
{% if monthly.size > 0 %}
## Monthly Review

{% for post in monthly %}
- [{{ post.title }}]({{ post.url | relative_url }})
{% endfor %}
{% endif %}

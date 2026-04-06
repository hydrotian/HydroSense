---
layout: default
title: Home
nav_order: 1
lang: en
lang_link: /zh/
---

# HydroSense - Intelligent Paper Harvesting

Automated literature tracking for hydrology and water resources research.

## Recent Highlights

### Daily Harvest

{% assign daily_posts = site.pages | where_exp: "page", "page.categories contains 'daily'" | sort: "date" | reverse %}
{% for post in daily_posts limit:5 %}
- **[{{ post.date | date: "%b %-d" }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

### Weekly Literature Review

{% assign weekly_posts = site.pages | where_exp: "page", "page.categories contains 'weekly'" | sort: "date" | reverse %}
{% for post in weekly_posts limit:5 %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

{% assign monthly_posts = site.pages | where_exp: "page", "page.categories contains 'monthly'" | sort: "date" | reverse %}
{% if monthly_posts.size > 0 %}
### Monthly Review

{% for post in monthly_posts limit:5 %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}
{% endif %}

{% assign yearly_posts = site.pages | where_exp: "page", "page.categories contains 'yearly'" | sort: "date" | reverse %}
{% if yearly_posts.size > 0 %}
### Annual Review

{% for post in yearly_posts limit:5 %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}
{% endif %}

## About

HydroSense monitors publications in hydrology, climate science, and earth system modeling through two complementary modes:

- **Daily Harvest**: 11 top-tier journals (Nature, Science, GRL, etc.) filtered by topic relevance
- **Weekly Review**: Keyword-based search across all academic databases, synthesized thematically

**Search:** Use the search box in the sidebar to find papers by author names, journal names, keywords, or topics.

---

*Powered by CrossRef, Semantic Scholar, OpenAlex, and Claude*

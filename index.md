---
layout: default
title: Home
nav_order: 1
---

# HydroSense - Intelligent Paper Harvesting

Automated literature tracking for hydrology and water resources research.

## Recent Reports

Browse all reports using the sidebar navigation, organized by **Year → Month → Daily Reports**.

**Recent Highlights:**

{% assign all_posts = site.pages | where_exp: "page", "page.grand_parent != nil" | sort: "date" | reverse %}
{% for post in all_posts limit:10 %}
{% if post.title contains "Monthly Summary" %}
- 📊 [{{ post.title }}]({{ post.url | relative_url }})
{% else %}
- [{{ post.title }}]({{ post.url | relative_url }})
{% endif %}
{% endfor %}

## About

HydroSense monitors publications in hydrology, climate science, and earth system modeling through two complementary modes:

- **Daily Harvest**: 11 top-tier journals (Nature, Science, GRL, etc.) filtered by topic relevance
- **Weekly Review**: Keyword-based search across all academic databases, synthesized thematically

**Search:** Use the search box in the sidebar to find papers by author names, journal names, keywords, or topics.

---

*Powered by CrossRef, Semantic Scholar, OpenAlex, and Claude*

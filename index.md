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

HydroSense automatically monitors publications from top-tier and high-impact journals in hydrology, climate science, and earth system modeling.

**Search:** Use the search box in the sidebar to find papers by author names, journal names, keywords, or topics.

**Classification System:**
- **Part 1**: Top-tier journals (Nature, Science, GRL, etc.) matching specific hydrology topics
- **Part 2**: High-impact specialized journals (WRR, JoH, HESS) matching topics

**Tracked Journals:** 11 top-tier + 18 high-impact journals including Nature, Science, Water Resources Research, and more.

---

*Powered by CrossRef, Semantic Scholar, OpenAlex, and Gemini LLM*

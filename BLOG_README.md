# HydroSense Blog Site

This directory contains a Jekyll-based blog site that hosts daily and monthly paper harvest reports. The site uses the `jekyll-gitbook` theme for a clean, searchable, book-like interface.

## Quick Start

### Local Development

```bash
# Install dependencies
bundle install

# Serve locally (with live reload)
bundle exec jekyll serve

# Site available at: http://localhost:4000/hydrosense/
```

### Adding New Posts

Posts are organized by year and month in collection folders:

```
_posts_2025/
├── 01-January/
│   ├── 2025-01-03-daily-harvest.md
│   ├── 2025-01-04-daily-harvest.md
│   └── 2025-01-31-monthly-summary.md
└── 02-February/
    └── 2025-02-01-daily-harvest.md
```

## Post Templates

### Daily Harvest Report

```yaml
---
layout: post
title: "Daily Harvest - January 3, 2025"
date: 2025-01-03
categories: [daily, 2025, january]
tags: [hydrology, climate, water-resources]
toc: true
---

# Paper Harvest Report

**Date Range:** 2025-01-03 to 2025-01-03

## Summary
[Statistics and overview]

## Part 1: Top-Tier Journals + Topic Match
[Papers...]

## Part 2: High-Impact Journals + Topic Match
[Papers...]

## Part 3: Top-Tier Journals + Field Match
[Papers...]
```

### Monthly Summary

```yaml
---
layout: post
title: "Monthly Summary - January 2025"
date: 2025-01-31
categories: [monthly, 2025, january]
tags: [summary, trends, hydrology]
toc: true
---

# Monthly Summary - January 2025

## Overview
[Statistics and highlights]

## Key Themes & Trends
[Analysis...]

## Breakthrough Papers
[Notable papers...]
```

## Site Structure

### Key Files

- `_config.yml` - Jekyll configuration and theme settings
- `index.md` - Homepage
- `_pages/about.md` - About page
- `Gemfile` - Ruby dependencies

### Collections

Posts are organized into year-based collections:
- `_posts_2025/` - 2025 reports
- `_posts_2026/` - 2026 reports

Each collection has month subdirectories (01-January, 02-February, etc.)

## Features

### Search

Full-text search is built into the theme:
- Searches all content including abstracts
- Access via search box in sidebar
- Results highlight matching text

### Navigation

- Sidebar shows hierarchical post organization
- Year → Month → Individual reports
- Table of contents for long posts (auto-generated from headers)

### Mobile Responsive

Theme is fully responsive and works on mobile devices.

## Deployment

### GitHub Pages (Automatic)

The site deploys automatically via GitHub Actions on push to main branch:

1. Workflow defined in `.github/workflows/jekyll.yml`
2. Builds Jekyll site
3. Deploys to `https://hydrotian.github.io/hydrosense/`

### Manual Deployment Trigger

1. Go to GitHub Actions tab
2. Select "Deploy Jekyll site to Pages"
3. Click "Run workflow"

## Theme Documentation

This site uses the `jekyll-gitbook` theme:
- GitHub: https://github.com/sighingnow/jekyll-gitbook
- Demo: https://sighingnow.github.io/jekyll-gitbook/

### Theme Features Used

- Hierarchical sidebar navigation
- Full-text search with gitbook-plugin-search-pro
- Table of contents generation
- Clean, readable typography
- Code syntax highlighting

## Troubleshooting

### Build Errors

```bash
# Clear cache and rebuild
bundle exec jekyll clean
bundle exec jekyll build

# Check for syntax errors
bundle exec jekyll build --verbose
```

### Search Not Working

Ensure `search.enabled: true` in `_config.yml` and rebuild site.

### Posts Not Showing

1. Check front matter is valid YAML
2. Verify date format: `YYYY-MM-DD`
3. Ensure file is in correct collection folder
4. Rebuild site

### Local Server Issues

```bash
# Kill existing Jekyll servers
pkill -f jekyll

# Clear Gemfile.lock and reinstall
rm Gemfile.lock
bundle install
bundle exec jekyll serve
```

## Customization

### Colors and Styling

Create `_sass/custom.scss` to override theme styles.

### Sidebar Order

Edit `ordered_collections` in `_config.yml` to change collection order.

### Homepage Content

Edit `index.md` to customize homepage.

### Add New Pages

Create `.md` files in `_pages/` directory with appropriate front matter.

## Performance

### Search Performance

Full-text search indexes all content. If search becomes slow:
1. Consider disabling abstract indexing in search config
2. Paginate long posts
3. Use build-time search index optimization

### Build Time

With many posts, builds can be slow. Optimize by:
- Using incremental builds: `jekyll serve --incremental`
- Excluding unnecessary files in `_config.yml`
- Limiting development builds to recent posts

## Best Practices

### Post Naming

- Daily: `YYYY-MM-DD-daily-harvest.md`
- Monthly: `YYYY-MM-31-monthly-summary.md`
- Be consistent for automation

### Front Matter

Always include:
- `layout: post`
- `title: "Descriptive Title"`
- `date: YYYY-MM-DD`
- `categories: [type, year, month]`
- `tags: [relevant, keywords]`
- `toc: true` (for long posts)

### Content Organization

- Use H1 (`#`) for main sections
- Use H2 (`##`) and H3 (`###`) for subsections
- Table of contents auto-generates from headers
- Keep abstracts under 800 characters for readability

## Automation

The harvesting script (`scripts/harvest.py`) generates markdown reports. Future automation possibilities:

1. Automated daily harvesting via cron/GitHub Actions
2. Auto-commit new reports to repository
3. Monthly summary generation script
4. Email notifications for high-priority papers

See `scripts/` directory for harvesting tools.

---

**Questions?** See `CLAUDE.md` for detailed architecture documentation or open an issue on GitHub.

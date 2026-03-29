# HydroSense Blog Site

This directory contains a Jekyll-based blog site that hosts daily and monthly paper harvest reports. The site uses the `just-the-docs` theme with a custom light blue color scheme and automatic dark mode.

## Quick Start

### Local Development

```bash
# Install dependencies
bundle install

# Serve locally (with live reload)
bundle exec jekyll serve

# Site available at: http://localhost:4000/
```

### Adding New Posts

Posts are organized by year and month in the `_pages` folder:

```
_pages/
├── 2025/
│   ├── index.md              # Year landing page
│   ├── january/
│   │   ├── index.md          # Month landing page
│   │   ├── 2025-01-03-daily-harvest.md
│   │   └── 2025-01-31-monthly-summary.md
│   └── february/
│       ├── index.md
│       └── ...
└── 2026/
    └── ...
```

## Post Templates

### Daily Harvest Report

```yaml
---
layout: default
title: "January 03 - Daily Harvest"
parent: January
grand_parent: 2025
nav_order: 3
date: 2025-01-03
categories: [daily, 2025, january]
tags: [hydrology, paper-harvest, research]
---

# Paper Harvest Report

**Date Range:** 2025-01-03 to 2025-01-03

## Today's Highlights
[AI-generated summary]

## Part 1: Top-Tier Journals + Topic Match
[Papers...]

## Part 2: High-Impact Journals + Topic Match
[Papers...]

## Statistics
[Stats...]
```

### Monthly Summary

```yaml
---
layout: default
title: "January 31 - Monthly Summary"
parent: January
grand_parent: 2025
nav_order: 31
date: 2025-01-31
categories: [monthly, 2025, january]
tags: [summary, trends, hydrology]
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

### Pages Structure

Posts are organized in nested folders under `_pages/`:
- `_pages/YYYY/index.md` - Year landing page
- `_pages/YYYY/monthname/index.md` - Month landing page
- `_pages/YYYY/monthname/YYYY-MM-DD-daily-harvest.md` - Daily reports

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
3. Deploys to `https://hydrosense.simhydro.com`

### Manual Deployment Trigger

1. Go to GitHub Actions tab
2. Select "Deploy Jekyll site to Pages"
3. Click "Run workflow"

## Theme Documentation

This site uses the `just-the-docs` theme:
- GitHub: https://github.com/just-the-docs/just-the-docs
- Docs: https://just-the-docs.com/

### Theme Features Used

- Hierarchical sidebar navigation (parent/grand_parent/has_children)
- Full-text search including abstracts
- Custom color scheme (light blue)
- Automatic dark mode via CSS media query
- Clean, readable typography

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

Use `nav_order` in front matter to control page order in the sidebar.

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
- `layout: default`
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

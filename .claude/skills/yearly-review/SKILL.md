---
name: yearly-review
description: Run yearly keyword-based literature review for a specific year, synthesize findings into a comprehensive survey, generate Jekyll post, and commit. Use for backfilling historical coverage.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# Yearly Literature Review

Search academic databases by keywords for an entire year, synthesize findings into a comprehensive survey, generate a Jekyll blog post, and commit.

## Usage

The user should specify which year to review, e.g.:
- "Run yearly review for 2001"
- "Run yearly review for 2020"

## Workflow

### Step 1: Run the search

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python scripts/search.py --from-date YYYY-01-01 --to-date YYYY-12-31 --max-per-topic 100 --output-format json > /tmp/yearly_review_output.json 2>/tmp/yearly_review_log.txt
```

Note: `--max-per-topic 100` to get broader coverage for a full year. This will take longer due to API rate limits.

### Step 2: Read and evaluate the results

Read `/tmp/yearly_review_output.json`. Papers are sorted by citation count.

**Relevance evaluation** — same criteria as other reviews:

Relevant: hydrologic modeling, reservoir operations, river routing, water management, flood/drought, climate impacts on water, land surface models, earth system models, ML for water resources, remote sensing for hydrology.

Not relevant: pure atmospheric science, medical/pharma, marine biology, pure geology, social science without hydrology, crop science only.

Yearly reviews will have many papers. Be highly selective — focus on:
1. High citation counts (the most impactful papers of the year)
2. Papers from top-tier journals (Nature, Science, WRR, HESS, etc.)
3. Papers found by multiple search queries
4. Papers found in multiple databases
5. Landmark/seminal papers that introduced new methods or datasets

### Step 3: Check paper registry for duplicates

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python -c "
from scripts.registry import load_registry, is_duplicate, get_cross_references
reg = load_registry()
doi = 'PAPER_DOI_HERE'
print(f'Duplicate in yearly: {is_duplicate(reg, doi, \"yearly\")}')
print(f'Cross-refs: {get_cross_references(reg, doi, \"yearly\")}')
"
```

### Step 4: Synthesize thematically

Group the relevant papers into 5-10 themes. This is a comprehensive annual survey — write substantive synthesis for each theme:
- What were the year's major advances?
- What methods gained traction?
- What datasets or models were introduced?
- What controversies or open questions emerged?

Write a 2-3 paragraph executive summary of the year's most significant developments in hydrology and water resources.

### Step 5: Generate the Jekyll post

Create a markdown file at `_pages/YYYY/YYYY-yearly-review.md`:

```yaml
---
layout: default
title: "YYYY - Annual Literature Review"
parent: YYYY
nav_order: 0
date: YYYY-12-31
categories: [yearly, YYYY]
tags: [hydrology, literature-review, research, annual]
---
```

Use `nav_order: 0` so the yearly review appears at the top of the year's page, before any month.

Post content structure:
1. `# Annual Literature Review: YYYY` header
2. Summary: "**X** significant papers identified across **Y** topics"
3. `## Executive Summary` — comprehensive synthesis of the year
4. `## Theme 1: [Theme Title]` (repeat for each theme)
   - Multi-paragraph synthesis
   - Key papers listed with title, authors, journal, DOI, citation count
5. `## Year in Numbers` — statistics, top journals, top authors
6. `## Search Statistics` — databases searched, topics, dedup stats

Create year index page if it doesn't exist.

### Step 6: Register papers in registry

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python -c "
from scripts.registry import load_registry, save_registry, register_papers, register_run
reg = load_registry()
run_id = 'yearly-YYYY'
reg = register_run(reg, run_id, 'yearly', date='YYYY-12-31', year=YYYY, topics=['list', 'of', 'topics'])
papers = [{'doi': '...', 'title': '...', 'journal': '...'}]
reg = register_papers(reg, run_id, papers)
save_registry(reg)
"
```

### Step 7: Commit and create PR

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
git checkout -b yearly-review/YYYY
git add _pages/ data/paper_registry.json
git commit -m "Annual literature review - YYYY"
git push -u origin yearly-review/YYYY
gh pr create --title "Annual literature review - YYYY" --body "Comprehensive keyword-based literature review for YYYY."
```

## Important Notes

- Yearly reviews for older years (pre-2020) will surface well-cited, established papers. Citation count is the strongest quality signal here.
- S2 search uses year-level filtering natively, so it works well for full-year searches.
- OpenAlex supports exact date ranges, so it will correctly filter to the target year.
- For very productive years, the search may return hundreds of papers. Focus on the top 30-50 most impactful ones.
- Consider running yearly reviews in reverse chronological order (2025, 2024, ... 2001) to build up the registry progressively.

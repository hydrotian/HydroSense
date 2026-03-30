---
name: monthly-review
description: Run monthly keyword-based literature review for a specific month, synthesize findings thematically, generate Jekyll post, and commit. Use for backfilling recent history or monthly summaries.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# Monthly Literature Review

Search academic databases by keywords for a specific month, synthesize findings into a thematic review, generate a Jekyll blog post, and commit.

## Usage

The user should specify which month to review, e.g.:
- "Run monthly review for January 2025"
- "Run monthly review for 2024-06"

If no month is specified, default to the previous month.

## Workflow

### Step 1: Run the search

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python scripts/search.py --from-date YYYY-MM-01 --to-date YYYY-MM-DD --output-format json > /tmp/monthly_review_output.json 2>/tmp/monthly_review_log.txt
```

Where `YYYY-MM-DD` for `--to-date` is the last day of the target month.

### Step 2: Read and evaluate the results

Read `/tmp/monthly_review_output.json`. Papers are sorted by citation count.

**Relevance evaluation** — same criteria as weekly review:

Relevant: hydrologic modeling, reservoir operations, river routing, water management, flood/drought, climate impacts on water, land surface models, earth system models, ML for water resources, remote sensing for hydrology.

Not relevant: pure atmospheric science, medical/pharma, marine biology, pure geology, social science without hydrology, crop science only.

Filter to only relevant papers. Monthly reviews will have more papers than weekly — be selective. Prioritize:
1. Papers found by multiple search queries (`matched_queries` has 2+ entries)
2. Papers found in multiple databases (`source_databases` has 2+ entries)
3. Higher citation counts (especially important for historical months)
4. Papers from top-tier and high-impact journals

### Step 3: Check paper registry for duplicates

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python -c "
from scripts.registry import load_registry, is_duplicate, get_cross_references
reg = load_registry()
doi = 'PAPER_DOI_HERE'
print(f'Duplicate in monthly: {is_duplicate(reg, doi, \"monthly\")}')
print(f'Cross-refs: {get_cross_references(reg, doi, \"monthly\")}')
"
```

- **Skip** papers already covered in a previous monthly review for the same month
- **Include** papers also in daily/weekly harvests, but note the cross-reference

### Step 4: Synthesize thematically

Group the relevant papers into 4-8 themes (more than weekly since there are more papers). Write deeper synthesis paragraphs for each theme. Identify the month's most significant contributions and emerging trends.

### Step 5: Generate the Jekyll post

Create a markdown file at `_pages/YYYY/monthname/YYYY-MM-monthly-review.md`:

```yaml
---
layout: default
title: "MonthName YYYY - Monthly Review"
parent: MonthName
grand_parent: YYYY
nav_order: 32
date: YYYY-MM-01
categories: [monthly, YYYY, monthname]
tags: [hydrology, literature-review, research]
---
```

Use `nav_order: 32` so monthly reviews sort after all daily posts (which use day-of-month 1-31).

Post content structure:
1. `# Monthly Literature Review` header with month and year
2. Summary: "**X** relevant papers found across **Y** topics"
3. `## Executive Summary` — the overall synthesis for the month
4. `## Theme 1: [Theme Title]` (repeat for each theme)
   - Synthesis paragraph(s)
   - Key papers listed with title, authors, journal, DOI, citation count
   - Cross-references to daily/weekly harvests where applicable
5. `## Search Statistics` — databases searched, topics, dedup stats
6. `## Important Papers` — papers flagged as important in registry

Create year/month index pages if they don't exist.

### Step 6: Register papers in registry

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python -c "
from scripts.registry import load_registry, save_registry, register_papers, register_run
reg = load_registry()
run_id = 'monthly-YYYY-MM'
reg = register_run(reg, run_id, 'monthly', date='YYYY-MM-01', month='YYYY-MM', topics=['list', 'of', 'topics'])
papers = [{'doi': '...', 'title': '...', 'journal': '...'}]
reg = register_papers(reg, run_id, papers)
save_registry(reg)
"
```

### Step 7: Commit and create PR

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
git checkout -b monthly-review/YYYY-MM
git add _pages/ data/paper_registry.json
git commit -m "Monthly literature review - YYYY-MM"
git push -u origin monthly-review/YYYY-MM
gh pr create --title "Monthly literature review - YYYY-MM" --body "Keyword-based literature review for MonthName YYYY."
```

## Important Notes

- Monthly reviews will have significantly more papers than weekly. Be more selective — focus on the most impactful and relevant work.
- For historical months (pre-2025), citation counts are more meaningful as a quality signal.
- If a month has very few relevant papers, note this and consider whether the search terms need adjustment.

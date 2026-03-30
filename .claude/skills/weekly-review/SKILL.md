---
name: weekly-review
description: Run weekly keyword-based literature review across academic databases, synthesize findings thematically, generate Jekyll post, and commit. Use when running the weekly automated literature review.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# Weekly Literature Review

Search academic databases by keywords, synthesize findings into a thematic review, generate a Jekyll blog post, and commit.

## Workflow

### Step 1: Run the weekly review search

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python scripts/weekly_review.py --weeks-back 1 --output-format json > /tmp/weekly_review_output.json 2> /tmp/weekly_review_log.txt
```

### Step 2: Read and evaluate the results

Read `/tmp/weekly_review_output.json`. The papers are sorted by citation count (most cited first).

**Relevance evaluation** — same criteria as daily harvest:

Relevant: hydrologic modeling, reservoir operations, river routing, water management, flood/drought, climate impacts on water, land surface models, earth system models, ML for water resources, remote sensing for hydrology.

Not relevant: pure atmospheric science, medical/pharma, marine biology, pure geology, social science without hydrology, crop science only.

Filter to only relevant papers. Prioritize:
1. Papers found by multiple search queries (`matched_queries` has 2+ entries)
2. Papers found in multiple databases (`source_databases` has 2+ entries)
3. Higher citation counts
4. Papers from top-tier journals

### Step 3: Check paper registry for duplicates

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python -c "
from scripts.registry import load_registry, is_duplicate, get_cross_references
reg = load_registry()
doi = 'PAPER_DOI_HERE'
print(f'Duplicate in weekly: {is_duplicate(reg, doi, \"weekly\")}')
print(f'Cross-refs: {get_cross_references(reg, doi, \"weekly\")}')
"
```

- **Skip** papers already covered in a previous weekly review (same-type duplicate)
- **Include** papers also in daily harvests, but note the cross-reference
- Papers appearing in both daily and weekly sources are strong relevance signals

### Step 4: Synthesize thematically

Group the relevant papers into 3-6 themes. Do NOT write study-by-study summaries. Instead, synthesize across papers within each theme.

Example themes (adapt based on actual papers found):
- Large-scale hydrologic modeling advances
- Reservoir and water management
- Climate change impacts on water resources
- Machine learning applications in hydrology
- Flood and drought research
- Remote sensing for water resources

For each theme:
- Identify the key findings and trends across papers
- Note consensus and controversies
- Highlight the most impactful papers (high citations, top journals)
- Note methodological advances

Write a 1-2 paragraph executive summary of the week's most significant developments.

### Step 5: Generate the Jekyll post

Create a markdown file at `_pages/YYYY/monthname/YYYY-MM-DD-weekly-review.md`:

```yaml
---
layout: default
title: "Week NN - Literature Review"
parent: MonthName
grand_parent: YYYY
nav_order: DD
date: YYYY-MM-DD
categories: [weekly, YYYY, monthname]
tags: [hydrology, literature-review, research]
---
```

Post content structure:
1. `# Weekly Literature Review` header with date range and week number
2. Summary: "**X** relevant papers found across **Y** topics"
3. `## Executive Summary` — the overall synthesis
4. `## Theme 1: [Theme Title]` (repeat for each theme)
   - Synthesis paragraph(s)
   - Key papers listed with title, authors, journal, DOI, citation count
   - Cross-references to daily harvests where applicable
5. `## Papers by Topic Match` — table showing which topics each paper matched
6. `## Search Statistics` — databases searched, topics, dedup stats
7. `## Important Papers` — papers flagged as important in registry (appeared multiple times)

Create year/month index pages if they don't exist (same as daily harvest).

### Step 6: Register papers in registry

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python -c "
import datetime
from scripts.registry import load_registry, save_registry, register_papers, register_run
reg = load_registry()
week_num = datetime.date.today().isocalendar()[1]
run_id = f'weekly-YYYY-W{week_num:02d}'
reg = register_run(reg, run_id, 'weekly', date='YYYY-MM-DD', topics=['list', 'of', 'topics'])
papers = [{'doi': '...', 'title': '...', 'journal': '...'}]
reg = register_papers(reg, run_id, papers)
save_registry(reg)
"
```

### Step 7: Commit and create PR

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
git checkout -b weekly-review/YYYY-WNN
git add _pages/ data/paper_registry.json
git commit -m "Weekly literature review - YYYY-WNN"
git push -u origin weekly-review/YYYY-WNN
gh pr create --title "Weekly literature review - YYYY-WNN" --body "Automated weekly literature review across academic databases."
```

## Important Notes

- The weekly review complements the daily harvest: daily covers top-tier journals specifically, weekly covers all venues by keyword.
- Papers appearing in both are strong relevance signals — flag them prominently.
- Sort themes by significance/impact, not alphabetically.
- For the first run, the registry will be empty — no dedup needed, just register everything.
- If very few papers are found (<5), consider whether the search date range is too narrow or if it was a slow week. Note this in the post.

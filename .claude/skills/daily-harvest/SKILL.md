---
name: daily-harvest
description: Run daily paper harvest for top-tier journals, filter with LLM relevance, generate Jekyll post, and commit. Use when running the daily automated paper harvest or when the user asks to harvest today's papers.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# Daily Paper Harvest

Harvest papers from top-tier journals, evaluate relevance, generate a Jekyll blog post, and commit to the repository.

## Workflow

### Step 1: Run the harvest script

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python scripts/harvest.py --date $(date +%Y-%m-%d) --journals top-tier --output-format json > /tmp/harvest_output.json 2> /tmp/harvest_log.txt
```

If `--date` should be yesterday (common for daily runs since papers may not appear same-day):
```bash
python scripts/harvest.py --date $(date -v-1d +%Y-%m-%d) --journals top-tier --output-format json > /tmp/harvest_output.json 2> /tmp/harvest_log.txt
```

### Step 2: Read and evaluate the results

Read `/tmp/harvest_output.json`. For each paper in `papers.part1` and `papers.part2`:

**Relevance evaluation criteria** (evaluate each paper):

This is for a researcher focused on:
- Large-scale hydrologic modeling (E3SM, MOSART, ELM)
- Reservoir operations and water management
- River routing and streamflow simulation
- Land surface modeling and earth system modeling
- Climate change impacts on water resources
- Flood and drought prediction
- Hydropower and irrigation systems

**Relevant topics include:**
- Hydrologic/hydraulic modeling at any scale
- Reservoir operations, dam management
- River routing, streamflow, runoff modeling
- Water resources management and planning
- Flood/drought forecasting and analysis
- Climate change impacts on hydrology
- Land surface models, earth system models
- Remote sensing for hydrology
- Machine learning for water resources

**NOT relevant (reject):**
- Pure atmospheric science without hydrology connection
- Medical, biochemistry, or pharmaceutical studies
- Marine biology or deep ocean studies
- Pure geology without water connection
- Social science without technical hydrology content
- Agricultural studies focused only on crop science

For each paper, decide: **relevant** or **not relevant**. Keep only relevant papers.

### Step 3: Check paper registry for duplicates and cross-references

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python -c "
from scripts.registry import load_registry, is_duplicate, get_cross_references
reg = load_registry()
# Check each paper DOI
doi = 'PAPER_DOI_HERE'
print(f'Duplicate: {is_duplicate(reg, doi, \"daily\")}')
print(f'Cross-refs: {get_cross_references(reg, doi, \"daily\")}')
"
```

- Skip papers that are duplicates within daily harvests
- Note cross-references with weekly reviews (include them but mention the cross-ref)

### Step 4: Generate the daily summary

Write a 2-3 sentence summary of the day's highlights, focusing on the most interesting findings across the relevant papers.

### Step 5: Generate the Jekyll post

Create a markdown file at `_pages/YYYY/monthname/YYYY-MM-DD-daily-harvest.md` with this structure:

```yaml
---
layout: default
title: "MonthName DD - Daily Harvest"
parent: MonthName
grand_parent: YYYY
nav_order: DD
date: YYYY-MM-DD
categories: [daily, YYYY, monthname]
tags: [hydrology, paper-harvest, research]
---
```

Post content structure:
1. `# Paper Harvest Report` header with date range
2. Summary line: "**X** top-tier papers selected out of **Y** total publications"
3. `## Today's Highlights` — the AI-generated summary
4. `## Top-Tier Journal Papers` — each paper formatted with title, authors, journal, DOI, matched topics, abstract
5. `## Statistics` section with counts
6. `## Filtering Criteria` listing topics and fields

Create year index (`_pages/YYYY/index.md`) and month index (`_pages/YYYY/monthname/index.md`) if they don't exist. Use:
- Year nav_order: `year - 2023`
- Month nav_order: month number (1-12)
- Both need `has_children: true`

### Step 6: Register papers in registry

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python -c "
from scripts.registry import load_registry, save_registry, register_papers, register_run
reg = load_registry()
run_id = 'daily-YYYY-MM-DD'
reg = register_run(reg, run_id, 'daily', date='YYYY-MM-DD', papers_found=N)
papers = [{'doi': '...', 'title': '...', 'journal': '...'}]  # list of selected papers
reg = register_papers(reg, run_id, papers)
save_registry(reg)
"
```

### Step 7: Commit and create PR

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
git checkout -b daily-harvest/YYYY-MM-DD
git add _pages/ data/paper_registry.json
git commit -m "Daily harvest - YYYY-MM-DD"
git push -u origin daily-harvest/YYYY-MM-DD
gh pr create --title "Daily harvest - YYYY-MM-DD" --body "Automated daily paper harvest from top-tier journals."
```

## Important Notes

- If no relevant papers are found for a day, still create a post noting "No relevant papers found today" with statistics.
- Papers flagged as `important` in the registry (appeared in multiple sources) should be marked with a star or note in the post.
- Always check the harvest log (`/tmp/harvest_log.txt`) for errors before proceeding.

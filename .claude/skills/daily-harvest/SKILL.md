---
name: daily-harvest
description: Run daily paper harvest for top-tier journals, filter with LLM relevance, generate Jekyll post, and commit. Use when running the daily automated paper harvest or when the user asks to harvest today's papers.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# Daily Paper Harvest

Harvest papers from top-tier journals, evaluate relevance, generate a Jekyll blog post, and commit to the repository.

## Workflow

### Step 1: Determine the harvest date

Default: 8 days before the current date (papers need ~7 days to appear in Semantic Scholar).

If the user specifies a date, use that instead.

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
HARVEST_DATE=$(date -v-8d +%Y-%m-%d 2>/dev/null || date -d '8 days ago' +%Y-%m-%d)
python scripts/harvest.py --date $HARVEST_DATE --journals top-tier --output-format json > /tmp/harvest_output.json 2> /tmp/harvest_log.txt
```

On Linux (cloud), use `date -d '8 days ago'` instead of `date -v-8d`.

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

Create a markdown file at `_pages/YYYY/monthname/YYYY-MM-DD-daily-harvest.md`.

**You MUST follow this EXACT template. Do not deviate from this structure or formatting.**

Replace placeholders in `{{...}}` with actual values. Repeat the paper block for each paper. Use lowercase month name for directory and categories (e.g., `march`), title-case for `parent` and title (e.g., `March`).

```markdown
---
layout: default
title: "{{MonthName}} {{DD}} - Daily Harvest"
parent: {{MonthName}}
grand_parent: "{{YYYY}}"
nav_order: {{DD}}
date: {{YYYY-MM-DD}}
categories: [daily, {{YYYY}}, {{monthname}}]
tags: [hydrology, paper-harvest, research]
paper_count: {{N_selected}}
highlight: "{{One sentence tweet-style summary of the most notable finding}}"
---

# Paper Harvest Report
{: .no_toc }

**Date range**: {{MonthName}} {{DD}}, {{YYYY}}
{: .text-grey-dk-000 }

**{{N_selected}}** top-tier papers selected out of **{{N_total}}** total publications
{: .fs-5 .fw-300 }

## Today's Highlights

{{2-3 sentence AI-generated summary of the day's most notable findings}}

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## Top-Tier Journal Papers

### {{Paper Title}}

**Authors**: {{Author1, Author2, Author3 et al.}}

**Journal**: *{{Journal Name}}* · **DOI**: [{{DOI}}](https://doi.org/{{DOI}})

**Matched topics**: {{topic1, topic2}}
{: .label .label-green }

> {{Abstract text. Use the full abstract if available. If no abstract, write "Abstract not available."}}

---

{{...repeat the above block (### through ---) for each paper...}}

## Statistics

| Metric | Count |
|:-------|------:|
| Journals searched | {{N}} |
| Total papers fetched | {{N}} |
| Passed deterministic filter | {{N}} |
| After LLM relevance filtering | {{N_selected}} |
| Rejected (not relevant) | {{N_rejected}} |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| {{Journal Name}} | {{N}} |

## Filtering Criteria

**Topics**: {{comma-separated list of all TOPICS from harvest.py}}

**Fields**: {{comma-separated list of RELEVANT_FIELDS from harvest.py}}
```

**Critical formatting rules:**
- The `# Paper Harvest Report` header MUST have `{: .no_toc }` on the next line
- The date range line MUST have `{: .text-grey-dk-000 }` on the next line
- The paper count line MUST have `{: .fs-5 .fw-300 }` on the next line
- The Table of Contents section MUST be included exactly as shown
- Each paper's matched topics MUST have `{: .label .label-green }` on the next line
- Abstracts MUST be in blockquotes (lines starting with `> `)
- Papers MUST be separated by `---` horizontal rules
- Author list: if more than 6 authors, show first 6 then "et al."
- Tables use left-aligned text columns (`:-------`) and right-aligned number columns (`------:`)

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

### Step 7: Commit and push to main

Push directly to `main` — no branch, no PR.

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
git add _pages/ data/paper_registry.json
git commit -m "Daily harvest - YYYY-MM-DD"
git push origin main
```

If the push fails due to conflicts (e.g., another run pushed first), pull and retry:

```bash
git pull --rebase origin main
git push origin main
```

### Step 8: Post to X (Twitter)

After the push succeeds (so the website link is live), post a tweet summarizing the day's harvest. The tweet should:

- Start with paper count ("N papers today.")
- Highlight 1-2 key findings — make it compelling and specific
- End with the link to the post (X auto-shortens URLs to 23 chars via t.co, so the full URL is fine)
- Stay under 280 characters total

**Tweet format:**

```
N papers today. [1-2 sentence highlight of the most interesting findings, mentioning journal names in parentheses].

hydrosense.simhydro.com/YYYY/monthname/YYYY-MM-DD-daily-harvest
```

**Example (March 25):**

```
7 papers today. Extreme climate outcomes possible even at 2°C warming (Nature). Only 13.4% of land meets WMO precipitation monitoring standards (Nature).

hydrosense.simhydro.com/2026/march/2026-03-25-daily-harvest
```

**Post the tweet:**

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python scripts/post_tweet.py "YOUR_TWEET_TEXT_HERE"
```

If the tweet fails (missing credentials, API error), log the error but do not fail the overall workflow — the push is more important.

## Important Notes

- **If no relevant papers are found after LLM filtering, STOP. Do not create a post, do not commit, do not push, do not tweet. Just skip this day entirely.**
- Papers flagged as `important` in the registry (appeared in multiple sources) should be noted with "(Also featured in weekly review)" or similar.
- Always check the harvest log (`/tmp/harvest_log.txt`) for errors before proceeding.
- Default harvest date is 8 days ago because same-day papers often get S2 404s.

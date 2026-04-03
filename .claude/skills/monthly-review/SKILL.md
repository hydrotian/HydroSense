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

Write a 2-3 paragraph executive summary of the month's highlights.

### Step 5: Generate the Jekyll post

Create a markdown file at `_pages/YYYY/monthname/YYYY-MM-monthly-review.md`.

**You MUST follow this EXACT template. Do not deviate from this structure or formatting.**

Replace placeholders in `{{...}}` with actual values. Use lowercase month name for directory and categories, title-case for `parent` and title.

```markdown
---
layout: default
title: "{{MonthName}} {{YYYY}} - Monthly Review"
parent: {{MonthName}}
grand_parent: "{{YYYY}}"
nav_order: 38
date: {{YYYY-MM-01}}
categories: [monthly, {{YYYY}}, {{monthname}}]
tags: [hydrology, literature-review, research]
---

# Monthly Literature Review
{: .no_toc }

**{{MonthName}} {{YYYY}}**
{: .text-grey-dk-000 }

**{{N_selected}}** relevant papers found across **{{N_themes}}** themes
{: .fs-5 .fw-300 }

## Executive Summary

{{2-3 paragraph overview of the month's most significant developments and emerging trends}}

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## {{Theme 1 Title}}

{{Synthesis paragraph(s) weaving together findings from papers in this theme.}}

### {{Paper Title}}

**Authors**: {{Author1, Author2, Author3 et al.}}

**Journal**: *{{Journal Name}}* · **DOI**: [{{DOI}}](https://doi.org/{{DOI}}) · **Citations**: {{N}}

**Matched topics**: {{topic1, topic2}}
{: .label .label-green }

> {{Abstract text or brief description.}}

---

{{...repeat ### paper block for each paper in this theme...}}

## {{Theme 2 Title}}

{{...repeat the theme section for each theme...}}

---

## Statistics

| Metric | Count |
|:-------|------:|
| Databases searched | {{N}} |
| Topics searched | {{N}} |
| Total papers fetched | {{N}} |
| After deduplication | {{N}} |
| After LLM relevance filtering | {{N_selected}} |
| Rejected (not relevant) | {{N_rejected}} |

### Papers by journal

| Journal | Papers |
|:--------|-------:|
| {{Journal Name}} | {{N}} |

## Filtering Criteria

**Topics**: {{comma-separated list of search topics}}

**Databases**: Semantic Scholar, OpenAlex
```

**Critical formatting rules:**
- The `# Monthly Literature Review` header MUST have `{: .no_toc }` on the next line
- The month/year line MUST have `{: .text-grey-dk-000 }` on the next line
- The paper count line MUST have `{: .fs-5 .fw-300 }` on the next line
- The Table of Contents section MUST be included exactly as shown
- Each paper's matched topics MUST have `{: .label .label-green }` on the next line
- Abstracts MUST be in blockquotes (lines starting with `> `)
- Theme sections and papers are separated by `---` horizontal rules
- Author list: if more than 6 authors, show first 6 then "et al."
- Tables use left-aligned text columns (`:-------`) and right-aligned number columns (`------:`)

Use `nav_order: 38` so monthly reviews sort after daily posts (1-31) and weekly posts (33-37) in the sidebar.

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
git push origin main
```

If the push fails due to conflicts, pull and retry:

```bash
git pull --rebase origin main
git push origin main
```

## Important Notes

- **If no relevant papers are found after LLM filtering, STOP. Do not create a post, do not commit, do not push. Skip entirely.**
- Monthly reviews will have significantly more papers than weekly. Be more selective — focus on the most impactful and relevant work.
- For historical months (pre-2025), citation counts are more meaningful as a quality signal.
- If a month has very few relevant papers, note this and consider whether the search terms need adjustment.

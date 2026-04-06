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
python scripts/search.py --weeks-back 1 --output-format json > /tmp/weekly_review_output.json 2>/tmp/weekly_review_log.txt
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

Group the relevant papers into 3-6 themes. For each theme, write a synthesis paragraph that weaves together findings across papers — do NOT just summarize each paper individually.

Example themes (adapt based on actual papers found):
- Large-scale hydrologic modeling advances
- Reservoir and water management
- Climate change impacts on water resources
- Machine learning applications in hydrology
- Flood and drought research
- Remote sensing for water resources

Write a 2-3 sentence executive summary of the week's most significant developments.

### Step 5: Generate the Jekyll post

Create a markdown file at `_pages/YYYY/monthname/YYYY-MM-DD-weekly-review.md`.

**You MUST follow this EXACT template. Do not deviate from this structure or formatting.**

Replace placeholders in `{{...}}` with actual values. Use lowercase month name for directory and categories, title-case for `parent` and title.

```markdown
---
layout: default
title: "Week {{WW}} - Literature Review"
parent: {{MonthName}}
grand_parent: "{{YYYY}}"
nav_order: {{32 + week_of_month}}
date: {{YYYY-MM-DD}}
categories: [weekly, {{YYYY}}, {{monthname}}]
tags: [hydrology, literature-review, research]
paper_count: {{N_selected}}
highlight: "{{One sentence tweet-style summary of the week's most notable finding}}"
---

# Weekly Literature Review
{: .no_toc }

**Week {{WW}}** · {{MonthName}} {{start_day}}–{{end_day}}, {{YYYY}}
{: .text-grey-dk-000 }

**{{N_selected}}** relevant papers found across **{{N_themes}}** themes
{: .fs-5 .fw-300 }

## Executive Summary

{{2-3 sentence overview of the week's most significant developments across all themes}}

---

## Table of Contents
{: .no_toc .text-delta }

1. TOC
{:toc}

---

## {{Theme 1 Title}}

{{Synthesis paragraph weaving together the findings from papers in this theme. Discuss what the papers collectively reveal, note methodological trends, and highlight the most significant results. Reference specific papers by first author name.}}

### {{Paper Title}}

**Authors**: {{Author1, Author2, Author3 et al.}}

**Journal**: *{{Journal Name}}* · **DOI**: [{{DOI}}](https://doi.org/{{DOI}}) · **Citations**: {{N}}

**Matched topics**: {{topic1, topic2}}
{: .label .label-green }

> {{Abstract text or brief description if abstract not available.}}

---

{{...repeat ### paper block for each paper in this theme...}}

## {{Theme 2 Title}}

{{...repeat the theme section (## through paper blocks) for each theme...}}

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
- The `# Weekly Literature Review` header MUST have `{: .no_toc }` on the next line
- The week/date line MUST have `{: .text-grey-dk-000 }` on the next line
- The paper count line MUST have `{: .fs-5 .fw-300 }` on the next line
- The Table of Contents section MUST be included exactly as shown
- Each paper's matched topics MUST have `{: .label .label-green }` on the next line
- Abstracts MUST be in blockquotes (lines starting with `> `)
- Theme sections (##) are separated by `---` horizontal rules
- Papers within a theme are also separated by `---`
- Author list: if more than 6 authors, show first 6 then "et al."
- Tables use left-aligned text columns (`:-------`) and right-aligned number columns (`------:`)
- Papers that also appeared in daily harvests should note "(Also featured in daily harvest on YYYY-MM-DD)" after the matched topics label

**Nav order scheme** — so that sidebar groups daily and weekly posts separately:
- Daily posts use `nav_order: DD` (day of month, 1-31)
- Weekly posts use `nav_order: 32 + week_of_month` (33, 34, 35, etc.)
- Monthly review uses `nav_order: 38`
- `week_of_month` = 1 for the first weekly review in a month, 2 for the second, etc.

Create year/month index pages if they don't exist — use the same rich index format as described in the daily-harvest skill (with `paper_count` and `highlight` displayed for each entry). Chain `where_exp` calls — NEVER use `and` in Liquid filters.

### Step 5b: Generate the Chinese translation

Create a Chinese version at `_pages/zh/YYYY/monthname/YYYY-MM-DD-weekly-review.md`.

**Translation rules:**
- Translate ALL text to Chinese: headers, theme titles, synthesis paragraphs, labels, descriptions, highlights, abstracts, table headers
- Keep paper titles in ORIGINAL English (do not translate)
- Keep author names, journal names, DOIs, URLs unchanged
- Keep all kramdown directives and markdown formatting exactly the same

**Front matter for Chinese page:**
```yaml
---
layout: default
title: "第{{WW}}周 - 文献综述"
nav_exclude: true
lang: zh
lang_link: /YYYY/monthname/YYYY-MM-DD-weekly-review
date: {{YYYY-MM-DD}}
categories: [weekly-zh, {{YYYY}}, {{monthname}}]
tags: [hydrology, literature-review, research]
paper_count: {{N_selected}}
highlight: "{{Chinese translation of the English highlight}}"
---
```

**Key differences from English version:**
- `nav_exclude: true`, `lang: zh`, `lang_link` to English version
- `categories: [weekly-zh, ...]` — uses `weekly-zh` instead of `weekly`
- No `parent` or `grand_parent`

Also add `lang: en` and `lang_link: /zh/YYYY/monthname/YYYY-MM-DD-weekly-review` to the English version's front matter.

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

### Step 7: Commit and push to main

Push directly to `main` — no branch, no PR.

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
git add _pages/ data/paper_registry.json
git commit -m "Weekly literature review - YYYY-WNN"
git push origin main
```

If the push fails due to conflicts, pull and retry:

```bash
git pull --rebase origin main
git push origin main
```

## Important Notes

- **If no relevant papers are found after LLM filtering, STOP. Do not create a post, do not commit, do not push. Skip entirely.**
- The weekly review complements the daily harvest: daily covers top-tier journals specifically, weekly covers all venues by keyword.
- Papers appearing in both are strong relevance signals — flag them prominently.
- Sort themes by significance/impact, not alphabetically.
- For the first run, the registry will be empty — no dedup needed, just register everything.
- If very few papers are found (<5), consider whether the search date range is too narrow or if it was a slow week. Note this in the post.

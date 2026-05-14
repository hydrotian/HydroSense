---
name: weekly-review
description: Run weekly keyword-based literature review across academic databases, synthesize findings thematically, generate Jekyll post, and commit. Use when running the weekly automated literature review.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# Weekly Literature Review

Search academic databases by keywords, synthesize findings into a thematic review, generate a Jekyll blog post, and commit.

## Workflow

### Step 1: Run the weekly review search

The weekly search is shifted by 7 days to stay in sync with the daily harvest (which is shifted by 8 days). Default window: from 14 days ago to 7 days ago.

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
WEEKLY_FROM=$(date -v-14d +%Y-%m-%d 2>/dev/null || date -d '14 days ago' +%Y-%m-%d)
WEEKLY_TO=$(date -v-7d  +%Y-%m-%d 2>/dev/null || date -d '7 days ago'  +%Y-%m-%d)
python scripts/search.py --from-date $WEEKLY_FROM --to-date $WEEKLY_TO --output-format json > /tmp/weekly_review_output.json 2>/tmp/weekly_review_log.txt
```

On Linux (cloud), use the `date -d '...'` form. If the user specifies an explicit `--from-date`/`--to-date`, use those instead.

**Important:** The "Week NN" label in the post title and body MUST be derived from the **data date range** (specifically the ISO week number of `WEEKLY_FROM`), NOT from today. The post is named after the week of papers it reviews, not the week it was generated. Compute it once and reuse:

```bash
WEEK_NUM=$(python -c "import datetime; d=datetime.date.fromisoformat('$WEEKLY_FROM'); print(f'{d.isocalendar()[1]:02d}')")
```

### Step 2: Read and evaluate the results

Read `/tmp/weekly_review_output.json`. Papers are pre-filtered, sorted, and capped by `search.py`:

- An ISSN blocklist removes mega-journals and low-bar venues (MDPI *Water*/*Sustainability*/*Hydrology*/etc., PLOS ONE, Heliyon, IEEE Access, …) — see `ISSN_BLOCKLIST` in `scripts/search.py`.
- Papers are sorted by topic-hit count + database-hit count (citations are only a tiebreaker for recent searches; for retrofit searches >365 days old the script auto-switches to citation-first).
- By default, search.py outputs all papers (no cap). The LLM reads the full list and selects the most relevant ones.

**Relevance evaluation** — narrower than daily harvest. The weekly review intentionally stays focused on the user's core hydrology / ESM-modeling work and excludes the adjacent areas the daily harvest accepts. The reasoning: daily harvest is constrained to top-tier journals so the broader net is manageable, but the weekly keyword search hits ALL journals and would be flooded by adjacent-area papers.

Relevant: hydrologic modeling, reservoir operations, river routing, water management, flood/drought, climate impacts on water, land surface models, earth system models, ML for water resources, remote sensing for hydrology.

Not relevant: pure atmospheric science, medical/pharma, marine biology, pure geology, social science without hydrology, crop science only.

**Excluded from weekly review (even though daily harvest accepts them):**
- Ocean / coastal / land-ocean coupling papers (estuaries, river plumes, marine heatwaves, ocean BGC) — keep these in daily harvest only
- Paleohydrology / Quaternary geology / fluvial geomorphology / river-network evolution / OSL dating / paleo-ESM — keep these in daily harvest only

Filter to only relevant papers. **Select up to 50 papers maximum** for the final post. Prioritization depends on whether this is a recent or retrofit search:

**Recent searches (≤6 months old):** Citation counts are noise — prioritize by:
1. Papers found by multiple search queries (`matched_queries` has 2+ entries)
2. Papers found in multiple databases (`source_databases` has 2+ entries)
3. Papers from well-known journals
4. Citation count (tiebreaker only)

**Retrofit searches (>6 months old, e.g. backfill runs):** Citation counts are meaningful and should be a primary factor — prioritize by:
1. Higher citation counts — the field has had time to react, highly cited papers are proven important
2. Papers found by multiple search queries (`matched_queries` has 2+ entries)
3. Papers found in multiple databases (`source_databases` has 2+ entries)
4. Papers from well-known journals

Check the `--from-date` / `--to-date` passed to search.py to determine which mode applies.

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
title: "Week {{WW}} ({{StartMonth}} {{start_day}} - {{EndMonth}} {{end_day}}), {{N_selected}} papers"
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

**Week {{WW}}** · {{StartMonth}} {{start_day}}–{{EndMonth}} {{end_day}}, {{YYYY}}
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

Create year/month index pages if they don't exist — use the same rich index format as described in the daily-harvest skill (with `paper_count` and `highlight` displayed for each entry). Chain `where_exp` calls — NEVER use `and` in Liquid filters. Always set explicit `permalink: /YYYY/` and `permalink: /YYYY/monthname/` on these index pages — without them, Jekyll generates `/_pages/YYYY/` URLs that break the language toggle.

### Step 5b: Generate the Chinese translation (MANDATORY — DO NOT SKIP)

**This step is required, not optional.** Every English post MUST have a Chinese counterpart. The site has a language toggle that hides itself when no Chinese version exists, so skipping this step results in a broken bilingual experience. You are not done with the post until both language versions exist on disk.

Create a Chinese version at `_pages/zh/YYYY/monthname/YYYY-MM-DD-weekly-review.md`.

**Translation rules:**
- Translate ALL text to Chinese: headers, theme titles, synthesis paragraphs, labels, descriptions, highlights, abstracts, table headers
- Keep paper titles in ORIGINAL English (do not translate)
- Keep author names, journal names, DOIs, URLs unchanged
- **Keep matched topic values in ORIGINAL English** (e.g. `**匹配主题**: hydrology, streamflow, flood` — never `水文学、水流量、洪水`). Topics come from the search keyword list and must stay in English so they remain searchable and consistent across languages. Only the label `**匹配主题**:` itself is translated.
- Keep all kramdown directives and markdown formatting exactly the same

**Front matter for Chinese page:**
```yaml
---
layout: default
title: "第{{WW}}周（{{StartMonthCN}}{{start_day}}日 - {{EndMonthCN}}{{end_day}}日），{{N_selected}}篇"
nav_order: {{32 + week_of_month}}
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

Also update the English version's front matter to add:
- `lang: en`
- `lang_link: /zh/YYYY/monthname/YYYY-MM-DD-weekly-review`

These two fields are what the site's language toggle reads to find the counterpart page. Without them the toggle falls back to URL guessing and may fail.

**Create Chinese year and month index pages if they don't exist** at `_pages/zh/YYYY/index.md` and `_pages/zh/YYYY/monthname/index.md`. The Chinese index files do NOT use Just-the-Docs `parent`/`has_children` navigation (zh pages are excluded from the sidebar via `nav_exclude: true`); they use a `permalink` instead.

**Chinese year index template** (`_pages/zh/YYYY/index.md`):
```markdown
---
layout: default
title: "YYYY"
permalink: /zh/YYYY/
nav_exclude: true
lang: zh
lang_link: /YYYY/
---

# YYYY

## 每日采集

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily-zh'" | sort: "date" | reverse %}
{% for post in daily limit:10 %}
- **[{{ post.date | date: "%m月%-d日" }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## 每周文献综述

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly-zh'" | sort: "date" | reverse %}
{% for post in weekly limit:10 %}
- **[{{ post.title }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}
```

**Chinese month index template** (`_pages/zh/YYYY/monthname/index.md`):
```markdown
---
layout: default
title: "{{MonthChinese}}"
permalink: /zh/YYYY/monthname/
nav_exclude: true
lang: zh
lang_link: /YYYY/monthname/
---

# YYYY年{{MonthChinese}}

## 每日采集

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily-zh'" | where_exp: "p", "p.categories contains 'monthname'" | sort: "date" | reverse %}
{% for post in daily %}
- **[{{ post.date | date: "%m月%-d日" }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## 每周文献综述

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly-zh'" | where_exp: "p", "p.categories contains 'monthname'" | sort: "date" | reverse %}
{% for post in weekly %}
- **[{{ post.title }}，{{ post.paper_count }} 篇]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}
```

`{{MonthChinese}}` mapping: January→一月, February→二月, March→三月, April→四月, May→五月, June→六月, July→七月, August→八月, September→九月, October→十月, November→十一月, December→十二月.

**Verification before committing.** Run this check and confirm both files exist and the English version has `lang_link` populated. Do not proceed to the commit step until this passes:

```bash
ls -la _pages/YYYY/monthname/YYYY-MM-DD-weekly-review.md \
       _pages/zh/YYYY/monthname/YYYY-MM-DD-weekly-review.md \
       _pages/zh/YYYY/monthname/index.md \
       _pages/zh/YYYY/index.md
grep -q "^lang_link:" _pages/YYYY/monthname/YYYY-MM-DD-weekly-review.md \
  && echo "OK: English has lang_link" \
  || echo "MISSING lang_link on English file — fix before commit"
```

### Step 6: Register papers in registry

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
python -c "
import datetime
from scripts.registry import load_registry, save_registry, register_papers, register_run
reg = load_registry()
week_num = datetime.date.fromisoformat('WEEKLY_FROM_DATE').isocalendar()[1]
run_id = f'weekly-YYYY-W{week_num:02d}'
reg = register_run(reg, run_id, 'weekly', date='YYYY-MM-DD', topics=['list', 'of', 'topics'])
papers = [{'doi': '...', 'title': '...', 'journal': '...'}]
reg = register_papers(reg, run_id, papers)
save_registry(reg)
"
```

### Step 7: Commit and push to main

The post MUST land on `main` for GitHub Pages to publish it. The repo has a "human-touch-only" ruleset that blocks direct pushes to `main` for non-admin actors; only `hydrotian` has bypass. In a cloud worktree (working branch is `claude/...`, author `Claude <noreply@anthropic.com>`), a plain `git push origin main` is rejected and the post gets stranded on the session branch. To handle both local and cloud cases, commit on the current branch, then either direct-push (local admin) or push-branch + open-and-merge-PR (cloud).

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
git add _pages/ data/paper_registry.json
git commit -m "Weekly literature review - YYYY-WNN"

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)

if [ "$CURRENT_BRANCH" = "main" ]; then
  if git push origin main 2>&1 | tee /tmp/push.log | grep -q "rejected\|protected\|rule violations"; then
    echo "Direct push to main rejected. Falling back to PR path." >&2
    BRANCH="weekly-review/YYYY-WNN"
    git push origin "main:$BRANCH"
  else
    BRANCH=""
  fi
else
  BRANCH="$CURRENT_BRANCH"
  git push origin "$CURRENT_BRANCH"
fi

if [ -n "$BRANCH" ]; then
  PR_URL=$(gh pr create --base main --head "$BRANCH" \
    --title "Weekly literature review - YYYY-WNN" \
    --body "Automated weekly review. Auto-merging via skill.")
  echo "PR: $PR_URL"
  gh pr merge "$PR_URL" --squash --auto --delete-branch || \
    gh pr merge "$PR_URL" --squash --delete-branch || \
    echo "Auto-merge failed — PR left open for manual merge."
fi
```

If the push said "rejected" due to upstream changes (another run pushed first), pull-rebase and retry:

```bash
git pull --rebase origin main
git push origin main   # or re-push the session branch
```

## Important Notes

- **If no relevant papers are found after LLM filtering**, write a minimal stub post (EN+ZH) so the week is recorded as processed and the backfill loop can advance past it. Use `paper_count: 0`, set `highlight` to "No relevant papers found this week.", omit the Table of Contents and all theme/paper/statistics sections, and replace the body with a one-line "No relevant papers found for week {{WW}}." Skip `register_papers` but still call `register_run` so the registry knows the week was searched. Commit and push as usual. Do NOT post a tweet (weekly reviews don't tweet anyway).
- The weekly review complements the daily harvest: daily covers top-tier journals specifically, weekly covers all venues by keyword.
- Papers appearing in both are strong relevance signals — flag them prominently.
- Sort themes by significance/impact, not alphabetically.
- For the first run, the registry will be empty — no dedup needed, just register everything.
- If very few papers are found (<5), consider whether the search date range is too narrow or if it was a slow week. Note this in the post.

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
- Coastal and estuarine processes where freshwater meets the ocean (collaborates with ocean scientists)
- Paleohydrology, Quaternary geology, fluvial geomorphology, river-network evolution (background area, still actively interested — especially where it connects to modern river routing and Earth-system modeling)

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
- **Coastal and ocean processes connected to land/freshwater**: estuaries, river plumes, freshwater discharge to the ocean, coastal circulation, sea-level rise impacts on coasts, marine heatwaves, ocean biogeochemistry (especially nutrient/carbon delivery from rivers), coupled land-ocean modeling
- **Paleohydrology, Quaternary geology, and landscape evolution**: paleoclimate / paleohydrologic reconstructions (Holocene, Pleistocene, Quaternary), drainage network and river-network formation/evolution, river capture, fluvial geomorphology, river terraces, loess–paleosol sequences, luminescence (OSL) dating of fluvial/aeolian deposits, paleo-glacial extents, deep-time Earth System Model simulations (paleo-ESM, e.g. Holocene, LGM, mid-Pliocene)

**NOT relevant (reject):**
- Pure atmospheric science without hydrology connection
- Medical, biochemistry, or pharmaceutical studies
- Deep-ocean / open-ocean dynamics with no land or freshwater connection (e.g. abyssal circulation, mid-ocean ridge processes, pure marine biology of pelagic species)
- Pure geology without water connection
- Social science without technical hydrology content
- Agricultural studies focused only on crop science

**Note on ocean papers:** The user collaborates with ocean scientists and is interested in land-ocean coupling. Accept ocean papers that have a clear connection to coasts, estuaries, freshwater inputs, river-borne nutrients/carbon, marine heatwaves, or coupled ESM-ocean processes. Only reject ocean papers that are purely about deep-sea or open-ocean dynamics with no land/freshwater linkage.

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
title: "{{Mon}} {{DD}}, {{N_selected}} papers"
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

{% if hero_image_url is non-empty %}
![Figure]({{hero_image_url}})
{% endif %}

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
- If a paper has a non-empty `hero_image_url` in the JSON, embed it as `![Figure](URL)` between the matched-topics label and the abstract blockquote. Omit the image line entirely if the field is empty.
- Papers MUST be separated by `---` horizontal rules
- Author list: if more than 6 authors, show first 6 then "et al."
- Tables use left-aligned text columns (`:-------`) and right-aligned number columns (`------:`)

Create year index (`_pages/YYYY/index.md`) and month index (`_pages/YYYY/monthname/index.md`) if they don't exist.

**Year index template** (`_pages/YYYY/index.md`):
```markdown
---
layout: default
title: "YYYY"
nav_order: {{year - 2023}}
has_children: true
permalink: /YYYY/
---

# YYYY

{% assign yearly = site.pages | where_exp: "p", "p.categories contains 'yearly'" | where_exp: "p", "p.parent == 'YYYY'" | sort: "date" | reverse %}
{% if yearly.size > 0 %}
## Annual Review

{% for post in yearly %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}
{% endif %}

## Daily Harvest

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily'" | where_exp: "p", "p.grand_parent == 'YYYY'" | sort: "date" | reverse %}
{% for post in daily limit:10 %}
- **[{{ post.date | date: "%b %-d" }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## Weekly Literature Review

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly'" | where_exp: "p", "p.grand_parent == 'YYYY'" | sort: "date" | reverse %}
{% for post in weekly limit:10 %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

{% assign monthly = site.pages | where_exp: "p", "p.categories contains 'monthly'" | where_exp: "p", "p.grand_parent == 'YYYY'" | sort: "date" | reverse %}
{% if monthly.size > 0 %}
## Monthly Review

{% for post in monthly %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}
{% endif %}
```

**Month index template** (`_pages/YYYY/monthname/index.md`):
```markdown
---
layout: default
title: {{MonthName}}
parent: "YYYY"
nav_order: {{month_number}}
has_children: true
permalink: /YYYY/monthname/
---

# {{MonthName}} YYYY

## Daily Harvest

{% assign daily = site.pages | where_exp: "p", "p.categories contains 'daily'" | where_exp: "p", "p.grand_parent == 'YYYY'" | where_exp: "p", "p.parent == 'MonthName'" | sort: "date" | reverse %}
{% for post in daily %}
- **[{{ post.date | date: "%b %-d" }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

## Weekly Literature Review

{% assign weekly = site.pages | where_exp: "p", "p.categories contains 'weekly'" | where_exp: "p", "p.grand_parent == 'YYYY'" | where_exp: "p", "p.parent == 'MonthName'" | sort: "date" | reverse %}
{% for post in weekly %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}

{% assign monthly = site.pages | where_exp: "p", "p.categories contains 'monthly'" | where_exp: "p", "p.grand_parent == 'YYYY'" | where_exp: "p", "p.parent == 'MonthName'" | sort: "date" | reverse %}
{% if monthly.size > 0 %}
## Monthly Review

{% for post in monthly %}
- **[{{ post.title }}, {{ post.paper_count }} papers]({{ post.url | relative_url }})** — {{ post.highlight }}
{% endfor %}
{% endif %}
```

**Critical Liquid rules:**
- NEVER use `and` in `where_exp` — chain multiple `where_exp` calls instead (Liquid 4.0.4 on GitHub Pages does not support `and`)
- Always quote `"YYYY"` in front matter for `grand_parent` and `parent` on year index — YAML parses unquoted numbers as integers, breaking Liquid string comparisons
- Always set explicit `permalink:` on year and month index pages (`/YYYY/` and `/YYYY/monthname/`). Without it, Jekyll's default permalink includes `_pages/` in the URL (e.g. `/_pages/2026/`), breaking the language toggle target and the zh sidebar rewrites.

### Step 5b: Generate the Chinese translation (MANDATORY — DO NOT SKIP)

**This step is required, not optional.** Every English post MUST have a Chinese counterpart. The site has a language toggle that hides itself when no Chinese version exists, so skipping this step results in a broken bilingual experience. You are not done with the post until both language versions exist on disk.

Create a Chinese version at `_pages/zh/YYYY/monthname/YYYY-MM-DD-daily-harvest.md`.

**Translation rules:**
- Translate ALL text to Chinese: headers, labels, descriptions, highlights, abstracts, table headers, statistics labels
- Keep paper titles in ORIGINAL English (do not translate)
- Keep author names, journal names, DOIs, URLs unchanged
- **Keep matched topic values in ORIGINAL English** (e.g. `**匹配主题**: climate change, river` — never `气候变化, 河流`). Topics come from the harvester's English keyword list and must stay in English so they remain searchable and consistent across languages. Only the label `**匹配主题**:` itself is translated.
- Keep the topic list under "筛选标准" / Filtering Criteria in ORIGINAL English (the full keyword list from harvest.py)
- Keep all kramdown directives (`{: .no_toc}`, `{: .label .label-green}`, etc.) exactly the same
- Keep all markdown formatting (bold, blockquotes, tables, `---` rules) the same
- Keep hero images (`![Figure](URL)`) exactly the same as the English version — same URL, same placement

**Front matter for Chinese page:**
```yaml
---
layout: default
title: "{{M}}月{{DD}}日，{{N_selected}}篇"
nav_exclude: true
lang: zh
lang_link: /YYYY/monthname/YYYY-MM-DD-daily-harvest
date: {{YYYY-MM-DD}}
categories: [daily-zh, {{YYYY}}, {{monthname}}]
tags: [hydrology, paper-harvest, research]
paper_count: {{N_selected}}
highlight: "{{Chinese translation of the English highlight}}"
---
```

**Key differences from English version:**
- `nav_exclude: true` — Chinese pages don't appear in sidebar navigation
- `lang: zh` and `lang_link` pointing to the English version URL
- `categories: [daily-zh, ...]` — uses `daily-zh` instead of `daily` to avoid mixing with English Liquid queries
- No `parent` or `grand_parent` (not in nav hierarchy)

Also update the English version's front matter to add:
- `lang: en`
- `lang_link: /zh/YYYY/monthname/YYYY-MM-DD-daily-harvest`

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
ls -la _pages/YYYY/monthname/YYYY-MM-DD-daily-harvest.md \
       _pages/zh/YYYY/monthname/YYYY-MM-DD-daily-harvest.md \
       _pages/zh/YYYY/monthname/index.md \
       _pages/zh/YYYY/index.md
grep -q "^lang_link:" _pages/YYYY/monthname/YYYY-MM-DD-daily-harvest.md \
  && echo "OK: English has lang_link" \
  || echo "MISSING lang_link on English file — fix before commit"
```

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

The post MUST land on `main` for GitHub Pages to publish it. The repo has a "human-touch-only" ruleset that blocks direct pushes to `main` for non-admin actors; only `hydrotian` has bypass. If you're running in a cloud worktree (your git identity is `Claude <noreply@anthropic.com>` and the working branch is `claude/...`), a direct `git push origin main` will be rejected, and the post will be stranded on the session branch with no PR. **This silently broke 8 daily/weekly posts in late April / early May 2026** — tweets went out with 404 links. Do not let that happen again.

**Always commit on a real branch first, then push that branch to origin and merge it into main via PR.** The PR + merge path works whether or not the actor has bypass: if bypass exists, the merge auto-succeeds; if not, the PR sits and the user is alerted (and crucially, no tweet is sent).

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense

# Stage and commit on the current branch (which may be `main` locally or a `claude/...` session branch in cloud)
git add _pages/ data/paper_registry.json
git commit -m "Daily harvest - YYYY-MM-DD"

CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
COMMIT_SHA=$(git rev-parse HEAD)

if [ "$CURRENT_BRANCH" = "main" ]; then
  # Local-laptop path: try direct push (admin bypass)
  if git push origin main 2>&1 | tee /tmp/push.log | grep -q "rejected\|protected\|rule violations"; then
    echo "Direct push to main rejected. Falling back to PR path." >&2
    git push origin "main:daily-harvest/YYYY-MM-DD"
    BRANCH_FOR_PR="daily-harvest/YYYY-MM-DD"
  else
    BRANCH_FOR_PR=""  # already on main, done
  fi
else
  # Cloud session-branch path: push the session branch and open a PR
  git push origin "$CURRENT_BRANCH"
  BRANCH_FOR_PR="$CURRENT_BRANCH"
fi

if [ -n "$BRANCH_FOR_PR" ]; then
  PR_URL=$(gh pr create --base main --head "$BRANCH_FOR_PR" \
    --title "Daily harvest - YYYY-MM-DD" \
    --body "Automated daily harvest. Auto-merging via skill.")
  echo "PR: $PR_URL"
  # Try to auto-merge — works if the actor has bypass; otherwise the PR sits for human review
  gh pr merge "$PR_URL" --squash --auto --delete-branch || \
    gh pr merge "$PR_URL" --squash --delete-branch || \
    { echo "Auto-merge failed — PR left open for manual merge."; SKIP_TWEET=1; }
fi
```

If you pushed and the push said "rejected" due to upstream changes (someone else pushed first), pull-rebase and retry:

```bash
git pull --rebase origin main
git push origin main   # or re-push the session branch
```

### Step 7b: Verify the post is live before tweeting

**This is non-negotiable.** Past failures shipped tweets pointing at 404 URLs because the skill assumed push → URL live. Verify with curl. If the URL isn't live (or `SKIP_TWEET=1` from a failed merge), do not tweet.

```bash
URL="https://hydrosense.simhydro.com/YYYY/monthname/YYYY-MM-DD-daily-harvest"
# Wait up to ~5 min for GitHub Pages to rebuild and serve the new post.
# (Pages typically rebuilds in 60-120s; we retry a few times.)
for attempt in 1 2 3 4 5 6; do
  CODE=$(curl -s -o /dev/null -w "%{http_code}" "$URL")
  echo "attempt $attempt: HTTP $CODE"
  if [ "$CODE" = "200" ]; then
    POST_LIVE=1
    break
  fi
  sleep 45
done

if [ "${POST_LIVE:-0}" != "1" ] || [ "${SKIP_TWEET:-0}" = "1" ]; then
  echo "Post URL not live — skipping tweet to avoid posting a 404 link."
  exit 0
fi
```

### Step 8: Post to X (Twitter)

Only run this step if Step 7b confirmed the URL is live. The tweet should:

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

- **If no relevant papers are found after LLM filtering**, still create a minimal "no papers" stub post (English + Chinese) so the day is recorded as processed. Use `paper_count: 0`, set `highlight` to a one-line note like "No relevant papers from top-tier journals on this date.", include the same Statistics table (with `After LLM relevance filtering: 0`), and **omit the entire "Top-Tier Journal Papers" section and Table of Contents** (no papers to list). Skip the registry `register_papers` call but still call `register_run` so the day is logged. Commit and push as usual, **but DO NOT post a tweet** for no-paper days.
- Papers flagged as `important` in the registry (appeared in multiple sources) should be noted with "(Also featured in weekly review)" or similar.
- Always check the harvest log (`/tmp/harvest_log.txt`) for errors before proceeding.
- Default harvest date is 8 days ago because same-day papers often get S2 404s.

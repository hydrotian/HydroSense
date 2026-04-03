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
grand_parent: {{YYYY}}
nav_order: {{DD}}
date: {{YYYY-MM-DD}}
categories: [daily, {{YYYY}}, {{monthname}}]
tags: [hydrology, paper-harvest, research]
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

### Step 7: Commit and create PR

```bash
cd /Users/zhou014/Local_Drive/Git_repo/HydroSense
HARVEST_DATE=YYYY-MM-DD
git checkout -b daily-harvest/$HARVEST_DATE
git add _pages/ data/paper_registry.json
git commit -m "Daily harvest - $HARVEST_DATE"
git push -u origin daily-harvest/$HARVEST_DATE
```

**Create the PR — you MUST get the PR created. Try each method in order until one succeeds:**

1. **GitHub MCP tools** (try first in cloud environment):
   Use the GitHub MCP `create_pull_request` tool with:
   - `owner`: "hydrotian"
   - `repo`: "HydroSense"
   - `title`: "Daily harvest - YYYY-MM-DD"
   - `body`: "Automated daily paper harvest from top-tier journals."
   - `head`: "daily-harvest/YYYY-MM-DD"
   - `base`: "main"

2. **gh CLI** (try second):
   ```bash
   gh pr create --title "Daily harvest - YYYY-MM-DD" --body "Automated daily paper harvest from top-tier journals."
   ```

3. **Install gh and retry** (if gh is not found):
   ```bash
   # On Ubuntu/Debian (cloud environment):
   curl -fsSL https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo dd of=/usr/share/keyrings/githubcli-archive-keyring.gpg
   echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null
   sudo apt-get update && sudo apt-get install -y gh
   ```
   Then authenticate and create the PR:
   ```bash
   gh auth login --with-token <<< "$GITHUB_TOKEN"
   gh pr create --title "Daily harvest - YYYY-MM-DD" --body "Automated daily paper harvest from top-tier journals."
   ```

4. **GitHub API via curl** (last resort):
   ```bash
   curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
     -H "Accept: application/vnd.github.v3+json" \
     https://api.github.com/repos/hydrotian/HydroSense/pulls \
     -d '{"title":"Daily harvest - YYYY-MM-DD","body":"Automated daily paper harvest from top-tier journals.","head":"daily-harvest/YYYY-MM-DD","base":"main"}'
   ```

**The PR is critical** — it triggers a push notification so the user can review and merge promptly. Failing to create PRs causes registry conflicts when multiple days pile up.

## Important Notes

- **If no relevant papers are found after LLM filtering, STOP. Do not create a post, do not commit, do not create a PR. Just skip this day entirely.**
- Papers flagged as `important` in the registry (appeared in multiple sources) should be noted with "(Also featured in weekly review)" or similar.
- Always check the harvest log (`/tmp/harvest_log.txt`) for errors before proceeding.
- Default harvest date is 8 days ago because same-day papers often get S2 404s.

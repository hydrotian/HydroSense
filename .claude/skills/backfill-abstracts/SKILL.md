---
name: backfill-abstracts
description: Scan published posts for missing abstracts, fetch from APIs, translate to Chinese, and patch both language versions. Use when the user asks to backfill abstracts or fill missing abstracts.
allowed-tools: [Bash, Read, Write, Edit, Glob, Grep]
---

# Backfill Missing Abstracts

Scan all published posts for papers with "Abstract not available", fetch the abstracts from academic APIs, translate to Chinese, and patch both English and Chinese files.

## Workflow

### Step 1: Run the backfill script

```bash
cd /Users/tianzhou/Documents/Gitrepos/HydroSense
python scripts/backfill_abstracts.py --apply
```

The script will:
- Scan all `_pages/**/*.md` (English only) for `> Abstract not available.` placeholders
- For each DOI, try Semantic Scholar → OpenAlex → publisher landing page
- Patch the English file with the fetched abstract
- Record results in `data/abstract_backfill.json`
- Skip DOIs already marked "completed" (previously filled)
- Retry DOIs marked "unavailable" (may have been indexed since last run)

Read the output carefully. Note which DOIs were filled and which files were patched.

### Step 2: Translate and patch Chinese counterparts

For each English file that was patched in Step 1, the corresponding Chinese file lives at `_pages/zh/...` (same relative path). Every English post must have a Chinese counterpart — if one is missing, that is a bug; report it to the user and create the missing Chinese file following the daily-harvest or weekly-review skill templates.

For each paper whose English abstract was just filled:

1. Read the newly patched English abstract from the English file (find the paper by DOI)
2. Translate the abstract to Chinese
3. Find the matching paper block in the Chinese file (locate by DOI)
4. Replace the Chinese placeholder (`> 摘要暂无。` or `> 摘要暂缺。` or `> 摘要未提供。`) with the translated Chinese abstract as a blockquote (`> ...`)

**Translation rules (same as daily-harvest/weekly-review skills):**
- Translate the abstract text to Chinese
- Keep technical terms, model names, acronyms, and place names in English where natural
- Keep all markdown formatting (blockquote `> ` prefix)
- The translated abstract should be a single paragraph in one blockquote line (matching the English format)

### Step 3: Handle "unavailable" papers

For papers still showing as "✗ Not available" in the script output, there is nothing more to do. The tracking file records them as "unavailable" and the script will retry them automatically on the next run. Do NOT manually write placeholder abstracts.

### Step 4: Commit and push

```bash
cd /Users/tianzhou/Documents/Gitrepos/HydroSense
git add _pages/ data/abstract_backfill.json
git commit -m "Backfill missing abstracts"
git push origin main
```

If the push fails due to conflicts:

```bash
git pull --rebase origin main
git push origin main
```

## Important Notes

- **Do not translate paper titles** — they stay in English in both language versions.
- **Do not modify any other part of the post files** — only replace the abstract placeholder lines.
- If a Chinese file has no placeholder for a paper (abstract was already filled differently), skip that paper in that file.
- The script uses a 3-source waterfall: Semantic Scholar → OpenAlex → publisher DOI landing page. The publisher source works for very recent papers that haven't been indexed yet.
- BAMS (journals.ametsoc.org) returns 403 for automated requests — those papers will remain unavailable until S2/OpenAlex indexes them.

---
name: process-scans
description: Use when JPEG scans are present in sans_to_parse/ directory, or when the user asks to process, transcribe, or convert handwritten math scans into Obsidian notes
---

# Process Scans

Converts handwritten math JPEG scans from `sans_to_parse/` into structured Obsidian Markdown notes via a 7-step pipeline. LaTeX conventions, output format, and wikilink rules are defined in the project CLAUDE.md — this skill provides the execution workflow.

**REQUIRED SUB-SKILLS:** Use `obsidian:obsidian-markdown` for Obsidian-flavored syntax (callouts, properties, embeds, block IDs).

**VAULT SEARCH TOOL:** Use `uv run python scripts/vault_search.py` for vault operations:
- `vault-search search <query>` — full-text search across notes (results grouped by file)
- `vault-search search --titles <query>` — search only note names and aliases (quick topic check)
- `vault-search list` — list all notes in the vault
- `vault-search list --tag <tag>` — list notes with a specific tag
- `vault-search resolve <wikilink>` — resolve a wikilink (by stem or alias) to a file path
- `vault-search backlinks <note>` — find all notes that link to a given note
- `vault-search links --check` — find broken wikilinks across the vault
- `vault-search tags` — list all tags with counts

## Pipeline

Create a todo per step. Complete each step for ALL scans before advancing.

### 1. Read & Rename

- Read every scan in `sans_to_parse/` to understand content
- Rename descriptively by topic: `power-series-1.jpeg`, `riemann-integration.jpeg`
- Numeric order (`Scan.jpeg`, `Scan 1.jpeg`, ...) = writing order — use for context

### 2. Transcribe

- Invoke `obsidian:obsidian-markdown` for full Obsidian syntax reference
- Convert handwritten math to Markdown + LaTeX (see CLAUDE.md for conventions)
- **Handwriting key:** A long single-stroke L shape = $\sum$ (summation sigma)
- Preserve mathematical rigor — do not simplify or omit steps from the original notes
- Ambiguous symbols: choose the mathematically sensible interpretation
- Mark any added clarifications with `%%clarification%%` (Obsidian comment — hidden in reading view)
- Use Obsidian-specific formatting:
  - `> [!theorem]` callout for theorem statements
  - `> [!definition]` callout for definitions
  - `> [!proof]-` foldable callout for proofs (collapsed by default)
  - `> [!example]` callout for worked examples
  - `> [!warning]` callout for common pitfalls or subtle points
  - `==highlighted text==` for key conclusions or critical conditions

### 3. Organize into Notes

- Use `uv run python scripts/vault_search.py search --titles "<topic>"` to check if a note on the topic exists, then `search "<topic>"` for full-text matches if needed
- **Integrate into existing notes** where content overlaps; only create new files when no suitable note exists
- Split multi-topic scans into separate files
- **Folder placement** — math notes live under `notes/math/` in topic subfolders:
  - List existing subfolders (`ls notes/math/`) and review their contents to understand each folder's scope
  - Place the new note in the best-fitting subfolder based on its topic and tags
  - If no existing subfolder fits, place it in `notes/math/` directly
  - Non-math content goes in `notes/Odds & Ends/`
- Every note needs proper YAML frontmatter (see `obsidian:obsidian-markdown` Properties section):
  - `aliases`, `tags`, `source`, `date` — all required
  - `source:` field points to final archived path: `sources/YYYY-MM-DD/filename.jpeg`
- Heading hierarchy: `#` > `##` > `###`
- End each note with `## See Also` containing wikilinks to related concepts
- Use `![[note#^block-id]]` embeds to reference specific theorems/definitions from other notes rather than restating them
- **Spaced repetition flashcards** — add a nested `flashcards/<subfolder>` tag matching the note's folder (e.g., `flashcards/analysis-foundations`, `flashcards/special-topics`, `flashcards/series-and-convergence`, `flashcards/integration-and-measure`). Then add Q&A cards for ==only the core concepts== a student must internalize:
  - Named theorems (statement + key hypotheses)
  - Definitions that are prerequisites for other results
  - Critical distinctions (e.g., "what extra hypothesis does the complex case need?")
  - Do NOT card: worked examples, proof steps, corollaries that restate the main theorem, or anything that just repeats the surrounding text
  - Place each card directly after the theorem/definition it tests, using multi-line `?` format:
    ```
    State Theorem X.
    ?
    Concise statement with key hypotheses.
    ```

### 4. Verify Correctness

- Check all theorems, definitions, and formulas for mathematical correctness
- If anything is wrong or missing hypotheses: **stop and ask the user**
- Do not silently include incorrect math or invent content not in the source

### 5. Verify Wikilinks

- Every `[[...]]` must use piped kebab-case: `[[kebab-filename|Display Name]]`
- Never bare alias: `[[Display Name]]` — Obsidian won't resolve it
- Use `uv run python scripts/vault_search.py links --check` to find broken wikilinks
- Use `uv run python scripts/vault_search.py backlinks <note>` to verify incoming links resolve correctly
- Use `uv run python scripts/vault_search.py tags` to check tag consistency with existing vault conventions
- Forward references to nonexistent notes are fine as plain text
- Re-check any notes modified during correctness verification

### 6. Add Diagrams

- Review each note created or modified in steps 2-3
- For each note, assess whether a diagram would clarify the content — good candidates:
  - Theorems with multiple prerequisites or dependencies
  - Chains of implications or equivalences
  - Classification of related concepts (types of convergence, function spaces, etc.)
  - Proof structures with distinct lemma/step dependencies
- If a note would benefit, use the **add-diagram** skill to create and insert the diagram
- Skip notes where the content is straightforward enough that a diagram adds no value

### 7. Archive

```bash
mkdir -p sources/YYYY-MM-DD  # today's date
mv sans_to_parse/*.jpeg sources/YYYY-MM-DD/
```

### 8. Report

Present a final summary that includes:
- New notes created (filenames + one-line description)
- Existing notes updated (filenames + what changed)
- **Diagrams**: Explicitly list every diagram added — which note it was added to and what it visualizes. If no diagrams were added, state that and explain why (e.g., "all notes were straightforward enough that diagrams would not add clarity").
- **Flashcards**: Number of Q&A cards added per note and what they cover.

## Boundaries

- **Do NOT touch** (unless user explicitly asks): `notes/Odds & Ends/`, `notes/.obsidian/`, `notes/copilot/`
- **Do NOT invent** content beyond what's in the scans
- **Do NOT silently fix** the author's math — flag and ask

## Large Batches (5+ scans)

Use subagents to parallelize steps 1-3:
- One subagent per scan or logical group
- Main agent handles steps 4-7 (verification, diagrams, archival) after all transcription completes
- This isolates verbose image-reading context from the main conversation

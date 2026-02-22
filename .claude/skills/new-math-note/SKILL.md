---
name: new-math-note
description: Use when creating a new Obsidian math note from scratch without a scan source, or when the user asks to write up, explain, or document a mathematical topic as a vault note
---

# New Math Note

Creates an Obsidian-compatible math note from scratch (no scan source). For notes transcribed from scans, use process-scans instead.

## Vault Search Tool

Use `uv run python scripts/vault_search.py` (from project root) for vault queries:

```bash
uv run python scripts/vault_search.py search <query>              # full-text search (grouped by file)
uv run python scripts/vault_search.py search --titles <query>     # search only note names and aliases
uv run python scripts/vault_search.py list                        # list all notes in the vault
uv run python scripts/vault_search.py list --tag <tag>            # list notes with a specific tag
uv run python scripts/vault_search.py resolve <wikilink>          # resolve name/alias to file
uv run python scripts/vault_search.py tags                        # list all tags with counts
uv run python scripts/vault_search.py backlinks <note>            # find notes linking to a note
uv run python scripts/vault_search.py links --check               # find broken wikilinks
```

## Before Writing

1. **Check if the note already exists** — use `vault-search search --titles "<topic>"` for a quick topic check, then `vault-search resolve "<name>"` if needed. Use full-text `search "<topic>"` to find related content in other notes. If a related note exists, extend it rather than creating a duplicate.
2. **Check tags** — use `vault-search tags` to see existing tag conventions, or `vault-search list --tag <tag>` to see notes in a topic area.
3. **Choose the right filename** — kebab-case, topic-based: `cauchy-schwarz-inequality.md`

## Template

```markdown
---
aliases: [Natural Title, Alternate Forms]
tags: [real-analysis, topic-tag]
date: YYYY-MM-DD
---

# Title

## Definition / Statement

Core definition or theorem statement with LaTeX.

## [Topic-specific sections]

Proofs, examples, intuition, corollaries — whatever the content calls for.

## See Also
- [[related-note|Related Note Title]]
```

## Checklist

- [ ] Frontmatter: `aliases` (natural title + variants), `tags`, `date` (today)
- [ ] No `source:` field (this note has no scan source)
- [ ] LaTeX uses `$...$` inline, `$$...$$` display (see CLAUDE.md for full conventions)
- [ ] Wikilinks use piped kebab-case: `[[kebab-file|Display Name]]`
- [ ] `## See Also` section with links to related vault notes
- [ ] File saved to `notes/` with kebab-case name
- [ ] Mathematical content is correct — verify before writing
- [ ] Wikilinks verified: `uv run python scripts/vault_search.py links --check`

## When Extending an Existing Note

If adding a section to an existing note rather than creating a new one:
- Read the existing note first to understand its structure
- Add new content in the appropriate place (maintain heading hierarchy)
- Update `## See Also` if new connections are relevant
- Do not restructure or rewrite existing sections unless asked

---
name: verify-wikilinks
description: Use when auditing or maintaining the Obsidian vault's wikilink integrity, after writing or editing notes, or when the user asks to check, fix, or audit links in the vault
---

# Verify Wikilinks

Audits `[[wikilinks]]` across the Obsidian vault in `notes/` for format compliance and target validity.

## Rules

1. **Piped kebab-case format required:** `[[kebab-filename|Display Name]]`
2. **Bare alias links are broken:** `[[Display Name]]` — Obsidian does not reliably resolve aliases
3. **Forward references are OK:** Links to notes that don't exist yet can stay as plain text (not wikilinks)
4. **Image embeds are exempt:** `![[image.png]]` follows Obsidian image syntax, skip these

## Vault Search Tool

Use `uv run python scripts/vault_search.py` (from project root) for all vault queries:

```bash
uv run python scripts/vault_search.py links --check              # find all broken wikilinks
uv run python scripts/vault_search.py resolve <wikilink>          # resolve a name/alias to file path
uv run python scripts/vault_search.py backlinks <note>            # find all notes linking to a note
uv run python scripts/vault_search.py tags                        # list all tags with counts
uv run python scripts/vault_search.py search <query>              # full-text search (grouped by file)
uv run python scripts/vault_search.py search --titles <query>     # search only note names and aliases
uv run python scripts/vault_search.py list                        # list all notes in the vault
uv run python scripts/vault_search.py list --tag <tag>            # list notes with a specific tag
```

The tool automatically skips media embeds (`.png`, `.webp`, etc.) and hidden directories (`.obsidian/`).

## Audit Procedure

### 1. Find broken links

```bash
uv run python scripts/vault_search.py links --check
```

This reports every broken wikilink with file and line number.

### 2. Classify each broken link

| Pattern | Status | Action |
|---------|--------|--------|
| `[[kebab-file\|Name]]` where file exists | Valid | None |
| `[[kebab-file\|Name]]` where file missing | Broken target | Report — may need new note or spelling fix |
| `[[Display Name]]` (no pipe) | **Bad format** | Fix to `[[kebab-file\|Display Name]]` |
| `![[image.ext]]` | Image embed | Skipped automatically by tool |

### 3. Fix bare alias links

Use `resolve` to find the correct target:

```bash
uv run python scripts/vault_search.py resolve "Display Name"
```

This checks both filenames and `aliases` frontmatter. If found, rewrite as `[[kebab-file|Display Name]]`. If not found, it's either a forward reference (use kebab-case format) or a typo.

### 4. Check filenames

- All note files should use kebab-case: `my-topic.md`
- Flag non-kebab filenames (e.g., `Arzelà-Ascoli Theorem.md` should be `arzela-ascoli-theorem.md`)
- Renaming a file requires updating all inbound links — use `backlinks` to find them:
  ```bash
  uv run python scripts/vault_search.py backlinks <old-name>
  ```

### 5. Verify fixes

After making changes, re-run the link checker to confirm no new issues:

```bash
uv run python scripts/vault_search.py links --check
```

## Scope Options

- **Full vault:** Audit all `notes/*.md` files
- **Single file:** Audit only the specified file (useful after editing a note)
- **Recent files:** Audit files modified today or in the last batch

## Common Mappings

When fixing bare alias links, use `vault-search resolve` to map display names to kebab filenames:

```bash
$ uv run python scripts/vault_search.py resolve "Dominated Convergence Theorem"
notes/dominated-convergence-theorem.md
```

→ Fix: `[[dominated-convergence-theorem|Dominated Convergence Theorem]]`

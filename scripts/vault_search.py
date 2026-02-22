"""Obsidian vault search utilities for MathNotes.

Usage:
    vault-search links --check              Find broken wikilinks
    vault-search backlinks <note>           What links to this note
    vault-search tags                       List all tags with counts
    vault-search resolve <wikilink>         Resolve a wikilink to a file path
    vault-search search <query>             Full-text search across notes
    vault-search search --titles <query>    Search only note names and aliases
    vault-search list                       List all notes in the vault
    vault-search list --tag <tag>           List notes with a specific tag
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import Counter
from pathlib import Path

import yaml

VAULT_DIR = Path(__file__).resolve().parent.parent / "notes"

# Matches [[target]] or [[target|display]]
WIKILINK_RE = re.compile(r"\[\[([^\]|#]+)(?:#[^\]|]*)?\s*(?:\|[^\]]+)?\]\]")

# File extensions that are media/embeds, not note links
MEDIA_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".bmp",
    ".mp3", ".ogg", ".wav", ".m4a", ".flac",
    ".mp4", ".webm", ".ogv", ".mov",
    ".pdf", ".csv",
}


def parse_frontmatter(path: Path) -> dict:
    """Extract YAML frontmatter from a markdown file."""
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}
    end = text.find("---", 3)
    if end == -1:
        return {}
    try:
        return yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return {}


def build_index(vault: Path) -> dict:
    """Build lookup maps: stem->path and alias->path."""
    stem_map: dict[str, Path] = {}
    alias_map: dict[str, Path] = {}
    for md in vault.rglob("*.md"):
        # Skip .obsidian and other hidden dirs
        if any(part.startswith(".") for part in md.relative_to(vault).parts):
            continue
        stem_map[md.stem.lower()] = md
        fm = parse_frontmatter(md)
        for alias in fm.get("aliases", []) or []:
            alias_map[str(alias).lower()] = md
    return {"stems": stem_map, "aliases": alias_map}


def resolve_link(target: str, index: dict) -> Path | None:
    """Resolve a wikilink target to a file path."""
    key = target.strip().lower()
    return index["stems"].get(key) or index["aliases"].get(key)


def extract_wikilinks(path: Path) -> list[tuple[int, str]]:
    """Extract all wikilink targets from a file with line numbers."""
    links = []
    in_code_block = False
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        stripped = line.strip()
        if stripped.startswith("```"):
            in_code_block = not in_code_block
            continue
        if in_code_block:
            continue
        for m in WIKILINK_RE.finditer(line):
            links.append((i, m.group(1).strip()))
    return links


# ── Commands ──────────────────────────────────────────────────


def cmd_check_links(vault: Path) -> int:
    """Find broken wikilinks across the vault."""
    index = build_index(vault)
    broken_count = 0
    for md in sorted(vault.rglob("*.md")):
        if any(part.startswith(".") for part in md.relative_to(vault).parts):
            continue
        for lineno, target in extract_wikilinks(md):
            # Skip media/embed links (images, audio, video, pdf)
            if Path(target).suffix.lower() in MEDIA_EXTENSIONS:
                continue
            if resolve_link(target, index) is None:
                rel = md.relative_to(vault)
                print(f"  {rel}:{lineno}  ->  [[{target}]]")
                broken_count += 1
    if broken_count == 0:
        print("No broken wikilinks found.")
    else:
        print(f"\n{broken_count} broken wikilink(s) found.")
    return 1 if broken_count else 0


def cmd_backlinks(vault: Path, note: str) -> int:
    """Find all notes that link to the given note."""
    index = build_index(vault)
    # Resolve the target note first
    target_path = resolve_link(note, index)
    if target_path is None:
        print(f"Note not found: {note}")
        return 1

    target_stem = target_path.stem.lower()
    # Also collect aliases for this note
    fm = parse_frontmatter(target_path)
    target_names = {target_stem}
    for alias in fm.get("aliases", []) or []:
        target_names.add(str(alias).lower())

    results = []
    for md in sorted(vault.rglob("*.md")):
        if md == target_path:
            continue
        if any(part.startswith(".") for part in md.relative_to(vault).parts):
            continue
        for lineno, link_target in extract_wikilinks(md):
            if link_target.strip().lower() in target_names:
                results.append((md.relative_to(vault), lineno, link_target))

    if not results:
        print(f"No backlinks to {target_path.stem}")
    else:
        print(f"Backlinks to {target_path.stem}:")
        for rel, lineno, lt in results:
            print(f"  {rel}:{lineno}  [[{lt}]]")
    return 0


def cmd_tags(vault: Path) -> int:
    """List all tags with counts."""
    tag_counter: Counter[str] = Counter()
    for md in vault.rglob("*.md"):
        if any(part.startswith(".") for part in md.relative_to(vault).parts):
            continue
        fm = parse_frontmatter(md)
        for tag in fm.get("tags", []) or []:
            tag_counter[str(tag)] += 1
    if not tag_counter:
        print("No tags found.")
        return 0
    for tag, count in tag_counter.most_common():
        print(f"  {tag}: {count}")
    return 0


def cmd_resolve(vault: Path, wikilink: str) -> int:
    """Resolve a wikilink to a file path."""
    index = build_index(vault)
    result = resolve_link(wikilink, index)
    if result:
        print(result.relative_to(vault.parent))
    else:
        print(f"Not found: [[{wikilink}]]")
        return 1
    return 0


def cmd_search(vault: Path, query: str, titles_only: bool = False) -> int:
    """Full-text search across notes, or title/alias search with --titles."""
    pattern = re.compile(re.escape(query), re.IGNORECASE)

    if titles_only:
        hits = 0
        for md in sorted(vault.rglob("*.md")):
            if any(part.startswith(".") for part in md.relative_to(vault).parts):
                continue
            rel = md.relative_to(vault)
            stem = md.stem
            fm = parse_frontmatter(md)
            aliases = fm.get("aliases", []) or []
            # Check stem and aliases
            matched = None
            if pattern.search(stem):
                matched = stem
            else:
                for alias in aliases:
                    if pattern.search(str(alias)):
                        matched = str(alias)
                        break
            if matched:
                alias_str = f"  (aliases: {', '.join(str(a) for a in aliases)})" if aliases else ""
                print(f"  {rel}{alias_str}")
                hits += 1
        if hits == 0:
            print(f"No notes matching: {query}")
        else:
            print(f"\n{hits} note(s) found.")
        return 0

    # Full-text search, grouped by file
    total_hits = 0
    for md in sorted(vault.rglob("*.md")):
        if any(part.startswith(".") for part in md.relative_to(vault).parts):
            continue
        rel = md.relative_to(vault)
        file_hits = []
        for i, line in enumerate(md.read_text(encoding="utf-8").splitlines(), 1):
            if pattern.search(line):
                file_hits.append((i, line.strip()))
        if file_hits:
            print(f"  {rel}")
            for lineno, text in file_hits:
                print(f"    {lineno}: {text}")
            total_hits += len(file_hits)
    if total_hits == 0:
        print(f"No results for: {query}")
    else:
        print(f"\n{total_hits} match(es).")
    return 0


def cmd_list(vault: Path, tag: str | None = None) -> int:
    """List all notes, optionally filtered by tag."""
    notes = []
    for md in sorted(vault.rglob("*.md")):
        if any(part.startswith(".") for part in md.relative_to(vault).parts):
            continue
        if tag:
            fm = parse_frontmatter(md)
            tags = [str(t) for t in (fm.get("tags", []) or [])]
            if tag not in tags:
                continue
        notes.append(md.relative_to(vault))
    if not notes:
        if tag:
            print(f"No notes with tag: {tag}")
        else:
            print("No notes found.")
        return 0
    for note in notes:
        print(f"  {note}")
    print(f"\n{len(notes)} note(s).")
    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Obsidian vault search utilities",
        prog="vault-search",
    )
    parser.add_argument(
        "--vault",
        type=Path,
        default=VAULT_DIR,
        help="Path to vault directory (default: notes/)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    # links --check
    p_links = sub.add_parser("links", help="Wikilink operations")
    p_links.add_argument("--check", action="store_true", help="Find broken wikilinks")

    # backlinks <note>
    p_back = sub.add_parser("backlinks", help="Find backlinks to a note")
    p_back.add_argument("note", help="Note name (stem or alias)")

    # tags
    sub.add_parser("tags", help="List all tags with counts")

    # resolve <wikilink>
    p_res = sub.add_parser("resolve", help="Resolve a wikilink to a file path")
    p_res.add_argument("wikilink", help="Wikilink target to resolve")

    # search <query>
    p_search = sub.add_parser("search", help="Full-text search across notes")
    p_search.add_argument("query", help="Search query")
    p_search.add_argument("--titles", action="store_true", help="Search only note names and aliases")

    # list
    p_list = sub.add_parser("list", help="List all notes in the vault")
    p_list.add_argument("--tag", help="Filter by tag")

    args = parser.parse_args()

    vault = args.vault

    if args.command == "links":
        if args.check:
            sys.exit(cmd_check_links(vault))
        else:
            parser.parse_args(["links", "--help"])
    elif args.command == "backlinks":
        sys.exit(cmd_backlinks(vault, args.note))
    elif args.command == "tags":
        sys.exit(cmd_tags(vault))
    elif args.command == "resolve":
        sys.exit(cmd_resolve(vault, args.wikilink))
    elif args.command == "search":
        sys.exit(cmd_search(vault, args.query, titles_only=args.titles))
    elif args.command == "list":
        sys.exit(cmd_list(vault, tag=args.tag))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""id_manager.py — Unique ID Manager for Arabic Grammar Book HTML pages.

Manages the bXXXXX ID system used on every significant content block.

Commands:
    auto-tag   Automatically add IDs to elements that are missing them.
    verify     Check for duplicate IDs across all pages.
    next-id    Print a single new unique ID (useful for manual editing).

Usage:
    python Jules-workspace/id_manager.py auto-tag
    python Jules-workspace/id_manager.py auto-tag --dry-run
    python Jules-workspace/id_manager.py auto-tag --files pages/01.0_intro.html
    python Jules-workspace/id_manager.py verify
    python Jules-workspace/id_manager.py next-id
"""

from __future__ import annotations

import argparse
import secrets
import sys
from dataclasses import dataclass, field
from pathlib import Path

from bs4 import BeautifulSoup, Tag

# ── Constants ─────────────────────────────────────────────────────────────────

PAGES_DIR = Path("pages")

#: CSS selectors for elements that MUST have a bXXXXX ID.
TARGET_SELECTORS: tuple[str, ...] = (
    "header",
    ".content-block",
    ".benefit-box",
    ".irab-box",
    ".poem-container",
    ".bio-card",
    ".exam-question",
    ".split-grid > *",
)


# ── Data Models ───────────────────────────────────────────────────────────────


@dataclass
class DuplicateID:
    filepath: Path
    id_value: str

    def __str__(self) -> str:
        return f"  • '{self.id_value}' — duplicate found in {self.filepath}"


@dataclass
class TagResult:
    filepath: Path
    ids_added: int


@dataclass
class AutoTagReport:
    results: list[TagResult] = field(default_factory=list)
    total_added: int = 0
    dry_run: bool = False

    def print_summary(self) -> None:
        mode = "[DRY RUN] " if self.dry_run else ""
        for r in self.results:
            action = "Would update" if self.dry_run else "Updated"
            print(f"  {mode}{action} {r.filepath}: +{r.ids_added} ID(s)")
        print(f"\n{'🔍 Dry-run:' if self.dry_run else '✅'} Total IDs added: {self.total_added}")


# ── Core Manager ──────────────────────────────────────────────────────────────


class IDManager:
    """Manages unique bXXXXX IDs across all HTML pages."""

    def __init__(self, root_dir: Path = PAGES_DIR) -> None:
        self.root_dir = root_dir
        self.existing_ids: set[str] = set()

    # ── File Discovery ────────────────────────────────────────────────────

    def get_html_files(self) -> list[Path]:
        """Return sorted list of HTML files under root_dir (recursive)."""
        return sorted(self.root_dir.rglob("*.html"))

    # ── ID Scanning ───────────────────────────────────────────────────────

    def scan_existing_ids(self) -> list[DuplicateID]:
        """Populate self.existing_ids from all HTML files. Returns duplicates."""
        self.existing_ids.clear()
        duplicates: list[DuplicateID] = []

        for filepath in self.get_html_files():
            try:
                soup = BeautifulSoup(filepath.read_text(encoding="utf-8"), "html.parser")
                for tag in soup.find_all(id=True):
                    tag_id: str = tag["id"]
                    if tag_id in self.existing_ids:
                        duplicates.append(DuplicateID(filepath=filepath, id_value=tag_id))
                    self.existing_ids.add(tag_id)
            except OSError as exc:
                print(f"⚠  Error reading {filepath}: {exc}", file=sys.stderr)

        return duplicates

    # ── ID Generation ─────────────────────────────────────────────────────

    def generate_id(self) -> str:
        """Generate a cryptographically random unique ID in format bXXXXX."""
        while True:
            # 5 decimal digits → 100_000 possibilities, collision-safe via set
            digits = "".join(str(secrets.randbelow(10)) for _ in range(5))
            new_id = f"b{digits}"
            if new_id not in self.existing_ids:
                self.existing_ids.add(new_id)
                return new_id

    # ── Auto-Tag ──────────────────────────────────────────────────────────

    def _collect_unique_candidates(self, soup: BeautifulSoup) -> list[Tag]:
        """Return deduplicated list of Tags matching TARGET_SELECTORS."""
        seen: set[int] = set()
        candidates: list[Tag] = []
        for selector in TARGET_SELECTORS:
            for tag in soup.select(selector):
                if id(tag) not in seen:
                    seen.add(id(tag))
                    candidates.append(tag)
        return candidates

    def auto_tag(
        self,
        *,
        dry_run: bool = False,
        files: list[Path] | None = None,
    ) -> AutoTagReport:
        """Add bXXXXX IDs to target elements that are missing them.

        Args:
            dry_run: If True, report changes without writing files.
            files:   Specific files to process (defaults to all pages).
        """
        self.scan_existing_ids()
        target_files = files if files is not None else self.get_html_files()
        report = AutoTagReport(dry_run=dry_run)

        for filepath in target_files:
            try:
                content = filepath.read_text(encoding="utf-8")
                soup = BeautifulSoup(content, "html.parser")
                candidates = self._collect_unique_candidates(soup)

                ids_added = 0
                for tag in candidates:
                    if not tag.has_attr("id"):
                        tag["id"] = self.generate_id()
                        ids_added += 1

                if ids_added > 0:
                    report.total_added += ids_added
                    tag_result = TagResult(filepath=filepath, ids_added=ids_added)
                    report.results.append(tag_result)
                    if not dry_run:
                        filepath.write_text(str(soup), encoding="utf-8")

            except OSError as exc:
                print(f"⚠  Error processing {filepath}: {exc}", file=sys.stderr)

        return report

    # ── Verify ────────────────────────────────────────────────────────────

    def verify(self) -> None:
        """Check for duplicate IDs. Exits with non-zero code on failure."""
        duplicates = self.scan_existing_ids()
        if duplicates:
            print("❌ Verification Failed! Duplicate IDs found:")
            for dup in duplicates:
                print(dup)
            sys.exit(1)
        print(f"✅ Verification Passed. {len(self.existing_ids)} unique IDs found.")

    # ── Next ID ───────────────────────────────────────────────────────────

    def next_id(self) -> str:
        """Scan existing IDs and print a single new unique ID."""
        self.scan_existing_ids()
        new_id = self.generate_id()
        print(new_id)
        return new_id


# ── CLI ───────────────────────────────────────────────────────────────────────


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="id_manager.py",
        description="Manage unique bXXXXX IDs for HTML content blocks.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--root",
        type=Path,
        default=PAGES_DIR,
        metavar="DIR",
        help=f"Root pages directory (default: {PAGES_DIR})",
    )

    subparsers = parser.add_subparsers(dest="command", metavar="COMMAND")

    # auto-tag
    sp_tag = subparsers.add_parser("auto-tag", help="Add IDs to elements missing them")
    sp_tag.add_argument(
        "--dry-run",
        action="store_true",
        help="Show what would change without writing files",
    )
    sp_tag.add_argument(
        "--files",
        nargs="+",
        type=Path,
        metavar="FILE",
        help="Target specific HTML files instead of all pages",
    )

    # verify
    subparsers.add_parser("verify", help="Check for duplicate IDs across all pages")

    # next-id
    subparsers.add_parser("next-id", help="Generate and print one new unique ID")

    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manager = IDManager(root_dir=args.root)

    match args.command:
        case "auto-tag":
            report = manager.auto_tag(dry_run=args.dry_run, files=args.files)
            report.print_summary()
        case "verify":
            manager.verify()
        case "next-id":
            manager.next_id()
        case _:
            # No subcommand given — print help
            print("No command specified. Use --help for usage.", file=sys.stderr)
            sys.exit(1)


if __name__ == "__main__":
    main()

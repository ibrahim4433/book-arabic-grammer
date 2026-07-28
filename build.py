#!/usr/bin/env python3
"""build.py — Arabic Grammar Book PDF Builder.

Compiles all pages in /pages/ into a single A4 PDF.

Usage:
    python build.py                          # auto-selects best engine
    python build.py --engine playwright      # Chrome via Playwright (recommended, matches preview)
    python build.py --engine weasyprint      # legacy WeasyPrint engine
    python build.py --output output/book.pdf
    python build.py --pages-dir pages/ --dry-run
"""

from __future__ import annotations

import argparse
import re
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path


@dataclass(frozen=True)
class BuildConfig:
    pages_dir: Path = Path("pages")
    output_pdf: Path = Path("output/export/book.pdf")
    front_cover: Path = Path("pages/cover/front-cover.jpg")
    back_cover: Path = Path("pages/cover/back-cover.jpg")
    stylesheet: Path = Path("styles/main.css")
    watermark_text: str = "أ. حنا خفيف"
    dry_run: bool = False


@dataclass
class BuildResult:
    pages_processed: int = 0
    pages_skipped: int = 0
    errors: list[str] = field(default_factory=list)
    output_path: Path | None = None
    duration_seconds: float = 0.0

    @property
    def success(self) -> bool:
        return len(self.errors) == 0


class BuildError(Exception):
    pass


def _extract_body(content: str, filepath: Path) -> str:
    body_match = re.search(r"<body[^>]*>(.*?)</body>", content, re.DOTALL | re.IGNORECASE)
    if body_match:
        return body_match.group(1)
    print(f"  → Info: No <body> tag in {filepath}. Using full content as fragment.")
    return content


def _build_cover_html(image_path: Path, *, break_after: str = "page") -> str:
    return f"""
    <div class="cover-page-wrapper" style="break-after: {break_after};">
        <img src="{image_path.as_posix()}" alt="Cover">
    </div>
    """


def _master_html(body_content: str, stylesheet: Path, watermark_text: str) -> str:
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Book Compilation</title>
    <link rel="stylesheet" href="{stylesheet.as_posix()}">
    <style>
        @page cover {{
            margin: 0;
            size: A4;
            @bottom-center {{ content: none; }}
        }}
        .cover-page-wrapper {{
            page: cover;
            width: 210mm;
            height: 297mm;
            overflow: hidden;
            break-after: page;
            position: relative;
            z-index: 20000;
            background: white;
        }}
        .cover-page-wrapper img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
    </style>
</head>
<body>
    <!-- Global Fixed Background -->
    <div class="global-background-layer"></div>

    <!-- Global Fixed Watermark -->
    <div class="global-watermark-layer">
        <span class="watermark-text">{watermark_text}</span>
    </div>

    <!-- Content Pages -->
    {body_content}
</body>
</html>
"""


def collect_pages(config: BuildConfig) -> list[Path]:
    all_files = sorted(config.pages_dir.glob("*.html"))
    return [f for f in all_files if "TEMPLATE_" not in f.name]


def build_book(config: BuildConfig) -> BuildResult:
    """WeasyPrint build pipeline."""
    result = BuildResult()
    start_time = time.perf_counter()

    try:
        from weasyprint import HTML
    except ImportError as exc:
        raise BuildError(
            "WeasyPrint is not installed.\nRun: pip install -r requirements.txt"
        ) from exc
    except OSError as exc:
        raise BuildError(
            "WeasyPrint is installed, but its native GTK/Pango libraries are missing.\n"
            "See: https://doc.courtbouillon.org/weasyprint/stable/first_steps.html"
        ) from exc

    pages = collect_pages(config)
    if not pages:
        raise BuildError(f"No HTML files found in '{config.pages_dir}'.")

    print(f"📄 Found {len(pages)} page(s) in '{config.pages_dir}'")

    has_front = config.front_cover.exists()
    has_back = config.back_cover.exists()
    if has_front:
        print(f"🖼  Front cover: {config.front_cover}")
    if has_back:
        print(f"🖼  Back cover:  {config.back_cover}")

    body_parts: list[str] = []

    if has_front:
        body_parts.append(_build_cover_html(config.front_cover))

    for page_file in pages:
        print(f"  ⚙  Processing {page_file.name}...")
        try:
            content = page_file.read_text(encoding="utf-8")
            body_parts.append(_extract_body(content, page_file))
            result.pages_processed += 1
        except OSError as exc:
            msg = f"Error reading {page_file}: {exc}"
            print(f"  ✗  {msg}")
            result.errors.append(msg)

    if has_back:
        body_parts.append(_build_cover_html(config.back_cover, break_after="auto"))

    full_html = _master_html(
        body_content="\n".join(body_parts),
        stylesheet=config.stylesheet,
        watermark_text=config.watermark_text,
    )

    if config.dry_run:
        print("\n🔍 Dry-run mode: skipping PDF render.")
        print(f"   Would output → {config.output_pdf}")
        result.duration_seconds = time.perf_counter() - start_time
        return result

    config.output_pdf.parent.mkdir(parents=True, exist_ok=True)
    print(f"\n🖨  Rendering PDF (WeasyPrint) → {config.output_pdf} ...")
    try:
        HTML(string=full_html, base_url=".").write_pdf(str(config.output_pdf))
    except Exception as exc:
        raise BuildError(f"PDF rendering failed: {exc}") from exc

    result.output_path = config.output_pdf
    result.duration_seconds = time.perf_counter() - start_time
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="build.py",
        description="Compile Arabic Grammar book pages into a single PDF.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--engine",
        choices=["playwright", "weasyprint", "auto"],
        default="auto",
        help=(
            "PDF rendering engine. 'playwright' uses Chrome for pixel-perfect output "
            "matching the calibration preview. 'weasyprint' is the legacy engine. "
            "'auto' uses Playwright if installed, otherwise WeasyPrint. (default: auto)"
        ),
    )
    parser.add_argument("--pages-dir", type=Path, default=Path("pages"), metavar="DIR")
    parser.add_argument("--output", type=Path, default=Path("output/export/book.pdf"), metavar="PATH")
    parser.add_argument("--watermark", default="أ. حنا خفيف", metavar="TEXT")
    parser.add_argument("--dry-run", action="store_true", help="Validate pages without rendering")
    parser.add_argument("--use-system-chrome", action="store_true", help="(Playwright) Auto-detect system Chrome")
    return parser.parse_args()


def _playwright_available() -> bool:
    try:
        import playwright  # noqa: F401
        return True
    except ImportError:
        return False


def main() -> None:
    args = parse_args()

    engine = args.engine
    if engine == "auto":
        if _playwright_available():
            engine = "playwright"
            print("🔧 Engine: Playwright (Chrome) — auto-selected for pixel-perfect output.")
            print("   Use --engine weasyprint to use the legacy engine instead.")
        else:
            engine = "weasyprint"
            print("🔧 Engine: WeasyPrint (legacy) — Playwright not found.")
            print("   For output matching the calibration preview exactly, run:")
            print("   pip install playwright && playwright install chromium")

    if engine == "playwright":
        _root = Path(__file__).resolve().parent
        playwright_script = _root / "build_playwright.py"
        if not playwright_script.exists():
            print("❌ build_playwright.py not found next to build.py.")
            sys.exit(1)

        fwd_args = [
            sys.executable, str(playwright_script),
            "--pages-dir", str(args.pages_dir),
            "--output", str(args.output),
            "--watermark", args.watermark,
        ]
        if args.dry_run:
            fwd_args.append("--dry-run")
        if args.use_system_chrome:
            fwd_args.append("--use-system-chrome")

        import subprocess
        result = subprocess.run(fwd_args)
        sys.exit(result.returncode)

    # WeasyPrint path
    config = BuildConfig(
        pages_dir=args.pages_dir,
        output_pdf=args.output,
        watermark_text=args.watermark,
        dry_run=args.dry_run,
    )

    try:
        result = build_book(config)
    except BuildError as exc:
        print(f"\n❌ Build failed: {exc}", file=sys.stderr)
        sys.exit(1)

    if result.errors:
        print(f"\n⚠  Build completed with {len(result.errors)} error(s):")
        for err in result.errors:
            print(f"   • {err}")
        sys.exit(1)

    if result.output_path:
        size_kb = result.output_path.stat().st_size / 1024
        print(
            f"\n✅ PDF generated: {result.output_path} "
            f"({size_kb:.1f} KB, {result.pages_processed} pages, "
            f"{result.duration_seconds:.1f}s)"
        )
    else:
        print(f"\n✅ Dry-run complete. {result.pages_processed} page(s) validated.")


if __name__ == "__main__":
    main()

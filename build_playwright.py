#!/usr/bin/env python3
"""build_playwright.py — Arabic Grammar Book PDF Builder using Playwright.

Compiles all pages in /pages/ into a single A4 PDF by rendering each page
individually (to preserve positioning, backgrounds, and margins) and then
merging them into a final PDF.

Usage:
    python build_playwright.py
    python build_playwright.py --output output/book.pdf
    python build_playwright.py --pages-dir pages/ --dry-run
"""

from __future__ import annotations

import argparse
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from dataclasses import dataclass, field
from pathlib import Path
from urllib.parse import urljoin

try:
    from pypdf import PdfWriter
except ImportError:
    print("❌ Error: pypdf is not installed. Run: pip install pypdf", file=sys.stderr)
    sys.exit(1)


PROJECT_ROOT = Path(__file__).resolve().parent


@dataclass(frozen=True)
class BuildConfig:
    pages_dir: Path = PROJECT_ROOT / "pages"
    output_pdf: Path = PROJECT_ROOT / "output/export/book.pdf"
    front_cover: Path = PROJECT_ROOT / "pages/cover/front-cover.jpg"
    back_cover: Path = PROJECT_ROOT / "pages/cover/back-cover.jpg"
    stylesheet: Path = PROJECT_ROOT / "styles/main.css"
    watermark_text: str = "أ. حنا خفيف"
    dry_run: bool = False
    chrome_executable: str | None = None


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


def _build_cover_html(image_path: Path) -> str:
    # Use file URL for image
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Cover</title>
    <style>
        @page {{
            margin: 0;
            size: A4;
            @bottom-center {{ content: none; }}
        }}
        body, html {{
            margin: 0;
            padding: 0;
            width: 100%;
            height: 100%;
            background: white;
            overflow: hidden;
        }}
        img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
        }}
    </style>
</head>
<body>
    <img src="{image_path.as_uri()}" alt="Cover">
</body>
</html>
"""


def collect_pages(config: BuildConfig) -> list[Path]:
    all_files = sorted(config.pages_dir.glob("*.html"))
    return [f for f in all_files if "TEMPLATE_" not in f.name]


def _is_wsl() -> bool:
    try:
        return "microsoft" in Path("/proc/version").read_text().lower()
    except Exception:
        return False


def _find_system_chrome() -> str | None:
    if _is_wsl():
        linux_candidates = [
            "/usr/bin/google-chrome",
            "/usr/bin/google-chrome-stable",
            "/usr/bin/chromium-browser",
            "/usr/bin/chromium",
            "/snap/bin/chromium",
        ]
        for path in linux_candidates:
            if Path(path).exists():
                return path
        for name in ["google-chrome", "google-chrome-stable", "chromium-browser", "chromium"]:
            found = shutil.which(name)
            if found:
                return found
        return None

    candidates = [
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
        "/snap/bin/chromium",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for path in candidates:
        if Path(path).exists():
            return path
    for name in ["google-chrome", "google-chrome-stable", "chromium-browser", "chromium"]:
        found = shutil.which(name)
        if found:
            return found
    return None

def check_emoji_font() -> None:
    """Warns if Noto Color Emoji is missing on Linux/WSL systems."""
    if sys.platform.startswith("linux") or _is_wsl():
        try:
            result = subprocess.run(
                ["fc-list", ":family=Noto Color Emoji"],
                capture_output=True,
                text=True
            )
            if not result.stdout.strip():
                print(
                    "\n⚠️  WARNING: 'Noto Color Emoji' font not found.\n"
                    "   Emojis may render as boxes or empty squares.\n"
                    "   To fix this, install the font (e.g. `sudo apt install fonts-noto-color-emoji`)\n"
                )
        except Exception:
            pass


def _render_page_to_pdf(page_obj, html_url: str, output_path: Path) -> None:
    page_obj.goto(html_url, wait_until="networkidle", timeout=90_000)
    page_obj.wait_for_timeout(500)  # Wait for fonts/images

    page_obj.pdf(
        path=str(output_path),
        format="A4",
        print_background=True,
        margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
        prefer_css_page_size=True,
    )


def build_book(config: BuildConfig) -> BuildResult:
    result = BuildResult()
    start_time = time.perf_counter()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise BuildError(
            "Playwright is not installed.\n"
            "Run: pip install playwright && playwright install chromium"
        ) from exc

    check_emoji_font()

    pages = collect_pages(config)
    if not pages:
        raise BuildError(f"No HTML files found in '{config.pages_dir}'.")

    print(f"📄 Found {len(pages)} page(s) in '{config.pages_dir}'")

    has_front = config.front_cover.exists()
    has_back = config.back_cover.exists()

    if config.dry_run:
        print("\n🔍 Dry-run mode: skipping PDF render.")
        print(f"   Would output → {config.output_pdf}")
        result.duration_seconds = time.perf_counter() - start_time
        return result

    config.output_pdf.parent.mkdir(parents=True, exist_ok=True)
    temp_dir = tempfile.mkdtemp(prefix="book_build_")
    pdf_parts = []

    try:
        chrome_exe = config.chrome_executable or _find_system_chrome()

        print("\n🖨  Rendering pages via Chrome...")
        if chrome_exe:
            print(f"   Chrome: {chrome_exe}")

        with sync_playwright() as p:
            launch_kwargs: dict = {
                "args": [
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                    "--disable-gpu",
                    "--allow-file-access-from-files",
                    "--disable-web-security",
                    "--font-render-hinting=none"
                ],
                "headless": True,
            }
            if chrome_exe:
                launch_kwargs["executable_path"] = chrome_exe

            browser = p.chromium.launch(**launch_kwargs)
            context = browser.new_context()
            page_obj = context.new_page()
            page_obj.emulate_media(media="print")

            # 1. Front Cover
            if has_front:
                print("  ⚙  Rendering front cover...")
                front_html_path = Path(temp_dir) / "front_cover.html"
                front_html_path.write_text(_build_cover_html(config.front_cover), encoding="utf-8")

                front_pdf_path = Path(temp_dir) / "front_cover.pdf"
                _render_page_to_pdf(page_obj, front_html_path.as_uri(), front_pdf_path)
                pdf_parts.append(front_pdf_path)

            # 2. Content Pages
            for i, page_file in enumerate(pages):
                print(f"  ⚙  Rendering {page_file.name} ({i+1}/{len(pages)})...")
                try:
                    # Inject watermark into the page before rendering
                    content = page_file.read_text(encoding="utf-8")

                    # Instead of parsing everything, just rely on file:// URLs matching the preview.
                    # We render the original page directly.
                    # If it lacks watermark layer, we could inject it, but the styling
                    # requires it to be inside <body>. The pages already include watermark logic
                    # or are expected to when loaded individually.
                    # Note: We append watermark to the body if it isn't there already.
                    if 'class="global-watermark-layer"' not in content:
                        watermark_html = f'''<div class="global-watermark-layer" style="position: fixed; z-index: 9999; top: 0; left: 0; width: 100%; height: 100%; display: flex; justify-content: center; align-items: center; pointer-events: none;">
        <span class="watermark-text" style="font-family: 'Noto Kufi Arabic'; font-weight: 900; font-size: 80pt; color: #000000; opacity: 0.4; transform: rotate(-45deg); white-space: nowrap;">{config.watermark_text}</span>
    </div>'''
                        content = content.replace('</body>', watermark_html + '\n</body>')

                    if 'class="global-background-layer"' not in content:
                        bg_html = '''<div class="global-background-layer" style="position: fixed; z-index: -1000; top: -5mm; left: -5mm; width: 210mm; height: 297mm; background-image: url('../assets/page-background/background.jpg'); background-size: cover; background-position: center;"></div>'''
                        content = re.sub(r'(<body[^>]*>)', r'\1\n' + bg_html, content, flags=re.IGNORECASE)

                    # Save modified content to a temp file in the same directory so relative links work
                    temp_page = page_file.with_name(f"_tmp_render_{page_file.name}")
                    try:
                        temp_page.write_text(content, encoding="utf-8")
                        out_pdf = Path(temp_dir) / f"page_{i}.pdf"

                        _render_page_to_pdf(page_obj, temp_page.resolve().as_uri(), out_pdf)
                        pdf_parts.append(out_pdf)
                        result.pages_processed += 1
                    finally:
                        if temp_page.exists():
                            temp_page.unlink()

                except Exception as exc:
                    msg = f"Error rendering {page_file.name}: {exc}"
                    print(f"  ✗  {msg}")
                    result.errors.append(msg)

            # 3. Back Cover
            if has_back:
                print("  ⚙  Rendering back cover...")
                back_html_path = Path(temp_dir) / "back_cover.html"
                back_html_path.write_text(_build_cover_html(config.back_cover), encoding="utf-8")

                back_pdf_path = Path(temp_dir) / "back_cover.pdf"
                _render_page_to_pdf(page_obj, back_html_path.as_uri(), back_pdf_path)
                pdf_parts.append(back_pdf_path)

            browser.close()

        # Merge PDFs
        print(f"\n🔗 Merging {len(pdf_parts)} PDF parts...")
        merger = PdfWriter()
        for pdf_path in pdf_parts:
            merger.append(str(pdf_path))

        merger.write(str(config.output_pdf))
        merger.close()

    finally:
        shutil.rmtree(temp_dir, ignore_errors=True)

    result.output_path = config.output_pdf
    result.duration_seconds = time.perf_counter() - start_time
    return result


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="build_playwright.py",
        description="Compile Arabic Grammar book pages into a PDF using Chrome (Playwright).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("--pages-dir", type=Path, default=PROJECT_ROOT / "pages", metavar="DIR")
    parser.add_argument("--output", type=Path, default=PROJECT_ROOT / "output/export/book.pdf", metavar="PATH")
    parser.add_argument("--watermark", default="أ. حنا خفيف", metavar="TEXT")
    parser.add_argument("--dry-run", action="store_true", help="Validate pages without rendering")
    parser.add_argument("--use-system-chrome", action="store_true", help="Auto-detect system Chrome")
    parser.add_argument("--chrome-path", type=str, default=None, metavar="PATH", help="Explicit Chrome path")
    parser.add_argument("--install-browsers", action="store_true", help="Install Playwright Chromium and exit")
    return parser.parse_args()


def main() -> None:
    args = parse_args()

    if args.install_browsers:
        print("📦 Installing Playwright Chromium browser...")
        subprocess.run([sys.executable, "-m", "playwright", "install", "chromium"], check=True)
        print("✅ Done! You can now run: python build_playwright.py")
        return

    chrome_exe = args.chrome_path
    if args.use_system_chrome and not chrome_exe:
        chrome_exe = _find_system_chrome()
        if not chrome_exe:
            print("⚠  Could not find system Chrome. Will use Playwright bundled Chromium.")

    config = BuildConfig(
        pages_dir=args.pages_dir,
        output_pdf=args.output,
        watermark_text=args.watermark,
        dry_run=args.dry_run,
        chrome_executable=chrome_exe,
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

#!/usr/bin/env python3
"""build_playwright.py — Arabic Grammar Book PDF Builder (Playwright / Chrome engine).

Uses headless Chromium via Playwright to render the book PDF. This guarantees
the output matches the calibration tool preview exactly, since both use the
same Chrome rendering engine.

Usage:
    python build_playwright.py
    python build_playwright.py --output output/export/book.pdf
    python build_playwright.py --pages-dir pages/ --dry-run
    python build_playwright.py --install-browsers   # First-time setup
    python build_playwright.py --use-system-chrome  # Use existing Chrome

Requirements:
    pip install playwright
    playwright install chromium
"""

from __future__ import annotations

import argparse
import re
import sys
import time
import tempfile
import shutil
from dataclasses import dataclass, field
from pathlib import Path

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
        <img src="{image_path.as_uri()}" alt="Cover">
    </div>
    """


def _master_html(body_content: str, stylesheet: Path, watermark_text: str) -> str:
    # Use file:// URIs for stylesheet and font/asset references so Playwright
    # can resolve them regardless of the temp file's location.
    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <title>Book Compilation</title>
    <link rel="stylesheet" href="{stylesheet.as_uri()}">
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
    <div class="global-background-layer"></div>
    <div class="global-watermark-layer">
        <span class="watermark-text">{watermark_text}</span>
    </div>
    {body_content}
</body>
</html>
"""


def collect_pages(config: BuildConfig) -> list[Path]:
    all_files = sorted(config.pages_dir.glob("*.html"))
    return [f for f in all_files if "TEMPLATE_" not in f.name]


def _is_wsl() -> bool:
    """Return True when running inside Windows Subsystem for Linux."""
    try:
        return "microsoft" in Path("/proc/version").read_text().lower()
    except Exception:
        return False


def _find_system_chrome() -> str | None:
    """Locate a native Linux Chrome/Chromium executable.

    Windows .exe binaries are deliberately excluded when running in WSL:
    Playwright communicates via --remote-debugging-pipe (Linux file
    descriptors), which Windows processes cannot use.
    """
    if _is_wsl():
        # Only look for native Linux binaries — skip Windows .exe paths
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
        # No native Linux Chrome found — return None so Playwright uses
        # its own bundled Chromium headless shell
        return None

    # Non-WSL (native Linux / macOS): check all standard paths
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


def build_book(config: BuildConfig) -> BuildResult:
    result = BuildResult()
    start_time = time.perf_counter()

    try:
        from playwright.sync_api import sync_playwright
    except ImportError as exc:
        raise BuildError(
            "Playwright is not installed.\n"
            "Run: pip install playwright && playwright install chromium\n"
            "     — or —\n"
            "     python build_playwright.py --install-browsers"
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

    tmp_html = None
    try:
        # Write temp HTML to project root so relative paths in CSS resolve correctly
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            suffix="_book_build.html",
            dir=str(PROJECT_ROOT),
            delete=False,
        ) as f:
            f.write(full_html)
            tmp_html = Path(f.name)

        temp_url = tmp_html.as_uri()
        config.output_pdf.parent.mkdir(parents=True, exist_ok=True)
        print(f"\n🖨  Rendering PDF via Chrome → {config.output_pdf} ...")

        chrome_exe = config.chrome_executable or _find_system_chrome()
        if chrome_exe:
            print(f"   Chrome: {chrome_exe}")
        else:
            print("   Using Playwright bundled Chromium")

        with sync_playwright() as p:
            launch_kwargs: dict = {
                "args": [
                    "--no-sandbox",
                    "--disable-dev-shm-usage",
                    "--disable-gpu",
                    "--allow-file-access-from-files",
                    "--disable-web-security",
                ],
                "headless": True,
            }
            if chrome_exe:
                launch_kwargs["executable_path"] = chrome_exe

            browser = p.chromium.launch(**launch_kwargs)
            context = browser.new_context()
            page = context.new_page()

            # Activate @media print rules and @page declarations
            page.emulate_media(media="print")

            print("   Loading HTML document...")
            page.goto(temp_url, wait_until="networkidle", timeout=90_000)
            # Allow fonts and background images to finish loading
            page.wait_for_timeout(1000)

            print("   Generating PDF...")
            page.pdf(
                path=str(config.output_pdf),
                format="A4",
                print_background=True,
                # Let CSS @page rules control all margins and page size
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                prefer_css_page_size=True,
            )

            browser.close()

    finally:
        if tmp_html and tmp_html.exists():
            tmp_html.unlink()

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
        import subprocess
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

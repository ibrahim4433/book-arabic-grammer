#!/usr/bin/env python3
"""compare_preview.py — Visual diff tool: Chrome preview vs WeasyPrint PDF output.

Renders a single page HTML file through both Chrome (Playwright) and WeasyPrint,
saves them as PNG screenshots, and optionally produces a side-by-side composite.

Usage:
    python compare_preview.py pages/page_101.html
    python compare_preview.py pages/page_101.html --output-dir output/debug/
    python compare_preview.py pages/page_101.html --no-weasyprint  # Chrome only
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
OUTPUT_DIR = PROJECT_ROOT / "output" / "debug"


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
        return None  # Let Playwright use its bundled Chromium headless shell

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


def render_chrome_screenshot(html_path: Path, out_png: Path, chrome_exe: str | None = None) -> bool:
    """Render the page using headless Chrome (print media) and save as PNG."""
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("  ⚠  Playwright not installed. Skipping Chrome screenshot.")
        print("     Run: pip install playwright && playwright install chromium")
        return False

    exe = chrome_exe or _find_system_chrome()
    url = html_path.as_uri()

    with sync_playwright() as p:
        launch_kwargs: dict = {
            "args": [
                "--no-sandbox", "--disable-dev-shm-usage", "--disable-gpu",
                "--allow-file-access-from-files", "--disable-web-security",
            ],
            "headless": True,
        }
        if exe:
            launch_kwargs["executable_path"] = exe
            print(f"  Chrome: {exe}")
        else:
            print("  Using Playwright bundled Chromium")

        browser = p.chromium.launch(**launch_kwargs)
        context = browser.new_context(
            viewport={"width": 794, "height": 1123},  # A4 at 96dpi
        )
        page = context.new_page()
        page.emulate_media(media="print")
        page.goto(url, wait_until="networkidle", timeout=30_000)
        page.wait_for_timeout(800)

        # Set viewport to A4 size for screenshot
        page.set_viewport_size({"width": 794, "height": 1123})
        page.screenshot(path=str(out_png), full_page=False, clip={"x": 0, "y": 0, "width": 794, "height": 1123})
        browser.close()

    print(f"  ✅ Chrome screenshot saved: {out_png}")
    return True


def render_weasyprint_screenshot(html_path: Path, out_png: Path) -> bool:
    """Render the page using WeasyPrint → PDF → PNG (via pdf2image or cairo)."""
    try:
        from weasyprint import HTML
    except ImportError:
        print("  ⚠  WeasyPrint not installed. Skipping WeasyPrint render.")
        return False

    import tempfile
    tmp_pdf = Path(tempfile.mktemp(suffix=".pdf"))
    try:
        base_url = str(html_path.parent) + "/"
        HTML(filename=str(html_path), base_url=base_url).write_pdf(str(tmp_pdf))

        # Convert first page of PDF to PNG
        try:
            from pdf2image import convert_from_path
            images = convert_from_path(str(tmp_pdf), first_page=1, last_page=1, dpi=96)
            if images:
                images[0].save(str(out_png))
                print(f"  ✅ WeasyPrint screenshot saved: {out_png}")
                return True
        except ImportError:
            print("  ⚠  pdf2image not installed. Saving PDF instead of PNG.")
            shutil.copy(str(tmp_pdf), str(out_png.with_suffix(".pdf")))
            return True
    finally:
        if tmp_pdf.exists():
            tmp_pdf.unlink()
    return False


def make_side_by_side(left: Path, right: Path, out: Path) -> None:
    """Create a side-by-side PNG comparison if Pillow is available."""
    try:
        from PIL import Image, ImageDraw, ImageFont
    except ImportError:
        print("  ⚠  Pillow not installed. Skipping side-by-side composite.")
        return

    if not left.exists() or not right.exists():
        return

    img_l = Image.open(str(left))
    img_r = Image.open(str(right))

    # Resize to same height
    h = max(img_l.height, img_r.height)
    if img_l.height != h:
        img_l = img_l.resize((int(img_l.width * h / img_l.height), h))
    if img_r.height != h:
        img_r = img_r.resize((int(img_r.width * h / img_r.height), h))

    label_h = 40
    total_w = img_l.width + img_r.width + 20
    composite = Image.new("RGB", (total_w, h + label_h), color="#2d2d2d")

    composite.paste(img_l, (0, label_h))
    composite.paste(img_r, (img_l.width + 20, label_h))

    draw = ImageDraw.Draw(composite)
    draw.text((img_l.width // 2 - 80, 8), "Chrome Preview (Playwright)", fill="white")
    draw.text((img_l.width + 20 + img_r.width // 2 - 80, 8), "WeasyPrint PDF", fill="#ff6b6b")

    composite.save(str(out))
    print(f"  ✅ Side-by-side comparison: {out}")


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="compare_preview.py",
        description="Visual diff: Chrome preview vs WeasyPrint PDF for a single page.",
    )
    parser.add_argument("html_file", type=Path, help="Path to a page HTML file (e.g. pages/page_101.html)")
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR, help="Output directory for PNGs")
    parser.add_argument("--no-weasyprint", action="store_true", help="Skip WeasyPrint rendering")
    parser.add_argument("--chrome-path", type=str, default=None, help="Explicit Chrome executable path")
    args = parser.parse_args()

    html_path = args.html_file.resolve()
    if not html_path.exists():
        print(f"❌ File not found: {html_path}")
        sys.exit(1)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    stem = html_path.stem

    chrome_png = args.output_dir / f"{stem}_chrome.png"
    weasy_png  = args.output_dir / f"{stem}_weasyprint.png"
    diff_png   = args.output_dir / f"{stem}_comparison.png"

    print(f"🔍 Comparing: {html_path.name}")
    print(f"   Output dir: {args.output_dir}\n")

    print("📸 Rendering with Chrome (Playwright)...")
    chrome_ok = render_chrome_screenshot(html_path, chrome_png, args.chrome_path)

    if not args.no_weasyprint:
        print("\n📸 Rendering with WeasyPrint...")
        weasy_ok = render_weasyprint_screenshot(html_path, weasy_png)
    else:
        weasy_ok = False

    if chrome_ok and weasy_ok:
        print("\n🖼  Creating side-by-side comparison...")
        make_side_by_side(chrome_png, weasy_png, diff_png)

    print(f"\n✅ Done. Open {args.output_dir} to view results.")


if __name__ == "__main__":
    main()

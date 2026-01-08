from playwright.sync_api import sync_playwright, expect
import os

def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        page = context.new_page()

        # Resolve absolute paths
        cwd = os.getcwd()
        frontmatter_path = f"file://{cwd}/pages/00_frontmatter.html"
        cover_path = f"file://{cwd}/pages/00_cover.html"

        print(f"Checking {frontmatter_path}...")
        page.goto(frontmatter_path)

        # Verify Font Family on Body
        body_font = page.evaluate("getComputedStyle(document.body).fontFamily")
        print(f"Body Font: {body_font}")
        # Note: Computed style might return quotes or not depending on browser
        if "Noto Naskh Arabic" not in body_font:
             print("WARNING: Body font does not seem to contain 'Noto Naskh Arabic'")

        # Verify Focus Point Border Color
        focus_point = page.locator(".focus-point")
        if focus_point.count() > 0:
            border_right_color = focus_point.evaluate("el => getComputedStyle(el).borderRightColor")
            print(f"Focus Point Border Right Color: {border_right_color}")
            # rgb(230, 74, 25) is #E64A19
            if "rgb(230, 74, 25)" not in border_right_color:
                print("WARNING: Focus Point border color mismatch!")
        else:
            print("ERROR: .focus-point not found in frontmatter")

        # Screenshot Frontmatter
        page.screenshot(path="verification/frontmatter.png")

        print(f"Checking {cover_path}...")
        page.goto(cover_path)

        # Verify Subtitle Color (should be --color-secondary -> #263238 -> rgb(38, 50, 56))
        subtitle = page.locator(".sub-title")
        if subtitle.count() > 0:
            color = subtitle.evaluate("el => getComputedStyle(el).color")
            print(f"Subtitle Color: {color}")
            if "rgb(38, 50, 56)" not in color:
                print("WARNING: Subtitle color mismatch!")
        else:
            print("ERROR: .sub-title not found in cover")

        # Screenshot Cover
        page.screenshot(path="verification/cover.png")

        browser.close()

if __name__ == "__main__":
    run()

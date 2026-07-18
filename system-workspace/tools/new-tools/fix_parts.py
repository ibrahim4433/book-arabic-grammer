import glob
import os
import re

from bs4 import BeautifulSoup


def convert_to_arabic_numeral(num):
    arabic_digits = {
        "0": "٠",
        "1": "١",
        "2": "٢",
        "3": "٣",
        "4": "٤",
        "5": "٥",
        "6": "٦",
        "7": "٧",
        "8": "٨",
        "9": "٩",
    }
    return "".join(arabic_digits.get(d, d) for d in str(num))


def fix_html_files():
    files = glob.glob("pages/*.html")
    for filepath in files:
        if "TOC" in filepath or "Answers" in filepath:
            continue

        with open(filepath, encoding="utf-8") as f:
            content = f.read()

        # Remove from <title>
        content = re.sub(r"(<title>.*?)\s*\(الْجُزْءُ [^\)]+\)(.*?</title>)", r"\1\2", content)
        # Remove from <h1>
        content = re.sub(r"(<h1[^>]*>.*?)\s*\(الْجُزْءُ [^\)]+\)(.*?</h1>)", r"\1\2", content)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)

        # Rename file
        filename = os.path.basename(filepath)
        new_filename = re.sub(r"\s*\(الْجُزْءُ [^\)]+\)", "", filename)
        new_filename = re.sub(r"_\d(?=\.html)", "", new_filename)  # remove _2.html -> .html
        if filename != new_filename:
            os.rename(filepath, os.path.join("pages", new_filename))
            print(f"Renamed: {filename} -> {new_filename}")


def fix_toc():
    for filepath in glob.glob("pages/*TOC*.html"):
        with open(filepath, encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        # We need to find all tr in the table.
        # But we shouldn't just parse and overwrite with BS4 if it breaks formatting.
        # Let's do it carefully with BS4.
        tables = soup.find_all("table")
        for table in tables:
            trs = table.find_all("tr")
            seen_titles = set()
            for tr in trs:
                tds = tr.find_all("td")
                if not tds:
                    continue
                # title is usually in the first or second td. Let's look for font-bold.
                title_td = tr.find("td", class_="font-bold")
                if title_td:
                    title_text = title_td.get_text().strip()
                    # Clean title
                    clean_title = re.sub(r"\s*\(الْجُزْءُ [^\)]+\)", "", title_text)
                    if clean_title != title_text:
                        title_td.string = clean_title

                    if clean_title in seen_titles:
                        tr.decompose()  # Remove this tr!
                    else:
                        seen_titles.add(clean_title)

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))
        print(f"Fixed TOC: {filepath}")


def fix_answers():
    filepath = "pages/98.00_p120_Answers.html"
    if not os.path.exists(filepath):
        return

    with open(filepath, encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")

    # We have <div class="block-header accent"> and <div class="block-body"> directly as siblings
    # Let's group them.
    headers = soup.find_all("div", class_="block-header")

    merged_blocks = {}  # base_title -> list of li tags

    for header in headers:
        title_span = header.find("span")
        if not title_span:
            continue
        title_text = title_span.get_text().strip()

        # Base title
        base_title = re.sub(r"\s*\(الْجُزْءُ [^\)]+\)", "", title_text)
        base_title = re.sub(r"_\d$", "", base_title)

        if base_title not in merged_blocks:
            merged_blocks[base_title] = []

        # The next sibling that is a div with class block-body
        body = header.find_next_sibling("div", class_="block-body")
        if body:
            lis = body.find_all("li")
            merged_blocks[base_title].extend(lis)

            # Decompose original header and body
            body.decompose()
        header.decompose()

    # Now append new merged blocks to the wrapper
    wrapper = soup.find("div", class_="force-new-page")
    if not wrapper:
        wrapper = soup.body

    for title, lis in merged_blocks.items():
        # Create block-header
        header_div = soup.new_tag("div", attrs={"class": "block-header accent"})
        span = soup.new_tag("span")
        span.string = title
        header_div.append(span)

        # Create block-body
        body_div = soup.new_tag("div", attrs={"class": "block-body"})
        ul = soup.new_tag("ul", attrs={"class": "structured-list"})

        # Renumber lis
        for i, li in enumerate(lis):
            marker = li.find("span", class_="marker")
            if marker:
                marker.string = convert_to_arabic_numeral(i + 1)
            ul.append(li)

        body_div.append(ul)

        wrapper.append(header_div)
        wrapper.append(body_div)

    with open(filepath, "w", encoding="utf-8") as f:
        # Avoid bs4 writing html entities for arabic
        f.write(soup.encode(formatter=None).decode("utf-8"))

    print("Fixed Answers.")


if __name__ == "__main__":
    fix_html_files()
    fix_toc()
    fix_answers()

import glob
import re

from bs4 import BeautifulSoup


def fix_toc():
    for filepath in glob.glob("pages/*TOC*.html"):
        with open(filepath, encoding="utf-8") as f:
            soup = BeautifulSoup(f.read(), "html.parser")

        tables = soup.find_all("table")
        for table in tables:
            trs = table.find_all("tr")
            seen_titles = set()
            for tr in list(trs):  # iterate over a copy so we can decompose
                title_td = tr.find("td", class_="font-bold")
                if title_td:
                    title_text = title_td.get_text().strip()
                    # Use a broader regex to catch all parts
                    # including possible zero-width spaces or weird characters
                    clean_title = re.sub(r"\(الْجُزْءُ.*?\)", "", title_text)
                    clean_title = clean_title.strip()

                    if clean_title != title_text:
                        title_td.string = clean_title

                    if clean_title in seen_titles:
                        tr.decompose()
                    else:
                        seen_titles.add(clean_title)

        # We also need to fix <h1> titles in TOC if they have parts
        for h1 in soup.find_all("h1"):
            if "(الْجُزْءُ" in h1.get_text():
                clean = re.sub(r"\(الْجُزْءُ.*?\)", "", h1.get_text()).strip()
                h1.string = clean

        with open(filepath, "w", encoding="utf-8") as f:
            f.write(soup.encode(formatter=None).decode("utf-8"))
        print(f"Fixed TOC: {filepath}")


if __name__ == "__main__":
    fix_toc()

import glob
import os

from bs4 import BeautifulSoup


def extract_content(file_path):
    with open(file_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    title = soup.find("title")
    title_text = title.text if title else os.path.basename(file_path)

    content = [
        f"\n{'=' * 50}\nFile: {os.path.basename(file_path)}\nTitle: {title_text}\n{'=' * 50}"
    ]

    # Find all section headers and bodies
    sections = soup.find_all("section")
    if not sections:
        content.append(soup.get_text(separator=" ", strip=True))
    else:
        for sec in sections:
            header = sec.find(class_="block-header")
            body = sec.find(class_="block-body")

            header_text = header.get_text(separator=" ", strip=True) if header else ""
            body_text = (
                body.get_text(separator=" ", strip=True)
                if body
                else sec.get_text(separator=" ", strip=True)
            )

            if header_text:
                content.append(f"\n--- {header_text} ---")
            content.append(body_text)

    return "\n".join(content)


c1_files = sorted(glob.glob("pages/C1/*.html"))
c2_files = sorted(glob.glob("pages/C2/*.html"))

with open("all_content.txt", "w", encoding="utf-8") as out:
    out.write("C1 CONTENT\n" + "#" * 50 + "\n")
    for f in c1_files:
        out.write(extract_content(f) + "\n")

    out.write("\n\nC2 CONTENT\n" + "#" * 50 + "\n")
    for f in c2_files:
        out.write(extract_content(f) + "\n")

print("Done extracting!")

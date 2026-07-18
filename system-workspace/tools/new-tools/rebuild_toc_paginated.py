import glob
import re

from bs4 import BeautifulSoup

ar_to_en = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")
en_to_ar = str.maketrans("0123456789", "٠١٢٣٤٥٦٧٨٩")

# Step 1: Collect and sort all 34 Answer entries from the backup files
entries = []
for f in glob.glob("backup_answers/98.*.html"):
    m = re.search(r"_p([0-9]+)_", f)
    if not m:
        continue
    page = int(m.group(1))

    text = open(f, encoding="utf-8").read()
    headers = re.findall(r"إِجَابَاتُ[^<]+", text)
    lessons = []
    for h in headers:
        m2 = re.search(r"الدَّرْسُ\s*([0-9]+)", h)
        if m2:
            lessons.append(int(m2.group(1)))

    if lessons:
        lessons = sorted(list(set(lessons)))
        entries.append((lessons, page))

entries.sort(key=lambda x: x[0][0])

answer_blocks = []
for lessons, page in entries:
    if len(lessons) > 2:
        lessons_str = " وَ ".join(str(l) for l in lessons)
        title = f"إِجَابَاتُ الدُّرُوسِ {lessons_str}".translate(en_to_ar)
    elif len(lessons) == 2:
        title = f"إِجَابَاتُ الدَّرْسِ {lessons[0]} وَ {lessons[1]}".translate(en_to_ar)
    else:
        title = f"إِجَابَاتُ الدَّرْسِ {lessons[0]}".translate(en_to_ar)
    ar_page = str(page).translate(en_to_ar)

    # We will represent an item as a tuple of 3 HTML strings for the <td>s
    td1 = '<td class="text-center font-bold text-grey bg-grey-lighter">٩٨</td>'
    td2 = f'<td class="font-bold bg-grey-lighter">{title}</td>'
    td3 = f'<td class="text-center font-bold text-primary bg-grey-lighter">{ar_page}</td>'
    answer_blocks.append([td1, td2, td3])

# Step 2: Read the lessons from 00.3_TOC.html.bak
with open("pages/00.3_TOC.html.bak", encoding="utf-8") as f:
    html_content = f.read()

soup = BeautifulSoup(html_content, "html.parser")
tbody = soup.find("tbody")

lesson_blocks = []
for tr in tbody.find_all("tr"):
    tds = tr.find_all("td")
    if len(tds) >= 3:
        lesson_num = tds[0].get_text(strip=True)
        if lesson_num.translate(ar_to_en) != "98":
            lesson_blocks.append([str(tds[0]), str(tds[1]), str(tds[2])])

# Total items
all_items = lesson_blocks + answer_blocks


# We want 24 rows per page = 48 items per page
def chunk_items(items, max_rows):
    pages = []
    for i in range(0, len(items), max_rows * 2):
        page_items = items[i : i + max_rows * 2]

        # Calculate rows for this page
        # If we have N items on this page, we need ceil(N / 2) rows.
        # Right column gets first half, Left column gets second half.
        num_items = len(page_items)
        rows_needed = (num_items + 1) // 2

        col1 = page_items[:rows_needed]
        col2 = page_items[rows_needed:]

        # Pad col2 if it's shorter
        while len(col2) < rows_needed:
            col2.append(None)

        page_rows = list(zip(col1, col2))
        pages.append(page_rows)
    return pages


pages = chunk_items(all_items, 24)

# Create the HTML files
for page_idx, page_rows in enumerate(pages):
    page_soup = BeautifulSoup(html_content, "html.parser")
    page_tbody = page_soup.find("tbody")
    page_tbody.clear()

    # Update page id to avoid duplicates
    header = page_soup.find("header")
    if header and header.has_attr("id"):
        header["id"] = f"b516{page_idx + 2}"  # unique enough for now, auto-tag will fix

    for col1_item, col2_item in page_rows:
        tr = page_soup.new_tag("tr")

        # Right column (Visual right, HTML first)
        for td_str in col1_item:
            tr.append(BeautifulSoup(td_str, "html.parser"))

        # Spacer
        spacer = page_soup.new_tag("td", attrs={"class": "spacer-col"})
        tr.append(spacer)

        # Left column (Visual left, HTML second)
        if col2_item:
            for td_str in col2_item:
                tr.append(BeautifulSoup(td_str, "html.parser"))
        else:
            # Empty cells
            td1 = page_soup.new_tag("td", attrs={"class": "text-center font-bold text-grey"})
            td2 = page_soup.new_tag("td", attrs={"class": "font-bold"})
            td3 = page_soup.new_tag("td", attrs={"class": "text-center font-bold text-primary"})
            tr.append(td1)
            tr.append(td2)
            tr.append(td3)

        page_tbody.append(tr)

    filename = f"pages/00.{3 + page_idx}_TOC.html"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(str(page_soup))
    print(f"Generated {filename}")

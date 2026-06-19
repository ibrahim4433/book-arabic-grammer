from bs4 import BeautifulSoup

def inject_notes(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")

    container = soup.find("div", class_="force-new-page")
    if not container:
        container = soup.body

    notes_html = """
    <section class="content-block" id="b_auto_notes">
        <div class="block-header accent">
            <span>ملاحظات إضافية</span>
        </div>
        <div class="block-body">
            <div class="benefit-box mt-0 p-2mm border-light">
                <p class="m-0 text-grey-dark">مساحة لتدوين الملاحظات والفوائد الإضافية...</p>
                <div class="h-8mm"></div>
                <div class="h-8mm"></div>
                <div class="h-8mm"></div>
            </div>
        </div>
    </section>
    """
    new_block = BeautifulSoup(notes_html, "html.parser")
    container.append(new_block)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(str(soup))

inject_notes("pages/12.1_nXX_الضَّمَائِرُ (الجزء الثاني)_تابع.html")

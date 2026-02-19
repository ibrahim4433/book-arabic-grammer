import os
import sys
import subprocess
import json
from bs4 import BeautifulSoup

PAGES_DIR = "pages/"
VERIFY_SCRIPT = "Jules workspace/verify_layout.py"

def get_blank_space(filepath):
    """Runs verify_layout.py and returns the blank space percentage."""
    try:
        # Check if VERIFY_SCRIPT exists
        if not os.path.exists(VERIFY_SCRIPT):
            print(f"Verify script not found at {VERIFY_SCRIPT}")
            return 0

        cmd = [sys.executable, VERIFY_SCRIPT, filepath]
        result = subprocess.run(cmd, capture_output=True, text=True)
        output = result.stdout.strip()

        try:
            data = json.loads(output)
            return float(data.get("blank_space_percentage", 0.0))
        except json.JSONDecodeError:
            print(f"Failed to parse verify_layout output for {filepath}: {output[:50]}...")
            return 0.0

    except Exception as e:
        print(f"Error checking whitespace for {filepath}: {e}")
        return 0.0

def inject_content(filepath, blank_pct):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    soup = BeautifulSoup(content, "html.parser")
    modified = False

    body = soup.body
    container = soup.find("div", class_="force-new-page")
    if not container:
        container = body

    # Check existing elements to avoid duplication
    has_notes = False
    for header in soup.find_all("div", class_="block-header"):
        if "ملاحظات" in header.get_text():
            has_notes = True
            break

    # Heuristics for injection
    # 30% is a good threshold for adding a notes box
    if not has_notes and blank_pct > 30:
        notes_html = """
        <section class="content-block" id="b_auto_notes">
            <div class="block-header accent">
                <span>ملاحظات إضافية</span>
            </div>
            <div class="block-body">
                <div class="benefit-box mt-0 p-2mm border-dashed">
                    <p class="m-0 text-grey-dark">مساحة لتدوين الملاحظات والفوائد الإضافية...</p>
                    <div class="h-20mm"></div>
                </div>
            </div>
        </section>
        """
        new_block = BeautifulSoup(notes_html, "html.parser")
        container.append(new_block)
        modified = True
        print(f" injected Notes block.")

    # Check for Exam Block
    exam_block = None
    for section in container.find_all("section", class_="content-block"):
        header = section.find("div", class_="block-header")
        if header and ("اختبر" in header.get_text() or "أسئلة" in header.get_text()):
            exam_block = section
            break

    # If plenty of space (>40%), add more questions
    if blank_pct > 40:
        if exam_block:
            body_div = exam_block.find("div", class_="block-body")
            if body_div:
                # Add 2 placeholder questions
                questions_html = """
                <div class="exam-question">
                    <p class="m-0 mb-2mm font-bold"><span class="exam-number">?</span> سؤال إضافي: ............................................</p>
                    <div class="border-light h-8mm bg-grey-lighter rounded"></div>
                </div>
                <div class="exam-question mb-0 border-none">
                    <p class="m-0 mb-2mm font-bold"><span class="exam-number">?</span> سؤال إضافي: ............................................</p>
                    <div class="border-light h-8mm bg-grey-lighter rounded"></div>
                </div>
                """
                new_qs = BeautifulSoup(questions_html, "html.parser")
                body_div.append(new_qs)
                modified = True
                print(f" injected Exam questions.")
        else:
            # Create Exam Block if missing
            exam_html = """
            <section class="content-block" id="b_auto_exam">
                <div class="block-header bg-dark">
                    <span>📝 اختبر نفسك</span>
                </div>
                <div class="block-body">
                    <div class="exam-question">
                        <p class="m-0 mb-2mm font-bold"><span class="exam-number">1</span> سؤال تطبيقي: ............................................</p>
                        <div class="border-light h-8mm bg-grey-lighter rounded"></div>
                    </div>
                    <div class="exam-question">
                        <p class="m-0 mb-2mm font-bold"><span class="exam-number">2</span> سؤال تطبيقي: ............................................</p>
                        <div class="border-light h-8mm bg-grey-lighter rounded"></div>
                    </div>
                </div>
            </section>
            """
            new_exam = BeautifulSoup(exam_html, "html.parser")
            container.append(new_exam)
            modified = True
            print(f" created Exam block.")

    if modified:
        print(f"Filled whitespace in: {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))

def main():
    if not os.path.exists(PAGES_DIR):
        print(f"Directory {PAGES_DIR} not found.")
        return

    files = sorted([f for f in os.listdir(PAGES_DIR) if f.endswith(".html")])

    for filename in files:
        filepath = os.path.join(PAGES_DIR, filename)

        # Run verify to check whitespace
        blank_pct = get_blank_space(filepath)

        if blank_pct > 30:
            print(f"High whitespace detected in {filename} ({blank_pct}%)")
            try:
                inject_content(filepath, blank_pct)
            except Exception as e:
                print(f"Error injecting content in {filename}: {e}")

if __name__ == "__main__":
    main()

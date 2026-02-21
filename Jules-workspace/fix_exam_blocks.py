import os
import sys
from bs4 import BeautifulSoup

# Add the current directory to sys.path so we can import if needed,
# though for this standalone script standard libs might suffice.

PAGES_DIR = "pages/"

def fix_exam_blocks(filepath):
    """
    Scans the file for .exam-question and .exercise-question blocks.
    Removes answer text.
    Ensures an empty answer placeholder exists.
    """
    with open(filepath, "r", encoding="utf-8") as f:
        html_content = f.read()

    soup = BeautifulSoup(html_content, "html.parser")
    modified = False

    # Find all question blocks
    question_blocks = soup.select(".exam-question, .exercise-question")

    for block in question_blocks:
        # 1. Identify Question vs Answer content
        # Strategy: Keep the first <p> (Question), remove others (Answers).
        # OR: Keep <p> that starts with 'س' or is bold?
        # Safe bet: First <p> is question.

        paragraphs = block.find_all("p")

        # If no paragraphs, skip (empty block?)
        if not paragraphs:
            continue

        # Keep the first paragraph (Question)
        question_p = paragraphs[0]

        # Remove subsequent paragraphs which are likely answers
        # Especially if they have text-grey-dark or start with 'ج'
        for p in paragraphs[1:]:
            # Check if it looks like an answer
            text = p.get_text().strip()
            if text.startswith("ج") or "text-grey-dark" in p.get("class", []):
                p.decompose()
                modified = True
            else:
                # If it doesn't look like an answer explicitly,
                # but we are in a question block, it's probably an answer explanation.
                # STRICT RULE: No answers. Remove it.
                p.decompose()
                modified = True

        # 2. Ensure Empty Answer Box exists
        # Standard Box: <div class="border-light h-8mm bg-grey-lighter rounded"></div>
        answer_box = block.find("div", class_="border-light")

        if answer_box:
            # Check if it has content (it shouldn't)
            if answer_box.get_text().strip():
                answer_box.clear()
                modified = True
        else:
            # Create it
            new_box = soup.new_tag("div", attrs={"class": "border-light h-8mm bg-grey-lighter rounded"})
            block.append(new_box)
            modified = True

        # Ensure 'mb-5mm' or similar spacing if needed?
        # The standard is .exam-question usually handles margin, but .exercise-question might need it.

    if modified:
        print(f"Fixed exam blocks in: {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(str(soup))

def main():
    if not os.path.exists(PAGES_DIR):
        print(f"Directory {PAGES_DIR} not found.")
        return

    files = sorted([f for f in os.listdir(PAGES_DIR) if f.endswith(".html")])

    for filename in files:
        filepath = os.path.join(PAGES_DIR, filename)
        try:
            fix_exam_blocks(filepath)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    main()

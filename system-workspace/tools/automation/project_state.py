import json
import os
import re
import sys

STATE_FILE = os.path.join(os.path.dirname(__file__), "project_state.json")


class ProjectState:
    def __init__(self):
        self.state = {
            "current_lesson_number": "",
            "current_lesson_title": "",
            "current_page_index": 0,
            "last_section_title": "",
            "last_file": "",
        }
        self.load()

    def load(self):
        if os.path.exists(STATE_FILE):
            try:
                with open(STATE_FILE, encoding="utf-8") as f:
                    self.state = json.load(f)
            except Exception as e:
                print(f"Error loading state: {e}")

    def save(self):
        try:
            with open(STATE_FILE, "w", encoding="utf-8") as f:
                json.dump(self.state, f, indent=2, ensure_ascii=False)
            print(f"State saved to {STATE_FILE}")
        except Exception as e:
            print(f"Error saving state: {e}")

    def extract_metadata(self, filepath):
        if not os.path.exists(filepath):
            return None

        try:
            with open(filepath, encoding="utf-8") as f:
                content = f.read()
        except Exception as e:
            print(f"Error reading file {filepath}: {e}")
            return None

        meta = {}

        # Extract Page Index from filename (e.g., ..._n03_...)
        filename = os.path.basename(filepath)
        match_idx = re.search(r"_n(\d+)_", filename)
        if match_idx:
            meta["page_index"] = int(match_idx.group(1))
        else:
            meta["page_index"] = 0

        # Extract Lesson Number
        match_num = re.search(r'<div class="lesson-number">([^<]+)</div>', content)
        meta["lesson_number"] = match_num.group(1).strip() if match_num else ""

        # Extract Lesson Title
        match_title = re.search(r'<h1 class="header-title">([^<]+)</h1>', content)
        meta["lesson_title"] = match_title.group(1).strip() if match_title else ""

        # Extract Last Section Title
        # We look for block-header spans.
        # This regex finds all spans inside block-headers (assuming simple structure)
        # <div class="block-header...>\s*<span>...</span>
        # We might need to be more robust for attributes in span
        headers = re.findall(
            r'<div class="block-header[^"]*">\s*<span[^>]*>([^<]+)</span>', content
        )
        if headers:
            meta["last_section"] = headers[-1].strip()
        else:
            meta["last_section"] = ""

        return meta

    def update(self, filepath):
        meta = self.extract_metadata(filepath)
        if not meta:
            print("Failed to extract metadata.")
            sys.exit(1)

        self.state["current_lesson_number"] = meta.get("lesson_number", "")
        self.state["current_lesson_title"] = meta.get("lesson_title", "")
        self.state["current_page_index"] = meta.get("page_index", 0)
        self.state["last_section_title"] = meta.get("last_section", "")
        self.state["last_file"] = filepath
        self.save()

    def verify(self, filepath):
        meta = self.extract_metadata(filepath)
        if not meta:
            print(json.dumps({"status": "FAIL", "message": "Could not read file"}))
            sys.exit(1)

        # Compare with state
        issues = []

        # Logic: We flag if the new page seems to be a continuation (same lesson number)
        # but has a DIFFERENT title.
        # If lesson number changes, we assume it's a new lesson and title SHOULD change.

        stored_num = self.state.get("current_lesson_number", "")
        stored_title = self.state.get("current_lesson_title", "")

        new_num = meta.get("lesson_number", "")
        new_title = meta.get("lesson_title", "")

        if new_num == stored_num and new_num != "":
            if new_title != stored_title:
                issues.append(
                    f"Title Mismatch: Expected '{stored_title}' (from active lesson {stored_num}), found '{new_title}'."
                )

        # Check page index continuity
        stored_idx = self.state.get("current_page_index", 0)
        new_idx = meta.get("page_index", 0)

        # If new index is not stored_idx + 1, warn (unless it's 0 or something)
        # But maybe we are verifying the *current* file which IS stored_idx?
        # Assuming we verify a NEW file.
        if new_idx > 0 and stored_idx > 0:
            if new_idx != stored_idx + 1:
                # Just a warning, maybe we skipped a page or are verifying an old one
                pass
                # issues.append(f"Page Index Jump: Last processed was n{stored_idx:02d}, this is n{new_idx:02d}.")

        if issues:
            print(
                json.dumps(
                    {
                        "status": "WARN",
                        "issues": issues,
                        "current_state": self.state,
                        "file_metadata": meta,
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            sys.exit(1)  # Fail if inconsistencies found
        else:
            print(
                json.dumps(
                    {
                        "status": "PASS",
                        "message": "Header is consistent with project state.",
                        "file_metadata": meta,
                    },
                    ensure_ascii=False,
                    indent=2,
                )
            )
            sys.exit(0)


def main():
    if len(sys.argv) < 2:
        print("Usage: python tools/project_state.py [init|read|update <file>|verify <file>]")
        sys.exit(1)

    cmd = sys.argv[1]
    ps = ProjectState()

    if cmd == "init":
        ps.state = {
            "current_lesson_number": "",
            "current_lesson_title": "",
            "current_page_index": 0,
            "last_section_title": "",
            "last_file": "",
        }
        ps.save()

    elif cmd == "read":
        print(json.dumps(ps.state, indent=2, ensure_ascii=False))

    elif cmd == "update":
        if len(sys.argv) < 3:
            print("Usage: update <filepath>")
            sys.exit(1)
        ps.update(sys.argv[2])

    elif cmd == "verify":
        if len(sys.argv) < 3:
            print("Usage: verify <filepath>")
            sys.exit(1)
        ps.verify(sys.argv[2])

    else:
        print(f"Unknown command: {cmd}")
        sys.exit(1)


if __name__ == "__main__":
    main()

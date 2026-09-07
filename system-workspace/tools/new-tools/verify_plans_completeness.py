#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path
from difflib import SequenceMatcher
from collections import defaultdict

try:
    from rich.console import Console
    from rich.table import Table
    has_rich = True
except ImportError:
    has_rich = False

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent

def strip_diacritics(text):
    # Arabic diacritics
    diacritics = re.compile(r'[\u064B-\u065F\u0670]')
    text = re.sub(diacritics, '', text)
    # Normalize common OCR letters
    text = re.sub(r'[إأآا]', 'ا', text)
    text = re.sub(r'ة', 'ه', text)
    text = re.sub(r'ى', 'ي', text)
    return text

def clean_markdown(text):
    # Remove markdown/html
    text = re.sub(r'<[^>]+>', ' ', text) # HTML tags
    text = re.sub(r'\[.*?\]\(.*?\)', ' ', text) # links
    text = re.sub(r'#.*', ' ', text) # headers
    text = re.sub(r'```.*?```', ' ', text, flags=re.DOTALL) # code blocks
    text = re.sub(r'\[.*?\]', ' ', text) # Template placeholders like [CONTENT]
    text = re.sub(r'===.*?===', ' ', text) # Block markers
    text = re.sub(r'\*\*', '', text) # bold
    text = re.sub(r'__', '', text) # bold/underline
    # Remove english letters and non-arabic punctuation/symbols
    text = re.sub(r'[a-zA-Z0-9_\-=\+\[\]\{\}\(\):;"\'\.,!؟\n\r\/\\\|~`]', ' ', text)
    return text

def get_raw_slice(raw_lines, start_marker, end_marker):
    extracted = []
    capturing = False
    start_pattern = f"[{start_marker}]"
    end_pattern = f"[{end_marker}]"
    for line in raw_lines:
        if start_pattern in line:
            capturing = True
        if capturing:
            clean_line = re.sub(r"^\[.*?\]\s*", "", line)
            extracted.append(clean_line)
        if end_pattern in line:
            capturing = False
            break
    return "\n".join(extracted)

def verify_plans():
    plans_dir = PROJECT_ROOT / "plans"
    index_path = PROJECT_ROOT / "system-workspace/text-data/raw_to_lesson_index.json"
    raw_path = PROJECT_ROOT / "system-workspace/text-data/full_raw_indexed.txt"
    
    if not plans_dir.exists() or not index_path.exists() or not raw_path.exists():
        print("Missing required directories/files.")
        return

    mapping = json.loads(index_path.read_text(encoding="utf-8"))
    raw_lines = raw_path.read_text(encoding="utf-8").splitlines()
    
    if has_rich:
        console = Console()
        table = Table(title="Plan Completeness Report (Aggregated by Lesson)")
        table.add_column("Lesson", style="magenta")
        table.add_column("Files Analysed", style="cyan")
        table.add_column("Missing Parts", style="red")
        table.add_column("Score", justify="right")
        table.add_column("Rating", style="bold")
    
    # Group by lesson number
    lesson_groups = defaultdict(list)
    for plan_file in plans_dir.glob("*.md"):
        filename = plan_file.name
        # Match format: 001.3_nXXX_TITLE-plan.md OR 001-TITLE-plan.md
        match = re.match(r'^(\d+)(?:\.(\d+))?', filename)
        if not match: continue
        
        lesson_num_str = match.group(1)
        part_num = match.group(2) if match.group(2) else "1"
        lesson_groups[lesson_num_str].append((int(part_num), plan_file))
        
    for lesson_num_str, files in lesson_groups.items():
        # Sort files by part number
        files.sort(key=lambda x: x[0])
        
        # Find mapping
        range_info = None
        lesson_title = ""
        for title, info in mapping.items():
            t_match = re.match(r"^(\d+)\s*-\s*(.*)", title)
            if t_match and t_match.group(1).zfill(3) == lesson_num_str:
                range_info = info
                lesson_title = title
                break
            elif not t_match:
                clean_title = re.sub(r'[<>:"/\\|?*]', '', title.strip())
                if any(clean_title in f[1].name for f in files):
                    range_info = info
                    lesson_title = title
                    break
                    
        if not range_info:
            print(f"Skipping {lesson_num_str}, no mapping found.")
            continue
            
        # Combine all parts texts
        combined_plan_text = ""
        part_numbers_found = []
        for part_num, p_file in files:
            combined_plan_text += p_file.read_text(encoding="utf-8") + "\n"
            part_numbers_found.append(str(part_num))
            
        missing_parts = []
        # If it's 1-part mode (they have dots), assume we need parts 1,2,3,4
        if any("." in f[1].name for f in files):
            for i in range(1, 5):
                if str(i) not in part_numbers_found:
                    missing_parts.append(str(i))
            
        raw_text = get_raw_slice(raw_lines, range_info["start"], range_info["end"])
        
        clean_raw = strip_diacritics(clean_markdown(raw_text))
        clean_plan = strip_diacritics(clean_markdown(combined_plan_text))
        
        raw_words = [w for w in clean_raw.split() if w.strip()]
        plan_words = [w for w in clean_plan.split() if w.strip()]
        
        # Use Bigram overlap for robustness against template insertions
        raw_bigrams = set(zip(raw_words, raw_words[1:])) if len(raw_words) > 1 else set()
        plan_bigrams = set(zip(plan_words, plan_words[1:])) if len(plan_words) > 1 else set()
        
        if not raw_bigrams:
            score = 100.0
        else:
            missing_bigrams = raw_bigrams - plan_bigrams
            score = (1 - len(missing_bigrams)/len(raw_bigrams)) * 100
            
        rating = "A+" if score >= 90 else "A" if score >= 80 else "B" if score >= 70 else "C" if score >= 50 else "F"
        color = "green" if score >= 80 else "yellow" if score >= 50 else "red"
        
        missing_str = ",".join(missing_parts) if missing_parts else "None"
        files_str = f"{len(files)} parts"
        
        if has_rich:
            table.add_row(lesson_title, files_str, missing_str, f"[{color}]{score:.1f}%[/{color}]", f"[{color}]{rating}[/{color}]")
        else:
            print(f"Lesson: {lesson_title} | Parts: {files_str} | Missing Parts: {missing_str} | Score: {score:.1f}% | Rating: {rating}")
            
    if has_rich:
        console.print(table)

if __name__ == '__main__':
    verify_plans()

#!/usr/bin/env python3
import subprocess
import sys
from pathlib import Path

# --- CONFIGURATION ---
PROJECT_ROOT = Path(__file__).parent.parent.parent.parent
INPUT_DIR = PROJECT_ROOT / "input"
OUTPUT_RAW_DIR = PROJECT_ROOT / "system-workspace/text-data/raw"


def transcribe_image(image_path, output_path):
    print(f"👁️ Transcribing {image_path.name}...")
    # Correct syntax for headless mode: gemini --prompt "instruction with path"
    prompt = (
        f"Extract all Arabic text from the attached image {image_path} with full diacritics (Tashkeel). "
        "Preserve the structure exactly. "
        "Output ONLY the raw Arabic text. "
        "Do NOT add any introduction, explanation, or conversational filler. "
        "Do NOT say 'Here is the transcription'. "
        "Just output the text."
    )

    try:
        with open(output_path, "w", encoding="utf-8") as out_f:
            subprocess.run(
                ["gemini", "--prompt", prompt],
                stdout=out_f,
                stderr=subprocess.PIPE,
                check=True,
                text=True,
            )
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Error transcribing {image_path.name}: {e.stderr}")
        return False


def main():
    OUTPUT_RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Sort images numerically if possible
    def sort_key(p):
        try:
            return int(p.stem)
        except ValueError:
            return p.stem

    images = sorted(list(INPUT_DIR.glob("*.jpg")) + list(INPUT_DIR.glob("*.png")), key=sort_key)

    if not images:
        print("⚠️ No images found in input/ directory.")
        return

    print(f"🚀 Starting batch transcription of {len(images)} images...")

    for img in images:
        out_file = OUTPUT_RAW_DIR / f"raw_{img.stem}.txt"

        # SKIP if file exists AND is not empty
        if (
            out_file.exists() and out_file.stat().st_size > 50
        ):  # Check > 50 to avoid small "header" only files
            print(f"⏭️ Skipping {img.name} (already exists).")
            continue

        transcribe_image(img, out_file)

    print("✅ Process complete.")

    print("🧹 Cleaning raw text files...")
    cleaner_script_path = PROJECT_ROOT / "Jules-workspace/clean_raw_text.py"
    subprocess.run([sys.executable, str(cleaner_script_path), str(OUTPUT_RAW_DIR)], check=True)
    print("🧼 Cleaning complete.")


if __name__ == "__main__":
    main()

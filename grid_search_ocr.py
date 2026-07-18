import os
import time
import difflib
from PIL import Image, ImageEnhance
import pytesseract
from pdf2image import convert_from_path

PDF_PATH = "xxxz.pdf"
GT_PATHS = [
    "ground_truth_page1.txt",
    "ground_truth_page2.txt",
    "ground_truth_page3.txt"
]

def load_ground_truths():
    gts = []
    for path in GT_PATHS:
        with open(path, "r", encoding="utf-8") as f:
            gts.append(f.read())
    return gts

def calculate_accuracy(truth, result):
    # Using difflib to find similarity ratio
    return difflib.SequenceMatcher(None, truth, result).ratio()

def process_and_ocr(img, threshold, contrast, psm):
    # 1. Apply Contrast
    if contrast != 1.0:
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)
    
    # 2. Convert to Grayscale & Threshold
    if threshold > 0:
        img = img.convert('L')
        img = img.point(lambda p: 255 if p > threshold else 0)
    
    # 3. Perform OCR
    config = f"--oem 1 --psm {psm}"
    text = pytesseract.image_to_string(img, lang="ara", config=config)
    
    # 4. Basic Cleanup to match GT format
    cleaned_lines = []
    import re
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if re.match(r'^[\d\W_]+$', stripped) and len(stripped) > 5:
            continue
        stripped = re.sub(r'[•\.]{3,}', '•••', stripped)
        cleaned_lines.append(stripped)
        
    return "\n".join(cleaned_lines)

def run_grid_search():
    print("Loading PDF pages...")
    images = convert_from_path(PDF_PATH, dpi=300)
    gts = load_ground_truths()
    
    thresholds = [120, 130, 140, 150, 160]
    contrasts = [1.0, 1.5, 2.0]
    psms = [3, 4, 6]
    
    results = []
    
    total_runs = len(thresholds) * len(contrasts) * len(psms)
    current_run = 0
    
    start_time = time.time()
    
    print(f"Starting Grid Search: {total_runs} configurations...")
    for t in thresholds:
        for c in contrasts:
            for p in psms:
                current_run += 1
                page_accuracies = []
                for i, img in enumerate(images):
                    if i >= len(gts):
                        break
                    
                    # Process
                    text = process_and_ocr(img.copy(), t, c, p)
                    
                    # Evaluate
                    acc = calculate_accuracy(gts[i], text)
                    page_accuracies.append(acc)
                
                avg_acc = sum(page_accuracies) / len(page_accuracies)
                results.append({
                    "threshold": t,
                    "contrast": c,
                    "psm": p,
                    "accuracy": avg_acc
                })
                print(f"[{current_run}/{total_runs}] T={t} C={c} PSM={p} -> Accuracy: {avg_acc:.4f}")

    # Sort results
    results.sort(key=lambda x: x["accuracy"], reverse=True)
    
    print("\n" + "="*50)
    print("TOP 5 CONFIGURATIONS:")
    print("="*50)
    for i in range(5):
        res = results[i]
        print(f"{i+1}. Threshold: {res['threshold']}, Contrast: {res['contrast']}, PSM: {res['psm']} | Accuracy: {res['accuracy']:.4f}")
        
    print("\nBEST CONFIGURATION FOUND:")
    best = results[0]
    print(f"Threshold: {best['threshold']}")
    print(f"Contrast: {best['contrast']}")
    print(f"PSM: {best['psm']}")
    print(f"Time taken: {time.time() - start_time:.2f} seconds")
    
if __name__ == "__main__":
    run_grid_search()

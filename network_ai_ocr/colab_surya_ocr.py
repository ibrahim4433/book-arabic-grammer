# ==========================================
# CELL 1: INSTALL DEPENDENCIES
# ==========================================
# Copy and paste this into the first cell of your Colab Notebook and run it.

!apt-get update
!apt-get install -y poppler-utils
!pip install surya-ocr pdf2image Pillow torch


# ==========================================
# CELL 2: MOUNT DRIVE & RUN AI OCR
# ==========================================
# Copy and paste this into the second cell and run it.

import os
import gc
import torch
from PIL import Image
from pdf2image import convert_from_path
from google.colab import drive

# Import Surya OCR models
from surya.ocr import run_ocr
from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor

# 1. Mount Google Drive
print("🔗 Mounting Google Drive...")
drive.mount('/content/drive')

# 2. Configuration
OCR_FOLDER = '/content/drive/MyDrive/OCR'

if not os.path.exists(OCR_FOLDER):
    print(f"❌ Error: Folder '{OCR_FOLDER}' does not exist in your Google Drive.")
else:
    # Find the first PDF in the folder
    pdf_files = [f for f in os.listdir(OCR_FOLDER) if f.lower().endswith('.pdf')]
    
    if not pdf_files:
        print(f"❌ No PDF files found in {OCR_FOLDER}")
    else:
        pdf_filename = pdf_files[0]
        pdf_path = os.path.join(OCR_FOLDER, pdf_filename)
        out_filename = pdf_filename.rsplit('.', 1)[0] + "_ocr_output.txt"
        out_path = os.path.join(OCR_FOLDER, out_filename)
        
        print(f"📖 Found Document: {pdf_path}")
        
        # 3. Load Models into Pro VRAM
        print("⏳ Loading AI Models into GPU VRAM (This takes a minute)...")
        det_processor, det_model = load_det_processor(), load_det_model()
        rec_model, rec_processor = load_rec_model(), load_rec_processor()
        print("✅ AI Models Loaded!")
        
        # 4. Convert PDF to Images
        print("📸 Converting PDF pages to images (This might take a moment for 300 pages)...")
        # You can test with a subset by adding parameters: first_page=1, last_page=3
        images = convert_from_path(pdf_path, dpi=300)
        print(f"✅ Extracted {len(images)} pages.")
        
        # 5. Process Page by Page to Prevent VRAM Overflows
        print("🚀 Starting Expert AI OCR Page by Page...")
        
        # We write incrementally so if Colab disconnects, you keep your progress!
        with open(out_path, "w", encoding="utf-8") as f:
            for i, img in enumerate(images):
                print(f"   -> Processing Page {i+1}/{len(images)}...")
                
                # Run OCR for Arabic ("ar")
                predictions = run_ocr([img.convert("RGB")], [["ar"]], det_model, det_processor, rec_model, rec_processor)
                
                page_text = []
                if predictions and len(predictions) > 0:
                    for text_line in predictions[0].text_lines:
                        page_text.append(text_line.text)
                
                f.write(f"\n\n--- Page {i+1} ---\n\n")
                f.write("\n".join(page_text))
                
                # Critically important for 300 pages: clear the VRAM after every page
                torch.cuda.empty_cache()
                gc.collect()
                
        print(f"\n🎉 SUCCESS! The fully accurate Arabic OCR text has been saved to:")
        print(f"📁 {out_path}")

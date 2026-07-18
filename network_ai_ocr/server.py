from fastapi import FastAPI, UploadFile, File
import uvicorn
from PIL import Image
import io
import os
import gc
import torch

# Import Surya OCR (State-of-the-Art Document OCR)
from surya.ocr import run_ocr
from surya.model.detection.model import load_model as load_det_model, load_processor as load_det_processor
from surya.model.recognition.model import load_model as load_rec_model
from surya.model.recognition.processor import load_processor as load_rec_processor

app = FastAPI(title="Local AI OCR Server")

print("⏳ Loading AI Models... This may take a minute on the first run.")
# Load the detection and recognition models into memory once at startup
det_processor, det_model = load_det_processor(), load_det_model()
rec_model, rec_processor = load_rec_model(), load_rec_processor()
print("✅ AI Models Loaded and Ready!")

@app.post("/api/ocr")
async def process_image(file: UploadFile = File(...)):
    try:
        # Read the image sent from the client PC
        image_bytes = await file.read()
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        
        # Run the AI OCR (Language set to Arabic 'ar')
        # Surya handles layout detection and complex Arabic diacritics automatically
        predictions = run_ocr([image], [["ar"]], det_model, det_processor, rec_model, rec_processor)
        
        # Extract the ordered text lines
        text_lines = []
        if predictions and len(predictions) > 0:
            for text_line in predictions[0].text_lines:
                text_lines.append(text_line.text)
                
        # Optional: Free up memory if running on a small GPU
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
        gc.collect()

        return {"status": "success", "text": "\n".join(text_lines)}

    except Exception as e:
        return {"status": "error", "message": str(e)}

if __name__ == "__main__":
    # Run the server on all network interfaces so the current PC can connect to it
    uvicorn.run(app, host="0.0.0.0", port=8000)

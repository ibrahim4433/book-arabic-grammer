### `./network_ai_ocr/server.py`
- **Status:** Usable
- **Purpose:** Runs a local FastAPI server hosting Surya OCR models to process uploaded images and extract Arabic text.
- **Inputs:** Image files via POST request to `/api/ocr`
- **Outputs:** JSON response containing the extracted text string.
- **Usage:** `python3 ./network_ai_ocr/server.py` (runs on `0.0.0.0:8000`)
- **Workflow Integration:** This tool acts as an independent external utility for converting scanned documents to raw text. It sits upstream of the new '1-Plan-Per-Page' workflow, which expects the raw text (with page markers) as its input.

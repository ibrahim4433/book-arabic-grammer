### `./system-workspace/tools/automation/modules/pdf_ocr_local.py`
- **Status:** Usable
- **Purpose:** Extracts text from PDF files using local Tesseract OCR. It features smart image preprocessing (grayscale, thresholding), optimized OCR configurations for Arabic text, chunked processing for large PDFs, and a custom autocorrect dictionary to fix common Arabic OCR errors.
- **Inputs:** `pdf_path` (string: path to the source PDF file)
- **Outputs:** `output_txt_path` (string: path to the output raw text file)
- **Usage:** `python -c "from modules.pdf_ocr_local import LocalPDFOCR; ocr = LocalPDFOCR(); ocr.process_pdf('input.pdf', 'output.txt')"`
- **Workflow Integration:** This tool is typically used in the early stages of both workflows to convert raw source materials (PDFs) into text. Its output forms the foundational text that will eventually be sliced by page markers (for the '1-Plan-Per-Page' workflow) or by lessons (for the old workflow) before being fed to the Jules agent for planning.

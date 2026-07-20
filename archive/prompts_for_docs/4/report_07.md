### `system-workspace/tools/automation/modules/pdf_ocr_network.py`
- **Status:** Usable
- **Purpose:** Converts local PDF files into images page-by-page and sends them to a network AI server for OCR processing, returning the extracted text.
- **Inputs:** Local PDF file path, output TXT file path.
- **Outputs:** Extracted text saved to the specified TXT file.
- **Usage:** Instantiated as `NetworkPDFOCR(server_ip)` and called via `.process_pdf(pdf_path, output_txt_path)`.
- **Workflow Integration:** Acts as an alternative OCR ingestion method to Jules. Fits into the pre-processing stage to get raw text, which must then be manually paginated for the '1-Plan-Per-Page' engine.

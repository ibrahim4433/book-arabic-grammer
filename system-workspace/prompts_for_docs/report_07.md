### `./network_ai_ocr/colab_surya_ocr.py`
- **Status:** Usable
- **Purpose:** A script intended to be run in a Google Colab notebook to perform batch Arabic OCR on PDF files stored in Google Drive using Surya OCR. It converts PDF pages to images and writes the extracted text page-by-page.
- **Inputs:** PDF files from Google Drive (`/content/drive/MyDrive/OCR`)
- **Outputs:** Text file (`..._ocr_output.txt`) in the same Drive folder.
- **Usage:** Run inside a Google Colab cell.
- **Workflow Integration:** Similar to `server.py`, this is an upstream text generation utility. It is highly relevant to the new '1-Plan-Per-Page' workflow, as its page-by-page output format (`--- Page X ---`) aligns closely with the new raw text slicing requirement (`----- PAGE X -----`).

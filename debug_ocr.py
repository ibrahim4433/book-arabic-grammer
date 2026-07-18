import gradio as gr
from PIL import Image, ImageEnhance
import pytesseract
from pdf2image import convert_from_path
import tempfile

# Helper function to perform preprocessing and OCR
def process_image(img, threshold, contrast, psm_mode):
    # If the user hasn't provided an image, return empty
    if img is None:
        return None, "Please upload an image or PDF."
    
    # 1. Apply Contrast
    if contrast != 1.0:
        enhancer = ImageEnhance.Contrast(img)
        img = enhancer.enhance(contrast)
    
    # 2. Convert to Grayscale & Threshold
    if threshold > 0:
        img = img.convert('L')
        img = img.point(lambda p: 255 if p > threshold else 0)
    
    # 3. Perform OCR
    # Extract the number from the PSM mode string (e.g. "PSM 3" -> "3")
    psm_val = psm_mode.split(" ")[1]
    config = f"--oem 1 --psm {psm_val}"
    
    try:
        text = pytesseract.image_to_string(img, lang="ara", config=config)
    except Exception as e:
        text = f"Error during OCR: {e}"
        
    return img, text

def load_pdf_page(pdf_file, page_number):
    if pdf_file is None:
        return None
    try:
        images = convert_from_path(pdf_file.name, first_page=page_number, last_page=page_number, dpi=300)
        if images:
            return images[0]
        return None
    except Exception as e:
        print(f"Error loading PDF: {e}")
        return None

# Build the Gradio Interface
with gr.Blocks(title="OCR Visual Debugger") as app:
    gr.Markdown("# 🔍 OCR Visual Debugger for Arabic Grammar Book")
    gr.Markdown("Upload a single image or a PDF. Adjust the preprocessing sliders on the left to immediately see how the image looks, and what Tesseract extracts from it.")
    
    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 1. Input")
            input_image = gr.Image(type="pil", label="Upload Image directly")
            
            with gr.Accordion("Or extract from PDF", open=False):
                input_pdf = gr.File(file_types=[".pdf"], label="Upload PDF")
                page_slider = gr.Slider(minimum=1, maximum=100, step=1, value=1, label="Page Number")
                load_btn = gr.Button("Load PDF Page")
                
                def handle_load_pdf(pdf, p_num):
                    return load_pdf_page(pdf, p_num)
                
                load_btn.click(handle_load_pdf, inputs=[input_pdf, page_slider], outputs=[input_image])
            
            gr.Markdown("### 2. Configuration")
            threshold_slider = gr.Slider(minimum=0, maximum=255, step=1, value=140, label="Binarization Threshold (0 = Off)")
            contrast_slider = gr.Slider(minimum=0.5, maximum=3.0, step=0.1, value=1.0, label="Contrast Enhancement (1.0 = Original)")
            psm_dropdown = gr.Dropdown(
                choices=["PSM 1 (Auto with OSD)", "PSM 3 (Auto, no OSD)", "PSM 4 (Single column variable sizes)", "PSM 6 (Single uniform block)"],
                value="PSM 3 (Auto, no OSD)", 
                label="Page Segmentation Mode"
            )
            
            run_btn = gr.Button("Process & OCR", variant="primary")
            
        with gr.Column(scale=2):
            gr.Markdown("### 3. Debug Output")
            with gr.Row():
                output_image = gr.Image(type="pil", label="Preprocessed Image (What OCR sees)")
            with gr.Row():
                output_text = gr.TextArea(label="OCR Extracted Text", lines=20)
                
    # Event listeners
    run_btn.click(
        process_image, 
        inputs=[input_image, threshold_slider, contrast_slider, psm_dropdown], 
        outputs=[output_image, output_text]
    )
    
app.launch(server_name="0.0.0.0", server_port=7860, share=False)

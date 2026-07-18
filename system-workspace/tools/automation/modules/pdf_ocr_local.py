import os
import sys
import tempfile
from pathlib import Path

import pytesseract
from pdf2image import convert_from_path
from rich.console import Console
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn

console = Console()

class LocalPDFOCR:
    def __init__(self, languages="ara"):
        self.languages = languages
        # Check if tesseract is installed
        try:
            pytesseract.get_tesseract_version()
        except Exception:
            console.print("[red]❌ Tesseract OCR is not installed or not in PATH.[/red]")
            console.print("[yellow]Please run the following command in your WSL terminal to install it:[/yellow]")
            console.print("sudo apt-get update && sudo apt-get install -y tesseract-ocr tesseract-ocr-ara tesseract-ocr-eng poppler-utils")
            sys.exit(1)

    def process_pdf(self, pdf_path: str, output_txt_path: str):
        pdf_path = Path(pdf_path)
        output_txt_path = Path(output_txt_path)

        if not pdf_path.exists():
            console.print(f"[red]❌ PDF not found at {pdf_path}[/red]")
            return False

        console.print(f"\n[cyan]📖 Starting Smart Local OCR on '{pdf_path.name}'...[/cyan]")
        console.print(f"[dim]Using languages: {self.languages}[/dim]")

        try:
            from pdf2image import pdfinfo_from_path
            info = pdfinfo_from_path(pdf_path)
            total_pages = info["Pages"]
        except Exception as e:
            console.print(f"[red]❌ Failed to read PDF info: {e}[/red]")
            console.print("[yellow]Ensure 'poppler-utils' is installed: sudo apt-get install poppler-utils[/yellow]")
            return False

        console.print(f"[green]Total pages detected: {total_pages}[/green]")

        output_txt_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_txt_path, "w", encoding="utf-8") as out_f, Progress(
            SpinnerColumn(),
            TextColumn("[progress.description]{task.description}"),
            BarColumn(),
            TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
            TextColumn("({task.completed}/{task.total} Pages)"),
            console=console,
        ) as progress:

            task = progress.add_task("[yellow]Converting and OCRing...", total=total_pages)

            # Process in chunks to prevent memory overload on huge PDFs
            chunk_size = 10
            import re
            
            with tempfile.TemporaryDirectory() as temp_dir:
                for i in range(1, total_pages + 1, chunk_size):
                    images = convert_from_path(
                        pdf_path,
                        first_page=i,
                        last_page=min(i + chunk_size - 1, total_pages),
                        output_folder=temp_dir,
                        fmt="jpeg",
                        dpi=300,  # High DPI for better OCR accuracy
                    )

                    for idx, img in enumerate(images):
                        page_num = i + idx
                        progress.update(task, description=f"[yellow]OCRing Page {page_num}...")
                        
                        # --- 1. SMART IMAGE PREPROCESSING ---
                        # Convert to grayscale
                        img = img.convert('L')
                        
                        # Apply strict threshold to eliminate background and faint watermarks (opacity 0.4)
                        # Grid search confirmed Threshold 150 yields highest accuracy across all pages.
                        img = img.point(lambda p: 255 if p > 150 else 0)
                        
                        # --- 2. OPTIMIZED OCR CONFIG ---
                        # psm 4: Assume a single column of text of variable sizes (Grid search proven best for this layout)
                        config = "--oem 1 --psm 4"
                        text = pytesseract.image_to_string(img, lang=self.languages, config=config)
                        
                        # --- 3. TEXT CLEANUP & AUTOCORRECT (Removing digital noise & fixing typos) ---
                        # Remove lines consisting only of numbers/symbols/dashes like "111111111"
                        
                        # Dictionary of known stubborn Tesseract Arabic OCR errors
                        autocorrect_dict = {
                            "تبهي": "تيهي",
                            "واشحبي": "واسحبي",
                            "واشّحبي": "واسحبي",
                            "فَؤقها": "فَوْقَهَا",
                            "فؤقها": "فَوْقَهَا",
                            "شَعَلَ مَتاصِب": "شَغَلَ مَنَاصِب",
                            "تعاحج": "تعالج",
                            "نَثَا": "نشأ",
                            "المستوى الفق:": "المستوى الفني",
                        }
                        
                        cleaned_lines = []
                        for line in text.splitlines():
                            stripped = line.strip()
                            if not stripped:
                                continue
                            # If a line is just repetitive numbers or dashes (the OCR'd dashed border)
                            if re.match(r'^[\d\W_]+$', stripped) and len(stripped) > 5:
                                continue
                            
                            # Clean up OCR'd "•••" (poetry separator)
                            stripped = re.sub(r'[•\.]{3,}', '•••', stripped)
                            
                            # Apply Smart Autocorrect for persistent OCR typos
                            for wrong, right in autocorrect_dict.items():
                                if wrong in stripped:
                                    stripped = stripped.replace(wrong, right)
                            
                            cleaned_lines.append(stripped)
                        
                        cleaned_text = "\n".join(cleaned_lines)
                        
                        # We don't output "--- Page X ---" to avoid it being treated as part of the book text,
                        # but we can add a small clean separator.
                        out_f.write(f"\n\n{cleaned_text}")
                        progress.advance(task)

        console.print(f"\n[bold green]✅ Finished! Text successfully extracted and saved to:[/bold green]")
        console.print(f"[bold white]{output_txt_path}[/bold white]")
        return True

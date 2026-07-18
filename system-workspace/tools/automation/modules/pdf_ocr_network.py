import os
import io
import sys
import tempfile
from pathlib import Path
import requests

from pdf2image import convert_from_path
from rich.console import Console
from rich.progress import BarColumn, Progress, SpinnerColumn, TextColumn
import questionary

console = Console()

class NetworkPDFOCR:
    def __init__(self, server_ip: str):
        self.server_ip = server_ip
        self.api_url = f"http://{self.server_ip}:8000/api/ocr"

    def process_pdf(self, pdf_path: str, output_txt_path: str):
        pdf_path = Path(pdf_path)
        output_txt_path = Path(output_txt_path)

        if not pdf_path.exists():
            console.print(f"[red]❌ PDF not found at {pdf_path}[/red]")
            return False

        # Test connection to the AI Server
        console.print(f"\n[cyan]🔗 Connecting to AI Server at {self.api_url}...[/cyan]")
        
        try:
            from pdf2image import pdfinfo_from_path
            info = pdfinfo_from_path(pdf_path)
            total_pages = info["Pages"]
        except Exception as e:
            console.print(f"[red]❌ Failed to read PDF info: {e}[/red]")
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

            task = progress.add_task("[magenta]Sending to AI Server...", total=total_pages)

            chunk_size = 10
            with tempfile.TemporaryDirectory() as temp_dir:
                for i in range(1, total_pages + 1, chunk_size):
                    images = convert_from_path(
                        pdf_path,
                        first_page=i,
                        last_page=min(i + chunk_size - 1, total_pages),
                        output_folder=temp_dir,
                        fmt="jpeg",
                        dpi=300, 
                    )

                    for idx, img in enumerate(images):
                        page_num = i + idx
                        progress.update(task, description=f"[magenta]AI Processing Page {page_num}...")
                        
                        # No need for Binarization/Thresholding! 
                        # Advanced AI models handle watermarks naturally.
                        
                        # Convert image to bytes to send over the network
                        img_byte_arr = io.BytesIO()
                        img.save(img_byte_arr, format='JPEG')
                        img_bytes = img_byte_arr.getvalue()
                        
                        try:
                            files = {'file': ('page.jpg', img_bytes, 'image/jpeg')}
                            response = requests.post(self.api_url, files=files, timeout=120)
                            
                            if response.status_code == 200:
                                data = response.json()
                                if data.get("status") == "success":
                                    text = data.get("text", "")
                                    out_f.write(f"\n\n{text}")
                                else:
                                    console.print(f"\n[red]Server Error on page {page_num}: {data.get('message')}[/red]")
                            else:
                                console.print(f"\n[red]HTTP Error {response.status_code} on page {page_num}[/red]")
                                
                        except Exception as e:
                            console.print(f"\n[red]Network Error while contacting AI Server: {e}[/red]")
                            return False
                            
                        progress.advance(task)

        console.print(f"\n[bold green]✅ Finished! Expert AI Text successfully saved to:[/bold green]")
        console.print(f"[bold white]{output_txt_path}[/bold white]")
        return True

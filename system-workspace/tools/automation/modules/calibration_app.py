import re
from pathlib import Path
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import subprocess

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent.parent.parent
CSS_PATH = PROJECT_ROOT / "styles/main.css"
ASSETS_PATH = PROJECT_ROOT / "assets"

app = FastAPI()
app.mount("/assets", StaticFiles(directory=str(ASSETS_PATH)), name="assets")

# Mount a temporary directory for HTML test pages if provided via command line or env
app.state.target_html_path = None

templates = Jinja2Templates(directory=str(Path(__file__).parent / "templates"))

def extract_css_variables():
    content = CSS_PATH.read_text(encoding="utf-8")
    root_match = re.search(r":root\s*{([^}]+)}", content)
    if not root_match:
        return {}

    variables = {}
    lines = root_match.group(1).split("\n")
    for line in lines:
        if ":" in line and "--" in line:
            parts = line.split(":")
            var_name = parts[0].strip()
            # Simple extract, ignore comments for now
            var_val = parts[1].split(";")[0].strip()
            variables[var_name] = var_val
    return variables

def update_css_variables(new_vars):
    content = CSS_PATH.read_text(encoding="utf-8")

    # We will do a simple string replace for each variable.
    # A more robust parser could be used, but this is fine for calibration.
    for var_name, new_val in new_vars.items():
        pattern = re.compile(rf"({var_name}\s*:\s*)([^;]+)(;)")
        content = pattern.sub(rf"\g<1>{new_val}\g<3>", content)

    CSS_PATH.write_text(content, encoding="utf-8")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    css_vars = extract_css_variables()
    html_content = ""
    if app.state.target_html_path and Path(app.state.target_html_path).exists():
        # Inject paged.js script into the head of the target HTML
        raw_html = Path(app.state.target_html_path).read_text(encoding="utf-8")
        if "</head>" in raw_html:
            pagedjs_tag = '<script src="/assets/js/paged.polyfill.js"></script>'
            # We also need to link the CSS file correctly since the preview is rendered in an iframe or div
            # Actually, the simplest approach is to render the HTML inside an iframe and have the iframe load paged.js.
            # But since we serve the whole page, let's just pass the URL to the iframe.
            pass

    return templates.TemplateResponse(request, "calibration.html", {"css_vars": css_vars})

@app.get("/preview", response_class=HTMLResponse)
async def preview():
    if not app.state.target_html_path or not Path(app.state.target_html_path).exists():
        return HTMLResponse("<h1>No target HTML selected or file not found.</h1>")

    raw_html = Path(app.state.target_html_path).read_text(encoding="utf-8")
    
    # Inject dynamic CSS and Paged.js
    # Replace relative CSS path with dynamic endpoint
    raw_html = re.sub(r'<link[^>]*href="[^"]*styles/main\.css"[^>]*>', '<link rel="stylesheet" href="/dynamic.css">', raw_html)
    
    if "</head>" in raw_html:
        injection = '<script src="/assets/js/paged.polyfill.js"></script>\n'
        # Add dynamic live injection script and Page Slicing UI
        injection += """
        <style>
            @media screen {
                body {
                    background-color: #525659 !important;
                }
                .pagedjs_pages {
                    display: flex;
                    flex-direction: column;
                    align-items: center;
                    padding: 40px 0;
                    gap: 40px;
                }
                .pagedjs_page {
                    background: white;
                    box-shadow: 0 4px 10px rgba(0,0,0,0.5);
                    margin: 0 !important;
                    flex-shrink: 0;
                }
            }
        </style>
        <script>
            window.addEventListener('message', function(event) {
                if(event.data && event.data.type === 'update-css-var') {
                    document.documentElement.style.setProperty(event.data.key, event.data.value);
                }
            });
        </script>
        """
        raw_html = raw_html.replace("</head>", f"{injection}</head>")

    return HTMLResponse(content=raw_html)

@app.get("/dynamic.css")
async def dynamic_css():
    """Serves the current main.css file."""
    content = CSS_PATH.read_text(encoding="utf-8")
    # Fix paths in CSS if necessary, assuming assets are in /assets
    content = content.replace("../assets/", "/assets/")
    from fastapi.responses import Response
    return Response(content=content, media_type="text/css")

@app.post("/save")
async def save_config(request: Request):
    data = await request.form()
    new_vars = dict(data)
    update_css_variables(new_vars)
    return {"status": "success", "message": "Variables saved to main.css"}

@app.post("/generate_pdf")
async def generate_pdf():
    if not app.state.target_html_path:
        return {"status": "error", "message": "No HTML target set."}

    output_pdf = PROJECT_ROOT / "calibration_test.pdf"
    target_html = app.state.target_html_path

    try:
        # Pass base-url as the project root so asset paths resolve correctly
        subprocess.run(["weasyprint", str(target_html), str(output_pdf), "--base-url", str(PROJECT_ROOT)], check=True)
        return {"status": "success", "message": f"PDF generated at {output_pdf.name}", "url": f"/download_pdf"}
    except Exception as e:
        return {"status": "error", "message": str(e)}

@app.get("/download_pdf")
async def download_pdf():
    output_pdf = PROJECT_ROOT / "calibration_test.pdf"
    from fastapi.responses import FileResponse
    if output_pdf.exists():
        return FileResponse(output_pdf, filename="calibration_test.pdf")
    return HTMLResponse("File not found", status_code=404)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

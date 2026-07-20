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
    """Serves the target HTML modified to include Paged.js and the main.css via API."""
    if not app.state.target_html_path or not Path(app.state.target_html_path).exists():
        return HTMLResponse("<h1>No target HTML selected</h1>")

    raw_html = Path(app.state.target_html_path).read_text(encoding="utf-8")

    # Inject our dynamic CSS endpoint and Paged.js
    css_link = '<link rel="stylesheet" href="/dynamic.css">'
    pagedjs_script = '<script src="/assets/js/paged.polyfill.js"></script>'

    if "</head>" in raw_html:
        raw_html = raw_html.replace("</head>", f"{css_link}\n{pagedjs_script}\n</head>")
    else:
         raw_html = f"<head>{css_link}\n{pagedjs_script}</head>\n" + raw_html

    return HTMLResponse(raw_html)

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
        # Assuming weasyprint is installed in the env
        subprocess.run(["weasyprint", str(target_html), str(output_pdf)], check=True)
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

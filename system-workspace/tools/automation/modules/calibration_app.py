import re
import shutil
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

def get_available_pages():
    pages_dir = PROJECT_ROOT / "pages"
    if not pages_dir.exists():
        return []
    return sorted([p.name for p in pages_dir.glob("*.html") if "TEMPLATE" not in p.name])

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
    
    # Create backup before saving
    import datetime
    import shutil
    backup_dir = PROJECT_ROOT / "styles" / "backups"
    backup_dir.mkdir(parents=True, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"main_backup_{timestamp}.css"
    shutil.copy2(CSS_PATH, backup_path)

    # We will do a simple string replace for each variable.
    # A more robust parser could be used, but this is fine for calibration.
    for var_name, new_val in new_vars.items():
        pattern = re.compile(rf"({var_name}\s*:\s*)([^;]+)(;)")
        content = pattern.sub(rf"\g<1>{new_val}\g<3>", content)

    CSS_PATH.write_text(content, encoding="utf-8")

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    css_vars = extract_css_variables()
    pages = get_available_pages()
    current_page = Path(app.state.target_html_path).name if app.state.target_html_path else ""
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

    return templates.TemplateResponse(request, "calibration.html", {"css_vars": css_vars, "pages": pages, "current_page": current_page})

@app.get("/preview", response_class=HTMLResponse)
async def preview():
    if not app.state.target_html_path or not Path(app.state.target_html_path).exists():
        return HTMLResponse("""
            <div style="display:flex; justify-content:center; align-items:center; height:100vh; background:#525659; color:white; font-family:sans-serif; text-align:center;">
                <div>
                    <h2 style="margin-bottom:10px;">📄 No Target HTML Selected</h2>
                    <p style="color:#aaa;">Please select a target page from the left sidebar to begin calibration.</p>
                </div>
            </div>
        """)

    try:
        raw_html = Path(app.state.target_html_path).read_text(encoding="utf-8")
    except Exception as e:
        return HTMLResponse(f"<h1>Error reading file: {str(e)}</h1>")
    
    # Inject dynamic CSS and Paged.js
    # Replace relative CSS path with dynamic endpoint
    raw_html = re.sub(r'<link[^>]*href="[^"]*styles/main\.css"[^>]*>', '<link rel="stylesheet" href="/dynamic.css">', raw_html)
    
    if "</head>" in raw_html:
        injection = '<script src="/assets/js/paged.polyfill.js"></script>\n'
        # Add dynamic live injection script and Page Slicing UI
        injection += """
        <style>
            @media screen {
                html {
                    background-color: #525659 !important;
                }
                body {
                    background-color: transparent !important;
                    margin: 0 !important;
                    padding: 0 !important;
                    min-height: 100vh;
                    overflow: auto !important;
                }
                /* If Paged.js fails, this acts as the paper */
                .calibration-preview-wrapper {
                    background-color: transparent !important;
                }
                /* When Paged.js runs, it adds .pagedjs_paged class to html/body */
                .pagedjs_pages {
                    display: flex !important;
                    flex-direction: column !important;
                    align-items: center !important;
                    padding: 40px 0 !important;
                    gap: 60px !important;
                    background-color: #525659 !important;
                }
                .pagedjs_page {
                    background-color: white !important;
                    box-shadow: 0 4px 20px rgba(0,0,0,0.6) !important;
                    margin: 0 !important;
                    flex-shrink: 0 !important;
                    position: relative;
                }
                .pagedjs_page * {
                    /* We don't want to override everything, just ensure the page itself is white */
                }
                .pagedjs_sheet {
                    background-color: white !important;
                }
                .pagedjs_pagebox {
                    background-color: transparent !important;
                }
                .pagedjs_page_content {
                    background-color: white !important;
                }
                /* Visual split line between pages when in continuous scroll mode */
                .pagedjs_page:not(:last-child)::after {
                    content: "";
                    position: absolute;
                    bottom: -35px;
                    left: 0;
                    right: 0;
                    height: 10px;
                    background: repeating-linear-gradient(45deg, transparent, transparent 10px, rgba(255,255,255,0.2) 10px, rgba(255,255,255,0.2) 20px);
                    border-radius: 5px;
                }
            }
            /* Inspector Styles */
            .inspector-hover {
                outline: 3px solid #ff4757 !important;
                background-color: rgba(255, 71, 87, 0.1) !important;
                cursor: crosshair !important;
            }
        </style>
        <script>
            let inspectorActive = false;
            let currentTarget = null;
            let pinnedTarget = null;
            let currentPage = 1;
            let singlePageMode = false;
            let totalPages = 1;
            
            function updatePagination() {
                const pages = document.querySelectorAll('.pagedjs_page');
                totalPages = pages.length;
                if(totalPages === 0) return;
                
                if(singlePageMode) {
                    pages.forEach((p, i) => {
                        p.style.display = (i + 1 === currentPage) ? 'block' : 'none';
                    });
                } else {
                    pages.forEach(p => p.style.display = 'block');
                }
                window.parent.postMessage({ type: 'page-info', current: currentPage, total: totalPages }, '*');
            }
            
            window.PagedConfig = {
                after: (flow) => {
                    updatePagination();
                }
            };

            window.addEventListener('message', function(event) {
                if(event.data && event.data.type === 'update-css-var') {
                    document.documentElement.style.setProperty(event.data.key, event.data.value);
                }
                if(event.data && event.data.type === 'toggle-inspector') {
                    inspectorActive = event.data.value;
                    if(!inspectorActive && currentTarget) {
                        currentTarget.classList.remove('inspector-hover');
                        window.parent.postMessage({ type: 'inspector-data', html: '' }, '*');
                    }
                }
                if(event.data && event.data.type === 'change-page') {
                    currentPage += event.data.delta;
                    if(currentPage < 1) currentPage = 1;
                    if(currentPage > totalPages) currentPage = totalPages;
                    updatePagination();
                }
                if(event.data && event.data.type === 'toggle-single-page') {
                    singlePageMode = event.data.enabled;
                    updatePagination();
                }
                if(event.data && event.data.type === 'pin-parent') {
                    if (pinnedTarget && pinnedTarget.parentElement && pinnedTarget.parentElement !== document.body && pinnedTarget.parentElement !== document.documentElement) {
                        pinnedTarget = pinnedTarget.parentElement;
                        const info = getInspectorInfo(pinnedTarget);
                        const vars = getUsedVariables(pinnedTarget);
                        window.parent.postMessage({ type: 'inspector-pinned-data', html: info, variables: vars }, '*');
                    }
                }
            });

            function getInspectorInfo(target) {
                const comp = window.getComputedStyle(target);
                let info = `<div><strong style="color:#ff4757; font-size:16px;">${target.tagName}</strong></div>`;
                if(target.id) info += `<div style="color:#f39c12; margin-top:4px;">#${target.id}</div>`;
                if(target.className && typeof target.className === 'string') {
                    let cls = target.className.replace('inspector-hover', '').trim();
                    if(cls) {
                        info += `<div style="color:#2ecc71; margin-top:4px; font-family:monospace; font-size:12px;">.${cls.split(' ').join('.')}</div>`;
                    }
                }
                
                info += `<div style="margin-top: 15px; border-top: 1px solid #444; padding-top: 10px;">`;
                info += `<div><strong>Font Size:</strong> ${comp.fontSize}</div>`;
                info += `<div><strong>Line Height:</strong> ${comp.lineHeight}</div>`;
                info += `<div><strong>Color:</strong> <span style="display:inline-block; width:12px; height:12px; background:${comp.color}; border:1px solid #fff; margin-bottom:-2px;"></span> ${comp.color}</div>`;
                info += `<div><strong>Margin:</strong> ${comp.marginTop} ${comp.marginRight} ${comp.marginBottom} ${comp.marginLeft}</div>`;
                info += `<div><strong>Padding:</strong> ${comp.paddingTop} ${comp.paddingRight} ${comp.paddingBottom} ${comp.paddingLeft}</div>`;
                info += `</div>`;
                return info;
            }

            document.addEventListener('mouseover', function(e) {
                if(!inspectorActive) return;
                if(e.target === document.body || e.target === document.documentElement) return;
                
                if(currentTarget) currentTarget.classList.remove('inspector-hover');
                currentTarget = e.target;
                currentTarget.classList.add('inspector-hover');
                
                const info = getInspectorInfo(currentTarget);
                window.parent.postMessage({ type: 'inspector-data', html: info }, '*');
            });
            
            function getUsedVariables(target) {
                let vars = new Set();
                try {
                    for (let i = 0; i < document.styleSheets.length; i++) {
                        let sheet = document.styleSheets[i];
                        try {
                            for (let j = 0; j < sheet.cssRules.length; j++) {
                                let rule = sheet.cssRules[j];
                                if (rule.type === CSSRule.STYLE_RULE) {
                                    if (rule.selectorText.includes(':root') || rule.selectorText.includes('html') || rule.selectorText === 'body') continue;
                                    
                                    let cleanSelector = rule.selectorText.replace(/::?(before|after|hover|active|focus|nth-child\\([^)]+\\))/g, '').trim();
                                    if (!cleanSelector) continue;
                                    
                                    try {
                                        if (target.matches(cleanSelector) || target.querySelector(cleanSelector)) {
                                            const matches = rule.style.cssText.match(/var\\(--[a-zA-Z0-9-]+\\b/g);
                                            if (matches) {
                                                matches.forEach(m => vars.add(m.substring(4)));
                                            }
                                        }
                                    } catch(e) {}
                                }
                            }
                        } catch(e) {}
                    }
                } catch(e) {
                    console.error("Error accessing styleSheets", e);
                }
                console.log("Used variables for", target, ":", Array.from(vars));
                return Array.from(vars);
            }

            document.addEventListener('click', function(e) {
                if(!inspectorActive) return;
                
                // Allow clicking through if Shift key is held (helps select elements behind others)
                if (e.shiftKey) return;
                
                if(e.target === document.body || e.target === document.documentElement) return;
                e.preventDefault();
                e.stopPropagation();
                
                pinnedTarget = e.target;
                const info = getInspectorInfo(pinnedTarget);
                const vars = getUsedVariables(pinnedTarget);
                window.parent.postMessage({ type: 'inspector-pinned-data', html: info, variables: vars }, '*');
            });
            
            document.addEventListener('selectionchange', function() {
                if(!inspectorActive) return;
                const selection = window.getSelection();
                if (selection.rangeCount > 0 && !selection.isCollapsed) {
                    let target = selection.anchorNode;
                    if (target.nodeType === 3) target = target.parentElement; // Get the element wrapping the text
                    
                    if(target === document.body || target === document.documentElement) return;
                    
                    pinnedTarget = target;
                    const info = getInspectorInfo(pinnedTarget);
                    const vars = getUsedVariables(pinnedTarget);
                    window.parent.postMessage({ type: 'inspector-pinned-data', html: info, variables: vars }, '*');
                }
            });
            
            document.addEventListener('mouseout', function(e) {
                if(!inspectorActive) return;
                if(currentTarget) currentTarget.classList.remove('inspector-hover');
                window.parent.postMessage({ type: 'inspector-data', html: '' }, '*');
            });
        </script>
        """
        raw_html = raw_html.replace("</head>", f"{injection}</head>")

        # Inject global backgrounds
        global_layers = """
        <!-- Global Fixed Background -->
        <div class="global-background-layer"></div>
        <div class="global-watermark-layer"></div>
        """
        raw_html = re.sub(r'(<body[^>]*>)', rf'\1{global_layers}', raw_html)


    raw_html = re.sub(r'<body([^>]*)>', r'<body\1><div class="calibration-rtl-wrapper" style="direction: rtl !important; text-align: start;">', raw_html)
    raw_html = raw_html.replace("</body>", "</div></body>")
    return HTMLResponse(content=raw_html)

@app.get("/dynamic.css")
async def dynamic_css():
    """Serves the current main.css file."""
    content = CSS_PATH.read_text(encoding="utf-8")
    # Fix paths in CSS if necessary, assuming assets are in /assets
    content = content.replace("../assets/", "/assets/")
    content = re.sub(r"(html\s*\{[^}]*)(direction:\s*rtl\s*;?)([^}]*\})", r"\1\3", content)
    from fastapi.responses import Response
    return Response(content=content, media_type="text/css")

@app.post("/save")
async def save_config(request: Request):
    data = await request.form()
    new_vars = dict(data)
    update_css_variables(new_vars)
    return {"status": "success", "message": "Variables saved to main.css"}

@app.post("/set_target")
async def set_target(request: Request):
    try:
        data = await request.form()
        filename = data.get("filename")
        if filename:
            file_path = PROJECT_ROOT / "pages" / filename
            if file_path.exists():
                app.state.target_html_path = str(file_path)
                return {"status": "success", "message": f"Target set to {filename}"}
        return {"status": "error", "message": "File not found or not provided"}
    except Exception as e:
        return {"status": "error", "message": f"Internal error: {str(e)}"}


def _is_wsl() -> bool:
    """Return True when running inside Windows Subsystem for Linux."""
    try:
        return "microsoft" in Path("/proc/version").read_text().lower()
    except Exception:
        return False


def _find_system_chrome() -> str | None:
    """Locate a native Linux Chrome/Chromium executable.

    Windows .exe paths are skipped in WSL because Playwright communicates
    via --remote-debugging-pipe (Linux file descriptors), which Windows
    processes cannot use.
    """
    if _is_wsl():
        linux_candidates = [
            "/usr/bin/google-chrome",
            "/usr/bin/google-chrome-stable",
            "/usr/bin/chromium-browser",
            "/usr/bin/chromium",
            "/snap/bin/chromium",
        ]
        for path in linux_candidates:
            if Path(path).exists():
                return path
        for name in ["google-chrome", "google-chrome-stable", "chromium-browser", "chromium"]:
            found = shutil.which(name)
            if found:
                return found
        return None  # Let Playwright use its bundled Chromium headless shell

    candidates = [
        "/usr/bin/google-chrome",
        "/usr/bin/google-chrome-stable",
        "/usr/bin/chromium-browser",
        "/usr/bin/chromium",
        "/snap/bin/chromium",
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    ]
    for path in candidates:
        if Path(path).exists():
            return path
    for name in ["google-chrome", "google-chrome-stable", "chromium-browser", "chromium"]:
        found = shutil.which(name)
        if found:
            return found
    return None


@app.post("/generate_pdf")
async def generate_pdf():
    if not app.state.target_html_path:
        return {"status": "error", "message": "No HTML target set."}

    output_pdf = PROJECT_ROOT / "calibration_test.pdf"
    target_html = Path(app.state.target_html_path)

    # ── Try Playwright first (matches preview exactly) ─────────────────────
    try:
        from playwright.async_api import async_playwright

        url = target_html.as_uri()
        chrome_exe = _find_system_chrome()

        launch_kwargs: dict = {
            "args": [
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
                "--allow-file-access-from-files",
                "--disable-web-security",
            ],
            "headless": True,
        }
        if chrome_exe:
            launch_kwargs["executable_path"] = chrome_exe

        async with async_playwright() as p:
            browser = await p.chromium.launch(**launch_kwargs)
            context = await browser.new_context()
            page = await context.new_page()
            await page.emulate_media(media="print")
            await page.goto(url, wait_until="networkidle", timeout=60_000)
            await page.wait_for_timeout(800)
            await page.pdf(
                path=str(output_pdf),
                format="A4",
                print_background=True,
                margin={"top": "0", "right": "0", "bottom": "0", "left": "0"},
                prefer_css_page_size=True,
            )
            await browser.close()

        engine_used = f"Chrome ({chrome_exe or 'Playwright Chromium'})"
        return {"status": "success", "message": f"PDF generated via {engine_used}", "url": "/download_pdf"}

    except ImportError:
        # ── Fallback: WeasyPrint ───────────────────────────────────────────
        # Note: WeasyPrint renders differently from the browser preview.
        # Install Playwright for matching output: pip install playwright && playwright install chromium
        try:
            base_url = str(target_html.parent) + "/"
            result = subprocess.run(
                ["weasyprint", str(target_html), str(output_pdf), "--base-url", base_url],
                check=True,
                capture_output=True,
                text=True,
            )
            return {
                "status": "success",
                "message": "PDF generated via WeasyPrint (⚠ may differ from preview — install Playwright for exact match)",
                "url": "/download_pdf",
            }
        except subprocess.CalledProcessError as e:
            err_detail = (e.stderr or "").strip()
            return {"status": "error", "message": f"WeasyPrint error: {err_detail or str(e)}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}

    except Exception as e:
        return {"status": "error", "message": f"Playwright error: {str(e)}"}


@app.get("/download_pdf")
async def download_pdf():
    output_pdf = PROJECT_ROOT / "calibration_test.pdf"
    from fastapi.responses import FileResponse
    if output_pdf.exists():
        return FileResponse(output_pdf, filename="calibration_test.pdf")
    return HTMLResponse("File not found", status_code=404)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

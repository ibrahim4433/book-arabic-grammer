# Arabic Grammar Book: Developer Guide

This guide covers the modern Python 3.12+ tools, testing suite, and API services recently integrated into the project.

## 1. Setting Up the Environment (Using `uv`)

The project has been modernized to use `uv`, the lightning-fast Python package manager, and `pyproject.toml` instead of legacy `requirements.txt`.

### Installation
1. **Install uv:**
   ```bash
   pip install uv
   ```
2. **Create a virtual environment and install all dependencies:**
   ```bash
   # Install core dependencies, development tools (pytest, ruff, mypy), and the API service (FastAPI)
   uv venv
   uv pip install -e ".[dev,api]"
   ```
3. **Activate the environment:**
   - **Windows (PowerShell):** `.\.venv\Scripts\activate`
   - **Linux/Mac:** `source .venv/bin/activate`

---

## 2. Running the Asynchronous Linter

The `lint_pages.py` tool has been upgraded to use Python 3.11+ `asyncio.TaskGroup`. It now reads and lints all HTML pages concurrently, drastically reducing execution time.

**Command:**
```bash
python Jules-workspace/lint_pages.py
```
*Note: This will recursively scan the `pages/` directory and ensure strict adherence to the Atomic Design rules.*

---

## 3. Running the Test Suite (Pytest)

A robust unit testing suite has been added to the `tests/` directory to ensure core logic (like the linter and batch refactor tools) doesn't break during future updates.

**Command:**
```bash
pytest tests/ -v
```
You should see output confirming that tests like `test_lint_file_inline_style_violation` and `test_batch_refactor_execute` passed successfully.

---

## 4. Code Formatting & Quality (Ruff)

The project now uses `ruff` for ultra-fast formatting and linting.

**Check for errors and auto-fix them:**
```bash
ruff check . --fix
```

**Format the codebase (similar to Black):**
```bash
ruff format .
```

---

## 5. Starting the FastAPI Service

A high-performance `api.py` microservice has been added to render the grammar book on demand. It offloads WeasyPrint's CPU-heavy rendering to background threads so the web server remains responsive.

**Start the Server:**
```bash
uvicorn api:app --reload
```

**Using the API:**
Once running (typically at `http://localhost:8000`), you can access the automatic interactive documentation:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

**Example Workflow:**
1. **Generate a PDF for Theme v1:**
   Send a `POST` request to `/api/v1/render` with a JSON body:
   ```json
   {
     "theme": "v1",
     "watermark": "أ. حنا خفيف"
   }
   ```
2. **Download the Generated PDF:**
   Send a `GET` request to `/api/v1/download/v1` to download the file directly to your browser.

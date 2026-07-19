import asyncio
from pathlib import Path

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Assuming build.py is accessible and we can import its core logic
from build import BuildConfig, BuildError, build_book

app = FastAPI(
    title="Arabic Grammar Book API",
    description="High-performance async API for rendering Arabic Grammar books on demand.",
    version="1.0.0",
)


class RenderRequest(BaseModel):
    theme: str = "v1"
    watermark: str = "أ. حنا خفيف"
    dry_run: bool = False


@app.get("/")
async def health_check():
    return {"status": "healthy", "service": "Grammar Book PDF Engine"}


@app.post("/api/v1/render")
async def render_pdf(req: RenderRequest):
    """
    Renders the PDF asynchronously.
    """
    # Resolve paths based on the theme
    theme_dir = Path(f"new-style-options/{req.theme}")

    if not theme_dir.exists() and not req.theme == "default":
        raise HTTPException(status_code=404, detail=f"Theme {req.theme} not found.")

    stylesheet = theme_dir / "main.css" if theme_dir.exists() else Path("styles/main.css")
    output_pdf = theme_dir / "book.pdf" if theme_dir.exists() else Path("output/export/book.pdf")

    config = BuildConfig(
        pages_dir=Path("pages"),
        output_pdf=output_pdf,
        stylesheet=stylesheet,
        watermark_text=req.watermark,
        dry_run=req.dry_run,
    )

    try:
        # Run CPU-bound WeasyPrint generation in a background thread to prevent event loop blocking!
        result = await asyncio.to_thread(build_book, config)

        if not result.success:
            raise HTTPException(status_code=500, detail={"errors": result.errors})

        return {
            "status": "success",
            "duration_seconds": round(result.duration_seconds, 2),
            "pages_processed": result.pages_processed,
            "output_path": str(result.output_path),
        }
    except BuildError as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/api/v1/download/{theme}")
async def download_pdf(theme: str):
    """
    Downloads the pre-generated PDF for a given theme.
    """
    pdf_path = Path(f"new-style-options/{theme}/book.pdf")
    if not pdf_path.exists():
        raise HTTPException(status_code=404, detail="PDF not found. Please render it first.")

    return FileResponse(
        path=pdf_path, filename=f"Arabic_Grammar_{theme}.pdf", media_type="application/pdf"
    )


if __name__ == "__main__":
    import uvicorn

    # Run the high-performance ASGI server
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)

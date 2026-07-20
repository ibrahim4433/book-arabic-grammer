### `./system-workspace/tools/new-tools/new-beta-page-maker/test_gemini_yt.py`
- **Status:** Usable
- **Purpose:** A simple script to test Gemini's multimodal capabilities by asking it to transcribe a YouTube video.
- **Inputs:** `GEMINI_API_KEY` (environment variable), YouTube URL (hardcoded)
- **Outputs:** Prints transcription text to standard output.
- **Usage:** `python test_gemini_yt.py`
- **Workflow Integration:** Similar to `test_pytubefix.py`, this is a utility script that could inform future AI pipeline additions (e.g. generating lessons from video content), though it is not part of the direct page generation process.

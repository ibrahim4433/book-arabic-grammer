# Original User Request

## 2026-06-15T16:25:38Z

# Teamwork Project Prompt — Draft

> Status: Launched
> Goal: Craft prompt → get user approval → delegate to teamwork_preview

Create a new tool for the Arabic Grammar book project that takes a YouTube video or playlist link, processes it using Jules AI (or Gemini) to directly transcribe the voice and text from the video, and saves the output to files named `Ny-raw.txt` (where N is the sequence number).

Working directory: `/mnt/c/users/ibrah/My Documents/GitHub/book-arabic-grammer`
Integrity mode: development

## Requirements

### R1. YouTube Video Processing
The tool must accept a YouTube URL (either a single video or a playlist). It should attempt to feed the video content (either by downloading the audio/video locally or via URL if supported) directly to the Jules AI (or Gemini Client) so the AI can "watch/listen" and generate an Arabic text script from the voice and on-screen text.

### R2. Output Formatting
The transcribed scripts must be saved into a designated raw text folder (e.g., `system-workspace/text-data/raw/`). The files must be named sequentially using the format `Ny-raw.txt` (where N is the video sequence number from the playlist, e.g., `1y-raw.txt`, `2y-raw.txt`).

### R3. Control Room Integration
The new tool must be integrated as a new interactive menu option inside the main `system.py` control room UI, allowing the user to easily launch the YouTube-to-Text workflow.

## Acceptance Criteria

### Functional Execution
- [ ] A test script can successfully take a short YouTube video link, run the processing pipeline, and generate a populated `1y-raw.txt` file containing the Arabic transcript.
- [ ] The `system.py` script successfully launches without syntax errors and displays the new menu option for the YouTube-to-Text tool.
- [ ] The pipeline successfully iterates over a playlist (or a list of links) and increments the sequence number `N` for each generated text file.

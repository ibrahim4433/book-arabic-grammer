### `./system-workspace/tools/automation/plan_refiner.py`
- **Status:** Usable
- **Purpose:** Generates an architectural plan using a sticky Gemini model fallback chain and refines it via an auditing process (using another Gemini prompt) until the plan is approved or maximum retries are reached.
- **Inputs:** Raw text file path (`<raw_text_path>`), `TOC.json`, `design_patterns.json`, `Architect_GEM_MASTER.md` and `Architect_AUDITOR.md`.
- **Outputs:** Refined plan text file saved to `<output_plan_path>`.
- **Usage:** `python system-workspace/tools/automation/plan_refiner.py <raw_text_path> <output_plan_path>`
- **Workflow Integration:** Fits the new 1-Plan-Per-Page workflow perfectly. Instead of taking an entire lesson as input, it can take an exact text slice (a single page) and will enforce fitting constraints during the generation and auditing cycles (with updated 1-page specific Prompts).

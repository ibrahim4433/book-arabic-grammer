# 🤖 Auto-Book-Maker V2: The "Self-Correcting" Architecture

## 🎯 Objective
Fully automate the conversion of Raw Arabic Lesson Images into "Gold Standard" HTML5 Book Pages. The system must be **stateless**, **self-correcting**, and **interactively smart**, capable of refining its own plans before execution and validating the final output against strict design laws.

---

## 🏗️ System Architecture: The 4-Phase Loop

The workflow is orchestrated by a central `workflow_manager.py` that moves a lesson through 4 distinct phases.

### Phase 1: Ingestion & Pattern Analysis
*   **Goal:** Prepare raw data and "teach" the AI the current design standard.
*   **Step 1.1: Vision (Images -> Text):**
    *   Tool: `beta-utilities/all_pics_to_text.py`
    *   Action: Convert `input/*.jpg` to `output/raw/raw_X.txt`.
*   **Step 1.2: Indexing (Text -> Context):**
    *   Tool: `beta-utilities/create_lesson_index.py`
    *   Action: Map specific lines in raw text to a Lesson Title (e.g., "Lesson 5 = raw_3.txt lines 20-50").
*   **Step 1.3: Pattern Extraction (New):**
    *   Tool: `beta-utilities/pattern_extractor.py` (TO-DO)
    *   Action: Scan existing "Good" pages (e.g., `08.x`, `09.x`). Extract the JSON structure of templates used, nesting depth, and common CSS utility classes.
    *   Output: `assets/design_patterns.json` (The "Style Guide").

### Phase 2: The "Refiner" Planning Loop (The Brain)
*   **Goal:** Generate a *perfect* plan for Jules by critiquing and fixing it *before* coding.
*   **Step 2.1: Draft Generation:**
    *   Agent: **Architect** (Gemini)
    *   Prompt: `Architect_GEM_MASTER.md` (Combines "Old" strictness + "New" design).
    *   Input: Raw Text + Project State + `design_patterns.json`.
    *   Output: `plans/draft_plan_X.md`.
*   **Step 2.2: The Audit (The Critic):**
    *   Agent: **Auditor** (Gemini - New Role)
    *   Prompt: `Architect_AUDITOR.md`
    *   Action: Compare `draft_plan_X.md` vs `Raw Text` vs `design_patterns.json`.
    *   Checklist:
        1.  Did we miss any sentence from raw text?
        2.  Is the Tashkeel preserved?
        3.  Does the layout follow the "Gold Standard" patterns?
        4.  Are the ID generation instructions explicit?
    *   Output: `Score (0-10)` + `Critique List`.
*   **Step 2.3: Optimization Loop:**
    *   Logic: IF Score < 9: Send Critique back to Architect -> Regenerate Plan.
    *   Repeat up to 3 times.
    *   Final Output: `plans/plan_X_perfect.md`.

### Phase 3: Execution & Dialogue (The Agent)
*   **Goal:** Execute the plan using Jules, handling any ambiguity intelligently.
*   **Step 3.1: Session Dispatch:**
    *   Tool: `beta-utilities/jules_client.py`
    *   Action: Create Jules Session with `plan_X_perfect.md`.
*   **Step 3.2: Intervention Handler (New):**
    *   Action: Poll Session status.
    *   Condition: IF `SUGGESTION_PENDING` (Jules asks a question):
        *   Agent: **Proxy** (Gemini).
        *   Action: Read Jules' question -> Read Plan/Context -> Generate Answer -> Reply to Jules.
*   **Step 3.3: PR Management:**
    *   Action: Wait for `COMPLETED`.
    *   Action: Auto-merge PR (via `gh` CLI) or notify user.

### Phase 4: Verification & Final Polish
*   **Goal:** Ensure the result is bug-free and physically printable.
*   **Step 4.1: The "One-Page Law" Check:**
    *   Tool: `beta-utilities/verify_headless.py` (TO-DO).
    *   Action: Render HTML with WeasyPrint.
    *   Fail: If Page Count > 1 or Content Overflow -> Mark "FAILED" -> Go to **Fix Loop**.
*   **Step 4.2: Content QA:**
    *   Agent: **QA Bot** (Gemini).
    *   Action: Compare Final HTML text vs Raw Text. Rate 1-10.
*   **Step 4.3: The Fix Loop:**
    *   Logic: If simple typo -> Auto-fix with Gemini `replace`.
    *   Logic: If layout fail -> Trigger "Re-Plan" for specific section.

---

## 📋 TO-DO List (Implementation Roadmap)

### 1. Core Utilities (The Foundation)
- [ ] **Create `beta-utilities/workflow_state.py`**: A robust state manager (JSON-based) to track every lesson's status (`RAW`, `PLANNED`, `CODED`, `VERIFIED`).
- [ ] **Create `beta-utilities/verify_headless.py`**: A non-interactive version of `preview.py` that returns JSON status (`{"pages": 1, "overflow": false}`).

### 2. Intelligent Planning (The Brain)
- [ ] **Create `beta-utilities/pattern_extractor.py`**: Script to analyze `pages/` and generate `assets/design_patterns.json`.
- [ ] **Create `Architect_GEM_MASTER.md`**: Merge the "Old" strict constraints with the "New" design vision.
- [ ] **Create `Architect_AUDITOR.md`**: The prompt for the "Critic" agent.
- [ ] **Create `beta-utilities/plan_refiner.py`**: The script that runs the `Draft -> Audit -> Fix` loop using Gemini CLI.

### 3. Jules Integration (The Hands)
- [ ] **Update `beta-utilities/orchestrator.py`**: Add the "Intervention Handler" logic to reply to Jules' questions automatically.
- [ ] **Add `gh` CLI Integration**: Automate the `gh pr merge` step (optional but recommended).

### 4. The Master Control
- [ ] **Create `beta-utilities/workflow_manager.py`**: The main CLI tool that ties it all together.
    *   `python workflow_manager.py --lesson "Lesson 5"`
    *   `python workflow_manager.py --auto-fix`

### 5. Self-Correction Data
- [ ] **Refine `Ideas_Fixes_Advises.md`**: Make this a structured JSON or CSV log so the tool can parse "Past Mistakes" and avoid them.

---

## 🛠️ Usage Example

```bash
# 1. Setup
python tools/state_init.py --reset

# 2. Run the Auto-Maker (Interactive Mode)
python beta-utilities/workflow_manager.py start

# Output:
# [INFO] Processing Lesson: "08.4 Irab Jumal"
# [PLAN] Generating Draft... (Attempt 1)
# [AUDIT] Score: 7/10. Issues: Missing "Golden Rule" box.
# [PLAN] Regenerating... (Attempt 2)
# [AUDIT] Score: 10/10. Plan Perfected.
# [JULES] Session Started. ID: 83920
# [JULES] Question: "Should I use a split grid here?"
# [PROXY] Answering: "Yes, per design_patterns.json rule #4."
# [JULES] PR Created. Merging...
# [VERIFY] Layout: PASS (1 Page). Content: PASS.
# [SUCCESS] Lesson 08.4 Complete!
```

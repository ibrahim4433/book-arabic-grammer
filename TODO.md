# Project TODO: The "Control Room" & System Refactoring

This document outlines the roadmap for transforming the current scripts into a centralized, interactive "Control Room" (`system.py`) utilizing the Jules API and the `system workspace` context.

## 🏗️ Phase 1: Infrastructure & API Integration (Jules)

- [ ] **Jules API Verification & Enhanced Wrapper**
    - [ ] **Research:** Deeply analyze `system workspace/tools/automation/dispatch_jules.py` against the "Jules v1alpha" capabilities (Sessions, Activities, Source Context).
    - [ ] **Refactor `dispatch_jules.py`:** Create a robust `JulesClient` module in `system workspace/tools/automation/modules/jules_client.py`.
        - [ ] Implement `create_session` with precise `sourceContext` (linking to the GitHub repo).
        - [ ] Implement **Session Monitoring**: Do not just "fire and forget". Add polling to check `session.status` or `activities` to confirm completion/PR creation.
        - [ ] Add error handling for API quotas or network failures.
    - [ ] **Test:** Create a `tests/test_jules_connectivity.py` script to verify authentication and basic session creation (dry-run).

- [ ] **System Workspace Consolidation**
    - [ ] **Path Updates:** Update all script references to point to `system workspace/` for prompts.
    - [ ] **Prompt Definition:**
        - [ ] Confirm `system workspace/Architect_GEM_MASTER.md` is the "Master Plan" prompt.
        - [ ] Confirm `system workspace/Architect_AUDITOR.md` is the "Auditor" prompt.
    - [ ] **Prompt Loading:** Create a utility `system workspace/tools/automation/modules/prompt_loader.py` to securely load these prompts.

## 🛠️ Phase 2: Core Tool Refactoring (Modularization)

*The existing tools in `system workspace/tools/automation/` must be refactored into importable modules for `system.py`.*

- [ ] **Module: Vision (OCR)** (`modules/vision.py`)
    - [ ] Refactor logic from `orchestrator.py` (VisionGEM class) and `all_pics_to_text.py`.
    - [ ] Ensure it inputs from `input/` and outputs "Raw Text" to `output/text-data/raw/`.
    - [ ] **Constraint:** Must strictly preserve diacritics (Harakat).

- [ ] **Module: Text Processor** (`modules/text_processing.py`)
    - [ ] Refactor `create_lesson_index.py`.
    - [ ] Functionality: Merge raw text fragments -> Identify Lesson Boundaries -> Map to `TOC.txt`.
    - [ ] Output: `output/text-data/full_raw_indexed.txt` (or structured JSON).

- [ ] **Module: Architect (Planner)** (`modules/planner.py`)
    - [ ] Refactor `plan_refiner.py`.
    - [ ] Input: Raw Lesson Text + `Architect_GEM_MASTER.md`.
    - [ ] Process: Use Gemini 1.5 Pro (Headless) to generate the "Content Stream" plan.
    - [ ] Output: `plans/plan_XX.md`.

- [ ] **Module: Compiler (Jules Dispatcher)** (`modules/compiler.py`)
    - [ ] Refactor `lesson_compiler.py`.
    - [ ] Input: `plans/plan_XX.md`.
    - [ ] Process: Send plan to `JulesClient`.
    - [ ] **Loop:** Monitor Jules -> Wait for PR/Commit -> Trigger "Auditor".

- [ ] **Module: Auditor (Quality Control)** (`modules/auditor.py`)
    - [ ] Implement logic using `Architect_AUDITOR.md` and `Jules workspace/verify_layout.py`.
    - [ ] Process:
        1. Pull generated HTML.
        2. Run `Jules workspace/verify_layout.py` (One-Page Law).
        3. Run Visual Inspection (Gemini Vision) or HTML Linting (`Jules workspace/lint_pages.py`).
        4. **Feedback Loop:** If score < Threshold, send feedback back to Jules (New Session or Reply).

## 🎛️ Phase 3: The "Control Room" (`system.py`)

*The central interactive CLI implementation.*

- [ ] **Interactive Menu Interface (TUI)**
    - [ ] Create `system.py` in the root directory.
    - [ ] Implement the `main` loop with the following menu:
        ```text
        [A] Full Auto Workflow (Images -> Book Page)
        [B] OCR Only (Images -> Raw Text)
        [C] Plan Generation (Raw Text -> Architect Plans)
        [D] Page Generation (Plans -> Jules -> HTML)
        [E] System Status & Debug
        [Q] Quit
        ```

- [ ] **State Management (`system workspace/tools/automation/project_workflow_state.json`)**
    - [ ] Ensure the system tracks the state of every lesson (e.g., `OCR_DONE`, `PLAN_READY`, `PAGE_GENERATED`, `AUDIT_PASS`).
    - [ ] Dashboard View: Option [E] should display a table of all lessons and their current status.

## 🔄 Phase 4: Workflow Implementation Details

- [ ] **Implement Option B (OCR)**
    - [ ] Scan `input/` for new images.
    - [ ] Call `modules.vision`.
    - [ ] Update State: `OCR_DONE`.

- [ ] **Implement Option C (Planning)**
    - [ ] Scan for text with `OCR_DONE` status.
    - [ ] Call `modules.text_processing` then `modules.planner`.
    - [ ] Update State: `PLAN_READY`.

- [ ] **Implement Option D (Generation)**
    - [ ] Scan for plans with `PLAN_READY` status.
    - [ ] Call `modules.compiler` (Jules Dispatch).
    - [ ] Update State: `WAITING_FOR_JULES` -> `PAGE_GENERATED`.

- [ ] **Implement Option A (Full Auto)**
    - [ ] Chain B -> C -> D sequentially for selected inputs.

## ✅ Phase 5: Verification & Testing

- [ ] **Unit Tests:**
    - [ ] Test OCR module with a sample image.
    - [ ] Test Plan generation with a text snippet.
- [ ] **Integration Test:**
    - [ ] Run a "Dry Run" of Option A (mocking the Jules API call) to ensure file flow works.
- [ ] **Jules Live Test:**
    - [ ] Run Option D on a single plan with the real Jules API.
    - [ ] Verify the PR/Commit in the GitHub repo.
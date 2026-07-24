# Project TODO: The "Control Room" & System Refactoring

This document outlines the roadmap for transforming the current scripts into a centralized, interactive "Control Room" (`system.py`) utilizing the Jules API and the `system-workspace` context.

## ✅ Phase 1: Infrastructure & API Integration (Jules)

- [x] **Jules API Verification & Enhanced Wrapper**
    - [x] **Research:** Deeply analyze `system-workspace/tools/automation/dispatch_jules.py`.
    - [x] **Refactor `dispatch_jules.py`:** Create `system-workspace/tools/automation/modules/jules_client.py`.
        - [x] Implement `create_session` with precise `sourceContext`.
        - [x] Implement **Session Monitoring** (polling).
        - [x] Add error handling.
    - [x] **Test:** Create `tests/test_jules_connectivity.py`.

- [x] **system-workspace Consolidation**
    - [x] **Path Updates:** Update all script references to point to `system-workspace/`.
    - [x] **Prompt Definition:** Confirmed prompts are in `system-workspace/`.

## ✅ Phase 2: Core Tool Refactoring (Modularization)

- [x] **Module: Vision (OCR)** (`modules/vision.py`)
    - [x] Refactor logic from `orchestrator.py` and `all_pics_to_text.py`.
    - [x] Use `GeminiClient` generic wrapper.
    - [x] **Constraint:** Strictly preserve diacritics (Harakat).

- [x] **Module: Text Processor** (`modules/text_processing.py`)
    - [x] Refactor `create_lesson_index.py`.
    - [x] **Validation:** Define and enforce `TOC.txt` structure.
    - [x] Functionality: Merge raw text fragments -> Identify Lesson Boundaries -> Map to `TOC.txt`.

- [x] **Module: Architect (Planner)** (`modules/planner.py`)
    - [x] Refactor `plan_refiner.py`.
    - [x] Input: Raw Lesson Text + `Architect_GEM_MASTER.md`.
    - [x] Process: Use Gemini 1.5 Pro (Headless via API).
    - [x] Output: `plans/plan_XX.md`.

- [x] **Module: Compiler (Jules Dispatcher)** (`modules/compiler.py`)
    - [x] Refactor `lesson_compiler.py`.
    - [x] **Critical:** Implement a **Plan-to-Template Mapping Schema** (`mappings/plan_to_template.json`).
    - [x] Update compiler to use this schema for intelligent replacement.
    - [x] Input: `plans/plan_XX.md`.
    - [x] Process: Local Compilation + `JulesClient` Dispatch option.

- [x] **Module: Auditor (Quality Control)** (`modules/auditor.py`)
    - [x] Implement logic using `Jules-workspace/verify_layout.py` and `lint_pages.py`.
    - [x] Process: Run layout verification and linting.

## ✅ Phase 3: The "Control Room" (`system.py`)

- [x] **Interactive Menu Interface (TUI)**
    - [x] Create `system.py` in the root directory.
    - [x] Implement the `main` loop with A-E menu.

- [x] **State Management (`modules/state_manager.py`)**
    - [x] Ensure the system tracks the state of every lesson (`OCR_DONE`, `PLAN_READY`, etc.).
    - [x] Dashboard View: Option [E] displays status.

## 🔄 Phase 4: Workflow Implementation Details

- [x] **Implement Option B (OCR)**
    - [x] Scan `input/` -> Call `modules.vision` -> Update State.

- [x] **Implement Option C (Planning)**
    - [x] Scan for text -> Call `modules.text_processing` -> `modules.planner`.

- [x] **Implement Option D (Generation)**
    - [x] Scan for plans -> Call `modules.compiler` -> `modules.auditor`.

- [x] **Implement Option A (Full Auto)**
    - [x] Chain B -> C -> D sequentially.

## ✅ Phase 5: 1-Page Mode Structural Enhancements

- [x] **Div Tag Enforcement**
    - [x] Update templates to include 1-page mode instructional comments.
    - [x] Update `Architect_GEM_MASTER_1_PAGE.md` to mandate `<div>` tags instead of `<section>` tags.
    - [x] Implement `--one-page-mode` flag in `lint_pages.py` to strictly enforce the `<section>` ban.

## 🚀 Future Tasks

- [ ] **Advanced Table Parsing:** Improve `Compiler._transform_table` to handle complex markdown tables robustly.
- [ ] **Jules Feedback Loop:** Automate the feedback loop where Auditor failure triggers a Jules retry session.

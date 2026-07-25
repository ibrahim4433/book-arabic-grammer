# 📚 Arabic Grammar Book: Curriculum Index

Welcome to the Master Curriculum for the Arabic Grammar Book repository! This index serves as your central hub to navigate the 26 learning modules (Modules 0-25). Each module is hyperlinked below with a description of what it covers.

Click on any module link to begin studying.

---

## 🏗️ Phase 1: The Foundation (Modules 0-2)
*Perfect for beginners bridging the gap into this specific repository.*

* **[Module 0: Python & HTML Fundamentals](module-0.md)**
  * **Description:** A minimalist primer teaching how Python string replacement interacts with HTML components, establishing the baseline mechanism for how this book is generated.
* **[Module 1: Scaling up to the Real Pipeline](module-1.md)**
  * **Description:** Introduces dynamic loops, dictionaries, and the assembly of full HTML pages using the Atomic Design snippets from the repository.
* **[Module 2: The True Foundations & Entry Points](module-2.md)**
  * **Description:** Maps the macro architecture of the repository and explores the `system.sh` boot sequence and `uv` virtual environments.

---

## ⚙️ Phase 2: The Engine Room (Modules 3-7)
*Understanding the core orchestration, generation, and validation pipelines.*

* **[Module 3: The Control Room (`system.py`)](module-3.md)**
  * **Description:** Dissects the `rich`/`questionary` UI engine, the `UILogHandler` for clean console logging, and `project_state.json` persistence.
* **[Module 4: AI, OCR & Automation Pipelines](module-4.md)**
  * **Description:** Explains how the system forms Base64 API payloads and utilizes strict zero-temperature prompts to extract Arabic text while preserving Tashkeel.
* **[Module 5: The HTML Engine & The 1-Page Law](module-5.md)**
  * **Description:** Covers the layout mathematics (pixel-to-millimeter conversion) and the cryptographic generation of `bXXXXX` tracking tags.
* **[Module 6: The Vibe-Coding Aftermath (Fixer Scripts)](module-6.md)**
  * **Description:** Examines AST DOM manipulation via `BeautifulSoup` to resolve technical debt, including standardized `argparse` boilerplate scripts.
* **[Module 7: Real-World Scenarios & Hardcore Debugging](module-7.md)**
  * **Description:** Presents three hardcore scenarios: fixing A4 Layout Overflows, resolving duplicate ID Collisions, and handling OCR hallucinations.

---

## 🚀 Phase 3: The Master Classes (Modules 8-10)
*Advanced CSS architecture and autonomous multimedia handling.*

* **[Module 8: The Paged Media CSS Architecture](module-8.md)**
  * **Description:** Deep dive into `styles/main.css`, revealing how `@page` rules define physical A4 dimensions and protect content from awkward PDF slicing.
* **[Module 9: The Markdown-to-HTML Generator Engine](module-9.md)**
  * **Description:** Explores the Anti-Hallucination wrappers, randomized API jitter, and the brilliant automated "Headless Q&A" fallback.
* **[Module 10: Advanced Multimedia Ingestion](module-10.md)**
  * **Description:** Examines how the system bypasses YouTube blocks using internal subtitle APIs and utilizes the offline `Mishkal` engine to chunk and vocalize Tashkeel.

---

## 🛠️ Phase 4: Exhaustive Codebase Deep Dives - Part 1 (Modules 11-20)
*100% line-by-line codebase breakdowns of the repository's most critical utilities.*

* **[Module 11: The Compiler (`build.py`)](module-11.md)**
  * **Description:** Exhaustive breakdown of the PDF compiler, covering local Python threading, WeasyPrint PDF conversion, and string buffer optimizations.
* **[Module 12: The Layout Enforcer (`verify_layout.py`)](module-12.md)**
  * **Description:** Dissection of the mathematical physics engine that enforces the strict A4 millimeter height limit using `asyncio` and `playwright`.
* **[Module 13: The Cryptographic Tagger (`id_manager.py`)](module-13.md)**
  * **Description:** Deep dive into the cryptographic hashing system that tags every block of Arabic text with a unique `bXXXXX` identifier.
* **[Module 14: The Compliance Linter (`lint_pages.py`)](module-14.md)**
  * **Description:** Breakdown of the BeautifulSoup AST parser that rigorously enforces Atomic HTML structures and rejects inline CSS styles.
* **[Module 15: The UI Control Room (`system.py`)](module-15.md)**
  * **Description:** 100% logic coverage of the main TUI dashboard, highlighting the multi-threaded routing and safe error handling.
* **[Module 16: The API Bridge (`gemini_client.py`)](module-16.md)**
  * **Description:** Detailed analysis of the fallback communication layer that switches between REST HTTP and Headless Subprocesses when rate-limited.
* **[Module 17: The Async OCR Engine (`jules_ocr.py`)](module-17.md)**
  * **Description:** Explores the parallel `ThreadPoolExecutor` and asynchronous wait polling used to batch process massive textbooks.
* **[Module 18: The Content Stream Orchestrator (`jules_planner.py`)](module-18.md)**
  * **Description:** Breakdown of the AI Planning phase, covering regex extraction, state tracking, and Context Starvation Prevention.
* **[Module 19: The HTML Generator & Autonomous Q&A (`jules_page_generator.py`)](module-19.md)**
  * **Description:** Detailed look at how the orchestrator creates AI sessions, limits hallucinations, and uses a local LLM to answer the remote AI's questions automatically.
* **[Module 20: The Data Indexer (`text_processing.py`)](module-20.md)**
  * **Description:** Dissection of the data normalizer that concatenates raw text files, numbers every line, and slices content at `----- PAGE X -----` markers.

---

## 🧩 Phase 5: Exhaustive Codebase Deep Dives - Part 2 (Modules 21-25)
*100% line-by-line codebase breakdowns of the Advanced Orchestration Suite.*

* **[Module 21: The Database Engine (`state_manager.py`)](module-21.md)**
  * **Description:** Breakdown of the JSON-based NoSQL persistence layer, covering garbage collection, physical file verification, and crash recovery.
* **[Module 22: The Supreme Orchestrator (`full_auto_workflow.py`)](module-22.md)**
  * **Description:** Massive deep dive into the 8-step Master State Machine, exploring Graceful Degradation via `ImportError` and safe `Ctrl+C` interrupt handling.
* **[Module 23: The Indexer (`rebuild_toc.py`)](module-23.md)**
  * **Description:** Analysis of the DOM mutator that calculates how to safely squeeze 30 Answer Keys and 20 Lessons into a single, perfectly balanced 2-column A4 HTML table.
* **[Module 24: The Synchronizer (`sync_pages.py`)](module-24.md)**
  * **Description:** Exhaustive look at the algorithmic renamer that mathematically syncs filenames to match absolute physical printing order.
* **[Module 25: The AST DOM Fixer (`fix_book.py`)](module-25.md)**
  * **Description:** Breakdown of the automated technical debt cleaner that uses Regex to correct AI hallucinated titles and dynamically updates dependent Answer Key files.

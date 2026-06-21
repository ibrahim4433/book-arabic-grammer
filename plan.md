1. **Explore and set up**
   - Read memory and rules. Ensure all work happens inside `Jules-workspace`.
   - Ensure the directory `Jules-workspace/pages/` exists.

2. **Generate the First Page (03.0_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ.html)**
   - Create the base HTML using components from `Jules-workspace/Templates/`.
   - Incorporate the header (`TEMPLATE_C_HEADER.html`).
   - Add Block 1 to Block 9 contents (`مُقَدَّمَةً` to `تَنْبِيه`).
   - Use utility classes `h-8mm`, `mt-2mm`, `highlight-green`, etc.
   - Run `python3 id_manager.py auto-tag` to generate unique IDs.
   - Run `python3 lint_pages.py` and `python3 verify_layout.py` to ensure it passes A4 validation.

3. **Generate the Second Page (03.1_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ.html)**
   - Create a new HTML file for the remaining content (Blocks 10 to 17).
   - Continue with the lesson content (`٣. فعَلّ الْأَمْرِ` and the exams).
   - Provide answers-less exam blocks at the end.
   - Use `h-8mm` for inputs.
   - Add extra padding questions to fill underflow so the page density is high.
   - Run `python3 id_manager.py auto-tag` to generate unique IDs.
   - Run `python3 lint_pages.py` and `python3 verify_layout.py` to verify formatting.

4. **Final Verifications & Pre-commit Steps**
   - Ensure `id_manager.py verify` passes successfully to check for duplicate IDs.
   - Verify Playwright UI verification via `frontend_verification_instructions` and verify screens.
   - Call `pre_commit_instructions` tool and execute the checks.
   - Ensure proper testing, verification, review, and reflection are done.

5. **Submit changes**
   - Commit and submit changes once all tests pass.

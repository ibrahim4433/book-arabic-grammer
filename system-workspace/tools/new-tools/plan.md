1. **Restore initial state:** Restore `pages/10.0_nXX_الْفَاعِلُ وَأَنْوَاعُهُ وَعَلَاَّمَاتُ إِعْرَابِهِ.html` from git to remove the changes that `id_manager.py auto-tag` performed.
2. **Re-create HTML File:** Create `Jules-workspace/pages/10.0_nXX_الْفَاعِلُ وَأَنْوَاعُهُ وَعَلَاَّمَاتُ إِعْرَابِهِ.html` containing the correct content per STREAM, matching the templates. Wait to run `auto-tag` later. The generated HTML will have the components as presented before, with the unique requirements.
3. **Run ID Manager:** Run `Jules-workspace/id_manager.py auto-tag` to generate missing IDs. Verify success.
4. **Final Layout Check:** Check layout by running `verify_layout.py`. Confirm the remaining blank space is below the recommended threshold. (We expect ~7.4% blank space, which was valid previously).
5. **Verify Formatting (Linting):** Run `lint_pages.py` to ensure zero inline styles are used and classes match `styles/main.css`.
6. **Pre-commit Steps:** Call `pre_commit_instructions` to ensure proper testing, verification, review, and reflection are done.
7. **Submit:** Submit changes.

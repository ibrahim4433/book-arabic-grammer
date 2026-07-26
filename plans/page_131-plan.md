# **SESSION 131**

[TASK DEFINITION]
Objective: Implement page 131.
File: `pages/page_131.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools. If it overflows, it is a catastrophic failure. Do NOT try to solve overflow by deleting text (Strict Typographer Rule). Solve it by choosing denser templates or omitting optional white-space.
2.5 Cut Content: If content is violently split by the page boundary, strictly follow the [CUT CONTENT HANDLING] rules using `TEMPLATE_CUT_BOX_PART_1.html` and `TEMPLATE_CUT_BOX_PART_2.html`. Ensure exact visual continuity (same title, same classes).
2.6 Cut Content Determinism: When handling cut content or starting a page mid-section, you MUST use the "Keyword-to-Template Deterministic Mapping" in `elements_index.md` to identify the correct template to use for the continuation. You are forbidden from guessing. Scan the raw text for the preceding keyword to determine the active template and apply the correct `_PART_2.html` wrapping.
3. text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice.
4. Highlighting: Use `.highlight-red` for primary focus words and `.highlight-blue`,`.highlight-green`  for secondary.
5. Definitions: Must use `.text-accent` class.
6. Mandatory Style Guide:
*   **Rule:** NO INLINE STYLES.
*   **Rule:** Irab Words inside `.irab-word` MUST be white. Do NOT use `.highlight-*` classes.
*   **Mapping:**
    *   `style="width: 20%"` -> `class="w-20pct"`
    *   `style="margin-top: 2mm"` -> `class="mt-2mm"`
    *   `style="text-align: center"` -> `class="text-center"`
    *   `style="font-weight: bold"` -> `class="font-bold"`
6. Templates: You are forbidden from inventing new HTML tags or classes or template elements. You must map all content using "Jules-workspace/Templates/" components as the STREAM says in suitable way. **CRITICAL 1-PAGE MODE RULE**: You MUST NOT use `<section>` tags when applying templates. Replace any `<section>` tags from the templates with `<div>` tags (keep `<header>` for page headers as is).
7. Unique IDs: All content blocks must have a unique ID (id='bXXXXX'). The ID MUST be applied to the `<div>` tag that replaced the `<section>` tag. Use "Jules-workspace/id_manager.py" to generate or verify them.
8. **Self-Correction:** Run "Jules-workspace/lint_pages.py --one-page-mode <filename>" after creating html files. If it fails, you MUST fix the errors (usually inline styles or forbidden section tags) before submitting.
9. Do not summarize examples.
10. Do not provide uncompleted text content using (...) .
11. You MUST preserve the EXACT Tashkeel (Harakat) from the input. Stripping diacritics is a critical failure. Do not generate bare Arabic letters without their vowels.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. **Page Wrappers**: The compiler will automatically wrap the final page in `TEMPLATE_C_PAGE_WRAPPER.html`. Do NOT include this template in your `[CONTENT STREAM]` blocks.
15. **Exam Section**: ONLY include the `TEMPLATE_C_EXAM.html` block if the provided raw text slice actually contains test/exam questions (e.g., keywords like "تطبيق", "امتحان"). Do NOT hallucinate an exam if it is not in the source text. **CRITICAL:** If an exam or exercise contains the answers in the raw text, you MUST use `TEMPLATE_C_EXAM_SOLVED.html` instead of `TEMPLATE_C_EXAM.html`.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[CATEGORY_HEADER]: 131
[SECTION_HEADER]: 131
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+
[LESSON_NUMBER]: 131
[CHAPTER_TITLE]: page 131

=== BLOCK 2: أبيات متفرقة ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b76426
[POEM_TITLE]:
[POET_NAME]:
[RIGHT_HEMISTICH]: لَنْ تَرَيْ حَفْنَةَ رَمْلٍ فَوْقَها
[LEFT_HEMISTICH]: لَمْ تُعَطَّرْ بِدِمَا حُرِّ أَبِي
[RIGHT_HEMISTICH]: قَدْ عَرَفْنَا مَهْرَكِ الغالي فَلَم
[LEFT_HEMISTICH]: نُرْخِصِ الْمَهْرَ وَلَمْ تَخْتَسِبِ
[RIGHT_HEMISTICH]: وَأَرَقُناها دِمَاءً حُرَّةً
[LEFT_HEMISTICH]: فَاغْرِفِي مَا شِنْتِ مِنْهَا وَاشْرَبي
[RIGHT_HEMISTICH]: يَا رَاقِدًا فِي رَوَابِي مَيْسَلُونَ أَفِقْ
[LEFT_HEMISTICH]: جَلَتْ فَرَنْسا فَمَا فِي الدَّارِ هَشَامُ

=== BLOCK 3: ثبات الحق ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b52041
[POEM_TITLE]: - ثبات الحق في وَجْهِ المُغْتَصِب:
[POET_NAME]: عمر أبو ريشة :
[RIGHT_HEMISTICH]: لا يَمُوتُ الحَقُّ مَهْمَا لَطَمَتْ
[LEFT_HEMISTICH]: عَارِضَيْهِ قَبْضَةُ المُغْتَصِبِ

=== BLOCK 4: الإصرار ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b87869
[POEM_TITLE]: ه - الإصرار على تَحَدِّي قُوَّةِ الْمُسْتَعْمِرِ رغم ضَعْفِ الإِمْكَانَات:ِ
[POET_NAME]: عمر أبو ريشة:
[RIGHT_HEMISTICH]: نَحْنُ مِنْ ضَعْفٍ بَنَيْنَا قُوَّةً
[LEFT_HEMISTICH]: لم تَلِنْ للمارج الملتهب

=== BLOCK 5: دور الأبطال ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b41578
[POEM_TITLE]: دور الأبطال في حمايةِ الْأَرْضِ وَحِفْظِ كَرَامَتِها رفض الحماية والوصاية والانْتِدَابِ مِنْ قِبَلِ الْمُسْتَعْمِرِ(:
[POET_NAME]: عمر أبو ريشة :
[RIGHT_HEMISTICH]: هَذِهِ تُرْبَتُنَا لَنْ تَزْدَهِي
[LEFT_HEMISTICH]: سوانا مِنْ حُمَاةٍ نُدُبِ

=== BLOCK 6: الاعتزاز بالماضي ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b20817
[POEM_TITLE]: الاعتزاز بالماضي المجيد والإشادة بمروءة العربي:
[POET_NAME]: عمر أبو ريشة
[RIGHT_HEMISTICH]: من هنا شق الهدى أكمامه
[LEFT_HEMISTICH]: وادی موكبا في موكب
[RIGHT_HEMISTICH]: وأتى الدنيا فَرَفَّتْ طَرَبًا
[LEFT_HEMISTICH]: وانْتَشَتْ مِنْ عَبْقِهِ الْمُنْسَكِبِ
[RIGHT_HEMISTICH]: وتعنت بالمروءات التي
[LEFT_HEMISTICH]: عَرَفَتْهَا فِي فَتَاها العربي

=== BLOCK 7: امتداد فتوحات ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b34456
[POEM_TITLE]: امتداد فتوحات العربي خارج نطاقِ الأَرْضِ الْعَرَبِيَّة:
[POET_NAME]: عمر أبو ريشة :
[RIGHT_HEMISTICH]: أَصْيَدُ ضَاقَتْ بِهِ صَحْرَاؤُهُ
[LEFT_HEMISTICH]: فأعدته لأفق أرحب
[RIGHT_HEMISTICH]: هب للفتح فَأَدْمى تَحْتَهُ
[LEFT_HEMISTICH]: حَافِرُ المُهْرِ جَبِينَ الكُوكَبِ

=== BLOCK 8: الإشادة بالدور ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b82186
[POEM_TITLE]: - الإشادة بالدورِ النِّصَالِي وَتَثْمِينُه:ُ
[POET_NAME]: نزار قباني:
[RIGHT_HEMISTICH]: وَضَعِي طَرْحَةَ الْعَرُوسِ لِأَجْلِي
[LEFT_HEMISTICH]: إِنَّ مَهْرَ الْمُنَاضِلَاتِ ثَمِينُ

=== BLOCK 9: رابعاً ===
(Component: TEMPLATE_C_TABLE.html)
[UNIQUE_ID]: b52017
[TITLE]: رابعاً
[CONTENT]: - الأدب وانتصارات تشرين:

=== BLOCK 10: التعبير عن مشاعر ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b55850
[POEM_TITLE]: - التَّعْبِيرِ عَنْ مَشَاعِرِ الفَرَحِ وَالزهو بِنَصْرِ تشرين :
[POET_NAME]: نزار قباني:
[RIGHT_HEMISTICH]: مَرَّقِي يَا دِمَشْقُ خَارِطَةَ الذ
[LEFT_HEMISTICH]: ذَلِ وَقُولي للدَّهْرِ كُنْ فَيَكُونُ
[RIGHT_HEMISTICH]: استَرَدَّتْ أَيَّامَهَا بِكِ بَدْرٌ
[LEFT_HEMISTICH]: واستَعَادَتْ شَبَابَهَا حِطِينُ
[RIGHT_HEMISTICH]: هُ مَ الرُّومُ بَعْدَ سَبْعِ عِجَافٍ
[LEFT_HEMISTICH]: وتَعَافَ وُجْدَانُنَا المُطْعُونُ

=== BLOCK 11: أثر انتصار ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b11624
[POEM_TITLE]: - أثر انتصار تشرین زوال آثَارِ نَكْسَةِ حُزَيْرَان(:
[POET_NAME]: نزار قباني:
[RIGHT_HEMISTICH]: هُ مَ الرُّوْمُ بَعْدَ سَبْعِ عِجَافٍ
[LEFT_HEMISTICH]: وتَعَالَى وُجْدَانُنَا المُطْعُونُ

=== BLOCK 12: التعبير عن الإصرار ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b37953
[POEM_TITLE]: التَّعْبِيرُ عَنِ الإِصْرَارِ على المُقَاوَمَةَ وَالنَّضَالِ مادام السلاح مُتَاحًا رفض الخنُوعِ والدُّل مادام السلاح مُتَاحًا(:
[POET_NAME]: عمر أبو ريشة :
[RIGHT_HEMISTICH]: ما حملنا ذل الْحَيَاةِ وَفِي القَوْ
[LEFT_HEMISTICH]: س نبال وفي الأَكْفٍ بَوَاتِر

=== BLOCK 13: خامساً ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
[UNIQUE_ID]: b06331
[TITLE]: خامساً
[CONTENT]: - الأدب الفلسطيني )مرحلة النهوض الثوري(

=== BLOCK 14: إبراز تمسك ===
(Component: TEMPLATE_C_POEM.html)
[UNIQUE_ID]: b50220
[POEM_TITLE]: - إبراز تمسك الفلسطينيين بفكرة النضال في سبيل الوجود:
[POET_NAME]: توفيق زیاد:
[RIGHT_HEMISTICH]: أَهْوَنُ أَلْفَ مَرَّهُ
[LEFT_HEMISTICH]: أَنْ تُدْخِلُوا الْفِيْلَ بِغَقُبِ إِبْرَهُ
[RIGHT_HEMISTICH]: مِنْ أَنْ تُمِيتُوا بِاصْطِهَادِكُم وَمِيضَ فِكْرَهُ
[LEFT_HEMISTICH]: وتَحْرِفُونَا عَنْ طَرِيقِنَا الذي اخْتَرْنَاهُ
[RIGHT_HEMISTICH]: قَيْدَ شَعْرَهُ
[LEFT_HEMISTICH]:

--- END STREAM ---
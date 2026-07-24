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
11. You must preserve the **exact** Tashkeel provided in the input and add any missing Tashkeel needed if any.
12. Visual Density: The page must be dense. Do NOT leave empty space. If content is split, ensure the remaining page is filled with relevant exercises or benefits.
13. balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal
14. Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html` (which provides `.force-new-page`) as defined in `elements_index.md`.
15. Exam section always be in the end of the lesson ( in the final page of that lesson) ,and without the answers !

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[LESSON_NUMBER]: 131
[CHAPTER_TITLE]: page 131
[CATEGORY_HEADER]: 131
[SECTION_HEADER]: 131
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+

=== BLOCK 2: تتمة القصيدة ===
(Component: TEMPLATE_CUT_BOX_PART_2.html)
Title: تتمة
Content:
Use `TEMPLATE_C_POEM.html` inside to display the following verses exactly as provided:
لَنْ تَرَيْ حَفْنَةَ رَمْلٍ فَوْقَها *** لَمْ تُعَطَّرْ بِدِمَا حُرِّ أَبِي
قَدْ عَرَفْنَا مَهْرَكِ الغالي فَلَم *** نُرْخِصِ الْمَهْرَ وَلَمْ تَخْتَسِبِ
وَأَرَقُناها دِمَاءً حُرَّةً *** فَاغْرِفِي مَا شِنْتِ مِنْهَا وَاشْرَبي
يَا رَاقِدًا فِي رَوَابِي مَيْسَلُونَ أَفِقْ *** جَلَتْ فَرَنْسا فَمَا فِي الدَّارِ هَشَامُ

=== BLOCK 3: مواقف الشعراء (The Core Matrix) ===
(Component: TEMPLATE_C_TABLE.html)
Table Headers: الفكرة | الشاعر | الشاهد
Row 1:
- الفكرة: - ثبات الحق في وَجْهِ المُغْتَصِب:
- الشاعر: عمر أبو ريشة :
- الشاهد: لا يَمُوتُ الحَقُّ مَهْمَا لَطَمَتْ *** عَارِضَيْهِ قَبْضَةُ المُغْتَصِبِ
Row 2:
- الفكرة: ه - الإصرار على تَحَدِّي قُوَّةِ الْمُسْتَعْمِرِ رغم ضَعْفِ الإِمْكَانَاتِ:
- الشاعر: عمر أبو ريشة:
- الشاهد: نَحْنُ مِنْ ضَعْفٍ بَنَيْنَا قُوَّةً *** لم تَلِنْ للمارج الملتهب
Row 3:
- الفكرة: دور الأبطال في حمايةِ الْأَرْضِ وَحِفْظِ كَرَامَتِها (رفض الحماية والوصاية والانْتِدَابِ مِنْ قِبَلِ الْمُسْتَعْمِرِ):
- الشاعر: عمر أبو ريشة :
- الشاهد: هَذِهِ تُرْبَتُنَا لَنْ تَزْدَهِي *** سوانا مِنْ حُمَاةٍ نُدُبِ

=== BLOCK 4: الاعتزاز والإشادة ===
(Component: TEMPLATE_C_BLOCK.html)
Title: الاعتزاز بالماضي المجيد والإشادة بمروءة العربي:
Content:
عمر أبو ريشة :
من هنا شق الهدى أكمامه *** وأدى موكبا في موكب
وأتى الدنيا فَرَفَّتْ طَرَبًا *** وانْتَشَتْ مِنْ عَبْقِهِ الْمُنْسَكِبِ
وتعنت بالمروءات التي *** عَرَفَتْهَا فِي فَتَاها العربي
(Add a sub-section/paragraph):
امتداد فتوحات العربي خارج نطاقِ الأَرْضِ الْعَرَبِيَّة:
عمر أبو ريشة :
أَصْيَدُ ضَاقَتْ بِهِ صَحْرَاؤُهُ *** فأعدته لأفق أرحب
هب للفتح فَأَدْمى تَحْتَهُ *** حَافِرُ المُهْرِ جَبِينَ الكُوكَبِ
(Add a sub-section/paragraph):
- الإشادة بالدورِ النِّصَالِي وَتَثْمِينُهُ:
نزار قباني:
وَضَعِي طَرْحَةَ الْعَرُوسِ لِأَجْلِي *** إِنَّ مَهْرَ الْمُنَاضِلَاتِ ثَمِينُ

=== BLOCK 5: الأدب وانتصارات تشرين ===
(Component: TEMPLATE_C_BLOCK.html)
Title: رابعاً - الأدب وانتصارات تشرين:
Content:
- التَّعْبِيرِ عَنْ مَشَاعِرِ الفَرَحِ وَالزهو بِنَصْرِ تشرين :
نزار قباني:
مَرِّقِي يَا دِمَشْقُ خَارِطَةَ الذُّلِّ *** وَقُولي للدَّهْرِ كُنْ فَيَكُونُ
استَرَدَّتْ أَيَّامَهَا بِكِ بَدْرٌ *** واستَعَادَتْ شَبَابَهَا حِطِينُ
هُزِمَ الرُّومُ بَعْدَ سَبْعِ عِجَافٍ *** وتَعَافَ وُجْدَانُنَا المُطْعُونُ
(Add a sub-section/paragraph):
- أثر انتصار تشرین (زوال آثَارِ نَكْسَةِ حُزَيْرَان):
نزار قباني:
هُزِمَ الرُّوْمُ بَعْدَ سَبْعِ عِجَافٍ *** وتَعَالَى وُجْدَانُنَا المُطْعُونُ
(Add a sub-section/paragraph):
التَّعْبِيرُ عَنِ الإِصْرَارِ على المُقَاوَمَةَ وَالنَّضَالِ مادام السلاح مُتَاحًا (رفض الخنُوعِ والدُّل مادام السلاح مُتَاحًا):
عمر أبو ريشة :
ما حملنا ذل الْحَيَاةِ وَفِي القَوْسِ *** نِبالٌ وفي الأَكُفِّ بَوَاتِرُ

=== BLOCK 6: الأدب الفلسطيني ===
(Component: TEMPLATE_C_BLOCK.html)
Title: خامساً - الأدب الفلسطيني (مرحلة النهوض الثوري)
Note: Use `.block-header accent` for this block's header to satisfy the teal/orange balance rule.
Content:
- إبراز تمسك الفلسطينيين بفكرة النضال في سبيل الوجود:
- -
توفيق زیاد:
أَهْوَنُ أَلْفَ مَرَّهُ
أَنْ تُدْخِلُوا الْفِيْلَ بِثَقْبِ إِبْرَهْ
مِنْ أَنْ تُمِيتُوا بِاضْطِهَادِكُمْ وَمِيضَ فِكْرَهْ
وتَحْرِفُونَا عَنْ طَرِيقِنَا الذي اخْتَرْنَاهُ
قَيْدَ شَعْرَهْ

--- END STREAM ---

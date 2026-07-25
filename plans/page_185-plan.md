# **SESSION 185**

[TASK DEFINITION]
Objective: Implement page 185.
File: `pages/page_185.html`
Reference: Follow patterns in design_patterns.json.

[CONSTRAINTS & PROTOCOLS]
1. Source of Truth: Adhere strictly to BOOK_RULES.md and elements_index.md
2. Strict 1-Page Fit: The generated content MUST visually fit on exactly one A4 page when rendered. You MUST instruct the generator to verify this using `verify_layout.py` or equivalent tools.
3. Text Content: 100% Arabic with full Harakat. Must use EVERY WORD from the provided text slice. Under the Typo Exception, obvious typos and OCR artifacts (like original page numbers) are corrected.
4. Mandatory Style Guide: NO INLINE STYLES. Use predefined utility classes.
5. Templates: You are forbidden from inventing new HTML tags. Use strictly `Jules-workspace/Templates/` components. Replace `<section>` tags from the templates with `<div>` tags (keep `<header>`).
6. Unique IDs: All content blocks must have a unique ID (id='bXXXXX') applied to the `<div>`. Use `id_manager.py` to generate or verify them.
7. You must preserve the exact Tashkeel provided in the input and add any missing Tashkeel needed.
8. Visual Density: The page must be dense. Do NOT leave empty space.
9. Balanced Page Colors: Ensure color balance by including at least one orange template element per page.
10. Page Wrappers: Every HTML page content must be wrapped using `TEMPLATE_C_PAGE_WRAPPER.html`.

[CONTENT STREAM]

--- START STREAM ---

=== BLOCK 1: Lesson Header ===
(Component: TEMPLATE_C_HEADER.html)
[CATEGORY_HEADER]: 185
[SECTION_HEADER]: 185
[AUTHOR_NAME]: أ.الياس خفيف
[AUTHOR_PHONE]: 994066850 963+
[CHAPTER_TITLE]: page 185
[LESSON_NUMBER]: 185

=== BLOCK 2: مقدمة ===
(Component: TEMPLATE_C_BLOCK.html)
Title:
Content: الغاب لديه كل شيء، وهو الأمل <span class="text-accent">النهائي</span> أيضًا لكل شيء. وعاد وأكد أنَّ الغِنَاءَ هو سر السَّعَادَةِ الحَقِيقِيَّةِ الخَالِدَة.ِ ومن هذه المقطوعة :

=== BLOCK 3: المقطوعة الأولى ===
(Component: TEMPLATE_C_POEM.html)
[POET_NAME]:
[RIGHT_HEMISTICH_1]: لَيْسَ فِي الغَابِ رَجَاءٌ
[LEFT_HEMISTICH_1]: لا ولا فِيهِ الْمَلَلْ
[RIGHT_HEMISTICH_2]: كيف يرجو الغَابُ جُزْءًا
[LEFT_HEMISTICH_2]: وعَلَى الكُلِّ حَصَل؟!
[RIGHT_HEMISTICH_3]: أَمَلا وهو الأمل؟
[LEFT_HEMISTICH_3]: وبما السَّعْيُ بِغَابِ
[RIGHT_HEMISTICH_4]: إنما العَيْشُ رَجَاءٌ
[LEFT_HEMISTICH_4]: إحدى هاتيك العلل
[RIGHT_HEMISTICH_5]: أَعْطِنِي النَّايَ وَغَنَ
[LEFT_HEMISTICH_5]: فالناي نَارٌ وَنُور
[RIGHT_HEMISTICH_6]: وأنينُ النَّاي شَوْقُ
[LEFT_HEMISTICH_6]: لا يُدَانِيهِ الفُتُور

=== BLOCK 4: وصف الغابة والطبيعة ===
(Component: TEMPLATE_C_BLOCK.html)
Title:
Content: المَقَطُوعَةُ السَّادِسة (مقطوعة وصف الغابة والطبيعة): اختَلَفَتِ المَقْطُوعَةُ السَّادِسَةُ عَنْ بَاقِي القَصِيدَةِ مِنْ حيث البنية التركيبية اللفظية، وأيضا وزن القافية، حيث وَصَفَ جبران طبيعة لبنان الخَلَّابَةَ وَتَخَيَّلَ نَفْسَهُ بين جبالها وسهولها،

=== BLOCK 5: ترك حياة التمدن ===
(Component: TEMPLATE_C_BENEFIT_WARNING.html)
Content: ودعا الناس لترك حياةِ التَّمَدُّنِ الزَّائِفَةِ وَالتَّوجه لحياة الغاب الطبيعية، حيث البقاء بين الماء، ورَحِيقِ الأزهار وأشعةِ الشَّمْسِ الدَّافِئَة،ِ والثمار اليانعة، والاستمتاع بالطَّبِيعَةِ السَّاحِرَةِ ،

=== BLOCK 6: ضعف الإنسان ===
(Component: TEMPLATE_C_TABLE.html)
[ROW_1_COL_1]: ثم أَقَرَ جبران
[ROW_1_COL_2]: بِضَعْفِ الإنسان وعَجْزِهِ عَنِ القيام بذلك؛
[ROW_2_COL_1]: لأن الحياة تفرض عليه
[ROW_2_COL_2]: تَعْقِيدَاتٍ صَارِمَةً بِتَحْقِيقِ مصالحه. ومن هذه المقطوعة:

=== BLOCK 7: المقطوعة السادسة ===
(Component: TEMPLATE_C_POEM.html)
[POET_NAME]:
[RIGHT_HEMISTICH_1]: لَيْسَ فِي الغَابَاتِ مَوت
[LEFT_HEMISTICH_1]: لا ولا فيهَا القُبُورُ
[RIGHT_HEMISTICH_2]: فَإِذَا نَيْسَانُ ولي
[LEFT_HEMISTICH_2]: لم يمت معه السرور
[RIGHT_HEMISTICH_3]: إِنَّ هَوْلَ الْمَوْتِ وَهُمْ
[LEFT_HEMISTICH_3]: يَنْثَنِي طَيَّ الصَّدُور
[RIGHT_HEMISTICH_4]: فالذي عَاشَ رَبِّيْعًا
[LEFT_HEMISTICH_4]: كالذي عاش الدهور
[RIGHT_HEMISTICH_5]: أَعْطِنِي النَّايَ وَغَنَّ
[LEFT_HEMISTICH_5]: فالناي سِرُّ الخُلُود
[RIGHT_HEMISTICH_6]: وأنينُ النَّايِ يَبْقَى
[LEFT_HEMISTICH_6]: بَعْدَ أَنْ يَفْنَى الوُجُود
[RIGHT_HEMISTICH_7]: أَعْطِنِي النَّايَ وَغَنَ
[LEFT_HEMISTICH_7]: وانس ما قُلْتُ وقُلْنا
[RIGHT_HEMISTICH_8]: إنما النُّطْقُ هَبَاءٌ
[LEFT_HEMISTICH_8]: فَأَفِدْنِي ما فَعَلُنا
[RIGHT_HEMISTICH_9]: هل تَخِذْتَ الغَابَ مِثْلِي
[LEFT_HEMISTICH_9]: مَنْزِلَا دُونَ القُصُور
[RIGHT_HEMISTICH_10]: والعَنَاقِيدُ تَدَلَّتْ
[LEFT_HEMISTICH_10]: كَتُرَيَّاتِ الذَّهَبْ؟
[RIGHT_HEMISTICH_11]: فهي الصَّادِي عُيُون
[LEFT_HEMISTICH_11]: وَلِمَنْ جَاعَ الطَّعَامُ
[RIGHT_HEMISTICH_12]: وهي شَهْدٌ وهي عطر
[LEFT_HEMISTICH_12]: وَلِمَنْ شَاءَ الْمُدَامُ
[RIGHT_HEMISTICH_13]: هَلْ فَرَشْتَ الْعُشْبَ لَيْلًا
[LEFT_HEMISTICH_13]: وَتَلَخَفُتَ الفَضَا
[RIGHT_HEMISTICH_14]: ما النَّاسُ سُطُور
[LEFT_HEMISTICH_14]: كُتِبَتْ لَكِنْ بِمَاءً
[RIGHT_HEMISTICH_15]: لَيْتَ شِعْرِي أَيُّ نَفْعِ
[LEFT_HEMISTICH_15]: في اجْتِمَاعِ وَزَحَامُ
[RIGHT_HEMISTICH_16]: وَجَدَالِ وَضَجِيجِ
[LEFT_HEMISTICH_16]: واحْتِجَاجِ وَخِصَامُ؟
[RIGHT_HEMISTICH_17]: كُلِّها أَنْفَاقُ خُلْدٍ
[LEFT_HEMISTICH_17]: وخيوط العَنْكَبُوتُ
[RIGHT_HEMISTICH_18]: فالذي يحيا بعجز
[LEFT_HEMISTICH_18]: فهو في بطء يموت

--- END STREAM ---

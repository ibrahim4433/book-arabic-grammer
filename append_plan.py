import re

filepath = "plans/003-الأمير الدمشقي-plan_uyvyw.md"
try:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    content = ""

if "=== BLOCK 1: TEMPLATE_C_HEADER.html ===" in content:
    # Since Part 3 should be isolated (strict part isolation) according to the Master Architect instructions:
    # "IF PART 3 IS REQUESTED: EXPLANATION STRUCTURE... Generate only the blocks relevant to the requested Part"
    # Wait, the 1-Part method dictates that the final plan for this run is for Part 3.
    # The output format specifies the filename part_3_lesson_003-plan.md, but the prompt says 003-الأمير الدمشقي-plan_uyvyw.md is the output, and I need to generate ONLY Part 3.
    # Actually, the file currently contains Session 003.1 (Part 1). I should rewrite or append. Let me check the prompt:
    # "When updating an existing Architect Plan file, never overwrite the entire file. You must read the existing file's contents and append any new template blocks specifically within the [CONTENT STREAM] section, preserving all previously generated and validated blocks."
    # Wait, the memory says "never overwrite the entire file. You must read the existing file's contents and append any new template blocks specifically within the `[CONTENT STREAM]` section".
    pass

new_blocks = """
=== BLOCK 3: TEMPLATE_LIT_PART_3_EXPLANATION.html ===
(Component: TEMPLATE_LIT_PART_3_EXPLANATION.html)
[UNIQUE_ID_1]
b1
[UNIQUE_ID_2]
b1_split
[UNIQUE_ID_3]
b1_col1
[UNIQUE_ID_4]
b1_block_exp
[UNIQUE_ID_5]
b1_col2
[UNIQUE_ID_6]
b1_block_irab
[POEM_VERSE_HEMISTICHS]
<div class="hemistich">فَهَلْ سَتُفَكِّرُ فِينَا قَلِيلًا ؟</div>
<div class="hemistich">وتَرْجِعُ فِي آخِرِ الصَّيْفِ حَتَّى نَرَاكَ ..</div>
<div class="hemistich">أتوفيق ...</div>
<div class="hemistich">إِنِّي جَبَانٌ أَمَامَ رِثَائِكَ ..</div>
<div class="hemistich">فَارْحَمْ أَبَاكَ ....</div>
[EXPLANATION_CONTENT_ITEMS]
<li>
  <span class="marker">•</span>
  <span>بَعْدَ فَقْدِكَ تَقَرَّحَتْ أَجْفَانِي، وَصِرْتُ عَاجِزًا لا أَقوَى عَلَى الْقِيَامِ بِأَيِّ شَيْءٍ كَطَائِرٍ مَهِيضِ الْجَنَاحِ فَحِينَمَا بَادَرْتُ إِلَى رِثَائِكَ، وَجَدْتُ الْكَلِمَاتِ مُشَوَّهَةً مُحَطَّمَةً، وَجَدْتُ اللُّغَةَ عَاجِزَةً عَنْ رِثَائِكَ، غَارِقَةً فِي دُمُوعِ أَحْزَانِي، مُتَلَاشِيَةً أَمَامَ نِيرَانِ فَقْدِكَ.</span>
</li>
[IRAB_CONTENT_ITEMS]


=== BLOCK 4: TEMPLATE_LIT_PART_3_EXPLANATION.html ===
(Component: TEMPLATE_LIT_PART_3_EXPLANATION.html)
[UNIQUE_ID_1]
b2
[UNIQUE_ID_2]
b2_split
[UNIQUE_ID_3]
b2_col1
[UNIQUE_ID_4]
b2_block_exp
[UNIQUE_ID_5]
b2_col2
[UNIQUE_ID_6]
b2_block_irab
[POEM_VERSE_HEMISTICHS]
<div class="hemistich">أَحْمِلُكَ فَوْقَ ظَهْرِي كَمِئْذَنَةٍ طَاهِرَةٍ انْشَطَرَتْ نِصْفَيْنِ</div>
<div class="hemistich">وقد ذَكَّرَتْنِي خُصْلَاتُ شَعْرِكَ الذَّهَبِيِّ بِسَنَابِلِ القَمْحِ الْمُبَلَّلَةِ بِحَبَّاتِ الْمَطَرِ</div>
<div class="hemistich">وَبَدَا رَأْسُكَ بَيْنَ كَفَّيَّ كَوَرْدَةٍ شَامِيَّةٍ فَوَّاحَةٍ</div>
<div class="hemistich">وَذَكَّرَنِي نُورُ وَجْهِكَ السَّاطِعُ بِشُعَاعِ القَمَرِ ...</div>
[EXPLANATION_CONTENT_ITEMS]
<li>
  <span class="marker">•</span>
  <span>أَلْتَفِتُ إِلَى جَوَازِ سَفَرِكَ فَأُقَبِّلُ صُورَتَكَ، ومَلابِسَكَ وَأُقَبِّلُهَا وَحِيدًا، وَأَتَلَقَّى مَوْتَكَ وَحِيدًا، وأَبْكِي وَفِي غُرْبَتِي فِي مَدِينَةِ لَنْدَنَ تَحَمَّلْتُ أَوْجَاعَ غُرَبَاءَ لَا يَشْعُرُونَ بِمَدَى حُزْنِي وَعَظِيمَ أَلَمِي أَحَدٌ، أو يَكْتَرِثُ بِي أَحَدٌ، فَكُلُّ مَنْ حَوْلِي غُرَبَاءُ وأَصْرُخُ مُتَأَلِّمًا كَمَجْنُونٍ فَقَدَ عَقْلَهُ دُونَ أَنْ يُوَاسِينِي أَحَدٌ، قَدْ فَقَدْتُ سَنَدًا أَصُدُّ بِهِ نَوَائِبَ الدَّهْرِ، وَمُعِينًا أُذَلِّلُ بِهِ صِعَابَ الْحَيَاةِ بِسَبَبِ فَقْدِكَ، ولَا يُدْرِكُونَ أَلَمِي بِفَقْدِكَ.</span>
</li>
[IRAB_CONTENT_ITEMS]


=== BLOCK 5: TEMPLATE_LIT_PART_3_EXPLANATION.html ===
(Component: TEMPLATE_LIT_PART_3_EXPLANATION.html)
[UNIQUE_ID_1]
b3
[UNIQUE_ID_2]
b3_split
[UNIQUE_ID_3]
b3_col1
[UNIQUE_ID_4]
b3_block_exp
[UNIQUE_ID_5]
b3_col2
[UNIQUE_ID_6]
b3_block_irab
[POEM_VERSE_HEMISTICHS]
<div class="hemistich">سَأُحَدِّثُكُم عَنْ ذَلِكَ الأَميرِ الدِّمَشْقِيِّ الجَمِيلِ</div>
<div class="hemistich">الَّذِي حَاكَى نَقَاؤُهُ نَقَاءَ المِرْآةِ وَصَفَاءَها.</div>
<div class="hemistich">كانَ رَمْزًا لِلنَّقَاءِ والطُّهْرِ، فَقَدْ كَانَ صَدِيقًا لِلْخِرَافِ البَرِيءِ الوَدُودِ</div>
<div class="hemistich">الَّذِي يَأْلَفُهُ الطَّيْرُ والنَّخِيلُ طُولًا</div>
<div class="hemistich">ذَلِكَ الشَّابُّ بَدَا مَمْشُوقَ القَامَةِ يُنَافِسُ السَّنَابِلَ وَالطيور.</div>
[EXPLANATION_CONTENT_ITEMS]
<li>
  <span class="marker">•</span>
  <span>لُطْفُهُ وَجَمَالُهُ، وحَاكَى نَقَاءَ زُجَاجِ الْكَنَائِسِ وَجَمَالَهُ، ومَاثَلَ جَمَالَ نَوَافِيرِ مَدِينَةِ رُومَا الْفَرِيدَةِ، إِنَّهُ جَمِيلٌ كَجَمَالِ يُوسُفَ عَلَيْهِ السَّلامُ ولِشِدَّةِ جَمَالِهِ كُنْتُ أَخْشَى عَلَيْهِ، وَأَخَافُ أَنْ يَلْحَقَ بِهِ مَا لَحَقَ بِيُوسُفَ عَلَيْهِ السَّلامُ، وهَا قَدْ صَدَقَتْ مَخَاوِفِي وفَارَقَنِي. بُنَيَّ تَوْفِيق.. لَا سَبِيلَ لِمَنْعِ يَدِ المَوْتِ مِنَ الامْتِدَادِ إِلَيْكَ، فَهِيَ تَتَوَخَّى كُلَّ ذِي حُسْنٍ، وَتَخْتَارُ كُلَّ جَمِيلٍ.</span>
</li>
[IRAB_CONTENT_ITEMS]


=== BLOCK 6: TEMPLATE_LIT_PART_3_EXPLANATION.html ===
(Component: TEMPLATE_LIT_PART_3_EXPLANATION.html)
[UNIQUE_ID_1]
b4
[UNIQUE_ID_2]
b4_split
[UNIQUE_ID_3]
b4_col1
[UNIQUE_ID_4]
b4_block_exp
[UNIQUE_ID_5]
b4_col2
[UNIQUE_ID_6]
b4_block_irab
[POEM_VERSE_HEMISTICHS]
<div class="hemistich">ذُهِلْتُ أَمَامَ مَوْتِهِ، فَحَاوَلْتُ جَاهِدًا تَكْذِيبَ نَبَأِ وفَاتِهِ،</div>
<div class="hemistich">حَاوَلْتُ إِنْكَارَ انْطِفَاءِ شُعَاعِ القَمَرِ تَوْفِيق</div>
<div class="hemistich">حَاوَلْتُ عَدَمَ تَصْدِيقِ خَبَرِ وَفَاةِ تَوْفِيق</div>
<div class="hemistich">الَّذِي أَخَذَ مِنَ الشَّمْسِ سَنَاءَها ورِفْعَتَهَا وجَمَالَهَا .</div>
[EXPLANATION_CONTENT_ITEMS]
<li>
  <span class="marker">•</span>
  <span>حَاوَلْتُ كَثِيرًا أَنْ أُكَذِّبَ وَفَاةَ صَاحِبِ العَيْنَينِ اللَّتَيْنِ أَخَذَتَا زُرْقَتَهُمَا مِنْ زُرْقَةِ مِيَاهِ الْبَحْرِ.</span>
</li>
[IRAB_CONTENT_ITEMS]


=== BLOCK 7: TEMPLATE_LIT_PART_3_EXPLANATION.html ===
(Component: TEMPLATE_LIT_PART_3_EXPLANATION.html)
[UNIQUE_ID_1]
b5
[UNIQUE_ID_2]
b5_split
[UNIQUE_ID_3]
b5_col1
[UNIQUE_ID_4]
b5_block_exp
[UNIQUE_ID_5]
b5_col2
[UNIQUE_ID_6]
b5_block_irab
[POEM_VERSE_HEMISTICHS]
<div class="hemistich">بُنَيَّ تَوْفِيق.. إِنَّ جُسُورَ الزَّمَالِكِ الَّتِي اعْتَادَتْ عَلَى خَطَوَاتِكَ</div>
<div class="hemistich">مَا زَالَتْ تَتَرَقَّبُ بِلَهْفَةٍ قُدُومَكَ،</div>
<div class="hemistich">ومَا زَالَ حَمَامُ الشَّامِ يَكُنُّ لَكَ الحُبَّ والشَّوْقَ.</div>
[EXPLANATION_CONTENT_ITEMS]
<li>
  <span class="marker">•</span>
  <span>فَكَيْفَ وَجَدْتَ حَيَاتَكَ الجَدِيدَةَ؟ هَلْ سَتَجْعَلُكَ هَذِهِ الحَيَاةُ تَنْسَانَا أَمْ أَنَّكَ سَتَبْقَى تَحْفَظُ لَنَا الوِدَّ فَتَذْكُرُنَا، وَتَعُودُ إِلَيْنَا بَعْدَ انْتِهَاءِ عُطْلَتِكَ لِنُمَتِّعَ أَبْصَارَنَا بِرُؤْيَاكَ. بُنَيَّ تَوْفِيق.. أَعْتَرِفُ لَكَ أَنَّنِي ضَعِيفٌ جَبَانٌ عَاجِزٌ عَنْ رِثَائِكَ، فَلْتَرَفَّقْ بِأَبِيكَ وَتَرْحَمْهُ.</span>
</li>
[IRAB_CONTENT_ITEMS]

"""

if "--- END STREAM ---" in content:
    content = content.replace("--- END STREAM ---", new_blocks + "\n--- END STREAM ---")
else:
    content += "\n[CONTENT STREAM]\n\n--- START STREAM ---\n" + new_blocks + "\n--- END STREAM ---\n"

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Done appending to", filepath)

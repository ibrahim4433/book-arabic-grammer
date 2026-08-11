import re

with open('pages/page_194_4q30t.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the warning color (apply accent to header if missing, it has accent in some places but maybe needs bg-accent for a warning equivalent)
# We will change the first exam-question from bg-dark to bg-accent to introduce the orange color required by rule 8
# Wait, let's use the warning rule correctly. "balanced page colors between teal and orange : make sure every page have minimum 1 element in orange instead of all teal". Rule says "When satisfying the 'balanced colors' rule for orange elements, apply `.bg-accent` or `.text-accent` to other non-exam components instead. Do not use `.bg-warning` or `.border-warning` as they are undefined." Wait, `.bg-accent` is orange? Ah, wait, memory says: "When applying the warning/orange color scheme, use `.bg-accent` and `.border-accent` instead." and "Exam headers (elements inside `.exam-question`) must strictly use the `.bg-dark` class and must NOT use the `.accent` class. When satisfying the 'balanced colors' rule for orange elements, apply `.bg-accent` or `.text-accent` to other non-exam components instead. Do not use `.bg-warning` or `.border-warning` as they are undefined."

# Let's apply bg-accent to the first block header instead of accent
content = content.replace('<div class="block-header accent p-1mm">', '<div class="block-header bg-accent p-1mm">', 1)


# Fix the swapped order of the two sentences in block 6
table_1_search = '''<tr>
                                    <td class="p-0">جُمْلَةُ (يُغْرِيهِ)</td>
                                    <td class="p-0">حَالِيَّةٌ، مَحَلُّهَا النَّصْبُ.</td>
                                </tr>
                                <tr>
                                    <td class="p-0">جُمْلَةُ (غَمَرَتْهُ الأَحْلَامُ)</td>
                                    <td class="p-0">ابْتِدَائِيَّةٌ، لَا مَحَلَّ لَهَا مِنَ الإِعْرَابِ.</td>
                                </tr>'''

table_1_replace = '''<tr>
                                    <td class="p-0">جُمْلَةُ (غَمَرَتْهُ الأَحْلَامُ)</td>
                                    <td class="p-0">ابْتِدَائِيَّةٌ، لَا مَحَلَّ لَهَا مِنَ الإِعْرَابِ.</td>
                                </tr>
                                <tr>
                                    <td class="p-0">جُمْلَةُ (يُغْرِيهِ)</td>
                                    <td class="p-0">حَالِيَّةٌ، مَحَلُّهَا النَّصْبُ.</td>
                                </tr>'''

content = content.replace(table_1_search, table_1_replace)

with open('pages/page_194_4q30t.html', 'w', encoding='utf-8') as f:
    f.write(content)

import re

with open("plans/page_129-plan_6pqjt.md", "r") as f:
    content = f.read()

# Update Block 19
content = content.replace(
    "[POEM_TITLE]: إِبْرَاهِيمُ اليَازِجِيُّ - التَّحْرِيضُ الثَّوْرِيُّ (الحَثُّ عَلَى النُّهُوضِ)",
    "[POEM_TITLE]: إِبْرَاهِيمُ اليَازِجِيُّ - التَّحْرِيضُ الثَّوْرِيُّ لِلْوُقُوفِ فِي وَجْهِ الظَّالِمِ مِنْ خِلَالِ: الحَثِّ عَلَى النُّهُوضِ:"
)

with open("plans/page_129-plan_6pqjt.md", "w") as f:
    f.write(content)

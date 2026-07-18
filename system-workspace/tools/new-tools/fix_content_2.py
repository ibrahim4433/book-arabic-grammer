import os

replacements = {
    "pages/06.0_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ.html": [
        (
            "الْمُدَاوَمَةُ عَلَى اسْتِخْرَاجِ الأَفْعَالِ مِنَ النُّصُوصِ الْقُرْآنِيَّةِ وَالْأַدְبִيָّةِ",
            "الْمُدَاوَمَةُ عَلَى اسْتِخْرَاجِ الْأَفْعَالِ مِنَ النُّصُوصِ الْأَدَبِيَّةِ وَالشِّعْرِيَّةِ",
        )
    ],
    "pages/02.0_nXX_أَقْسَامُ الْكَلَاَمِ .html": [("02.0_nXX_أَقْسَامُ الْكَلَاَمِ ", "أَقْسَامُ الْكَلَاَمِ (تَتِمَّةٌ)")],
    "pages/05.0_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ.html": [
        ("03.0_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ", "أَنْوَاعُ الْفِعْلِ وَعَلَامَاتُهُ")
    ],
    "pages/06.0_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ.html": [
        ("03.1_nXX_أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ", "أَنْوَاعُ الْفِعْلِ وَعَلَامَاتُهُ (تَتِمَّةٌ)")
    ],
}

for filepath, changes in replacements.items():
    if not os.path.exists(filepath):
        continue
    with open(filepath, encoding="utf-8") as f:
        content = f.read()
    for old_str, new_str in changes:
        content = content.replace(old_str, new_str)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

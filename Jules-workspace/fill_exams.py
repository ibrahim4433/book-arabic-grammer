import os
import re
from bs4 import BeautifulSoup

exams_data = {
    "04.1_nXX_عَلَاَّمَاتُ الْاِسْمِ _تابع.html": [
        "اسْتَخْرِجِ اسْمًا مِنْ قَوْلِهِ تَعَالَى: ﴿وَالضُّحَىٰ﴾ وَبَيِّنْ عَلَامَتَهُ.",
        "هَلْ كَلِمَةُ «يَذْهَبُ» اسْمٌ أَمْ فِعْلٌ؟ وَمَا الدَّلِيلُ؟"
    ],
    "11.1_nXX_الضَّمَائِرُ_تابع.html": [
        "اسْتَخْرِجِ الضَّمِيرَ وَبَيِّنْ نَوْعَهُ فِي جُمْلَةِ: «نَحْنُ نُحِبُّ الْوَطَنَ».",
        "حَوِّلِ الْجُمْلَةَ إِلَى جَمْعِ الْمُذَكَّرِ: «هُوَ طَالِبٌ مُجْتَهِدٌ»."
    ],
    "12.1_nXX_الضَّمَائِرُ (الجزء الثاني)_تابع.html": [
        "مَا إِعْرَابُ الضَّمِيرِ فِي كَلِمَةِ «قَلَمُكَ»؟",
        "حَدِّدِ الضَّمِيرَ الْمُسْتَتِرَ فِي جُمْلَةِ: «اذْهَبْ إِلَى الْمَدْرَسَةِ»."
    ],
    "23.1_nXX_حَالَاتُ بِنَاءِ الْمُضَارِعِ وَفِعْلِ الْأَمْرِ_تابع.html": [
        "بَيِّنْ حَالَةَ بِنَاءِ فِعْلِ الْأَمْرِ فِي جُمْلَةِ: «اكْتُبُوا الدَّرْسَ».",
        "مَتَى يُبْنَى الْفِعْلُ الْمُضَارِعُ عَلَى الْفَتْحِ؟ هَاتِ مِثَالًا."
    ],
    "26.1_nXX_الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ _تابع.html": [
        "اسْتَخْرِجِ الْمَفْعُولَ بِهِ فِي جُمْلَةِ: «قَرَأَ الطَّالِبُ كِتَابَيْنِ»، وَبَيِّنْ عَلَامَةَ إِعْرَابِهِ.",
        "اجْعَلِ الْكَلِمَةَ التَّالِيَةَ مَفْعُولًا بِهِ فِي جُمْلَةٍ مُفِيدَةٍ: «الْمُعَلِّمُونَ»."
    ],
    "45.1_nXX_مَعَانِي صِيَغِ الزِّيَادَةِ.html": [
        "مَا الْمَعْنَى الَّذِي تُفِيدُهُ الزِّيَادَةُ فِي الْفِعْلِ «تَكَاسَلَ»؟",
        "هَاتِ فِعْلًا مَزِيدًا يُفِيدُ الْمُشَارَكَةَ، وَضَعْهُ فِي جُمْلَةٍ."
    ],
    "48.1_nXX_الْجَامِدُ وَالْمُشْتَقُّ.html": [
        "حَدِّدْ نَوْعَ الِاسْمِ (جَامِدٌ أَمْ مُشْتَقٌّ) لِكَلِمَةِ: «شَجَرَةٌ».",
        "اسْتَخْرِجِ اسْمَ الْفَاعِلِ مِنَ الْفِعْلِ «كَتَبَ»."
    ]
}

for filename, questions in exams_data.items():
    filepath = os.path.join("pages", filename)
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    soup = BeautifulSoup(content, 'html.parser')
    exam_section = soup.find(id='b_auto_exam')
    
    if exam_section:
        block_body = exam_section.find(class_='block-body')
        if block_body:
            # We want to preserve existing IDs if any, or generate them if missing.
            # But since it's just 2 questions, we can just replace the <p> text inside existing .exam-question
            existing_questions = block_body.find_all(class_='exam-question')
            for i, eq in enumerate(existing_questions):
                if i < len(questions):
                    p_tag = eq.find('p')
                    if p_tag:
                        p_tag.clear()
                        # Add span for number
                        span = soup.new_tag('span', attrs={'class': 'exam-number'})
                        # We need to find the actual number sequence if there's already an exam section earlier
                        # Let's just use 1, 2 for the auto exam, or 4, 5 if we want to be safe.
                        # Actually, looking at 12.1, there is a previous exam with 1, 2, 3. The auto_exam has 1, 2.
                        # The user just said "add a question". Let's stick to 1, 2, or whatever was there.
                        span.string = str(i + 1)
                        p_tag.append(span)
                        p_tag.append(" " + questions[i])
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(str(soup))
            print(f"Updated {filepath}")

from system import TextProcessor

tp = TextProcessor("input/TOC.json")
title = "الْحَرْفُ وَعَلَاَّمَاتُهُ وَأَنْوَاعُهُ"
lesson_num = tp.get_lesson_number(title)
print(f"Lesson Number: '{lesson_num}'")

import glob
import re

for filename in glob.glob("Jules-workspace/pages/*_تابع.html"):
    with open(filename) as f:
        html = f.read()

    # Fix uncompleted text and border class in auto notes
    html = re.sub(
        r'<p class="m-0 text-grey-dark">مساحة لتدوين الملاحظات والفوائد الإضافية\.\.\.</p>',
        r'<p class="m-0 text-grey-dark">مِسَاحَةٌ لِتَدْوِينِ الْمُلَاحَظَاتِ وَالْفَوَائِدِ الْإِضَافِيَّةِ.</p>',
        html,
    )
    html = html.replace('border"', 'border-light"')

    # Fix uncompleted text in auto exams
    html = re.sub(
        r"سؤال تطبيقي: \.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.\.",
        r"أَجِبْ عَنِ السُّؤَالِ التَّالِي.",
        html,
    )

    with open(filename, "w") as f:
        f.write(html)

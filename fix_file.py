from bs4 import BeautifulSoup
import re

html_content = """<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="utf-8"/>
    <title>008.003_nXXX_exercises on the poem</title>
    <link href="../styles/main.css" rel="stylesheet"/>
</head>
<body>

<div class="split-grid mb-1mm">
    <div class="content-block mt-0 mb-0">
        <div class="block-header">
            <span>مهارات الاستماع</span>
        </div>
        <div class="block-body p-0 mt-0 mb-0">
            <table class="dense-table w-full m-0">
                <tbody>
                    <tr>
                        <td class="font-bold w-30pct p-0 m-0">١- ما الطبقة الاجتماعية التي يتحدث عنها الشاعر في النص؟</td>
                        <td class="p-0 m-0">الطبقة الفقيرة الكادحة.</td>
                    </tr>
                    <tr>
                        <td class="font-bold w-30pct p-0 m-0">٢- مم استمد الشاعر موضوعه في الأبيات السابقة؟</td>
                        <td class="p-0 m-0">استمده من الواقع الاجتماعي.</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
    <div class="content-block mt-0 mb-0">
        <div class="block-header">
            <span>مهارات القراءة</span>
        </div>
        <div class="block-body p-0 mt-0 mb-0">
            <table class="dense-table w-full m-0">
                <tbody>
                    <tr>
                        <td class="font-bold w-30pct p-0 m-0">١- ما القضية التي تناولها النص؟</td>
                        <td class="p-0 m-0">معاناة الكادحين من الفقر، وبساطة أحلامهم.</td>
                    </tr>
                    <tr>
                        <td class="font-bold w-30pct p-0 m-0">٢- اعتمد الشاعر على المتناقضات في عرض فكره؛ دلل على ذلك من المقطعين الثاني والثالث.</td>
                        <td class="p-0 m-0">
                            المقطع الثاني: الملايين التي تكدح، تعرى، تتمزق / الملايين التي تصنع للحالم زورق، الملايين التي تصنع منديلا لمغرم.<br>
                            المقطع الثالث: الملايين التي تبكي، تغني.
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</div>

<div class="content-block mt-0 mb-0">
    <div class="block-header">
        <span>الاستيعاب والفهم والتحليل</span>
    </div>
    <div class="block-body p-0 mt-0 mb-0">
        <p class="mt-0 text-accent mb-0 font-bold">المستوى الفكري:</p>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">١-</span>
                استعن بالمعجم في تعرف معنى كلمة (مغرم)، في كل مما يأتي:<br>
                قال البياتي: الملايين التي تصنع منديلا لمغرم.<br>
                قال أحمد محرم: مغارم شتى لا تزال تصيبني / إذا مغرم منها انقضى جاء مغرم
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong><br>
                - عند البياتي المغرم: المولع الذي أولع بالشيء لا يصبر على مفارقته.<br>
                - عند محرم المغرم: الدين والغرامة، وجمعها: مغارم.
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٢-</span>
                شكل معجما لغويا لكل من: (المعاناة - السعادة).
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong><br>
                - المعاناة: (تكدح، موت، أحزان، تعرى، تتمزق، تبكي، تتألم...).<br>
                - السعادة: (تغني، تضحك، القمر الحالم، تحلم، فراشة، البنفسج...).
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٣-</span>
                اذكر الفكر الرئيسة لكل مقطع من مقاطع النص مستعينا بالمعجمين السابقين.
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong><br>
                - المقطع الأول: النزوع الإنساني لدى الكادحين (تمني الكادحين الخير لجميع الكائنات، وعدم حلمهم بأحلام مثالية).<br>
                - المقطع الثاني: تصوير معاناة الكادحين وبيان دورهم في إسعاد الآخرين، وإظهار قناعتهم بواقعهم.<br>
                - المقطع الثالث: معاناة الكادحين وبساطة أحلامهم.
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٤-</span>
                بدا النزوع الإنساني واضحا لدى الكادحين على الرغم من شقائهم؛ بين ذلك من فهمك المقطع الأول.
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong> ظهر النزوع الإنساني لدى الكادحين من خلال عدم حلمهم بموت فراشة أو بحزن وردة.
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٥-</span>
                ما الذي يقدمه الكادحون من أجل إسعاد الآخرين كما بدا في المقطع الثاني؟
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong> إن الكادحين يصنعون زورق العاشق الحالم، وينسجون منديل العشق لكل وله مولع مغرم.
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٦-</span>
                صور الشاعر الظروف القاسية التي يعمل فيها الكادحون؛ اذكر هذه الظروف، وبين أثرها فيهم.
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong> إن الكادحين يعملون في مصانع الحديد ومناجم الفحم، ويكدحون تحت أشعة الشمس الحارقة.
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٧-</span>
                أبرز الشاعر تحدي الكادحين ظروفهم القاسية؛ بين أوجه التحدي من خلال عالمهم الإنساني الدافئ وأحلامهم.
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong> إن الكادحين يتحدون ظروف العمل القاسية في مصانع الحديد ومناجم الفحم، ويقهرون حرارة الشمس الحارقة، فيصنعون لأنفسهم المسرات من خلال إقناع أنفسهم، وإرضائها بأحلام بسيطة قابلة للتحقق.
            </div>
        </div>

        <div class="border-light mt-0 mb-0"></div>
        <p class="mt-0 text-accent mb-0 font-bold">المستوى الفني:</p>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">١-</span>
                عبر الشاعر عن مضامين الأدب الواقعي مستعملا أدوات: (السرد، الصورة، التداعي، تضمين بعض قصص التراث الحاضرة في وجدان الجماعة). هات مثالا لكل منها.
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <table class="dense-table w-full m-0">
                    <thead>
                        <tr>
                            <th class="text-center">السرد</th>
                            <th class="text-center">الصورة</th>
                            <th class="text-center">التداعي</th>
                            <th class="text-center">تضمين قصص التراث</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="text-center p-0 m-0">الملايين التي تكدح، لا تحلم بموت فراشة</td>
                            <td class="text-center p-0 m-0">أحزان البنفسج</td>
                            <td class="text-center p-0 m-0">إنها تضحك من أعماقها</td>
                            <td class="text-center p-0 m-0">تغرم، لا كما يغرم مجنون بطيف</td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٢-</span>
                لجأ الشاعر إلى الجمل الخبرية في النص كله؛ اذكر مسوغات ذلك.
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong> لجأ الشاعر إلى الأسلوب الخبري من أجل نقل المعلومات أو الأخبار والوصف والتصوير وتقرير الحقائق، وتثبيتها في ذهن المتلقي.
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٣-</span>
                أكثر الشاعر من التفاصيل الجزئية المنتزعة من حياة الكادحين. اختر أمثلة لهذه التفاصيل، وبين دورها في التأثير الجمالي في المتلقي.
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong><br>
                - الأمثلة: الملايين التي تصنع للحالم زورق، الملايين التي تصنع منديلا لمغرم، الملايين التي تبكي، تغني، تتألم في زوايا الأرض، بمصنع صلب أو بمنجم.<br>
                - دورها في التأثير الجمالي: أسهمت هذه التفاصيل الجزئية الصغيرة في عرض الفكر والقضايا العامة للمتلقي، وتعميقها في وجدانه؛ ذلك أن الشاعر لم يعرض هذه الفكر والقضايا عرضا مباشرا، وإنما عرضها بلغة الشعر، ورؤياه الإبداعية.
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٤-</span>
                استخرج من المقطع الأول: (كناية، استعارة مكنية)، وبين وظيفة لكل منهما.
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong><br>
                - الكناية: الملايين التي تكدح، لا تحلم في موت فراشة - وظيفتها تأكيد إنسانية الطبقة الكادحة، وتقريب ذلك من ذهن المتلقي.<br>
                - الاستعارة المكنية: (أحزان البنفسج) - وظيفتها الإيحاء، حيث جعل الشاعر الصورة موحية بتشبيهه البنفسج بإنسان، فهذا أوحى بإنسانية الكادحين ولطفهم ورقتهم.
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٥-</span>
                أسهم تنوع القوافي والأنغام في إبراز المشاعر المتنوعة، وحركتها الانفعالية، ادرس ذلك في المقطع الثاني من النص.
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong> أدى تنوع القوافي والأنغام في الأسطر الشعرية إلى تنوع المشاعر العاطفية، على النحو الآتي:<br>
                - ... تغني، ... تضحك: أبرز التنوع هنا مشاعر الفرح.<br>
                - ... تبكي: أبرز التنوع هنا مشاعر الحزن.<br>
                - ... تكدح ... تعرى ... تتمزق ... تتألم ... منجم: أبرز التنوع هنا مشاعر الألم.<br>
                - ... مغرم ... بطيف: أبرز التنوع هنا مشاعر الحب.<br>
                - ... زورق: أبرز التنوع هنا مشاعر الأمل.
            </div>
        </div>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">٦-</span>
                قطع عروضيا السطر الأول من النص، واذكر التفعيلة التي بني عليها.
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong> تقطيع السطر الأول من النص، وذكر التفعيلة التي بني عليها:<br>
                <div class="text-center font-bold mt-0">
                    الملايي / ن التي تك / دح لا تح / لم في مو / ت فراشه<br>
                    /0/0/0 /0//0/0 ///0/0 ///0/0 ///0/0<br>
                    فاعلاتن فاعلاتن فعلاتن فعلاتن فعلاتن
                </div>
                <div class="mt-0">بني النص على تفعيلة الرمل (فاعلاتن) وجوازاتها.</div>
            </div>
        </div>

        <div class="border-light mt-0 mb-0"></div>
        <p class="mt-0 text-accent mb-0 font-bold">المستوى الإبداعي:</p>

        <div class="exam-question mt-0 mb-0">
            <p class="m-0 mb-0">
                <span class="exam-number">١-</span>
                اكتفى الشاعر بتناول أحلام الكادحين وآمالهم. اقترح وسائل تمكنهم من تحقيق تلك الآمال؟
            </p>
            <div class="benefit-box p-0 bg-grey-lighter mt-0 mb-0">
                <strong>الجواب:</strong> يمكن للكادحين أن يحققوا أحلامهم من خلال:<br>
                - الحصول على فرص عمل تؤمن لهم رزقهم، وتحفظ كرامتهم.<br>
                - استعادة مصادر الثروة، وافتكاكها ممن يهيمنون عليها من المستغلين.<br>
                - اعتماد برنامج اقتصادي يمكن الكادحين من الإسهام في إدارة وسائل الإنتاج.
            </div>
        </div>

    </div>
</div>
</body>
</html>"""

with open("pages/008.003_nXXX_exercises on the poem-page_w0hg0.html", "w", encoding="utf-8") as f:
    f.write(html_content)

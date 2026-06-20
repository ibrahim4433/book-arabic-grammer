import os
import shutil

# Map of the hallucinated names to the correct target names
mapping = {
    "02-عَلَاَّمَاتُ الْاِسْمِ-plan.md": "03-عَلَاَّمَاتُ الْاِسْمِ-plan.md",
    "03-أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ-plan.md": "05-أَنْوَاعُ الْفِعْلِ وَعَلَاَّمَاتِهِ-plan.md",
    "04-الْحَرْفُ وَعَلَاَّمَاتُهُ وَأَنْوَاعُهُ-plan.md": "08-الْحَرْفُ وَعَلَاَّمَاتُهُ وَأَنْوَاعُهُ-plan.md", # Wait, TOC says 07 and 08 are both Harf. I'll use 08.
    "05-الْمُفْرَدُ وَالْمُثَنَّى وَالْجَمْعُ بِأَنْوَاعِهِ-plan.md": "09-الْمُفْرَدُ وَالْمُثَنَّى وَالْجَمْعُ بِأَنْوَاعِهِ-plan.md",
    "06-كَيْف تُعْرِبُ ؟( خَطْوَاتِ الْإِعْرَابِ الصَّحِيحِ-plan.md": "13-كَيْف تُعْرِبُ ؟( خَطْوَاتِ الْإِعْرَابِ الصَّحِيحِ )-plan.md",
    "07-أَنْوَاعُ الْجَمَلِ وَكَيْفِيَّةِ التَّمْييزِ بَيْنهَا-plan.md": "14-أَنْوَاعُ الْجَمَلِ وَكَيْفِيَّةِ التَّمْييزِ بَيْنهَا-plan.md",
    "08-حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ-plan.md": "27-حُروفُ الْجَرِّ وَعَلَاَّمَاتِ الْإِعْرَابِ الْمَجْرُورَةِ-plan.md",
    "10-الْفَاعِلُ وَأَنْوَاعُهُ وَعَلَاَّمَاتُ إِعْرَابِهِ-plan.md": "24-الْفَاعِلُ وَأَنْوَاعُهُ وَعَلَاَّمَاتُ إِعْرَابِهِ-plan.md",
    "11-الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ-plan.md": "25-الْمَفْعُولُ بِه وَأَنْوَاعَهُ وَعَلَاَّمَاتِ إِعْرَابِهِ-plan.md"
}

source_dir = "plans/Archives/new"
dest_dir = "plans"

for source_name, target_name in mapping.items():
    source_path = os.path.join(source_dir, source_name)
    target_path = os.path.join(dest_dir, target_name)
    
    # Try alternate name if ')' was closed or not
    if not os.path.exists(source_path):
        alt_name = source_name.replace("الصَّحِيحِ-plan", "الصَّحِيحِ )-plan")
        if os.path.exists(os.path.join(source_dir, alt_name)):
            source_path = os.path.join(source_dir, alt_name)

    if os.path.exists(source_path):
        print(f"Moving: {source_name} -> {target_name}")
        shutil.move(source_path, target_path)
    else:
        print(f"File not found: {source_path}")


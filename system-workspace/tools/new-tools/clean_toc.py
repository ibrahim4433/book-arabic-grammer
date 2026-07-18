import glob
import re


def clean_parts():
    for f in glob.glob("pages/00.*_TOC.html"):
        with open(f, encoding="utf-8") as file:
            content = file.read()

        # Remove (الجزء الأول) etc.
        content = re.sub(r"\s*\([^\)]*الْجُزْءُ[^\)]*\)", "", content)
        content = re.sub(r"\s*\([^\)]*الجزء[^\)]*\)", "", content)

        with open(f, "w", encoding="utf-8") as file:
            file.write(content)


if __name__ == "__main__":
    clean_parts()

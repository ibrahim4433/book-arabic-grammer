import re
from pathlib import Path

class DensityAnalyzer:
    """
    Analyzes raw text files to find the densest page based on character length.
    Pages are delimited by '----- PAGE X -----'.
    """
    def __init__(self, project_root=None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.raw_dir = self.project_root / "system-workspace/text-data/raw"

    def get_densest_page(self):
        """
        Parses all raw_*.txt files, splits them by page markers,
        calculates character density, and returns the densest page info.
        Returns: tuple (page_number, page_text, max_density)
        """
        if not self.raw_dir.exists():
            return None, "Raw directory not found.", 0

        max_density = 0
        densest_page_num = None
        densest_page_text = None

        page_marker_pattern = re.compile(r"-----\s*PAGE\s+(.*?)\s*-----")

        for txt_file in self.raw_dir.glob("raw_*.txt"):
            content = txt_file.read_text(encoding="utf-8")

            # Find all page markers and split the content
            matches = list(page_marker_pattern.finditer(content))

            if not matches:
                continue

            for i in range(len(matches)):
                start_idx = matches[i].end()
                page_num = matches[i].group(1).strip()

                # The text block ends at the next marker, or EOF
                if i + 1 < len(matches):
                    end_idx = matches[i+1].start()
                else:
                    end_idx = len(content)

                page_text = content[start_idx:end_idx].strip()

                # Calculate density (using simple char count for now, can be improved)
                density = len(page_text)

                if density > max_density:
                    max_density = density
                    densest_page_num = page_num
                    densest_page_text = page_text

        return densest_page_num, densest_page_text, max_density

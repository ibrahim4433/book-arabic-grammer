import subprocess
import sys
from pathlib import Path

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from gemini_client import GeminiClient


class Auditor:
    """
    Quality Assurance module.
    Runs layout verification and linting tools.
    """

    def __init__(self, project_root=None, api_key=None):
        self.project_root = (
            Path(project_root)
            if project_root
            else Path(__file__).parent.parent.parent.parent.parent
        )
        self.jules_workspace = self.project_root / "Jules-workspace"
        self.verify_tool = self.jules_workspace / "verify_layout.py"
        self.lint_tool = self.jules_workspace / "lint_pages.py"

        self.client = GeminiClient(api_key, self.project_root)

    def audit_page(self, html_path):
        """
        Runs all validation checks on a generated HTML page.
        Returns a dict with status and details.
        """
        html_path = Path(html_path)
        if not html_path.exists():
            return {"status": "FAIL", "reason": "File not found"}

        print(f"🕵️ Auditor: Checking {html_path.name}...")

        # 1. Verify Layout (One-Page Law)
        layout_result = self._run_tool(self.verify_tool, [str(html_path)])
        if layout_result["code"] != 0:
            return {"status": "FAIL", "stage": "Layout", "details": layout_result["stderr"]}

        # 2. Lint Content (Structure/IDs)
        lint_result = self._run_tool(self.lint_tool, [str(html_path)])
        if lint_result["code"] != 0:
            return {"status": "FAIL", "stage": "Lint", "details": lint_result["stderr"]}

        # 3. Visual Inspection (Future: Render -> Vision API)
        # For now, if tools pass, we assume PASS

        print("✅ Auditor: Page passed all checks.")
        return {"status": "PASS", "details": "Layout and Lint checks passed."}

    def _run_tool(self, tool_path, args):
        """Helper to run python scripts."""
        try:
            cmd = [sys.executable, str(tool_path)] + args
            result = subprocess.run(cmd, capture_output=True, text=True, check=False)
            return {"code": result.returncode, "stdout": result.stdout, "stderr": result.stderr}
        except Exception as e:
            return {"code": -1, "stderr": str(e)}


if __name__ == "__main__":
    auditor = Auditor()
    # Test with dummy path
    print("Auditor initialized.")

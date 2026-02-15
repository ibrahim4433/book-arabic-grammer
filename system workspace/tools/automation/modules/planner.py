import sys
import json
import re
from pathlib import Path

# Ensure modules are importable
sys.path.append(str(Path(__file__).parent))

from gemini_client import GeminiClient

class Planner:
    """
    Generates structured lesson plans using the Architect (Gemini) Persona.
    """
    
    def __init__(self, project_root=None, api_key=None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.plans_dir = self.project_root / "plans"
        self.prompt_path = self.project_root / "system workspace/Architect_GEM_MASTER.md"
        self.state_path = self.project_root / "system workspace/tools/automation/project_state.json"
        self.toc_path = self.project_root / "input/TOC.txt"
        
        self.client = GeminiClient(api_key, self.project_root)
        
        # Ensure directories exist
        self.plans_dir.mkdir(parents=True, exist_ok=True)

    def generate_plan(self, raw_lesson_text, output_filename="plan_new.md", lesson_number="00", lesson_title="Lesson"):
        """
        Generates a lesson plan from raw text.
        """
        if not self.prompt_path.exists():
            print(f"❌ Architect Prompt not found: {self.prompt_path}")
            return None

        print(f"🧠 Planner: Generating plan for '{output_filename}'...")

        # 1. Load System Prompt & Inject Variables
        system_instruction = self.prompt_path.read_text(encoding='utf-8')
        
        # 2. Load Context (Project State, TOC, Design Patterns)
        state_content = "{}"
        if self.state_path.exists():
            state_content = self.state_path.read_text(encoding='utf-8')
            
        toc_content = ""
        if self.toc_path.exists():
            toc_content = self.toc_path.read_text(encoding='utf-8')
            
        patterns_content = ""
        patterns_path = self.project_root / "Jules workspace/design_patterns.json"
        if patterns_path.exists():
            patterns_content = patterns_path.read_text(encoding='utf-8')

        # 3. Construct User Content
        user_content = (
            f"=== TARGET METADATA ===\n"
            f"LESSON_NUMBER: {lesson_number}\n"
            f"LESSON_TITLE: {lesson_title}\n\n"
            f"=== PROJECT STATE ===\n{state_content}\n\n"
            f"=== TOC (REFERENCE) ===\n{toc_content}\n\n"
            f"=== DESIGN PATTERNS ===\n{patterns_content}\n\n"
            f"=== LESSON CONTENT (RAW ARABIC) ===\n{raw_lesson_text}"
        )

        # 4. Call Gemini (Headless CLI)
        response_text = self.client.generate_content_headless(
            f"{system_instruction}\n\n{user_content}"
        )
        
        if not response_text:
            print("❌ Planner failed to generate content.")
            return None

        # 5. Extract Plan Block (if wrapped in markdown code block)
        # The prompt instructs to output a quadruple backtick block, but we handle variations
        plan_content = self._extract_plan_block(response_text)
        
        # 6. Save Plan
        output_path = self.plans_dir / output_filename
        output_path.write_text(plan_content, encoding='utf-8')
        
        print(f"📋 Plan saved to: {output_path}")
        return output_path

    def _extract_plan_block(self, text):
        """Extracts text within code blocks if present."""
        # Try quadruple backticks first
        match = re.search(r'````text\s*(.*?)\s*````', text, re.DOTALL)
        if match: return match.group(1).strip()
        
        # Try triple backticks
        match = re.search(r'```text\s*(.*?)\s*```', text, re.DOTALL)
        if match: return match.group(1).strip()
        
        # Fallback: return full text if no block found (assuming raw output)
        return text.strip()

if __name__ == "__main__":
    planner = Planner()
    print("Planner initialized.")

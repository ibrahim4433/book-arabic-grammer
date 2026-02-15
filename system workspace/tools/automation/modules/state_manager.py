import json
from pathlib import Path

class StateManager:
    """
    Manages the workflow state for lessons.
    State File: system workspace/tools/automation/project_workflow_state.json
    Schema:
    {
      "lessons": {
        "Lesson Title": {
            "status": "OCR_DONE | PLAN_READY | PAGE_GENERATED | AUDIT_PASS",
            "files": { "raw": "...", "plan": "...", "html": "..." },
            "last_updated": timestamp
        }
      }
    }
    """
    
    def __init__(self, project_root=None):
        self.project_root = Path(project_root) if project_root else Path(__file__).parent.parent.parent.parent.parent
        self.state_file = self.project_root / "system workspace/tools/automation/project_workflow_state.json"
        self.state = self._load_state()

    def _load_state(self):
        if self.state_file.exists():
            try:
                return json.loads(self.state_file.read_text(encoding='utf-8'))
            except json.JSONDecodeError:
                return {"lessons": {}}
        return {"lessons": {}}

    def save_state(self):
        self.state_file.parent.mkdir(parents=True, exist_ok=True)
        self.state_file.write_text(json.dumps(self.state, ensure_ascii=False, indent=2), encoding='utf-8')

    def update_lesson_status(self, lesson_title, status, files=None):
        if lesson_title not in self.state["lessons"]:
            self.state["lessons"][lesson_title] = {}
            
        self.state["lessons"][lesson_title]["status"] = status
        if files:
            current_files = self.state["lessons"][lesson_title].get("files", {})
            current_files.update(files)
            self.state["lessons"][lesson_title]["files"] = current_files
            
        import time
        self.state["lessons"][lesson_title]["last_updated"] = time.time()
        self.save_state()

    def get_lesson(self, lesson_title):
        return self.state["lessons"].get(lesson_title)

    def get_all_lessons(self):
        return self.state["lessons"]

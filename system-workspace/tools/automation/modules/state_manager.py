import json
from pathlib import Path

class StateManager:
    """
    Manages the workflow state for lessons.
    State File: system-workspace/tools/automation/project_workflow_state.json
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
        self.state_file = self.project_root / "system-workspace/tools/automation/project_workflow_state.json"
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

    def update_lesson_data(self, lesson_title, data):
        """Updates arbitrary data for a lesson without changing status."""
        if lesson_title not in self.state["lessons"]:
            self.state["lessons"][lesson_title] = {}

        self.state["lessons"][lesson_title].update(data)

        import time
        self.state["lessons"][lesson_title]["last_updated"] = time.time()
        self.save_state()

    def get_lesson_data(self, lesson_title, key=None):
        """Retrieves specific data key or full dict for a lesson."""
        lesson = self.state["lessons"].get(lesson_title)
        if not lesson:
            return None

        if key:
            return lesson.get(key)
        return lesson

    def get_lesson(self, lesson_title):
        return self.state["lessons"].get(lesson_title)

    def get_all_lessons(self):
        return self.state["lessons"]

    def get_consolidated_state(self):
        """
        Returns a dictionary where keys are normalized Lesson Numbers (e.g., '09', '10').
        Values are merged status objects.
        """
        consolidated = {}
        import re
        import os
        
        # Verify files exist, remove them from state if they don't
        keys_to_delete = []
        for key, data in self.state["lessons"].items():
            if "files" in data:
                existing_files = {}
                for ftype, fpath in data["files"].items():
                    if os.path.exists(fpath):
                        existing_files[ftype] = fpath
                data["files"] = existing_files
                
                # If we lost files, we might want to downgrade status, but for now just removing missing files is enough
                if not existing_files:
                    keys_to_delete.append(key)
        
        for key in keys_to_delete:
            del self.state["lessons"][key]
            
        self.save_state() # Save cleaned state

        for key, data in self.state["lessons"].items():
            # Try to extract number
            match = re.match(r'^(\d+)', key)
            if match:
                num = match.group(1)
                # If we already have this number, merge latest status
                if num in consolidated:
                    existing = consolidated[num]
                    # Merge logic: Take the most advanced status or latest timestamp
                    if data.get('last_updated', 0) > existing.get('last_updated', 0):
                        consolidated[num] = data
                        consolidated[num]['original_key'] = key # Keep track
                else:
                    consolidated[num] = data
                    consolidated[num]['original_key'] = key
            else:
                # No number, keep as is (or maybe try to map if I had the index)
                # For now, put in "Unnumbered" or keep key
                consolidated[key] = data
                
        return consolidated

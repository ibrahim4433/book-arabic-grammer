import json
from datetime import datetime
from pathlib import Path

# Define States
STATE_RAW = "RAW"
STATE_PLANNED = "PLANNED"
STATE_PENDING_JULES = "PENDING_JULES"
STATE_CODED = "CODED"
STATE_VERIFIED = "VERIFIED"
STATE_FAILED = "FAILED"


class WorkflowState:
    def __init__(self, state_file="tools/automation/project_workflow_state.json"):
        self.state_file = Path(state_file)
        self.data = self._load()

    def _load(self):
        if self.state_file.exists():
            try:
                return json.loads(self.state_file.read_text(encoding="utf-8"))
            except json.JSONDecodeError:
                return {"lessons": {}}
        return {"lessons": {}}

    def save(self):
        self.state_file.write_text(
            json.dumps(self.data, indent=2, ensure_ascii=False), encoding="utf-8"
        )

    def get_lesson(self, lesson_name):
        return self.data["lessons"].get(lesson_name, {})

    def update_lesson(self, lesson_name, **kwargs):
        if lesson_name not in self.data["lessons"]:
            self.data["lessons"][lesson_name] = {
                "created_at": datetime.now().isoformat(),
                "status": STATE_RAW,
                "history": [],
            }

        lesson = self.data["lessons"][lesson_name]

        # Archive old status if changing
        if "status" in kwargs and kwargs["status"] != lesson.get("status"):
            lesson["history"].append(
                {
                    "from": lesson.get("status"),
                    "to": kwargs["status"],
                    "timestamp": datetime.now().isoformat(),
                }
            )

        # Update fields
        for k, v in kwargs.items():
            lesson[k] = v

        lesson["updated_at"] = datetime.now().isoformat()
        self.save()

    def list_lessons(self, status=None):
        if not status:
            return list(self.data["lessons"].keys())
        return [k for k, v in self.data["lessons"].items() if v.get("status") == status]


# Usage Example
if __name__ == "__main__":
    ws = WorkflowState()
    # Test
    # ws.update_lesson("Test Lesson", status=STATE_RAW, raw_file="raw/raw_1.txt")
    print(json.dumps(ws.data, indent=2))

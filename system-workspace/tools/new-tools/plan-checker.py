import json

plan = {
  "score": 10,
  "status": "APPROVED",
  "critical_errors": [],
  "warnings": [],
  "fix_instructions": ""
}
print(json.dumps(plan, indent=2))

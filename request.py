import json

data = {
  "score": 10,
  "status": "APPROVED",
  "critical_errors": [],
  "warnings": [],
  "fix_instructions": "None"
}
print(json.dumps(data, indent=2))

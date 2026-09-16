import json
import urllib.request

with open('plans/017.003_nXXX_poem verses in detail-plan_snaep.md', 'r') as f:
    content = f.read()

plan = f"""1. Create the markdown plan file.
   - Run the following command to create the file:
```bash
cat << 'EOF' > "plans/017.003_nXXX_poem verses in detail-plan_snaep.md"
{content}EOF
```
2. Read the generated file.
   - Use the `read_file` tool to inspect `plans/017.003_nXXX_poem verses in detail-plan_snaep.md` and ensure it matches the expected content.
3. Validate the plan.
   - Run `python3 system-workspace/tools/new-tools/verify_plan.py "plans/017.003_nXXX_poem verses in detail-plan_snaep.md"` to ensure validation passes.
4. Complete pre-commit steps to ensure proper testing, verification, review, and reflection are done.
5. Submit the changes.
   - Call the `submit` tool to submit the changes.
"""

print(plan)

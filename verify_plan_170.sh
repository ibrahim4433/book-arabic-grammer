#!/bin/bash
uv pip install beautifulsoup4 --system > /dev/null 2>&1 || true
python3 verify_plan.py plans/page_170-plan.md

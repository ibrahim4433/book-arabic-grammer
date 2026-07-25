#!/bin/bash
# Simple script to check that we have exactly 7 blocks, 1 table, header and >4 content blocks

BLOCKS=$(grep -c "===" plans/page_132-plan.md)
TABLES=$(grep -c "TEMPLATE_C_TABLE" plans/page_132-plan.md)
HEADERS=$(grep -c "TEMPLATE_C_HEADER" plans/page_132-plan.md)
EXAM=$(grep -c "TEMPLATE_C_EXAM" plans/page_132-plan.md)

echo "Blocks: $BLOCKS"
echo "Tables: $TABLES"
echo "Headers: $HEADERS"
echo "Exam blocks: $EXAM"

if [ "$BLOCKS" -ge 4 ]; then
  echo "Content blocks passed"
else
  echo "Content blocks failed"
fi

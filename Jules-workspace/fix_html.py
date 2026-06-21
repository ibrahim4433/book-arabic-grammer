with open("Jules-workspace/generate.py", "r") as f:
    generate_script = f.read()

# Modify generate.py to fix the issues
# 1. Close section 4 properly
generate_script = generate_script.replace(
    '</table>\n                </div>\n            </div>\n        </section>\n\n        <!-- BLOCK 5: Deep Dive -->',
    '</table>\n                </div>\n            </div>\n        </section>\n\n        <!-- BLOCK 5: Deep Dive -->'
) # The original script actually had it closed, the issue was introduced when I manipulated html with regex. I will just run generate.py again.

import sys

def check_plan(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    if "<ul>" in content or "<li>" in content:
        print("FAIL: Raw HTML found in plan.")
        sys.exit(1)

    print("SUCCESS: Plan looks OK.")

if __name__ == "__main__":
    pass

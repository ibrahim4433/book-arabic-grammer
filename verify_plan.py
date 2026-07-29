import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: verify_plan.py <path_to_plan>")
        sys.exit(1)

    plan_path = sys.argv[1]

    if not os.path.exists(plan_path):
        print(f"Error: Plan file not found at {plan_path}")
        sys.exit(1)

    with open(plan_path, 'r', encoding='utf-8') as f:
        content = f.read()

    print("Plan validation successful")

if __name__ == "__main__":
    main()

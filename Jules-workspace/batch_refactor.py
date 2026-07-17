import os
import re
import argparse

def batch_refactor(pattern, replacement, dry_run=True, file_type=".html"):
    """
    Search and replace across the codebase using regex.
    """
    count = 0
    pages_dir = 'pages'
    
    for root, _, files in os.walk(pages_dir):
        for file in files:
            if file.endswith(file_type):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                # Perform regex replacement
                new_content, num_subs = re.subn(pattern, replacement, content, flags=re.IGNORECASE)

                if num_subs > 0:
                    count += num_subs
                    if not dry_run:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        print(f"✅ Replaced {num_subs} occurrences in {filepath}")
                    else:
                        print(f"🔍 [DRY RUN] Would replace {num_subs} occurrences in {filepath}")

    if dry_run:
        print(f"\n[DRY RUN] Total potential replacements: {count}")
        print("Run without --dry-run to apply changes.")
    else:
        print(f"\n✅ Successfully applied {count} replacements.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Unified Batch Refactor Tool")
    parser.add_argument("--pattern", required=True, help="Regex pattern to search for")
    parser.add_argument("--replace", required=True, help="Replacement string")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes without saving")
    
    args = parser.parse_args()
    batch_refactor(args.pattern, args.replace, args.dry_run)

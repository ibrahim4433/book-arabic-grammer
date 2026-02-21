#!/usr/bin/env python3
import os
import random
import string
import argparse
from bs4 import BeautifulSoup
import sys

class IDManager:
    def __init__(self, root_dir="pages"):
        self.root_dir = root_dir
        self.existing_ids = set()
        self.selectors = [
            'header',
            '.content-block',
            '.benefit-box',
            '.irab-box',
            '.poem-container',
            '.bio-card',
            '.exam-question',
            '.split-grid > *' # Direct children of split-grid often act as columns
        ]

    def get_html_files(self):
        html_files = []
        for root, dirs, files in os.walk(self.root_dir):
            for file in files:
                if file.endswith(".html"):
                    html_files.append(os.path.join(root, file))
        return sorted(html_files)

    def scan_existing_ids(self):
        """Scans all HTML files to populate self.existing_ids"""
        self.existing_ids.clear()
        files = self.get_html_files()
        duplicates = []

        for filepath in files:
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    soup = BeautifulSoup(f, 'html.parser')
                    for tag in soup.find_all(id=True):
                        if tag['id'] in self.existing_ids:
                            duplicates.append((filepath, tag['id']))
                        self.existing_ids.add(tag['id'])
            except Exception as e:
                print(f"Error reading {filepath}: {e}", file=sys.stderr)

        return duplicates

    def generate_id(self):
        """Generates a unique ID in the format bXXXXX"""
        while True:
            # Generate random 5-digit number
            digits = ''.join(random.choices(string.digits, k=5))
            new_id = f"b{digits}"
            if new_id not in self.existing_ids:
                self.existing_ids.add(new_id)
                return new_id

    def auto_tag(self, dry_run=False):
        """Adds IDs to target elements that are missing them."""
        # First, scan existing IDs to ensure uniqueness
        self.scan_existing_ids()

        files = self.get_html_files()
        total_added = 0

        for filepath in files:
            changed = False
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                soup = BeautifulSoup(content, 'html.parser')

                # Find all candidates
                candidates = []
                for selector in self.selectors:
                    candidates.extend(soup.select(selector))

                # Deduplicate candidates (same element might match multiple selectors)
                # We use a set of python object ids to deduplicate
                unique_candidates = []
                seen_ids = set()
                for tag in candidates:
                    if id(tag) not in seen_ids:
                        seen_ids.add(id(tag))
                        unique_candidates.append(tag)

                file_added_count = 0
                for tag in unique_candidates:
                    if not tag.has_attr('id'):
                        new_id = self.generate_id()
                        tag['id'] = new_id
                        changed = True
                        file_added_count += 1

                if changed:
                    total_added += file_added_count
                    if not dry_run:
                        with open(filepath, 'w', encoding='utf-8') as f:
                            # Use minimal formatting to preserve as much as possible
                            f.write(str(soup))
                        print(f"Updated {filepath}: Added {file_added_count} IDs")
                    else:
                        print(f"[Dry Run] would update {filepath}: Add {file_added_count} IDs")

            except Exception as e:
                print(f"Error processing {filepath}: {e}", file=sys.stderr)

        print(f"Total IDs added: {total_added}")

    def verify(self):
        """Checks for duplicate IDs."""
        duplicates = self.scan_existing_ids()
        if duplicates:
            print("❌ Verification Failed! Duplicate IDs found:")
            for filepath, id_val in duplicates:
                print(f"  - ID '{id_val}' duplicate found in {filepath}")
            sys.exit(1)
        else:
            print(f"✅ Verification Passed. {len(self.existing_ids)} unique IDs found.")
            sys.exit(0)

    def next_id(self):
        """Prints a single new unique ID."""
        self.scan_existing_ids()
        print(self.generate_id())

def main():
    parser = argparse.ArgumentParser(description="Manage unique IDs for HTML content blocks.")
    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # auto-tag command
    parser_tag = subparsers.add_parser('auto-tag', help='Automatically add IDs to elements missing them')
    parser_tag.add_argument('--dry-run', action='store_true', help='Show what would be done without modifying files')

    # verify command
    parser_verify = subparsers.add_parser('verify', help='Check for duplicate IDs')

    # next-id command
    parser_next = subparsers.add_parser('next-id', help='Generate a new unique ID')

    args = parser.parse_args()

    manager = IDManager()

    if args.command == 'auto-tag':
        manager.auto_tag(dry_run=args.dry_run)
    elif args.command == 'verify':
        manager.verify()
    elif args.command == 'next-id':
        manager.next_id()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()

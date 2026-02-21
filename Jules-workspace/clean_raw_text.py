import os
import re
import argparse

def clean_file(file_path):
    """
    Removes English words from the beginning and end of a text file.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to match English words, numbers, and some punctuation at the start of the string
    # It will also match newlines and spaces surrounding the english words
    start_pattern = re.compile(r'^[\s\na-zA-Z0-9.,!?;:\'"-]*')

    # Regex to match English words, numbers, and some punctuation at the end of the string
    # It will also match newlines and spaces surrounding the english words
    end_pattern = re.compile(r'[\s\na-zA-Z0-9.,!?;:\'"-]*$')

    # Remove matching patterns from the start and end of the content
    cleaned_content = start_pattern.sub('', content)
    cleaned_content = end_pattern.sub('', cleaned_content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(cleaned_content)

def main():
    parser = argparse.ArgumentParser(description="Clean raw text files by removing English words from the start and end.")
    parser.add_argument("directory", help="The directory containing the raw text files.")
    args = parser.parse_args()

    if not os.path.isdir(args.directory):
        print(f"Error: Directory not found at {args.directory}")
        return

    print(f"Cleaning files in {args.directory}...")

    for filename in os.listdir(args.directory):
        if filename.endswith(".txt"):
            file_path = os.path.join(args.directory, filename)
            print(f"Cleaning {filename}...")
            clean_file(file_path)

    print("Cleaning complete.")

if __name__ == "__main__":
    main()

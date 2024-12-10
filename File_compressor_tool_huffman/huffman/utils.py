import sys
import os
from collections import Counter
import typing

def parse_arguments() -> typing.Tuple[str, str]:
    """Parse command-line arguments."""
    arguments = sys.argv[1:]

    if len(arguments) < 2:
        print("Usage: python main.py <flag> <file_path>")
        sys.exit(1)

    flag = arguments[0]
    file_path = arguments[1]

    return flag, file_path

def validate_file(file_path: str) -> str:
    """Validate if the file exists and is readable."""
    if not os.path.isfile(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)
    return os.path.abspath(file_path)


def calculate_character_frequency(file_path : str) -> Counter:
    """Calculate the frequency of each character in the file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = file.read()
            if not data.strip():
                print(f"Error: File '{file_path}' is empty.")
                sys.exit(1)
            return Counter(data)
    except Exception as e:
        print(f"Error reading file '{file_path}': {e}")
        sys.exit(1)


def log_frequency_table(frequency_table : Counter):
    """Log the frequency table in a readable format."""
    print("\nCharacter Frequency Table:")
    for char, freq in sorted(frequency_table.items(), key=lambda x: (-x[1], x[0])):
        printable_char = repr(char) if char.strip() else "Whitespace"
        print(f"{printable_char}: {freq}")
import sys
from typing import List

def read_input(filename: str = None) -> List[str]:
    """
    Reads lines from a file or stdin.
    """

    lines = []

    try:
        if filename:
            with open(filename, 'r', encoding='utf-8', errors='ignore') as f:
                lines = f.readlines()
        elif not sys.stdin.isatty():
            lines = sys.stdin.readlines()
        else:
            return []
        
        return [line.strip() for line in lines]
    
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error reading input: {e}", file=sys.stderr)
        sys.exit(1)
#!/usr/bin/python3

import argparse
import os
import sys


class WordCounter:
    def __init__(self):
        pass

    def count_bytes(self, filename):
        return os.path.getsize(filename)

    def count_newlines(self, data):
        return data.count('\n')

    def count_words(self, data):
        return len(data.split())

    def count_characters(self, data):
        return len(data)


def main():
    wc = WordCounter()

    # Argument parser setup
    parser = argparse.ArgumentParser(description="Count bytes, lines, words, and characters in a file or input.")
    parser.add_argument("-c", "--bytes", help="Print the byte counts", action="store_true")
    parser.add_argument("-l", "--lines", help="Print the line counts", action="store_true")
    parser.add_argument("-w", "--words", help="Print the word counts", action="store_true")
    parser.add_argument("-m", "--chars", help="Print the character counts", action="store_true")
    parser.add_argument("filename", help="The file to process", nargs="?")
    args = parser.parse_args()

    if args.filename:
        with open(args.filename, 'r', encoding="utf8") as file:
            data = file.read()
        source = args.filename
    elif not sys.stdin.isatty():
        data = sys.stdin.read()
        source = ""
    else:
        print("No input provided. Please specify a file or pipe input through stdin.")
        parser.print_help()
        return

    if not (args.bytes or args.lines or args.words or args.chars):
        file_size = wc.count_bytes(args.filename) if args.filename else len(data.encode('utf-8'))
        line_count = wc.count_newlines(data)
        word_count = wc.count_words(data)
        char_count = wc.count_characters(data)
        print(f"{line_count} {word_count} {file_size} {source}")
        return


    if args.bytes:
        file_size = wc.count_bytes(args.filename) if args.filename else len(data.encode('utf-8'))
        print(f"{file_size} {source}")
    if args.lines:
        line_count = wc.count_newlines(data)
        print(f"{line_count} {source}")
    if args.words:
        word_count = wc.count_words(data)
        print(f"{word_count} {source}")
    if args.chars:
        char_count = wc.count_characters(data)
        print(f"{char_count} {source}")


if __name__ == "__main__":
    main()

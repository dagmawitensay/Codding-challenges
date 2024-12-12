# Huffman Compression Tool

This directory contains a Python-based implementation of a Huffman compression and decompression tool. It is designed to encode and decode files efficiently using Huffman coding, a lossless data compression algorithm.

## Overview

This project solves the [Huffman Compression Challenge](https://codingchallenges.fyi/challenges/challenge-huffman) by implementing a command-line tool for file compression and decompression. The algorithm effectively handles both ASCII and Unicode characters, utilizing a frequency-based Huffman tree structure for efficient data encoding.

## Features

- **Huffman Tree Construction**: Generates a binary tree based on character frequencies.
- **File Compression**: Converts text into compact binary data.
- **File Decompression**: Restores the original file from compressed data.
- **Unicode Support**: Handles both ASCII and non-ASCII characters.
- **Compact Frequency Serialization**: Stores frequency data in an optimized format.
- **Command-line Interface**: Supports compress and decompress commands for easy file handling.

## Installation

### Requirements

- Python 3.8 or higher

### Setup

1. Install dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

2. Run the main program:
   ```bash
   python main.py
   ```

## Usage

### Commands

#### Compression
Compress a file into a Huffman-encoded binary format:
```bash
python main.py compress <input_file> <output_file>
```
Example:
```bash
python main.py compress sample.txt compressed.huf
```

#### Decompression
Decompress a Huffman-encoded file:
```bash
python main.py decompress <input_file> <output_file>
```
Example:
```bash
python main.py decompress compressed.huf decompressed.txt
```

## How It Works

1. **Character Frequency Calculation**: Counts the frequency of each character in the input file.
2. **Huffman Tree Construction**: Builds a binary tree to generate unique binary codes for each character.
3. **Encoding**: Encodes input text using the Huffman codes.
4. **Serialization**: Saves the frequency table and compressed data in the output file.
5. **Decoding**: Reads the frequency table, reconstructs the Huffman tree, and restores the original content.

## Example

### Input File (`sample.txt`):
```
HELLO WORLD
```

### Compressed File (`compressed.huf`):
- Contains binary data with a header including:
  - Magic number (`HUFCMP`)
  - Serialized frequency table

### Decompressed File (`decompressed.txt`):
```
HELLO WORLD
```

## Implementation Details

### Frequency Table Serialization
- The frequency table is serialized compactly:
  1. Number of entries (4 bytes, big-endian).
  2. Each entry includes:
     - ASCII characters: `0 + character`.
     - Non-ASCII characters: `1 + length (2 bytes) + UTF-8 bytes`.
     - Frequency: Encoded using variable-length encoding.

### Variable-Length Encoding
- Frequencies are stored using 7-bit chunks with a continuation bit (`0x80`) for multi-byte values.

## Edge Cases

1. Handles empty files gracefully.
2. Compresses files with a single unique character.
3. Supports mixed ASCII and non-ASCII content.
4. Ensures decompressed output matches the original input exactly.

## Acknowledgments

- Inspired by the [Coding Challenges Huffman Compression](https://codingchallenges.fyi/challenges/challenge-huffman).
- Special thanks to [Huffman Coding Explained](https://www.youtube.com/watch?v=co4_ahEDCho) and [Data Compression with Huffman Coding](https://www.youtube.com/watch?v=B3y0RsVCyrw&t=1258s) for insightful explanations.



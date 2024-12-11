import sys
import os
from collections import Counter
from huffman.tree import HuffmanTree
from typing import Dict

class CompressorUtils:
    @staticmethod
    def validate_file(file_path: str) -> str:
        """Validate if the file exists and is readable."""
        if not os.path.isfile(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            sys.exit(1)
        return os.path.abspath(file_path)

    @staticmethod
    def get_file_content(file_path: str) -> str:
        """Read the content of the file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except Exception as e:
            print(f"Error reading file '{file_path}': {e}")
            sys.exit(1)

    @staticmethod
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

    @staticmethod
    def log_frequency_table(frequency_table : Counter):
        """Log the frequency table in a readable format."""
        print("\nCharacter Frequency Table:")
        for char, freq in sorted(frequency_table.items(), key=lambda x: (-x[1], x[0])):
            printable_char = repr(char) if char.strip() else "Whitespace"
            print(f"{printable_char}: {freq}")
    
    @staticmethod
    def encode_text(data: str, codes: dict) -> str:
        """Encode the text using the Huffman codes."""
        return ''.join(codes[char] for char in data)
    
    @staticmethod
    def get_byte_arary(encoded_text: str) -> bytes:
        """Convert the encoded text to a byte array."""
        # Pad the encoded text to a multiple of 8
        padding = 8 - len(encoded_text) % 8
        encoded_text += '0' * padding

        # Convert the encoded text to bytes
        byte_array = bytes([int(encoded_text[i:i + 8], 2) for i in range(0, len(encoded_text), 8)])

        return bytes([padding]) + byte_array

    @staticmethod
    def write_header_with_compressed_data(output_file: str, frequency_table: Dict[str, int], compressed_data: bytes) -> None:
        """
        Write the header with the serialized frequency table and compressed data to the output file.
        Args:
            output_file: The output file object.
            frequency_table: The frequency table to write.
            compressed_data: The compressed data to write.
        """

        serialized_frequency_table = HuffmanTree.serialize_frequency_table(frequency_table)
        header_length = len(serialized_frequency_table)

        with open(output_file, 'wb') as file:
            file.write(b'HUFCMP') 
            file.write(header_length.to_bytes(4, byteorder='big'))

            file.write(serialized_frequency_table)
            file.write(CompressorUtils.get_byte_arary(compressed_data))


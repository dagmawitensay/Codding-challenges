from huffman.tree import HuffmanTree
from typing import Dict

class DecompressorUtils:
    @staticmethod
    def read_header_and_data(input_file: str) -> str:
        """
        Read and parse the header and compressed data from the input file.

        Args:
            input_file: Path to the input compressed file.

        Returns:
            A tuple (frequency_table, compressed_data).
        """
        with open(input_file, 'rb') as file:
            # Validate magic number
            magic = file.read(6)
            if magic != b'HUFCMP':
                raise ValueError("Invalid file format.")
            
            # Read header length
            header_length = int.from_bytes(file.read(4), 'big')
            
            # Read serialized header
            serialized_header = file.read(header_length)
            frequency_table = HuffmanTree.deserialize_frequency_table(serialized_header)
            
            # Read compressed data
            compressed_data = file.read()
        
        return frequency_table, compressed_data

    @staticmethod
    def get_binary_string(byte_array: bytes) -> str:
        """Convert a byte array back into a binary string."""
        padding = byte_array[0]
        # Convert each byte in the byte array to its binary representation
        binary_string = ''.join(format(byte, '08b') for byte in byte_array[1:])

        if padding > 0:
            binary_string = binary_string[:-padding]
        
        return binary_string
    
    @staticmethod
    def decode_text(encoded_text: str, reverse_code_table: Dict[str, str]) -> str:
        """
        Decode the encoded text using the reverse code table.
        """
        code_string = ""
        decoded_text = ""
        for bit in encoded_text:
            code_string += bit
            if code_string in reverse_code_table:
                decoded_text += reverse_code_table[code_string]
                code_string = ""
        
        return decoded_text
    
    @staticmethod
    def write_to_file(decoded_text: str, output_file: str) -> None:
        """Write the decoded text to a file."""
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(decoded_text)



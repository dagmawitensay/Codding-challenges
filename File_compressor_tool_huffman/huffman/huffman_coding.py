from huffman.compressor_utils import CompressorUtils
from huffman.decompressor_utils import DecompressorUtils
from huffman.tree import HuffmanTree

class HuffmanCoding:
    """
    Performs compression and decompression using Huffman Coding.
    Attributes:
        file_path (str): The path to the input file.
        tree (HuffmanTree): The Huffman tree used for encoding and decoding.
    """
    def __init__(self, file_path: str) -> None:
        """
        Initialize the HuffmanCoding object.
        Args:
            file_path (str): The path to the input file.
        """
        self.file_path = file_path
        self.tree = None
    
    def compress(self, output_path: str) -> None:
        """
        Compress the input file using Huffman Coding.
        """
        frequency_table = CompressorUtils.calculate_character_frequency(self.file_path)
        self.tree = HuffmanTree(frequency_table)
        self.tree.build_tree()
        self.tree.generate_codes()
        text = CompressorUtils.get_file_content(self.file_path)
        compressed_text = CompressorUtils.encode_text(text, self.tree.get_codes())
        CompressorUtils.write_header_with_compressed_data(output_path, frequency_table, compressed_text)

        print("Compression complete.")
    
    def decompress(self, input_path: str, output_path: str) -> None:
        """
        Decompress the input file using Huffman Coding.
        """
        frequency_table, compressed_data = DecompressorUtils.read_header_and_data(input_path)
        tree = HuffmanTree(frequency_table)
        tree.build_tree()
        tree.generate_codes()
        decoded_text = DecompressorUtils.decode_text(DecompressorUtils.get_binary_string(compressed_data), tree.reverse_codes)
        DecompressorUtils.write_to_file(decoded_text, output_path)
        
        print("Decompression complete")
import unittest
from collections import Counter
from huffman.tree import HuffmanTree

class TestHuffmanTree(unittest.TestCase):
    def test_huffman_tree(self):
        frequency_table = Counter({'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45})
        huffman_tree = HuffmanTree(frequency_table)
        huffman_tree.build_tree()
        huffman_tree.generate_codes()
        codes = huffman_tree.get_codes()

        # Verify the codes (order may vary)
        self.assertIn('A', codes)
        self.assertIn('B', codes)
        self.assertIn('C', codes)
        self.assertIn('D', codes)
        self.assertIn('E', codes)
        self.assertIn('F', codes)

        # Verify total number of codes
        self.assertEqual(len(codes), len(frequency_table))
    
    def test_basic_huffman_codes():
        frequency_table = Counter({'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45})
        huffman_tree = HuffmanTree(frequency_table)
        
        huffman_tree.build_tree()
        huffman_tree.generate_codes()
        codes = huffman_tree.get_codes()
        
        # Verify that all characters have a code
        assert set(codes.keys()) == set(frequency_table.keys())
        
        # Verify that codes are non-empty and unique
        assert all(len(code) > 0 for code in codes.values())
        assert len(set(codes.values())) == len(frequency_table)
    
    def test_single_character():
        frequency_table = Counter({'A': 10})
        huffman_tree = HuffmanTree(frequency_table)
        
        huffman_tree.build_tree()
        huffman_tree.generate_codes()
        codes = huffman_tree.get_codes()
        
        # Single character should have a code of "0"
        assert codes == {'A': '0'}  
    
    def test_empty_frequency_table():
        frequency_table = Counter()
        huffman_tree = HuffmanTree(frequency_table)
        
        try:
            huffman_tree.build_tree()
            huffman_tree.generate_codes()
        except ValueError as e:
            assert str(e) == "Huffman tree has not been built yet."
        else:
            assert False, "Expected ValueError for empty frequency table."

if __name__ == "__main__":
    unittest.main()
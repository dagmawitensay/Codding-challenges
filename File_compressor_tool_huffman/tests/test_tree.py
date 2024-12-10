import unittest
from collections import Counter
from huffman.tree import HuffmanTree

class TestHuffmanTree(unittest.TestCase):
    def test_huffman_tree(self):
        frequency_table = Counter({'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45})
        huffman_tree = HuffmanTree(frequency_table)
        huffman_tree.build_tree()
        # huffman_tree.generate_codes()
        # codes = huffman_tree.get_codes()

        # # Verify the codes (order may vary)
        # self.assertIn('A', codes)
        # self.assertIn('B', codes)
        # self.assertIn('C', codes)
        # self.assertIn('D', codes)
        # self.assertIn('E', codes)
        # self.assertIn('F', codes)

        # # Verify total number of codes
        # self.assertEqual(len(codes), len(frequency_table))

if __name__ == "__main__":
    unittest.main()
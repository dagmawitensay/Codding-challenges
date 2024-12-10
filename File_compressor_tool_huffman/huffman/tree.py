import heapq
from collections import Counter
from typing import Dict, List, Optional, Tuple


class HuffmanNode:
    def __init__(self, value: Optional[str], frequency: int):
        """
        A node in the Huffman tree.

        :param value: The character value of the node (None for internal nodes).
        :param frequency: The frequency of the character or combined frequency for internal nodes.
        """
        self.value: Optional[str] = value
        self.frequency: int = frequency
        self.left: Optional['HuffmanNode'] = None
        self.right: Optional['HuffmanNode'] = None
        self.isLeaf: bool = value is not None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.frequency < other.frequency

    def __repr__(self) -> str:
        return f"HuffmanNode(value={self.value}, frequency={self.frequency})"


class HuffmanTree:
    def __init__(self, frequency_table: Counter):
        """
        Initialize the HuffmanTree with a frequency table.

        :param frequency_table: A Counter object containing character frequencies.
        """
        self.frequency_table: Dict[str, int] = frequency_table
        self.root: Optional[HuffmanNode] = None
        self.codes: Dict[str, str] = {}

    def build_tree(self):
        """
        Build the Huffman tree using a priority queue (min-heap).
        """
        priority_queue: List[HuffmanNode] = []

        for char, freq in self.frequency_table.items():
            heapq.heappush(priority_queue, HuffmanNode(char, freq))

        # Build the tree by combining the two smallest nodes until one tree remains
        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)

            parent = HuffmanNode(None, left.frequency + right.frequency)
            parent.left = left
            parent.right = right
            heapq.heappush(priority_queue, parent)
            
        self.root = priority_queue[0]


# Example usage
if __name__ == "__main__":
    # Example frequency table from the linked URL
    frequency_table = Counter({
        'C': 32, 'D': 42, 'E': 120, 'K': 7, 'L': 42, 'M': 24, 'U': 37, 'Z': 2
    })

    # Build the Huffman tree
    huffman_tree = HuffmanTree(frequency_table)
    huffman_tree.build_tree()

    # Generate and print the Huffman codes
    huffman_tree.generate_codes()
    huffman_codes = huffman_tree.get_codes()
    print("Huffman Codes:", huffman_codes)
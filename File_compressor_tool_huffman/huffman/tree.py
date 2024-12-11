import heapq
import struct
from collections import Counter
from typing import Dict, List, Optional


class HuffmanNode:
    def __init__(self, value: Optional[str], frequency: int, right: Optional['HuffmanNode'] = None, left: Optional['HuffmanNode'] = None):
        """
        A node in the Huffman tree.

        :param value: The character value of the node (None for internal nodes).
        :param frequency: The frequency of the character or combined frequency for internal nodes.
        """
        self.value: Optional[str] = value
        self.frequency: int = frequency
        self.right: Optional['HuffmanNode'] = right
        self.left: Optional['HuffmanNode'] = left
        self.is_leaf: bool = value is not None

    def __lt__(self, other: 'HuffmanNode') -> bool:
        return self.frequency < other.frequency

    def __repr__(self) -> str:
        return f"HuffmanNode(value={self.value}, frequency={self.frequency})"


class HuffmanTree:
    def __init__(self, frequency_table: Counter) -> None:
        """
        Initialize the HuffmanTree with a frequency table.

        :param frequency_table: A Counter object containing character frequencies.
        """
        self.frequency_table: Dict[str, int] = frequency_table
        self.root: Optional[HuffmanNode] = None
        self.codes: Dict[str, str] = {}
        self.reverse_codes: Dict[str, str] = {}

    def build_tree(self) -> None:
        """
        Build the Huffman tree using a priority queue (min-heap).
        """

        if not self.frequency_table:
            raise ValueError("Frequency table is empty. Cannot build Huffman tree.")

        priority_queue: List[HuffmanNode] = []

        for char, freq in self.frequency_table.items():
            heapq.heappush(priority_queue, HuffmanNode(char, freq))
        
        if len(priority_queue) == 1:
            single_node = heapq.heappop(priority_queue)
            self.root = HuffmanNode(None, single_node.frequency, left=single_node)
            return

        # Build the tree by combining the two smallest nodes until one tree remains
        while len(priority_queue) > 1:
            left = heapq.heappop(priority_queue)
            right = heapq.heappop(priority_queue)

            heapq.heappush(priority_queue, HuffmanNode(None, left.frequency + right.frequency, right, left))
            
        self.root = priority_queue[0]
    
    def generate_codes(self) -> None:
        """
        Generate the Huffman codes for each character in the fequency table
        """
        if self.root is None:
            raise ValueError("Huffman tree has not been built yet.")
        
        self._generate_codes_helper(self.root, '')

    def _generate_codes_helper(self, node: HuffmanNode, code: str) -> None:
        """
        Recursively generate the Huffman codes for each character in the tree.
        Args:
            node: The current node in the tree.
            code: The current code being generated.
        """
        if node.is_leaf:
            self.codes[node.value] = code
            self.reverse_codes[code] = node.value
            return
        
        if node.left:
            self._generate_codes_helper(node.left, code + '0')
        
        if node.right:
            self._generate_codes_helper(node.right, code + '1')
    
    def get_codes(self) -> Dict[str, str]:
        """
        Get the generated Huffman codes.
        Returns:
            A dictionary containing the Huffman codes for each character.
        """
        return self.codes

    @staticmethod
    def serialize_frequency_table(frequency_table: Dict[str, int]) -> bytes:
        """
        Serialize a frequency table into a compact byte format.
        
        Args:
            frequency_table: Dictionary with characters as keys and frequencies as values.
        
        Returns:
            A serialized byte array.
        """
        serialized = bytearray()

        # Number of entries in the table (4 bytes, big-endian)
        serialized.extend(struct.pack('>I', len(frequency_table)))

        for char, freq in frequency_table.items():
            char_bytes = char.encode('utf-8')  # UTF-8 encoding
            char_length = len(char_bytes)

            # Encode character length and content
            if char_length == 1 and char_bytes[0] < 128:  # ASCII optimization
                # For ASCII, store directly without length
                serialized.append(0)  # ASCII marker
                serialized.extend(char_bytes)
            else:
                # For non-ASCII, store length and bytes
                serialized.append(1)  # Unicode marker
                serialized.extend(struct.pack('>H', char_length))  # 2-byte length
                serialized.extend(char_bytes)

            # Encode frequency using variable-length encoding
            while freq >= 0x80:  # More significant bytes follow
                serialized.append((freq & 0x7F) | 0x80)  # Store 7 bits with continuation bit
                freq >>= 7
            serialized.append(freq & 0x7F)  # Final byte without continuation

        return bytes(serialized)

    @staticmethod
    def deserialize_frequency_table(serialized_data: bytes) -> Dict[str, int]:
        """
        Deserialize a frequency table from a compact byte format.
        
        Args:
            serialized_data: Serialized byte array.
        
        Returns:
            A dictionary with characters as keys and frequencies as values.
        """
        frequency_table = {}
        index = 0

        # Read number of entries (4 bytes)
        num_entries = struct.unpack_from('>I', serialized_data, index)[0]
        index += 4

        for _ in range(num_entries):
            marker = serialized_data[index]
            index += 1

            if marker == 0:  # ASCII
                char = chr(serialized_data[index])
                index += 1
            elif marker == 1:  # Unicode
                char_length = struct.unpack_from('>H', serialized_data, index)[0]
                index += 2
                char = serialized_data[index:index + char_length].decode('utf-8')
                index += char_length
            else:
                raise ValueError("Invalid marker in serialized data.")

            freq = 0
            shift = 0
            while True:
                byte = serialized_data[index]
                index += 1
                freq |= (byte & 0x7F) << shift
                if byte & 0x80 == 0:  # Last byte
                    break
                shift += 7

            frequency_table[char] = freq

        return frequency_table
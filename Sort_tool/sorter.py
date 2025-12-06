from typing import List
from .algorithms import ALGORITHM_MAP

class Sorter:
    def __init__(self, algorithm_name: str, unique: bool):
        self.algo_func = ALGORITHM_MAP.get(algorithm_name, sorted)
        self.unique = unique
    
    def process(self, data: List[str]) -> List[str]:
        if not data:
            return []
        
        result = self.algo_func(data)

        if self.unique:
            result = self._deduplicate(result)
        
        return result
    
    def _deduplicate(self, sorted_data: List[str]) -> List[str]:
        """Removes adjacent duplicates (requires sorted list)."""
        if not sorted_data:
            return []
        
        unique_list = [sorted_data[0]]
        for i in range(1, len(sorted_data)):
            if sorted_data[i] != sorted_data[i - 1]:
                unique_list.append(sorted_data[i])
        
        return unique_list
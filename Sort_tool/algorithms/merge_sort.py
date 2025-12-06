from typing import List

def merge_sort(data: List[str]) -> List[str]:
    """Implementaion of Merge Sort."""

    if len(data) <= 1:
        return data

    mid = len(data) // 2

    left_half = merge_sort(data[:mid])
    right_half = merge_sort(data[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        
    
    result.extend(left[i:])
    result.extend(right[j:])

    return result
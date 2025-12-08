from typing import List

def radix_sort(data: List[str]) -> List[str]:
    byte_data = [s.encode('utf-8') for s in data]
    
    if not byte_data:
        return []

    longest = max(len(b) for b in byte_data)
    
    for i in range(longest - 1, -1, -1):
        byte_data = bucket_sort(byte_data, i)
    
    return [b.decode('utf-8') for b in byte_data]


def bucket_sort(data: List[bytes], current_index: int) -> List[bytes]:
    buckets = [[] for _ in range(256)]

    for word in data:
        if current_index < len(word):
            bucket_index = word[current_index]
        else:
            bucket_index = 0
            
        buckets[bucket_index].append(word)

    res = []
    for bucket in buckets:
        res.extend(bucket)
        
    return res
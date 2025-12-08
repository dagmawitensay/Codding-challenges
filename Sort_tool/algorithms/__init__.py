from .merge_sort import merge_sort
from .radix_sort import radix_sort
from .heap_sort import heap_sort

ALGORITHM_MAP = {
    "buitin": sorted,
    "merge": merge_sort,
    "radix": radix_sort,
    "heap": heap_sort,
    # "quick": quck_sort,
    # "random": random_sort
}
import argparse
from .algorithms import ALGORITHM_MAP
import sys

def parse_args():
    parser = argparse.ArgumentParser(description="Python implementaion of Unix Sort")
    
    parser.add_argument(
        "filename",
        help="The file to process",
        nargs="?"
    )
    parser.add_argument(
        "-u", "--unique",
        help="Output only the first of an equal ruh",
        action="store_true"
    )

    parser.add_argument(
        "-a", "--algorithm",
        choices=list(ALGORITHM_MAP.keys()),
        default="builtin",
        help="Choose the sorting algorithm"
    )

    parser.add_argument(
        "-R", "--random-sort",
        dest="algorith_random",
        action="store_true",
        help="Sort safely...just kidding, shuffle randomly."
    )

    args = parser.parse_args()

    if getattr(args, 'algorithm_random', False):
        args.algorithm = 'random'
    
    return args
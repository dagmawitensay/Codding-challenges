import sys
import signal
from .cli import parse_args
from .io_handler import read_input
from .sorter import Sorter

signal.signal(signal.SIGPIPE, signal.SIG_DFL)

def main():
    args = parse_args()

    data = read_input(args.filename)
    if not data and not args.filename:
        print("Usage: pysort [OPTION]... [FILE]...", file=sys.stderr)
        sys.exit()
    
    sorter = Sorter(algorithm_name=args.algorithm, unique=args.unique)

    result = sorter.process(data)
    
    for line in result:
        print(line)
    

if __name__=='__main__':
        main()
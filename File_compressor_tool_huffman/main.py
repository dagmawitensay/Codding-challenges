from huffman.compressor_utils import CompressorUtils
from huffman.huffman_coding import HuffmanCoding
import argparse
import sys


def main():
    parser = argparse.ArgumentParser(description="A command-line tool for file compression and decompression.")

    subparsers = parser.add_subparsers(
        title="Commands", 
        description="Valid commands", 
        help="Available commands"
    )
    
    # Compress command
    compress_parser = subparsers.add_parser(
        "compress", 
        help="Compress a file."
    )
    compress_parser.add_argument(
        "input_path", 
        type=CompressorUtils.validate_file, 
        help="The path to the file to compress."
    )
    compress_parser.add_argument(
        "output_path", 
        type=str, 
        help="The path where the compressed file will be saved."
    )
    compress_parser.set_defaults(command="compress")
    
    # Decompress command
    decompress_parser = subparsers.add_parser(
        "decompress", 
        help="Decompress a file."
    )
    decompress_parser.add_argument(
        "input_path", 
        type=CompressorUtils.validate_file,  
        help="The path to the compressed file to decompress."
    )
    decompress_parser.add_argument(
        "output_path", 
        type=str, 
        help="The path where the decompressed file will be saved."
    )
    decompress_parser.set_defaults(command="decompress")
    
    args = parser.parse_args()
    
    if not hasattr(args, "command"):
        parser.print_help()
    else:

        if args.command == "compress":
            file_path = CompressorUtils.validate_file(args.input_path)
            huffman_coding = HuffmanCoding(file_path)
            huffman_coding.compress(args.output_path)

            print(f"Compressing file {args.input_path} to {args.output_path}...")
        elif args.command == "decompress":
            file_path = CompressorUtils.validate_file(args.input_path)
            if not file_path.endswith('.huff'):
                print(f"Error: Input file '{file_path}' does not appear to be a valid compressed file.")
                sys.exit(1)
            huffman_coding = HuffmanCoding(file_path)
            huffman_coding.decompress(args.input_path, args.output_path)
            print(f"Decompressing file {args.input_path} to {args.output_path}...")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

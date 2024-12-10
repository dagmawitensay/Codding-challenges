from huffman.utils import parse_arguments, validate_file, calculate_character_frequency, log_frequency_table


def main():
    flag, file_path = parse_arguments()

    file_path = validate_file(file_path)

    character_frequency = calculate_character_frequency(file_path)

    # Log the character frequency table if the flag is set to --log
    if flag == "--log":
        log_frequency_table(character_frequency)
    else:
        print(character_frequency)


if __name__ == '__main__':
    main()
import unittest
from collections import Counter
from main import calculate_character_frequency

class TestCharacterFrequency(unittest.TestCase):
    def test_frequency_with_sample_data(self):
        # Simulate input data
        data = "aaabbcXttttt"
        expected_frequency = Counter({'t': 5, 'a': 3, 'b': 2, 'c': 1, 'X': 1})

        # Write data to a temporary file
        with open("test_input.txt", "w") as file:
            file.write(data)

        # Calculate frequency
        actual_frequency = calculate_character_frequency("test_input.txt")

        # Assert the expected result
        self.assertEqual(actual_frequency, expected_frequency)

    def test_empty_file(self):
        # Create an empty file
        with open("empty.txt", "w") as file:
            pass

        # Assert it raises an error
        with self.assertRaises(SystemExit):
            calculate_character_frequency("empty.txt")


if __name__ == "__main__":
    unittest.main()
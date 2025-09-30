# Contents of /Merging_Motion_ELAN/Merging_Motion_ELAN/tests/test_processing.py

import unittest
from src.main import merge_data  # Assuming merge_data is a function in main.py

class TestProcessing(unittest.TestCase):

    def test_merge_data(self):
        # Example test case for the merge_data function
        input_data_1 = "path/to/first/input"
        input_data_2 = "path/to/second/input"
        expected_output = "path/to/expected/output"

        result = merge_data(input_data_1, input_data_2)
        self.assertEqual(result, expected_output)

    def test_merge_data_invalid(self):
        # Example test case for handling invalid input
        input_data_1 = "invalid/path"
        input_data_2 = "another/invalid/path"

        with self.assertRaises(FileNotFoundError):
            merge_data(input_data_1, input_data_2)

if __name__ == '__main__':
    unittest.main()
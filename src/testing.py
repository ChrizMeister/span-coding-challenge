# Code by Christopher Sommerville
# Span coding challenge

import unittest
import json
import os
import os.path
from os import path

from NotificationModFunctions import old_to_new, get_epoch, convert_priority, remove_duplicates, sort_notifications

class NotificationTests(unittest.TestCase): 
  
    def setUp(self): 
        pass

    # Part 1 tests
  
    # Returns true if the strings are converted properly
    def test_priority_converting(self):
        prio_str_1 = "HIGH" # 2
        prio_str_2 = "MID" # 1
        prio_str_3 = "LOW" # 0
        self.assertEqual(convert_priority(prio_str_1), 2)
        self.assertEqual(convert_priority(prio_str_2), 1)
        self.assertEqual(convert_priority(prio_str_3), 0)
        self.assertEqual(convert_priority("EXTRA HIGH"), -1)
  
    # Returns true if the ISO string is converted to unix epoch correctly
    def test_epoch_converting(self):
        input_str = "2021-03-20T00:37:48.100Z"
        expected_output = 1616200668100 
        self.assertEqual(get_epoch(input_str), expected_output) 

    # Returns true if the notification was converted correctly
    def test_old_to_new(self): 
        path_parent = os.path.dirname(os.getcwd())
        os.chdir(path_parent)
        # Load input file        
        input_file =  os.getcwd() + "\\tests\\" + 'part1_test_input.json'
        with open(input_file) as in_file:
            input_data = json.load(in_file)
        
        # Load comparison file
        expected_output_file =  os.getcwd() + "\\tests\\" + 'part1_test_expected_output.json'
        with open(expected_output_file) as comparison_file:
            comparison_data = json.load(comparison_file)

        self.assertEqual(comparison_data[0], old_to_new(input_data[0]))

    # Part 2 tests

    # Returns true if the proper duplicates were removed
    def test_removing_duplicates(self):
        # Load input file        
        input_file =  os.getcwd() + "\\tests\\" + 'part2_test_input.json'
        with open(input_file) as in_file:
            input_data = json.load(in_file)
        
        # Load comparison file
        expected_output_file =  os.getcwd() + "\\tests\\" + 'part2_test_expected_output.json'
        with open(expected_output_file) as comparison_file:
            comparison_data = json.load(comparison_file)

        self.assertEqual(comparison_data, remove_duplicates(input_data))

    # Part 3 tests

    # Returns true if the notifications were sorted properly
    def test_sorting(self):
        # Load input file        
        input_file =  os.getcwd() + "\\tests\\" + 'part3_test_input.json'
        with open(input_file) as in_file:
            input_data = json.load(in_file)
        
        # Load comparison file
        expected_output_file =  os.getcwd() + "\\tests\\" + 'part3_test_expected_output.json'
        with open(expected_output_file) as comparison_file:
            comparison_data = json.load(comparison_file)

        sort_notifications(input_data)

        self.assertEqual(comparison_data, input_data)


if __name__ == '__main__':
    unittest.main()
    
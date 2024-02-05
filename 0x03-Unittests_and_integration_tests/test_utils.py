#!/usr/bin/env python3
'''test_utils'''
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    '''This class inherits from unittest.TestCase
    and the method tests whether the method returns
    what it is supposed to'''

    @parameterized.expand([
         ({"a": 1}, ("a",), 1),
         ({"a": {"b": 2}}, ("a",), {"b": 2}),
         ({"a": {"b": 2}}, ("a", "b"), 2),
     ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        '''This method tests whether the function returns the expected
        values'''
        self.assertEqual(access_nested_map(nested_map, path), expected_result)

    @parameterized.expand([
        ({}, ["a"], KeyError, "Key 'a' not found in nested map"),
        ({"a": 1}, ["a", "b"], KeyError, "Key 'b' not found in nested map"),
    ])
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_exception, expected_message):
        '''This function tests whether the
        correct error is raised'''
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()

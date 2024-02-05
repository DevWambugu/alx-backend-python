#!/usr/bin/env python3
'''test_utils'''
import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json


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


class TestGetJson(unittest.TestCase):
    '''This class implements the TestGetJson.test_get_json
    method to test that utils.get_json returns the expected result'''

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_requests_get):
        '''This function tests the get_json method'''
        mock_json = Mock()
        mock_json.return_value = test_payload
        mock_response = Mock()
        mock_response.json = mock_json
        mock_requests_get.return_value = mock_response
        result = get_json(test_url)
        mock_requests_get.assert_called_once_with(test_url)
        self.assertEqual(result, test_payload)


if __name__ == '__main__':
    unittest.main()

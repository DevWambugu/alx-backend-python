#!/usr/bin/env python3
'''test_utils'''
import unittest
from parameterized import parameterized
from utils import access_nested_map
from unittest.mock import patch, Mock
from utils import get_json
from utils import memoize


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


class TestMemoize(unittest.TestCase):
    '''This class tests the memoize method'''
    def test_memoize(self):
        '''This method contains a class that defines
        methods to test the memoize function'''
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(TestClass, 'a_method') as mock_a_method:
            test_class = TestClass()
            result1 = test_class.a_property
            result2 = test_class.a_property
            mock_a_method.assert_called_once()
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)


if __name__ == '__main__':
    unittest.main()

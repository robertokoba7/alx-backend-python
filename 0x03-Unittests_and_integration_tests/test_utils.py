#!/usr/bin/env python3

"""Test suite for the Utils module"""

import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test case for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, path, expected_output):
        """Test that access_nested_map returns the correct output"""
        real_output = access_nested_map(map, path)
        self.assertEqual(real_output, expected_output)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, map, path, wrong_output):
        """Test that access_nested_map raises the correct exception"""
        with self.assertRaises(KeyError) as e:
            access_nested_map(map, path)
            self.assertEqual(wrong_output, e.exception)


class TestGetJson(unittest.TestCase):
    """Test case for get_json function"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that get_json returns the correct output"""
        # Set up mock response with the test payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload

        # Use a patch to intercept requests.get and return the mock response
        with patch('requests.get', return_value=mock_response):
            real_response = get_json(test_url)
            self.assertEqual(real_response, test_payload)

            # Check that the mocked method was called once per input
            mock_response.json.assert_called_once()


class TestMemoize(unittest.TestCase):
    """Test case for memoize decorator"""

    def test_memoize(self):
        """Test that the memoize function works correctly"""

        class TestClass:
            """Class used for testing memoize decorator"""

            def a_method(self):
                """Method that always returns 42"""
                return 42

            @memoize
            def a_property(self):
                """Memoized property that calls a_method"""
                return self.a_method()

        # Use a patch to intercept calls to a_method and return 42
        with patch.object(TestClass, 'a_method', return_value=42) as patched:
            test_class = TestClass()

            # Call a_property twice to verify memoization
            real_return = test_class.a_property
            real_return = test_class.a_property

            self.assertEqual(real_return, 42)

            # Check that a_method was only called once
            patched.assert_called_once()


if __name__ == "__main__":
    unittest.main()

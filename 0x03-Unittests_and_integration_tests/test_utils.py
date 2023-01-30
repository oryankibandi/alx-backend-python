#!/usr/bin/env python3

"""
Tests the utils.access_nested_map function
"""


import unittest
import typing
from unittest.mock import MagicMock, patch, call
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """
    Tests the utils.access_nested_map function
    """

    @parameterized.expand([
        ('single_seq', {"a": 1}, ("a",), 1),
        ('dictionary', {"a": {"b": 2}}, ("a",), {"b": 2}),
        ('double_seq', {"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self, name: str, nested_map: map,
            sequence: typing.Sequence, expected) -> None:
        """tests correct result"""
        self.assertEqual(access_nested_map(nested_map, sequence), expected)

    @parameterized.expand([
        ("empty_path", {}, ("a",)),
        ("empty_path", {"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(
            self, name: str, nested: map, path: typing.Sequence) -> None:
        """Tests for a KeyError"""
        self.assertRaises(KeyError, access_nested_map, nested, path)


class TestGetJson(unittest.TestCase):
    """Tests get_json"""

    @parameterized.expand([
        ('example.com', "http://example.com", {"payload": True}),
        ('holberton.io', "http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests')
    def test_get_json(self, url: str, res: typing.Dict):
        """tests get_json"""
        mock_response = MagicMock()
        mock_response.json.return_value = res

        mock_requests.get.return_value = mock_response

        self.assertEqual(get_json(url), res)
        # self.assertEqual(mock_requests.call_count, 2)


class TesrMemoize(unittest.TestCase):
    """tests memoize function"""

    def test_memoize(self):
        """test memoize"""
        class TestClass:

            def a_method(self):
                """return 42"""
                return 42

            @memoize
            def a_property(self):
                """memoize a func"""
                return self.a_method()

        mock = MagicMock()
        test = TestClass()
        test.a_method = mock
        memoized = memoize(test.a_property)
        memoized(self)
        memoized(self)
        self.assertEqual(mock.call_count, 1)

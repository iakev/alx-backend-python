#!/usr/bin/env python3
"""
Contains Unit test for utils.access_nested_map function
"""
from parameterized import parameterized
from typing import Any, Mapping, Sequence
import unittest
from utils import access_nested_map, get_json
from unittest.mock import patch
from unittest.mock import Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    A testing class for utils.access_nested_map
    """

    @parameterized.expand([
        ("level_0_map", {"a": 1}, ("a",), 1),
        ("level_1_map", {"a": {"b": 2}}, ("a",), {"b": 2}),
        ("level_2_map", {"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, _: str, map: Mapping,
                               path: Sequence, expected: Any) -> None:
        """Method that tests that access_nested_map"""
        self.assertEqual(access_nested_map(map, path), expected)

    @parameterized.expand([
        ("No map", {}, ("a",), ("a")),
        ("1 level map", {"a": 1}, ("a", "b"), ("b"))
    ])
    def test_access_nested_map_exception(self, _: str, map: Mapping,
                                         path: Sequence, expected: Any) -> None:
        """Method testing access_nested_map exception"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(map, path)
        expected_msg = str(cm.exception)
        expected_msg = expected_msg[1:-1]
        self.assertEqual(expected_msg, expected)


class TestGetJson(unittest.TestCase):
    """
    Implementation to test utils.get_json method
    """

    @parameterized.expand([ 
        ("example.com", "http://example.com", {"payload": True}),
        ("holberton.io", "http://holberton.io", {"payload": False})
    ])
    @patch('utils.requests.get')
    def test_get_json(self, _: str, test_url: str, 
                      test_payload: Mapping, mock_get: Mock) -> None:
        """
        Tests that utils.get_json returns expected result
        """
        mock_get.return_value = Mock()
        mock_get.return_value.json.return_value = test_payload
        response = mock_get(test_url)
        mock_get.assert_called_once_with(test_url)
        self.assertEqual(response.json(), test_payload)

#!/usr/bin/env python3
"""
Contains Unit test for utils.access_nested_map function
"""
import unittest
from utils import access_nested_map
from parameterized import parameterized
from typing import Any, Mapping, Sequence


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
                                         path: Sequence, expected) -> None:
        """Method testing access_nested_map exception"""
        with self.assertRaises(KeyError) as cm:
            access_nested_map(map, path)
        expected_msg = str(cm.exception)
        expected_msg = expected_msg[1:-1]
        self.assertEqual(expected_msg, expected)

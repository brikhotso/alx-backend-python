#!/usr/bin/env python3
""" Unittest Task."""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """
    Define TestAccessNestedMap class
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected_result):
        """
        Test the access_nested_map function
        """
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_result)


    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected_exception):
        """
        Test that accessing a non-existent key raises a KeyError
        """
        with self.assertRaises(expected_exception) as context:
            access_nested_map(nested_map, path)

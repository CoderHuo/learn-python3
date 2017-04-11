#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from versionCompare import version_compare

__author__ = 'Mr.Huo'


class TestVerCmp(unittest.TestCase):
    def test_version_length_equal_element_have_same_length_list(self):
        """测试长度相等"""
        v1 = '10.1a'
        v2 = '10.2a'
        v3 = '10.2b'
        v4 = '10.b1'
        v5 = '.1'
        v6 = '.a'
        v7 = 'a.2'
        self.assertEqual(version_compare(v1, v1), 0)
        self.assertEqual(version_compare(v1, v2), -1)
        self.assertEqual(version_compare(v2, v1), 1)
        self.assertEqual(version_compare(v3, v4), -1)
        self.assertEqual(version_compare(v5, v5), 0)
        self.assertEqual(version_compare(v5, v6), -1)
        self.assertEqual(version_compare(v5, v7), -1)
        self.assertEqual(version_compare(v7, v5), 1)

    def test_version_length_equal_element_have_unequal_length_list(self):
        v1 = '10.11a'
        v2 = '10.1a20'
        v3 = '10.0b'
        v4 = '10.0b1'
        self.assertEqual(version_compare(v1, v2), 1)
        self.assertEqual(version_compare(v2, v1), -1)
        self.assertEqual(version_compare(v3, v4), -1)
        self.assertEqual(version_compare(v4, v3), 1)

    def test_length_unequal(self):
        """测试长度不相等"""
        v1 = '1.2'
        v2 = '1'
        self.assertEqual(version_compare(v1, v2), 1)
        self.assertEqual(version_compare(v2, v1), -1)

    def test_empty(self):
        """测试空"""
        v1 = ''
        v2 = '1'

        with self.assertRaises(RuntimeError):
            version_compare(v1, v2)
        with self.assertRaises(RuntimeError):
            version_compare(v2, v1)
        with self.assertRaises(RuntimeError):
            version_compare(v1, v1)

if __name__ == '__main__':
    unittest.main()
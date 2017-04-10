#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from .versionCompare import version_compare

__author__ = 'Mr.Huo'


class TestVerCom(unittest.TestCase):

    def setUp(self):
        self.v1 = ''
        self.v2 = '10'
        self.v3 = '11'
        self.v4 = 'ab'
        self.v5 = 'ac'
        #self.v6 = '12ab'
        #self.v7 = '1ab'
        self.v7 = '12ab1'
        self.v5 = '.10'
        self.v6 = '.ab'
        self.v7 = '.ab12'
        self.v8 = '12ab.'
        self.v9 = '1abc.0'
        self.v10 = '2ab.A'
        self.v11 = '11a2.1a'

    def test_two_version_length_equal_v1_v2_element_have_same_length_list(self):
        """测试长度相等"""
        self.assertEqual(version_compare(self.v1, self.v1), 0)
        self.assertEqual(version_compare(self.v1, self.v2), -1)
        self.assertEqual(version_compare(self.v2, self.v1), 1)
        self.assertEqual(version_compare(self.v3, self.v4), -1)
        self.assertEqual(version_compare(self.v5, self.v5), 0)
        self.assertEqual(version_compare(self.v5, self.v6), -1)

    def test_two_version_length_equal_v1_v2_element_have_unequal_length_list(self):
        v1 = '1.2b2c'
        v2 = '1.2B1'
        v3 = '1.'
        self.assertEqual(version_compare(v1, v2), 1)
        self.assertEqual(version_compare(v2, v1), -1)
        self.assertEqual(version_compare(v1, v3), 1)
        self.assertEqual(version_compare(v3, v1), -1)

    def test_length_unequal(self):
        """测试长度不相等"""
        v1 = '1.2.3'
        v2 = '1'
        self.assertEqual(version_compare(v1, v2), 1)
        self.assertEqual(version_compare(v2, v1), -1)

    def test_empty(self):
        """测试长度为空"""
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

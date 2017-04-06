#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from .versionCompare import version_compare

__author__ = 'Mr.Huo'


class TestVerCom(unittest.TestCase):
    def test_equal(self):
        """测试长度相等"""
        v1 = '1a'
        v2 = '1a'
        self.assertEqual(version_compare(v1, v2), 0)
        v1 = '1.2.2.a'
        v2 = '1.2.2.b'
        self.assertEqual(version_compare(v1, v2), -1)

    def test_unequal(self):
        """测试长度不相等"""
        v1 = '1.2.3'
        v2 = '1'
        self.assertEqual(version_compare(v1, v2), 1)
        v1 = '1'
        v2 = '1.2.3'
        self.assertEqual(version_compare(v1, v2), -1)

    def test_empty(self):
        """测试长度为空"""
        v1 = ''
        v2 = ''
        self.assertRaises(RuntimeError)
        v1 = '1-'
        v2 = ''
        self.assertRaises(RuntimeError)
        v1 = ''
        v2 = '-'
        self.assertRaises(RuntimeError)
        v1 = '1.1..1.-.'
        v2 = '1.1..1.-.'
        self.assertEqual(version_compare(v1, v2), 0)

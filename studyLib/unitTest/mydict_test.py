#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import sys

__author__ = 'Mr.Huo'

print(sys.path)
from .mydict import MyDict


class TestMyDict(unittest.TestCase):
    def test_init(self):
        d = MyDict(a=1, b='test', test=2)
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, 'test')
        self.assertEqual(d.test, 2)
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = MyDict()
        d['key'] = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d.key, 'value')

    def test_attr(self):
        d = MyDict()
        d.key = 'value'
        self.assertTrue('key' in d)
        self.assertEqual(d['key'], 'value')


if __name__ == '__main__':
    unittest.main()

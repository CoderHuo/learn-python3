#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib

__author__ = 'Mr.Huo'


class MyHash(object):
    def __init__(self, file='', alg='md5'):
        if file:
            with open(file, 'rb') as fp:
                data = fp.read()
            if alg in ('MD5', 'md5'):
                self.alg = hashlib.md5()
                self.alg.update(data)
            elif alg in ('SHA256', 'sha256'):
                self.alg = hashlib.sha256()
                self.alg.update(data)
        else:
            if alg in ('MD5', 'md5'):
                self.alg = hashlib.md5()
            elif alg in ('SHA256', 'sha256'):
                self.alg = hashlib.sha256()

    def get_hexdigest(self):
        return self.alg.hexdigest()

    def __str__(self):
        return self.alg.hexdigest()

    def update(self, data):
        self.alg.update(data)


def main():
    s1 = '擎天柱'
    md5 = hashlib.md5()
    md5.update(s1.encode(encoding='utf-8'))
    print(md5.hexdigest())

    myhash1 = MyHash(file='bmptest.bmp')
    print(myhash1)
    myhash2 = MyHash(file='bmptest.bmp', alg='sha256')
    print(myhash2)
    myhash2.update("擎天柱".encode())
    print(myhash2)
    myhash3 = MyHash(alg='sha256')
    print(myhash3)
    sha256 = hashlib.sha256()
    print(sha256.hexdigest())
    pass


if __name__ == '__main__':
    main()

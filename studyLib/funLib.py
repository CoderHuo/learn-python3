#!/usr/bin/env python3
# coding: utf-8

def Hanoi_Move(n, a='a', b='b', c='c'):
    if (n == 1):
        print(a, "-->", c)
        return
    Hanoi_Move(n - 1, a, c, b)
    print(a, "-->", c)
    Hanoi_Move(n - 1, b, a, c)

def main():
    Hanoi_Move(10)

if __name__ == '__main__':
    main()
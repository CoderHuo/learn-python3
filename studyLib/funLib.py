def Hanoi_Move(n, a, b, c):
    if (n == 1):
        print(a, "-->", c)
        return
    Hanoi_Move(n - 1, a, c, b)
    print(a, "-->", c)
    Hanoi_Move(n - 1, b, a, c)

if __name__ == '__main__':
    Hanoi_Move(10, 'a', 'b', 'c')

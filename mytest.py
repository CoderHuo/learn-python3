somelist = [3, 2, 2, 3]

y = somelist


def delete(list):
    print(list[:])
    print(1, id(list))
    list[:] = [x for x in list if x != 3]

    print(list[:])
    print(2, id(list))
    print("func:", list)


print(3, id(somelist))
delete(somelist)
print(somelist)
print(4, id(somelist))
print(y)
somelist[0] = 1
print(y)

print(5, id(y))

print(len(b'INVITE sip:bob@biloxi.com SIP/2.0\r\n'
          b'Via: SIP/2.0/UDP server10.biloxi.com;branch=z9hG4bKnashds8\r\nMax-Forwards: 70\r\n'
          b'To: Bob <sip:bob@biloxi.com>;tag=a6c85cf\r\n'
          b'From: Alice <sip:alice@atlanta.com>;tag=1928301774\r\n'
          b'Call-ID: a84b4c76e66710@pc33.atlanta.com\r\n'
          b'CSeq: 314159 INVITE\r\n'
          b'Contact: <sip:bob@192.0.2.4>\r\n'
          b'Content-Type: application/sdp\r\n'
          b'Content-Length: 0\r\n\r\n'))
data = b"""INVITE sip:bob@biloxi.com SIP/2.0\r
Via: SIP/2.0/UDP server10.biloxi.com;branch=z9hG4bKnashds8\r\nMax-Forwards: 70\r
To: Bob <sip:bob@biloxi.com>;tag=a6c85cf\r
From: Alice <sip:alice@atlanta.com>;tag=1928301774\r
Call-ID: a84b4c76e66710@pc33.atlanta.com\r
CSeq: 314159 INVITE\r
Contact: <sip:bob@192.0.2.4>\r
Content-Type: application/sdp\r
Content-Length: 0\r\n\r\n"""
print(len(data))
print(data)
print(data[-1])
print(data[-22])
print(data[-21])
print(data[-23])
print(type(data))
print(bytes([x for x in range(256)]))
print(bytes.fromhex("7b 7d"))


class A:
    def __init__(self):
        print('A__init__run')

    def serve_forever(self):
        self.A()

    def A(self):
        print('AAA')


class B(A):
    def __init__(self):
        A.__init__(self)
        print('B__init__run')

    def A(self):
        print('BBB')


class C:
    def __init__(self):
        print('C__init__run')

    def A(self):
        print('CCC')


class F(B, C, A):
    pass


class D(B, C):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)

    pass


class E(B, C, A):
    def __init__(self):
        super().__init__()


split_str = '----------' * 3
print(split_str)
d = D()
print(split_str)
d.A()
print(split_str)
d.serve_forever()
print(split_str)
e = E()
print(split_str)
e.serve_forever()

print('-' * 100)
i, j = 1, 100
guess_num = int(input("Please enter a integer from 1 to 100: "))
guess_times = int(input("Please enter the number to guess: "))
counter = 1

import random

while counter <= guess_times:
    counter += 1
    print('I J ', i, j)
    num = random.randint(i, j)
    if num == guess_num:
        print("guess right,the number is:", num)
        break
    elif num > guess_num:
        print("the number(%s) is biger." % num)
        j = num
    elif num < guess_num:
        print("the number(%s) is smaller." % num)
        i = num
    pass


class Name:
    name = 'huo'

    def __init__(self, name=None):
        if name is not None:
            self.name = name

        print("name", name)
        print("self.name", self.name)


name = Name()
print(name.name)
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
        print('A__init__')

    def serve_forever(self):
        self.A()

    def A(self):
        print('AAA')


class B(A):
    def __init__(self):
        print('B__init__ run')


class C:
    def __init__(self):
        print('C__init__ run')

    def A(self):
        print('CCC')


class D(C, B):
    def __init__(self):
        C.__init__(self)
        B.__init__(self)
    pass


d = D()
d.A()
d.serve_forever()

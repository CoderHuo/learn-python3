somelist = [3,2,2,3]

y=somelist

def delete(list):
    print(list[:])
    print(1,id(list))
    list[:] = [x for x in list if x !=3]

    print(list[:])
    print(2,id(list))
    print("func:",list)

print(3,id(somelist))
delete(somelist)
print(somelist)
print(4,id(somelist))
print(y)
somelist[0] =1
print(y)

print(5,id(y))


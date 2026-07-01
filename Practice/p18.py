a , *b = 1,2,3,4,5
print(type(b))

def ok(*c):
    print(type(c))

ok(1,2,3,3)
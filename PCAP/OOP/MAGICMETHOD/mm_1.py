class A:

    x=0
    def __init__(self):
        self.x = A.x
    def __str__(self):
        return "str"
    def __repr__(self):
        return 'repr'

class B:
    y=0

class C:

    def __repr__(self):
        return 'defaulted'

a = A()
b = B()
c = C()

print(str(a))
print(str(b))
print(str(c))

print(repr(a))
print(repr(b))

print(str("asdf"))
print(str(True))
print(str(-1))
z = str()
print(type(z))

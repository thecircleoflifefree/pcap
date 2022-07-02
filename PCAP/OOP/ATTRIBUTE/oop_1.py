class A():
    pass

class B():
    Var = 2
    _kar = 5
    __jar = 'jar'

class C():
    def __init__(self):
        self.foo=4

class D():
    Var = 'asdf'
    def __init__(self):
        pass

a = A()
b = B()
c = C()
d = D()

print("dir(a) -> ", dir(a))
print("dir(A) -> ", dir(A))
print("dir(b) -> ", dir(b))
print("dir(B) -> ", dir(B))
print("dir(c) -> ", dir(c))
print("dir(C) -> ", dir(C))
print("dir(d) -> ", dir(d))
print("dir(D)-> ", dir(D))

class x():
    Var = 2
    _kar = 5
    __jar = 'jar'
    def __init__(self,foo):
        self.foo = foo
    def somemethod(self):
        pass

z = x(5)

print("x.__class__ ->", x.__class__)
print("z.__class__ ->", z.__class__)
print()
try:
    print("dict(x) -> ", dict(x))
    print("dict(z) -> ", dict(z))
except Exception as e:
    print("EXCEPTION -> ",e)
print()
print("x.__dict__ -> ", x.__dict__)
print("z.__dict__ -> ", z.__dict__)
print()
print("dir(x) -> ", dir(x))
print("dir(z) -> ", dir(z))
print()
print("x.__dir__ -> ", x.__dir__)
print("z.__dir__ -> ", z.__dir__)
print()
print("x.__doc__ -> ", x.__doc__)
print("z.__doc__ -> ", z.__doc__)

print("x.__repr__ -> ", x.__repr__)
print("z.__repr__ -> ", z.__repr__)

print("x.__module__, -> ", x.__module__,)
print("z.__module__, -> ", z.__module__,)

print("x.__str__, -> ", x.__str__,)
print("z.__str__, -> ", z.__str__,)
#__dict__', '__dir__', '__doc__', __repr__' ,__module__, '__str__',


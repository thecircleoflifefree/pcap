class __Z():
    __foo = "foo"

z = __Z()


print("z.__class__ ->", z.__class__)
print("z.__dict__ -> ", z.__dict__)
print("z.__dir__ -> ", z.__dir__)
print("z.__doc__ -> ", z.__doc__)
print("z.__repr__ -> ", z.__repr__)
print("z.__module__, -> ", z.__module__)
print("z.__str__, -> ", z.__str__)
print()
print("__Z.__class__ ->", __Z.__class__)
print("__Z.__dict__ -> ", __Z.__dict__)
print("__Z.__dir__ -> ", __Z.__dir__)
print("__Z.__doc__ -> ", __Z.__doc__)
print("__Z.__repr__ -> ", __Z.__repr__)
print("__Z.__module__, -> ", __Z.__module__)
print("__Z.__str__, -> ", __Z.__str__)

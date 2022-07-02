class __Z():
    foo = "foo"

class X():
    foo = "foo"

z = __Z()
x = X()

print("Z.__dict__ -> ", __Z.__dict__)
print("X.__dict__ -> ", X.__dict__)


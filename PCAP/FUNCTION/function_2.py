try:
    def foo(a, b=a):
        print("a ->", a)
        print("b ->", b)
except Exception as e:
    print("asdf")

def var(x=1,y=x):
    print(x)

var(3)

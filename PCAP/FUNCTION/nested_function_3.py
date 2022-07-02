x = 9

def foo(x):
    print("foo:x -> ", x)
    x+=x
    def bar(x):
        print("bar:x -> ", x)
        return x * x
    return bar

a = foo(3)
print(a)
try:
    print(a())
except Exception as e:
    print("EXCEPTION RAISED FROM TRY SCOPE-> ", e)
    print(a(2))

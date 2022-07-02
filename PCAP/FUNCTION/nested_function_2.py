def foo(y):
    print("foo:y -> ", y)
    def bar(x):
        print("bar:x -> ", x)
        return x * y
    return bar

a = foo(3)
print(a)
try:
    print(a())
except Exception as e:
    print("EXCEPTION RAISED FROM TRY SCOPE-> ",e)
    print(a(2))

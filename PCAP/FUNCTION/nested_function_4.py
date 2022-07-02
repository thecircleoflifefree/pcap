x = 9

def x(x):
    print("outer x:x -> ", x)
    x+=x
    def x(x):
        print("nested x:x -> ", x)
        return x * x
    return x

x = x(3)
print(x)
try:
    print(x())
except Exception as e:
    print("EXCEPTION RAISED FROM TRY SCOPE-> ", e)
    print(x(2))

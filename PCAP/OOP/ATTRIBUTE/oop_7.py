class E:
    def __init__(self, __s):
        self.a = __s

e= E(10000)
print("e -->", e)
print("e.a -->", e.a)

try:
    print("try scope: e --> ", e.p)
except Exception as e:
    print("EXCEPTION! asdf")

print("e --> ", e)

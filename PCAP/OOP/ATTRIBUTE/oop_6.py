class E:
    def __init__(self, __s, __a):

        self.__s = __s
        self.a = __a

# creating object of a class
e= E(100,4)

print("e.a -->", e.a)
print("e.__dir__  -->", e.__dir__)
print("E.__dir__  -->", E.__dir__)
print("e.__dict__ -->", e.__dict__)
print("e._E__s -->", e._E__s)


try:
    print("try scope: e --> ", e)
except Exception as e:
    print("EXCEPTION! asdf")
try:
    print(e.__s)
except Exception as e:
    print("EXCEPTION! e.__s  -->", e)

try:
    print(e._E__a)
except Exception as e:
    print("EXCEPTION! e._E__a  -->", e)
try:
    print("e-->", e)
except Exception as r:
    print("EXCEPTION! r -->", r)

print("final e --> ", e)

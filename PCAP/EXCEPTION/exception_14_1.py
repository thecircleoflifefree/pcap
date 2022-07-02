# EXCEPTION CASE 14_1
try:
    print("try scope")
    raise Exception
except BaseException:
    print("base_exception_1")
    2/0
except BaseException:
    print("base_exception_2")
else:
    print("foo")
finally:
    print("no matter what")

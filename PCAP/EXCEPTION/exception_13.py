# EXCEPTION CASE 13
try:
    raise
except BaseException:
    print("base_exception_1")
except BaseException:
    print("base_exception_2")
else:
    print("foo")
finally:
    print("no matter what")

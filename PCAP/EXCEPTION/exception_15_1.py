# EXCEPTION CASE 15
try:
    print("try scope")
    raise Exception
except BaseException:
    print("base_exception_1")
    try:
        2/0
    except ZeroDivisionError:
        print("nested except err")
except BaseException:
    print("base_exception_2")
else:
    print("foo")
finally:
    print("no matter what")

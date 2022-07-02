# EXCEPTION CASE 17
try:
    print("try scope")
    raise
except BaseException:
    print("base_exception_1")
    try:
        2/0
    except ZeroDivisionError:
        print("nested except err")
        raise
    finally:
        print("nested finally")
except BaseException:
    print("base_exception_2")
else:
    print("foo")
finally:
    print("no matter what")

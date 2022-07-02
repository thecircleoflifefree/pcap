# EXCEPTION CASE 10
try:
    2/0
    raise
except ZeroDivisionError:
    print("zerodivisionerr")
    raise
except ArithmeticError:
    print("aritmeticerr")
except:
    print("net")
else:
    print("foo")

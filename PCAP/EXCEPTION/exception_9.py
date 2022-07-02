# EXCEPTION CASE 9
try:
    2/0
except ArithmeticError:
    print("aritmeticerr")
    raise
except ZeroDivisionError:
    print("zerodivisionerr")
except:
    print("net")
else:
    print("foo")

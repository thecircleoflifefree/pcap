# EXCEPTION CASE 8
try:
    2/0
except ArithmeticError:
    print("aritmeticerr")
except ZeroDivisionError:
    print("zerodivisionerr")
except:
    print("net")
else:
    print("foo")

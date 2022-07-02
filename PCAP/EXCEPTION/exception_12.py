# EXCEPTION CASE 12
try:
    raise
except:
    print("net2")
except BaseException:
    print("net1")
else:
    print("foo")
finally:
    print("no matter what")

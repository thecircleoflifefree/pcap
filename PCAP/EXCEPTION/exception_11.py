# EXCEPTION CASE 11
try:
    raise
except:
    print("net1")
except:
    print("net2")
else:
    print("foo")
finally:
    print("no matter what")

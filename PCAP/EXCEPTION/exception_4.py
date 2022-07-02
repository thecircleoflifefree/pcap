# EXCEPTION CASE 4
try:
    pass
    raise
except Exception:
    print("foovar-->",e)
    pass
except:
    print("net")
else:
    print("foo")
    pass

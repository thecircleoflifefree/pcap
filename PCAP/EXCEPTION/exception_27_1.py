# EXCEPTION CASE 27_1
try:
    print("try scope")
    raise
except:
    continue
    print("exception")
else:
    print("no exception found")
finally:
    print("finally....")

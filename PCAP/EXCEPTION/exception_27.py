# EXCEPTION CASE 27
try:
    continue
    print("try scope")
    raise
except:
    print("exception")
else:
    print("no exception found")
finally:
    print("finally....")

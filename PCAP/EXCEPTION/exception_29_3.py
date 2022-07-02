# EXCEPTION CASE 29_3
try:
    x = 9
    raise
except:
    print("exception")
    raise
else:
    raise
    print("no exception found")
finally:
    raise
    print("final output")

print(x)

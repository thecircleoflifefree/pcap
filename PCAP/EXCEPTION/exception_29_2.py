# EXCEPTION CASE 29_2
try:
    x = 9

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

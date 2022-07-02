# EXCEPTION CASE 30

try:
    4/0
    open("foovar", mode='rw')
except Exception as e:
    print(e)

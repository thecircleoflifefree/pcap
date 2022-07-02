#open("new_file.txt", mode='x')

try:
    open("existing_file.txt", mode='x')
except Exception as e:
    print(e)

try:
    open("non_existing_file.txt", mode='xr')
except Exception as e:
    print(e)
try:
    open("non_existing_file.txt", mode='xw')
except Exception as e:
    print(e)

try:
    open("non_existing_file.txt", mode='xa')
except Exception as e:
    print(e)

try:
    open("non_existing_file.txt", mode='xa')
except Exception as e:
    print(e)

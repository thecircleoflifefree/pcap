try:
    f1 = open("file_1.py", mode='b')
except Exception as e:
    print(e)

try:
    f2 = open("file_5.py", mode='bt')
except Exception as e:
    print(e)

try:
    f3 = open("file_5.py", mode='b+')
except Exception as e:
    print(e)

f4 = open("file_1.py", mode='br')
f5 = open("file_1.py", mode='bw')
f6 = open("file_1.py", mode='bw+')

f7 = open("file_1.py", mode='br+')

print(f4)
print(f5)
print(f6)
print(f7)

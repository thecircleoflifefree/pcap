f1 = open("file_4.py")
f2 = open("file_1.py", mode='r')
f3 = open("file_2.py", mode='rt')

try:
    f4 = open("file_2.py", mode='rw')
except Exception as e:
    print(e)
try:
    f5 = open("file_6.py", mode='ra')
except Exception as e:
    print(e)

f6 = open("file_6.py", mode='r+')
f7 = open("file_1.py", mode='rb+')


print(f1)
print(f2)
print(f3)
print(f6)
print(f7)

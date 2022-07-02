print('a' > "a")
print('a' < "b")
print('a' > "b")
try:
    print('a' > 1)
except Exception as e:
    print(e)
    try:
        print(1 > "x")
    except Exception as e:
        print(e)

print("len('a') >= 1 -> ", len('a') >= 1)
print("'a' > str(1) -> ", 'a' > str(1))
print("'a' >= str(1) -> ", 'a' >= str(1))
print("'a' > str(1234567890) -> ", 'a' > str(1234567890))
print("'a' < str(1234567890) -> ", 'a' < str(1234567890))
print("'a' >= str(1234567890) -> ", 'a' >= str(1234567890))

print("'a' > 'A' -> ", 'a' > 'A')
print("'a' >= 'A' -> ", 'a' >= 'A')

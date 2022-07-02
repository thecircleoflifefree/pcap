try:
    print('a' & "a")
except Exception as e:
    print(e)

print("'a' and \"a\" -> ", 'a' and "a")
print("'a' and \"b\" -> ", 'a' and "b")
print("'a' and \"A\" -> ", 'a' and "A")

print("'a' and 1 -> ", 'a' and 1)
print("1 and \"a\" -> ", 1 and "a")
print("'$' and \"#\" -> ", '$' and "#")

print("1 and 0 -> ", 4 and 0)
print("0 and 1 -> ", 0 and 2)

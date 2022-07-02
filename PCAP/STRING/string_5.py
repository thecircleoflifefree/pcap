try:
    print('a' | "a")
except Exception as e:
    print(e)

print("'a' or \"a\" -> ", 'a' or "a")
print("'a' or \"b\" -> ", 'a' or "b")
print("'a' or \"A\" -> ", 'a' or "A")

print("'a' or 1 -> ", 'a' or 1)
print("1 or \"a\" -> ", 1 or "a")
print("'$' or \"#\" -> ", '$' or "#")

print("1 ord 0 -> ", 4 or 0)
print("0 or 1 -> ", 0 or 2)

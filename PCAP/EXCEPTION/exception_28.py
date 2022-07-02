def foo():
    try:
        return True
    finally:
        return False

def bar():
    try:
        return True
    else:
        return False

print(foo())
print(bar())

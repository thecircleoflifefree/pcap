# single line comment

"""
multiline
string which CAN be used for comments
if not used for function or class
"""

"some string floating"

#some floating variable
7

empty_st1 = ""
print("empty_st length -> ", len(empty_st1))
empty_st2 = ''
print("empty_st2 length -> ", len(empty_st2))

x = """
"""
print("x length -> ", len(x))

x1 = """
hi!"""
print("x1 length -> ", len(x1))

#four doble quotes will comment everything below
#y = """"
#print("y length ->", len(y))

#six doble quotes
y = """"""
print("y length ->", len(y))

# twelve doble quotes
y1 = """"""""""""
print("y1 length ->", len(y1))

y2 = """"""""
print("y2 length ->", len(y2))

y3 = """''"""
print("y3 length ->", len(y3))

w = """ """
print("w length ->", len(w))

z = """\n"""
print("z length ->", len(z))



if 0:
    print("0")
else:
    print("if 0 -> false")

if 1:
    print("1")
else:
    print("if 1 -> false")

if -1:
    print("-1")
else:
    print("if -1 is eval as false")

if not 0:
    print("not 0 --> false is negated, hence true")
else:
    print("not 0 --> if 0 is eval as false")

if 0 != 0:
    print("0 != 0 --> true")
else:
    print("0 != 0 --> are in fact the same")

if 0 != False:
    print("0 != False --> true")
else:
    print("0 != False --> false")

if 0 is not False:
    print("0 is not False--> zero is indeed falsy")
else:
    print("0 is not False--> zero would be truthly")

if 0 is False:
    print("0 is False--> zero is indeed falsy")
else:
    print("0 is False--> zero would be truthly")

not False
not True

if True is not False:
    print("True is not False --> true")
else:
    print("True is not False--> false")

if True is not True:
    print("True is not True --> true")
else:
    print("True is not True--> false")

true_var= True

if true_var is not True:
    print("true_var is not True --> true")
else:
    print("true_var is not True--> false")

if not 0 is not False:
    print("not 0 is not False --> true")
else:
    print("not 0 is not False --> false")



# != : compares the value or equality of two objects,
# is not : checks whether two variables point to the same object in memory.

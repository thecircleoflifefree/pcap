class A():
    Var = 1
    def __init__(self,x):
        A.Var += 1
        self.prop = x + A.Var

obj1 = A(2)
print(obj1.prop , obj1.Var)
print(A.Var)
obj2 = A(2)
print(obj2.prop , obj2.Var)
print(A.Var)

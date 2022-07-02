class A():
    Var = 1
    def __init__(self,x):
        self.x = x
        self.prop = self.x + A.Var

obj1 = A(2)
print(obj1.x , obj1.prop , obj1.Var)
print(A.Var)

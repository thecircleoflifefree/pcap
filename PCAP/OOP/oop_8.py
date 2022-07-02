class A():
    Var = 0
    def __init__(self,x):
        self.x = x
        self.prop = self.x + Var

obj1 = A(2)
print(obj1.x)

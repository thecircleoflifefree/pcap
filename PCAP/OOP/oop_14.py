class A():
    Var = 1
    Ver = 5
    def __init__(self,x):
        self.x = x
        self.Var = self.x + A.Var

a = A(2)
print(a.Var)
print(A.Var)
print(a.Ver)

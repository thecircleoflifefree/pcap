class A():
    Var = 1
    def __init__(self,x):
        A.Var += 1
        self.prop = x + A.Var
    def showVar(self):
        print(self.Var)

ob=A(2)
print(ob.showVar())

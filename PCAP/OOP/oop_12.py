class A():
    Var = 1
    def __init__(self,x):
        A.Var += 1
        self.prop = x + A.Var

class B(A):
    Var = 3
    def __init__(self,x):
        A.Var += 1
        self.prop = x + A.Var
    def showVar(self):
        print(self.Var)


ob=B(2)
print(ob.showVar())
#print(ob.getVar())

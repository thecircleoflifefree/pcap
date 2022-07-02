class Employee:

    name=""
    def __init__(self, name, salary):

        self.__salary = salary

    def show(self):
        print("Name: ", self.name)

    def show_2(self):
        print("Name: ", name)


# creating object of a class
emp = Employee('Jessa', 10000)
emp.show()
#emp.show_2()

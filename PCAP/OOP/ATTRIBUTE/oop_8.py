class Employee:

    def __init__(self, name, salary):

        self.name = name
        self.__salary = salary

    def show(self):
        print("Name: ", self.name, 'Salary:', self.__salary)

    def show_2(self):
        print(name)

    def show_3(self):
        print("show_2--> Name: ", self.name, 'Salary:', Employee.__salary)

# creating object of a class
emp = Employee('Jessa', 10000)
emp.show()
emp.show_2()

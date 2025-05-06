
# **** ____________________ Assigment 20______________***

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def display(self):
        print(f"Employee Name: {self.name}, Position: {self.position}")


class Department:
    def __init__(self, department_name, employee):
        self.department_name = department_name
        self.employee = employee 

    def show_department(self):
        print(f"Department: {self.department_name}")
        self.employee.display()  


e1 = Employee("zainab", "Artifical inteligence")

d1 = Department("IT", e1)


d1.show_department()

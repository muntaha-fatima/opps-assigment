# **** ____________________ Assigment 8______________***

class Person:
    def __init__(self, name):
        
        self.name = name 
        print(f"Person created: {self.name}")


class Teacher(Person):

    def __init__(self, name, subject):
        super().__init__(name)  

        self.subject = subject
        print(f"Teacher of: {self.subject}")

t1 = Teacher("Miss Sana", "Islamiat")





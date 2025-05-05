
class Dog:

    def __init__(self, name, breed):

        self.name = name  

        self.breed = breed   

    def bark(self):            
        print(f"{self.name} is barking! Woof woof 🐶")

d1 = Dog('tomy', 'labrador')

d1.bark()
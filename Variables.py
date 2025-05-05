

class Car:
   
    brand = "Toyota"
    
    def start(self): 
        print(f"{self.brand} car is starting!")

my_car = Car()

print(my_car.brand) 

my_car.start() 



# def add_greeting(cls):
#     def greet(self):
#         return f"Hello {self.name} Decorator!"
#     cls.greet = greet
#     return cls

# @add_greeting
# class Person:
#     def __init__(self, name):
#         self.name = name


# p = Person("Amna")
# print(p.greet())

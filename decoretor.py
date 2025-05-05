def add_greeting(cls):
    def greet(self):
        return f"Hello {self.name}, from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name
p = Person("seerat fatima")
print(p.greet())

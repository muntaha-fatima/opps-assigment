
class Student:

    def __init__(self, name, marks):
       
       self.name=name
       self.marks=marks

    def display(self):
           print(f'Name:{self.name}, Marks:{self.marks}')

s1 = Student('seerat',95)

s1.display()


# class Product:
#     def __init__(self, price):
#         self._price = price  

#     @property
#     def price(self):
#         return self._price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             print("Price negative nahi ho sakta!")
#         else:
#             self._price = value

#     @price.deleter
#     def price(self):
#         print("Price delete kiya gaya.")
#         del self._price

# p = Product(100)

# print(p.price)      

# p.price = 200       
# print(p.price)      

# p.price = -50       


# del p.price        


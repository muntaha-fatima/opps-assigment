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




# class Countdown:
#     def __init__(self, start):
#         self.start = start

#     def __iter__(self):
#         self.current = self.start
#         return self

#     def __next__(self):
#         if self.current < 0:
#             raise StopIteration
#         else:
#             num = self.current
#             self.current -= 1
#             return num


# cd = Countdown(5)

# for num in cd:
#     print(num)

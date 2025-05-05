
class Mathutils:

    @staticmethod

    def add(a,b):
        return a + b
    
print(Mathutils.add(5,3))

m = Mathutils()

print(m.add(10,15))




# class InvalidAgeError(Exception):
#     pass


# def check_age(age):
#     if age < 18:
#         raise InvalidAgeError("Age must be at least 18.")
#     else:
#         print("Access granted.")


# try:
#     user_age = int(input("Enter your age: "))
#     check_age(user_age)
# except InvalidAgeError as e:
#     print("InvalidAgeError:", e)

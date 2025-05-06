
# **** ____________________ Assigment 18______________***

class Multiplier:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, value):
        return self.factor * value


times3 = Multiplier(3)

print(callable(times3))


print(times3(5))      

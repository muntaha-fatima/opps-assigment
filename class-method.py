



# **** ____________________ Assigment 17______________***

class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            num = self.current
            self.current -= 1
            return num


cd = Countdown(5)

for num in cd:
    print(num)

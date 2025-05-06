
# **** ____________________ Assigment 14______________***

class Engine:
    def start(self):
        print("Engine started!")

class Car:
    def __init__(self, engine):
        self.engine = engine  

    def start_car(self):
        print("Car starting...")
        self.engine.start()

e = Engine()        
c = Car(e)   

c.start_car()       



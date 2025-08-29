class Car:
    @staticmethod
    def Start():
        print("Car Started")

    @staticmethod
    def Stop():
        print("Car Stopped")

class Toyota_car(Car):
    def __init__(self,name,brand):
        self.name = name
        self.brand = brand

class Fortuner(Toyota_car):
    def __init__(self,type):
        self.type = type

car = Fortuner("Brand")
car = Toyota_car("Toyota","Ty")
car.Start()
print(car.name)

class A:
    varA = "This is A"

class B:
    varB = "This is B"

class C(A,B):
    varC = "This is C"

caa = C()
print(caa.varA)
print(caa.varB)
print(caa.varC)


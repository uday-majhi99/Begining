class Car:
    car_color = "Red"
    @staticmethod
    def Start():
        print("Car Started")

    @staticmethod
    def Stop():
        print("Car Stopped")

class Ford(Car):
    def __init__(self,name):
        self.name = name

car = Ford
Ford.Start()
print(car.car_color)
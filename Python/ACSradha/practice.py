class Car():
    def __init__(self):
        self.acc = False
        self.clutch = False
        self.brk = False

    def Start(self):
        self.acc = True
        self.clutch = True
        print("Car Started Successfully")

car = Car()
car.Start()

class Account():
    def __init__(self,acc,bal,name):
        self.name = name
        self.acc = acc
        self.bal = bal

    def debitted(self,amount):
        self.bal -= amount
        print(f"{account.name}  Your account is debitted by {amount} Your Current Balance is {self.bal}")

    def creditted(self,amount):
        self.bal += amount
        print(f"{account.name}  Your account is creditted by {amount} Your Current Balance is {self.bal}")

account = Account(123456,10000, "Uday")
account.creditted(100)
account.debitted(100)
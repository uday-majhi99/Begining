# Abstraction is the hiding implementation detail of class nd only showing the essential features to the user
#Encapsulation is the wrapping data and function into single unit (Object)

class Car():
    def __init__(self):
        self.acc = False
        self.brek = False
        self.clutch = False

    def Start(self):
        self.clutch = True
        self.acc = True
        print("Car started successfully")


c1 = Car()
c1.Start()

class Account():
    def __init__(self, account_number, balance, name):
        self.account_number = account_number
        self.balance = balance
        self.name = name

    def debit(self,amount):
        self.balance -= amount
        print(f"{ac1.name} Your account is debited by ", amount)
        print("Now your balance is", self.balance)

    def credit(self,amount):
        self.balance += amount
        print(f"{ac1.name} Your account is credited by ", amount)
        print("Now your balance is", self.balance)

    def get_balance(self):
        return ac1.balance

ac1 = Account(123456789,100000,"Tony")
print(f"{ac1.name} your account balance is ",ac1.balance)
print(f"{ac1.name} your account number is ",ac1.account_number)

ac1.debit(200)
ac1.credit(300)
ac1.credit(100000000)
ac1.debit(10)
# ac1.get_balance()



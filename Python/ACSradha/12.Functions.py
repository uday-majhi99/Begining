"""
Block of statements that perform a specific task.
def func_name(param1,param2):(Defining function)
    some_work
    return value

def func_name(arg1,arg2) - Function call
"""


def sum_calc(a,b):
    return a+b

sums = sum_calc(2,3)
print(sums)

def func():
    return "Hello"

functi = func()
print(functi)

def add_all(*args):
    return sum(args)

print(add_all(1, 2, 3, 4))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

print_info(name = "Uday Majhi", age = 27)

def infor(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} = {value}")

infor(city = "Biratnagar", Zone = "Koshi", Village = "Sakhuware")
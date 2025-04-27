#WAP to check if a number entered by a user is odd or even
number = int(input("Enter a number : "))


if number % 2 == 0:
    print(f"{number} is a odd number")

else:
    print(f"{number} is even")

numb1 = int(input("Enter a first number : "))
numb2 = int(input("Enter a second number : "))
numb3 = int(input("Enter a third number : "))

if numb1 > numb2 and numb1 > numb3:
    print(f"{numb1} is the greatest number")

elif numb2 > numb3 and numb2 > numb1:
    print(f"{numb2} is the greatest number")

else:
    print(f"{numb3} is the greatest number")

multiple_seven = int(input("Enter a number : "))

if multiple_seven % 7 == 0:
    print(f"{multiple_seven} is the multiple of 7")
else:
    print(f"{multiple_seven} is not a multiple 7")
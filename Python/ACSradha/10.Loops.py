# """
# Loops are used to repeat instructions
# While loops:
# """
# count = 1
# while count <= 10:
#     print("Hello")
#     count = count + 1
#
# print(count)
#
# for i in range(5):
#     print("Hello World")
#
# user_input = input("Enter Something :")
# for i in range(5):
#     print(user_input)
#
# i = 4
# for i in range(10):
#     print(i)
#     i = i + 1

# i = 1
# while i <=100:
#     print(i)
#     i = i + 1
# j = 100
# while j >=1:
#     print(j)
#     j = j - 1

# multi = int(input("Enter a number for multiplication"))
# i = 1
# while i <= 10:
#     print(multi*i)
#     i = i + 1

# i = 1
# squares = []
# while i <=10:
#     print(i*i)
#     squares.append(i*i)
#     i = i + 1
#
# tup = tuple(squares)
# print(tup)
#
# inputs = int(input("Enter a number: "))
# while True:
#     if inputs in tup:
#         print(f"Searching your {inputs}")
#         print(f"It has {inputs}")
#         break
#     else:
#         print(f"{inputs} is not in a tuple")
#         break
#
# num = int(input("Enter a number to match  with the tuple:"))
# i = 0  # Start from index 0
#
# found = False
#
# while i < len(tup):
#     if tup[i] == num:
#         print(f"{num} is found at index: {i}")
#         found = True
#         break
#     else:
#         print("Searching.....")
#     i = i + 1
#
# if not found:
#     print(f"{num} is not found in the tuple.")

#For
"""
For loop is used for sequential traversal. For traveling the list,string,tuple,etc
for el in list :
    Some work

Example : List  = [1,2,3]
for el in list :
    print(el)

For loop with else
for el in list:
    Some work
else:
    Work when loop ends

Example:
    for el in list:
        print(el)
    else:
        print("End")
"""



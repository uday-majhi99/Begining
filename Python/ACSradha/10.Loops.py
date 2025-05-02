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

i = 1
squares = []
while i <=10:
    print(i*i)
    squares.append(i*i)
    i = i + 1

tup = tuple(squares)
print(tup)

inputs = int(input("Enter a number: "))
while inputs in tup:
    print(f"It has {inputs}")
    print(f"Finding")
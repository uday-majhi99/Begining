# squares = []
#
# for i in range(1,11):
#     squares.append(i*i)
#
# print(f"List of elements is ",squares)
# squaress = tuple(squares)
# print(f"List of elements is ",squaress)
#
# odds = []
# for j in range(1,100,2):
#     odds.append(j)
# print(odds)
# lists = tuple(odds)
# print(lists)
#
# even = []
# for o in range(0,100,2):
#     even.append(o)
# print(even)
#
# hundred = []
# for o in range(1,100,1):
#     hundred.append(o)
# print(hundred)
#
# hundreds = []
# for o in range(100,1,-1):
#     hundreds.append(o)
# print(hundreds)
#
# multi = int(input("Enter a number for multiplication:"))
# multip = []
# for i in range(1,11,1):
#     multip.append(multi*i)
#
# print(multip)

#Sum of first n number
first_number = int(input("Enter a number for sum: "))
sum = 0
for i in range(1,first_number,1):
    sum += i
print(sum)

#factorail of first n number
factorial_num = int(input("Enter a number for factorial: "))
sum = 0
for i in range(1,factorial_num,1):
    factorial_num *= i
print(factorial_num)
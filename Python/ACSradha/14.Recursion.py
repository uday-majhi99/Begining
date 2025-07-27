# def show(n):
#     if n == 0:
#         return n
#     print(n)
#     show(n-1 )
#
# show(5)

# def show(n):
#         if(n==0):
#             return
#         print(n)
#         show(n-1)
#         print("End")
#
# show(5)

# def fact(num):
#     result = 1
#     for i in range(1, num + 1):
#         result *= i
#     print(result)
#
# fact(3)

def fact(n):
    if (n==1 or n==0):
        return 1
    return fact(n-1)*n

print(fact(3))
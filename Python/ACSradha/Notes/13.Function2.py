def calc(a,b):
    sum = a + b
    print(sum)
    return sum

calc(2,3)

def ad_sum(a, b):
    if a == 0:
        return None
    return a + b

sums = ad_sum(2, 3)
print(sums)

print("Hello this", end= "  ")
print("Uday")

def calculate_mul(a=2,b=2):
    print(a*b)
    return a * b

calculate_mul()

cities = ["Kathmandu","Lalitpur","Bhaktapur"]
villages = ["Sakhuware","Aurabani","Bhamari"]

def prin_list(list):
    print(len(list))

def print_list1(list):
    for item in list:
        print(item, end = " ")

# print_list1(cities)
#
# num = 5
# fact = 1
# for i in range(1,num+1):
#     fact *= i
#
# print("\n",fact)

def cal_fact():
    num = 4
    fact = 1
    for i in range(1,num+1):
        fact *= i
    print(fact)
    return fact

print(cal_fact())

#  USD to NRS



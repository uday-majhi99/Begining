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


def usd_to_npr():
    nrs = int(input("Enter the value of NPR : "))
    usds = 137.28
    NPR = usds * nrs
    return NPR

print(f"The value in npr is ",usd_to_npr())

def converter(usd_val):
    nrs_value = usd_val * 137.28
    print(usd_val, "USD : ", nrs_value, "NPR")

converter(2)


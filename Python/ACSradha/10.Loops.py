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
apple_varieties = [
    "Adam's Pearmain", "Akane", "Alkmene", "Allington Pippin", "Ambrosia",
    "Anna", "Antonovka", "Api Etoile", "Arkansas Black", "Ashmead's Kernel",
    "Aurora Golden Gala", "Autumn Glory", "Bailey Sweet", "Baldwin", "Ballyfatten",
    "Beacon", "Beauty of Bath", "Belle de Boskoop", "Ben Davis", "Bismarck",
    "Black Diamond", "Black Gilliflower", "Black Oxford", "Black Twig", "Blenheim Orange",
    "Bloody Ploughman", "Blue Pearmain", "Braeburn", "Bramley's Seedling", "Brock",
    "Calville Blanc d'Hiver", "Cameo", "Campanino", "Cap of Liberty", "Cellini",
    "Champion", "Chelmsford Wonder", "Chisel Jersey", "Civni (Rubens)", "Clarke Pearmain",
    "Claygate Pearmain", "Clivia", "Coccagee", "Cornish Aromatic", "Cornish Gilliflower",
    "Cosmic Crisp", "Costard", "Court Pendu Plat", "Cox's Orange Pippin", "Creston",
    "Crimson Beauty", "Crimson Bramley", "Crimson Delight", "Crimson Gold", "Cripps Pink (Pink Lady)",
    "Cortland", "Daybreak Fuji", "Egremont Russet", "Empire", "Enterprise",
    "Envy", "EverCrisp", "Firecracker", "Fuji", "Gala",
    "Golden Delicious", "Golden Russet", "Granny Smith", "Gravenstein", "Honeycrisp",
    "Hokuto", "Indo", "Jazz", "Jonagold", "Jonathan",
    "Kanzi", "Knobby Russet", "Liberty", "Lucy Glo", "Lucy Rose",
    "McIntosh", "Mila Zagoras Piliou", "Milo Kastorias", "MN55 (Rave)", "Mutsu (Crispin)",
    "Newton Pippin", "Opal", "Orin", "Pink Luster", "Red Delicious",
    "Reinette du Canada", "Ribston Pippin", "Rome Beauty", "Roxbury Russet", "Ruby Frost",
    "Sekai Ichi", "Shizuka", "SnapDragon", "SugarBee", "SweeTango"
]
print("Types of potatoes are :")
for el in apple_varieties:
    print(el)
print("\n")

print("List of potato types:")
potato_types = (
    "Russet Burbank",
    "Yukon Gold",
    "Red Pontiac",
    "Kennebec",
    "Adirondack Blue",
    "Fingerling",
    "German Butterball",
    "Purple Majesty",
    "Carola",
    "Maris Piper"
)

for el1 in potato_types:
    print(el1)
else:
    print("End of the potato types")
#if-elif-else(Conditional Statements)
age = int(input("Enter your age :"))

if age <5:
    print("You are a toddler")

elif age < 12:
    print("You are a toddler")

elif age < 20:
    print("You are a teenager")

elif age < 50:
    print("You are an adult")

else:
    print("You are in your  old age")

thisString = "Here is the string, This is a string"

print(thisString[3])
print(thisString[6]) #character can b access through indexing

#Slicing
sliceThis = "you can slice the following  the sentence effectively"
print(sliceThis)
print(sliceThis[4:10])
print(sliceThis[4:len(sliceThis)])
print(sliceThis[4:])
print(sliceThis[:10])
print(sliceThis[-6:])
print(sliceThis[8:13])
print(sliceThis[-40:-35])
print(sliceThis.capitalize())
print(sliceThis.endswith("ely"))
print(sliceThis.endswith("el"))
print(sliceThis.replace("e","o"))
print(sliceThis.find("slice"))
print(sliceThis.find("q"))
print(sliceThis.count("the"))
print(sliceThis.count("o"))

#WAP to input user's first name and print its length
name = input("Enter your full name : ")
print(name)
print(len(name))

#WAP to find he occurrence of "$" in a string
strng = "He$$ i $m h$re to $lp you"
print(strng.count("$"))

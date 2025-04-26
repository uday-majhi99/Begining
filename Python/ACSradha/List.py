"""List is a built in datatype that stores set of values
    It can store elements of different types (integer, float, string,etc.) """

""""""
marks = [2,3,4,5,6,7,1]
for x in marks:
    print(x)
print(marks[-2:-4])

students = ["Uday", 90.4, "Excellent"]
print(students)
students[0] = "Majhi"
students[1] = 20
students[2] = "Worst"
print(students)
print(students[1:])
print(students[-1:-4:-1])

students.append("Good") #add one element to the end

marks.sort() #sort in ascending order

marks.sort(reverse = True) #sorts in descending order

students.reverse() #reverse the list

students.insert(1,"Hello")

print(students)
print(marks)

list1 = ['a','b','d','e','c']
list1.insert(3,'z')
print(list1)
print(sorted(list1))
'''OR'''
list1.sort()
print(list1)
list1.pop(2)

list1.reverse()
print(list1)

print(list(reversed(list1)))
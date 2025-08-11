# OOPS :to map with real world scenarios, we started using objects in code. This is called object-oriented language

#Creating an object
class Student:
    name = "Uday"
    faculty = "BIM"

s1 = Student()
print(s1.name)
print(s1.faculty)

# Constructor
# class factory:
#     name = "Karan"
#     def __init__(self):
#         print("Adding new student in database")
#
# f1 = factory()

# Constructor
class factory:
    # Default constructor
    def __ini__(self):
        pass

    # Parameterized constructor
    def __init__(self,fullname,staff_no):
        self.name = fullname
        self.staff_no = staff_no

#Creating Object
f1 = factory("Uday","20")
print(f1.name,f1.staff_no)

# Attributes

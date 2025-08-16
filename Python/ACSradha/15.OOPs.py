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
# class factory:
#     # Default constructor
#     def __ini__(self):
#         pass
#
#     # Parameterized constructor
#     def __init__(self,fullname,staff_no):
#         self.name = fullname  #attributes
#         self.staff_no = staff_no
#
# #Creating Object
# f1 = factory("Uday","20")
# print(f1.name,f1.staff_no)


class car:
    def __init__(self,car_color,car_version):
        self.car_color = car_color
        self.car_version =  car_version

    def welcome(self):
        print("Heelo world",self.car_color)

    def version(self):
        return self.car_version

c1 = car("Red","V4")
print(c1.car_color,c1.car_version)

c1.welcome()
print(c1.version())


class Student:
    def __init__(self,name,physics,chemistry,biology):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.biology = biology
        self.average = (physics+biology+chemistry)

    def average(self):
        return self.average

s1 = Student("Tony",20,90,200)
print(f"The average mark of {s1.name} is ",s1.average/3)



class studen:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks

    def avrg(self):
        som = 0
        for val in self.marks:
            som += val
        print(f"This it the average ",som/3)


stu1 = studen("Rohal", [98,97,99])
stu1.avrg()


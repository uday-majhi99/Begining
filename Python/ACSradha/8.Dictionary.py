"""
Dictionaries are used to store data values in key:value pairs
They are unordered,mutable(changeable) and don't allow duplicate keys
dict = {
    "key" : "values",
    "key" : "values"
"""

this_dict = {
    "name" : "Uday Majhi",
    "age" : 26,
    "address" : "Lalitpur",
    "is_adult" : True,
    "fav_num" : 20.2,
    "languages" : ["Python","C","Java"],
    "tuples_here" : ("Hello","This","is","a","tuple")
}
print(this_dict)
print(this_dict["languages"]) #Access keys in a dictionaries

#assign new value to the dictionaries
this_dict["name"] = "Shyam"
this_dict["surname"] = "Phaudar"
print(this_dict)

null_dict = {

}
null_dict["name"] = "Uday"
print(null_dict)

#nested dictionary
students = {
    "name" : "Rahul Dahal",
    "subjects" : {
        "Physics": 93,
        "Chemistry" :20
    }
}
print(students["subjects"]) #access nested
print(students["subjects"]["Physics"]) #access to nested dictionary
print(students)

#convert into list with dictionary methods
print(list(students))
print(list(students.keys()))
print(type(students.keys()))
print(list(students.values()))
print((students.items()))
print(list(students.items()))

print(students["name"]) #If there is no key called as name it will throw an error
print(students.get("name1")) #If there is not such field it will not throw any error

#Update a dictionary
students.update({"City" : "Lalitpur"})
print(students)


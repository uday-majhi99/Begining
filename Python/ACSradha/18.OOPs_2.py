#del keyword helps to delete object properties or itself del s1.name/ del s1
"""Private attributes(like) and methods are meant to be used only within the class and are not accessible
    from outside the class
 """

class hello:
    def __init__(self, cc, bb):
        self.cc = cc
        self.__bb = bb

    def new(self):
        return self.__bb
        print(self.__bb)

s1 = hello(11,22)
print(s1.cc)
print(s1.new())



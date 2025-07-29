# Read files
f = open("fileinputoutput.txt", "r")
dates = f.read(3)
data = f.read()
print(dates)
print(data)
print(type(data))
f.close()

fi = open("/Users/udaymajhi/Documents/Begining/Begining/Python/ACSradha/Notes/demo.txt","r")
datas = fi.read()
print(datas)
fi.close()


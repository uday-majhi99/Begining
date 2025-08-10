# Read files
f = open("fileinputoutput.txt", "r")
# dates = f.read(3)
data = f.read()
# print(dates)
print(data)
# print(type(data))
f.close()
#
# fi = open("/Users/udaymajhi/Documents/Begining/Begining/Python/ACSradha/Notes/demo.txt","r")
# datas = fi.read()
# print(datas)
# fi.close()

# g = open("fileinputoutput.txt","r")
# # inp = g.read()
# line1 = g.readline()
# # print(inp)
# print(line1)
# line2 = g.readline()
# print(line2)
# g.close()

# Write a data in a file
f = open("fileinputoutput.txt", "w")
f.write("hello is the learning input and output")
f.close()

# Append(add) data in a file
f = open("fileinputoutput.txt","a")
f.write("\nThis line are added line")
f.close()

# Create a new file
f = open("newfile.txt","w")
dat = f.write("Hello")
print(dat)
f.close()

f = open("readandwrite.text", "r+")
f.write("This")
print(f.read())
f.write("That")
f.close()



squares = []

for i in range(1,11):
    squares.append(i*i)

print(f"List of elements is ",squares)
squaress = tuple(squares)
print(f"List of elements is ",squaress)

odds = []
for j in range(1,100,2):
    odds.append(j)
print(odds)
lists = tuple(odds)
print(lists)

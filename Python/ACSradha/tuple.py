tup = (1,5,2,4,3,9,7)
print(tup)
print(type(tup))
print(sorted(tup))

# Slicing in tuple
print(tup[1:4])
print(tup.index(3))

#WAP to ask the user to enter names of their 3 favorite movies and store them in a list
favorite_movies = []
for i in range(3):
    movie  = input(f"Enter your favorite movie name {i+1}:")
    favorite_movies.append(movie)

print("Your favorite movies are : ", favorite_movies)

#WAP to check if a list contains a palindrome of elements(use copy() method

original_list = input("Enter your values: ").split()
print("Original list:", original_list)

reversed_list = original_list.copy()
reversed_list.reverse()

print("Reversed list:", reversed_list)

if original_list == reversed_list:
    print(f"{original_list} is a palindrome")
else:
    print(f"{original_list} is not a palindrome")

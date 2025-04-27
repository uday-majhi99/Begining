# Take input from user
strn = input("Enter a list of items separated by spaces: ")

# Convert string to list
original_list = strn.split()

# Print original list
print("Original list:", original_list)

# Copy and reverse
rev_list = original_list.copy()
rev_list.reverse()

# Print reversed list
print("Reversed list:", rev_list)

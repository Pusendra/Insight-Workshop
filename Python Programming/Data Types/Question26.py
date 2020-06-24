# Question 26: Write a Python program to insert a given string at the beginning of all items in
# a list.

item_list = [1, 2, 3, 4, 5]
add_str = 'Emp'
print([*map(lambda a: add_str + str(a), item_list)])
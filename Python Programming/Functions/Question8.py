# Question 8: Write a Python function that takes a list and returns a new list with unique
# elements of the first list.

def unique_list(*args):
    return [*set(*args)]

print(unique_list([1, 1, 1, 2, 2, 3, 4, 5, 5, 5]))
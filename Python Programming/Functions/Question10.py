# Question 10: Write a Python program to print the even numbers from a given list.

def even_number(*args):
    return [*filter(lambda a: a % 2 == 0, *args)]

print(even_number([1, 2, 3, 4, 5, 6]))
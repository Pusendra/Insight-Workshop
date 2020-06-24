# Question 3: Write a Python function to multiply all the numbers in a list.

from functools import reduce

def mul_numbers(*args):
    return reduce(lambda a,b:a * b, *args)

print(mul_numbers([1, 2, 3, 4]))
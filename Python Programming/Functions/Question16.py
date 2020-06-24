# Question 16: Write a Python program to square and cube every number in a given list of
# integers using Lambda.

sample_list = [1, 2, 3, 4, 5]
print([*map(lambda a: (a, a*a, a*a*a), sample_list)])
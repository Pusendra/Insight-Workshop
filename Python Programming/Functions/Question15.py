# Question 15: Write a Python program to filter a list of integers using Lambda.

sample_list = range(-5, 6)
print([*filter(lambda a: a < 0, sample_list)])
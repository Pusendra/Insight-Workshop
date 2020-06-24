# Question 39: Write a Python program to unpack a tuple in several variables.

sample_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
a, *b, c = sample_tuple
print(sample_tuple)
print(a)
print(b)
print(c)
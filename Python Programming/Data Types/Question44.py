# Question 44: Write a Python program to slice a tuple.

sample_tuple = ('J', 'u', 'n', 'S', 'u', 's', 'h', 't', 'h')
print(''.join((*sample_tuple[0:3], *sample_tuple[-2:])))
# Question 35: Write a Python program to iterate over dictionaries using for loops.

sample_dict = {'Junth': 21,
               'Supreme': 22,
               'James': 14,
               'Sushmita': 20}

print([(k,v) for k,v in sample_dict.items()])
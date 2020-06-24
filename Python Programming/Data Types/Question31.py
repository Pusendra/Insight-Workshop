# Question 31: Write a Python program to iterate over dictionaries using for loops.

sample_dict = {'Red': 1, 
               'Green': 2, 
               'Blue': 3}

print([(k, v) for k,v in sample_dict.items()])
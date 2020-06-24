# Question 10: Write a Python program to remove the characters which have 
# odd index values of a given string.

sample_string = 'abcdef'
even_string = ''
for i in range(0,len(sample_string), 2):
    even_string += sample_string[i]
print(even_string)
    
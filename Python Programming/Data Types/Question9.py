# Question 9: Write a Python program to change a given string to a new string where the first
# and last chars have been exchanged.

sample_string = 'abcde'
print(sample_string[-1] + sample_string[1:-1] + sample_string[0])
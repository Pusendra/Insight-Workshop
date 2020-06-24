# Question 3: Write a Python program to get a string from a given string where all 
# occurrences of its first char have been changed to '$', except the first char itself.

sample_string = 'restart'
result = sample_string[0] + ''.join([*map(lambda a:'$' if sample_string[0] == a else a, sample_string[1:])])
print(result)

# Question 5: Write a Python program to add 'ing' at the end of a given string (length should
# be at least 3). If the given string already ends with 'ing' then add 'ly' instead. If the
# string length of the given string is less than 3, leave it unchanged.

sample_string = 'string'
result = sample_string + 'ly' if sample_string[-3:] == 'ing' else sample_string + 'ing' \
         if len(sample_string) >=3 else sample_string
print(result)
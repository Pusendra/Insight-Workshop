# Question 2: Write a Python program to get a string made of the first 2 and the last 2 chars
# from a given a string. If the string length is less than 2, return instead of the
# empty string.

sample_string = 'Python'
print(sample_string_1[:2] + sample_string_1[-2:] if len(sample_string_1) >=2 
      else 'Empty String')
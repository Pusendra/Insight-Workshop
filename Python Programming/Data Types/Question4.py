# Write a Python program to get a single string from two given strings, separated
# by a space and swap the first two characters of each string.

sample_string = ['abc', 'xyz']
result = sample_string[1][:2] + sample_string[0][2:] + ' ' + sample_string[0][:2] + sample_string[1][2:]
print(result)

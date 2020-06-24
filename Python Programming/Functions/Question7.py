# Question 7: Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters.

def number_upper_lower(text):
    return f'Number of Uppercase Char: {len([*filter(lambda a: a.isupper(), text)])}\
             Number of Lowercase Char: {len([*filter(lambda a: a.islower(), text)])}'

print(number_upper_lower('Junth 19'))
# Question 37: Write a Python program to multiply all the items in a dictionary.

cho_dict = {'Junth': 1,
            'Sushmita': 2,
            'Supreme': 3,
            'James': 4}

result = 1
for i in cho_dict.values():
    result *= i
print(result)
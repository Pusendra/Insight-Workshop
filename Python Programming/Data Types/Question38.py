# Question 38: Write a Python program to remove a key from a dictionary.


def removeKey(sample_dict, k):
    return sample_dict.pop(k, None)

sample_dict = {'Junth': 21,
               'Supreme': 22,
               'James': 14,
               'Sushmita': 20}

print(removeKey(sample_dict, 'Supreme'))
print(sample_dict)
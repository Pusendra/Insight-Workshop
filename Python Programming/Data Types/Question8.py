# Question 8: Write a Python program to remove the nth index character from a nonempty string.

def remove_index(sample_string, index):
    """
    Removes nth index character from a nonempty string.
    """
    return sample_string[:index] + sample_string[index + 1:]

sample_string = 'abcde'
print(remove_index(sample_string, 4))

# Question 15: Write a Python function to insert a string in the middle of a string.

def insert_string_middle(a, word):
    """
    Returns word inserted in between a.
    """
    middle = len(a) // 2
    return a[:middle] + word + a[middle:]

print(insert_string_middle('[[]]', 'Junth Basnet'))
print(insert_string_middle('{{{}}}', 'Supreme'))
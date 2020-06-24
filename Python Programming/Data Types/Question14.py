# Question 14: Write a Python function to create the HTML string with tags around the
# word(s).

def add_tags(tag, word):
    """
    Create HTML string with tags around the word.
    """
    return f'<{tag}>{word}</{tag}>'

print(add_tags('i', 'Hello World'))
print(add_tags('b', 'Hey there!'))
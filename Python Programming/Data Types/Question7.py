# Question 7: Write a Python function that takes a list of words and returns the length of the
# longest one.

list_words = ['Junth', 'Clementine', 'Katherine', 'Supreme']
result = sorted(([*map(lambda a : (a, len(a)), list_words)]), key = lambda a:a[1], reverse=True)
print(result[0])






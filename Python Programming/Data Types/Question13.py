# Question 13: Write a Python program that accepts a comma separated sequence of words
# as input and prints the unique words in sorted form (alphanumerically).

samples = 'red, black, pink, green'.split(',')
print(', '.join(sorted(set([sample.strip() for sample in samples]))))

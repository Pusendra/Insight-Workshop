# Question 11: Write a Python program to count the occurrences of each word in a given
# sentence.

sample_string = 'the quick brown fox jumps over the lazy dog.'.split(' ')
result = {k:sample_string.count(k) for k in sample_string}
print(result)


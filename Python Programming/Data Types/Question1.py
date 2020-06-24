# Question 1: Write a Python program to count the number of characters (character frequency) in a string. 
# Sample String : google.com'

# Alternative 1
# =============================================================================
# from collections import Counter
# sample_string = 'google.com'
# count_string = Counter(sample_string)
# print({k:v for k,v in count_string.items()})
# =============================================================================

# Alternative 2
sample_string = 'google.com'
count_string = {k:sample_string.count(k) for k in sample_string}
print(count_string)
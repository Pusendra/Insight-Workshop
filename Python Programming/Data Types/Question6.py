# Question 6: Write a Python program to find the first appearance of the substring 'not' and
# 'poor' from a given string, if 'not' follows the 'poor', replace the whole 'not'...'poor'
# substring with 'good'. Return the resulting string.

sample_string = 'The lyrics is not that poor!'
not_index = sample_string.index('not')
poor_index = sample_string.index('poor')
result = sample_string.replace(sample_string[not_index:poor_index + 4], 'good',1) \
         if not_index < poor_index else sample_string
print(result)

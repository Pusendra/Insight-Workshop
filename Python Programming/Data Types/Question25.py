# Question 25: Write a Python program to check whether all dictionaries in a list are empty or
# not.

dict_list = [{}, {}, {}]
print(all([True if not i else False for i in dict_list]))
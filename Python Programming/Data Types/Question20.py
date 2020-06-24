# Question 20: Write a Python program to count the number of strings where the string
# length is 2 or more and the first and last character are same from a given list of
# strings.

item_list = ['abc', 'aba', 'cdc', 'efg', 'cdcdc']
print(len([item for item in item_list if item[0] == item[-1] and len(item) >= 2]))
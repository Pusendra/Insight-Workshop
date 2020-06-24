# Question 21: Write a Python program to get a list, sorted in increasing order by the last
# element in each tuple from a given list of non-empty tuples.

tuple_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(sorted(tuple_list, key = lambda a:a[-1]))
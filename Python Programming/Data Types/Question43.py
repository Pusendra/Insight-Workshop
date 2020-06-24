# Question 43: Write a Python program to remove an item from a tuple.

# Since tuples are immutable.
sample_tuple = list((1, 2, 3, 4, 5, 'J', 6, 7))
sample_tuple.pop(-3)    # 'J' is popped
print(sample_tuple)
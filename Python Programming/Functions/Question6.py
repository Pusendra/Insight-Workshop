# Question 6: Write a Python function to check whether a number is in a given range.

def checkRange(min_n, max_n, num):
    return True if num in range(min_n, max_n + 1) else False

print(checkRange(5, 20, 10))
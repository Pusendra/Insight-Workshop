# Question 1: Write a Python function to find the Max of three numbers.

def max_three(*args):
    """
    Returns the max of three numbers
    """
    return max(*args)

print(max_three(1, 2, 3))
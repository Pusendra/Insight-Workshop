# Question 12: Write a Python program to create a function that takes one argument, and
# that argument will be multiplied with an unknown given number.

def lambda_return(num):
    return lambda a: a * num

result = lambda_return(2)
print(result(15))

result = lambda_return(3)
print(result(15))

result = lambda_return(4)
print(result(15))
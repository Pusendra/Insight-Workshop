# Question 9: Write a Python function that takes a number as a parameter and check the
# number is prime or not.

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

print(is_prime(17))
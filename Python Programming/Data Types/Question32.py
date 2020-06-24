# Question 32: Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).

n = 10
print({k:k*k for k in range(1, n + 1)})
# Question 20: Write a Python program to find intersection of two given arrays using Lambda.

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print([*filter(lambda a: a in list1, list2)])
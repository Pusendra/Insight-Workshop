# Question 30: Write a Python script to check whether a given key already exists in a
# dictionary.

def check_key(key, dic):
    return True if key in dic else False

dic = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
print(check_key(6, dic))
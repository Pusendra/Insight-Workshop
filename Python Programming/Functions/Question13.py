# Question 13: Write a Python program to sort a list of tuples using Lambda.

sample_tuple = [('English', 88), 
                ('Science', 90), 
                ('Maths', 97), 
                ('Social sciences', 82)]

print(sorted(sample_tuple, key=lambda a:a[-1]))
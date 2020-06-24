# Question 14: Write a Python program to sort a list of dictionaries using Lambda.

sample_dict = [{ "name" : "Junth", "age" : 21},
               { "name" : "Sushmita", "age" : 20 }, 
               { "name" : "Supreme", "age" : 22 }, 
               { "name" : "James" , "age" : 14 }] 

print(sorted(sample_dict, key=lambda a:a['age']))
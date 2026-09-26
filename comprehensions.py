#-----------List Comprehension-------------

# names = ["Vansh", "Aman", "Rahul", "Rohan", "Kartik", "Ritik"]

# res = [name for name in names if name[0].lower() == 'r']

# print(res)

# scores = [10, 50, 60, 95, 54]

# updated_scores = [score+10 for score in scores if not(score > 90)]

# print(updated_scores)

#-------------Set Comprehension------------------

names = ["Vansh","Aman","Rahul","Kartik","Rahul","Rahul"]

res_names = {name for name in names}

print(res_names)
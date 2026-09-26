#-----------List Comprehension-------------

# names = ["Vansh", "Aman", "Rahul", "Rohan", "Kartik", "Ritik"]

# res = [name for name in names if name[0].lower() == 'r']

# print(res)

# scores = [10, 50, 60, 95, 54]

# updated_scores = [score+10 for score in scores if not(score > 90)]

# print(updated_scores)

#-------------Set Comprehension------------------

# names = ["Vansh","Aman","Rahul","Kartik","Rahul","Rahul"]

# res_names = {name for name in names}

# print(res_names)

#--------------Dictionary Comprehension--------------

# users = {"Vansh":67,"Aman":90, "Rahul":45, "Kartik":34}

# # res_marks = {name:users[name]+10 for name in users if users[name] < 91}

# res_marks = {key:val+10 for key,val in users.items() if val < 91}

# print(res_marks)


# users = [{
#     'name':"Vansh",
#     'email':"vansh@gmail.com",
#     'age':23
# },{
#     'name':"Aman",
#     'email':"aman@gmail.com",
#     'age':23
# },{
#     'name':"Kartik",
#     'email':"kartik@gmail.com",
#     'age':23
# },{
#     'name':"Rahul",
#     'email':"rahul@gmail.com",
#     'age':23
# }]


# res_user = {key:val for user in users if user['email'] == "vansh@gmail.com" for key, val in user.items()}

# print(res_user)

#-----------Generator Comprehension----------


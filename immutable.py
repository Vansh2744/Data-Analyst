# score = 25

# print(score)
# print(id(score))
# print(id(25))

# score = 50

# print(score)
# print(id(score))
# print(id(50))

#------------------------

# is_valid = True

# print(id(is_valid))
# print(id(True))

# is_valid = False

# print(id(is_valid))
# print(id(False))

#--------------------------

# name = "Vansh"

# print(id(name))
# print(id("Vansh"))

# name = "Aman"

# print(id(name))
# print(id("Aman"))

#-----------------------------

# role = ('USER','ADMIN')

# print(id(role))
# print(id(('USER','ADMIN')))

# role = ('STUDENT','TEACHER')

# print(id(role))
# print(id(('STUDENT','TEACHER')))

#------------------------------

users = frozenset(["Vansh","Aman","Rahul"])

print(id(users))

users = frozenset(["Vansh","Aman","Kartik"])

print(id(users))
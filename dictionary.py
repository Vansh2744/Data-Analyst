user1 = dict(name="Vansh", email="vansh@gmail.com", age=23)

print(user1)

user2 = {'name':'Vansh', 'email':'vansh@gmail.com', 'age':23}

print(user2)

user3 = {}
user3['name'] = 'Vansh'
user3['email'] = 'vansh@gmail.com'
user3['age'] = 23

# print(user3)

# print(user3.keys())
# print(user3.values())
# print(user3.items())

# print(user3.popitem())

user4 = {'name':'Vansh','email':'vansh@gmail.com'}
user5 = {'age':23}

# user4.update(user5)

# print(user4)

print(user3['name'])

print(user3.get('email',"abc"))

print(user3.get('my_score',50))

a = {'name':'Vansh','email':'vansh@gmail.com'}
b = {'name':'Vansh', 'age':23}

print(a | b)
print(a.keys() | b.keys())
print(a.keys() & b.keys())
print(a.keys() - b.keys())
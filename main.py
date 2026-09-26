data = [{
    'name':"Vansh",
    'email':"vansh@gmail.com",
    'age':23
},{
    'name':"Aman",
    'email':"aman@gmail.com",
    'age':23
},{
    'name':"Kartik",
    'email':"kartik@gmail.com",
    'age':23
},{
    'name':"Rahul",
    'email':"rahul@gmail.com",
    'age':23
}]

res = next((user for user in data if user['email'] == "vansh@gmail.com"))

print(res)
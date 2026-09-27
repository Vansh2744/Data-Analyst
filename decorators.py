# def built_decorator(fn):
#     def wrapper():
#         print("Starting.....")
#         fn()
#         print("Ending.....")

#     return wrapper

# @built_decorator
# def greet():
#     print("Hello Vansh")

# greet()

# def sub_decorator(fn):
#     def wrapper(a, b):
#         if b > a:
#             return "Result will be negative cannot subtract"
#         return fn(a,b)

#     return wrapper

# @sub_decorator
# def sub(a,b):
#     return a - b

# print(sub(340,56))

# def validate_user(fn):
#     def wrapper(**kwargs):
#         print("Validating User...")
#         if not kwargs['email'] == "vansh@gmail.com":
#             return f"User with Email : {kwargs['email']} is an Invalid User"
#         return fn(**kwargs)

#     return wrapper

# @validate_user
# def display_user(**kwargs):
#     return kwargs

# print(display_user(name='Vansh',email='vansh@gmail.com',age=23))

#---------------------------

# from functools import wraps

# def built_decorator(fn):
#     @wraps(fn)
#     def wrapper():
#         print("Starting.....")
#         fn()
#         print("Ending.....")

#     return wrapper

# @built_decorator
# def greet():
#     print("Hello Vansh")

# print(greet.__name__)

#--------------------------

# def logger(fn):
#     def wrapper(*args, **kwargs):
#         print(f"Args : {args}")
#         print(f"Kwargs : {kwargs}")
        
#         return fn(*args, **kwargs)

#     return wrapper

# @logger
# def display(*args, **kwargs):
#     return kwargs, args

# print(display(23, 45, 67, name='Vansh', email='vansh@gmail.com'))
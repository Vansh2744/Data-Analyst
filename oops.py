#-----------Object Namespace-------------

# class Student:
#     school_name = "GSSS"

# print(Student.school_name)

# std = Student()

# print(std.school_name)

# std.school_name = "HPSSS"

# print(Student.school_name)
# print(std.school_name)

# std.student_name = "Vansh"

# print(std.student_name)

#---------Attribute Shadowing----------

# class Student:
#     school_name = "GSSS"

# std = Student()

# std.school_name = "HPSSS"

# print(std.school_name)

# del std.school_name

# print(std.school_name)

#------------self argument----------------

# class Student:
#     school = "GSSS"

#     def info(self):
#         print(self.school)

# std = Student()

# std.info()

# Student.info(std)

#-----------__init__--------------------

# class Student:
#     def __init__(self, school_name, student_name):
#         self.school_name = school_name
#         self.student_name = student_name

#     def display_info(self):
#         print(f"School Name : {self.school_name}")
#         print(f"Student Name : {self.student_name}")

# std1 = Student("GSSS", "Vansh")

# std1.display_info()

# std2 = Student("HPSSS", "Aman")

# std2.display_info()

#----------Inheritance------------------

# class School:
#     def __init__(self, school_name):
#         self.school_name = school_name

#     def display_info(self):
#         return f"School Name : {self.school_name}"

# class Student(School):
#     def __init__(self, school_name, student_name):
#         super().__init__(school_name)
#         self.student_name = student_name

#     def student_info(self):
#         return f"School Name : {self.student_name}"

# std = Student("GSSS","Vansh")

# print(std.student_info())
# print(std.display_info())

# class Random:
#     school = School
#     def __init__(self):
#         self.rand = self.school("HPSSS")

#     def display(self):
#         return f"School Name(Random class) : {self.rand.school_name}"

# class ChildRandom(Random):
#     std = Student

# rand = Random()

# print(rand.display())

# child = ChildRandom()

# print(child.rand.display_info())
# print(child.std("HPSSS","Aman").student_info())

#----------Explicit way to access base class-----------

# class Student:
#     def __init__(self, name):
#         self.name = name

#     def display_std(self):
#             return f"Name : {self.name}"

# class Student1(Student):
#     def __init__(self, name, email):
#         Student.__init__(self, name)
#         self.email = email

#     def display(self):
#         return f"Name : {self.name}  Email : {self.email}"

# std = Student1("Vansh", "vansh@gmail.com")

# print(std.display())
# print(std.display_std())
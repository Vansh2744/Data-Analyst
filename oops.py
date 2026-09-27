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
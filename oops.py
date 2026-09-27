#-----------Object Namespace-------------

class Student:
    school_name = "GSSS"

print(Student.school_name)

std = Student()

print(std.school_name)

std.school_name = "HPSSS"

print(Student.school_name)
print(std.school_name)
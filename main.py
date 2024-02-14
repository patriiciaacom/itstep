# class Student:
#     print("Hi")
#     def __init__(self):
#         self.height = 160
#         print("I am alive")
#
# first_student = Student()
#
# print(first_student.height)

class Student:
    def __init__(self, height = 160):
        self.height = height

nick = Student()
kate = Student(height = 170)
Chirll = Student(height = 2833)
print(nick.height)
print(kate.height)
print(chirll.height)
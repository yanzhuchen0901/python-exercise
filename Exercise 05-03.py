# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/22
student = {}
student["Name"] = "James"
student["Age"] = 21
student["Course"] = "IT"
student["ID"] = "2016A001"
print(student)
print(student["Name"] + ":", student["ID"])
del student["Course"]
for i in student:
    print(student[i])

class Student:
    def __init__ (self, name, age, course, ID):
        self.name = name
        self.age = age
        self.course = course
        self.ID = ID

student1 = Student("James", 21, "IT", "2016A001")

print("My name is " + student1.name + "." + "And I'm " + str(student1.age) + "major in " + student1.course + "." + "My ID is " + student1.ID + ".")
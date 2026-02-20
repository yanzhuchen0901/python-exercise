# Name: Xing Ziyi
# ID: 202010701580011
# Date:  2021/9/22
marks = {"Sam": 90.5, "Jane": 85.4, "Max": 92.3, "Alice": 64.5, "John": 69.4}
sum = 0
for i in marks:
    sum += marks[i]
print("Sum:", sum)
print("Average:", sum / len(marks))

class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

print("输入0来终止输入")
total = 0
count = 0
while True:
    name = input("请输入学生姓名")
    if name == "0":
        break
    grade = float(input("请输入学生成绩"))
    student = Student(name, grade)
    total += grade
    count += 1
print("平均成绩为：%.2f" % (total / count))
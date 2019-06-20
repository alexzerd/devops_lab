
print("Input number of students")

n = int(input())

student_marks = {}

print("Input students records")

for i in range(n):

    record = input().split()

    name, marks = record[0], record[1:]

    marks = list(map(float, marks))

    student_marks[name] = marks

query = input("Input name of student\t")

print(sum(student_marks[query])/3)

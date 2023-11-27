lines = int(input())
students = {}
for _ in range(lines):
    student = input()
    grade = float(input())
    if student not in students.keys():
        students[student] = [grade]
    else:
        students[student].append(grade)

final_student_list = {name: (sum(grades)/len(grades)) for name, grades in students.items()}
for student, average_grade in final_student_list.items():
    if average_grade >= 4.5:
        print(f"{student} -> {average_grade:.2f}")

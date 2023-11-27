courses = {}
while True:
    command = input()
    if command == "end":
        break

    course_name, student_name = command.split(" : ")
    if course_name in courses.keys():
        courses[course_name].append(student_name)
    else:
        courses[course_name] = [student_name]

for course in courses.keys():
    print(f"{course}: {len(courses[course])}")
    for student in range(len(courses[course])):
        print(f"-- {courses[course][student]}")

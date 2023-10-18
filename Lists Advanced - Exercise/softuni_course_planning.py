def handle_course_start(current_schedule, current_exercises):
    for i in range(len(current_schedule)):
        for element in current_exercises:
            if element == current_schedule[i]:
                current_schedule.insert(i+1, f'{element}-Exercise')

    for i in range(len(current_schedule)):
        print(f"{i + 1}.{current_schedule[i]}")


schedule = input().split(", ")
exercises = []

while True:
    command = input()
    if command == "course start":
        handle_course_start(schedule, exercises)
        break
    command = command.split(":")
    action = command[0]
    first_new_lesson = command[1]

    if action == "Add":
        if first_new_lesson not in schedule:
            schedule.append(first_new_lesson)

    elif action == "Insert":
        if first_new_lesson not in schedule:
            index = int(command[2])
            if 0 <= index < len(schedule):
                schedule.insert(index, first_new_lesson)

    elif action == "Remove":
        if first_new_lesson in schedule:
            index_of_exercise = schedule.index(first_new_lesson)
            schedule.remove(first_new_lesson)

    elif action == "Swap":
        second_new_lesson = command[2]
        if first_new_lesson in schedule and second_new_lesson in schedule:
            first_index = schedule.index(first_new_lesson)
            second_index = schedule.index(second_new_lesson)
            schedule[first_index], schedule[second_index] = schedule[second_index], schedule[first_index]

    elif action == "Exercise":
        if first_new_lesson in schedule:
            exercises.append(first_new_lesson)
        elif first_new_lesson not in schedule:
            schedule.append(first_new_lesson)
            exercises.append(first_new_lesson)

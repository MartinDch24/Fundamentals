def handle_course_start(current_schedule, current_exercises):
    i = 0
    current_index = i + 1
    while i < len(current_schedule):
        print(f"{current_index}.{current_schedule[i]}")
        if current_schedule[i] in current_exercises:
            current_index += 1
            print(f"{current_index}.{current_schedule[i]}-Exercise")
        i += 1
        current_index += 1


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
            schedule.insert(index, first_new_lesson)

    elif action == "Remove":
        if first_new_lesson in schedule:
            schedule.remove(first_new_lesson)
            if first_new_lesson in exercises:
                exercises.remove(first_new_lesson)

    elif action == "Swap":
        second_new_lesson = command[2]
        if first_new_lesson in schedule and second_new_lesson in schedule:
            first_index = schedule.index(first_new_lesson)
            second_index = schedule.index(second_new_lesson)
            schedule[first_index], schedule[second_index] = schedule[second_index], schedule[first_index]

    elif action == "Exercise":
        if first_new_lesson in schedule and first_new_lesson not in exercises:
            exercises.append(first_new_lesson)
        elif first_new_lesson not in schedule:
            schedule.append(first_new_lesson)
            exercises.append(first_new_lesson)

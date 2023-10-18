command = input()

while command != "End":
    if command == "SoftUni":
        command = input()
        continue
    new_string = ""
    for char in command:
        new_string += char*2
    print(new_string)

    command = input()

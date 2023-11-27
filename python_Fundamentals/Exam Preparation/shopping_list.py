items = input().split("!")

while True:
    command = input()
    if command == "Go Shopping!":
        break
    else:
        command = command.split()
    if command[0] == "Urgent":
        if command[1] not in items:
            items.insert(0, command[1])
    elif command[0] == "Unnecessary":
        if command[1] in items:
            items.remove(command[1])
    elif command[0] == "Correct":
        if command[1] in items:
            item_index = items.index(command[1])
            items[item_index] = command[2]
    elif command[0] == "Rearrange":
        if command[1] in items:
            items.remove(command[1])
            items.append(command[1])

print(", ".join(items))

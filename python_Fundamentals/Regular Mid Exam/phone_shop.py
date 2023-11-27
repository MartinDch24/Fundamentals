storage = input().split(", ")

while True:
    command = input()
    if command == "End":
        break

    command = command.split(" - ")
    action = command[0]
    phone = command[1]

    if action == "Add":
        if phone not in storage:
            storage.append(phone)

    elif action == "Remove":
        if phone in storage:
            storage.remove(phone)

    elif action == "Bonus phone":
        old_phone, new_phone = phone.split(":")
        if old_phone in storage:
            index_of_old_phone = storage.index(old_phone)
            storage.insert(index_of_old_phone+1, new_phone)

    elif action == "Last":
        if phone in storage:
            storage.remove(phone)
            storage.append(phone)

print(", ".join(storage))

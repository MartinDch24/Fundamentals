friends = input().split(", ")
blacklisted_names = 0
lost_names = 0

while True:
    command = input()
    if command == "Report":
        break

    command = command.split()
    action = command[0]
    name_or_index = command[1]

    if action == "Blacklist":
        if name_or_index in friends:
            blacklisted_names += 1
            friends[friends.index(name_or_index)] = "Blacklisted"
            print(f"{name_or_index} was blacklisted.")
        else:
            print(f"{name_or_index} was not found.")

    elif action == "Error":
        name_or_index = int(name_or_index)
        if 0 <= name_or_index < len(friends):
            if friends[name_or_index] != "Blacklisted" and friends[name_or_index] != "Lost":
                print(f"{friends[name_or_index]} was lost due to an error.")
                lost_names += 1
                friends[name_or_index] = "Lost"

    elif action == "Change":
        new_name = command[2]
        name_or_index = int(name_or_index)
        if 0 <= name_or_index < len(friends):
            print(f"{friends[name_or_index]} changed his username to {new_name}.")
            friends[name_or_index] = new_name

print(f"Blacklisted names: {blacklisted_names}")
print(f"Lost names: {lost_names}")
print(" ".join(friends))

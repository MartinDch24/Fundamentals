company = {}

while True:
    command = input()
    if command == "End":
        break

    name, ID = command.split("->")
    if name in company:
        if ID not in company[name]:
            company[name].append(ID)
    else:
        company[name] = [ID]

for current_name in company.keys():
    print(f"{current_name}")
    for current_ID in company[current_name]:
        print(f"--{current_ID}")

coffee_counter = 0

command = input()
while command != "END":
    if command.lower() == "coding":
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2

    elif command.lower() == "dog":
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2

    elif command.lower() == "cat":
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2

    elif command.lower() == "movie":
        if command.islower():
            coffee_counter += 1
        else:
            coffee_counter += 2

    command = input()

if coffee_counter > 5:
    print("You need extra sleep")
else:
    print(coffee_counter)

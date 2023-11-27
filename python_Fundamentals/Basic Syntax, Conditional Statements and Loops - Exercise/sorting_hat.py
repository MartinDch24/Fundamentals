command = input()
voldemort_presence = False

while command != "Welcome!":
    name = command

    if name == "Voldemort":
        print(f"You must not speak of that name!")
        voldemort_presence = True
        break

    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")

    command = input()

if not voldemort_presence:
    print("Welcome to Hogwarts.")

gifts = input().split()

while True:
    command = input()
    if command == "No Money":
        break
    elif "OutOfStock" in command:
        gift = command[11:]
        for index in range(len(gifts)):
            if gift == gifts[index]:
                gifts[index] = "None"
    elif "Required" in command:
        gift, index = command[9:].split()
        if 0 <= int(index) <= len(gifts) - 1:
            gifts[int(index)] = gift
    elif "JustInCase" in command:
        gifts[-1] = command[11:]

for element in gifts:
    if element != "None":
        print(element, end=" ")

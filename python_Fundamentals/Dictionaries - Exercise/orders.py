items = {}

while True:
    command = input()
    if command == "buy":
        break

    name, price, quantity = command.split()
    if name not in items.keys():
        items[name] = [float(price), int(quantity)]
    else:
        items[name][0] = float(price)
        items[name][1] += int(quantity)

for key, value in items.items():
    print(f"{key} -> {value[0] * value[1]:.2f}")

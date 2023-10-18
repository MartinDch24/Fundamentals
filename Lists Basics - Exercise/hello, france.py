items = input().split("|")
budget = float(input())
initial_budget = budget
new_prices = []
profit = 0.00

for i in range(len(items)):
    item, price = items[i].split("->")
    price = f"{float(price):.2f}"
    price = float(price)
    if item == "Clothes" and price <= 50 and budget - price >= 0:
        budget -= price
        new_prices.append(f"{price * 1.4:.2f}")
        profit += price * 0.4
    elif item == "Shoes" and price <= 35 and budget - price >= 0:
        budget -= price
        new_prices.append(f"{price * 1.4:.2f}")
        profit += price * 0.4
    elif item == "Accessories" and price <= 20.5 and budget - price >= 0:
        budget -= price
        new_prices.append(f"{price * 1.4:.2f}")
        profit += price * 0.4
    else:
        continue
print(" ".join(new_prices))
print(f"Profit: {profit:.2f}")
if initial_budget + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

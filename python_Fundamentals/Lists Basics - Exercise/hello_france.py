items = input().split("|")
budget = float(input())
initial_budget = budget
new_prices = []
profit = 0.00

for current_item in items:
    item, price = current_item.split("->")
    price = float(price)
    if item == "Clothes" and 0 <= price <= 50 and budget - price >= 0:
        budget -= price
        profit += price * 0.4
        new_prices.append(f"{price * 1.4:.2f}")
    elif item == "Shoes" and 0 <= price <= 35 and budget - price >= 0:
        budget -= price
        profit += price * 0.4
        new_prices.append(f"{price * 1.4:.2f}")
    elif item == "Accessories" and 0 <= price <= 20.5 and budget - price >= 0:
        budget -= price
        profit += price * 0.4
        new_prices.append(f"{price * 1.4:.2f}")

print(" ".join(new_prices))
print(f"Profit: {profit:.2f}")

initial_budget += profit
if initial_budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")

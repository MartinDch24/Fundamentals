ORNAMENT_SET_PRICE = 2
SKIRT_PRICE = 5
GARLAND_PRICE = 3
LIGHTS_PRICE = 15

quantity_of_decorations = int(input())
remaining_days = int(input())
total_spirit = 0
total_cost = 0

for current_day in range(1, remaining_days + 1):
    if current_day % 11 == 0:
        quantity_of_decorations += 2
    if current_day % 2 == 0:
        total_cost += quantity_of_decorations * ORNAMENT_SET_PRICE
        total_spirit += 5
    if current_day % 3 == 0:
        total_cost += quantity_of_decorations * (SKIRT_PRICE + GARLAND_PRICE)
        total_spirit += 13
    if current_day % 5 == 0:
        total_cost += quantity_of_decorations * LIGHTS_PRICE
        total_spirit += 17
        if current_day % 3 == 0:
            total_spirit += 30

    if current_day % 10 == 0:
        total_spirit -= 20
        total_cost += SKIRT_PRICE + LIGHTS_PRICE + GARLAND_PRICE

if remaining_days % 10 == 0:
    total_spirit -= 30

print(f"Total cost: {total_cost}")
print(f"Total spirit: {total_spirit}")

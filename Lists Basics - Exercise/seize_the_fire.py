fires = input().split("#")
water = int(input())
effort = 0
total_fire = 0
cells_to_print = []

for i in range(len(fires)):
    type_of_fire, value_of_cell = fires[i].split(" = ")
    value_of_cell = int(value_of_cell)
    if type_of_fire == "Low" and 1 <= value_of_cell <= 50:
        if water >= value_of_cell:
            water -= value_of_cell
            effort += 0.25 * value_of_cell
            total_fire += value_of_cell
            cells_to_print.append(f" - {value_of_cell}")
        else:
            continue
    elif type_of_fire == "Medium" and 51 <= value_of_cell <= 80:
        if water >= value_of_cell:
            water -= value_of_cell
            effort += 0.25 * value_of_cell
            total_fire += value_of_cell
            cells_to_print.append(f" - {value_of_cell}")
        else:
            continue
    elif type_of_fire == "High" and 81 <= value_of_cell <= 125:
        if water >= value_of_cell:
            water -= value_of_cell
            effort += 0.25 * value_of_cell
            total_fire += value_of_cell
            cells_to_print.append(f" - {value_of_cell}")
        else:
            continue

print("Cells:")
for element in cells_to_print:
    print(element)
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

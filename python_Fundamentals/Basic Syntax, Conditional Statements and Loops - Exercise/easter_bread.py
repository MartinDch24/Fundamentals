budget = float(input())
price_flour = float(input())
price_eggs = 0.75 * price_flour
price_milk = 1.25/4 * price_flour

loaf_cost = price_flour + price_eggs + price_milk
colored_eggs_count = 0

total_loafs = budget // loaf_cost
total_loafs = int(total_loafs)
total_loaf_cost = total_loafs * loaf_cost

for current_bread_count in range(1, total_loafs + 1):
    colored_eggs_count += 3
    if current_bread_count % 3 == 0:
        colored_eggs_count -= (current_bread_count - 2)

print(f"You made {total_loafs} loaves of Easter bread!"
      f" Now you have {colored_eggs_count}"
      f" eggs and {budget - total_loaf_cost:.2f}BGN left.")

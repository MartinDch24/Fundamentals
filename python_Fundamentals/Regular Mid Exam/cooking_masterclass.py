from math import ceil

budget = float(input())
students = int(input())
flour_price = float(input())
egg_price = float(input())
apron_price = float(input())
sum_of_prices = 0.0

flour = 0.0
eggs = egg_price * 10 * students
aprons = apron_price * ceil(students * 1.20)

for i in range(1, students+1):
    if i % 5 != 0:
        flour += flour_price

sum_of_prices = flour + eggs + aprons
if sum_of_prices <= budget:
    print(f"Items purchased for {sum_of_prices:.2f}$.")
else:
    print(f"{sum_of_prices - budget:.2f}$ more needed.")

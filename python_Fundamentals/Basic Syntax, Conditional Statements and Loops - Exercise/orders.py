orders = int(input())
price = 0.00
total_price = 0.00

for _ in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not 0.01 <= price_per_capsule <= 100.00 or\
            not 1 <= days <= 31 or\
            not 1 <= capsules_per_day <= 2000:
        continue

    price = price_per_capsule * days * capsules_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total_price:.2f}")

def order(current_product: str, current_quantity: int) -> float:
    if current_product == "coffee":
        price = 1.50 * current_quantity
    elif current_product == "water":
        price = 1.00 * current_quantity
    elif current_product == "coke":
        price = 1.40 * current_quantity
    elif current_product == "snacks":
        price = 2.00 * current_quantity
    return price


product = input()
quantity = int(input())
result = order(product, quantity)
print(f"{result:.2f}")

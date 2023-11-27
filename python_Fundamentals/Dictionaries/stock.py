data = input().split()
products = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = data[i+1]
    products[key] = int(value)

products_to_search = input().split()

for element in products_to_search:
    if element in products.keys():
        print(f"We have {products[element]} of {element} left")
    else:
        print(f"Sorry, we don't have {element}")

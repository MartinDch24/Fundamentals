numbers = int(input())

for number in range(1, numbers + 1):
    digit_count = 0
    is_special = False
    for digit in str(number):
        digit_count += int(digit)
        if digit_count in [5, 7, 11]:
            is_special = True

    print(f"{number} -> {is_special}")

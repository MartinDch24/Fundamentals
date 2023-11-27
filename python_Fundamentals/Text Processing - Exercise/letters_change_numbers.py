strings = input().split()
total_sum = 0.0
for string in strings:
    if string[0].isupper():
        new_number = int(string[1:-1]) / (ord(string[0]) - 64)
    else:
        new_number = int(string[1:-1]) * (ord(string[0]) - 96)

    if string[-1].isupper():
        new_number -= (ord(string[-1]) - 64)
    else:
        new_number += (ord(string[-1]) - 96)

    total_sum += new_number

print(f"{total_sum:.2f}")

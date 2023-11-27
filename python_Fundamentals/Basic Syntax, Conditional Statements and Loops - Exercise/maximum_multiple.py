divisor = int(input())
boundary = int(input())
max_number = 0

for current_number in range(boundary, 0, -1):
    if current_number % divisor == 0:
        if current_number > max_number:
            max_number = current_number

print(max_number)

lines = int(input())
filtered = []
numbers = [int(input()) for _ in range(lines)]

command = input()

for num in numbers:
    filtered_command = ((command == "even" and num % 2 == 0) or
                        (command == "odd" and num % 2 != 0) or
                        (command == "positive" and num >= 0) or
                        (command == "negative" and num < 0))

    if filtered_command:
        filtered.append(num)

print(filtered)

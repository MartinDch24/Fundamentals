numbers = list(map(int, input().split(", ")))

indices = map(lambda x: x if numbers[x] % 2 == 0 else 'None', range(len(numbers)))
even_indices = list(filter(lambda a: a != 'None', indices))

print(even_indices)

def is_even(number):
    if number % 2 == 0:
        return True
    return False


numbers_as_string = input().split()
numbers_as_int = []
for current_number in numbers_as_string:
    numbers_as_int.append(int(current_number))
result = list(filter(is_even, numbers_as_int))

print(result)

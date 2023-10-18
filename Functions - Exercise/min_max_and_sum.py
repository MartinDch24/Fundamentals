def min_max_and_sum(some_list: list) -> int:
    int_numbers = []
    for number in some_list:
        int_numbers.append(int(number))
    smallest = min(int_numbers)
    largest = max(int_numbers)
    sum_of_numbers = sum(int_numbers)
    return smallest, largest, sum_of_numbers


numbers = input().split()
minimum, maximum, sum_of_all_numbers = min_max_and_sum(numbers)

print(f"The minimum number is {minimum}")
print(f"The maximum number is {maximum}")
print(f"The sum number is: {sum_of_all_numbers}")

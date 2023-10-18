def sort(some_list: list) -> list:
    some_sorted_list = sorted(some_list, key=int)
    for i in range(len(some_sorted_list)):
        some_sorted_list[i] = int(some_sorted_list[i])
    return some_sorted_list


numbers = input().split()
sorted_list = sort(numbers)
print(sorted_list)

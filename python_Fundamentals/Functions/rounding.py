def rounding(current_list: list) -> list:
    rounded_list = []
    for i in range(len(current_list)):
        rounded_list.append(round(current_list[i]))
    return rounded_list


numbers = input().split()
float_numbers = [float(num) for num in numbers]
result = rounding(float_numbers)
print(result)

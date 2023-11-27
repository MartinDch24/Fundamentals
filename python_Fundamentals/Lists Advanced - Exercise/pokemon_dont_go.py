distances = [int(num) for num in input().split()]
sum_of_elements = 0

while distances:
    current_element = int(input())
    element_value = 0
    if current_element < 0:
        element_value = distances[0]
        distances[0] = distances[-1]
    elif current_element > len(distances) - 1:
        element_value = distances[-1]
        distances[-1] = distances[0]
    else:
        element_value = distances[current_element]
        del distances[current_element]
    sum_of_elements += element_value

    for i in range(len(distances)):
        if element_value < distances[i]:
            distances[i] = distances[i] - element_value
        elif element_value >= distances[i]:
            distances[i] = distances[i] + element_value

print(sum_of_elements)

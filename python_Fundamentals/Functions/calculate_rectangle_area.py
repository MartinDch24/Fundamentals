def area(current_length: int, current_width: int) -> int:
    calculated_area = current_length * current_width
    return calculated_area


length = int(input())
width = int(input())
result = area(length, width)
print(result)

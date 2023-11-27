first_num = int(input())
second_num = int(input())
third_number = int(input())
largest_num = first_num

if largest_num < second_num:
    largest_num = second_num
if largest_num < third_number:
    largest_num = third_number

print(largest_num)

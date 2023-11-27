def calculator(operator, first, second):
    if operator == "add":
        return first + second
    elif operator == "subtract":
        return first - second
    elif operator == "multiply":
        return first * second
    elif operator == "divide":
        return first / second


input_operator = input()
first_number = int(input())
second_number = int(input())

result = int(calculator(input_operator, first_number, second_number))

print(result)

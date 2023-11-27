number_of_strings = int(input())
current_string = ""
pure_or_not_pure = ""
for _ in range(number_of_strings):
    current_string = input()
    if "." in current_string or\
            "," in current_string or\
            "_" in current_string:
        pure_or_not_pure = "not pure!"
    else:
        pure_or_not_pure = "pure."

    print(f"{current_string} is {pure_or_not_pure}")

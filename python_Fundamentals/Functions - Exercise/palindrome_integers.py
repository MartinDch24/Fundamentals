def is_palindrome(number: str) -> bool:
    if number == number[::-1]:
        return True
    return False


list_of_numbers = input().split(", ")
for list_of_numbers in list_of_numbers:
    print(is_palindrome(list_of_numbers))

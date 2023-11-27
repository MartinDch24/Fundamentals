def password_validator(some_password: str) -> list:
    list_of_errors = []
    if len(some_password) < 6 or 10 < len(some_password):
        list_of_errors.append("Password must be between 6 and 10 characters")
    if not some_password.isalnum():
        list_of_errors.append("Password must consist only of letters and digits")
    digits = 0
    for char in some_password:
        if char.isdigit():
            digits += 1
    if digits < 2:
        list_of_errors.append("Password must have at least 2 digits")
    return list_of_errors


password = input()
validated_password = password_validator(password)
if not validated_password:
    print("Password is valid")
else:
    print('\n'.join(validated_password))

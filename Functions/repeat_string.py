def repeat(some_string, counter) -> str:
    new_string = some_string * counter
    return new_string


string = input()
n = int(input())
result = repeat(string, n)
print(result)

strings = input().split()

for word in strings:
    length = len(word)
    print(word*length, end="")

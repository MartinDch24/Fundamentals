lines = int(input())
key_word = input()
words = []
matching_words = []

for _ in range(lines):
    current_string = input()
    words.append(current_string)
    if key_word in current_string:
        matching_words.append(current_string)

print(words)
print(matching_words)

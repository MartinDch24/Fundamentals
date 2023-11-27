banned_words = input().split(", ")
text = input()
for current_word in banned_words:
    new_word = "*" * len(current_word)
    while current_word in text:
        text = text.replace(current_word, new_word)
print(text)

text = input()
capital_letter_positions = []
for i in range(len(text)):
    if text[i].isupper():
        capital_letter_positions.append(i)
print(capital_letter_positions)

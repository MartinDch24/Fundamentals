words = input().split()
deciphered_words = []
for word in words:
    word = list(word)
    if word[2].isdigit():
        word[3], word[-1] = word[-1], word[3]
        letter = chr(int(''.join(word[0:3])))
        word[0:3] = letter
        deciphered_words.append(''.join(word))
    else:
        word[2], word[-1] = word[-1], word[2]
        letter = chr(int(''.join(word[0:2])))
        word[0:2] = letter
        deciphered_words.append(''.join(word))


print(' '.join(deciphered_words))

word = input()
no_vowels = [char for char in word if char.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(no_vowels))

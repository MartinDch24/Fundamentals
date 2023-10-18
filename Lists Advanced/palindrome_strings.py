words = input().split()
palindromes = [pal for pal in words if pal == pal[::-1]]
searched_palindrome = input()
times_word_is_repeated = palindromes.count(searched_palindrome)

print(palindromes)
print(f"Found palindrome {times_word_is_repeated} times")

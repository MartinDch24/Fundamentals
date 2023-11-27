import re

text = input()
pattern = r'(?i)(sand|water|sun|fish)'
matches = re.findall(pattern, text)
print(len(matches))

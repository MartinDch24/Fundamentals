import re

phone_numbers = input()

regex_pattern = r'\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b'
matches = re.findall(regex_pattern, phone_numbers)

print(", ".join(matches))

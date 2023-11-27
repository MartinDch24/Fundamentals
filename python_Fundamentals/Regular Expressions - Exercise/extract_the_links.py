import re

valid_urls = []
pattern = r"(w{3}\.[A-Za-z0-9\-\.]+\.[a-z]+)"
line = input()
while line:
    match = re.search(pattern, line)
    if match:
        valid_url = match.group(1)
        valid_urls.append(valid_url)
    line = input()
print("\n".join(valid_urls))

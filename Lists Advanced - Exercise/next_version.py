version = input().split(".")
new_version = int("".join(version)) + 1
new_version = ".".join(str(new_version))
print(new_version)

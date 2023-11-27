lines = int(input())
entries = {}
for _ in range(lines):
    command = input().split()
    if command[0] == "register":
        username, license_plate = command[1], command[2]
        if username not in entries.keys():
            entries[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {entries[username]}")

    elif command[0] == "unregister":
        username = command[1]
        if username in entries.keys():
            print(f"{username} unregistered successfully")
            del entries[username]
        else:
            print(f"ERROR: user {username} not found")

for username, plate in entries.items():
    print(f"{username} => {plate}")

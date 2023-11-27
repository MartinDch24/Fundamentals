usernames = {}
languages = {}
while True:
    command = input()
    if command == "exam finished":
        break

    data = command.split("-")
    username = data[0]
    if len(data) == 3:
        language = data[1]
        points = int(data[2])
        if username not in usernames.keys():
            usernames[username] = {'points': points, 'language': [language]}
        else:
            if usernames[username]['points'] < points:
                usernames[username]['points'] = points
        if language not in usernames[username]['language']:
            usernames[username]['language'].append(language)
        if language not in languages:
            languages[language] = 1
        else:
            languages[language] += 1
    else:
        if username in usernames.keys():
            usernames[f'banned-{username}'] = usernames.pop(username)

print("Results:")
for username in usernames.keys():
    if "banned-" not in username:
        print(f"{username} | {usernames[username]['points']}")
print("Submissions:")
for language, students in languages.items():
    print(f"{language} - {students}")

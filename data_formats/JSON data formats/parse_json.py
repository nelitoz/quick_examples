import json

with open("user.json", "r") as fhand:
    data = json.load(fhand)

user = data['user']
print(user)

for role in user["roles"]:
    print(role)

user['location']['state'] = "Texas"

with open("user.json", "w") as fhand:
    json.dump(data, fhand, indent=4)

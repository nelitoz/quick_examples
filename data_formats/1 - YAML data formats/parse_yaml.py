import yaml

with open("user.yml") as fhand:
    data = yaml.safe_load(fhand)

user = data['user']
print(user['name'])

for role in user["roles"]:
    print(role)
user['location']['city'] = "CDMX"

with open("user.yml", 'w') as fhand:
    yaml.dump(user, fhand, default_flow_style=False)

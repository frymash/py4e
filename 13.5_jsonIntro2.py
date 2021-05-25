import json

data = '''[

    {
    "id":"001",
    "x":"1",
    "name":"Alpha"
    },

    {
    "id":"002",
    "x":"2",
    "name":"Bravo"
    }

]'''

info = json.loads(data)
print("User count:", len(info),"\n")
for item in info:
    print("Name:",item['name'])
    print("ID:",item['id'])
    print("Attribute:",item['x'],"\n")

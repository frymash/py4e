import json

data = '''{
    "name":"Isaac",
    "phone": {
        "type":"intl",
        "number": "+65 8490 5180"
    },
    "email": {
        "hide":"yes"
    }
}'''

info = json.loads(data)
print('Name:',info["name"])
print("Attribute:",info["email"]["hide"])

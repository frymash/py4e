import xml.etree.ElementTree as et

input = ''' <stuff>
    <users>
        <user x="1">
            <id>001</id>
            <name>Alpha</name>
        </user>

        <user x="2">
            <id>002</id>
            <name>Bravo</name>
        </user>
    </users>
</stuff> '''

stuff = et.fromstring(input)
lst = stuff.findall('users/user')
print('User count:',len(lst),'\n')
for item in lst: # for each user in users,
    print('Name:', item.find('name').text)
    print('ID:', item.find('id').text)
    print('Attribute:',item.get("x"),'\n') # get attribute in self-closing tag

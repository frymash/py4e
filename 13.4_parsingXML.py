import xml.etree.ElementTree as et
data = '''<person>
    <name>Isaac</name>
    <phone type="intl">
        +65 8490 5180
    </phone>
    <email hide="yes"/>
</person>'''

tree = et.fromstring(data)
print('Name:', tree.find('name').text)
print('Attribute:', tree.find('email').get('hide'))

# Returns the following lines:
# Name: Isaac
# Attribute: yes

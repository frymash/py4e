from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

print('---Extracting Data from XML---\n\n')

url = input('Enter URL: ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Load XML data from the URL into the ET and sum all counts.
xml = urlopen(url, context=ctx).read()
commentinfo = ET.fromstring(xml)
sum = 0
for count in commentinfo.findall('.//count'):
    sum += int(count.text)
print('\nSum:', sum)

''' At line 17, an alternative method could be used where the 'comments' node
is evaluated before a for loop is run through its child nodes:

comments = commentinfo.findall('comments/comment')
sum = 0

for comment in comments:
    sum += int(comment.find('count').text)

print('\nSum:', sum)
'''



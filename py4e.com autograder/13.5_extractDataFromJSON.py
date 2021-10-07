from urllib.request import urlopen
import json
import ssl

print('---Extracting Data from JSON---\n\n')

url = input('Enter URL - ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Load JSON data from link
data = urlopen(url, context=ctx).read()
info = json.loads(data)

sum = 0
for item in info['comments']:
    sum += item['count']

print('Sum:', sum)
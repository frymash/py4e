from urllib.request import urlopen
from urllib.parse import urlencode
import json
import ssl

print('---Calling a JSON API - Using the geoJSON API---\n\n')

api_key = False

if api_key is False:
    api_key = 42
    service_url = 'http://py4e-data.dr-chuck.net/json?'
else:
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

address = input('Enter location: ')

# Generating API URL for the address from the location input.
parms = dict()
parms['address'] = address
if api_key is not False:
    parms['key'] = api_key
url = service_url + urlencode(parms)

# Retrieving JSON information (place_id of the location) from the URL.
print('Retrieving:', url)
data = urlopen(url, context=ctx).read()
info = json.loads(data)
print('Retrieved:', len(data), 'characters')
print('place_id:', info['results'][0]['place_id']) # [0] must be included as info['results'] is a list and not a dict
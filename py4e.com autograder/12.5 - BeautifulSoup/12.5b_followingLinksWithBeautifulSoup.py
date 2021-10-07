print('---Following Links in Python---')
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Please enter a URL - ')
pos = int(input('Which link number would you like to access? '))-1
num_repetitions = int(input('How many times do you want to repeat this process? '))

for i in range(num_repetitions):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')   
    # Retrieve all of the anchor tags
    tags = soup('a')
    url = tags[pos].get('href', None)
    print('Retrieving: ', url)

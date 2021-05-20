# Notes on BeautifulSoup:
# The installation for the 'beautifulsoup4' package can be done by either
# downloading the .zip package from a browser or by using the command line.

# When using the command line, type 'pip3 install beautifulsoup' to install the
# beautifulsoup4 (bs4) package. If running this .py script doesn't work due to
# missing modules, find out where the pip3 command installed bs4 and copy
# the package over to your working directory. It should work fine from there.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup # BeautifulSoup is NOT a module; it's a class in bs4.
# import ssl

# ignore SSL certificate errors
# ctx = ssl.create_default_context()
# ctx.check_hostname = False
# ctx.verify_mode = ssl.CERT_NONE

print('----------------------------------------------')
print('HTML Parser with BeautifulSoup: Link Retriever')
print('----------------------------------------------')

print('The purpose of this script is to extract links from a HTML page.\n')

url = input('Enter the URL to the webpage you want parsed: ')
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags.
tags = soup('a')
for tag in tags:
    print(tag.get('href', None))

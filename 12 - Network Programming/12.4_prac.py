# Aim: to read the webpage 'http://www.dr-chuck.com/page1.htm' via
# the Python shell.

import urllib.request
import urllib.parse
import urllib.error

handle = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in handle:
    print(line.decode().strip())

# Aim: show how many times each word in romeo.txt appears. romeo.txt is located
# in 'http://data.pr4e.org/romeo.txt'. Use the urllib library to complete
# this task.

import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

wcounts = dict()
for line in fhand:
    words = line.decode().split() # words in romeo.txt are received as bytes
    for word in words:
        wcounts[word] = wcounts.get(word, 0) + 1
print(wcounts)

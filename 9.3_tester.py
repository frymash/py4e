# Line counter

# Register line input
line = input('Enter line here: ')
# Generate list of words from line and add them to a dictionary (wordCount)
wordCount = dict()
words = line.split()
for word in words:
    wordCount[word] = wordCount.get(word,0) + 1
print('Number of times each word appears:', wordCount)

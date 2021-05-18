mail = open('mbox-short.txt')
for line in mail:
    words = line.split()
    address = words[1]
    domain = address.split('@')
    print('Domain found:', domain[1])

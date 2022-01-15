name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

tcounts = dict()

for line in handle:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        words = line.split()
        time = words[5]
        hour = time[0:2]
        tcounts[hour] = tcounts.get(hour,0)+1

lst = sorted(tcounts.items())

# 21/12 2021 note:
# alternatively,
# lst = list(tcounts.items())
# lst.sort()

for k,v in lst:
	print(k,v)

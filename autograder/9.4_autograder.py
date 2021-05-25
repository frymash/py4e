name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

commits = dict()

for line in handle:

    if line.startswith('From'):
        if line.startswith('From:'):
            continue
    	words = line.split()
        email = words[1]
        commits[email] = commits.get(email,0)+1

bestCommitter = max(commits, key=commits.get)
print(bestCommitter, commits[bestCommitter])

'''
A variation which breeds the same result goes as follows:

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

commits = dict()

for line in handle:

    if line.startswith('From'):
        if line.startswith('From:'):
            continue
    	words = line.split()
        email = words[1]
        commits[email] = commits.get(email,0)+1

bestCommitter = None
mostCommits = None
for k,v in commits.items():
    if bestCommitter is None:
        bestCommitter = k
        mostCommits = v
    if v > mostCommits:
		bestCommitter = k
		mostCommits = v

print(bestCommitter,mostCommits)

'''

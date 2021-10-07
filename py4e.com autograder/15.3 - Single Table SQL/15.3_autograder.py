import sqlite3

print('---Counting Emails in a Database: Counting Organisations---')

con = sqlite3.connect('15.3_emaildb.sqlite')
cur = con.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('''CREATE TABLE Counts(
    org TEXT,
    count INTEGER
)
''')

fname = input('Enter filename: ')
if len(fname) < 1:
    fname = 'mbox.txt'
fh = open(fname)

count = 0

for line in fh:
    if not line.startswith('From:'):
        continue
    words = line.split()
    address = words[1]
    split_address = address.split('@')
    org = split_address[1]
    cur.execute('SELECT * FROM Counts WHERE org = ?', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(org, count) VALUES (?,1)',(org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',(org,))
    con.commit()
    count += 1

print('Total number of email domains:', count)
cur.close()

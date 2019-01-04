import sqlite

conn = sqlite3.connect('orgdb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

orgMap = {}
fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox.txt'
fh = open(fname)
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    parts = email.split('@')
    org = parts[-1]
    orgMap[org] = orgMap.get(org, 0) + 1

for org in orgMap:
    #print(org, orgMap[org])
    cur.execute('''INSERT INTO Counts (org, count) 
                VALUES ( ?, ? )''', ( org, orgMap[org],) )
    conn.commit()

# print("updated done")
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 100'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

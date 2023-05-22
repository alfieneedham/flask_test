import sqlite3

# conn.execute('''CREATE TABLE USERSDB
#          (USERNAME TEXT PRIMARY KEY     NOT NULL,
#          REALNAME       TEXT    NOT NULL,
#          PASSWORD       TEXT    NOT NULL);''')

conn = sqlite3.connect('vault/users.db')
print ("Opened database successfully")

cursor = conn.execute("SELECT USERNAME, REALNAME, PASSWORD from USERSDB")
for row in cursor:
   print("USERNAME = ", row[0])
   print("REALNAME = ", row[1])
   print("PASSWORD = ", row[2], "\n")

print ("Operation done successfully")
conn.close()
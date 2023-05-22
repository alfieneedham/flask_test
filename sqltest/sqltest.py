import sqlite3

username = "ADMINN"

# conn.execute('''CREATE TABLE USERSDB
#          (USERNAME TEXT PRIMARY KEY     NOT NULL,
#          REALNAME       TEXT    NOT NULL,
#          PASSWORD       TEXT    NOT NULL);''')

conn = sqlite3.connect('vault/users.db')
print ("Opened database successfully", "\n")

cursor = conn.execute("SELECT USERNAME, REALNAME, PASSWORD FROM USERSDB")
for row in cursor:
   print("REALNAME =", row[1])
   print("USERNAME =", row[0])
   print("PASSWORD =", row[2], "\n")
print ("Operation done successfully")

# cur = conn.cursor()
# cur.execute("SELECT PASSWORD FROM USERSDB WHERE USERNAME=?",[username])
# result = cur.fetchone()
# print(result)
# if "ADMIN" == str(*result):
#     print(True)
# else:
#     print(False)



conn.close()
import sqlite3

db = sqlite3.connect("version1.db")

for row in db.execute("SELECT * FROM account"):
    print(row)


def print(row1):
    pass


for row1 in db.execute("SELECT * FROM vaccine_date"):
    print(row1)
db.close()

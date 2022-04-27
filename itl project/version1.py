import sqlite3

db = sqlite3.connect("version1.db")

cursor = db.cursor()
# cursor.execute("CREATE TABLE IF NOT EXISTS account (client_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
#                "c_name VARCHAR(30), p_name VARCHAR(30), c_dob DATE,"
#                " email VARCHAR(30))")
# cursor.execute("ALTER TABLE account ADD client_id INTEGER")
# cursor.execute("ALTER TABLE account ADD PRIMARY KEY client_id")
# cursor.execute("UPDATE account SET client_id = 1000")
# cursor.execute("DELETE FROM account")
# cursor.execute("CREATE TABLE IF NOT EXISTS vaccine_date (vaccine_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
#                " BCG TEXT, OPV TEXT,"
#                "IPV TEXT, PENTAVALENT TEXT,"
#                "MEASLES1 TEXT, VITAMINA TEXT, DPT TEXT,"
#                "FOREIGN KEY (vaccine_id) REFERENCES account(client_id))")
# cursor.execute("UPDATE vaccine_date SET vaccine_id = 1000")
# cursor.execute("CREATE TABLE IF NOT EXISTS vaccine_master (vacc_name VARCHAR(20), vacc_due VARCHAR(20))")
# cursor.execute("INSERT INTO vaccine_master VALUES('BCG','+1 year'),('OPV','+15 day'),('IPV','+98 day'),"
#                "('PENTAVALENT','+42 day'),('MEASLES1','+9 month'),('VITAMINA','+9 month'),('DPT','+16 month')")
# cursor.execute("INSERT INTO vaccine_master VALUES('BCG','1 year'),('OPV','15 day'),('IPV','98 day'),
# ('PENTAVALENT','42 day'),('MEASLES1','9 month'),('VITAMINA','9 month'),('DPT','16 month')")
# cursor.execute("CREATE TABLE IF NOT EXISTS vaccine_date (vaccine_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
#                " BCG DATE, OPV DATE,"
#                "IPV DATE, PENTAVALENT DATE,"
#                "MEASLES1 DATE, VITAMINA DATE, DPT DATE,"
#                "FOREIGN KEY (vaccine_id) REFERENCES account(client_id))")
# cursor.execute("CREATE TABLE IF NOT EXISTS vaccine_date (vaccine_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
#                " BCG DATE, OPV DATE,"
#                "IPV DATE, PENTAVALENT DATE,"
#                "MEASLES1 DATE, VITAMINA DATE, DPT DATE,"
#                "FOREIGN KEY (vaccine_id) REFERENCES account(client_id))")
# cursor.execute("UPDATE vaccine_date SET vaccine_id = 1000")

cursor.connection.commit()
cursor.close()
db.close()

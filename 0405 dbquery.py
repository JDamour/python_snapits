import sqlite3 as db

conn = db.connect('test.db')
conn.row_factory = db.Row
cursor = conn.cursor()

cursor.execute("select * from person")
rows = cursor.fetchall()
for row in rows:
   print("%s %s %s %s" % (row["id"], row["name"], row["email"], row['age']))
conn.close()

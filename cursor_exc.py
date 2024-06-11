import sqlite3

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

sql = "INSERT INTO Students (name, group_id) VALUES ('Don Pollo', 1)"
cursor.execute(sql)

conn.commit()

conn.close()

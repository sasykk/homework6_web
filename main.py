from faker import Faker
import sqlite3

fake = Faker()

conn = sqlite3.connect('mydatabase.db')
cursor = conn.cursor()

for _ in range(30):
    name = fake.name()
    group_id = fake.random_int(min=1, max=3)
    cursor.execute("INSERT INTO Students (name, group_id) VALUES (?, ?)", (name, group_id))
  
conn.commit()

conn.close()

import sqlite3

conn = sqlite3.connect('scorss.db')
cur = conn.cursor()

cur.execute("""
INSERT INTO citizens (first_name, middle_name, last_name, gender, birth_date, address, contact_number, email)
VALUES (?, ?, ?, ?, ?, ?, ?, ?)
""", ("Juan", "Dela", "Cruz", "Male", "1955-06-22", "Baybay, Leyte", "09123456789", "juan@example.com"))

conn.commit()
print("Inserted sample citizen id:", cur.lastrowid)
conn.close()
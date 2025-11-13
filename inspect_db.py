import sqlite3, pathlib, json

db = 'scorss.db'
if not pathlib.Path(db).exists():
    print("DB file not found:", db)
    raise SystemExit

conn = sqlite3.connect(db)
cur = conn.cursor()

# list tables
cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = [r[0] for r in cur.fetchall()]
print("Tables:", tables)

# show first 5 rows of each table
for t in tables:
    print(f"\n--- {t} (up to 5 rows) ---")
    try:
        cur.execute(f"SELECT * FROM {t} LIMIT 5;")
        rows = cur.fetchall()
        for r in rows:
            print(r)
        if not rows:
            print("(no rows)")
    except Exception as e:
        print("error reading table:", e)

conn.close()
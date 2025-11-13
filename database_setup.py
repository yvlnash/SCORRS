import sqlite3

conn = sqlite3.connect('scorss.db')   # file will be created in project root
cursor = conn.cursor()

schema = """
CREATE TABLE IF NOT EXISTS citizens (
    citizen_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    middle_name TEXT,
    last_name TEXT NOT NULL,
    gender TEXT CHECK(gender IN ('Male', 'Female', 'Other')),
    birth_date DATE,
    address TEXT,
    contact_number TEXT,
    email TEXT UNIQUE,
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS verification (
    verification_id INTEGER PRIMARY KEY AUTOINCREMENT,
    citizen_id INTEGER NOT NULL,
    senior_citizen_id_number TEXT,
    government_id_number TEXT,
    barangay_certificate_number TEXT,
    verified INTEGER DEFAULT 0,
    verification_date TIMESTAMP,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)
);

CREATE TABLE IF NOT EXISTS documents (
    document_id INTEGER PRIMARY KEY AUTOINCREMENT,
    citizen_id INTEGER NOT NULL,
    doc_type TEXT CHECK(doc_type IN ('Senior ID', 'Government ID', 'Barangay Certificate', 'Birth Certificate', 'Medical Certificate')),
    file_name TEXT,
    file_path TEXT,
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)
);

CREATE TABLE IF NOT EXISTS submissions (
    submission_id INTEGER PRIMARY KEY AUTOINCREMENT,
    citizen_id INTEGER NOT NULL,
    submission_code TEXT UNIQUE,
    submission_status TEXT DEFAULT 'Pending',
    submission_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)
);
"""

cursor.executescript(schema)
conn.commit()
conn.close()
print("scorss.db created (or already exists) and schema applied")
import sqlite3
from hashlib import sha256

DB_NAME = "users.db"

def create_users_table():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            email TEXT UNIQUE,
            password TEXT,
            phone TEXT,
            age INTEGER,
            address TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def add_user(name, email, password, phone, age, address):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    hashed_pw = sha256(password.encode()).hexdigest()
    try:
        c.execute(
            "INSERT INTO users (name, email, password, phone, age, address) VALUES (?, ?, ?, ?, ?, ?)",
            (name, email, hashed_pw, phone, age, address)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def verify_user(email, password):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    hashed_pw = sha256(password.encode()).hexdigest()
    c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, hashed_pw))
    user = c.fetchone()
    conn.close()
    return user

def get_all_users():
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT name, email, phone, age, address, created_at FROM users")
    rows = c.fetchall()
    conn.close()
    return rows
def get_user_by_email(email):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE email=?", (email,))
    user = c.fetchone()
    conn.close()
    return user
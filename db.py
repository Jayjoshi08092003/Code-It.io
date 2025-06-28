# db.py
import sqlite3
from datetime import datetime

def connect_db():
    return sqlite3.connect("data.db", check_same_thread=False)

def create_user_table():
    conn = connect_db()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    language TEXT DEFAULT 'python',
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )''')
    conn.commit()
    conn.close()

def add_user(name, email, password, language='python'):
    conn = connect_db()
    c = conn.cursor()
    c.execute('INSERT INTO users (name, email, password, language) VALUES (?, ?, ?, ?)',
              (name, email, password, language))
    conn.commit()
    conn.close()

def get_user_by_email(email):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ?', (email,))
    data = c.fetchone()
    conn.close()
    return data

def get_all_users():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT id, name, email, language, created_at FROM users')
    data = c.fetchall()
    conn.close()
    return data
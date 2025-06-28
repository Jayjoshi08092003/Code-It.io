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
def update_user_language(email, language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('UPDATE users SET language = ? WHERE email = ?', (language, email))
    conn.commit()
    conn.close()
def delete_user(email):
    conn = connect_db()
    c = conn.cursor()
    c.execute('DELETE FROM users WHERE email = ?', (email,))
    conn.commit()
    conn.close()
def get_user_count():
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT COUNT(*) FROM users')
    count = c.fetchone()[0]
    conn.close()
    return count
def get_user_by_id(user_id):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE id = ?', (user_id,))
    data = c.fetchone()
    conn.close()
    return data
def get_user_by_name(name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name = ?', (name,))
    data = c.fetchone()
    conn.close()
    return data
def get_user_by_language(language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE language = ?', (language,))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_date_range(start_date, end_date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE created_at BETWEEN ? AND ?', (start_date, end_date))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_email(partial_email):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email LIKE ?', ('%' + partial_email + '%',))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_name(partial_name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name LIKE ?', ('%' + partial_name + '%',))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_language(partial_language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE language LIKE ?', ('%' + partial_language + '%',))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_date_range(partial_start_date, partial_end_date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE created_at BETWEEN ? AND ?', (partial_start_date, partial_end_date))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_email_and_password(email, password):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND password = ?', (email, password))
    data = c.fetchone()
    conn.close()
    return data
def get_user_by_email_or_name(email, name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? OR name = ?', (email, name))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_email_and_language(email, language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND language = ?', (email, language))
    data = c.fetchone()
    conn.close()
    return data
def get_user_by_email_and_date(email, date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND created_at = ?', (email, date))
    data = c.fetchone()
    conn.close()
    return data
def get_user_by_email_and_partial_name(email, partial_name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND name LIKE ?', (email, '%' + partial_name + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_email_and_partial_language(email, partial_language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND language LIKE ?', (email, '%' + partial_language + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_email_and_partial_date(email, partial_date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email = ? AND created_at LIKE ?', (email, '%' + partial_date + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_name_and_language(name, language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name = ? AND language = ?', (name, language))
    data = c.fetchone()
    conn.close()
    return data
def get_user_by_name_and_date(name, date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name = ? AND created_at = ?', (name, date))
    data = c.fetchone()
    conn.close()
    return data
def get_user_by_name_and_partial_language(name, partial_language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name = ? AND language LIKE ?', (name, '%' + partial_language + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_name_and_partial_date(name, partial_date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name = ? AND created_at LIKE ?', (name, '%' + partial_date + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_language_and_date(language, date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE language = ? AND created_at = ?', (language, date))
    data = c.fetchone()
    conn.close()
    return data
def get_user_by_language_and_partial_date(language, partial_date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE language = ? AND created_at LIKE ?', (language, '%' + partial_date + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_date_and_partial_language(date, partial_language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE created_at = ? AND language LIKE ?', (date, '%' + partial_language + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_date_and_partial_name(date, partial_name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE created_at = ? AND name LIKE ?', (date, '%' + partial_name + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_email_and_language(partial_email, language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email LIKE ? AND language = ?', ('%' + partial_email + '%', language))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_email_and_date(partial_email, date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email LIKE ? AND created_at = ?', ('%' + partial_email + '%', date))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_email_and_partial_name(partial_email, partial_name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email LIKE ? AND name LIKE ?', ('%' + partial_email + '%', '%' + partial_name + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_email_and_partial_language(partial_email, partial_language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email LIKE ? AND language LIKE ?', ('%' + partial_email + '%', '%' + partial_language + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_email_and_partial_date(partial_email, partial_date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE email LIKE ? AND created_at LIKE ?', ('%' + partial_email + '%', '%' + partial_date + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_name_and_language(partial_name, language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name LIKE ? AND language = ?', ('%' + partial_name + '%', language))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_name_and_date(partial_name, date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name LIKE ? AND created_at = ?', ('%' + partial_name + '%', date))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_name_and_partial_language(partial_name, partial_language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name LIKE ? AND language LIKE ?', ('%' + partial_name + '%', '%' + partial_language + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_name_and_partial_date(partial_name, partial_date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE name LIKE ? AND created_at LIKE ?', ('%' + partial_name + '%', '%' + partial_date + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_language_and_date(partial_language, date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE language LIKE ? AND created_at = ?', ('%' + partial_language + '%', date))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_language_and_partial_date(partial_language, partial_date):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE language LIKE ? AND created_at LIKE ?', ('%' + partial_language + '%', '%' + partial_date + '%'))
    data = c.fetchall()
    conn.close()
    return data
def get_user_by_partial_date_and_language(partial_date, language):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE created_at LIKE ? AND language = ?', ('%' + partial_date + '%', language))
    data = c.fetchall()
    conn.close()
    return data

def get_user_by_partial_date_and_name(partial_date, name):
    conn = connect_db()
    c = conn.cursor()
    c.execute('SELECT * FROM users WHERE created_at LIKE ? AND name = ?', ('%' + partial_date + '%', name))
    data = c.fetchall()
    conn.close()
    return data

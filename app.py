import streamlit as st
import sqlite3

# Connect to database
conn = sqlite3.connect("users.db", check_same_thread=False)
c = conn.cursor()

# Create user table
def create_table():
    c.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL
    )''')
    conn.commit()

# Insert user
def add_user(name, email, password):
    c.execute('INSERT INTO users (name, email, password) VALUES (?, ?, ?)', (name, email, password))
    conn.commit()

# Fetch users
def get_users():
    c.execute('SELECT * FROM users')
    return c.fetchall()

# Streamlit UI
st.title("User Registration App")
create_table()

name = st.text_input("Name")
email = st.text_input("Email")
password = st.text_input("Password", type="password")

if st.button("Register"):
    add_user(name, email, password)
    st.success("User registered successfully!")

if st.checkbox("Show All Users"):
    users = get_users()
    st.write(users)

import streamlit as st
from db import verify_user, create_users_table

def login_page():
    st.header("🔐 Login")

    create_users_table()

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = verify_user(email, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.user_email = email
            st.success(f"Welcome, {email}!")
        else:
            st.error("Invalid email or password.")


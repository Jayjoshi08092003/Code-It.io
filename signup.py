# signup.py
import streamlit as st
from db import add_user, get_user_by_email, create_user_table


def signup_page():
    st.subheader("Signup")
    name = st.text_input("Name", key="signup_name")
    email = st.text_input("Email", key="signup_email")
    password = st.text_input("Password", type="password", key="signup_password")
    language = st.selectbox("Preferred Language", ["python", "java", "c", "c++", "php", "ruby", "go", "kotlin"], key="signup_language")

    if st.button("Register", key="register_button"):
        if get_user_by_email(email):
            st.warning("User already exists. Please login.")
        else:
            add_user(name, email, password, language)
            st.success("Signup successful! Please log in.")
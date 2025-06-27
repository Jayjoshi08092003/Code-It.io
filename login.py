import streamlit as st
import pandas as pd

def login_page():
    st.header("🔐 Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        try:
            df = pd.read_csv("users.csv")
            user = df[(df["email"] == email) & (df["password"] == password)]
            if not user.empty:
                st.session_state.logged_in = True
                st.session_state.user_email = email
                st.success(f"Welcome, {email}!")
            else:
                st.error("Invalid email or password.")
        except FileNotFoundError:
            st.error("User database not found. Please sign up first.")

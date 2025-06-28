import streamlit as st
from db import get_user_by_email_and_password

def login_page():
    st.subheader("Login")
    email = st.text_input("Email", key="login_email")
    password = st.text_input("Password", type="password", key="login_password")

    if st.button("Login", key="login_button"):
        user = get_user_by_email_and_password(email, password)
        if user:
            st.session_state.logged_in = True
            st.session_state.user_email = user[2]
            st.success(f"Welcome {user[1]}!")
        else:
            st.error("Invalid credentials.")


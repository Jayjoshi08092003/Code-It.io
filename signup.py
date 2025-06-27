import streamlit as st
from db import add_user, create_users_table

def signup_page():
    st.header("📝 Signup")

    create_users_table()

    name = st.text_input("Full Name")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    phone = st.text_input("Phone")
    age = st.number_input("Age", min_value=1, max_value=120)
    address = st.text_area("Address")

    if st.button("Create Account"):
        if name and email and password and phone and address:
            success = add_user(name, email, password, phone, age, address)
            if success:
                st.success("Account created! You can now log in.")
            else:
                st.error("Email already exists.")
        else:
            st.warning("Please fill all fields.")

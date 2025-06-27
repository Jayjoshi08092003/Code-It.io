import streamlit as st
import pandas as pd
import os

def signup_page():
    st.header("📝 Signup")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Create Account"):
        if email and password:
            if os.path.exists("users.csv"):
                df = pd.read_csv("users.csv")
                if email in df["email"].values:
                    st.warning("Email already registered. Please login.")
                    return
            else:
                df = pd.DataFrame(columns=["email", "password"])

            df = df.append({"email": email, "password": password}, ignore_index=True)
            df.to_csv("users.csv", index=False)
            st.success("Account created successfully! Now go to Login.")
        else:
            st.warning("Please enter both email and password.")

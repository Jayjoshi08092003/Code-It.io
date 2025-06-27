import streamlit as st
from login import login_page
from signup import signup_page
from home import home_page

st.set_page_config(page_title="Code It.io", layout="centered")

# Track login status
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

# Navigation
page = st.sidebar.selectbox("Navigate", ["Login", "Signup", "Home"])

# Route pages
if page == "Login":
    login_page()
elif page == "Signup":
    signup_page()
elif page == "Home":
    if st.session_state.logged_in:
        home_page()
    else:
        st.warning("Please log in first.")

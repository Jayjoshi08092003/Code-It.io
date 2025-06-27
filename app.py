import streamlit as st
from login import login_page
from signup import signup_page
from home import home_page

st.set_page_config(page_title="Code It.io", layout="centered")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""

page = st.sidebar.selectbox("Go to", ["Login", "Signup", "Home"])

if page == "Login":
    login_page()
elif page == "Signup":
    signup_page()
elif page == "Home":
    if st.session_state.logged_in:
        home_page()
    else:
        st.warning("Please log in to view your dashboard.")

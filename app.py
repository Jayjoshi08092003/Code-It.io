import streamlit as st
from db import create_user_table
from login import login_page
from signup import signup_page
from home import home_page

# App Configuration
st.set_page_config(page_title="Code It.io", layout="wide")

# Initialize the DB table
create_user_table()

# Initialize session states
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = ""
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "user_language" not in st.session_state:
    st.session_state.user_language = ""

# Sidebar Navigation
st.sidebar.title("📘 Code It.io Navigation")
page = st.sidebar.radio("Choose a page:", ["Login", "Signup", "Home"])

# Page Routing
if page == "Login":
    login_page()
elif page == "Signup":
    signup_page()
elif page == "Home":
    if st.session_state.logged_in:
        home_page()
    else:
        st.warning("🔒 Please log in to view your dashboard.")

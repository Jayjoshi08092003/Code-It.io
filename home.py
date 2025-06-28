import streamlit as st
from db import get_user_by_email

def home_page():
    st.title("🏠 Central Home Page")
    email = st.session_state.get("user_email")
    if email:
        user = get_user_by_email(email)
        if user:
            st.markdown(f"### 👋 Welcome, {user[1]} ({user[2]})")
            st.markdown(f"**Preferred Language:** {user[4]}")
            st.markdown(f"**Joined On:** {user[5]}")
        else:
            st.error("User not found. Please login again.")
    else:
        st.warning("Please log in to access your home page.")
    st.markdown("---")
    st.markdown("### 📚 Available Features")
import streamlit as st

def home_page():
    st.header("🏠 Welcome to Your Dashboard")
    st.success(f"You are logged in as {st.session_state.user_email}")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_email = ""
        st.experimental_rerun()

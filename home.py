import streamlit as st
from db import get_all_users

def home_page():
    st.header("🏠 Dashboard")

    st.success(f"Logged in as: {st.session_state.user_email}")

    # View users (admin dashboard)
    st.subheader("📋 Registered Users")
    users = get_all_users()

    if users:
        for user in users:
            st.markdown(f"""
                **Name:** {user[0]}  
                **Email:** {user[1]}  
                **Phone:** {user[2]}  
                **Age:** {user[3]}  
                **Address:** {user[4]}  
                **Signed Up On:** {user[5]}  
                ---
            """)
    else:
        st.info("No users registered yet.")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.user_email = ""
        st.success("You have been logged out.")
        st.experimental_rerun()

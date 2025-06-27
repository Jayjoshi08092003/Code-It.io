import streamlit as st
import re

st.set_page_config(page_title="Signup Page", page_icon="📝")

# Title
st.title("📝 Sign Up Page")

# User Input
username = st.text_input("Username")
email = st.text_input("Email")
password = st.text_input("Password", type="password")
confirm_password = st.text_input("Confirm Password", type="password")

# Email Validation Function
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

# Signup Button
if st.button("Sign Up"):
    if not username or not email or not password or not confirm_password:
        st.warning("🚨 Please fill in all fields.")
    elif not is_valid_email(email):
        st.error("❌ Invalid email format.")
    elif password != confirm_password:
        st.error("🔑 Passwords do not match.")
    else:
        # Simulate success (add DB logic here)
        st.success(f"✅ Account created successfully for {username}!")
        st.info("👉 You can now proceed to log in.")

# Footer
st.markdown("---")
st.markdown("Already have an account? [Click here to login](#)", unsafe_allow_html=True)

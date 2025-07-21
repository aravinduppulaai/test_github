import streamlit as st
import app

st.title("Login App (Streamlit UI)")

if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'username' not in st.session_state:
    st.session_state.username = ''

username = st.text_input("Username", value=st.session_state.username)
password = st.text_input("Password", type="password")

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Login"):
        if app.login(username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success(f"Logged in as {username}")
        else:
            st.warning("Username and password required.")

with col2:
    if st.button("Logout"):
        app.logout()
        st.session_state.logged_in = False
        st.session_state.username = ''
        st.info("Logged out.")

with col3:
    if st.button("Show User Details"):
        if app.current_user:
            st.info(f"Current user: {app.current_user}")
        else:
            st.info("No user is currently logged in.")

if st.session_state.logged_in:
    st.write(f"Welcome, {st.session_state.username}!") 
import streamlit as st


def login(session_state):
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Your authentication logic here
        # Here, you can validate the username and password
        # For simplicity, we'll just assume any non-empty username and password are valid
        if username and password:
            session_state.logged_in = True
            session_state.username = username
            session_state.password = password
        else:
            st.error("Invalid username or password")

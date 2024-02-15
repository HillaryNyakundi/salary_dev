import streamlit as st
from app import session_state


def show_login_page():
    st.title("Login")

    if not session_state.logged_in:
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
    else:
        st.write("You are already logged in.")


if __name__ == "__main__":
    show_login_page()

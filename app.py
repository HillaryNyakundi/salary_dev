import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Define a session state class


class SessionState:
    def __init__(self):
        self.logged_in = False
        self.username = None
        self.password = None


# Create a session state instance
session_state = SessionState()


def login():
    if not session_state.logged_in:
        session_state.username = st.text_input("Username")
        session_state.password = st.text_input("Password", type="password")

        if st.button("Login"):
            # Your authentication logic here
            # Here, you can validate the username and password
            # For simplicity, we'll just assume any non-empty username and password are valid
            if session_state.username and session_state.password:
                session_state.logged_in = True
                st.success("Login successful!")
            else:
                st.error("Invalid username or password")


def main():
    login()

    if session_state.logged_in:
        page = st.sidebar.selectbox(
            "Explore or Predict", ("Predict", "Explore"))

        if page == "Predict":
            show_predict_page()
        else:
            show_explore_page()


if __name__ == "__main__":
    main()

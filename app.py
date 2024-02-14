import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

# Define a class to hold session state


class SessionState:
    def __init__(self):
        self.username = None
        self.password = None


# Create a session state instance
session_state = SessionState()


def login():
    if session_state.username is None:
        session_state.username = st.text_input("Username")
        session_state.password = st.text_input("Password", type="password")

        if st.button("Login"):
            # Your authentication logic here
            # Here, you can store the username and password in a database or some secure storage
            # For simplicity, we'll just print them out
            st.success("Login successful! Username: {}, Password: {}".format(
                session_state.username, session_state.password))
    else:
        st.sidebar.write("Logged in as:", session_state.username)
        if st.sidebar.button("Log out"):
            # Clear session state upon logout
            session_state.username = None
            session_state.password = None
            st.success("Logged out successfully!")


def main():
    login()

    if session_state.username is not None:
        page = st.sidebar.selectbox(
            "Explore or Predict", ("Predict", "Explore"))

        if page == "Predict":
            show_predict_page()
        else:
            show_explore_page()


if __name__ == "__main__":
    main()

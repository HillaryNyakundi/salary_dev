import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from login import login  # Importing the login functionality

# Define a session state class


class SessionState:
    def __init__(self):
        self.logged_in = False
        self.username = None
        self.password = None


# Create a session state instance
session_state = SessionState()


def main():
    if session_state.logged_in:
        st.write("Logged in as:", session_state.username)
        page = st.sidebar.selectbox(
            "Explore or Predict", ("Predict", "Explore"))

        if page == "Predict":
            show_predict_page()
        else:
            show_explore_page()
    else:
        login()  # Display the login page if not logged in


if __name__ == "__main__":
    main()

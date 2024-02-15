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


def main():
    if session_state.logged_in:
        page = st.sidebar.selectbox(
            "Explore or Predict", ("Predict", "Explore"))

        if page == "Predict":
            show_predict_page()
        else:
            show_explore_page()
    else:
        st.write("You are not logged in.")
        st.write("Please log in to access the application.")


if __name__ == "__main__":
    main()

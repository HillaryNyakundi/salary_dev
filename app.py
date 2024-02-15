import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page
from login import login  # Importing the login functionality
from session import session_state  # Importing session_state from session.py


def logout():
    session_state.logged_in = False
    session_state.username = None
    session_state.password = None
    st.success("Logged out successfully!")


def main():
    if session_state.logged_in:
        st.write("Logged in as:", session_state.username)
        page = st.sidebar.selectbox(
            "Explore or Predict", ("Predict", "Explore", "Logout"))

        if page == "Predict":
            show_predict_page()
        elif page == "Explore":
            show_explore_page()
        elif page == "Logout":
            logout()
    else:
        login(session_state)  # Display the login page if not logged in
        if session_state.logged_in:
            st.experimental_rerun()  # Refresh the UI if user logs in


if __name__ == "__main__":
    main()

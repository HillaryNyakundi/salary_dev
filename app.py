import streamlit as st
from predict_page import show_predict_page
from explore_page import show_explore_page

def login():
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    if st.sidebar.button("Login"):
        # Your authentication logic here
        if username == "your_username" and password == "your_password":
            st.success("Login successful!")
            return True
        else:
            st.error("Invalid username or password")
            return False

def main():
    if login():
        page = st.sidebar.selectbox("Explore or Predict", ("Predict", "Explore"))

        if page == "Predict":
            show_predict_page()
        else:
            show_explore_page()

if __name__ == "__main__":
    main()


import streamlit as st
import requests
import os # Import the 'os' module

st.title("Streamlit Frontend 🎈")

# Get the backend URL from an environment variable set in Render.
# The default "http://backend:8000" is for local Docker Compose development.
BACKEND_URL = os.environ.get("BACKEND_URL", "http://backend:8000")

st.header("Get a Personalized Greeting")

# Text input for the user's name
user_name = st.text_input("Enter your name")

# Create a button that calls the greet function
if st.button("Greet Me!"):
    if user_name:
        try:
            # Make a request to the new /greet endpoint with the name as a parameter
            params = {"name": user_name}
            response = requests.get(f"{BACKEND_URL}/greet", params=params)
            response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

            data = response.json()
            st.success(f"🎉 {data['greeting']}")

        except requests.exceptions.RequestException as e:
            st.error(f"Failed to get greeting from backend: {e}")
            st.info(f"Backend URL used: {BACKEND_URL}") # Helpful for debugging
    else:
        st.warning("Please enter a name first.")
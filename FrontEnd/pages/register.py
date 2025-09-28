import streamlit as st
import requests

st.title("📝 Register for Event")

# Ensure this matches your running API port
FASTAPI_BASE_URL = "http://127.0.0.1:8001" 

name = st.text_input("Enter your name")
email = st.text_input("Enter your email")
event_id = st.number_input("Event ID", min_value=1, step=1, value=1)

if st.button("Register"):
    payload = {"name": name, "email": email, "event_id": event_id}
    
    try:
        res = requests.post(f"{FASTAPI_BASE_URL}/participants/register", json=payload)

        if res.status_code == 200:
            st.success("✅ Registered successfully!")
        else:
            error_message = res.json().get('detail', 'An unknown error occurred during registration.')
            st.error(f"Error: {error_message}")
            
    except requests.exceptions.ConnectionError:
        st.error("Failed to connect to the backend API. Check if FastAPI is running on port 8001.")
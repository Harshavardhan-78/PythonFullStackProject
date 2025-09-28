import streamlit as st
import requests

st.title("📅 Event List")

# Ensure this matches your running API port
FASTAPI_BASE_URL = "http://127.0.0.1:8000" 

try:
    res = requests.get(f"{FASTAPI_BASE_URL}/events/")
    events = res.json().get("events", [])
except requests.exceptions.ConnectionError:
    st.error("Failed to connect to the backend API. Please ensure FastAPI is running on port 8000.")
    events = []

if events:
    for event in events:
        st.success(f"ID: {event.get('id')} | {event['name']} 📍 {event['venue']} 🗓 {event['date']}")
else:
    st.warning("No events available.")
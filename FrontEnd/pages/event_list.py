import streamlit as st
import requests

st.title("📅 Event List")

# ✅ Make sure this matches your backend port
FASTAPI_BASE_URL = "http://127.0.0.1:8000"

try:
    res = requests.get(f"{FASTAPI_BASE_URL}/events/")

    if res.status_code == 200:
        try:
            data = res.json()
            events = data.get("events", [])
        except ValueError:
            st.error("⚠️ Backend response is not valid JSON.")
            events = []
    else:
        st.error(f"⚠️ Backend returned status code {res.status_code}")
        events = []

except requests.exceptions.ConnectionError:
    st.error("🚫 Cannot connect to backend. Make sure FastAPI is running on port 8000.")
    events = []

# ✅ Display events neatly
if events:
    st.subheader("Available Events")
    for event in events:
        st.success(f"🆔 {event.get('id')} — **{event.get('name')}** 📍 {event.get('venue')} 🗓 {event.get('date')}")
else:
    st.info("No events available or failed to fetch.")

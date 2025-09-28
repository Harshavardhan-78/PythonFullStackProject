import streamlit as st
import requests

st.title("📊 Event Reports")
st.markdown("---")

# Assuming the backend is running on port 8001
FASTAPI_BASE_URL = "http://127.0.0.1:8001"

try:
    res = requests.get(f"{FASTAPI_BASE_URL}/events/reports")
    reports = res.json().get("reports", [])
except requests.exceptions.ConnectionError:
    st.error("Failed to connect to the backend API. Please ensure FastAPI is running.")
    reports = []

if reports:
    for report in reports:
        event_name = report.get("name")
        event_venue = report.get("venue")
        event_date = report.get("date")
        participants = report.get("participants", [])

        st.subheader(f"📅 {event_name}")
        st.markdown(f"**Venue:** {event_venue} | **Date:** {event_date}")
        
        if participants:
            st.markdown(f"**Participants ({len(participants)}):**")
            participant_names = [p.get('name') for p in participants]
            st.markdown(", ".join(participant_names))
        else:
            st.markdown("**No participants registered yet.**")
            
        st.markdown("---")
else:
    st.warning("No events or reports available.")

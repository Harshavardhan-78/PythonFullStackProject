import streamlit as st
import requests
import datetime

st.title("➕ Create New Event (Public Access)")
st.info("Note: This endpoint uses a default Organizer ID for simplicity.")

# Assuming the backend is running on port 8001
FASTAPI_BASE_URL = "http://127.0.0.1:8001"

# Input form for the new event
name = st.text_input("Event Name")
date_obj = st.date_input("Event Date", datetime.date.today()) 
venue = st.text_input("Venue")

if st.button("Submit Event"):
    if not name or not venue:
        st.error("Please fill in all event details.")
    else:
        date_str = date_obj.isoformat() 
        
        payload = {
            "name": name, 
            "date": date_str, 
            "venue": venue,
            "organizer_id": 1 # Hardcoded for this public route
        }
        
        try:
            res = requests.post(f"{FASTAPI_BASE_URL}/events/", data=payload)

            if res.status_code == 200:
                st.success("✅ Event created successfully!")
            else:
                st.error(f"Failed to create event: {res.json().get('detail', 'Unknown error')}")
        
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the backend API. Check if FastAPI is running on port 8001.")

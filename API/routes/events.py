from fastapi import APIRouter, Form
from src.Db import create_event_db, get_all_events_db, get_all_event_reports_db

router = APIRouter()

@router.get("/")
def list_events():
    events = get_all_events_db()
    return {"events": events}

@router.post("/")
def create_event(
    name: str = Form(...),
    date: str = Form(...),
    venue: str = Form(...),
    organizer_id: int = Form(1) # Hardcoded for public access
):
    event_data = create_event_db(name, date, venue, organizer_id)
    return {"message": "Event created ✅", "event": event_data}

@router.get("/reports")
def get_event_reports():
    reports = get_all_event_reports_db()
    return {"reports": reports}

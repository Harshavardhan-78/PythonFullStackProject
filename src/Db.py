from supabase import create_client
from fastapi import HTTPException
from pydantic import BaseModel
from typing import List
from src.Logic import get_settings

# --- Client Initialization ---
settings = get_settings()
supabase = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)

# --- Data Models ---
class Participant(BaseModel):
    name: str
    email: str
    event_id: int

# --- CRUD Operations for Events Table ---
def create_event_db(name: str, date: str, venue: str, organizer_id: int) -> dict:
    """Inserts a new event record into Supabase."""
    data = {
        "name": name,
        "date": date,
        "venue": venue,
        "organizer_id": organizer_id
    }
    try:
        res = supabase.table("events").insert(data).execute()
        return res.data[0]
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Database error creating event: {str(e)}")

def get_all_events_db() -> List[dict]:
    """Fetches all events from Supabase."""
    res = supabase.table("events").select("*").execute()
    return res.data

# --- CRUD Operations for Participants Table ---
def register_participant_db(data: Participant) -> dict:
    """Registers a new participant for an event."""
    try:
        res = supabase.table("participants").insert(data.model_dump()).execute()
        return res.data[0]
    except Exception as e:
        error_detail = str(e)
        if "duplicate key value violates unique constraint" in error_detail:
            raise HTTPException(status_code=400, detail="Registration failed: This email is already registered.")
        raise HTTPException(status_code=400, detail=f"Registration failed: {error_detail}")

def get_event_participants_db(event_id: int) -> List[dict]:
    """Fetches all participants for a specific event."""
    res = supabase.table("participants").select("*").eq("event_id", event_id).execute()
    return res.data

def get_all_event_reports_db() -> List[dict]:
    """
    Fetches all events and joins them with their participants.
    """
    res = supabase.table("events").select("*, participants(*)").execute()
    return res.data

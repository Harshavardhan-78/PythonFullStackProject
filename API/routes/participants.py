from fastapi import APIRouter
from src.Db import register_participant_db, get_event_participants_db, Participant

router = APIRouter()

@router.post("/register")
def register_participant(data: Participant):
    participant_data = register_participant_db(data)
    return {"message": "Participant registered ✅", "data": participant_data}

@router.get("/event/{event_id}")
def get_event_participants(event_id: int):
    participants = get_event_participants_db(event_id)
    return {"participants": participants}
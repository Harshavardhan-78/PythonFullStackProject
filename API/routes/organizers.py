# API/routes/organizers.py

from fastapi import APIRouter
from pydantic import BaseModel
from src.Db import login_organizer_db 

router = APIRouter()

class OrganizerLogin(BaseModel):
    email: str
    password: str

@router.post("/login")
def login_organizer(data: OrganizerLogin):
    login_data = login_organizer_db(data.email, data.password)
    return login_data
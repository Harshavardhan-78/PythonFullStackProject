from fastapi import FastAPI
from API.routes import events, participants

app = FastAPI(title="Event Organisation System API")
# Include Routers
app.include_router(events.router, prefix="/events", tags=["Events"])
app.include_router(participants.router, prefix="/participants", tags=["Participants"])

@app.get("/")
def root():
    return {"message": "Event Organisation System API is running 🚀"}

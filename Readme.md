🎟️ Event Registration System
The system enables organizers to create and manage events, while participants can register online using a simple form. All registration data is stored securely in the database. Organizers can view the participants list for each event and generate reports for administrative purposes.

## Features

    📅 Browse Events – View upcoming events with details.

    📝 Online Registration – Register quickly using a simple form.

    🚫 Prevent Duplicate Registration – Same email cannot register for the same event twice.

    ⏰ Automatic Timestamp – Track registration date and time.

    🔒 Secure Organizer Login – Create, update, or delete events safely.

    👥 View Participants – Check the list of registered participants per event.

    📊 Generate Reports – Export participant lists for records.

    🖥️ User-Friendly Interface – Easy navigation for participants and organizers.

    🔗 Relational Data – Link organizers, events, and participants.

    ⚡ Scalable System – Supports multiple events and participants efficiently.

## Project Structure

EventOrganisationSystem/
│── src/                     #core application Logic
│   ├── Db.py                # Database operations
│   └── Logic.py             # Core business logic(event,particpants)
│                   
│── API/                     #Backend
│   └── main.py              # Main API entry point
│
│── FrontEnd/                # Frontend application
│   └── app.py               # Streamlit web interface
│
│── requirements.txt         # Python dependencies
|
│── Readme.md                # Project documentation
|
│__. env                     # python Variables
 
## Quick start

### Prerequisites
- pyhton 3.8 or higher 
- A Supabase account
- Git(Push,cloning)

### 1.clone or Download the project 
# option 1: Clone with Git
git clone <repository-url>
# option 2:Download and extract the ZIP file 
### 2.Install all required python packages
pip install -r requirements.txt
### 3.Set up Supabase Database
1.create a supebase Projects:
2.create the Tasks Tables:
-Go to the Sql Editor in your Supabase dashboard
-Run this SQL Command:
```sql
        create table organizers(id int primary key,
        name text not null,email text unique not null,password text not null,  created_at timestamp default now());

        create table events (
        id serial primary key,      
        name text not null,
        date date not null,
        venue text not null,
        organizer_id int references organizers(id) on delete cascade,
        created_at timestamp default now()
        );

        create table participants(id serial primary key,name text not null,email text unique not null,  event_id int references events(id) on delete cascade , registered_at timestamp default now());
```
3. Get Your Credentials:
### 4. configure Environment Variables
1.create a `.env` file in the project root
2.Add your Supabase Credentials to `.env`fil;

EX:
SUPABASE_URL=your_project_url_here
SUPABASE_KEY=your_annon_key_here
### Run the Application

## Streamlit Frontend
streamlit run frontend/app.py

The app will open in your browser at`https://localhost:8501`

## FastAPI Backkend

cd api
python main.py

The API will be available at `https://localhost:8000`

## How to use

# For Event Organizers

Create a new event by entering the event name, date, and venue.

Manage events: update or delete events if needed.

View participants for your events.

Generate reports: export participant lists for administrative purposes.

# For Participants
Open the app and browse available events.

Select an event and fill in your name and email to register.

The system automatically records your registration date and time.

You will see a confirmation of successful registration.

Same email cannot register twice for the same event.

## Technical Details
### Technologies Used

_** Frontend**
    🖥️ Streamlit – Build interactive web forms for event registration and participant view.

    🌐 HTML/CSS (optional) – Customize the layout and styling of the interface.


_** Backend**
    🐍 Python – Core programming language for the application logic.

    🗄️ Supabase (PostgreSQL) – Database for storing organizers, events, and participants.

    🌿 python-dotenv – Manage environment variables like Supabase URL and API keys.

_** API / Server**
    ⚡ FastAPI – RESTful API to handle requests from frontend, manage events, and participants.

    🚀 Uvicorn – ASGI server to run the FastAPI application
### Key Comonenets
1.`src/Db.py`:Database operations
    -handles all CRUD operation
2.`src/Logic.py`:Business logic 
    -Task validation and processing

## Troubleshooting

### Error 1: `PydanticImportError: BaseSettings has been moved`
- **Cause:** In `pydantic v2`, `BaseSettings` is no longer available directly in `pydantic`. It has been moved to a separate package: [`pydantic-settings`](https://docs.pydantic.dev/2.11/migration/#basesettings-has-moved-to-pydantic-settings).
- **Fix:**
  1. Install the missing package:
     ```bash
     pip install pydantic-settings
     ```
  2. Update imports in your code:
     ```python
     # ❌ Old
     from pydantic import BaseSettings

     # ✅ New
     from pydantic_settings import BaseSettings
     ```

---

### Error 2: `Test FAILED: name 'login_organizer_db' is not defined`
- **Cause:** The function could not be imported because of a Python module path issue. Running from the interactive shell doesn’t recognize `src/` as a module.
- **Fix:**
  1. Create a test script in your project root (e.g. `test_login.py`):
     ```python
     from src.database import login_organizer_db

     print(login_organizer_db("your_email", "your_password"))
     ```
  2. Run it:
     ```bash
     python test_login.py
     ```
  This ensures imports work correctly since the project root is on the module path.



## Common Issues

- **Untracked files showing in `git status`:**
  - If you see `../venv/` or `../errors.txt`, it means files outside your repo folder are being picked up.
  - Add them to `.gitignore`:
    ```gitignore
    venv/
    errors.txt
    ```

- **FastAPI not auto-reloading changes:**
  - Make sure you run the server with:
    ```bash
    uvicorn API.Main:app --reload
    ```

- **Invalid credentials when logging in:**
  - Check if your test user is correctly inserted in Supabase.
  - Ensure email/password match exactly with what’s stored.

## Future Enhancements
1.Email Notifications 📧

Send confirmation emails to participants upon registration.

Notify organizers when new participants register.

2.Organizer Authentication & Roles 🔒

Implement multi-level access (admin, organizer).

Two-factor authentication for enhanced security.

3.Payment Integration 💳

Allow paid events with online payment gateways.

Track payments for participants.

4.Event Categories & Filters 🗂️

Categorize events by type (workshop, seminar, hackathon).

Enable participants to filter events based on date, category, or location.

5.Dashboard & Analytics 📊

Show event statistics like total participants, registrations over time, popular events.

Visual charts and graphs for organizers.

6.Mobile App Version 📱

Develop a mobile-friendly version for easier access on smartphones.

## Support

If you encounter any issues or have Questions:
email:`123ter@gmail.com`
phone:`8008581292`
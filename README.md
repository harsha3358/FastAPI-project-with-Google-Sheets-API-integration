# FastAPI Google Sheets User Authentication System

## Overview

This project is a lightweight user management and authentication backend built using FastAPI and Google Sheets as a serverless datastore.

It demonstrates:

- REST API development using FastAPI
- Secure password hashing using bcrypt
- Google Sheets API integration via service account authentication
- Cloud-based persistent storage without a traditional database
- Clean separation of backend logic and frontend interface
- Production-style project structure

This project is suitable for learning modern backend architecture, cloud integrations, and API development.

---

## Architecture

Client (Browser UI)  
→ FastAPI Backend  
→ Google Sheets API  
→ Google Sheets (Cloud Data Store)

The system uses Google Sheets as a lightweight database for storing user records.

---

## Features

- User registration endpoint
- Password hashing using bcrypt
- Automatic timestamp generation
- Fetch and display all users
- Google Sheets integration using service account
- Graceful error handling
- Clean modular structure

---

## Tech Stack

Backend:
- FastAPI
- Pydantic
- bcrypt
- Uvicorn

Cloud Integration:
- Google Sheets API
- Google Service Account Authentication

Frontend:
- HTML
- Vanilla JavaScript (Fetch API)

---

## Project Structure

```
google_sheets_api/
│
├── main.py
├── models.py
├── sheets_service.py
├── requirements.txt
├── credentials.json
└── templates/
      └── index.html
```

---

## Google Sheet Structure

Your Google Sheet must contain the following columns:

email | password | role | created_at

The first row should contain headers.

---

## Setup Instructions

### 1. Clone the Repository

```
git clone https://github.com/your-username/fastapi-google-sheets-user-auth.git
cd fastapi-google-sheets-user-auth
```

### 2. Create Virtual Environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Configure Google Sheets

- Create a Google Cloud project
- Enable Google Sheets API
- Create a Service Account
- Download the credentials JSON file
- Rename it to `credentials.json`
- Place it in the project root
- Share your Google Sheet with the service account email (Editor access)

### 5. Add Spreadsheet ID

In `sheets_service.py`, replace:

```
SPREADSHEET_ID = "PASTE_YOUR_SHEET_ID"
```

with your actual Google Sheet ID.

---

## Running the Application

Start the server:

```
uvicorn main:app --reload
```

Open in browser:

```
http://127.0.0.1:8000
```

---

## API Endpoints

GET `/`  
Serves the frontend interface.

GET `/users`  
Returns all registered users (excluding header row).

POST `/register`  
Registers a new user.

Example request body:

```
{
  "email": "user@example.com",
  "password": "securepassword",
  "role": "user"
}
```

---

## Security Considerations

- Passwords are hashed using bcrypt before storage.
- Service account credentials should never be committed to public repositories.
- For production use, SSL verification should not be disabled.
- Environment variables should be used for sensitive configuration.

---

## Learning Outcomes

This project demonstrates:

- RESTful API design
- Authentication fundamentals
- Cloud API integration
- Serverless data storage concepts
- Backend error handling
- Separation of concerns

---

## License

This project is intended for educational and demonstration purposes.

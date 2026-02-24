from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from models import User
import bcrypt
import json
from datetime import datetime
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

DB_FILE = "users.json"

# Ensure users.json exists
if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump([], f)

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/users")
def get_users():
    with open(DB_FILE, "r") as f:
        data = json.load(f)
    return {"data": data}

@app.post("/register")
def register(user: User):
    with open(DB_FILE, "r") as f:
        users = json.load(f)

    hashed = bcrypt.hashpw(
        user.password.encode(),
        bcrypt.gensalt()
    ).decode()

    new_user = {
        "email": user.email,
        "password": hashed,
        "role": user.role,
        "created_at": str(datetime.now())
    }

    users.append(new_user)

    with open(DB_FILE, "w") as f:
        json.dump(users, f, indent=4)

    return {"message": "🚀 User Registered Successfully!"}
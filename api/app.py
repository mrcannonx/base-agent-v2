from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from typing import Optional, List
import uuid

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class User(BaseModel):
    id: str
    username: str
    email: str
    disabled: bool = False

class UserCreate(BaseModel):
    username: str
    email: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str

# Mock database
users_db = {}

# Authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Utility endpoints
@app.get("/")
async def root():
    return {"message": "Hello from FastAPI backend"}

@app.get("/api/health")
async def health_check():
    return {"status": "healthy"}

# Authentication endpoints
@app.post("/api/auth/register", response_model=User)
async def register(user: UserCreate):
    if user.username in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already registered"
        )
    user_id = str(uuid.uuid4())
    db_user = User(
        id=user_id,
        username=user.username,
        email=user.email,
        disabled=False
    )
    users_db[user.username] = db_user
    return db_user

@app.post("/api/auth/login", response_model=Token)
async def login(username: str, password: str):
    user = users_db.get(username)
    if not user or password != "password":  # In real app, use proper password hashing
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password"
        )
    return {"access_token": str(uuid.uuid4()), "token_type": "bearer"}

# User endpoints
@app.get("/api/users", response_model=List[User])
async def get_users():
    return list(users_db.values())

@app.get("/api/users/{user_id}", response_model=User)
async def get_user(user_id: str):
    for user in users_db.values():
        if user.id == user_id:
            return user
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User not found"
    )

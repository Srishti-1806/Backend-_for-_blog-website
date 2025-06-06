from fastapi import APIRouter, Depends, HTTPException, response_model
from sqlalchemy.orm import Session
from . import models, schemas
from .database import get_db
from passlib.context import crypt_context   # Importing crypt_context for password hashing
router = APIRouter()

pwd_context = crypt_context(schemes=["bcrypt"], deprecated="auto") # Password hashing context

@router.post("/login")
def login(user_credentials: schemas.User, db:Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == user_credentials.email).first()
    if not user:
      raise HTTPException(status_code=404, detail= "User not found")
    if not verify_password(user_credentials.password, user.password):
    raise HTTPException(status_code=403, detail="Invalid credentials")
  return {"message": "Login successful", "user": user}

    

def verify_password(plain_password, hashed_password):
  return pwd_password.verify(plain_password, hashed_password)
  
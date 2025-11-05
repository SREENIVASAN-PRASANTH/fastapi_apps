# auth/google_auth.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from google.oauth2 import id_token
from google.auth.transport import requests
from auth.jwt_handler import create_access_token
import models
from database import get_db
import os
from dotenv import load_dotenv
load_dotenv()

router = APIRouter(prefix="/google", tags=["Google Auth"])

GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")

@router.post("/signin")
def google_signin(token: str, db: Session = Depends(get_db)):
    try:
        idinfo = id_token.verify_oauth2_token(token, requests.Request(), GOOGLE_CLIENT_ID)
        email = idinfo["email"]
        name = idinfo.get("name", email.split("@")[0])

        user = db.query(models.User).filter(models.User.email == email).first()
        if not user:
            user = models.User(username=name, email=email, provider="google")
            db.add(user)
            db.commit()
            db.refresh(user)

        access_token = create_access_token({"sub": email})
        return {"access_token": access_token, "token_type": "bearer"}
    except Exception:
        raise HTTPException(status_code=400, detail="Invalid Google token")

# main.py
from fastapi import FastAPI
from database import Base, engine
import models
from auth import routes as auth_routes
from auth import google_auth as google_routes

app = FastAPI(title="Blog App Backend - Auth Module")

models.Base.metadata.create_all(bind=engine)

app.include_router(auth_routes.router)
app.include_router(google_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to the Blog App Backend!"}

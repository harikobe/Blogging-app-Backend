from fastapi import FastAPI,Depends
from typing import Annotated
from .routers import crud
from fastapi.security import HTTPBasic,HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()

app.include_router(crud.router)

@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}
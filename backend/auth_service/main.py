# main.py for fastapi entry point

from fastapi import FastAPI, Depends, HTTPException
from .authenticate import Authenticator
from .validator import Validator

app = FastAPI()

authenticator = Authenticator()
validator = Validator()

@app.post("/login")
def login(username: str, password: str):
    """Process user login attemps.  
    inputs: username, password
    returns: access_token"""
    if not validator.validate_credentials(username, password):
        raise HTTPException(status_code=400, detail="Invalid credentials")

    token = authenticator.generate_token(username)
    return {"access_token": token, "token_type": "bearer"}



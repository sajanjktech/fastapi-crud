"""
This file helps in authentication of user 
the user provides username and password and if both are correct then access token is sent to the user
this file is made with the help of fastapi official docs 
https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#update-the-token-path-operation

"""


from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
from typing import Annotated
from datetime import datetime, timedelta, timezone
from jose import JWTError,jwt
import os
from dotenv import load_dotenv
from app.models.auth import UserInDb,Token
from app.db.db import fake_users_db


load_dotenv()

# JWT configuration
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES","30"))

# Password hashing context
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# OAuth2 scheme for token extraction
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# Create a router instance
router = APIRouter()

def verify_password(plain: str, hashed: str) -> bool:
    """
    Verifies a plain-text password against a hashed password.
    """
    return pwd_context.verify(plain, hashed)

def get_user(db,username):
    if username in db:
        userdict = db[username]
        return UserInDb(**userdict)

def authenticate_user(db,username: str, password: str):
    """
    Authenticates a user by username and password.

    """
    user = get_user(db,username)
    if not user :
        return False
    if not verify_password(password, user.hashed_password):
        return False
    return user

def create_access_token(data: dict, expires_delta: timedelta|None = None) -> str:
    """

    Creates a JWT token

    """
    to_encode = data.copy() 
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    print(ALGORITHM)
    encoded_jwt = jwt.encode(to_encode,SECRET_KEY,algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str = Depends(oauth2_scheme)) -> str:
    """
    Verify JWT token and extract the username (subject).

    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("sub")
        if username is None:
            raise HTTPException(status_code = 401,detail = "Invalid token")
        return username
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

@router.post("/token", summary="User login and JWT generation", tags=["Authentication"])
def login(form_data:Annotated[OAuth2PasswordRequestForm,Depends()])->Token:
    """
    Authenticates user credentials and returns a JWT access token.
    Raises:
    - HTTP 401 if authentication fails
    """
    user = authenticate_user(fake_users_db,form_data.username, form_data.password)

    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username},
        expires_delta=access_token_expires
    )
    return Token(access_token= access_token,token_type="bearer")

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from passlib.context import CryptContext
from datetime import datetime, timedelta
from jose import JWTError, jwt

# Simulated user database with hashed passwords
fake_users_db = {
    "sajan": {
        "username": "sajan",
        "hashed_password": "$2b$12$xAeFfCFB1cowY23slrkfBOIXUPrlbG7vK52UK3eHXVLO1wkfXvv5y",  # password: secret
    },
    "sajal": {
        "username": "sajal",
        "hashed_password": "$2b$12$mtczYF3NJERTEsSD8dCeieZExDqiNkwaijFJ9C0UM1BH0uBcmPZsa",  # password: secret1
    }
}

# JWT configuration
SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

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

def authenticate_user(username: str, password: str):
    """
    Authenticates a user by username and password.

    Returns the user dictionary if authentication is successful, otherwise False.
    """
    user = fake_users_db.get(username)
    if not user :
        return False
    if not verify_password(password, user["hashed_password"]):
        return False
    return user

def create_token(data: dict, expires_delta: timedelta = None) -> str:
    """
    Creates a JWT token with optional expiration time.

    Parameters:
    - data (dict): Data to encode in the token
    - expires_delta (timedelta, optional): Token validity duration

    Returns:
    - Encoded JWT token as a string
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/token", summary="User login and JWT generation", tags=["Authentication"])
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    Authenticates user credentials and returns a JWT access token.

    Request Body:
    - username: User's login name
    - password: User's password

    Response:
    - access_token: JWT access token
    - token_type: Type of token (bearer)

    Raises:
    - HTTP 401 if authentication fails
    """
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Incorrect username or password")
    token = create_token(data={"sub": user["username"]})
    return {"access_token": token, "token_type": "bearer"}

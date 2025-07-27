from datetime import datetime, timedelta, timezone
import jwt
import os
from fastapi.security import OAuth2PasswordBearer
import bcrypt

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 30

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login")


def get_password_hash(password):
    pwhash = bcrypt.hashpw(password.encode('utf8'), bcrypt.gensalt())
    return pwhash.decode('utf8') 

def verify_password(plain_password, hashed_password):
     return bcrypt.checkpw(
        bytes(plain_password, encoding="utf-8"),
        bytes(hashed_password, encoding="utf-8"),
    )

def decode_jwt(token: str):
    try:
        decoded_token = jwt.decode(token, os.getenv("TOKEN_SECRET_KEY"), algorithms=[ALGORITHM])
        isValid = decoded_token["exp"] >= datetime.now(timezone.utc).timestamp()
        return decoded_token if isValid else None
    except Exception as e:
        return {}

def create_access_token(data: dict):
    to_encode = data.copy()
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now(timezone.utc) + access_token_expires
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv('TOKEN_SECRET_KEY'), algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict):
    to_encode = data.copy()
    refresh_token_expires = timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    expire = datetime.now(timezone.utc) + refresh_token_expires
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, os.getenv('REFRESH_TOKEN_SECRET_KEY'), algorithm=ALGORITHM)
    return encoded_jwt

def verify_jwt(jwtoken: str) -> bool:
        isTokenValid: bool = False
        try:
            payload = decode_jwt(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True

        return isTokenValid
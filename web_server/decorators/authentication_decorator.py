import os
from functools import wraps
from fastapi import HTTPException, Request
from jose import JWTError
import jwt

secret_key = os.environ.get("SECRET_KEY")
hashing_algorithm = os.environ.get("HASHING_ALGORITHM")

def decode_token(token: str):
    try:
        payload = jwt.decode(jwt=token, key=secret_key, algorithms=[hashing_algorithm])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def protected(func):
    @wraps(func)
    async def wrapper(*args, **kwargs):
        request: Request = kwargs.get("request") or args[0]
        token = request.headers.get("Authorization")
        if not token or not token.startswith("Bearer "):
            raise HTTPException(status_code=401, detail="Unauthorized access")
        token = token[len("Bearer "):]  # Remove "Bearer " prefix
        decode_token(token)  # Validate the token
        return await func(*args, **kwargs)
    return wrapper

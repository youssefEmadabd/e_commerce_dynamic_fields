import os, hashlib
from dotenv import load_dotenv
import jwt

load_dotenv()


secret_key = os.environ.get("SECRET_KEY")
hashing_algorithm = os.environ.get("HASHING_ALGORITHM")
print(secret_key)

def hash_password(password: str) -> str:
    """
    Hash the password using HS256
    """
    return hashlib.sha256(password.encode()).hexdigest()

def is_valid_password(hashed_password: str, plain_password: str) -> bool:
    """
    Verify hash
    """
    return hashed_password == hash_password(plain_password)

def create_access_token(data: dict) -> str:
    """
    Create JWT token.
    """
    print(data, secret_key, hashing_algorithm)
    return jwt.encode(payload=data, key=secret_key, algorithm=hashing_algorithm)

def validate_fields(data: dict, fields: list) -> bool:
    """
    Validate fields
    """
    return all(key in fields for key in data.keys())
import jwt
from dotenv import load_dotenv
import os
import time

try:
    load_dotenv("./.env")
except:
    pass

JWT_KEY = os.getenv("JWT_KEY")

def create_login_token() -> str:
    return jwt.encode(
        payload={
            "exp": time.time() + 7 * 24 * 60 * 60
        },
        key=JWT_KEY,
        algorithm="HS256"
    )

def is_token_valid(token: str) -> bool:
    try:
        jwt.decode(jwt=token, key=JWT_KEY, algorithms=["HS256"])
        return True
    except:
        return False

from hashlib import sha512
from dotenv import load_dotenv
import os

try:
    load_dotenv("./.env")
except:
    pass

SALT = os.getenv("HASH_SALT")
INITAL_PASSWORD = os.getenv("INITAL_PASSWORD")

def hash_func(password: str) -> bytes:
    return sha512((password + SALT).encode()).digest()

try:
    with open("./admin_password.bin", "xb") as file:
        file.write(hash_func(INITAL_PASSWORD))
except:
    pass
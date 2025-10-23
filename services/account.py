from fastapi import Request, HTTPException, Depends
from utils.crypto_macro import hash_func
from utils.tokener import is_token_valid

def get_current_password() -> bytes:
    with open("./admin_password.bin", "rb") as file:
        password = file.read()
    return password

def is_login_able(password: str) -> bool:
    if hash_func(password) == get_current_password(): return True
    return False

def check_login(request: Request) -> bool:
    login_token = request.cookies.get("login_token")
    if login_token is None:
        return False

    if is_token_valid(login_token):
        return True
    return False

def set_password(newpassword: str) -> None:
    with open("./admin_password.bin", "wb") as file:
        file.write(hash_func(newpassword))
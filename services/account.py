from utils.crypto_macro import hash_func

def get_current_password() -> bytes:
    with open("./admin_password.bin", "rb") as file:
        password = file.read()
    return password

def is_login_able(password: str) -> bool:
    if hash_func(password) == get_current_password(): return True
    return False

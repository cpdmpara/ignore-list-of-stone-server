from fastapi import APIRouter, Response, Depends
from services.account import is_login_able, check_login, set_password
from utils.tokener import create_login_token

router = APIRouter(prefix="/account", tags=["account"])

@router.get("")
def login_router(password: str):
    if is_login_able(password):
        response = Response()
        login_token = create_login_token()

        response.set_cookie(
            key = "login_token", 
            value = login_token, 
            max_age = 7 * 24 * 60 * 60,
            httponly=True,
            secure=False # 배포시 변경
        )
        
        return response

    return Response(status_code=401)

@router.get("/logout")
def logout_router():
    response = Response()
    response.delete_cookie("login_token")
    
    return response

@router.put("/password")
def change_password_router(newpassword: str, logined: bool=Depends(check_login)):
    if not logined:
        return Response(status_code=401)
    
    set_password(newpassword)

    return Response(status_code=200)
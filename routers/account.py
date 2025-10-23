from fastapi import APIRouter, Response
from services.account import is_login_able
from utils.tokener import create_login_token

router = APIRouter(prefix="/account", tags=["account"])

@router.get("")
def login_router(password: str):
    if is_login_able(password):
        response = Response()
        login_token = create_login_token()

        response.set_cookie("login_token", login_token, max_age = 7 * 24 * 60 * 60)
        
        return response

    return Response(status_code=401)
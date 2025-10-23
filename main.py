from fastapi import FastAPI
from routers import account

server = FastAPI()

server.include_router(account.router)
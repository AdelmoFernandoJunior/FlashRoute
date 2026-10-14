from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")

app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(order_router, prefix="/orders", tags=["orders"])



# & ".\.venv\Scripts\python.exe" -m uvicorn main:app --reload



# Rest APIs
# Get -> leitura/pegar
# Post -> enviar/criar
# Put -> atualizar
# Patch -> atualizar parcialmente
# Delete -> deletar
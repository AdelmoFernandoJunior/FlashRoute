from fastapi import FastAPI
from passlib.context import CryptContext
from dotenv import load_dotenv
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))
REFRESH_TOKEN_EXPIRE_MINUTES = int(os.getenv("REFRESH_TOKEN_EXPIRE_MINUTES"))


app = FastAPI()

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from auth_routes import auth_router
from order_routes import order_router

app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(order_router, prefix="/orders", tags=["orders"])



# ./.venv/Scripts/python.exe -m uvicorn main:app --reload



# Rest APIs
# Get -> leitura/pegar
# Post -> enviar/criar
# Put -> atualizar
# Patch -> atualizar parcialmente
# Delete -> deletar

# GET	    Consultar dados	                            GET /simulacoes/123
# POST	    Criar um recurso ou iniciar uma operação	POST /simulacoes
# PUT	    Substituir integralmente um recurso     	PUT /simulacoes/123
# PATCH	    Atualizar parcialmente um recurso	        PATCH /simulacoes/123
# DELETE	Excluir um recurso	                        DELETE /simulacoes/123
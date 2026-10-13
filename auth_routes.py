from fastapi import APIRouter

auth_router = APIRouter()

@auth_router.get("/")
async def autenticar():
    
    return {"message": "Você está na rota de autenticação!"}




from fastapi import APIRouter, Depends, HTTPException
from dependecies import pegar_sessao
from models import Usuario
from main import bcrypt_context

auth_router = APIRouter()

@auth_router.get("/")
async def autenticar():
    
    return {"message": "Você está na rota de autenticação!"}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter_by(email=email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    else:
        senha_criptografada = bcrypt_context.hash(senha)
        novo_usuario = Usuario(nome=nome, email=email, senha=senha_criptografada)
        session.add(novo_usuario)
        session.commit()
        return {"message": "Conta criada com sucesso!"}

    

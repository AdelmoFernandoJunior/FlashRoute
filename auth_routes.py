from fastapi import APIRouter, Depends
from dependecies import pegar_sessao
from models import Usuario

auth_router = APIRouter()

@auth_router.get("/")
async def autenticar():
    
    return {"message": "Você está na rota de autenticação!"}

@auth_router.post("/criar_conta")
async def criar_conta(email: str, senha: str, nome: str, session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter_by(email=email).first()
    if usuario:
        return {"message": "Email já cadastrado!"}
    else:
        novo_usuario = Usuario(nome=nome, email=email, senha=senha)
        session.add(novo_usuario)
        session.commit()
        return {"message": "Conta criada com sucesso!"}

    

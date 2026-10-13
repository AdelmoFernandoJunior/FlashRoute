from fastapi import APIRouter, Depends, HTTPException
from dependecies import pegar_sessao
from models import Usuario
from main import bcrypt_context
from schemas import UsuarioSchema
from sqlalchemy.orm import Session

auth_router = APIRouter()

@auth_router.get("/")
async def autenticar():
    
    return {"message": "Você está na rota de autenticação!"}

@auth_router.post("/criar_conta")
async def criar_conta(usuario_schema: UsuarioSchema, session = Depends(pegar_sessao)):

    usuario = session.query(Usuario).filter_by(email=usuario_schema.email).first()
    if usuario:
        raise HTTPException(status_code=400, detail="Email já cadastrado.")
    else:
        senha_criptografada = bcrypt_context.hash(usuario_schema.senha)
        novo_usuario = Usuario(usuario_schema.nome, usuario_schema.email, senha_criptografada, usuario_schema.ativo, usuario_schema.admin)
        session.add(novo_usuario)
        session.commit()
        return {"message": f"Conta criada com sucesso!{usuario_schema.email}"}

    

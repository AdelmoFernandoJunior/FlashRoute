from fastapi import APIRouter, Depends, HTTPException
from dependecies import pegar_sessao
from models import Usuario
from main import bcrypt_context
from schemas import UsuarioSchema, LoginSchema
from sqlalchemy.orm import Session

auth_router = APIRouter()

# Função para criar token (exemplo simples, você pode usar JWT ou outra abordagem)
def criar_token(usuario_id: int):
    return f"token_para_{usuario_id}"

# Função para autenticar usuário
def autenticar_usuario(email: str, senha: str, session: Session):
    usuario = session.query(Usuario).filter_by(email=email).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciais inválidas.")
    elif not bcrypt_context.verify(senha, usuario.senha):
        return False
    
    return usuario

# Rota de autenticação (GET) 
@auth_router.get("/")
async def autenticar():
    
    return {"message": "Você está na rota de autenticação!"}

# Rota de criação de conta (POST)
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

# Rota de login (POST)
@auth_router.post("/login")
async def login(Login_schema: LoginSchema, session = Depends(pegar_sessao)):
    usuario = autenticar_usuario(Login_schema.email, Login_schema.senha, session)
    if not usuario:
        raise HTTPException(status_code=401, detail="Usuario não encontrado ou credenciais inválidas.")
    return {
        "access_token": criar_token(usuario.id),
        "token_type": "bearer"
    }

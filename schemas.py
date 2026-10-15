from pydantic import BaseModel, EmailStr
from typing import Optional

# Essa classe serve para validação de dados de entrada
class UsuarioSchema(BaseModel):
   
    nome: str
    email: EmailStr
    senha: str
    ativo: Optional[bool] = True
    admin: Optional[bool] = False

    class Config:
        from_attributes = True

# Essa classe serve para validação de dados de entrada para pedidos
class PedidoSchema(BaseModel):
    usuario: int

    class Config:
        from_attributes = True

# Essa classe serve para validação de dados de entrada para login
class LoginSchema(BaseModel):
    email: EmailStr
    senha: str

    class Config:
        from_attributes = True
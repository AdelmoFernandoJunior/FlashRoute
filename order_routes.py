from fastapi import APIRouter, Depends
from dependecies import pegar_sessao
from schemas import PedidoSchema
from sqlalchemy.orm import Session
from models import Pedido

order_router = APIRouter()

@order_router.get("/")
async def pedidos():
    """
    Rota padrão de pedidos do nosso sistema.
    """
    return {"message": "Você está na rota de pedidos!"}

@order_router.post("/pedidos")
async def criar_pedido(pedido_schema: PedidoSchema, session = Depends(pegar_sessao)):
    novo_pedido = Pedido(usuario=pedido_schema.usuario_id)
    session.add(novo_pedido)
    session.commit()
    return {"message": f"Pedido criado com sucesso. ID do pedido: {novo_pedido.id}"}